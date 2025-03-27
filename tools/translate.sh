#!/usr/bin/env bash
# Script om vertalingen van het GGM te maken voor opgegeven talen.

echo "Script om vertalingen van het GGM te maken. Inputparameters: VERSION (string)."

VERSION=${1:-}
if [ -z "$VERSION" ]; then
    read -p "Enter the version of GGM that needs to be updated (e.g., v1.0): " VERSION
    if [ -z "$VERSION" ]; then
        echo "Error: Version cannot be empty."
        exit 1
    fi
fi

# Controleer of de versie-directory bestaat
VERSION_DIR="./$VERSION"
if [ ! -d "$VERSION_DIR" ]; then
    echo "Error: The directory '$VERSION_DIR' does not exist. Please create it before running the script."
    exit 1
fi

# Maak de 'translations' directory binnen de versie-directory als deze nog niet bestaat
TRANSLATIONS_DIR="$VERSION_DIR/translations"
if [ ! -d "$TRANSLATIONS_DIR" ]; then
    mkdir -p "$TRANSLATIONS_DIR"
fi

XMI="./$VERSION/Gemeentelijk Gegevensmodel XMI2.1.xml"
ROOT_GGM=EAPK_073A3334_C42A_41a6_A0C6_38DFF8C70236
i18N_FILE=./$VERSION/translations/ggm.i18n.json

# Controleer of de vereiste bestanden bestaan
if [ ! -f "$XMI" ]; then
    echo "Error: The XMI file '$XMI' does not exist."
    exit 1
fi

if [ ! -f "$i18N_FILE" ]; then
    echo "Error: The i18n file '$i18N_FILE' does not exist."
    exit 1
fi

# Controleer of crunch_uml is geïnstalleerd
if ! command -v crunch_uml &> /dev/null; then
    echo "This tool makes use of crunch_uml, but it is not installed. Please install crunch_uml before proceeding. See: https://github.com/brienen/crunch_uml"
    exit 1
fi

# Vraag talen op via de commandline
read -p "Enter the list of language codes (comma-separated, e.g., en,fr,de): " LANGUAGES_INPUT
if [ -z "$LANGUAGES_INPUT" ]; then
    echo "Error: Language codes cannot be empty."
    exit 1
fi

# Splits de input in een array
IFS=',' read -r -a LANGUAGES <<< "$LANGUAGES_INPUT"

# Lees het XMI-bestand
echo "Reading GGM Datamodel $XMI..."
#crunch_uml import -f "$XMI" -t eaxmi -db_create

# Loop door de talenlijst en voer vertalingen uit
for LANG in "${LANGUAGES[@]}"; do
    LANG=$(echo "$LANG" | xargs)  # Verwijder spaties rond de taalcode
    echo "Translating GGM to language $LANG..."
    crunch_uml export -t i18n -f "$i18N_FILE" --language "$LANG" --translate True --from_language "nl"

    if [ $? -eq 0 ]; then
        echo "Translation for language $LANG completed successfully."
    else
        echo "Error: Translation for language $LANG failed."
        exit 1
    fi
done

echo "All translations completed successfully."