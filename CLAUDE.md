# CLAUDE.md

Project-specific guidelines for Claude when working on this repository.

## Project overview

This repository contains the **Gemeentelijk Gegevensmodel (GGM)** — an integral municipal information model developed by Gemeente Delft. The public-facing site is built with **MkDocs Material**, versioned with **mike**, and deployed to GitHub Pages at <https://www.gemeentelijkgegevensmodel.nl/>.

Source of truth for the model is Enterprise Architect (`.qea`) → XMI export → processed by `crunch_uml` into a SQLite database → rendered to Markdown via a Jinja2 template (`tools/ggm_markdown.j2`). The full pipeline is orchestrated by `TaskFile.yml`.

## Naming conventions

- **Dutch (default language):** *Gemeentelijk Gegevensmodel*, abbreviated **GGM**.
- **English:** ***Delft Municipal Data Model*** — and always explain on first use that the Dutch name is *Gemeentelijk Gegevensmodel* and that **GGM** is the Dutch abbreviation that continues to be used across the site for tooling, URLs and file names.
- Do NOT invent an English abbreviation (no "DMDM" etc.). The abbreviation "GGM" stays because all artefacts (repo names, files, Excel, TTL, DCAT, Python packages) use it.

Typical first-use pattern in an English page:

> The Delft Municipal Data Model (Dutch: *Gemeentelijk Gegevensmodel*, abbreviated **GGM**) is …

## Translations (mkdocs-static-i18n)

- Default language is **Dutch** (`locale: nl`). English is a secondary language (`locale: en`). Plugin: `mkdocs-static-i18n` with `docs_structure: suffix`.
- For each translatable Dutch page `docs/foo.md`, the English version lives next to it as `docs/foo.en.md`. The plugin automatically falls back to the Dutch version when an `.en.md` is absent (`fallback_to_default: true`).
- Navigation-label translations live in `mkdocs.yml` under the `en` language block → `nav_translations`.

### Dutch images in English pages

Most diagrams are exported from Enterprise Architect and contain Dutch text. Do NOT regenerate or translate the images. Instead, add a caption **one blank line after** the image describing it in English, so crawlers and non-Dutch readers understand:

```markdown
![Diagram title][refId]

<em>Diagram (in Dutch): short English description of what the diagram shows.</em>
```

**Always** leave a blank line between the image and the `<em>` caption, otherwise Markdown renders the caption inline with the image and it looks cramped.

### Relative paths under `/en/`

When the page URL is `/en/index.html`, a relative path `image/foo.png` resolves to `/en/image/foo.png`, which does not exist — assets are only copied to the default-language root. Rules:

- **Prefer Markdown image syntax** — `![alt](image/foo.png)` or reference-style `![alt][ref]` — MkDocs rewrites those correctly.
- **Only use raw `<img src="...">` when you need HTML attributes** (e.g. `width`, `align`). In that case write the path as `../image/foo.png` so it resolves correctly from `/en/…` and from versioned `/vX.Y.Z/en/…`.

## schema.org / SEO

- schema.org JSON-LD is injected in every page's `<head>` by the theme override `overrides/main.html`.
- Author and organisation metadata is sourced from `docs/_data/authors.yml`, loaded into `config.extra` by the hook `tools/mkdocs_hooks.py`.
- Per-page meta descriptions use Markdown front-matter (`description:` key).
- Canonical URLs are set automatically by Material from `site_url` in `mkdocs.yml`.
- Do NOT add Open Graph / Twitter Cards / social-card PNGs (explicitly out of scope).

## IndexNow / search-engine notifications

- The IndexNow key is the filename of `docs/<uuid>.txt`. It is **not** a secret (IndexNow verifies ownership by serving the key at `https://<host>/<uuid>.txt`), so it is hardcoded in `.github/workflows/reindex.yml`.
- The workflow pings Bing / Yandex / DuckDuckGo / Seznam on every push to the `gh-pages` branch. Google we let discover passively via `sitemap.xml`; if later the Google Search Console API is wired up, use repo secret `GSC_SERVICE_ACCOUNT_JSON`.

## Linked Data

- A draft TTL (`v{VERSION}/Gemeentelijk Gegevensmodel Linked Data-draft.ttl`) is already produced by `crunch_uml export -t ttl`. URI strategy: `https://lod.gemeentelijkgegevensmodel.nl/{package}/{class}`.
- The full Linked Data / RDF / SKOS / DCAT stack is **parked** for a later phase (see `.claude/plans/twinkly-whistling-owl.md`). Do not add RDF/JSON-LD-for-classes / SPARQL endpoint / content negotiation work unless explicitly requested.

## Build and deploy

- Everything is orchestrated by [`TaskFile.yml`](TaskFile.yml). Use `task --list` to see all tasks.
- Key tasks:
  - `task generate-docs` — regenerate `docs/definities/*.md` from the model.
  - `task full-deploy` — full build chain (translations, Excel, TTL, MIM, diff-md, MkDocs build).
  - `task publish-docs` — push to `gh-pages` branch. Requires confirmation prompt.
- Local preview: `mkdocs serve`.
- Versioning: `mike` aliases `latest` to the canonical version (see `mkdocs.yml` → `plugins.mike.canonical_version`).

## Files NOT to touch unless asked

- `docs/definities/*.md` — auto-generated. Edit the EA model instead, then re-run `task generate-docs`.
- `v{VERSION}/*.ttl`, `v{VERSION}/*.xlsx`, `v{VERSION}/Gemeentelijk Gegevensmodel XMI2.1.xml` — all generated.
- `crunch_uml.db` — binary artefact of the import process.

## General behavioural rules

- Scope small. The author prefers incremental, practical changes over sweeping refactors. When in doubt, propose a scoped plan and ask before expanding it.
- **Never** invent model content in Markdown that should come from the model itself — all GGM class/attribute documentation flows from EA via `crunch_uml`.
- Keep the Dutch source as the authoritative version. English translations follow.
- When introducing changes that affect build / deploy, also update `TaskFile.yml` and this file.
