#!/usr/bin/env python3
"""Negen overzichtsdiagrammen hernoemen naar 'View <model>' in de EA-repository van het GGM
(.qea = SQLite), volgens het advies van 11 november 2026 en de keuze van Arjen.

Aanleiding: in de LOD-browser (lod.gemeentelijkgegevensmodel.nl) is het pad van een deelmodel het
pakketpad plus de diagramnaam. Heet het overzichtsdiagram van een model hetzelfde als zijn pakket,
dan herhaalt het laatste segment zich: kern/bag/bag, interne-organisatie/subsidies/subsidies. Met
de conventie 'View <model>' wordt dat kern/bag/view-bag enzovoort. De documentatie kent geen
diagramnamen en verandert niet.

  1. Acht diagrammen krijgen de naam 'View <model>' (BAG, Subsidies, Samenwerkomgeving, Inburgering,
     Normafwijking, Vroegsignalering, Generieke Entiteiten Erfgoed, Burgerzaken).
  2. Het diagram Bedrijfsprocessen (Kern > RGBZPlus > Diagram > Bedrijfsprocessen) wordt
     'View Bedrijfsprocessen', verhuist naar RGBZPlus > Diagram, en het dan lege pakket
     Bedrijfsprocessen (t_package + zijn t_object-rij) vervalt. Pad: kern/rgbzplus/view-bedrijfsprocessen.

Zelfde werkwijze als tools/fixes/fix_zwembaden.py: één transactie, standaard een dry-run op een
tijdelijke kopie, met --apply vastleggen in de echte .qea. Idempotent: een tweede run meldt 0
wijzigingen. Enterprise Architect gesloten, back-up gemaakt.

Gebruik:
  python3 -I tools/fixes/fix_view_namen.py "v3.0.0/Gemeentelijk Gegevensmodel.qea"          # dry-run
  python3 -I tools/fixes/fix_view_namen.py "v3.0.0/Gemeentelijk Gegevensmodel.qea" --apply  # doorvoeren
"""
import argparse
import pathlib
import shutil
import sqlite3
import sys
import tempfile
from datetime import datetime

# --- Vaste punten in de v3.0.0-.qea (ea_guid, huidige naam, nieuwe naam) -------------------------
DIAGRAMS = [
    ("{53E16E43-EDF1-4b47-B0DD-C77D8FEFCCA3}", "BAG", "View BAG"),
    ("{F408BDED-51D4-4204-9B95-F0C6C2474DC3}", "Subsidies", "View Subsidies"),
    ("{8FAD3A01-3E43-4848-8621-B47FE3B5EA4F}", "Samenwerkomgeving", "View Samenwerkomgeving"),
    ("{96927C60-9F7B-4e67-806A-02EE0191983D}", "Inburgering", "View Inburgering"),
    ("{1818B773-1463-43c7-BACA-FEE391FE27CD}", "Normafwijking", "View Normafwijking"),
    ("{07334A5A-E2F0-41ce-8510-B41BAF6876BD}", "Vroegsignalering", "View Vroegsignalering"),
    ("{B7192738-00E7-4b65-902A-B8292E79261B}", "Generieke entiteiten Erfgoed", "View Generieke Entiteiten Erfgoed"),
    ("{D9511F60-3CA7-43bd-B6C8-F66447D66DBA}", "Burgerzaken", "View Burgerzaken"),
    ("{63323A39-82A4-4607-8A45-E4CBD1D800B0}", "Bedrijfsprocessen", "View Bedrijfsprocessen"),
]
DIAGRAM_BEDRIJFSPROCESSEN = DIAGRAMS[-1][0]
PKG_BEDRIJFSPROCESSEN = ("{CCFD7DA0-19FE-4c02-86EA-6C4EFEA6CC2C}", "Bedrijfsprocessen")   # map met één diagram
PKG_RGBZPLUS_DIAGRAM = ("{55858D70-7BBF-4841-8A65-BE28AFED16F4}", "Diagram")              # Kern > RGBZPlus > Diagram


class Fixer:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.conn.row_factory = sqlite3.Row
        self.changes = 0
        self.now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # -- hulpjes -----------------------------------------------------------------------------
    def one(self, sql, *params):
        return self.conn.execute(sql, params).fetchone()

    def all(self, sql, *params):
        return self.conn.execute(sql, params).fetchall()

    def run(self, sql, *params):
        cur = self.conn.execute(sql, params)
        self.changes += cur.rowcount
        return cur.rowcount

    @staticmethod
    def step(title):
        print(f"\n== {title}")

    @staticmethod
    def say(msg):
        print(f"  {msg}")

    # -- 0. controle van de uitgangspunten ---------------------------------------------------
    def check(self):
        self.step("0. Uitgangspunten")
        for guid, old, new in DIAGRAMS:
            r = self.one("SELECT Diagram_ID, Name, Package_ID FROM t_diagram WHERE ea_guid=?", guid)
            if r is None:
                raise SystemExit(f"diagram {guid} ({old}) niet gevonden")
            if r["Name"] not in (old, new):
                raise SystemExit(f"diagram {guid} heet '{r['Name']}', verwacht '{old}' of '{new}'")
            self.say(f"diagram {r['Diagram_ID']:5d} '{r['Name']}' in pakket {r['Package_ID']}")
        for guid, name in (PKG_RGBZPLUS_DIAGRAM,):
            r = self.one("SELECT Package_ID, Name FROM t_package WHERE ea_guid=?", guid)
            if r is None or r["Name"] != name:
                raise SystemExit(f"pakket {guid} ({name}) niet gevonden of anders genoemd")
            self.say(f"pakket {r['Package_ID']} '{r['Name']}' aanwezig")
        r = self.one("SELECT Package_ID, Name, Parent_ID FROM t_package WHERE ea_guid=?", PKG_BEDRIJFSPROCESSEN[0])
        if r is None:
            self.say(f"pakket '{PKG_BEDRIJFSPROCESSEN[1]}' is al weg")
        else:
            if r["Name"] != PKG_BEDRIJFSPROCESSEN[1]:
                raise SystemExit(f"pakket {PKG_BEDRIJFSPROCESSEN[0]} heet '{r['Name']}'")
            parent = self.one("SELECT Package_ID FROM t_package WHERE ea_guid=?", PKG_RGBZPLUS_DIAGRAM[0])
            if r["Parent_ID"] != parent["Package_ID"]:
                raise SystemExit(f"pakket '{r['Name']}' hangt niet onder RGBZPlus > Diagram")
            self.say(f"pakket {r['Package_ID']} '{r['Name']}' onder {r['Parent_ID']}")

    # -- 1. diagrammen hernoemen -------------------------------------------------------------
    def rename(self):
        self.step("1. Overzichtsdiagrammen hernoemen naar 'View <model>'")
        for guid, old, new in DIAGRAMS:
            r = self.one("SELECT Diagram_ID, Name, Package_ID FROM t_diagram WHERE ea_guid=?", guid)
            if r["Name"] == new:
                self.say(f"{r['Diagram_ID']:5d} '{new}': al goed")
                continue
            twin = self.one("SELECT Diagram_ID FROM t_diagram WHERE Package_ID=? AND Name=? AND ea_guid<>?",
                            r["Package_ID"], new, guid)
            if twin:
                raise SystemExit(f"pakket {r['Package_ID']} heeft al een diagram '{new}' ({twin['Diagram_ID']})")
            self.run("UPDATE t_diagram SET Name=?, ModifiedDate=? WHERE ea_guid=?", new, self.now, guid)
            self.say(f"{r['Diagram_ID']:5d} '{old}' -> '{new}'")

    # -- 2. Bedrijfsprocessen uit zijn map ---------------------------------------------------
    def move(self):
        self.step("2. Diagram Bedrijfsprocessen naar RGBZPlus > Diagram, lege map weg")
        pkg = self.one("SELECT Package_ID FROM t_package WHERE ea_guid=?", PKG_BEDRIJFSPROCESSEN[0])
        target = self.one("SELECT Package_ID FROM t_package WHERE ea_guid=?", PKG_RGBZPLUS_DIAGRAM[0])["Package_ID"]
        d = self.one("SELECT Diagram_ID, Package_ID, Name FROM t_diagram WHERE ea_guid=?", DIAGRAM_BEDRIJFSPROCESSEN)
        if d["Package_ID"] == target:
            self.say(f"diagram {d['Diagram_ID']} staat al in pakket {target}")
        else:
            if pkg is None or d["Package_ID"] != pkg["Package_ID"]:
                raise SystemExit(f"diagram {d['Diagram_ID']} staat in pakket {d['Package_ID']}, verwacht de map Bedrijfsprocessen")
            twin = self.one("SELECT Diagram_ID FROM t_diagram WHERE Package_ID=? AND Name=?", target, d["Name"])
            if twin:
                raise SystemExit(f"pakket {target} heeft al een diagram '{d['Name']}' ({twin['Diagram_ID']})")
            self.run("UPDATE t_diagram SET Package_ID=?, ModifiedDate=? WHERE ea_guid=?", target, self.now, DIAGRAM_BEDRIJFSPROCESSEN)
            self.say(f"diagram {d['Diagram_ID']} '{d['Name']}': pakket {d['Package_ID']} -> {target}")
        if pkg is None:
            self.say("map Bedrijfsprocessen is al weg")
            return
        pid = pkg["Package_ID"]
        inhoud = (self.one("SELECT COUNT(*) AS n FROM t_object WHERE Package_ID=?", pid)["n"],
                  self.one("SELECT COUNT(*) AS n FROM t_diagram WHERE Package_ID=?", pid)["n"],
                  self.one("SELECT COUNT(*) AS n FROM t_package WHERE Parent_ID=?", pid)["n"],
                  self.one("SELECT COUNT(*) AS n FROM t_xref WHERE Client=?", PKG_BEDRIJFSPROCESSEN[0])["n"])
        if any(inhoud):
            raise SystemExit(f"map Bedrijfsprocessen is niet leeg (objecten, diagrammen, subpakketten, xrefs = {inhoud})")
        n_obj = self.run("DELETE FROM t_object WHERE Object_Type='Package' AND ea_guid=?", PKG_BEDRIJFSPROCESSEN[0])
        n_pkg = self.run("DELETE FROM t_package WHERE Package_ID=?", pid)
        self.say(f"map Bedrijfsprocessen ({pid}) verwijderd: {n_pkg} pakketrij, {n_obj} objectrij")

    # -- 3. eindcontrole ---------------------------------------------------------------------
    def verify(self) -> int:
        self.step("3. Eindcontrole")
        problems = []
        for guid, old, new in DIAGRAMS:
            r = self.one("SELECT d.Diagram_ID, d.Name, p.Name AS pkg, p.Package_ID FROM t_diagram d "
                         "JOIN t_package p ON p.Package_ID=d.Package_ID WHERE d.ea_guid=?", guid)
            if r is None or r["Name"] != new:
                problems.append(f"diagram {guid} heet niet '{new}'")
                continue
            dubbel = self.one("SELECT COUNT(*) AS n FROM t_diagram WHERE Package_ID=? AND Name=?", r["Package_ID"], new)["n"]
            if dubbel != 1:
                problems.append(f"'{new}' komt {dubbel}x voor in pakket {r['pkg']}")
            self.say(f"{r['Diagram_ID']:5d} '{r['Name']}' in {r['pkg']} ({r['Package_ID']})")
        target = self.one("SELECT Package_ID FROM t_package WHERE ea_guid=?", PKG_RGBZPLUS_DIAGRAM[0])["Package_ID"]
        d = self.one("SELECT Package_ID FROM t_diagram WHERE ea_guid=?", DIAGRAM_BEDRIJFSPROCESSEN)
        if d["Package_ID"] != target:
            problems.append("View Bedrijfsprocessen staat niet in RGBZPlus > Diagram")
        if self.one("SELECT 1 FROM t_package WHERE ea_guid=?", PKG_BEDRIJFSPROCESSEN[0]):
            problems.append("map Bedrijfsprocessen bestaat nog")
        if self.one("SELECT 1 FROM t_object WHERE ea_guid=?", PKG_BEDRIJFSPROCESSEN[0]):
            problems.append("objectrij van de map Bedrijfsprocessen bestaat nog")
        wezen = self.one("SELECT COUNT(*) AS n FROM t_object o WHERE o.Object_Type='Package' AND NOT EXISTS "
                         "(SELECT 1 FROM t_package p WHERE p.ea_guid=o.ea_guid)")["n"]
        if wezen:
            problems.append(f"{wezen} pakketobject(en) zonder pakketrij")
        wezen = self.one("SELECT COUNT(*) AS n FROM t_diagram d WHERE NOT EXISTS "
                         "(SELECT 1 FROM t_package p WHERE p.Package_ID=d.Package_ID)")["n"]
        if wezen:
            problems.append(f"{wezen} diagram(men) in een onbestaand pakket")
        self.say(f"{len(DIAGRAMS)} diagrammen gecontroleerd; {len(problems)} afwijking(en)")
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
        tmp = tempfile.NamedTemporaryFile(prefix="fix_view_namen-", suffix=".qea", delete=False)
        tmp.close()
        shutil.copyfile(args.qea, tmp.name)
        target = tmp.name
    conn = sqlite3.connect(target, isolation_level=None)
    conn.execute("BEGIN")
    f = Fixer(conn)
    try:
        f.check()
        f.rename()
        f.move()
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
