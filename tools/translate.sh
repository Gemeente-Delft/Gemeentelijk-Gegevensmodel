#!/usr/bin/env bash
XMI="./Gemeentelijk Gegevensmodel XMI2.1.xml"
GGM="./Gemeentelijk Gegevensmodel EA16.qea"
ROOT_GGM=EAPK_073A3334_C42A_41a6_A0C6_38DFF8C70236
i18N_FILE=./ggm.i18n.json

echo "Script to translate Gemeentelijk Gegevensmodel (GGM) from file $GGM to another language using language file $i18N_FILE and writing translation to a new repository."

# Check if the version parameter (language) is provided
if [ -z "$1" ]; then
    echo "Please provide the language to which the GGM needs to be translated."
    exit 1
fi
LANG="$1"
TRANSLATION_SCHEMA=translation_$LANG

# Check if the XMI file exists
if [ ! -f "$XMI" ]; then
    echo "Error: The XMI file '$XMI' does not exist."
    exit 1
fi

# Check if the GGM file exists
if [ ! -f "$GGM" ]; then
    echo "Error: The GGM file '$GGM' does not exist."
    exit 1
fi

# Check if the i18n file exists
if [ ! -f "$i18N_FILE" ]; then
    echo "Error: The i18n file '$i18N_FILE' does not exist."
    exit 1
fi

# Check if crunch_uml is installed
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

# Read the XMI file
echo "Reading GGM Datamodel $XMI..."
crunch_uml import -f "$XMI" -t eaxmi -db_create

# Perform transformation and copy GGM schema to the language-specific schema
echo "Copying GGM from default schema to schema $LANG..."
crunch_uml transform -ttp copy -sch_to $TRANSLATION_SCHEMA --root_package $ROOT_GGM 

# Read translation for the specified language from the i18n file
echo "Reading translation for $LANG from file $i18N_FILE into schema $TRANSLATION_SCHEMA..."
crunch_uml -sch $TRANSLATION_SCHEMA import -f $i18N_FILE -t i18n --language $LANG

# Copy the GGM file to a new file with the language tag
naam="${GGM%.*}"   # Extract the name of the file without the extension
extensie="${GGM##*.}"  # Extract the extension
ggm_vertaald="${naam}_$LANG.$extensie"

# Move the original GGM file to the translated file
echo "Moving $GGM to $ggm_vertaald"
cp "$GGM" "$ggm_vertaald"

# Export the translation to the new file
echo "Writing translation from schema $TRANSLATION_SCHEMA into file $ggm_vertaald..."
crunch_uml -sch $TRANSLATION_SCHEMA export -f "$ggm_vertaald" -t earepo --tag_strategy update

echo "Translation completed successfully."