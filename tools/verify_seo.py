#!/usr/bin/env python3
"""SEO-sanity check voor een gebouwde MkDocs site.

Aanroep:
    python tools/verify_seo.py site/

Controleert:
1. Geen `latesten` voorkomens (i18n+mike hreflang-bug).
2. Elke <loc> in sitemap.xml resolveert lokaal naar een bestaand bestand.
3. Elke canonical-tag wijst naar https://www.gemeentelijkgegevensmodel.nl/
   (niet naar het oude github.io-domein).
4. Elke pagina onder een v*-map heeft een noindex meta-tag.

Exit-code 0 bij succes, 1 bij gevonden problemen.
"""
from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlparse

EXPECTED_HOST = "www.gemeentelijkgegevensmodel.nl"
LEGACY_HOST_FRAGMENT = "github.io"
# Google's Rich Results vereisten voor Dataset.description.
DATASET_DESC_MIN = 50
DATASET_DESC_MAX = 5000
CANONICAL_RE = re.compile(
    r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)["\']',
    re.IGNORECASE,
)
NOINDEX_RE = re.compile(
    r'<meta[^>]+name=["\']robots["\'][^>]+content=["\'][^"\']*noindex',
    re.IGNORECASE,
)
JSONLD_RE = re.compile(
    r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
    re.IGNORECASE | re.DOTALL,
)
SITEMAP_NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}


def check_no_latesten(site: Path) -> list[str]:
    errors: list[str] = []
    for path in site.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in {".html", ".xml", ".json", ".txt"}:
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if "latesten" in content:
            errors.append(f"{path.relative_to(site)}: bevat 'latesten'")
    return errors


def check_sitemap_locs(site: Path, is_ghpages: bool) -> list[str]:
    """Check sitemap <loc> entries against the on-disk site.

    In een lokale mkdocs build zit geen /latest/ prefix; mike voegt die
    pas toe bij gh-pages deploy. Strip de prefix dus alleen in de lokale
    context bij het zoeken naar het bestand.
    """
    errors: list[str] = []
    sitemap = site / "sitemap.xml"
    if not sitemap.exists():
        return [f"sitemap.xml ontbreekt in {site}"]
    tree = ET.parse(sitemap)
    locs = [
        elem.text
        for elem in tree.iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
        if elem.text
    ]
    for loc in locs:
        parsed = urlparse(loc)
        if parsed.netloc != EXPECTED_HOST:
            errors.append(f"sitemap loc op verkeerd domein: {loc}")
            continue
        relative = unquote(parsed.path).strip("/")
        if not is_ghpages and relative.startswith("latest/"):
            relative = relative[len("latest/") :]
        elif not is_ghpages and relative == "latest":
            relative = ""
        candidate_html = site / relative / "index.html" if relative else site / "index.html"
        candidate_direct = site / relative if relative else site
        if not (candidate_html.exists() or candidate_direct.exists()):
            errors.append(f"sitemap loc resolveert niet lokaal: {loc}")
    return errors


def check_canonicals(site: Path) -> list[str]:
    """Verifieer canonical-hosts. Pagina's met noindex worden overgeslagen:
    Google indexeert ze toch niet, dus een verouderde canonical is onschadelijk.
    """
    errors: list[str] = []
    for html in site.rglob("*.html"):
        try:
            content = html.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if NOINDEX_RE.search(content):
            continue
        for canonical in CANONICAL_RE.findall(content):
            if LEGACY_HOST_FRAGMENT in canonical:
                errors.append(
                    f"{html.relative_to(site)}: canonical naar legacy host: {canonical}"
                )
            elif EXPECTED_HOST not in canonical:
                errors.append(
                    f"{html.relative_to(site)}: canonical op onbekende host: {canonical}"
                )
    return errors


def _iter_jsonld_nodes(content: str):
    for match in JSONLD_RE.findall(content):
        try:
            data = json.loads(match)
        except json.JSONDecodeError:
            continue
        graph = data.get("@graph") if isinstance(data, dict) else None
        nodes = graph if isinstance(graph, list) else [data]
        for node in nodes:
            if isinstance(node, dict):
                yield node


def check_jsonld_dataset_description(site: Path) -> list[str]:
    """Google Rich Results: Dataset.description moet 50-5000 tekens zijn.

    Skip noindex'd pagina's (oude mike-versies) — Google verwerkt die
    structured data toch niet.
    """
    errors: list[str] = []
    for html in site.rglob("*.html"):
        try:
            content = html.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if NOINDEX_RE.search(content):
            continue
        for node in _iter_jsonld_nodes(content):
            if node.get("@type") != "Dataset":
                continue
            desc = node.get("description")
            if not isinstance(desc, str):
                errors.append(
                    f"{html.relative_to(site)}: Dataset zonder description"
                )
                continue
            length = len(desc)
            if length < DATASET_DESC_MIN:
                errors.append(
                    f"{html.relative_to(site)}: Dataset.description "
                    f"{length} tekens (min {DATASET_DESC_MIN})"
                )
            elif length > DATASET_DESC_MAX:
                errors.append(
                    f"{html.relative_to(site)}: Dataset.description "
                    f"{length} tekens (max {DATASET_DESC_MAX})"
                )
    return errors


def check_noindex_on_old_versions(site: Path) -> list[str]:
    """Alleen relevant op een gh-pages checkout met mike-versies in v*/-mappen."""
    errors: list[str] = []
    for version_dir in sorted(site.glob("v*")):
        if not version_dir.is_dir():
            continue
        for html in version_dir.rglob("*.html"):
            try:
                content = html.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            if not NOINDEX_RE.search(content):
                errors.append(
                    f"{html.relative_to(site)}: mist noindex meta-tag"
                )
    return errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(f"usage: {argv[0]} <site-directory>", file=sys.stderr)
        return 2
    site = Path(argv[1]).resolve()
    if not site.is_dir():
        print(f"niet een directory: {site}", file=sys.stderr)
        return 2

    is_ghpages = (site / "versions.json").exists()
    all_errors: list[tuple[str, list[str]]] = [
        ("Geen 'latesten' paden", check_no_latesten(site)),
        ("Sitemap <loc> resolveert lokaal", check_sitemap_locs(site, is_ghpages)),
        ("Canonicals wijzen naar juiste domein", check_canonicals(site)),
        (
            "JSON-LD Dataset.description lengte (50-5000)",
            check_jsonld_dataset_description(site),
        ),
    ]
    if is_ghpages:
        all_errors.append(
            ("noindex op v*-mappen", check_noindex_on_old_versions(site))
        )

    failed = False
    for label, errors in all_errors:
        if errors:
            failed = True
            print(f"FAIL: {label} ({len(errors)} probleem(en))")
            for err in errors[:20]:
                print(f"  - {err}")
            if len(errors) > 20:
                print(f"  ... en nog {len(errors) - 20}")
        else:
            print(f"OK:   {label}")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
