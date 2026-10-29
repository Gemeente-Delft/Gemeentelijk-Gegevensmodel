#!/usr/bin/env python
"""Controleert de deelmodellen (één Turtle-bestand per EA-diagram) en maakt daaruit:

  --stage OUT     een boom voor de dropmap van de lod-browser-stack (task publish:lod);
  --merged FILE   één samengevoegd Turtle-bestand met alle deelmodellen, om te committen en
                  te downloaden (task generate:lod-views-merged; publish:lod werkt het bij).

Controle per bronbestand (bij elke fout exit 1 en wordt niets geschreven of klaargezet):

  1. de kopregel '# graph: <NAMESPACE/pad>' lezen; het pad mag alleen a-z, 0-9, _ - . en /
     bevatten en moet uniek zijn. Begint het pad al met PREFIX/ (crunch_uml zet met
     --lod_version de versie zelf in de graph-IRI), dan wordt die niet nog eens toegevoegd;
  2. het bestand met rdflib parsen, zodat een kapot bestand hier faalt en niet elke ronde
     opnieuw bij de loader op de server.

Staging (--stage). De loader op de server leest de kopregel NIET: hij leidt de graph-URI af
uit het relatieve pad in de dropmap (GRAPH_BASE + pad zonder .ttl). De dropmap moet dus de
graph-URI's volgen, niet de EA-packagestructuur van de bronmap
(3_Economie/Diagram/kvk.ttl -> economie/kvk.ttl). Elk bestand komt op OUT/pad.ttl, met de
kopregel herschreven naar de graph die het op de server wordt: NAMESPACE/PREFIX/pad
(PREFIX = release, bv. v3.0.0). Rechten worden expliciet gezet (mappen 755, bestanden 644):
rsync -a neemt de rechten van de bron over en de loader-container leest als een andere
gebruiker; een map met 700 (zoals mktemp -d die maakt) maakt de views daar onzichtbaar.

Samenvoegen (--merged). De vereniging van alle triples van alle deelmodellen: een klasse
die in meerdere diagrammen voorkomt, staat er één keer in. Turtle kent geen named graphs; de
indeling per diagram zit alleen in de losse bestanden en in de graphs op de server. De
uitvoer is deterministisch (zelfde invoer = byte-gelijk bestand), zodat git alleen echte
wijzigingen ziet. Het samengevoegde bestand mag in SRC zelf staan; het wordt dan niet als
deelmodel meegelezen.

Gebruik: stage_lod_views.py SRC --namespace NS [--prefix v3.0.0] [--stage OUT] [--merged FILE]
"""
import argparse
import os
import re
import sys
import tempfile
from pathlib import Path

import rdflib

GRAPH_LINE = re.compile(r"^# graph: <(?P<uri>[^>]+)>$")
# Kale slugs (Ashkans generator: underscores; crunch_uml: koppeltekens) en een versiesegment
# zoals v3.0.0; de loader leidt hieruit het relatieve pad in de dropmap af.
GRAPH_PATH = re.compile(r"^[a-z0-9_.-]+(/[a-z0-9_.-]+)*$")


def write_merged(merged: rdflib.Graph, target: Path, header: str) -> None:
    """Schrijft het samengevoegde bestand atomair (tijdelijk bestand + rename), rechten 644."""
    body = merged.serialize(format="turtle")
    target.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=target.parent, prefix=".merged-", suffix=".ttl")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(header)
            fh.write(body)
        os.chmod(tmp, 0o644)
        os.replace(tmp, target)
    except BaseException:
        Path(tmp).unlink(missing_ok=True)
        raise


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("src", type=Path, help="bronmap met de deelmodellen (*.ttl, recursief)")
    ap.add_argument("--namespace", required=True, help="LINKED_DATA_NS, bv. https://lod.gemeentelijkgegevensmodel.nl")
    ap.add_argument("--prefix", default="", help="versieprefix voor de graphs, bv. v3.0.0 (leeg = ongeversioneerd)")
    ap.add_argument("--stage", type=Path, help="lege uitvoermap; krijgt de structuur van de graph-paden")
    ap.add_argument("--merged", type=Path, help="pad van het samengevoegde Turtle-bestand")
    args = ap.parse_args()
    if not args.stage and not args.merged:
        ap.error("geef --stage, --merged of beide")

    ns = args.namespace.rstrip("/")
    prefix = args.prefix.strip("/")
    graph_base = f"{ns}/{prefix}/" if prefix else f"{ns}/"
    merged_path = args.merged.resolve() if args.merged else None
    errors: list[str] = []
    seen: dict[str, Path] = {}
    parsed: list[tuple[str, Path, str, rdflib.Graph]] = []

    if not args.src.is_dir():
        print(f"Error: bronmap '{args.src}' bestaat niet.")
        return 1
    files = sorted(f for f in args.src.rglob("*.ttl") if f.resolve() != merged_path)
    if not files:
        print(f"Error: geen *.ttl gevonden in '{args.src}'.")
        return 1

    # 1. Controleren en parsen; nog niets schrijven.
    for f in files:
        with f.open(encoding="utf-8") as fh:
            first = fh.readline().rstrip("\n")
            rest = fh.read()
        m = GRAPH_LINE.match(first)
        if not m or not m["uri"].startswith(ns + "/"):
            errors.append(f"{f}: begint niet met '# graph: <{ns}/...>' (gevonden: '{first}')")
            continue
        rel = m["uri"][len(ns) + 1:]
        if not GRAPH_PATH.match(rel):
            errors.append(f"{f}: graph-pad '{rel}' bevat tekens die de loader niet accepteert (alleen a-z 0-9 _ - . /)")
            continue
        if prefix and rel.startswith(prefix + "/"):
            # De bron draagt de versie al (crunch_uml --lod_version): niet dubbel prefixen.
            rel = rel[len(prefix) + 1:]
        if rel in seen:
            errors.append(f"{f}: graph <{ns}/{rel}> komt ook voor in {seen[rel]}")
            continue
        seen[rel] = f
        try:
            g = rdflib.Graph().parse(data=rest, format="turtle")
        except Exception as e:  # noqa: BLE001 - elke parsefout is een reden om te stoppen
            errors.append(f"{f}: geen geldige Turtle: {str(e).splitlines()[0]}")
            continue
        parsed.append((rel, f, rest, g))

    for e in errors:
        print(f"Error: {e}")
    if errors:
        print(f"Error: {len(errors)} fout(en); er is niets geschreven of klaargezet.")
        return 1

    # 2. Staging-boom voor de dropmap.
    if args.stage:
        for rel, _, rest, _ in parsed:
            target = args.stage / f"{rel}.ttl"
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(f"# graph: <{graph_base}{rel}>\n{rest}", encoding="utf-8")
            os.chmod(target, 0o644)
        os.chmod(args.stage, 0o755)
        for d in args.stage.rglob("*"):
            if d.is_dir():
                os.chmod(d, 0o755)
        print(f"{len(parsed)} deelmodellen klaargezet als graphs onder {graph_base}")

    # 3. Samengevoegd bestand.
    if args.merged:
        merged = rdflib.Graph()
        for _, _, _, g in parsed:
            for pfx, uri in g.namespaces():
                if pfx:  # prefixen van de bron (bv. dct) gaan voor op de rdflib-standaard (dcterms)
                    merged.bind(pfx, uri, override=True)
            merged += g
        release = f" {prefix}" if prefix else ""
        header = (
            f"# Gemeentelijk Gegevensmodel{release}: het geheel, alle deelmodellen samengevoegd\n"
            f"#\n"
            f"# Dit bestand bevat de {len(parsed)} deelmodellen (één per EA-diagram) uit deze map als\n"
            f"# één geheel: de vereniging van hun triples ({len(merged)} unieke triples). Een klasse die in\n"
            f"# meerdere diagrammen voorkomt, staat er één keer in. Per diagram staat elk deelmodel\n"
            f"# ook als eigen bestand in deze map en als named graph onder <{graph_base}>.\n"
            f"#\n"
            f"# Gegenereerd door tools/stage_lod_views.py (task generate:lod-views-merged).\n"
            f"# Niet met de hand bewerken: wijzigingen horen in de deelmodellen.\n\n"
        )
        write_merged(merged, args.merged, header)
        print(f"{len(parsed)} deelmodellen samengevoegd in {args.merged} ({len(merged)} unieke triples)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
