#!/usr/bin/env bash
# Vraag de versie op
echo "Script om aanpassingen uit een Excel-bestand te verwerken In de EA-repo van het GGM. Inputparameters: VERSION (string), EXCEL_FILE (string)"
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

DEFAULT_EXCEL_FILE="./$VERSION/Gemeentelijk Gegevensmodel-import.xlsx"
# Vraag hette verwerken Excel-bestand op
EXCEL_FILE=${2:-}
if [ -z "$EXCEL_FILE" ]; then
    read -p "Geef de naam het het te verwerken Excel-bestand [default: $DEFAULT_EXCEL_FILE]: " EXCEL_FILE
    if [[ -z "$EXCEL_FILE" ]]; then
        EXCEL_FILE=$DEFAULT_EXCEL_FILE
    fi
    echo "Processing Excel File: $EXCEL_FILE"
fi

GGM="./$VERSION/Gemeentelijk Gegevensmodel EA16.qea"
# Controleer of de vereiste bestanden bestaan
if [ ! -f "$GGM" ]; then
    echo "Error: The GGM Repo file '$GGM' does not exist."
    exit 1
fi

# Controleer of crunch_uml is geïnstalleerd
if ! command -v crunch_uml &> /dev/null; then
    echo "This tool makes use of crunch_uml, but it is not installed. Please install crunch_uml before proceeding. See: https://github.com/brienen/crunch_uml"
    exit 1
fi

# Lees het XMI-bestand
echo "Reading Excel file into repo $EXCEL_FILE..."
crunch_uml import -f "$EXCEL_FILE" -t xlsx -db_create
echo "Excel file $EXCEL_FILE successfully imported."

# Exporteer de vertaling naar het nieuwe bestand
echo "Writing imported Excel into file $GGM..."
crunch_uml export -f "$GGM" -t earepo --tag_strategy upsert
echo "Excel file $EXCEL_FILE successfully exported to $GGM."