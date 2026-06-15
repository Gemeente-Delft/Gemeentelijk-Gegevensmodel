#!/usr/bin/env bash
# Opschonen van pre-mike content uit de gh-pages root.
#
# Achtergrond: vóór de overstap op `mike` werd de site direct in de
# gh-pages root gepubliceerd. Die oude bestanden bestaan nog steeds en
# bevatten canonical-tags naar het oude github.io-domein. Resultaat:
# Google ziet ze als duplicates van /latest/ met een verkeerde canonical.
#
# Dit script verwijdert al die losse pre-mike pagina's en assets, maar
# laat de structuur die `mike` beheert ongemoeid:
#
#   bewaard:  latest/  v*/  versions.json  CNAME  .nojekyll  404.html
#             (404.html wordt door GitHub Pages gebruikt voor 404-respons)
#
# Daarnaast:
#   - schrijft een nieuwe root sitemap.xml gebaseerd op latest/sitemap.xml,
#   - laat robots.txt (in latest/) ongemoeid; de root sitemap blijft op
#     https://<host>/sitemap.xml staan.
#
# Aanroep:
#   ./tools/cleanup_ghpages_root.sh <pad-naar-gh-pages-worktree>
#
# Het is een no-op als de gh-pages root al opgeschoond is.

set -euo pipefail

if [ $# -ne 1 ]; then
    echo "usage: $0 <pad-naar-gh-pages-worktree>" >&2
    exit 2
fi

ROOT="$1"

if [ ! -d "$ROOT" ]; then
    echo "Niet een directory: $ROOT" >&2
    exit 2
fi

if [ ! -f "$ROOT/versions.json" ] || [ ! -d "$ROOT/latest" ]; then
    echo "Lijkt geen mike gh-pages root: ontbreekt versions.json of latest/" >&2
    exit 2
fi

cd "$ROOT"

# Whitelist van entries die we behouden. Alles wat niet matcht en niet
# een v*-map of een dotfile is, wordt verwijderd.
KEEP=( ".nojekyll" "CNAME" "404.html" "latest" "versions.json" "robots.txt" )

is_kept() {
    local entry="$1"
    for k in "${KEEP[@]}"; do
        [ "$entry" = "$k" ] && return 0
    done
    # mike-versies: v1.2.3, v2.0.0, etc.
    if [[ "$entry" =~ ^v[0-9] ]]; then
        return 0
    fi
    return 1
}

REMOVED=0
for entry in *; do
    if is_kept "$entry"; then
        continue
    fi
    echo "  removing: $entry"
    rm -rf -- "$entry"
    REMOVED=$((REMOVED + 1))
done

# Verwijder ook de oude root-sitemap; we maken hieronder een nieuwe.
rm -f sitemap.xml sitemap.xml.gz

# Nieuwe root sitemap: hergebruik latest/sitemap.xml, met absolute URLs
# die al op het juiste domein staan (mike's canonical_version: latest
# zorgt dat /latest/sitemap.xml correcte URLs bevat na de post-build
# hook in tools/mkdocs_hooks.py).
# Defensieve fix: ook al zou de mkdocs post-build hook al `latesten/`
# naar `latest/en/` hebben omgezet, sla geen tweede kans over voor een
# gh-pages worktree die van een oudere build komt. Fix latest/ en alle
# v*-sitemaps (laatste worden weliswaar noindex'd, maar netter ook hier
# correct).
for sm in latest/sitemap.xml v*/sitemap.xml; do
    [ -f "$sm" ] || continue
    if grep -q "latesten" "$sm"; then
        sed -i.bak -E 's#/latesten/#/latest/en/#g; s#\blatesten\b#latest/en#g' "$sm"
        rm -f "$sm.bak"
        gzip -k -f "$sm"
        echo "  /latesten/ → /latest/en/ in $sm gefixed"
    fi
done

if [ -f "latest/sitemap.xml" ]; then
    cp latest/sitemap.xml sitemap.xml
    gzip -k -f sitemap.xml
    echo "  root sitemap.xml vervangen door kopie van latest/sitemap.xml"
fi

# Schrijf robots.txt als die ontbreekt of nog naar de github.io-host
# verwijst. We mikken expliciet op de root sitemap op het custom domein.
ROBOTS_TARGET="https://www.gemeentelijkgegevensmodel.nl/sitemap.xml"
if [ ! -f robots.txt ] || ! grep -q "$ROBOTS_TARGET" robots.txt; then
    cat > robots.txt <<EOF
User-agent: *
Allow: /

Sitemap: $ROBOTS_TARGET
EOF
    echo "  robots.txt geschreven"
fi

echo "Opgeschoond: $REMOVED top-level entries verwijderd."
