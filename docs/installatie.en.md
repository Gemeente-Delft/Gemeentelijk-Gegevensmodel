---
description: "How to install and load the Delft Municipal Data Model (GGM) in Enterprise Architect, Bizzdesign or Blue Dolphin."
---

# Installing the Delft Municipal Data Model

The **Delft Municipal Data Model** (Dutch: *Gemeentelijk Gegevensmodel*, abbreviated **GGM**) can be installed in a few different UML / enterprise-architecture tools. The Dutch abbreviation *GGM* is used throughout this site.

## Using the example file

This is the easiest way to get started with the GGM. It also works with the [Enterprise Architect viewer](https://sparxsystems.com/enterprise_architect_user_guide/17.0/getting_started/ea_lite.html).

1. Install Enterprise Architect or the Enterprise Architect viewer.
2. Download the file `Gemeentelijk_Gegevensmodel.qea`.
3. Open `Gemeentelijk_Gegevensmodel.qea` in Enterprise Architect.

## Importing the XMI file into a project

The Municipal Information Model (GGM) can be imported in [XMI format](https://www.omg.org/spec/XMI/About-XMI/) into an existing project in [Enterprise Architect](https://sparxsystems.com). This option does *not* work with the Enterprise Architect viewer.

You can also import it into another tool that supports UML. We have no experience yet with other tools — feedback is welcome!

The steps to import it into a new or existing Enterprise Architect project are:

1. Download the [GGM XMI file (compatible with Enterprise Architect 15, 16 and 17)](https://github.com/Gemeente-Delft/Gemeentelijk-Gegevensmodel/blob/master/v2.5.0/Gemeentelijk%20Gegevensmodel%20XMI2.1.xml) and save it locally.
2. Start Enterprise Architect (or another XMI-compatible tool).
3. (Optional) Create a new project.
4. Choose *"Import Package from XMI"*.

![Import XMI][importXMI]

<em>Screenshot (in Dutch / Enterprise Architect UI): the "Import Package from XMI" option in the Publish tab.</em>

5\. Select the downloaded file `Gemeentelijk Gegevensmodel XMI2.1.xml` for *"Filename"*.

![Select Filename][selectFilename]

<em>Screenshot: file-selection dialog showing the chosen XMI file.</em>

6\. Leave the settings as they are and press *"Import"*.

![Import Package][importPackage]

<em>Screenshot: import dialog with default settings, "Import" button highlighted.</em>

7\. Wait a moment…
8\. Open the model and you will see the various policy domains and their diagrams.

![Open Diagram][openDiagram]

<em>Screenshot: the loaded GGM model in the Enterprise Architect Project Browser, showing policy domains.</em>

8\. Done!

## Installing the GGM in Bizzdesign

The GGM can be imported in [XMI format](https://www.omg.org/spec/XMI/About-XMI/) into an existing project in [Bizzdesign](https://bizzdesign.com). A separate script — provided by Bizzdesign specifically for the GGM — is used for this.

### Importing the GGM into Bizzdesign

The steps to import it into a new Bizzdesign project are:

1\. Download the file [Gemeentelijk Gegevensmodel XMI2.1](https://github.com/Gemeente-Delft/Gemeentelijk-Gegevensmodel/blob/master/v2.5.0/Gemeentelijk%20Gegevensmodel%20XMI2.1.xml).

2\. Start Bizzdesign.

3\. Open a new model package containing an empty UML model, or add an empty UML model to an existing model package.

![Open a new model package][Bizzdesign_stap1]

<em>Screenshot (in Dutch / Bizzdesign UI): creating a new model package with an empty UML model.</em>

4\. Select the UML model and open the query editor with Ctrl-Q. Copy the contents of the script file [UML XMI import Bizzdesign.txt](https://github.com/Gemeente-Delft/Gemeentelijk-Gegevensmodel/blob/master/UML%20XMI%20import%20Bizzdesign.txt) into the query editor. Optionally save the script in the model.

![Select the UML model][Bizzdesign_stap2]

<em>Screenshot (in Dutch / Bizzdesign UI): the query editor with the import script loaded.</em>

5\. Run the script via the Execute button of the query editor, and select the `Gemeentelijk Gegevensmodel XMI2.1` XMI file you just downloaded. The contents are imported into the selected UML model. Make sure the output type is set to *"No output"* or *"Table"*, not *"Text file"*. You may see warnings while the script runs — these can be ignored.

6\. Wait a moment…

7\. Done!

## Installing in Blue Dolphin

Below are the steps to load the AMEFF file into Blue Dolphin. For questions, contact your ValueBlue account or customer-success manager.

1\. Download the [AMEFF file](https://github.com/VNG-Realisatie/GEMMA-GGM-Archi-repository/blob/develop/exports/GEMMA-GGM%20AMEFF.xml) from the GEMMA repository.

2\. As a Blue Dolphin user with the Administrator role, you can upload AMEFF files. See the [manual: importing AMEFF files](https://support.valueblue.nl/hc/nl/articles/360013407860-AMEFF-bestanden-importeren-naar-BlueDolphin) (Dutch).

3\. Done!


[Bizzdesign_stap1]: image/Bizzdesign_stap1.png "Open a new model package"
[Bizzdesign_stap2]: image/Bizzdesign_stap2.png "Select the UML model"

[importXMI]: image/ImportPackage.png "Import XMI via Publish tab"
[selectFilename]: image/SelectFilename.png "Select Filename"
[importPackage]: image/ImportPackage.png "Import Package"
[openDiagram]: image/OpenDiagram.png "Open Diagram"
