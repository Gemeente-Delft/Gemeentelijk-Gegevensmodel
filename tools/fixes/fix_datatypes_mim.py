#!/usr/bin/env python3
"""Omzetting van de attribuuttypen in de EA-repository van het GGM naar de MIM-primitieven (nov 2026).

Stand voor de omzetting: de typetekst van de attributen (t_attribute.Type) is bij ruim 2.300
attributen nog de RSGB/StUF-notatie (AN80, N2, int, datum, Text, string ...), terwijl de classifier
meestal al naar het pakket 'MIM11 Primitieve datatypen' wijst. De lengte staat in de typetekst en in
het EA-veld Length, bijna nooit in de MIM-tag Lengte. Alle generatoren (crunch_uml en de
codegeneratietemplates) werken op de typetekst. De mapping staat in tools/mim-datatypes-mapping.md.

Wat het script doet, per attribuut (enumeratiewaarden slaat het over):
  - typetekst en classifier naar het MIM-datatype volgens de mapping; typetekst gelijk aan de
    classifiernaam waar die afwijkt (ook GML3: Point -> GM_Point);
  - tag Lengte als kaal getal (maximumlengte), bij Decimal 'cijfers,decimalen'; de EA-velden Length,
    Precision en Scale gevuld voor de DDL-templates; een bestaande '50.0' wordt '50';
  - tag Eenheid (EUR bij bedragen), Formeel patroon (GUID, e-mail, IBAN, telefoonnummer) en
    Mogelijk geen waarde = Ja bij attributen die nu de enumeratie Boolean (Ja/Nee/Onbekend/Leeg) hebben;
  - INDIC en StdIndJN blijven een eigen enumeratie (keuze beheerder, 4 nov 2026): StdIndJN bestaat,
    INDIC wordt aangemaakt in het pakket Enumeratiesoort met de waarden Ja en Nee;
  - Time wordt het eigen primitieve datatype Tijd, aangemaakt in GGM Datatypes.

Wat het script niet doet (apart, na controle in EA): de dan onverwezen datatypen verwijderen
(Bedrag, Dag, Jaar, Maand, Email, GUID, IBAN, Telefoonnummer, Geldbedrag, CompositeID, de twee
enumeraties Boolean), NEN3610ID herstructureren tot gestructureerd datatype, de stereotypen
«Primitief datatype» zetten, en de losse typenamen zonder classifier (IMBOR/BOR) koppelen. Het
rapport noemt ze wel, met het aantal resterende verwijzingen.

Standaard dry-run: leest de .qea alleen (mode=ro) en schrijft een rapport (--rapport) en een CSV met
alle geplande wijzigingen (--csv). Met --apply voert het de wijzigingen in één transactie door:
sluit Enterprise Architect en maak eerst een back-up. Idempotent: een tweede run meldt 0.

Gebruik:
  python3 -I tools/fixes/fix_datatypes_mim.py "v3.0.0/Gemeentelijk Gegevensmodel.qea" \
      --rapport tools/mim-datatypes-dryrun.md --csv /tmp/mim-datatypes-detail.csv
  python3 -I tools/fixes/fix_datatypes_mim.py "v3.0.0/Gemeentelijk Gegevensmodel.qea" --apply
"""
import argparse
import collections
import csv
import re
import sqlite3
import sys
import uuid
from dataclasses import dataclass, field
from datetime import datetime

MIM11_PKG = "MIM11 Primitieve datatypen"
GGM_PKG = "GGM Datatypes"
GML_PKG = "GML3"
INDIC_PKG = "Enumeratiesoort"  # RSGB-enumeraties (het pakket met de enumeratie Boolean van RSGB)
INDIC_NOTE = "Indicatie ja/nee (RSGB/StUF-type INDIC)."
INDIC_LITERALS = ("Ja", "Nee")
TIJD_NOTE = "Een tijdstip op de dag in uren, minuten en seconden (ISO 8601, uu:mm:ss)."

PATROON = {
    "guid": r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
    "email": r"^[^@\s]+@[^@\s]+\.[^@\s]+$",
    "iban": r"^[A-Z]{2}[0-9]{2}[A-Z0-9]{1,30}$",
    "telefoonnummer": r"^[0-9]{10}$",
}
GEO = {"point": "GM_Point", "punt": "GM_Point", "spatial": "GM_Point", "surface": "GM_Surface",
       "vlak": "GM_Surface", "multisurface": "GM_MultiSurface", "curve": "GM_Curve", "lijn": "GM_Curve",
       "multicurve": "GM_MultiCurve", "multipoint": "GM_MultiPoint", "object": "GM_Object",
       "polygon": "GM_Polygon", "linestring": "GM_LineString", "multilinestring": "GM_MultiLineString",
       "geometry": "GM_Geometry"}
CHAR = {"an", "text", "tekst", "string", "varchar", "char", "characterstring"}
BUITEN_SCOPE = "buiten scope: losse typenaam zonder classifier"
TE_VERWIJDEREN = ("Bedrag", "Dag", "Jaar", "Maand", "Email", "GUID", "IBAN", "Telefoonnummer",
                  "Geldbedrag", "CompositeID", "Boolean")


def new_guid() -> str:
    return "{" + str(uuid.uuid4()).upper() + "}"


def norm_len(v):
    """'50.0' -> '50'; '10,2' blijft; leeg -> None."""
    if v is None:
        return None
    s = str(v).strip()
    if not s:
        return None
    if re.fullmatch(r"\d+\.0+", s):
        s = s.split(".")[0]
    return s


def as_int(v):
    try:
        return int(str(v).strip()) if str(v).strip() else 0
    except ValueError:
        return 0


@dataclass
class Plan:
    doel: str
    type: str | None = None           # nieuwe typetekst (None = ongewijzigd)
    classifier: object = None         # Object_ID, 'INDIC'/'Tijd' (aan te maken) of None = ongewijzigd
    lengte: str | None = None         # gewenste tag Lengte (None = laten zoals hij is, wel normaliseren)
    tags: dict = field(default_factory=dict)  # overige tags: Property -> VALUE
    notitie: str = ""
    handmatig: bool = False


class Omzetter:
    def __init__(self, conn: sqlite3.Connection):
        self.c = conn
        self.c.row_factory = sqlite3.Row
        self.now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.changes = 0
        self.warnings: list[str] = []
        self.created: dict[str, int] = {}
        self._load()

    # -- inlezen --------------------------------------------------------------------------
    def _load(self) -> None:
        self.pkg = {r["Package_ID"]: r["Name"] for r in self.c.execute("SELECT Package_ID, Name FROM t_package")}
        self.obj = {r["Object_ID"]: r for r in self.c.execute(
            "SELECT Object_ID, Name, Object_Type, Package_ID, ea_guid FROM t_object "
            "WHERE Object_Type IN ('Class','DataType','Enumeration')")}
        by_pkg = collections.defaultdict(dict)
        for o in self.obj.values():
            by_pkg[self.pkg.get(o["Package_ID"])][o["Name"]] = o["Object_ID"]
        self.mim = by_pkg[MIM11_PKG]
        self.ggm = by_pkg[GGM_PKG]
        self.gml = by_pkg[GML_PKG]
        missing = [n for n in ("CharacterString", "Integer", "Decimal", "Boolean", "Date", "DateTime",
                               "Year", "Day", "Month", "URI") if n not in self.mim]
        missing += [n for n in ("Blob", "OnvolledigeDatum", "NEN3610ID") if n not in self.ggm]
        if missing:
            raise SystemExit(f"datatypen niet gevonden in het model: {missing}")
        enums = {o["Object_ID"]: o for o in self.obj.values() if o["Object_Type"] == "Enumeration"}
        self.boolean_enums = {i for i, o in enums.items() if o["Name"] == "Boolean"}
        std = [i for i, o in enums.items() if o["Name"] == "StdIndJN"]
        if len(std) != 1:
            raise SystemExit(f"verwacht precies één enumeratie StdIndJN, gevonden {len(std)}")
        self.stdindjn = std[0]
        indic = [i for i, o in enums.items() if o["Name"] == "INDIC"]
        self.indic = indic[0] if indic else "INDIC"
        self.tijd = self.ggm.get("Tijd", "Tijd")
        self.byname = collections.defaultdict(list)
        for i, o in self.obj.items():
            self.byname[o["Name"].strip().casefold()].append(i)
        self.attrs = self.c.execute(
            "SELECT a.ID, a.ea_guid, a.Object_ID, a.Name, a.Type, a.Classifier, a.Length, a.Precision, a.Scale, "
            "o.Name AS owner, p.Name AS pkg FROM t_attribute a "
            "JOIN t_object o ON o.Object_ID=a.Object_ID JOIN t_package p ON p.Package_ID=o.Package_ID "
            "WHERE o.Object_Type <> 'Enumeration' ORDER BY p.Name, o.Name, a.Pos, a.Name").fetchall()
        self.tag = {}
        for r in self.c.execute("SELECT PropertyID, ElementID, Property, VALUE FROM t_attributetag "
                                "WHERE Property IN ('Lengte','Eenheid','Formeel patroon','Mogelijk geen waarde')"):
            self.tag[(r["ElementID"], r["Property"])] = (r["PropertyID"], r["VALUE"])
        self.tagged = {r[0] for r in self.c.execute("SELECT DISTINCT ElementID FROM t_attributetag")}

    def cls_name(self, cid) -> str:
        if cid in ("INDIC", "Tijd"):
            return f"{cid} (nieuw)"
        o = self.obj.get(cid) if cid else None
        return o["Name"] if o else ""

    # -- de mapping -----------------------------------------------------------------------
    def plan(self, a) -> Plan:
        t = (a["Type"] or "").strip()
        n = t.casefold()
        cid0 = as_int(a["Classifier"])  # t_attribute.Classifier is tekst ('37', '0', '')
        cur = self.obj.get(cid0) if cid0 else None
        ea_len = as_int(a["Length"])
        tag_len = norm_len((self.tag.get((a["ID"], "Lengte")) or (None, None))[1])
        inherited = str(ea_len) if ea_len else tag_len  # lengte die al ergens staat

        def mim(name, doel=None, lengte=None, **tags):
            return Plan(doel or name, name, self.mim[name], lengte, dict(tags))

        def cs(doel="CharacterString", lengte=None, **tags):
            return mim("CharacterString", doel, lengte, **tags)

        if n in GEO or n.startswith("gm_"):
            name = GEO.get(n) or next((k for k in self.gml if k.casefold() == n), None)
            if name in self.gml:
                return Plan("GM_* (GML3, ongewijzigd)", name, self.gml[name])
        if m := re.fullmatch(r"an\s*(\d+)", n):
            return cs("CharacterString + Lengte", m.group(1))
        if n == "a1":
            return cs("CharacterString + Lengte", "1")
        if n in CHAR:
            return cs("CharacterString + Lengte" if inherited else "CharacterString (zonder lengte)", inherited)
        if m := re.fullmatch(r"n\s*(\d+)", n):
            return mim("Integer", "Integer + Lengte", m.group(1))
        if m := re.fullmatch(r"n\s*(\d+)[.,](\d+)", n):
            return mim("Decimal", "Decimal + Lengte", f"{m.group(1)},{m.group(2)}")
        if n in {"int", "integer", "number"}:
            return mim("Integer", "Integer + Lengte" if inherited else "Integer", inherited)
        if n == "ntatie":
            return mim("Decimal", "Decimal", notitie="afgekapte typenaam (oriëntatie in graden), aangenomen Decimal") if False else \
                Plan("Decimal", "Decimal", self.mim["Decimal"], None, {}, "afgekapte typenaam (oriëntatie), aangenomen Decimal")
        if n in {"date", "datum"}:
            return mim("Date")
        if n in {"datetime", "datumtijd"}:
            return mim("DateTime")
        if n == "time":
            return Plan("Tijd (eigen primitief datatype)", "Tijd", self.tijd)
        if n in {"boolean", "bool"}:
            if cur and cur["Object_ID"] in self.boolean_enums:
                return Plan("Boolean (was enumeratie Ja/Nee/Onbekend/Leeg)", "Boolean", self.mim["Boolean"],
                            None, {"Mogelijk geen waarde": "Ja"})
            return mim("Boolean")
        if n == "indic":
            return Plan("INDIC (eigen enumeratie)", "INDIC", self.indic)
        if n == "stdindjn":
            return Plan("StdIndJN (eigen enumeratie)", "StdIndJN", self.stdindjn)
        if n in {"double", "decimal", "real"}:
            return mim("Decimal")
        if n in {"bedrag", "geldbedrag"} or (n == "2" and a["owner"] == "TypeBedrag"):
            return mim("Decimal", "Decimal 10,2 EUR (was Bedrag/Geldbedrag)", "10,2", Eenheid="EUR")
        if n == "1" and a["owner"] == "TypeLabelpositie":
            return Plan("Decimal", "Decimal", self.mim["Decimal"], None, {}, "typetekst '1' (hoek), aangenomen Decimal")
        if n == "guid":
            return cs("CharacterString 36 + patroon (was GUID)", "36", **{"Formeel patroon": PATROON["guid"]})
        if n == "email":
            return cs("CharacterString + patroon (was Email/IBAN/Telefoonnummer)", inherited,
                      **{"Formeel patroon": PATROON["email"]})
        if n == "iban":
            return cs("CharacterString + patroon (was Email/IBAN/Telefoonnummer)", "34",
                      **{"Formeel patroon": PATROON["iban"]})
        if n == "telefoonnummer":
            return cs("CharacterString + patroon (was Email/IBAN/Telefoonnummer)", "10",
                      **{"Formeel patroon": PATROON["telefoonnummer"]})
        if n in {"url", "uri"}:
            return mim("URI")
        if n == "jaar":
            return mim("Year", "Year (was Jaar)")
        if n == "dag":
            return mim("Day", "Day (was Dag)")
        if n == "maand":
            return mim("Month", "Month (was Maand)")
        if n in {"blob", "image"}:
            return Plan("Blob (eigen primitief datatype)", "Blob", self.ggm["Blob"])
        if n == "onvolledigedatum":
            return Plan("OnvolledigeDatum (eigen primitief datatype)", "OnvolledigeDatum", self.ggm["OnvolledigeDatum"])
        if n in {"nen3610id", "compositeid"}:
            return Plan("NEN3610ID (gestructureerd datatype, herstructurering apart)", "NEN3610ID",
                        self.ggm["NEN3610ID"])
        if n == "enum":
            return Plan("handmatig", handmatig=True, notitie="typetekst 'Enum' zonder enumeratie")
        if cur:
            if cur["Name"] != t:
                return Plan("typetekst gelijk aan classifier", cur["Name"], None, None, {},
                            f"{cur['Object_Type']} in {self.pkg.get(cur['Package_ID'])}")
            return Plan("ongewijzigd (enumeratie, objecttype of datatype als type)")
        if not n:
            return Plan("handmatig", handmatig=True, notitie="leeg type zonder classifier")
        cands = self.byname.get(n, [])
        hint = "; ".join(f"{self.obj[i]['Object_Type']} {self.obj[i]['Name']} in {self.pkg.get(self.obj[i]['Package_ID'])}"
                         for i in cands[:3])
        return Plan(BUITEN_SCOPE, notitie=f"gelijknamig: {hint}" if hint else "")

    # -- verschil tussen plan en huidige stand ----------------------------------------------
    def diff(self, a, p: Plan) -> list[tuple]:
        d = []
        if p.type is not None and p.type != (a["Type"] or ""):
            d.append(("Type", a["Type"] or "", p.type))
        if p.classifier is not None:
            cur = as_int(a["Classifier"])
            if isinstance(p.classifier, str) or p.classifier != cur:
                d.append(("Classifier", self.cls_name(cur) or str(cur), self.cls_name(p.classifier)))
        raw = self.tag.get((a["ID"], "Lengte"))
        want = p.lengte if p.lengte is not None else norm_len(raw[1] if raw else None)
        if want is not None and want != ((raw[1] or "") if raw else None):
            d.append(("tag Lengte" if raw else "tag Lengte (nieuwe rij)", raw[1] if raw else "", want))
        for prop, val in p.tags.items():
            r = self.tag.get((a["ID"], prop))
            if val != ((r[1] or "") if r else None):
                d.append((f"tag {prop}" if r else f"tag {prop} (nieuwe rij)", r[1] if r else "", val))
        if want and re.fullmatch(r"\d+", want) and as_int(a["Length"]) != int(want):
            d.append(("Length", str(as_int(a["Length"])), want))
        if want and (m := re.fullmatch(r"(\d+),(\d+)", want)):
            if as_int(a["Precision"]) != int(m.group(1)):
                d.append(("Precision", str(as_int(a["Precision"])), m.group(1)))
            if as_int(a["Scale"]) != int(m.group(2)):
                d.append(("Scale", str(as_int(a["Scale"])), m.group(2)))
        return d

    def plans(self):
        for a in self.attrs:
            p = self.plan(a)
            yield a, p, self.diff(a, p)

    # -- rapport --------------------------------------------------------------------------
    def rapport(self, path: str | None, csv_path: str | None, mode: str) -> None:
        rows = list(self.plans())
        per_doel = collections.OrderedDict()
        bron = collections.defaultdict(collections.Counter)
        handmatig, buiten, conflict, naamhint = [], collections.defaultdict(collections.Counter), [], collections.Counter()
        kinds = ("Type", "Classifier", "tag Lengte", "tag Lengte (nieuwe rij)", "Length", "Precision", "Scale")
        planned_cls = collections.Counter()
        for a, p, d in rows:
            s = per_doel.setdefault(p.doel, collections.Counter())
            s["attributen"] += 1
            if d:
                s["gewijzigd"] += 1
            for k in kinds:
                if any(x[0] == k for x in d):
                    s[k] += 1
            if any(x[0].startswith("tag ") and not x[0].startswith("tag Lengte") for x in d):
                s["andere tags"] += 1
            bron[p.doel][a["Type"] or "(leeg)"] += 1
            if p.handmatig:
                handmatig.append((a, p))
            if p.doel == BUITEN_SCOPE:
                buiten[a["pkg"]][a["Type"]] += 1
                if p.notitie:
                    naamhint[(a["Type"], p.notitie)] += 1
            if p.lengte and re.fullmatch(r"\d+", p.lengte):
                raw = self.tag.get((a["ID"], "Lengte"))
                if raw and norm_len(raw[1]) and norm_len(raw[1]) != p.lengte:
                    conflict.append((a, raw[1], p.lengte, "tag Lengte"))
                if as_int(a["Length"]) and as_int(a["Length"]) != int(p.lengte):
                    conflict.append((a, str(a["Length"]), p.lengte, "EA Length"))
            cid = p.classifier if p.classifier is not None else as_int(a["Classifier"])
            planned_cls[cid] += 1
        zonder_tags = sum(1 for a, p, d in rows if a["ID"] not in self.tagged)

        out = []
        w = out.append
        w(f"# Omzetting datatypes naar MIM: {mode}\n")
        w(f"*{self.now}, script tools/fixes/fix_datatypes_mim.py, mapping in tools/mim-datatypes-mapping.md.*\n")
        n_all = len(rows)
        n_chg = sum(1 for _, _, d in rows if d)
        w(f"Attributen (zonder enumeratiewaarden): {n_all}. Met een geplande wijziging: {n_chg}. "
          f"Handmatig te beoordelen: {len(handmatig)}. Buiten scope: {per_doel.get(BUITEN_SCOPE, {}).get('attributen', 0)}. "
          f"Attributen zonder enige MIM-tag: {zonder_tags}.\n")
        w("## Samenvatting per doel\n")
        w("| Doel | Attributen | Gewijzigd | Typetekst | Classifier | Tag Lengte | Lengte-rij nieuw | Andere tags | EA Length/Prec/Scale |")
        w("| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |")
        for doel, s in sorted(per_doel.items(), key=lambda x: -x[1]["attributen"]):
            w(f"| {doel} | {s['attributen']} | {s['gewijzigd']} | {s['Type']} | {s['Classifier']} | {s['tag Lengte']} | "
              f"{s['tag Lengte (nieuwe rij)']} | {s['andere tags']} | {s['Length'] + s['Precision'] + s['Scale']} |")
        w("\n## Brontypen per doel\n")
        for doel, cnt in sorted(bron.items(), key=lambda x: -sum(x[1].values())):
            top = ", ".join(f"{t} ×{n}" for t, n in cnt.most_common(12))
            extra = f" … (+{len(cnt) - 12} andere)" if len(cnt) > 12 else ""
            w(f"- **{doel}**: {top}{extra}")
        w("\n## Nieuwe en vervallende modelelementen\n")
        w(f"- Aan te maken: enumeratie **INDIC** ({'/'.join(INDIC_LITERALS)}) in pakket {INDIC_PKG}"
          f"{' (bestaat al)' if not isinstance(self.indic, str) else ''}; eigen primitief datatype **Tijd** in {GGM_PKG}"
          f"{' (bestaat al)' if not isinstance(self.tijd, str) else ''}.")
        w("- Na de omzetting onverwezen (verwijderen gebeurt apart, na controle in EA):\n")
        w("| Element | Pakket | Attributen nu | Attributen na omzetting | Op diagrammen | Connectors |")
        w("| :--- | :--- | ---: | ---: | ---: | ---: |")
        for o in sorted(self.obj.values(), key=lambda o: o["Name"]):
            if o["Name"] not in TE_VERWIJDEREN:
                continue
            if o["Name"] == "Boolean" and o["Object_ID"] not in self.boolean_enums:
                continue
            if o["Name"] in ("Geldbedrag", "CompositeID") and o["Object_Type"] != "DataType":
                continue
            if o["Name"] in self.ggm and self.ggm[o["Name"]] != o["Object_ID"] and o["Name"] != "Boolean":
                continue
            oid = o["Object_ID"]
            now_n = self.c.execute("SELECT COUNT(*) FROM t_attribute WHERE Classifier=?", (oid,)).fetchone()[0]
            dia = self.c.execute("SELECT COUNT(*) FROM t_diagramobjects WHERE Object_ID=?", (oid,)).fetchone()[0]
            con = self.c.execute("SELECT COUNT(*) FROM t_connector WHERE Start_Object_ID=? OR End_Object_ID=?",
                                 (oid, oid)).fetchone()[0]
            w(f"| {o['Object_Type']} {o['Name']} | {self.pkg.get(o['Package_ID'])} | {now_n} | {planned_cls.get(oid, 0)} | {dia} | {con} |")
        w("- Apart te doen: NEN3610ID herstructureren tot «Gestructureerd datatype» (namespace, lokaalID, versie) "
          "met CompositeID erin; stereotype «Primitief datatype» op Blob, OnvolledigeDatum en Tijd.")
        w(f"\n## Handmatig te beoordelen ({len(handmatig)})\n")
        for a, p in handmatig:
            w(f"- {a['pkg']} › {a['owner']}.{a['Name']} : `{a['Type']}` — {p.notitie}")
        w(f"\n## Lengteconflicten ({len(conflict)})\n")
        w("Gevallen waar de bestaande tag Lengte of het EA-veld Length afwijkt van de lengte uit de typetekst; "
          "de typetekst wint.\n")
        for a, oud, nieuw, waar in conflict:
            w(f"- {a['pkg']} › {a['owner']}.{a['Name']} : `{a['Type']}`, {waar} {oud} → {nieuw}")
        n_buiten = sum(sum(c.values()) for c in buiten.values())
        w(f"\n## Buiten scope: losse typenamen zonder classifier ({n_buiten} attributen)\n")
        w("Niet omgezet; apart te koppelen aan enumeraties (IMBOR-werk). Per pakket, met de typenamen:\n")
        for pkg, cnt in sorted(buiten.items(), key=lambda x: -sum(x[1].values())):
            w(f"- **{pkg}** ({sum(cnt.values())}): " + ", ".join(f"{t} ×{n}" for t, n in cnt.most_common()))
        if naamhint:
            w("\nTypenamen waarvoor een gelijknamig element bestaat (niet automatisch gekoppeld; controleer of het past):\n")
            for (t, hint), n in sorted(naamhint.items(), key=lambda x: -x[1]):
                w(f"- `{t}` ×{n}: {hint}")
        text = "\n".join(out) + "\n"
        if path:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(text)
            print(f"rapport geschreven: {path}")
        else:
            print(text)
        if csv_path:
            with open(csv_path, "w", encoding="utf-8", newline="") as fh:
                cw = csv.writer(fh, delimiter=";")
                cw.writerow(["ID", "ea_guid", "pakket", "klasse", "attribuut", "doel", "type_oud", "type_nieuw",
                             "classifier_oud", "classifier_nieuw", "lengte_tag_oud", "lengte_nieuw",
                             "overige_tags", "EA_velden", "notitie"])
                for a, p, d in rows:
                    dd = {x[0]: x for x in d}
                    raw = self.tag.get((a["ID"], "Lengte"))
                    cw.writerow([a["ID"], a["ea_guid"], a["pkg"], a["owner"], a["Name"], p.doel, a["Type"] or "",
                                 p.type or "", self.cls_name(as_int(a["Classifier"])), self.cls_name(p.classifier) if p.classifier is not None else "",
                                 raw[1] if raw else "", p.lengte if p.lengte is not None else (norm_len(raw[1]) if raw else ""),
                                 "; ".join(f"{k}={v}" for k, v in p.tags.items()),
                                 "; ".join(f"{k} {x[1]}→{x[2]}" for k, x in dd.items() if k in ("Length", "Precision", "Scale")),
                                 p.notitie])
            print(f"detail-CSV geschreven: {csv_path} ({len(rows)} rijen)")

    # -- doorvoeren -----------------------------------------------------------------------
    def run(self, sql: str, *params) -> int:
        n = self.c.execute(sql, params).rowcount
        self.changes += max(n, 0)
        return n

    def insert(self, table: str, vals: dict) -> int:
        cols = ", ".join(f'"{k}"' for k in vals)
        marks = ", ".join("?" for _ in vals)
        cur = self.c.execute(f'INSERT INTO {table} ({cols}) VALUES ({marks})', tuple(vals.values()))
        self.changes += 1
        return cur.lastrowid

    def _copy_object(self, template_id: int, name: str, note: str, package_id: int) -> int:
        tpl = self.c.execute("SELECT * FROM t_object WHERE Object_ID=?", (template_id,)).fetchone()
        vals = {k: tpl[k] for k in tpl.keys() if k != "Object_ID"}
        vals.update({"Name": name, "Note": note, "Package_ID": package_id, "ea_guid": new_guid(),
                     "CreatedDate": self.now, "ModifiedDate": self.now, "Author": "fix_datatypes_mim"})
        oid = self.insert("t_object", vals)
        for x in self.c.execute("SELECT * FROM t_xref WHERE upper(Client)=upper(?)", (tpl["ea_guid"],)).fetchall():
            xv = {k: x[k] for k in x.keys()}
            xv.update({"XrefID": new_guid(), "Client": vals["ea_guid"]})
            self.insert("t_xref", xv)
        for t in self.c.execute("SELECT * FROM t_objectproperties WHERE Object_ID=?", (template_id,)).fetchall():
            tv = {k: t[k] for k in t.keys() if k != "PropertyID"}
            tv.update({"Object_ID": oid, "ea_guid": new_guid()})
            self.insert("t_objectproperties", tv)
        return oid

    def ensure_created(self, key: str) -> int:
        if key in self.created:
            return self.created[key]
        if key == "INDIC":
            rsgb_bool = next((i for i in self.boolean_enums if self.pkg.get(self.obj[i]["Package_ID"]) == INDIC_PKG), None)
            pkg_id = self.obj[rsgb_bool]["Package_ID"] if rsgb_bool else self.obj[self.stdindjn]["Package_ID"]
            oid = self._copy_object(self.stdindjn, "INDIC", INDIC_NOTE, pkg_id)
            lits = self.c.execute("SELECT * FROM t_attribute WHERE Object_ID=? ORDER BY Pos", (self.stdindjn,)).fetchall()
            for pos, name in enumerate(INDIC_LITERALS):
                tpl = next((l for l in lits if l["Name"] == name), lits[0])
                av = {k: tpl[k] for k in tpl.keys() if k != "ID"}
                av.update({"Object_ID": oid, "Name": name, "Pos": pos, "ea_guid": new_guid(), "Notes": ""})
                aid = self.insert("t_attribute", av)
                for x in self.c.execute("SELECT * FROM t_xref WHERE upper(Client)=upper(?)", (tpl["ea_guid"],)).fetchall():
                    xv = {k: x[k] for k in x.keys()}
                    xv.update({"XrefID": new_guid(), "Client": av["ea_guid"]})
                    self.insert("t_xref", xv)
                for t in self.c.execute("SELECT * FROM t_attributetag WHERE ElementID=?", (tpl["ID"],)).fetchall():
                    tv = {k: t[k] for k in t.keys() if k != "PropertyID"}
                    tv.update({"ElementID": aid, "ea_guid": new_guid()})
                    self.insert("t_attributetag", tv)
            print(f"    aangemaakt: enumeratie INDIC ({'/'.join(INDIC_LITERALS)}) in {self.pkg.get(pkg_id)}, Object_ID {oid}")
        elif key == "Tijd":
            oid = self._copy_object(self.ggm["OnvolledigeDatum"], "Tijd", TIJD_NOTE, self.obj[self.ggm["OnvolledigeDatum"]]["Package_ID"])
            print(f"    aangemaakt: datatype Tijd in {GGM_PKG}, Object_ID {oid}")
        else:
            raise ValueError(key)
        self.created[key] = oid
        return oid

    def apply(self) -> None:
        touched = set()
        n_attr = 0
        for a, p, d in list(self.plans()):
            if not d or p.handmatig:
                continue
            n_attr += 1
            sets, vals = [], []
            for fld, _, new in d:
                if fld == "Type":
                    sets.append("Type=?"); vals.append(new)
                elif fld == "Classifier":
                    cid = self.ensure_created(p.classifier) if isinstance(p.classifier, str) else p.classifier
                    sets.append("Classifier=?"); vals.append(cid)
                elif fld in ("Length", "Precision", "Scale"):
                    sets.append(f"{fld}=?"); vals.append(int(new))
                elif fld.startswith("tag "):
                    prop = fld[4:].replace(" (nieuwe rij)", "")
                    r = self.tag.get((a["ID"], prop))
                    if r:
                        self.run("UPDATE t_attributetag SET VALUE=? WHERE PropertyID=?", new, r[0])
                    else:
                        self.insert("t_attributetag", {"ElementID": a["ID"], "Property": prop, "VALUE": new,
                                                       "NOTES": "", "ea_guid": new_guid()})
            if sets:
                self.run(f"UPDATE t_attribute SET {', '.join(sets)} WHERE ID=?", *vals, a["ID"])
            touched.add(a["Object_ID"])
        for oid in touched:
            self.run("UPDATE t_object SET ModifiedDate=? WHERE Object_ID=?", self.now, oid)
        print(f"    {n_attr} attributen bijgewerkt in {len(touched)} klassen")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("qea", help="pad naar de .qea (SQLite) van Enterprise Architect")
    ap.add_argument("--apply", action="store_true", help="wijzigingen vastleggen (zonder: dry-run, alleen lezen)")
    ap.add_argument("--rapport", help="markdown-rapport (zonder: naar het scherm)")
    ap.add_argument("--csv", help="CSV met alle geplande wijzigingen per attribuut")
    args = ap.parse_args()

    if not args.apply:
        conn = sqlite3.connect(f"file:{args.qea}?mode=ro", uri=True)
        o = Omzetter(conn)
        o.rapport(args.rapport, args.csv, "dry-run")
        conn.close()
        print("DRY-RUN: de .qea is alleen gelezen (gebruik --apply om door te voeren)")
        return 0

    conn = sqlite3.connect(args.qea, isolation_level=None)
    conn.execute("BEGIN")
    o = Omzetter(conn)
    try:
        o.rapport(args.rapport, args.csv, "doorgevoerd")
        print("\nDoorvoeren")
        o.apply()
    except Exception:
        conn.execute("ROLLBACK")
        raise
    print(f"\n{o.changes} gewijzigde rijen; {len(o.warnings)} waarschuwing(en)")
    conn.execute("COMMIT")
    ok = conn.execute("PRAGMA integrity_check").fetchone()[0]
    print(f"TOEGEPAST en vastgelegd in {args.qea}; integrity_check: {ok}")
    return 0 if ok == "ok" else 1


if __name__ == "__main__":
    sys.exit(main())
