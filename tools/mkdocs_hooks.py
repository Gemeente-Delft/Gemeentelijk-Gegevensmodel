"""MkDocs hook voor de GGM-site.

Laadt docs/_data/authors.yml in config.extra, zodat de theme-override
overrides/main.html de auteur- en organisatie-metadata kan gebruiken voor
schema.org JSON-LD-injectie in de <head>.

Daarnaast: post-build correctie voor de mkdocs-static-i18n + mike
interactie. De i18n-plugin plakt de locale-code als suffix achter het
pad-segment in plaats van als nieuw segment, waardoor in de sitemap en
in hreflang-tags `/latesten/...` verschijnt in plaats van `/latest/en/...`.
Die URL bestaat niet en levert 404's op in Google Search Console.
"""
import gzip
import re
from pathlib import Path

import yaml


def on_config(config, **kwargs):
    """Merge authors.yml into config.extra before the site is built."""
    authors_file = Path(config["docs_dir"]) / "_data" / "authors.yml"
    if not authors_file.exists():
        return config

    data = yaml.safe_load(authors_file.read_text(encoding="utf-8")) or {}

    extra = config.get("extra") or {}
    extra["authors"] = data.get("authors", [])
    extra["organization"] = data.get("organization", {})
    config["extra"] = extra

    return config


_LATESTEN_PATTERNS = [
    (re.compile(r"/latesten/"), "/latest/en/"),
    (re.compile(r"\blatesten\b"), "latest/en"),
]


def _fix_latesten(text: str) -> tuple[str, int]:
    total = 0
    for pattern, replacement in _LATESTEN_PATTERNS:
        text, n = pattern.subn(replacement, text)
        total += n
    return text, total


def on_post_build(config, **kwargs):
    """Repareer foutieve `/latesten/` paden in de gebouwde site.

    Schrijft direct in `site_dir` na de mkdocs-build:
      - `sitemap.xml` en `sitemap.xml.gz` (her-gzippen)
      - alle HTML-bestanden onder site_dir
    Idempotent: een tweede run is een no-op.
    """
    site_dir = Path(config["site_dir"])
    total_replacements = 0
    touched_files = 0

    sitemap = site_dir / "sitemap.xml"
    if sitemap.exists():
        original = sitemap.read_text(encoding="utf-8")
        fixed, n = _fix_latesten(original)
        if n:
            sitemap.write_text(fixed, encoding="utf-8")
            total_replacements += n
            touched_files += 1

            gz = site_dir / "sitemap.xml.gz"
            with gzip.open(gz, "wb") as fh:
                fh.write(fixed.encode("utf-8"))

    for html in site_dir.rglob("*.html"):
        try:
            original = html.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        fixed, n = _fix_latesten(original)
        if n:
            html.write_text(fixed, encoding="utf-8")
            total_replacements += n
            touched_files += 1

    if total_replacements:
        print(
            f"[mkdocs_hooks] /latesten/ → /latest/en/: "
            f"{total_replacements} vervangingen in {touched_files} bestanden."
        )
