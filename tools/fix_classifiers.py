#!/usr/bin/env python3
"""Koppelt losse typenamen van attributen aan de gelijknamige klasse, enumeratie of datatype (nov 2026).

Na de MIM-omzetting (tools/fix_datatypes_mim.py) resteren attributen waarvan de typetekst
(t_attribute.Type) een naam uit het model is, maar zonder classifier: 'Type', 'Leverancier',
'statusOpenbareRuimte', 'LAND' ... De generatoren vallen dan terug op naam-matching (crunch_uml,
LOD) of op xsd:string. Een datatype mag ook een klasse/objecttype, referentielijst of enumeratie
zijn; de koppeling hoort in het model te staan.

Regels, per attribuut (alleen attributen van klassen; typetekst gevuld, classifier leeg):
  - kandidaten: objecten (Class, Enumeration, DataType) met precies die naam, dezelfde naam zonder
    hoofdletterverschil, of 'enum_' + naam (IMBOR-conventie, pakket Enumeratiesoort);
  - keuze bij meer kandidaten op nabijheid: zelfde modelpakket > zelfde domeinmap > 99 Kern;
    gelijke stand = meerduidig, handmatig;
  - automatisch alleen als de kandidaat dichtbij staat (zelfde model, zelfde domeinmap of Kern) en de
    attribuutnaam op de typenaam lijkt (de een bevat de ander, zonder hoofdletters en tekens), of
    als het de IMBOR-conventie enum_<naam> in hetzelfde model betreft;
  - anders 'te beoordelen' met de reden: verwijst naar de eigen klasse, naam lijkt niet op het type
    (vaak een verkeerd gekozen typetekst), of kandidaat in een ander model;
  - geen kandidaat: 'geen match' (Enum, Kleuren, Adres ...), handmatig.

Doorvoeren zet Classifier op het Object_ID en de typetekst op de exacte naam van het doel
('Land', 'enum_Type'), zoals EA zelf doet bij het kiezen van een classifier, en zet ModifiedDate
van de klasse. Idempotent. Standaard dry-run (mode=ro); --apply schrijft in één transactie.
Sluit Enterprise Architect en maak eerst een back-up. --zonder-imbor slaat het pakket
'Model Basis IMBOR' over (daar loopt de IMBOR-omzetting nog).

Gebruik:
  python3 -I tools/fix_classifiers.py "v3.0.0/Gemeentelijk Gegevensmodel.qea" \
      --rapport tools/classifiers-koppelen-dryrun.md --csv /tmp/classifiers.csv
  python3 -I tools/fix_classifiers.py "v3.0.0/Gemeentelijk Gegevensmodel.qea" --apply --zonder-imbor
"""
import argparse
import collections
import csv
import re
import sqlite3
import sys
from dataclasses import dataclass
from datetime import datetime

IMBOR_PKG = "Model Basis IMBOR"
KERN_PKG = "99 Kern"
AUTO, BEOORDELEN, MEERDUIDIG, GEEN = "automatisch", "te beoordelen", "meerduidig", "geen match"


def norm(s: str) -> str:
    return re.sub(r"[^0-9a-z]", "", (s or "").casefold())


def lijkt_op(attr: str, doel: str) -> bool:
    a, d = norm(attr), norm(re.sub(r"^enum_", "", doel or ""))
    return bool(a and d) and (a in d or d in a)


def as_int(v):
    try:
        return int(v)
    except (TypeError, ValueError):
        return 0


@dataclass
class Plan:
    cat: str
    doel: int | None = None      # Object_ID van het doel
    reden: str = ""
    kandidaten: tuple = ()       # Object_ID's bij meerduidig


class Koppelaar:
    def __init__(self, conn: sqlite3.Connection, zonder_imbor: bool):
        self.c = conn
        self.c.row_factory = sqlite3.Row
        self.now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.zonder_imbor = zonder_imbor
        self._load()

    def _load(self) -> None:
        pk = {r["Package_ID"]: (r["Parent_ID"], r["Name"]) for r in
              self.c.execute("SELECT Package_ID, Parent_ID, Name FROM t_package")}
        self.pad: dict[int, tuple] = {}

        def pad(pid):
            if pid not in self.pad:
                parent, name = pk.get(pid, (0, "?"))
                self.pad[pid] = (pad(parent) + (name,)) if parent and parent in pk else (name,)
            return self.pad[pid]
        for pid in pk:
            pad(pid)
        self.obj = {r["Object_ID"]: r for r in self.c.execute(
            "SELECT Object_ID, Name, Object_Type, Package_ID, Stereotype FROM t_object "
            "WHERE Object_Type IN ('Class','DataType','Enumeration')")}
        self.exact = collections.defaultdict(list)
        self.fold = collections.defaultdict(list)
        for i, o in self.obj.items():
            self.exact[o["Name"].strip()].append(i)
            self.fold[o["Name"].strip().casefold()].append(i)
        self.attrs = self.c.execute(
            "SELECT a.ID, a.Object_ID, a.Name, a.Type, a.Classifier, o.Name AS owner, o.Package_ID AS pkg "
            "FROM t_attribute a JOIN t_object o ON o.Object_ID=a.Object_ID "
            "WHERE o.Object_Type='Class' AND a.Type IS NOT NULL AND a.Type <> '' "
            "ORDER BY o.Package_ID, o.Name, a.Pos, a.Name").fetchall()
        self.attrs = [a for a in self.attrs if as_int(a["Classifier"]) == 0]

    # -- hulpfuncties -----------------------------------------------------------------------
    def pakket(self, oid) -> str:
        return " / ".join(self.pad[self.obj[oid]["Package_ID"]][2:])

    def is_imbor(self, pid) -> bool:
        return IMBOR_PKG in self.pad[pid]

    def nabijheid(self, attr_pid, kand_pid) -> int:
        a, k = self.pad[attr_pid], self.pad[kand_pid]
        if a[:5] == k[:5] and len(a) >= 5:
            return 3
        if a[:4] == k[:4] and len(a) >= 4:
            return 2
        if KERN_PKG in k:
            return 1
        return 0

    def kandidaten(self, typ: str) -> list[int]:
        """Alle objecten met deze naam, zonder hoofdletterverschil, of met het voorvoegsel enum_
        (IMBOR-conventie); de nabijheid beslist daarna, zodat enum_Leverancier in IMBOR wint van
        de klassen Leverancier elders."""
        typ = typ.strip()
        gezien, uit = set(), []
        for lst in (self.exact.get(typ, []), self.fold.get(typ.casefold(), []),
                    self.exact.get("enum_" + typ, []), self.fold.get("enum_" + typ.casefold(), [])):
            for i in lst:
                if i not in gezien:
                    gezien.add(i)
                    uit.append(i)
        return uit

    # -- planning ---------------------------------------------------------------------------
    def plan(self, a) -> Plan:
        kand = self.kandidaten(a["Type"])
        if not kand:
            return Plan(GEEN)
        scores = {k: self.nabijheid(a["pkg"], self.obj[k]["Package_ID"]) for k in kand}
        best = max(scores.values())
        top = [k for k, s in scores.items() if s == best]
        if len(top) > 1:
            return Plan(MEERDUIDIG, kandidaten=tuple(top))
        doel = top[0]
        o = self.obj[doel]
        if doel == a["Object_ID"]:
            return Plan(BEOORDELEN, doel, "verwijst naar de eigen klasse")
        if best == 0:
            return Plan(BEOORDELEN, doel, f"kandidaat in een ander model ({self.pakket(doel)})")
        imbor_conv = o["Name"].startswith("enum_") and best == 3
        if not imbor_conv and not lijkt_op(a["Name"], o["Name"]):
            return Plan(BEOORDELEN, doel, "attribuutnaam lijkt niet op de typenaam")
        return Plan(AUTO, doel)

    def plans(self):
        for a in self.attrs:
            if self.zonder_imbor and self.is_imbor(a["pkg"]):
                continue
            yield a, self.plan(a)

    # -- rapport ----------------------------------------------------------------------------
    def rapport(self, path, csv_path, mode) -> None:
        rows = list(self.plans())
        L = []
        L.append(f"# Koppeling van losse typenamen aan classifiers ({mode}, {self.now})\n")
        L.append("Bron: `v3.0.0/Gemeentelijk Gegevensmodel.qea`, attributen van klassen met een typetekst zonder "
                 "classifier. Script: `tools/fix_classifiers.py`." + (" Pakket Model Basis IMBOR overgeslagen "
                 "(--zonder-imbor)." if self.zonder_imbor else "") + "\n")
        L.append("## Samenvatting\n")
        L.append("| Categorie | IMBOR | Overig | Totaal |\n|---|---:|---:|---:|")
        tel = collections.Counter()
        for a, p in rows:
            tel[(p.cat, self.is_imbor(a["pkg"]))] += 1
        for cat in (AUTO, BEOORDELEN, MEERDUIDIG, GEEN):
            i, ov = tel[(cat, True)], tel[(cat, False)]
            L.append(f"| {cat} | {i} | {ov} | {i + ov} |")
        L.append(f"| **totaal** | {sum(v for (c, im), v in tel.items() if im)} | "
                 f"{sum(v for (c, im), v in tel.items() if not im)} | {len(rows)} |\n")

        def doelnaam(oid):
            o = self.obj[oid]
            return f"{o['Name']} ({o['Object_Type']}, {self.pakket(oid)})"

        L.append(f"## {AUTO.capitalize()}\n")
        L.append("Classifier wordt het doel; de typetekst wordt de exacte naam van het doel.\n")
        groep = collections.defaultdict(list)
        for a, p in rows:
            if p.cat == AUTO:
                groep[(a["Type"], p.doel)].append(a)
        L.append("| Typetekst nu | Doel | Attributen |\n|---|---|---|")
        for (typ, doel), lst in sorted(groep.items(), key=lambda kv: (self.is_imbor(kv[1][0]["pkg"]), kv[0][0].casefold())):
            attrs = ", ".join(f"{a['owner']}.{a['Name']}" for a in lst[:6]) + (f" … ({len(lst)})" if len(lst) > 6 else "")
            L.append(f"| {typ} | {doelnaam(doel)} | {attrs} |")
        L.append("")

        L.append(f"## {BEOORDELEN.capitalize()}\n")
        L.append("Niet automatisch gekoppeld; het voorgestelde doel staat erbij. Oordeel per regel.\n")
        L.append("| Klasse.attribuut | Typetekst | Voorgesteld doel | Reden |\n|---|---|---|---|")
        for a, p in rows:
            if p.cat == BEOORDELEN:
                L.append(f"| {a['owner']}.{a['Name']} ({self.pakket(a['Object_ID'])}) | {a['Type']} | "
                         f"{doelnaam(p.doel)} | {p.reden} |")
        L.append("")

        L.append(f"## {MEERDUIDIG.capitalize()}\n")
        L.append("| Klasse.attribuut | Typetekst | Kandidaten |\n|---|---|---|")
        for a, p in rows:
            if p.cat == MEERDUIDIG:
                L.append(f"| {a['owner']}.{a['Name']} ({self.pakket(a['Object_ID'])}) | {a['Type']} | "
                         f"{'; '.join(doelnaam(k) for k in p.kandidaten)} |")
        L.append("")

        L.append(f"## {GEEN.capitalize()}\n")
        L.append("Geen klasse, enumeratie of datatype met deze naam in het model.\n")
        g = collections.defaultdict(list)
        for a, p in rows:
            if p.cat == GEEN:
                g[a["Type"]].append(a)
        L.append("| Typetekst | Attributen |\n|---|---|")
        for typ, lst in sorted(g.items(), key=lambda kv: kv[0].casefold()):
            L.append(f"| {typ} | " + ", ".join(f"{a['owner']}.{a['Name']}" for a in lst) + " |")
        L.append("")

        tekst = "\n".join(L)
        if path:
            with open(path, "w", encoding="utf-8") as f:
                f.write(tekst)
            print(f"rapport: {path}")
        else:
            print(tekst)
        if csv_path:
            with open(csv_path, "w", newline="", encoding="utf-8") as f:
                w = csv.writer(f)
                w.writerow(["categorie", "pakket", "klasse", "attribuut", "type", "doel_id", "doel", "doel_pakket", "reden"])
                for a, p in rows:
                    d = p.doel
                    w.writerow([p.cat, self.pakket(a["Object_ID"]), a["owner"], a["Name"], a["Type"], d or "",
                                self.obj[d]["Name"] if d else "", self.pakket(d) if d else "", p.reden])
            print(f"csv: {csv_path}")
        self.rows = rows

    # -- doorvoeren -------------------------------------------------------------------------
    def apply(self) -> int:
        n, touched = 0, set()
        for a, p in self.rows:
            if p.cat != AUTO:
                continue
            o = self.obj[p.doel]
            self.c.execute("UPDATE t_attribute SET Classifier=?, Type=? WHERE ID=?", (p.doel, o["Name"], a["ID"]))
            touched.add(a["Object_ID"])
            n += 1
        for oid in touched:
            self.c.execute("UPDATE t_object SET ModifiedDate=? WHERE Object_ID=?", (self.now, oid))
        print(f"{n} attributen gekoppeld in {len(touched)} klassen")
        return n


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("qea", help="pad naar de .qea (SQLite) van Enterprise Architect")
    ap.add_argument("--apply", action="store_true", help="wijzigingen vastleggen (zonder: dry-run, alleen lezen)")
    ap.add_argument("--zonder-imbor", action="store_true", help="pakket 'Model Basis IMBOR' overslaan")
    ap.add_argument("--rapport", help="markdown-rapport (zonder: naar het scherm)")
    ap.add_argument("--csv", help="CSV met alle beoordeelde attributen")
    args = ap.parse_args()

    if not args.apply:
        conn = sqlite3.connect(f"file:{args.qea}?mode=ro", uri=True)
        Koppelaar(conn, args.zonder_imbor).rapport(args.rapport, args.csv, "dry-run")
        conn.close()
        print("DRY-RUN: de .qea is alleen gelezen (gebruik --apply om door te voeren)")
        return 0

    conn = sqlite3.connect(args.qea, isolation_level=None)
    conn.execute("BEGIN")
    try:
        k = Koppelaar(conn, args.zonder_imbor)
        k.rapport(args.rapport, args.csv, "doorgevoerd")
        k.apply()
    except Exception:
        conn.execute("ROLLBACK")
        raise
    conn.execute("COMMIT")
    ok = conn.execute("PRAGMA integrity_check").fetchone()[0]
    print(f"TOEGEPAST en vastgelegd in {args.qea}; integrity_check: {ok}")
    return 0 if ok == "ok" else 1


if __name__ == "__main__":
    sys.exit(main())
