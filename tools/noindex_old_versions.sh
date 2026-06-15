#!/usr/bin/env bash
# Injecteert <meta name="robots" content="noindex,follow"> in elke HTML
# onder v*-mappen van een mike gh-pages worktree. /latest/ blijft
# indexeerbaar; alleen de versie-snapshots krijgen noindex.
#
# Idempotent: een marker-comment zorgt dat een tweede run niets doet.
#
# Aanroep:
#   ./tools/noindex_old_versions.sh <pad-naar-gh-pages-worktree>

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

MARKER="<!-- ggm-noindex-injected -->"
META="<meta name=\"robots\" content=\"noindex,follow\">"

INJECTED=0
SKIPPED=0

shopt -s nullglob
for vdir in "$ROOT"/v*; do
    [ -d "$vdir" ] || continue
    while IFS= read -r -d '' html; do
        if grep -qF "$MARKER" "$html"; then
            SKIPPED=$((SKIPPED + 1))
            continue
        fi
        # Voeg meta + marker direct na de openings-<head> toe. Werkt
        # ongeacht of <head> attributen heeft, zolang het op één regel staat.
        python3 - "$html" "$META" "$MARKER" <<'PY'
import sys, re
path, meta, marker = sys.argv[1], sys.argv[2], sys.argv[3]
with open(path, "r", encoding="utf-8") as f:
    content = f.read()
new, n = re.subn(
    r"(<head\b[^>]*>)",
    r"\1\n  " + marker + "\n  " + meta,
    content,
    count=1,
)
if n:
    with open(path, "w", encoding="utf-8") as f:
        f.write(new)
PY
        INJECTED=$((INJECTED + 1))
    done < <(find "$vdir" -type f -name '*.html' -print0)
done

echo "noindex geïnjecteerd in $INJECTED bestanden ($SKIPPED al voorzien)."
