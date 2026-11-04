#!/usr/bin/env python3
"""Proposal Samenwerkomgeving (Erik de Lepper, gemeente 's-Hertogenbosch, 2025; openbare consultatie
mei-juni 2026) opnemen in de EA-repository van het GGM (.qea = SQLite), volgens de uitwerking in
tools/proposal-samenwerkomgeving.md (aanbevolen keuzes: eigen package, Teamlidmaatschap met
enumeratie Teamrol, Chatbox vervalt, Lid wordt Teamlid met relatie naar Medewerker uit Kern RGBZ).

Zelfde werkwijze als tools/fix_proposal_mor.py: één transactie, standaard een dry-run op een
tijdelijke kopie, met --apply vastleggen in de echte .qea. Idempotent: een tweede run meldt 0
wijzigingen. Enterprise Architect gesloten, back-up gemaakt.

Wat het script doet, alles gekopieerd van bestaande rijen (package HR, klasse Werknemer, enumeratie
Applicatiecategorie, relatie 'kan leiden tot', diagram 'Domain Objects' van HR) met nieuwe GUID's:
  1. Package «Domein» Samenwerkomgeving onder 9 Interne Organisatie, met subpackages Diagram en
     Model Samenwerkomgeving, inclusief de package-tags (Release, Datum opname, Herkomst).
  2. Enumeratie «Enumeratie» Teamrol (eigenaar, lid, gast).
  3. Vijftien objecttypen «Objecttype» met definitie, de MIM-tagset en attributen met MIM-datatypes
     (CharacterString met Lengte, Boolean, Date, DateTime, Decimal, URI).
  4. Eenentwintig relaties «Relatiesoort» met kardinaliteiten, waaronder Teamlid 'is medewerker'
     Medewerker (Model Kern RGBZ).
  5. Diagram 'Samenwerkomgeving' met alle elementen (attributen zichtbaar) en alle relaties.

Gebruik:
  python3 -I tools/add_samenwerkomgeving.py "v3.0.0/Gemeentelijk Gegevensmodel.qea"          # dry-run
  python3 -I tools/add_samenwerkomgeving.py "v3.0.0/Gemeentelijk Gegevensmodel.qea" --apply  # doorvoeren
"""
import argparse
import pathlib
import shutil
import sqlite3
import sys
import tempfile
import uuid
from datetime import datetime

# --- Sjablonen en vaste punten in de v3.0.0-.qea (ea_guid, verwachte naam) ----------------------
PARENT_PACKAGE = "9 Interne Organisatie"
TPL_PKG_DOMEIN = ("{1825F01E-BA3C-4e53-B3B3-BD1E69F94A10}", "HR")
TPL_PKG_DIAGRAM = ("{CBDBF4A5-72BE-4e6b-9028-141B290AEEAA}", "Diagram")
TPL_PKG_MODEL = ("{9ADEFB08-F150-4278-8D32-32465C57E8A7}", "Model HR")
TPL_CLASS = ("{BBBB63AC-B546-409b-B6D4-53DB561253B7}", "Werknemer")
TPL_ATTR = ("{96DB65D5-F296-4d9b-857F-8327DFF570DE}", "naam")
TPL_ENUM = ("{A030D866-E2E7-4854-ACFD-C62DB3ABDA38}", "Applicatiecategorie")
TPL_LITERAL = ("{EE0C3E87-BCB5-499e-ABBB-CB158AB71B84}", "Kernapplicatie")
TPL_CONNECTOR = ("{87F9EA19-0A1D-4c3f-ADCA-C8F48F216312}", "kan leiden tot")
TPL_DIAGRAM = ("{891372E6-27FB-442d-9CC4-08C2659E8C53}", "Domain Objects")
MEDEWERKER = ("{16EB3936-03CB-4854-9CD8-9F0911EEA51B}", "Medewerker")
DIAGRAM_OBJECT_STYLE = ("NSL=0;BCol=-1;BFol=-1;LCol=-1;LWth=-1;fontsz=0;bold=0;black=0;italic=0;ul=0;charset=0;"
                        "pitch=0;AttPro=0;AttPri=0;AttPub=0;AttPkg=0;OpPro=0;OpPri=0;OpPub=0;OpPkg=0;AttCustom=0;"
                        "OpCustom=0;RzO=1;")

PACKAGE = "Samenwerkomgeving"
MODEL_PACKAGE = "Model Samenwerkomgeving"
DIAGRAM = "Samenwerkomgeving"
AUTHOR = "Arjen Brienen"
HERKOMST = "Proposal Samenwerkomgeving, gemeente 's-Hertogenbosch (Erik de Lepper, 2025)"
DATUM_OPNAME = "4 november 2026"
RELEASE = "20261104"
PACKAGE_NOTE = ("Het informatiesubdomein dat gegevens omvat over de digitale samenwerkomgevingen van de gemeente, "
                "zoals Microsoft Teams en SharePoint, gericht op teams, hun leden en rollen, kanalen en "
                "chatberichten, bestanden, lijsten en de gezamenlijke mailbox met agenda en taken.")

CS, BOOL, DATE, DATETIME, DECIMAL, URI = "CharacterString", "Boolean", "Date", "DateTime", "Decimal", "URI"
ENUM = ("Teamrol", "Rechtenrol die een teamlid binnen een team heeft.", ["eigenaar", "lid", "gast"])

# naam -> (definitie, [(attribuut, datatype, lengte, definitie)])
CLASSES = {
    "Samenwerkomgeving": (
        "Digitale werkomgeving van een team waarin de leden samenwerken aan bestanden, lijsten en gesprekken, "
        "zoals een site in Microsoft Teams of SharePoint. Als in een team een privékanaal wordt aangemaakt, "
        "ontstaat een nieuwe samenwerkomgeving met eigen leden en een eigen kanaal.",
        [("titel", CS, 200, "Titel van de samenwerkomgeving."),
         ("beschrijving", CS, 0, "Beschrijving van de samenwerkomgeving."),
         ("URL", URI, 0, "Locatie van en link naar de samenwerkomgeving."),
         ("datumCreatie", DATETIME, 0, "Datum en tijd waarop de samenwerkomgeving is aangemaakt."),
         ("datumLaatstGebruikt", DATE, 0, "Datum waarop de samenwerkomgeving voor het laatst is gebruikt."),
         ("grootte", DECIMAL, 0, "Opslagruimte die de totale samenwerkomgeving inneemt, in MB."),
         ("soort", CS, 80, "Soort samenwerkomgeving, zoals hubsite, teamsite of communicatiesite.")]),
    "Team": (
        "Groep personen die binnen een samenwerkomgeving samenwerkt, met eigen leden en rollen, kanalen en "
        "een gezamenlijke mailbox.",
        [("naam", CS, 200, "Naam van het team."),
         ("indicatieHoofdteam", BOOL, 0, "Indicatie of dit het hoofdteam is waaruit privékanalen zijn afgesplitst."),
         ("omschrijving", CS, 0, "Omschrijving van het team.")]),
    "Kanaal": (
        "Kanaal binnen een samenwerkomgeving, gewijd aan een onderwerp of deelgroep, waarin teamleden "
        "chatberichten uitwisselen.",
        [("naam", CS, 200, "Naam van het kanaal."),
         ("omschrijving", CS, 0, "Omschrijving van het kanaal.")]),
    "Chatbericht": (
        "Bericht van een teamlid in een kanaal van de samenwerkomgeving.",
        [("datumCreatie", DATETIME, 0, "Datum en tijd waarop het bericht is aangemaakt."),
         ("datumLaatsteWijziging", DATETIME, 0, "Datum en tijd waarop het bericht voor het laatst is gewijzigd."),
         ("inhoud", CS, 0, "Het bericht zelf.")]),
    "Teamlid": (
        "Interne medewerker of externe persoon die lid is van een team en daarmee rechten heeft in de "
        "samenwerkomgeving.",
        [("naam", CS, 200, "Naam die wordt getoond."),
         ("emailadres", CS, 254, "E-mailadres van het teamlid; identificeert interne en externe leden uniform."),
         ("organisatorischeEenheid", CS, 200, "Organisatorische eenheid waartoe het teamlid behoort.")]),
    "Teamlidmaatschap": (
        "Het lidmaatschap van een teamlid van een team, met de rol die het teamlid in dat team heeft.",
        [("rol", "Teamrol", 0, "Rechtenrol van het teamlid binnen het team."),
         ("datumToetreding", DATE, 0, "Datum waarop het teamlid tot het team is toegetreden.")]),
    "Mailbox": (
        "Mailbox van het team waarin teammails, de teamagenda en teamtaken worden vastgelegd.",
        [("emailadres", CS, 254, "E-mailadres van het team.")]),
    "Emailbericht": (
        "E-mailbericht dat via de mailbox van het team is ontvangen of verzonden.",
        [("onderwerp", CS, 200, "Onderwerp van het e-mailbericht."),
         ("datumVerzonden", DATETIME, 0, "Datum en tijd waarop het e-mailbericht is verzonden."),
         ("afzender", CS, 254, "E-mailadres van de afzender.")]),
    "AgendaItem": (
        "Afspraak of gebeurtenis in de gezamenlijke agenda van het team.",
        [("onderwerp", CS, 200, "Onderwerp van het agenda-item."),
         ("datumTijdBegin", DATETIME, 0, "Datum en tijd waarop het agenda-item begint."),
         ("datumTijdEinde", DATETIME, 0, "Datum en tijd waarop het agenda-item eindigt."),
         ("locatie", CS, 200, "Locatie van het agenda-item.")]),
    "Teamtaak": (
        "Taak in de gezamenlijke takenlijst van het team, die aan een teamlid kan zijn toegewezen.",
        [("titel", CS, 200, "Titel van de taak."),
         ("status", CS, 80, "Status van de taak, zoals niet gestart, bezig of afgerond."),
         ("datumGereed", DATE, 0, "Datum waarop de taak gereed moet zijn.")]),
    "Bibliotheek": (
        "Logische groepering van bestanden binnen een samenwerkomgeving.",
        [("naam", CS, 200, "Naam van de bibliotheek.")]),
    "Bestand": (
        "Bestand dat in een bibliotheek van de samenwerkomgeving is opgeslagen.",
        [("naam", CS, 255, "Naam van het bestand."),
         ("bestandstype", CS, 100, "Bestandsformaat (mimetype)."),
         ("grootte", DECIMAL, 0, "Grootte van het bestand in MB."),
         ("datumCreatie", DATETIME, 0, "Datum en tijd waarop het bestand is aangemaakt."),
         ("datumLaatsteWijziging", DATETIME, 0, "Datum en tijd waarop het bestand voor het laatst is gewijzigd.")]),
    "Lijst": (
        "Lijst met een groep eigenschappen (kolommen) waarin gegevens binnen de samenwerkomgeving worden "
        "vastgelegd.",
        [("naam", CS, 200, "Naam van de lijst.")]),
    "Inhoudstype": (
        "Groep van kenmerken (kolommen) die samen een soort inhoud in een lijst beschrijft.",
        [("naam", CS, 200, "Naam van het inhoudstype.")]),
    "Kolom": (
        "Kenmerk (veld) van een inhoudstype in een lijst.",
        [("naam", CS, 200, "Naam van de kolom."),
         ("datatype", CS, 80, "Datatype van de kolom.")]),
    "Lijstitem": (
        "Waarde van een kenmerk voor een item in een lijst.",
        [("waarde", CS, 0, "Waarde van een veld in een lijst.")]),
}
# (bron, relatienaam, doel, kardinaliteit bron, kardinaliteit doel)
RELATIONS = [
    ("Team", "heeft samenwerkomgevingen", "Samenwerkomgeving", "0..1", "1..*"),
    ("Team", "heeft mailbox", "Mailbox", "0..1", "1"),
    ("Samenwerkomgeving", "heeft kanalen", "Kanaal", "1", "1..*"),
    ("Samenwerkomgeving", "heeft bibliotheken", "Bibliotheek", "1", "0..*"),
    ("Samenwerkomgeving", "heeft lijsten", "Lijst", "1", "0..*"),
    ("Kanaal", "bevat chatberichten", "Chatbericht", "1", "0..*"),
    ("Chatbericht", "geschreven door", "Teamlid", "0..*", "1"),
    ("Teamlidmaatschap", "van teamlid", "Teamlid", "0..*", "1"),
    ("Teamlidmaatschap", "in team", "Team", "0..*", "1"),
    ("Teamlid", "is medewerker", "Medewerker", "0..1", "0..1"),
    ("Mailbox", "heeft emailberichten", "Emailbericht", "1", "0..*"),
    ("Mailbox", "heeft agenda-items", "AgendaItem", "1", "0..*"),
    ("Mailbox", "heeft taken", "Teamtaak", "1", "0..*"),
    ("Teamtaak", "toegewezen aan", "Teamlid", "0..*", "0..1"),
    ("Bibliotheek", "heeft bestanden", "Bestand", "1", "0..*"),
    ("Bestand", "aangemaakt door", "Teamlid", "0..*", "1"),
    ("Bestand", "gewijzigd door", "Teamlid", "0..*", "0..1"),
    ("Lijst", "heeft inhoudstypen", "Inhoudstype", "1..*", "1..*"),
    ("Lijst", "heeft items", "Lijstitem", "1", "0..*"),
    ("Inhoudstype", "heeft kolommen", "Kolom", "0..*", "1..*"),
    ("Kolom", "heeft waarden", "Lijstitem", "1..*", "0..*"),
]
# Diagramraster: naam -> (kolom, rij); kolommen 270 breed, rijen 270 hoog.
LAYOUT = {
    "Team": (0, 0), "Teamlidmaatschap": (1, 0), "Teamlid": (2, 0), "Medewerker": (3, 0), "Teamrol": (4, 0),
    "Mailbox": (0, 1), "Samenwerkomgeving": (1, 1), "Kanaal": (2, 1), "Chatbericht": (3, 1),
    "Emailbericht": (0, 2), "AgendaItem": (1, 2), "Teamtaak": (2, 2), "Bibliotheek": (3, 2), "Bestand": (4, 2),
    "Lijst": (0, 3), "Inhoudstype": (1, 3), "Kolom": (2, 3), "Lijstitem": (3, 3),
}
COL_X, ROW_Y, WIDTH = [30, 300, 570, 840, 1110], [-30, -300, -570, -840], 230
GEMMA_TAGS = {"GEMMA alternate name", "GEMMA bron", "GEMMA definitie", "GEMMA guid", "GEMMA naam",
              "GEMMA synoniemen", "GEMMA toelichting", "GEMMA type", "GEMMA url", "Datum tijd export"}


def new_guid() -> str:
    return "{" + str(uuid.uuid4()).upper() + "}"


def new_duid() -> str:
    return uuid.uuid4().hex[:8].upper()


class Builder:
    def __init__(self, conn: sqlite3.Connection):
        self.c = conn
        self.c.row_factory = sqlite3.Row
        self.now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.changes = 0
        self.warnings: list[str] = []
        self.ids: dict[str, int] = {}        # elementnaam -> Object_ID (klassen, enumeratie, Medewerker)
        self.guids: dict[str, str] = {}      # elementnaam -> ea_guid
        self.connectors: list[tuple[int, str, str]] = []  # (Connector_ID, bron, doel)

    def say(self, msg: str) -> None:
        print(f"    {msg}")

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)
        print(f"    LET OP: {msg}")

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
        self.c.execute(f"INSERT INTO {table} ({', '.join(f'\"{k}\"' for k in cols)}) VALUES ({', '.join('?' * len(cols))})",
                       [vals[k] for k in cols])
        self.changes += 1
        return self.c.execute("SELECT last_insert_rowid()").fetchone()[0]

    def row(self, table: str, guid_col: str, ref: tuple[str, str], name_col: str = "Name"):
        r = self.one(f"SELECT * FROM {table} WHERE upper({guid_col})=upper(?)", ref[0])
        if r is None or r[name_col] != ref[1]:
            raise SystemExit(f"sjabloon {ref[1]} ({ref[0]}) niet gevonden in {table}; niets gewijzigd")
        return r

    def copy_tags(self, template_object_id: int, object_id: int, overrides: dict) -> int:
        n = 0
        for t in self.all("SELECT Property, Value, Notes FROM t_objectproperties WHERE Object_ID=? ORDER BY PropertyID", template_object_id):
            value = "" if t["Property"] in GEMMA_TAGS else t["Value"]
            self.insert("t_objectproperties", {"Object_ID": object_id, "Property": t["Property"],
                                               "Value": overrides.get(t["Property"], value), "Notes": t["Notes"],
                                               "ea_guid": new_guid()})
            n += 1
        return n

    def copy_xref(self, template_guid: str, guid: str) -> int:
        n = 0
        for x in self.all("SELECT * FROM t_xref WHERE upper(Client)=upper(?)", template_guid):
            vals = {k: x[k] for k in x.keys()}
            vals.update({"XrefID": new_guid(), "Client": guid})
            self.insert("t_xref", vals)
            n += 1
        return n

    def datatype_id(self, name: str) -> int:
        if name in self.ids:
            return self.ids[name]
        r = self.one("SELECT Object_ID FROM t_object WHERE Object_Type='DataType' AND Package_ID=6 AND Name=?", name)
        if r is None:
            raise SystemExit(f"datatype {name} niet gevonden in het datatype-package")
        self.ids[name] = r["Object_ID"]
        return r["Object_ID"]

    # -- 1. packages ----------------------------------------------------------------------
    def packages(self) -> tuple[int, int, int]:
        self.step("1. Packages")
        parent = self.one("SELECT Package_ID FROM t_package WHERE Name=?", PARENT_PACKAGE)
        if parent is None:
            raise SystemExit(f"package {PARENT_PACKAGE} niet gevonden")
        pid = parent["Package_ID"]
        existing = self.one("SELECT Package_ID FROM t_package WHERE Parent_ID=? AND Name=?", pid, PACKAGE)
        if existing:
            dom = existing["Package_ID"]
            dia = self.one("SELECT Package_ID FROM t_package WHERE Parent_ID=? AND Name='Diagram'", dom)["Package_ID"]
            mdl = self.one("SELECT Package_ID FROM t_package WHERE Parent_ID=? AND Name=?", dom, MODEL_PACKAGE)["Package_ID"]
            self.say(f"al gedaan: {PACKAGE} ({dom}), Diagram ({dia}), {MODEL_PACKAGE} ({mdl})")
            return dom, dia, mdl
        tpos = (self.one("SELECT MAX(TPos) FROM t_package WHERE Parent_ID=?", pid)[0] or 0) + 1
        ids = []
        for tpl_ref, name, parent_id, note in ((TPL_PKG_DOMEIN, PACKAGE, pid, PACKAGE_NOTE),
                                               (TPL_PKG_DIAGRAM, "Diagram", None, ""),
                                               (TPL_PKG_MODEL, MODEL_PACKAGE, None, PACKAGE_NOTE)):
            parent_id = parent_id if parent_id is not None else ids[0]
            p = self.row("t_package", "ea_guid", tpl_ref)
            guid = new_guid()
            pvals = {k: p[k] for k in p.keys() if k != "Package_ID"}
            pvals.update({"Name": name, "Parent_ID": parent_id, "Notes": note, "ea_guid": guid,
                          "CreatedDate": self.now, "ModifiedDate": self.now, "LastLoadDate": self.now,
                          "LastSaveDate": self.now, "Version": "1.0", "TPos": tpos if name == PACKAGE else 0})
            new_pid = self.insert("t_package", pvals)
            o = self.row("t_object", "ea_guid", tpl_ref)
            ovals = {k: o[k] for k in o.keys() if k != "Object_ID"}
            ovals.update({"Name": name, "Note": note, "Package_ID": parent_id, "PDATA1": str(new_pid), "ea_guid": guid,
                          "Author": AUTHOR, "Version": "1.0", "CreatedDate": self.now, "ModifiedDate": self.now,
                          "StyleEx": ""})
            new_oid = self.insert("t_object", ovals)
            tags = self.copy_tags(o["Object_ID"], new_oid, {"Release": RELEASE, "Datum opname": DATUM_OPNAME,
                                                             "Herkomst": HERKOMST})
            xref = self.copy_xref(o["ea_guid"], guid)
            ids.append(new_pid)
            self.say(f"aangemaakt: package {name} ({new_pid}; {tags} tags, {xref} xref, stereotype {o['Stereotype'] or '-'})")
        return ids[0], ids[1], ids[2]

    # -- 2. enumeratie ---------------------------------------------------------------------
    def enumeration(self, model_pid: int) -> None:
        self.step("2. Enumeratie Teamrol")
        name, note, literals = ENUM
        existing = self.one("SELECT Object_ID, ea_guid FROM t_object WHERE Package_ID=? AND Name=?", model_pid, name)
        if existing:
            self.ids[name], self.guids[name] = existing["Object_ID"], existing["ea_guid"]
            self.say(f"al gedaan: {name}")
            return
        tpl = self.row("t_object", "ea_guid", TPL_ENUM)
        guid = new_guid()
        vals = {k: tpl[k] for k in tpl.keys() if k != "Object_ID"}
        vals.update({"Name": name, "Note": note, "Package_ID": model_pid, "ea_guid": guid, "Author": AUTHOR,
                     "Version": "1.0", "CreatedDate": self.now, "ModifiedDate": self.now})
        oid = self.insert("t_object", vals)
        tags = self.copy_tags(tpl["Object_ID"], oid, {"Datum opname": DATUM_OPNAME, "Herkomst": HERKOMST})
        xref = self.copy_xref(tpl["ea_guid"], guid)
        lit = self.row("t_attribute", "ea_guid", TPL_LITERAL)
        lit_tags = self.all("SELECT Property, VALUE, NOTES FROM t_attributetag WHERE ElementID=?", lit["ID"])
        for pos, literal in enumerate(literals):
            lvals = {k: lit[k] for k in lit.keys() if k != "ID"}
            lvals.update({"Object_ID": oid, "Name": literal, "Pos": pos, "Notes": "", "ea_guid": new_guid()})
            lid = self.insert("t_attribute", lvals)
            for t in lit_tags:
                self.insert("t_attributetag", {"ElementID": lid, "Property": t["Property"], "VALUE": t["VALUE"],
                                               "NOTES": t["NOTES"], "ea_guid": new_guid()})
            self.copy_xref(lit["ea_guid"], lvals["ea_guid"])
        self.ids[name], self.guids[name] = oid, guid
        self.say(f"aangemaakt: {name} met {len(literals)} waarden ({tags} tags, {xref} xref)")

    # -- 3. objecttypen en attributen -----------------------------------------------------
    def classes(self, model_pid: int) -> None:
        self.step("3. Objecttypen en attributen")
        tpl = self.row("t_object", "ea_guid", TPL_CLASS)
        attr_tpl = self.row("t_attribute", "ea_guid", TPL_ATTR)
        attr_tags = self.all("SELECT Property, VALUE, NOTES FROM t_attributetag WHERE ElementID=? ORDER BY PropertyID", attr_tpl["ID"])
        med = self.row("t_object", "ea_guid", MEDEWERKER)
        self.ids["Medewerker"], self.guids["Medewerker"] = med["Object_ID"], med["ea_guid"]
        for name, (note, attrs) in CLASSES.items():
            existing = self.one("SELECT Object_ID, ea_guid FROM t_object WHERE Package_ID=? AND Name=?", model_pid, name)
            if existing:
                oid, guid = existing["Object_ID"], existing["ea_guid"]
                self.say(f"al gedaan: {name}")
            else:
                guid = new_guid()
                vals = {k: tpl[k] for k in tpl.keys() if k != "Object_ID"}
                vals.update({"Name": name, "Note": note, "Package_ID": model_pid, "ea_guid": guid, "Author": AUTHOR,
                             "Version": "1.0", "CreatedDate": self.now, "ModifiedDate": self.now})
                oid = self.insert("t_object", vals)
                self.copy_tags(tpl["Object_ID"], oid, {"Datum opname": DATUM_OPNAME, "Herkomst": HERKOMST})
                self.copy_xref(tpl["ea_guid"], guid)
                self.say(f"aangemaakt: «Objecttype» {name}")
            self.ids[name], self.guids[name] = oid, guid
            pos = (self.one("SELECT MAX(Pos) FROM t_attribute WHERE Object_ID=?", oid)[0]
                   if self.one("SELECT 1 FROM t_attribute WHERE Object_ID=?", oid) else -1) + 1
            added = []
            for aname, dtype, length, anote in attrs:
                if self.one("SELECT 1 FROM t_attribute WHERE Object_ID=? AND Name=?", oid, aname):
                    continue
                dt_id = self.ids[dtype] if dtype == ENUM[0] else self.datatype_id(dtype)
                avals = {k: attr_tpl[k] for k in attr_tpl.keys() if k != "ID"}
                avals.update({"Object_ID": oid, "Name": aname, "Type": dtype, "Classifier": str(dt_id), "Length": length,
                              "Notes": anote, "Pos": pos, "Default": "", "Style": "", "ea_guid": new_guid()})
                pos += 1
                aid = self.insert("t_attribute", avals)
                overrides = {"Lengte": str(length) if length else "", "Herkomst": HERKOMST,
                             "Datum opname": DATUM_OPNAME, "Mogelijk geen waarde": "Ja"}
                for t in attr_tags:
                    self.insert("t_attributetag", {"ElementID": aid, "Property": t["Property"],
                                                   "VALUE": overrides.get(t["Property"], t["VALUE"]),
                                                   "NOTES": t["NOTES"], "ea_guid": new_guid()})
                self.copy_xref(attr_tpl["ea_guid"], avals["ea_guid"])
                added.append(f"{aname} : {dtype}" + (f" ({length})" if length else ""))
            if added:
                self.say(f"    attributen: {', '.join(added)}")

    # -- 4. relaties -------------------------------------------------------------------------
    def relations(self) -> None:
        self.step("4. Relaties")
        tpl = self.row("t_connector", "ea_guid", TPL_CONNECTOR)
        for src, name, dst, scard, dcard in RELATIONS:
            sid, did = self.ids[src], self.ids[dst]
            existing = self.one("SELECT Connector_ID FROM t_connector WHERE Start_Object_ID=? AND End_Object_ID=? "
                                "AND Connector_Type='Association' AND Name=?", sid, did, name)
            if existing:
                self.connectors.append((existing["Connector_ID"], src, dst))
                continue
            vals = {k: tpl[k] for k in tpl.keys() if k != "Connector_ID"}
            vals.update({"Name": name, "Notes": "", "Direction": "Source -> Destination", "SourceCard": scard,
                         "DestCard": dcard, "Btm_Start_Label": scard, "Btm_End_Label": dcard, "Top_Mid_Label": name,
                         "Start_Object_ID": sid, "End_Object_ID": did, "DiagramID": 0, "ea_guid": new_guid()})
            cid = self.insert("t_connector", vals)
            self.copy_xref(tpl["ea_guid"], vals["ea_guid"])
            self.connectors.append((cid, src, dst))
            self.say(f"{src} {scard} '{name}' -> {dst} {dcard}")
        self.say(f"{len(self.connectors)} relaties aanwezig")

    # -- 5. diagram --------------------------------------------------------------------------
    def diagram(self, diagram_pid: int) -> None:
        self.step("5. Diagram")
        existing = self.one("SELECT Diagram_ID FROM t_diagram WHERE Package_ID=? AND Name=?", diagram_pid, DIAGRAM)
        if existing:
            did = existing["Diagram_ID"]
            self.say(f"al gedaan: diagram {DIAGRAM} ({did})")
        else:
            tpl = self.row("t_diagram", "ea_guid", TPL_DIAGRAM)
            vals = {k: tpl[k] for k in tpl.keys() if k != "Diagram_ID"}
            vals.update({"Package_ID": diagram_pid, "ParentID": 0, "Name": DIAGRAM, "Author": AUTHOR, "Version": "1.0",
                         "CreatedDate": self.now, "ModifiedDate": self.now, "ea_guid": new_guid(),
                         "PDATA": (tpl["PDATA"] or "").replace("HideAtts=1", "HideAtts=0"),
                         "StyleEx": "SaveTag=" + new_duid() + ";" + (tpl["StyleEx"] or "").split(";", 1)[1]})
            did = self.insert("t_diagram", vals)
            self.say(f"aangemaakt: diagram {DIAGRAM} ({did})")
        duids: dict[str, str] = {}
        seq = (self.one("SELECT MAX(Sequence) FROM t_diagramobjects WHERE Diagram_ID=?", did)[0] or 0) + 1
        placed = 0
        for name, (col, rw) in LAYOUT.items():
            oid = self.ids[name]
            r = self.one("SELECT ObjectStyle FROM t_diagramobjects WHERE Diagram_ID=? AND Object_ID=?", did, oid)
            if r:
                duids[name] = r["ObjectStyle"].split("DUID=")[1].split(";")[0]
                continue
            n_attrs = self.one("SELECT COUNT(*) FROM t_attribute WHERE Object_ID=?", oid)[0]
            height = max(60, 46 + 17 * n_attrs)
            duid = new_duid()
            self.insert("t_diagramobjects", {"Diagram_ID": did, "Object_ID": oid, "RectTop": ROW_Y[rw],
                                             "RectLeft": COL_X[col], "RectRight": COL_X[col] + WIDTH,
                                             "RectBottom": ROW_Y[rw] - height, "Sequence": seq,
                                             "ObjectStyle": "DUID=" + duid + ";" + DIAGRAM_OBJECT_STYLE})
            seq += 1
            duids[name] = duid
            placed += 1
        linked = 0
        for cid, src, dst in self.connectors:
            if self.one("SELECT 1 FROM t_diagramlinks WHERE DiagramID=? AND ConnectorID=?", did, cid):
                continue
            self.insert("t_diagramlinks", {
                "DiagramID": did, "ConnectorID": cid,
                "Geometry": "SX=0;SY=0;EX=0;EY=0;EDGE=1;$LLB=;LLT=;LMT=;LMB=;LRT=;LRB=;IRHS=;ILHS=;",
                "Style": f"Mode=3;EOID={duids[dst]};SOID={duids[src]};Color=-1;LWidth=0;", "Hidden": 0, "Path": ""})
            linked += 1
        self.say(f"{placed} elementen geplaatst, {linked} relaties als link toegevoegd")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("qea", help="pad naar de .qea (SQLite) van Enterprise Architect")
    ap.add_argument("--apply", action="store_true", help="wijzigingen vastleggen (zonder: dry-run op een kopie)")
    args = ap.parse_args()

    target = args.qea
    if not args.apply:
        tmp = tempfile.NamedTemporaryFile(prefix="add_samenwerkomgeving-", suffix=".qea", delete=False)
        tmp.close()
        shutil.copyfile(args.qea, tmp.name)
        target = tmp.name
    conn = sqlite3.connect(target, isolation_level=None)
    conn.execute("BEGIN")
    b = Builder(conn)
    try:
        dom, dia, mdl = b.packages()
        b.enumeration(mdl)
        b.classes(mdl)
        b.relations()
        b.diagram(dia)
    except Exception:
        conn.execute("ROLLBACK")
        raise

    print(f"\n{b.changes} gewijzigde rijen; {len(b.warnings)} waarschuwing(en)")
    if args.apply:
        conn.execute("COMMIT")
        ok = conn.execute("PRAGMA integrity_check").fetchone()[0]
        print(f"TOEGEPAST en vastgelegd in {args.qea}; integrity_check: {ok}")
        return 0 if ok == "ok" else 1
    conn.execute("ROLLBACK")
    conn.close()
    pathlib.Path(target).unlink(missing_ok=True)
    print("DRY-RUN op een tijdelijke kopie: niets opgeslagen (gebruik --apply om door te voeren)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
