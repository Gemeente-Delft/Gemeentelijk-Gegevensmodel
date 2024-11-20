#!/usr/bin/env bash
# Vraag de versie op
echo "Script to deploy the Gemeentelijk Gegevensmodel (GGM) for version $VERSION in directory $VERSION_DIR. Inputparameters: VERSION (string), PUBLISH (true/false), USE_EXISTING_CRUNCH_DB (true/false)"
VERSION=${1:-}
if [ -z "$VERSION" ]; then
    read -p "Enter the version for this translation (e.g., v1.0): " VERSION
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

# Vraag de publish-parameter op, standaard 'false'
PUBLISH=${2:-}
if [ -z "$PUBLISH" ]; then
    read -p "Do you want to publish the documentation to GitHub Pages after processing? (true/false) [default: false]: " PUBLISH
    if [[ ! "$PUBLISH" == "true" ]]; then
        PUBLISH="false"
    fi
    echo "Publish documentation: $PUBLISH"
fi

XMI="./$VERSION/Gemeentelijk Gegevensmodel XMI2.1.xml"
EXCEL="./$VERSION/Gemeentelijk Gegevensmodel.xlsx"
IMPORT_EXCEL="./$VERSION/Gemeentelijk Gegevensmodel-import.xlsx"
GGM="./$VERSION/Gemeentelijk Gegevensmodel EA16.qea"
ROOT_GGM=EAPK_073A3334_C42A_41a6_A0C6_38DFF8C70236
TRANSLATIONS_DIR="$VERSION_DIR/translations"
i18N_FILE=./$TRANSLATIONS_DIR/ggm.i18n.json
DOCS="./docs"
DEFS="./$DOCS/definities"
GGM_ROOT_SCHEMA="GGM_ROOT_SCHEMA"
CRUNCH_UML_DB="./crunch_uml.db"


# Vraag of de bestaande crunch_uml.db gebruikt moet worden (om snel te teste), standaard 'false'
USE_EXISTING_CRUNCH_DB="false"
if [ -f "$CRUNCH_UML_DB" ]; then
    USE_EXISTING_CRUNCH_DB=${3:-}
    if [ -z "$USE_EXISTING_CRUNCH_DB" ]; then
        read -p "Moet de bestaande Crunch_uml.db gebruikt worden (om snel te testen)? (true/false) [default: false]: " USE_EXISTING_CRUNCH_DB
    fi
    if [[ ! "$USE_EXISTING_CRUNCH_DB" == "true" ]]; then
        USE_EXISTING_CRUNCH_DB="false"
    fi
    echo "Bestaande Crunch_uml.db gebruiken: $USE_EXISTING_CRUNCH_DB"
fi

# Als er een import-excel is, vraag dan of deze moet worden geïmporteerd als update op het ingelezen model
#USE_IMPORT_EXCEL="false"
#if [ -f "$IMPORT_EXCEL" ]; then
#    USE_IMPORT_EXCEL=${4:-}
#    if [ -z "$USE_IMPORT_EXCEL" ]; then
#        read -p "Moet de het bestand $IMPORT_EXCEL worden ingelezen om het ingelezen model up te daten? (true/false) [default: false]: " USE_IMPORT_EXCEL
#    fi
#    if [[ ! "$USE_IMPORT_EXCEL" == "true" ]]; then
#        USE_IMPORT_EXCEL="false"
#    fi
#    echo "Model updaten met $USE_IMPORT_EXCEL: $USE_IMPORT_EXCEL"
#fi



# Controleer of de vereiste bestanden bestaan
if [ ! -f "$XMI" ]; then
    echo "Error: The XMI file '$XMI' does not exist."
    exit 1
fi


if [ ! -d "$DOCS" ]; then
    echo "Error: The DOCS directory '$DOCS' does not exist."
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

# Check if mkdocs is installed
if ! command -v mkdocs &> /dev/null; then
    echo "This tool makes use of mkdocs, but is not installed. Please install mkdocs before proceeding. See: https://www.mkdocs.org"
    exit 1
fi
# Check if mike is installed
if ! command -v mike &> /dev/null; then
    echo "This tool makes use of mike for versioned documentation, but is not installed. Please install mike before proceeding. See: https://github.com/jimporter/mike"
    exit 1
fi

if [[ "$USE_EXISTING_CRUNCH_DB" == "false" ]]; then
    # Lees het XMI-bestand
    echo "Reading GGM Datamodel $XMI..."
    crunch_uml import -f "$XMI" -t eaxmi -db_create
    echo "XMI file $XMI successfully imported."

    # Extract GGM Datamodel only, discard  
    echo "Copying Core GGM Model to $GGM_ROOT_SCHEMA..."
    crunch_uml transform -ttp copy -sch_to $GGM_ROOT_SCHEMA -rt_pkg $ROOT_GGM 
    echo "Core GGM Datamodel successfully copied to schema $GGM_ROOT_SCHEMA."
fi

# Generate Markdown for documentation from '$GGM_ROOT_SCHEMA'
echo "Generate Markdown for documentation if informatiemodel..."
# Check if the directory with the name of the version exists
if [ ! -d "$DEFS" ]; then
    # Create the directory if it doesn't exist
    mkdir "$DEFS"
    echo "Created directory $DEFS"
fi
# Before genratring translations, delete existing translations
echo "Deleting existing markdown in $DEFS..."
rm -r "$DEFS"/*.md

crunch_uml  -sch $GGM_ROOT_SCHEMA export -t jinja2 --output_jinja2_template ggm_markdown.j2 -f $DEFS/definitie.md --output_jinja2_templatedir ./tools/
echo "Markdown documentation generated successfully. Cleaning up unwanted md-files..."
# Verwijder .md-bestanden uit $DEF die niet beginnen met 'definitie_Model'
if [ -d "$DEFS" ]; then
    echo "Cleaning up .md files in '$DEFS' that do not start with 'definitie_Model'..."
    find "$DEFS" -type f -name '*.md' ! -name 'definitie_Model *' -exec rm -v {} \;
    echo "Cleanup completed successfully."
else
    echo "Warning: Directory '$DEFS' does not exist. Skipping cleanup."
fi

# Generate Excel with specification..."
crunch_uml -sch $GGM_ROOT_SCHEMA export -t xlsx -f "$EXCEL"
echo "Excel specification generated successfully."

# Generate Translations for GGM
echo "Generating language-specific translations for GGM..."
# Haal de lijst met talen op uit het i18n-bestand
echo "Fetching languages from $i18N_FILE..."
LANGUAGES=$(jq -r 'keys[]' "$i18N_FILE")
if [ -z "$LANGUAGES" ]; then
    echo "Error: No languages found in $i18N_FILE."
else
    echo "Languages found in $i18N_FILE: $LANGUAGES"
fi

# Before genratring translations, delete existing translations
if [ -d "$TRANSLATIONS_DIR" ]; then
    echo "Deleting existing translations in $TRANSLATIONS_DIR..."
    rm -r "$TRANSLATIONS_DIR"/*.qea
else
    echo "Creating directory $TRANSLATIONS_DIR..."
    mkdir "$TRANSLATIONS_DIR"
fi

# Itereer door elke taal en voer de vertaling uit
for LANG in $LANGUAGES; do
    echo "Processing language: $LANG"
    TRANSLATION_SCHEMA=translation_$LANG

    # Controleer of de taal gedefinieerd is in het i18n-bestand
    if ! jq -e "has(\"$LANG\")" "$i18N_FILE" > /dev/null; then
        echo "Error: The language '$LANG' is not defined in $i18N_FILE."
        continue
    fi

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
done

########
# Deploy the documentation
# Generate mkdcos documentation for new version
mkdocs build
# Add new version to documentation tree
mike deploy $VERSION
# Set new version as default
mike set-default $VERSION 

# Deploy documentation
if [[ "$PUBLISH" == "true" ]]; then
    echo "Publishing documentation to GitHub Pages..."
    # git push origin gh-pages
fi




echo "Deployment for version $VERSION completed successfully."