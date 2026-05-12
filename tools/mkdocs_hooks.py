"""MkDocs hook voor de GGM-site.

Laadt docs/_data/authors.yml in config.extra, zodat de theme-override
overrides/main.html de auteur- en organisatie-metadata kan gebruiken voor
schema.org JSON-LD-injectie in de <head>.
"""
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
