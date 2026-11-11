#!/usr/bin/env python
"""Opschonen van EA-tagwaarden in een .qea-repository: '#NOTES#'-resten en herhaalde memotekst.

Achtergrond in tools/opschonen-tags.md. EA bewaart een tagged value in twee kolommen: Value (de
waarde, of '<memo>' bij een memo-tag) en Notes (bij een memo-tag de tekst; anders de notities van de
tagdefinitie, 'Description: ...'). De XMI-export plakt beide aan elkaar als 'Value#NOTES#Notes'. Door
terugschrijven van zulke XMI-waarden in de repository (crunch_uml export -t earepo, vóór 0.8.6) staat
'#NOTES#' nu letterlijk in Value, en herhaalt Notes dezelfde tekst tot dertien keer.

Regels per rij (t_objectproperties, t_attributetag, t_connectortag):
  * Value wordt het deel vóór de eerste '#NOTES#';
  * is dat '<memo>', dan wordt Notes de tekst: elk deel uit Value-staart en Notes één keer, in
    volgorde, zonder tagdefinities ('Description:', 'Values:', 'Default:', 'Type:');
  * is de waarde leeg en staat er echte tekst (geen tagdefinitie) achter de scheider, dan wordt
    die tekst de waarde; anders blijft de waarde en wordt Notes het eerste niet-lege deel van
    Notes (de tagdefinitie); echte tekst in de Value-staart die afwijkt van de waarde wordt gemeld
    (komt in het GGM niet voor);
  * rijen zonder '#NOTES#' blijven ongemoeid.

Gebruik:  opschoon_tags.py BRON.qea                 rapport (er wordt niets geschreven)
          opschoon_tags.py BRON.qea --output DOEL.qea  kopie van BRON met de opschoning toegepast
EA moet het bestand niet open hebben. Werk altijd op een kopie en controleer het resultaat in EA.
"""
import argparse
import collections
import re
import shutil
import sqlite3
import sys
from pathlib import Path

SEP = "#NOTES#"
META = re.compile(r"^(description|values|default|type)\s*:", re.IGNORECASE)
# tabel -> (sleutelkolom, waardekolom, notitiekolom, naamkolom van het element)
TABELLEN = {
    "t_objectproperties": ("PropertyID", "Value", "Notes"),
    "t_attributetag": ("PropertyID", "VALUE", "NOTES"),
    "t_connectortag": ("PropertyID", "VALUE", "NOTES"),
}


# Beschrijvingen uit het MIM-profiel die EA bij een lege memo-tag zonder label in Notes zet; na een
# rondreis staan ze als '#NOTES#<beschrijving>' in Value en lijken ze een waarde. Per tag, kleine letters.
BEKENDE_DEFINITIES = {
    "toelichting": {
        "een inhoudelijke toelichting op de toepassing van het informatie-element.",
        "mim 1.1: een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding.",
    },
    "populatie": {
        "voor objecttypen die deel uitmaken van een (basis)registratie betreft dit de beschrijving van de "
        "exemplaren van het gedefinieerde objecttype die in de desbetreffende registratie voorkomen."
    },
}


def is_definitie(deel, definities, prop=None):
    """Is dit deel (een stuk van) de tagdefinitie: 'Description: ...', die tekst zonder label, of een
    bekende profielbeschrijving van deze tag?"""
    tekst = deel.casefold()
    if META.match(deel) or tekst in definities:
        return True
    return any(tekst.startswith(bekend[:60]) for bekend in BEKENDE_DEFINITIES.get((prop or "").casefold(), ()))


def schoon(value, notes, prop=None):
    """(nieuwe value, nieuwe notes, reden, verloren tekst); reden None als er niets verandert."""
    value = value or ""
    notes = notes or ""
    if SEP not in value and SEP not in notes:
        return value, notes, None, None
    kop, *staart = (deel.strip() for deel in value.split(SEP))
    staart = [deel for deel in staart if deel]
    delen_notes = [deel.strip() for deel in notes.split(SEP)]
    delen_notes = [deel for deel in delen_notes if deel]
    # De tekst van de tagdefinitie komt ook zonder label voor ('Een inhoudelijke toelichting op de
    # toepassing van het informatie-element.' achter een lege Toelichting); die is geen waarde.
    definities = set()
    for deel in staart + delen_notes:
        m = META.match(deel)
        if m:
            definities.add(deel[m.end():].strip().casefold())
    if kop.casefold() == "<memo>":
        teksten = [deel for deel in staart + delen_notes if not is_definitie(deel, definities, prop)]
        uniek = list(dict.fromkeys(teksten))
        return "<memo>", "\r\n\r\n".join(uniek), "memo: tekst in Notes, ontdubbeld", None
    teksten = list(dict.fromkeys(deel for deel in staart if not is_definitie(deel, definities, prop)))
    nieuwe_notes = delen_notes[0] if delen_notes else ""
    if not kop and teksten:
        # 'Toelichting' met de tekst achter de scheider: de tekst is de waarde (zoals EA die bij
        # schone rijen ook in Value bewaart).
        return teksten[0], nieuwe_notes, "lege waarde met tekst erachter: tekst wordt de waarde", None
    verloren = [tekst for tekst in teksten if tekst != kop]
    reden = "waarde losgeknipt van de tagdefinitie" if kop else "lege waarde: tagdefinitie uit Value"
    return kop, nieuwe_notes, reden, (verloren[0] if verloren else None)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("bron", type=Path, help="het .qea-bestand (wordt alleen gelezen)")
    ap.add_argument("--output", type=Path, help="schrijf een opgeschoonde kopie naar dit bestand")
    ap.add_argument("--voorbeelden", type=int, default=3, help="aantal voorbeelden per reden in het rapport")
    args = ap.parse_args()
    if not args.bron.is_file():
        print(f"Error: {args.bron} bestaat niet")
        return 1
    if args.output and args.output.resolve() == args.bron.resolve():
        print("Error: --output mag niet het bronbestand zijn; werk op een kopie")
        return 1

    con = sqlite3.connect(f"file:{args.bron}?mode=ro", uri=True)
    wijzigingen = {}  # tabel -> [(id, value, notes)]
    rapport = collections.Counter()
    voorbeelden = collections.defaultdict(list)
    verloren_tekst = []
    per_property = collections.Counter()
    for tabel, (sleutel, kol_value, kol_notes) in TABELLEN.items():
        try:
            rijen = con.execute(f"SELECT {sleutel}, Property, {kol_value}, {kol_notes} FROM {tabel}").fetchall()
        except sqlite3.OperationalError as e:
            print(f"{tabel}: overgeslagen ({e})")
            continue
        lijst = []
        for rij_id, prop, value, notes in rijen:
            nieuw_value, nieuw_notes, reden, verloren = schoon(value, notes, prop)
            if reden is None:
                continue
            lijst.append((rij_id, nieuw_value, nieuw_notes))
            rapport[(tabel, reden)] += 1
            per_property[(tabel, prop)] += 1
            if len(voorbeelden[(tabel, reden)]) < args.voorbeelden:
                voorbeelden[(tabel, reden)].append((prop, (value or "")[:70], (notes or "")[:50], nieuw_value[:40], nieuw_notes[:50]))
            if verloren:
                verloren_tekst.append((tabel, rij_id, prop, verloren[:80]))
        wijzigingen[tabel] = lijst
    con.close()

    totaal = sum(len(v) for v in wijzigingen.values())
    print(f"{args.bron}: {totaal} tagwaarden met '{SEP}' te schonen")
    for (tabel, reden), n in sorted(rapport.items()):
        print(f"  {tabel}: {n} x {reden}")
        for prop, oud_v, oud_n, nw_v, nw_n in voorbeelden[(tabel, reden)]:
            print(f"      [{prop}] Value {oud_v!r} | Notes {oud_n!r}  ->  Value {nw_v!r} | Notes {nw_n!r}")
    print("  per tag:", ", ".join(f"{prop} {n}" for (tabel, prop), n in sorted(per_property.items(), key=lambda kv: -kv[1])))
    if verloren_tekst:
        print(f"  LET OP: {len(verloren_tekst)} rijen met tekst in de Value-staart die niet wordt overgenomen:")
        for tabel, rij_id, prop, tekst in verloren_tekst[:10]:
            print(f"      {tabel} {rij_id} [{prop}]: {tekst!r}")
    if not args.output:
        print("Niets geschreven (geen --output).")
        return 0

    shutil.copyfile(args.bron, args.output)
    con = sqlite3.connect(args.output)
    try:
        for tabel, (sleutel, kol_value, kol_notes) in TABELLEN.items():
            for rij_id, nieuw_value, nieuw_notes in wijzigingen.get(tabel, []):
                con.execute(f"UPDATE {tabel} SET {kol_value} = ?, {kol_notes} = ? WHERE {sleutel} = ?", (nieuw_value, nieuw_notes, rij_id))
        con.commit()
        rest = sum(
            con.execute(f"SELECT count(*) FROM {t} WHERE {v} LIKE '%{SEP}%' OR {n} LIKE '%{SEP}%'").fetchone()[0]
            for t, (_, v, n) in TABELLEN.items()
        )
    finally:
        con.close()
    print(f"Opgeschoonde kopie geschreven: {args.output} ({totaal} rijen bijgewerkt, {rest} rijen met '{SEP}' over)")
    return 0 if rest == 0 else 2


if __name__ == "__main__":
    sys.exit(main())
