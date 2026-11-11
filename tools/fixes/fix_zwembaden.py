#!/usr/bin/env python3
"""Proposal Zwembaden (Michiel Verhoef, VNG, november 2026) op orde brengen in de EA-repository van het
GGM (.qea = SQLite), volgens het advies van 11 november 2026 en de keuzes van Arjen:

  1. De klassen Gebruik, Gebruikstype, Rooster, Activiteit en Afnemer komen rechtstreeks in Model Sport.
  2. Activiteit wordt Roosteractiviteit (het GGM kent al Activiteit in Model Musea en Model Omgevingswet).
  3. status blijft CharacterString (Lengte 80).
  4. Zwembadgebouw (kopie uit IMBOR 2025) komt onder Beheer Openbare Ruimte, in het package
     'Model IMBOR 2025' naast het bestaande 'Model Basis IMBOR'.
  5. Model Zwembaden (met Zwembad) wordt een apart model onder Model Sport; het diagram verhuist naar
     Sport > Diagram; de packages Zwembaden, Diagram en Gebruik en de klasse Type1 vervallen.
  6. Alles krijgt MIM: stereotypen «Objecttype», «Attribuutsoort», «Relatiesoort» en «Generalisatie»
     (profiel VNGR SIM+Grouping NL), MIM-datatypes, definities, toelichtingen en de MIM-tagsets.

Zelfde werkwijze als tools/fixes/add_samenwerkomgeving.py: één transactie, standaard een dry-run op een
tijdelijke kopie, met --apply vastleggen in de echte .qea. Idempotent: een tweede run meldt 0
wijzigingen. Enterprise Architect gesloten, back-up gemaakt.

Gebruik:
  python3 -I tools/fixes/fix_zwembaden.py "v3.0.0/Gemeentelijk Gegevensmodel.qea"          # dry-run
  python3 -I tools/fixes/fix_zwembaden.py "v3.0.0/Gemeentelijk Gegevensmodel.qea" --apply  # doorvoeren
"""
import argparse
import pathlib
import shutil
import sqlite3
import sys
import tempfile
import uuid
from datetime import datetime

# --- Vaste punten in de v3.0.0-.qea (ea_guid, verwachte naam) -----------------------------------
PKG_ZWEMBADEN = ("{F091D51E-5BE7-49fe-85FA-E96635885603}", "Zwembaden")
PKG_ZW_DIAGRAM = ("{D1B43921-3791-4b02-ACAE-881C9F47342A}", "Diagram")
PKG_GEBRUIK = ("{68BC62C7-75AF-46e2-9F6F-7E0C10514CC4}", "Gebruik")
PKG_IMBOR2025 = ("{5DD42CE9-62AD-4e99-AD9D-A3169B225199}", "Model IMBOR 2025")
PKG_MODEL_ZWEMBADEN = ("{0FBD0CBA-1C5F-4f77-AE0C-518C51EF3D02}", "Model Zwembaden")
PKG_MODEL_SPORT = ("{D6E7B2AB-8AD0-4c88-8742-3970AEDB4203}", "Model Sport")
PKG_SPORT_DIAGRAM = ("{679330EA-F82A-4e75-9BA3-D61B94798B91}", "Diagram")
PKG_BOR = ("{C3BA35EC-ABFA-4a7d-BEE9-07FF7563442D}", "Beheer Openbare Ruimte")
DIAGRAM = ("{5B708D19-E69C-49dd-A9AD-C0E58A573CC5}", "Diagram Zwembaden")

TPL_CLASS = ("{BBBB63AC-B546-409b-B6D4-53DB561253B7}", "Werknemer")
TPL_ATTR = ("{96DB65D5-F296-4d9b-857F-8327DFF570DE}", "naam")
TPL_ASSOC = ("{87F9EA19-0A1D-4c3f-ADCA-C8F48F216312}", "kan leiden tot")   # rij + stereotype-xref
TPL_ASSOC_TAGS = ("{1778947E-A0EE-C776-2C1C-281C33036576}", "leidt tot")   # MIM-tagset relatiesoort
TPL_GEN = ("{05E467BB-6588-411b-9079-294A9FA41A1F}", None)                 # Huurder -> Rechtspersoon

# naam -> ea_guid van objecttypen (eigen en hergebruikt)
OBJ = {
    "Zwembad": "{397B4ED8-307A-48c9-ADEA-E3D840DA8F28}",
    "Zwembadgebouw": "{42A61A85-526A-4813-96CA-7922FD6DD049}",
    "Gebruik": "{C5B5AF34-2388-4c5c-987C-FCA542BDF6C5}",
    "Gebruikstype": "{29F5D117-2C0D-4eb8-80B1-E38134D32C1F}",
    "Rooster": "{C545314E-6554-47a0-A26B-10F2E42A61C2}",
    "Roosteractiviteit": "{86C87DB9-0D96-485f-83D0-43C16AFE9266}",   # was Activiteit
    "Afnemer": "{DD90D4E4-CBF6-4a4f-A86A-0C464E5D9C73}",
    "Sportlocatie": "{BE5E10D0-FD83-4b0a-B5D2-4A7EE6B9C53B}",
    "Sportvereniging": "{852AD372-B353-49c2-A4E7-F87D8AA96AD7}",
    "Factuur": "{E1DA56C3-6ECA-4ec9-8CF4-FC57E1C43102}",
    "Rechtspersoon": "{9DF5AC43-3673-4b9a-BB5E-6DCA7BE28835}",
    "NatuurlijkPersoon": "{9F4E12E4-B228-4931-AC83-1B1F60958A89}",
    "OrganisatorischeEenheid": "{936A4E8B-3E5A-44b6-8A5D-EFB39F83FB6D}",
    "OrganisatorischeEenheidHR": "{53B0C49F-1BDE-4fee-BB0B-0D82517177CC}",
}
OLD_NAMES = {"Roosteractiviteit": "Activiteit"}
IN_MODEL_SPORT = ["Gebruik", "Gebruikstype", "Rooster", "Roosteractiviteit", "Afnemer"]
NOTES_KEEP = ["{3F6936DD-1E08-47c4-B61D-9C55468E0C40}",    # LET OP: IMBOR 2025
              "{521A6319-C1C3-4cfd-AFFD-A94639385841}",    # Zwembad tegenover Sportterrein
              "{73A545BC-82CA-4977-A2A5-1C0355A60639}"]    # Sportpark tegenover IMBOR-Sportterrein
NOTE_DROP = "{C77CA072-1156-4633-BDE1-6BA85471A9A8}"       # 'Kan een Zwembadgebouw ook voor buitenbaden?'
TYPE1 = "{3B47B2CC-5406-44e7-A80E-7F606EEA38A2}"

AUTHOR = "Arjen Brienen"
HERKOMST = "Proposal Zwembaden (Michiel Verhoef, VNG, 2026)"
HERKOMST_DEF = "GGM"
HERKOMST_IMBOR = "IMBOR 2025 (CROW)"
DATUM_OPNAME = "11 november 2026"

NOTE_MODEL_ZWEMBADEN = ("Deelmodel van Model Sport met de objecttypen die specifiek zijn voor zwembaden. Het gebruik "
                        "van een zwembad (gebruik, rooster, afnemer) is generiek gemodelleerd in Model Sport; het "
                        "zwembadgebouw komt uit IMBOR 2025.")
NOTE_MODEL_IMBOR2025 = ("Objecttypen uit IMBOR 2025 (CROW) die vooruitlopend op de opname van IMBOR 2025 in het GGM "
                        "zijn overgenomen. Bij de opname van IMBOR 2025 worden deze objecttypen vervangen door de "
                        "objecttypen uit IMBOR 2025.")

CS, INT, DEC, BOOL, DATE, DATETIME = "CharacterString", "Integer", "Decimal", "Boolean", "Date", "DateTime"

# naam -> (definitie, toelichting, herkomst, herkomst definitie)
CLASSES = {
    "Zwembad": (
        "Kunstmatig aangelegd bassin met water dat bestemd is om in te zwemmen of te baden.",
        "Met een zwembad is hier één bassin bedoeld, zoals een wedstrijdbad, instructiebad of peuterbad, en niet "
        "de hele zwemaccommodatie; dat is de Sportlocatie. Een binnenbad is onderdeel van een Zwembadgebouw, een "
        "buitenbad niet.",
        HERKOMST, HERKOMST_DEF),
    "Zwembadgebouw": (
        "Een zwembadgebouw is een gebouw dat is ontworpen en gebouwd om een of meer zwembaden te huisvesten, "
        "inclusief voorzieningen voor zwemmers en toeschouwers, en andere ondersteunende functies. Het kan een "
        "openbaar of particulier zwembad zijn en omvat vaak kleedkamers, douches, sanitaire voorzieningen, een "
        "ontvangstruimte en technische ruimtes voor de waterbehandeling en verwarming.",
        "Dit objecttype komt uit IMBOR 2025 (CROW) en is voor het proposal Zwembaden overgenomen omdat IMBOR 2025 "
        "nog niet in het GGM is opgenomen. Bij de opname van IMBOR 2025 moet dit objecttype worden vervangen door "
        "het objecttype uit IMBOR 2025. In IMBOR heeft Zwembadgebouw geen eigen attributen en is het samengesteld "
        "uit Constructie, FysiekObject, Gebouw, Geo-object, Object en ReëelObject.",
        HERKOMST_IMBOR, HERKOMST_IMBOR),
    "Gebruik": (
        "Het gebruik van een sportlocatie door een afnemer in een bepaalde periode, volgens een gebruikstype.",
        "Niet alleen voor zwembaden: het objecttype zou ook moeten passen op musea, speeltuinen, tentoonstellingen, "
        "festivals en dergelijke.",
        HERKOMST, HERKOMST_DEF),
    "Gebruikstype": (
        "Typering van de vorm waarin een afnemer een sportlocatie gebruikt, zoals huur, gratis toegang, losse "
        "entree, tienrittenkaart of abonnement.",
        "",
        HERKOMST, HERKOMST_DEF),
    "Rooster": (
        "Overzicht van de activiteiten die in een bepaalde periode op een sportlocatie zijn gepland.",
        "Nog te besluiten: leidt een wijziging in een rooster tot een nieuw rooster, of alleen tot nieuwe of "
        "gewijzigde activiteiten?",
        HERKOMST, HERKOMST_DEF),
    "Roosteractiviteit": (
        "Geplande bezigheid op een sportlocatie op een vastgesteld tijdstip of volgens een herhalingspatroon, "
        "zoals banenzwemmen, zwemles of een verenigingstraining.",
        "In het proposal heette dit objecttype Activiteit. Het is hernoemd omdat het GGM al objecttypen Activiteit "
        "kent in Model Musea en Model Omgevingswet, met een andere betekenis.",
        HERKOMST, HERKOMST_DEF),
    "Afnemer": (
        "Natuurlijk of niet-natuurlijk persoon die gebruikmaakt van een sportlocatie.",
        "Een afnemer kan een natuurlijk persoon zijn of een niet-natuurlijk persoon, zoals een sportvereniging of "
        "een school. Daarom is Afnemer een specialisatie van Rechtspersoon.",
        HERKOMST, HERKOMST_DEF),
}

# naam -> [(oude naam of None voor nieuw, naam, datatype, lengte, eenheid, definitie)], in de volgorde van het model
ATTRS = {
    "Zwembad": [
        (None, "naam", CS, 200, "", "Naam van het zwembad."),
        (None, "soort", CS, 80, "", "Soort zwembad, zoals wedstrijdbad, instructiebad, recreatiebad, peuterbad of "
                                    "doelgroepenbad."),
        (None, "lengte", DEC, 0, "m", "Lengte van het zwembad in meters."),
        (None, "breedte", DEC, 0, "m", "Breedte van het zwembad in meters."),
        (None, "diepteMinimaal", DEC, 0, "m", "Kleinste waterdiepte van het zwembad in meters."),
        (None, "diepteMaximaal", DEC, 0, "m", "Grootste waterdiepte van het zwembad in meters."),
        (None, "aantalBanen", INT, 0, "", "Aantal zwembanen van het zwembad."),
        (None, "indicatieBuitenbad", BOOL, 0, "", "Indicatie of het zwembad in de openlucht ligt."),
        (None, "indicatieBeweegbareBodem", BOOL, 0, "", "Indicatie of het zwembad een beweegbare bodem heeft."),
    ],
    "Zwembadgebouw": [
        (None, "naam", CS, 200, "", "Naam van het zwembadgebouw."),
    ],
    "Gebruik": [
        ("datumBegingeldigheid", "datumBeginGeldigheid", DATE, 0, "", "Datum waarop het gebruik ingaat."),
        ("datumEindgeldigheid", "datumEindeGeldigheid", DATE, 0, "", "Datum waarop het gebruik eindigt."),
    ],
    "Gebruikstype": [
        ("datumBeginGeldigheid", "datumBeginGeldigheid", DATE, 0, "", "Datum waarop het gebruikstype geldig wordt."),
        ("datumEindGeldigheid", "datumEindeGeldigheid", DATE, 0, "",
         "Datum waarop de geldigheid van het gebruikstype eindigt."),
        ("gebruikssoort", "gebruikssoort", CS, 80, "",
         "Soort gebruik waarop het gebruikstype betrekking heeft, zoals huur, gratis toegang, losse entree, "
         "tienrittenkaart of abonnement."),
    ],
    "Rooster": [
        ("datumBegingeldigheid", "datumBeginGeldigheid", DATE, 0, "", "Datum waarop het rooster ingaat."),
        ("datumEindgeldigheid", "datumEindeGeldigheid", DATE, 0, "", "Datum waarop het rooster eindigt."),
        ("status", "status", CS, 80, "", "Status van het rooster, zoals concept, vastgesteld of vervallen."),
        ("omschrijving", "omschrijving", CS, 0, "",
         "Omschrijving van het rooster, zoals zomerrooster of vakantierooster."),
        ("herhalend", "indicatieHerhalend", BOOL, 0, "", "Indicatie of het rooster zich periodiek herhaalt."),
    ],
    "Roosteractiviteit": [
        ("startDatumTijd", "startDatumTijd", DATETIME, 0, "", "Datum en tijdstip waarop de activiteit begint."),
        ("eindDatumTijd", "eindDatumTijd", DATETIME, 0, "", "Datum en tijdstip waarop de activiteit eindigt."),
        ("duur", "duur", INT, 0, "minuten", "Duur van de activiteit in minuten."),
        ("herhalingspatroon", "herhalingspatroon", CS, 200, "",
         "Patroon waarmee de activiteit zich herhaalt, bijvoorbeeld wekelijks op dinsdag."),
        ("datumBegingeldigheid", "datumBeginGeldigheid", DATE, 0, "",
         "Datum waarop de activiteit in het rooster geldig wordt."),
        ("datumEindgeldigheid", "datumEindeGeldigheid", DATE, 0, "",
         "Datum waarop de geldigheid van de activiteit in het rooster eindigt."),
        ("status", "status", CS, 80, "", "Status van de activiteit, zoals gepland, vervallen of uitgevoerd."),
        ("omschrijving", "omschrijving", CS, 0, "",
         "Omschrijving van de activiteit, zoals banenzwemmen, zwemles of training."),
    ],
    "Afnemer": [
        ("datumBegingeldigheid", "datumBeginGeldigheid", DATE, 0, "",
         "Datum vanaf wanneer de persoon als afnemer is geregistreerd."),
        ("datumEindgeldigheid", "datumEindeGeldigheid", DATE, 0, "",
         "Datum tot wanneer de persoon als afnemer is geregistreerd."),
    ],
}

# Bestaande relaties: ea_guid -> (bron, naam, doel, kardinaliteit bron, kardinaliteit doel, definitie)
RELATIONS = {
    "{D45F17CB-12C6-4e54-9AA3-6395B6F78C7D}": (
        "Zwembad", "is onderdeel van", "Zwembadgebouw", "1..*", "0..1",
        "Het zwembadgebouw waarin het zwembad ligt. Een buitenbad is geen onderdeel van een zwembadgebouw."),
    "{5A591CF3-8EDE-42ec-B0C2-656D0BFFE449}": (
        "Zwembadgebouw", "ligt op", "Sportlocatie", "0..*", "1",
        "De sportlocatie waarop het zwembadgebouw staat."),
    "{DC462817-1B91-430e-B42B-B85D7FEAAA90}": (
        "Rooster", "wordt onderhouden door", "OrganisatorischeEenheid", "0..*", "0..1",
        "De organisatorische eenheid die het rooster opstelt en bijhoudt."),
    "{A1E536C5-8B33-4752-8A1B-DADC674A24CF}": (
        "Rooster", "beschrijft gebruik van", "Sportlocatie", "0..*", "0..*",
        "De sportlocatie waarvan het rooster het gebruik beschrijft."),
    "{F62D4A46-803A-4cda-8E57-9E5D74EDDC44}": (
        "Rooster", "bevat", "Roosteractiviteit", "0..*", "0..*",
        "De activiteiten die in het rooster zijn opgenomen."),
    "{FEE4F19C-20E9-4d0f-A699-7CE7ADB6D2A0}": (
        "Gebruik", "betreft", "Sportlocatie", "0..*", "0..*",
        "De sportlocatie die wordt gebruikt."),
    "{CF1B59F5-06C4-4051-90F9-464845AAAD61}": (
        "Gebruik", "leidt tot", "Factuur", "0..*", "0..*",
        "De factuur die voor het gebruik is opgesteld."),
    "{ACDEC262-B0C7-45cb-B1FB-35A717A28D1D}": (
        "Gebruik", "wordt afgenomen door", "Afnemer", "0..*", "1",
        "De afnemer die van de sportlocatie gebruikmaakt."),
    "{28BD06B0-3E38-4ae3-AF0C-4BC33ADE0209}": (      # was Gebruikstype (1) 'is van' Gebruik (0..*): omgedraaid
        "Gebruik", "is van", "Gebruikstype", "0..*", "1",
        "Het gebruikstype dat op het gebruik van toepassing is."),
}
# Associaties 'is een' die vervallen (vervangen door de generalisatie Afnemer -> Rechtspersoon)
RELATIONS_DROP = ["{5821F4AF-2B61-42f8-BA65-AE5ECD4CB843}",   # Afnemer 'is een' NatuurlijkPersoon
                  "{72D100B6-8094-4096-82C2-0E539F272359}"]   # Sportvereniging 'is een' Afnemer
NEW_ASSOC = ("Zwembad", "ligt op", "Sportlocatie", "0..*", "1", "De sportlocatie waartoe het zwembad behoort.")
NEW_GEN = ("Afnemer", "Rechtspersoon")

GEMMA_TAGS = {"GEMMA alternate name", "GEMMA bron", "GEMMA definitie", "GEMMA guid", "GEMMA naam",
              "GEMMA synoniemen", "GEMMA toelichting", "GEMMA type", "GEMMA url", "Datum tijd export"}
JUNK_TAGS = ("documentation", "IMBOR-niveau", "IMBOR-rol", "Is afgeleid", "Samengesteld uit", "stereotype")
STYLE_FOREIGN = ("NSL=0;BCol=-1;BFol=-1;LCol=-1;fontsz=0;bold=0;black=0;italic=0;ul=0;charset=0;pitch=0;"
                 "HideIcon=0;LWth=2;")
GEOMETRY = "SX=0;SY=0;EX=0;EY=0;EDGE={edge};$LLB=;LLT=;LMT=;LMB=;LRT=;LRB=;IRHS=;ILHS=;"
RECHTSPERSOON_RECT = (15, -374, 115, -444)   # links van Afnemer: (left, top, right, bottom)


def new_guid() -> str:
    return "{" + str(uuid.uuid4()).upper() + "}"


def new_duid() -> str:
    return uuid.uuid4().hex[:8].upper()


class Fixer:
    def __init__(self, conn: sqlite3.Connection):
        self.c = conn
        self.c.row_factory = sqlite3.Row
        self.now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.changes = 0
        self.ids: dict[str, int] = {}

    # -- hulpfuncties ----------------------------------------------------------------------
    def say(self, msg: str) -> None:
        print(f"    {msg}")

    def step(self, title: str) -> None:
        print(f"\n{title}")

    def one(self, sql: str, *params):
        return self.c.execute(sql, params).fetchone()

    def all(self, sql: str, *params):
        return self.c.execute(sql, params).fetchall()

    def run(self, sql: str, *params) -> int:
        n = self.c.execute(sql, params).rowcount
        self.changes += n
        return n

    def insert(self, table: str, vals: dict) -> int:
        cols = list(vals)
        self.c.execute(f"INSERT INTO {table} ({', '.join(f'\"{k}\"' for k in cols)}) "
                       f"VALUES ({', '.join('?' * len(cols))})", [vals[k] for k in cols])
        self.changes += 1
        return self.c.execute("SELECT last_insert_rowid()").fetchone()[0]

    def set(self, table: str, key: str, keyval, **vals) -> list[str]:
        """Zet kolommen op de doelwaarde; geeft de namen van de kolommen die echt veranderden."""
        r = self.one(f"SELECT * FROM {table} WHERE {key}=?", keyval)
        if r is None:
            raise SystemExit(f"rij {keyval} niet gevonden in {table}; niets gewijzigd")
        diff = {k: v for k, v in vals.items() if r[k] != v}
        if diff:
            self.c.execute(f"UPDATE {table} SET {', '.join(f'\"{k}\"=?' for k in diff)} WHERE {key}=?",
                           [*diff.values(), keyval])
            self.changes += 1
        return list(diff)

    def row(self, table: str, ref: tuple, name_col: str = "Name"):
        r = self.one(f"SELECT * FROM {table} WHERE upper(ea_guid)=upper(?)", ref[0])
        if r is None or (ref[1] is not None and r[name_col] != ref[1]):
            raise SystemExit(f"{ref[1]} ({ref[0]}) niet gevonden in {table}; niets gewijzigd")
        return r

    def pkg(self, ref: tuple):
        """Package_ID bij een package-GUID, of None als het package al is vervallen."""
        r = self.one("SELECT Package_ID, Name FROM t_package WHERE upper(ea_guid)=upper(?)", ref[0])
        if r is not None and r["Name"] != ref[1]:
            raise SystemExit(f"package {ref[0]} heet {r['Name']}, verwacht {ref[1]}; niets gewijzigd")
        return r["Package_ID"] if r else None

    def stereotype_xref(self, guid: str, template_guid: str) -> int:
        """Stereotype-xref gelijk maken aan die van het sjabloon (profiel VNGR SIM+Grouping NL)."""
        tpl = self.one("SELECT * FROM t_xref WHERE upper(Client)=upper(?) AND Name='Stereotypes'", template_guid)
        cur = self.all("SELECT XrefID, Description FROM t_xref WHERE upper(Client)=upper(?) AND Name='Stereotypes'",
                       guid)
        if len(cur) == 1 and cur[0]["Description"] == tpl["Description"]:
            return 0
        for x in cur:
            self.run("DELETE FROM t_xref WHERE XrefID=?", x["XrefID"])
        vals = {k: tpl[k] for k in tpl.keys()}
        vals.update({"XrefID": new_guid(), "Client": guid})
        self.insert("t_xref", vals)
        return 1

    @staticmethod
    def memo(text: str) -> tuple:
        """EA bewaart lange tagwaarden als <memo> met de tekst in Notes."""
        if not text:
            return None, None
        return (text, None) if len(text) <= 255 else ("<memo>", text)

    # -- 0. controle -------------------------------------------------------------------------
    def check(self) -> None:
        self.step("0. Controle van de vaste punten")
        for name, guid in OBJ.items():
            r = self.one("SELECT Object_ID, Name FROM t_object WHERE upper(ea_guid)=upper(?)", guid)
            if r is None or r["Name"] not in (name, OLD_NAMES.get(name)):
                raise SystemExit(f"objecttype {name} ({guid}) niet gevonden; niets gewijzigd")
            self.ids[name] = r["Object_ID"]
        for ref in (PKG_MODEL_ZWEMBADEN, PKG_IMBOR2025, PKG_MODEL_SPORT, PKG_SPORT_DIAGRAM, PKG_BOR):
            if self.pkg(ref) is None:
                raise SystemExit(f"package {ref[1]} ({ref[0]}) niet gevonden; niets gewijzigd")
        self.row("t_diagram", DIAGRAM)
        self.say(f"{len(OBJ)} objecttypen, 5 packages en het diagram gevonden")

    # -- 1. packages -------------------------------------------------------------------------
    def packages(self) -> None:
        self.step("1. Packages verplaatsen en opruimen")
        sport, sport_dia, bor = self.pkg(PKG_MODEL_SPORT), self.pkg(PKG_SPORT_DIAGRAM), self.pkg(PKG_BOR)
        for ref, parent, parent_name, note in ((PKG_MODEL_ZWEMBADEN, sport, "Model Sport", NOTE_MODEL_ZWEMBADEN),
                                               (PKG_IMBOR2025, bor, "Beheer Openbare Ruimte", NOTE_MODEL_IMBOR2025)):
            d1 = self.set("t_package", "ea_guid", ref[0], Parent_ID=parent, Notes=note)
            d2 = self.set("t_object", "ea_guid", ref[0], Package_ID=parent, Note=note)
            if d1 or d2:
                self.set("t_package", "ea_guid", ref[0], ModifiedDate=self.now)
                self.set("t_object", "ea_guid", ref[0], ModifiedDate=self.now)
                self.say(f"package {ref[1]} staat nu onder {parent_name}, met beschrijving")
        moved = [n for n in IN_MODEL_SPORT if self.set("t_object", "Object_ID", self.ids[n], Package_ID=sport)]
        if moved:
            self.say(f"naar Model Sport: {', '.join(OLD_NAMES.get(n, n) for n in moved)}")
        if self.set("t_diagram", "ea_guid", DIAGRAM[0], Package_ID=sport_dia):
            self.set("t_diagram", "ea_guid", DIAGRAM[0], ModifiedDate=self.now)
            self.say("Diagram Zwembaden staat nu in Sport > Diagram")
        notes = [g for g in NOTES_KEEP if self.set("t_object", "ea_guid", g, Package_ID=sport_dia)]
        if notes:
            self.say(f"{len(notes)} notities meeverhuisd naar Sport > Diagram")
        for guid, what in ((NOTE_DROP, "notitie over buitenbaden"), (TYPE1, "klasse Type1")):
            r = self.one("SELECT Object_ID FROM t_object WHERE upper(ea_guid)=upper(?)", guid)
            if r is None:
                continue
            oid = r["Object_ID"]
            if self.one("SELECT 1 FROM t_connector WHERE Start_Object_ID=? OR End_Object_ID=?", oid, oid) or \
                    self.one("SELECT 1 FROM t_attribute WHERE Object_ID=?", oid):
                raise SystemExit(f"{what} heeft relaties of attributen; niets gewijzigd")
            self.run("DELETE FROM t_diagramobjects WHERE Object_ID=?", oid)
            self.run("DELETE FROM t_objectproperties WHERE Object_ID=?", oid)
            self.run("DELETE FROM t_xref WHERE upper(Client)=upper(?)", guid)
            self.run("DELETE FROM t_object WHERE Object_ID=?", oid)
            self.say(f"vervallen: {what}")
        for ref in (PKG_ZW_DIAGRAM, PKG_GEBRUIK, PKG_ZWEMBADEN):      # kinderen eerst
            pid = self.pkg(ref)
            if pid is None:
                continue
            rest = (self.one("SELECT COUNT(*) FROM t_object WHERE Package_ID=?", pid)[0]
                    + self.one("SELECT COUNT(*) FROM t_diagram WHERE Package_ID=?", pid)[0]
                    + self.one("SELECT COUNT(*) FROM t_package WHERE Parent_ID=?", pid)[0])
            if rest:
                raise SystemExit(f"package {ref[1]} ({pid}) is niet leeg ({rest} elementen); niets gewijzigd")
            self.run("DELETE FROM t_objectproperties WHERE Object_ID IN "
                     "(SELECT Object_ID FROM t_object WHERE upper(ea_guid)=upper(?))", ref[0])
            self.run("DELETE FROM t_xref WHERE upper(Client)=upper(?)", ref[0])
            self.run("DELETE FROM t_object WHERE upper(ea_guid)=upper(?) AND Object_Type='Package'", ref[0])
            self.run("DELETE FROM t_package WHERE Package_ID=?", pid)
            self.say(f"vervallen: leeg package {ref[1]} ({pid})")

    # -- 2. objecttypen ----------------------------------------------------------------------
    def classes(self) -> None:
        self.step("2. Objecttypen: stereotype, definitie, toelichting en MIM-tagset")
        tpl = self.row("t_object", TPL_CLASS)
        tpl_tags = self.all("SELECT Property, Value, Notes FROM t_objectproperties WHERE Object_ID=? "
                            "ORDER BY PropertyID", tpl["Object_ID"])
        for name, (definition, toelichting, herkomst, herkomst_def) in CLASSES.items():
            oid, guid = self.ids[name], OBJ[name]
            done = []
            d = self.set("t_object", "Object_ID", oid, Name=name, Stereotype="Objecttype", Note=definition,
                         Status="Proposed", Backcolor=-1, BorderWidth=-1, Fontcolor=-1, Bordercolor=-1)
            if "Name" in d:
                done.append(f"hernoemd van {OLD_NAMES[name]}")
            if "Stereotype" in d:
                done.append("«Objecttype»")
            if "Note" in d:
                done.append("definitie")
            if self.stereotype_xref(guid, TPL_CLASS[0]):
                done.append("profiel VNGR SIM")
            n = self.c.execute(f"DELETE FROM t_objectproperties WHERE Object_ID=? AND Property IN "
                               f"({', '.join('?' * len(JUNK_TAGS))})", [oid, *JUNK_TAGS]).rowcount
            if n:
                self.changes += n
                done.append(f"{n} importtags weg")
            t_val, t_notes = self.memo(toelichting)
            overrides = {"Herkomst": (herkomst, None), "Herkomst definitie": (herkomst_def, None),
                         "Datum opname": (DATUM_OPNAME, None), "Toelichting": (t_val, t_notes)}
            added = changed = 0
            for t in tpl_tags:
                prop = t["Property"]
                value, notes = overrides.get(prop, (None if prop in GEMMA_TAGS else t["Value"], t["Notes"]))
                cur = self.one("SELECT PropertyID, Value, Notes FROM t_objectproperties WHERE Object_ID=? AND Property=?",
                               oid, prop)
                if cur is None:
                    self.insert("t_objectproperties", {"Object_ID": oid, "Property": prop, "Value": value,
                                                       "Notes": notes, "ea_guid": new_guid()})
                    added += 1
                elif prop in overrides and (cur["Value"], cur["Notes"]) != (value, notes):
                    self.run("UPDATE t_objectproperties SET Value=?, Notes=? WHERE PropertyID=?",
                             value, notes, cur["PropertyID"])
                    changed += 1
            if added or changed:
                done.append(f"{added} tags toegevoegd" + (f", {changed} bijgewerkt" if changed else ""))
            if done:
                self.set("t_object", "Object_ID", oid, ModifiedDate=self.now)
                self.say(f"{name}: {'; '.join(done)}")

    # -- 3. attributen -----------------------------------------------------------------------
    def attributes(self) -> None:
        self.step("3. Attributen: «Attribuutsoort», MIM-datatype, definitie en MIM-tagset")
        tpl = self.row("t_attribute", TPL_ATTR)
        tpl_tags = self.all("SELECT Property, VALUE, NOTES FROM t_attributetag WHERE ElementID=? ORDER BY PropertyID",
                            tpl["ID"])
        dt = {r["Name"]: r["Object_ID"] for r in
              self.all("SELECT Object_ID, Name FROM t_object WHERE Object_Type='DataType' AND Package_ID=6")}
        for cname, attrs in ATTRS.items():
            oid = self.ids[cname]
            lines = []
            for pos, (old, name, dtype, length, eenheid, definition) in enumerate(attrs):
                if dtype not in dt:
                    raise SystemExit(f"datatype {dtype} niet gevonden in het datatype-package; niets gewijzigd")
                cur = self.one("SELECT * FROM t_attribute WHERE Object_ID=? AND Name IN (?, ?)", oid, name, old or name)
                target = {"Name": name, "Type": dtype, "Classifier": str(dt[dtype]), "Length": length,
                          "Stereotype": "Attribuutsoort", "Scope": "Public", "Notes": definition, "Pos": pos}
                if cur is None:
                    if old is not None:
                        raise SystemExit(f"attribuut {cname}.{old} niet gevonden; niets gewijzigd")
                    vals = {k: tpl[k] for k in tpl.keys() if k != "ID"}
                    vals.update(target)
                    vals.update({"Object_ID": oid, "Default": "", "Style": "", "ea_guid": new_guid()})
                    aid, aguid = self.insert("t_attribute", vals), vals["ea_guid"]
                    lines.append(f"+ {name} : {dtype}" + (f" ({length})" if length else ""))
                else:
                    aid, aguid = cur["ID"], cur["ea_guid"]
                    d = self.set("t_attribute", "ID", aid, **target)
                    if d:
                        was = f"{cur['Name']} : {cur['Type']}"
                        lines.append(f"{was} -> {name} : {dtype}" + (f" ({length})" if length else ""))
                self.stereotype_xref(aguid, TPL_ATTR[0])
                overrides = {"Lengte": str(length) if length else "", "Eenheid": eenheid or None,
                             "Herkomst": HERKOMST, "Datum opname": DATUM_OPNAME, "Mogelijk geen waarde": "Ja"}
                for t in tpl_tags:
                    prop = t["Property"]
                    value = overrides.get(prop, t["VALUE"])
                    c = self.one("SELECT PropertyID, VALUE FROM t_attributetag WHERE ElementID=? AND Property=?",
                                 aid, prop)
                    if c is None:
                        self.insert("t_attributetag", {"ElementID": aid, "Property": prop, "VALUE": value,
                                                       "NOTES": t["NOTES"], "ea_guid": new_guid()})
                    elif prop in overrides and c["VALUE"] != value:
                        self.run("UPDATE t_attributetag SET VALUE=? WHERE PropertyID=?", value, c["PropertyID"])
            if lines:
                self.set("t_object", "Object_ID", oid, ModifiedDate=self.now)
                self.say(f"{cname}:")
                for line in lines:
                    self.say(f"    {line}")

    # -- 4. relaties -------------------------------------------------------------------------
    def connector_tags(self, cid: int, tpl_tags) -> int:
        overrides = {"Herkomst": HERKOMST, "Datum opname": DATUM_OPNAME, "Authentiek": "Overig"}
        n = 0
        for t in tpl_tags:
            prop = t["Property"]
            if self.one("SELECT 1 FROM t_connectortag WHERE ElementID=? AND Property=?", cid, prop):
                continue
            self.insert("t_connectortag", {"ElementID": cid, "Property": prop, "VALUE": overrides.get(prop, t["VALUE"]),
                                           "NOTES": t["NOTES"], "ea_guid": new_guid()})
            n += 1
        return n

    def relations(self) -> None:
        self.step("4. Relaties: «Relatiesoort», leesrichting, kardinaliteit, definitie en MIM-tagset")
        tpl = self.row("t_connector", TPL_ASSOC)
        tag_tpl = self.row("t_connector", TPL_ASSOC_TAGS)
        tpl_tags = self.all("SELECT Property, VALUE, NOTES FROM t_connectortag WHERE ElementID=? ORDER BY PropertyID",
                            tag_tpl["Connector_ID"])
        style = {k: tpl[k] for k in ("Direction", "SourceStyle", "DestStyle", "SourceIsNavigable", "DestIsNavigable")}
        dia = self.row("t_diagram", DIAGRAM)["Diagram_ID"]

        for guid in RELATIONS_DROP:
            r = self.one("SELECT c.Connector_ID, c.Name, s.Name AS s, d.Name AS d FROM t_connector c "
                         "JOIN t_object s ON s.Object_ID=c.Start_Object_ID JOIN t_object d ON d.Object_ID=c.End_Object_ID "
                         "WHERE upper(c.ea_guid)=upper(?)", guid)
            if r is None:
                continue
            self.run("DELETE FROM t_diagramlinks WHERE ConnectorID=?", r["Connector_ID"])
            self.run("DELETE FROM t_connectortag WHERE ElementID=?", r["Connector_ID"])
            self.run("DELETE FROM t_xref WHERE upper(Client)=upper(?)", guid)
            self.run("DELETE FROM t_connector WHERE Connector_ID=?", r["Connector_ID"])
            self.say(f"vervallen: associatie {r['s']} '{r['Name']}' {r['d']}")

        for guid, (src, name, dst, scard, dcard, definition) in RELATIONS.items():
            cur = self.one("SELECT c.*, s.Name AS s, d.Name AS d FROM t_connector c "
                           "JOIN t_object s ON s.Object_ID=c.Start_Object_ID JOIN t_object d ON d.Object_ID=c.End_Object_ID "
                           "WHERE upper(c.ea_guid)=upper(?)", guid)
            if cur is None:
                raise SystemExit(f"relatie {src} '{name}' {dst} ({guid}) niet gevonden; niets gewijzigd")
            cid = cur["Connector_ID"]
            reversed_ = cur["Start_Object_ID"] == self.ids[dst] and cur["End_Object_ID"] == self.ids[src]
            d = self.set("t_connector", "Connector_ID", cid, Name=name, Stereotype="Relatiesoort", Notes=definition,
                         Start_Object_ID=self.ids[src], End_Object_ID=self.ids[dst], SourceCard=scard, DestCard=dcard,
                         Top_Mid_Label=name, Btm_Start_Label=scard, Btm_End_Label=dcard, **style)
            x = self.stereotype_xref(guid, TPL_ASSOC[0])
            t = self.connector_tags(cid, tpl_tags)
            if reversed_:
                link = self.one("SELECT Instance_ID, Style FROM t_diagramlinks WHERE DiagramID=? AND ConnectorID=?", dia, cid)
                if link:
                    parts = dict(p.split("=", 1) for p in link["Style"].split(";") if "=" in p)
                    parts["SOID"], parts["EOID"] = parts.get("EOID", ""), parts.get("SOID", "")
                    self.run("UPDATE t_diagramlinks SET Style=?, Geometry=? WHERE Instance_ID=?",
                             "".join(f"{k}={v};" for k, v in parts.items()), GEOMETRY.format(edge=3), link["Instance_ID"])
            if d or x or t:
                was = f"{cur['s']} {cur['SourceCard']} '{cur['Name']}' {cur['d']} {cur['DestCard']}"
                now = f"{src} {scard} '{name}' {dst} {dcard}"
                self.say(now if was == now else f"{now}   (was: {was})")

        # nieuwe associatie Zwembad 'ligt op' Sportlocatie
        src, name, dst, scard, dcard, definition = NEW_ASSOC
        cur = self.one("SELECT Connector_ID FROM t_connector WHERE Start_Object_ID=? AND End_Object_ID=? AND "
                       "Connector_Type='Association' AND Name=?", self.ids[src], self.ids[dst], name)
        if cur is None:
            vals = {k: tpl[k] for k in tpl.keys() if k != "Connector_ID"}
            vals.update({"Name": name, "Notes": definition, "SourceCard": scard, "DestCard": dcard,
                         "Btm_Start_Label": scard, "Btm_End_Label": dcard, "Top_Mid_Label": name,
                         "Start_Object_ID": self.ids[src], "End_Object_ID": self.ids[dst], "DiagramID": 0,
                         "ea_guid": new_guid()})
            cid = self.insert("t_connector", vals)
            self.stereotype_xref(vals["ea_guid"], TPL_ASSOC[0])
            self.connector_tags(cid, tpl_tags)
            self.say(f"nieuw: {src} {scard} '{name}' {dst} {dcard}")
        self.new_assoc = self.one("SELECT Connector_ID FROM t_connector WHERE Start_Object_ID=? AND End_Object_ID=? "
                                  "AND Connector_Type='Association' AND Name=?",
                                  self.ids[src], self.ids[dst], name)["Connector_ID"]

        # nieuwe generalisatie Afnemer -> Rechtspersoon
        sub, sup = NEW_GEN
        cur = self.one("SELECT Connector_ID FROM t_connector WHERE Start_Object_ID=? AND End_Object_ID=? AND "
                       "Connector_Type='Generalization'", self.ids[sub], self.ids[sup])
        if cur is None:
            gen = self.row("t_connector", TPL_GEN)
            vals = {k: gen[k] for k in gen.keys() if k != "Connector_ID"}
            vals.update({"Start_Object_ID": self.ids[sub], "End_Object_ID": self.ids[sup], "DiagramID": 0,
                         "Notes": None, "ea_guid": new_guid()})
            self.insert("t_connector", vals)
            self.stereotype_xref(vals["ea_guid"], TPL_GEN[0])
            self.say(f"nieuw: «Generalisatie» {sub} -> {sup}")
        self.new_gen = self.one("SELECT Connector_ID FROM t_connector WHERE Start_Object_ID=? AND End_Object_ID=? "
                                "AND Connector_Type='Generalization'", self.ids[sub], self.ids[sup])["Connector_ID"]

    # -- 5. diagram --------------------------------------------------------------------------
    def duid(self, dia: int, oid: int):
        r = self.one("SELECT ObjectStyle FROM t_diagramobjects WHERE Diagram_ID=? AND Object_ID=?", dia, oid)
        return r["ObjectStyle"].split("DUID=")[1].split(";")[0] if r else None

    def diagram(self) -> None:
        self.step("5. Diagram Zwembaden bijwerken")
        dia = self.row("t_diagram", DIAGRAM)["Diagram_ID"]
        before = self.changes
        hr, oe = self.ids["OrganisatorischeEenheidHR"], self.ids["OrganisatorischeEenheid"]
        if self.duid(dia, hr) and not self.duid(dia, oe):
            self.run("UPDATE t_diagramobjects SET Object_ID=? WHERE Diagram_ID=? AND Object_ID=?", oe, dia, hr)
            self.say("OrganisatorischeEenheidHR vervangen door OrganisatorischeEenheid (Kern RGBZ)")
        rp = self.ids["Rechtspersoon"]
        if not self.duid(dia, rp):
            left, top, right, bottom = RECHTSPERSOON_RECT
            seq = (self.one("SELECT MAX(Sequence) FROM t_diagramobjects WHERE Diagram_ID=?", dia)[0] or 0) + 1
            self.insert("t_diagramobjects", {"Diagram_ID": dia, "Object_ID": rp, "RectTop": top, "RectLeft": left,
                                             "RectRight": right, "RectBottom": bottom, "Sequence": seq,
                                             "ObjectStyle": "DUID=" + new_duid() + ";" + STYLE_FOREIGN})
            self.say("Rechtspersoon geplaatst, links van Afnemer")
        for cid, src, dst, edge in ((self.new_gen, "Afnemer", "Rechtspersoon", 4),
                                    (self.new_assoc, "Zwembad", "Sportlocatie", 1)):
            if self.one("SELECT 1 FROM t_diagramlinks WHERE DiagramID=? AND ConnectorID=?", dia, cid):
                continue
            self.insert("t_diagramlinks", {
                "DiagramID": dia, "ConnectorID": cid, "Geometry": GEOMETRY.format(edge=edge),
                "Style": f"Mode=3;EOID={self.duid(dia, self.ids[dst])};SOID={self.duid(dia, self.ids[src])};"
                         f"Color=-1;LWidth=0;", "Hidden": 0, "Path": ""})
            self.say(f"link toegevoegd: {src} -> {dst}")
        if self.changes != before:
            self.set("t_diagram", "Diagram_ID", dia, ModifiedDate=self.now)

    # -- 6. eindcontrole ---------------------------------------------------------------------
    def verify(self) -> int:
        self.step("6. Eindcontrole (cookbook m1, m3, m4, m7 en MIM-stereotypen)")
        problems = []
        ids = [self.ids[n] for n in CLASSES]
        marks = ", ".join("?" * len(ids))
        for r in self.all(f"SELECT o.Name, o.Stereotype, o.Note, p.Name AS pkg, "
                          f"(SELECT COUNT(*) FROM t_attribute a WHERE a.Object_ID=o.Object_ID) AS n "
                          f"FROM t_object o JOIN t_package p ON p.Package_ID=o.Package_ID WHERE o.Object_ID IN ({marks}) "
                          f"ORDER BY p.Name, o.Name", *ids):
            self.say(f"{r['pkg']} > {r['Name']} «{r['Stereotype']}», {r['n']} attributen")
            if r["Stereotype"] != "Objecttype" or not r["Note"] or r["n"] == 0:
                problems.append(f"objecttype {r['Name']}")
        for r in self.all(f"SELECT o.Name AS o, a.Name, a.Type, a.Stereotype, a.Notes, c.Name AS cls FROM t_attribute a "
                          f"JOIN t_object o ON o.Object_ID=a.Object_ID LEFT JOIN t_object c ON c.Object_ID=a.Classifier "
                          f"WHERE a.Object_ID IN ({marks})", *ids):
            if r["Stereotype"] != "Attribuutsoort" or not r["Notes"] or r["cls"] != r["Type"]:
                problems.append(f"attribuut {r['o']}.{r['Name']}")
        for r in self.all(f"SELECT c.Connector_Type, c.Stereotype, c.Name, c.SourceCard, c.DestCard, c.Direction, "
                          f"s.Name AS s, d.Name AS d FROM t_connector c JOIN t_object s ON s.Object_ID=c.Start_Object_ID "
                          f"JOIN t_object d ON d.Object_ID=c.End_Object_ID WHERE (c.Start_Object_ID IN ({marks}) "
                          f"OR c.End_Object_ID IN ({marks})) AND c.Connector_Type<>'NoteLink' "   # notitiekoppelingen tellen niet
                          f"ORDER BY s.Name, c.Name", *ids, *ids):
            assoc = r["Connector_Type"] == "Association"
            ok = (r["Stereotype"] == "Relatiesoort" and r["SourceCard"] and r["DestCard"]
                  and r["Direction"] == "Source -> Destination") if assoc else r["Stereotype"] == "Generalisatie"
            if not ok:
                problems.append(f"relatie {r['s']} '{r['Name']}' {r['d']}")
        n_attr = self.one(f"SELECT COUNT(*) FROM t_attribute WHERE Object_ID IN ({marks})", *ids)[0]
        n_rel = self.one(f"SELECT COUNT(*) FROM t_connector WHERE (Start_Object_ID IN ({marks}) OR End_Object_ID IN ({marks})) "
                         f"AND Connector_Type<>'NoteLink'", *ids, *ids)[0]
        self.say(f"{len(ids)} objecttypen, {n_attr} attributen, {n_rel} relaties; {len(problems)} afwijking(en)")
        for p in problems:
            self.say(f"    AFWIJKING: {p}")
        return len(problems)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("qea", help="pad naar de .qea (SQLite) van Enterprise Architect")
    ap.add_argument("--apply", action="store_true", help="wijzigingen vastleggen (zonder: dry-run op een kopie)")
    args = ap.parse_args()

    target = args.qea
    if not args.apply:
        tmp = tempfile.NamedTemporaryFile(prefix="fix_zwembaden-", suffix=".qea", delete=False)
        tmp.close()
        shutil.copyfile(args.qea, tmp.name)
        target = tmp.name
    conn = sqlite3.connect(target, isolation_level=None)
    conn.execute("BEGIN")
    f = Fixer(conn)
    try:
        f.check()
        f.packages()
        f.classes()
        f.attributes()
        f.relations()
        f.diagram()
        problems = f.verify()
    except BaseException:
        conn.execute("ROLLBACK")
        if not args.apply:
            conn.close()
            pathlib.Path(target).unlink(missing_ok=True)
        raise

    print(f"\n{f.changes} gewijzigde rijen; {problems} afwijking(en) in de eindcontrole")
    if args.apply and problems == 0:
        conn.execute("COMMIT")
        ok = conn.execute("PRAGMA integrity_check").fetchone()[0]
        print(f"TOEGEPAST en vastgelegd in {args.qea}; integrity_check: {ok}")
        return 0 if ok == "ok" else 1
    conn.execute("ROLLBACK")
    conn.close()
    if args.apply:
        print("NIET toegepast: de eindcontrole meldt afwijkingen")
        return 1
    pathlib.Path(target).unlink(missing_ok=True)
    print("DRY-RUN op een tijdelijke kopie: niets opgeslagen (gebruik --apply om door te voeren)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
