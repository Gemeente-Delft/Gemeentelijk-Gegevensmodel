#!/usr/bin/env python
"""Controleert de deelmodellen (één Turtle-bestand per EA-diagram, uit crunch_uml) en maakt daaruit:

  --stage OUT         een boom voor de dropmap van de lod-browser-stack (task publish:lod);
  --merged FILE       één samengevoegd Turtle-bestand met alle deelmodellen: het geheel, om te
                      committen en te downloaden (task generate:lod-geheel; publish:lod werkt het bij);
  --live-graphs FILE  (bij --stage) de graphs die nu op de server staan; voor elke graph onder
                      NAMESPACE/VERSION/ die geen deelmodel meer is komt een leeg bestand in de
                      staging, zodat de loader die graph leegmaakt (hij wist zelf nooit een graph).

Controle per bronbestand (bij elke fout exit 1 en wordt niets geschreven of klaargezet):

  1. de kopregel '# graph: <NAMESPACE/VERSION/pad>' lezen (crunch_uml --lod_version zet de versie
     zelf in de graph-IRI); het pad mag alleen a-z, 0-9, _ - . en / bevatten en moet uniek zijn;
  2. het bestand met rdflib parsen, zodat een kapot bestand hier faalt en niet elke ronde opnieuw
     bij de loader op de server.

Staging (--stage). De loader op de server leest de kopregel NIET: hij leidt de graph-URI af uit het
relatieve pad in de dropmap (GRAPH_BASE + pad zonder .ttl). De dropmap moet dus de graph-URI's
volgen. Elk bestand komt op OUT/pad.ttl (zonder het versiesegment: publish:lod rsynct OUT/ naar
<dropmap>/<VERSION>/). Rechten worden expliciet gezet (mappen 755, bestanden 644): rsync -a neemt de
rechten van de bron over en de loader-container leest als een andere gebruiker.

Samenvoegen (--merged). De vereniging van alle triples van alle deelmodellen: een klasse die in
meerdere diagrammen voorkomt, staat er één keer in. De uitvoer is deterministisch (zelfde invoer =
byte-gelijk bestand), zodat git alleen echte wijzigingen ziet. Het samengevoegde bestand mag in SRC
zelf staan; het wordt dan niet als deelmodel meegelezen.

Gebruik: stage_lod_views.py SRC --namespace NS --version v3.0.0 [--stage OUT] [--merged FILE]
         [--live-graphs FILE]
"""
import argparse
import os
import re
import sys
import tempfile
from pathlib import Path

import rdflib

GRAPH_LINE = re.compile(r"^# graph: <(?P<uri>[^>]+)>$")
GRAPH_PATH = re.compile(r"^[a-z0-9_.-]+(/[a-z0-9_.-]+)*$")
IRI_IN_LINE = re.compile(r"https?://[^\s\",<>]+")


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


def live_paths(live_file: Path, graph_base: str) -> set[str]:
    """De graph-paden onder graph_base uit een lijst live graphs (CSV of één IRI per regel)."""
    paths: set[str] = set()
    for line in live_file.read_text(encoding="utf-8").splitlines():
        for iri in IRI_IN_LINE.findall(line):
            if iri.startswith(graph_base):
                rel = iri[len(graph_base):].strip("/")
                if rel and GRAPH_PATH.match(rel):
                    paths.add(rel)
    return paths


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("src", type=Path, help="bronmap met de deelmodellen (*.ttl, recursief)")
    ap.add_argument("--namespace", required=True, help="LINKED_DATA_NS, bv. https://lod.gemeentelijkgegevensmodel.nl")
    ap.add_argument("--version", required=True, help="versiesegment dat elke graph-IRI moet dragen, bv. v3.0.0")
    ap.add_argument("--stage", type=Path, help="lege uitvoermap; krijgt de structuur van de graph-paden")
    ap.add_argument("--merged", type=Path, help="pad van het samengevoegde Turtle-bestand (het geheel)")
    ap.add_argument("--live-graphs", type=Path, help="bestand met de graphs die nu op de server staan (bij --stage)")
    args = ap.parse_args()
    if not args.stage and not args.merged:
        ap.error("geef --stage, --merged of beide")

    ns = args.namespace.rstrip("/")
    version = args.version.strip("/")
    graph_base = f"{ns}/{version}/"
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
        if not m or not m["uri"].startswith(graph_base):
            errors.append(f"{f}: begint niet met '# graph: <{graph_base}...>' (gevonden: '{first}')")
            continue
        rel = m["uri"][len(graph_base):]
        if not GRAPH_PATH.match(rel):
            errors.append(f"{f}: graph-pad '{rel}' bevat tekens die de loader niet accepteert (alleen a-z 0-9 _ - . /)")
            continue
        if rel in seen:
            errors.append(f"{f}: graph <{graph_base}{rel}> komt ook voor in {seen[rel]}")
            continue
        seen[rel] = f
        try:
            g = rdflib.Graph().parse(data=rest, format="turtle")
        except Exception as e:  # noqa: BLE001 - elke parsefout is een reden om te stoppen
            errors.append(f"{f}: geen geldige Turtle: {str(e).splitlines()[0]}")
            continue
        parsed.append((rel, f, first + "\n" + rest, g))

    for e in errors:
        print(f"Error: {e}")
    if errors:
        print(f"Error: {len(errors)} fout(en); er is niets geschreven of klaargezet.")
        return 1

    # 2. Staging-boom voor de dropmap, plus lege bestanden voor verdwenen graphs.
    if args.stage:
        for rel, _, text, _ in parsed:
            target = args.stage / f"{rel}.ttl"
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text, encoding="utf-8")
            os.chmod(target, 0o644)
        verdwenen: list[str] = []
        if args.live_graphs:
            verdwenen = sorted(live_paths(args.live_graphs, graph_base) - set(seen))
            for rel in verdwenen:
                target = args.stage / f"{rel}.ttl"
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(
                    f"# graph: <{graph_base}{rel}>\n"
                    "# Dit diagram is geen deelmodel meer; de graph is leeggemaakt (task publish:lod).\n",
                    encoding="utf-8",
                )
                os.chmod(target, 0o644)
        os.chmod(args.stage, 0o755)
        for d in args.stage.rglob("*"):
            if d.is_dir():
                os.chmod(d, 0o755)
        print(f"{len(parsed)} deelmodellen klaargezet als graphs onder {graph_base}")
        if verdwenen:
            print(f"{len(verdwenen)} graphs die geen deelmodel meer zijn worden leeggemaakt: " + ", ".join(verdwenen))

    # 3. Het geheel.
    if args.merged:
        merged = rdflib.Graph()
        for _, _, _, g in parsed:
            for pfx, uri in g.namespaces():
                if pfx:  # prefixen van de bron (bv. dct) gaan voor op de rdflib-standaard (dcterms)
                    merged.bind(pfx, uri, override=True)
            merged += g
        header = (
            f"# Gemeentelijk Gegevensmodel {version}: het geheel, alle deelmodellen samengevoegd\n"
            f"#\n"
            f"# Dit bestand bevat de {len(parsed)} deelmodellen (één per EA-diagram) uit deze map als\n"
            f"# één geheel: de vereniging van hun triples ({len(merged)} unieke triples). Een klasse die in\n"
            f"# meerdere diagrammen voorkomt, staat er één keer in. Per diagram staat elk deelmodel\n"
            f"# ook als eigen bestand in deze map en als named graph onder <{graph_base}>.\n"
            f"#\n"
            f"# Gegenereerd door tools/stage_lod_views.py (task generate:lod).\n"
            f"# Niet met de hand bewerken: wijzigingen horen in het model.\n\n"
        )
        write_merged(merged, args.merged, header)
        print(f"{len(parsed)} deelmodellen samengevoegd in {args.merged} ({len(merged)} unieke triples)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
