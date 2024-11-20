#!/usr/bin/env bash
echo "Script to translate Gemeentelijk Gegevensmodel (GGM) from file $GGM to another language using language file $i18N_FILE and writing translation to a versioned directory."

# Vraag de versie op
read -p "Enter the version for this translation (e.g., v1.0): " VERSION
if [ -z "$VERSION" ]; then
    echo "Error: Version cannot be empty."
    exit 1
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
GGM="./$VERSION/Gemeentelijk Gegevensmodel EA16.qea"
ROOT_GGM=EAPK_073A3334_C42A_41a6_A0C6_38DFF8C70236
i18N_FILE=./$VERSION/ggm.i18n.json

# Controleer of de taalparameter (language) is opgegeven
if [ -z "$1" ]; then
    echo "Please provide the language to which the GGM needs to be translated."
    exit 1
fi
LANG="$1"
TRANSLATION_SCHEMA=translation_$LANG

# Controleer of de vereiste bestanden bestaan
if [ ! -f "$XMI" ]; then
    echo "Error: The XMI file '$XMI' does not exist."
    exit 1
fi

if [ ! -f "$GGM" ]; then
    echo "Error: The GGM file '$GGM' does not exist."
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

# Controleer of de taal voorkomt in het JSON-bestand
if ! jq -e "has(\"$LANG\")" "$i18N_FILE" > /dev/null; then
    echo "Error: The language '$LANG' is not defined in $i18N_FILE."
    exit 1
fi
echo "The language '$LANG' exists in $i18N_FILE."

# Lees het XMI-bestand
echo "Reading GGM Datamodel $XMI..."
crunch_uml import -f "$XMI" -t eaxmi -db_create

# Transformeer en kopieer het GGM-schema naar het taal-specifieke schema
echo "Copying GGM from default schema to schema $LANG..."
crunch_uml transform -ttp copy -sch_to $TRANSLATION_SCHEMA --root_package $ROOT_GGM

# Lees de vertaling voor de opgegeven taal uit het i18n-bestand
echo "Reading translation for $LANG from file $i18N_FILE into schema $TRANSLATION_SCHEMA..."
crunch_uml -sch $TRANSLATION_SCHEMA import -f $i18N_FILE -t i18n --language $LANG

# Stel het pad in voor de vertaalde bestanden in de 'translations' directory
naam="${GGM##*/}"   # Extract the file name (without path)
naam_zonder_ext="${naam%.*}"  # Extract the name without extension
extensie="${naam##*.}"  # Extract the extension
ggm_vertaald="$TRANSLATIONS_DIR/${naam_zonder_ext}_$LANG.$extensie"

# Kopieer het originele GGM-bestand naar de vertaalde locatie
echo "Copying $GGM to $ggm_vertaald"
cp "$GGM" "$ggm_vertaald"

# Exporteer de vertaling naar het nieuwe bestand
echo "Writing translation from schema $TRANSLATION_SCHEMA into file $ggm_vertaald..."
crunch_uml -sch $TRANSLATION_SCHEMA export -f "$ggm_vertaald" -t earepo --tag_strategy update

echo "Translation completed successfully. Files are stored in the '$TRANSLATIONS_DIR' directory."