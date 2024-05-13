# Installatie Gemeentelijk Gegevensmodel

## Voorbeeldbestand gebruiken

Dit is de gemakkelijkste manier om te starten met het Gemeentelijk Gegevensmodel. Het werkt ook met de [viewer van Enterprise Architect](https://www.sparxsystems.eu/enterprise-architect/ea-lite-edition/).

1. Installeer Enterprise Architect of de viewer van Enterprise Architect. 
2. Download het bestand 'Gemeentelijk_Gegevensmodel.qua'.
3. Open 'Gemeentelijk_Gegevensmodel.qua' met de Enterprise Architect.

## XMI-bestand importeren in project

Het Gemeentelijk Gegevensmodel (GGM) kan als [XMI-vorm](https://www.omg.org/spec/XMI/About-XMI/) worden geïmporteerd in een bestaand project in [Enterprise Architect](https://sparxsystems.com). Deze optie werkt niet met de viewer van Enterprise Architect. 

Je kunt het ook importeren in een ander tool met UML-ondersteuning. Wij hebben nog geen ervaring met importeren in een ander tool, en feedback van gebruikers is welkom!

Hieronder de te nemen stappen om het in een nieuw of bestaand project binnen Enterprise Architect te importeren.

1\. Download het bestand 'Gemeentelijk_Gegevensmodel.xml'
2\. Start Enterprise Architect (of andere XMI-Compatible tooling)
3\. (Optioneel) Maak nieuw project
4\. Kies _"Import Package from XMI"_

![Import XMI][importXMI]

5\. Selecteer bij ”Filename” het gedownloade bestand “Gemeentelijk Gegevensmodel XML2.1.2.xml”

![Select Filename][selectFilename]

6\. Laat de instellingen zoals ze staan en druk op _“Import”_

![Import Package][importPackage]

7\. Even wachten….
8\. Open het Model en je ziet de verschillende Beleidsdomeinen en de bijbehorende diagrammen

![Open Diagram][openDiagram]

8\. Succes!

## Installatie Gemeentelijk Gegevensmodel in Bizzdesign

Het Gemeentelijk Gegevensmodel (GGM) kan als [XMI-vorm](https://www.omg.org/spec/XMI/About-XMI/) worden geïmporteerd in een bestaand project in [Bizzdesign](https://bizzdesign.com). Hiervoor wordt een apart script gebruikt dat Bizzdesign speciaal voor het GGM beschikbaar heeft gesteld.

### GGM importeren in Bizzdesign

Hieronder de te nemen stappen om het in een nieuw 
project binnen Bizzdesign te importeren.

1\. Download het bestand [Gemeentelijk Gegevensmodel XMI2.1.2](https://github.com/Gemeente-Delft/Gemeentelijk-Gegevensmodel/blob/master/Gemeentelijk%20Gegevensmodel%20XMI2.1.2.xml)

2\. Start Bizzdesign

3\. Open een nieuw modelpackage met een leeg UML-model, of voeg een leeg UML-model toe aan een bestaand modelpackage

![Open een nieuw modelpackage][Bizzdesign_stap1]

4\. Selecteer het UML-model, en open de query-editor met ctrl-Q. Kopieer de inhoud van het scriptbestand [UML XMI import Bizzdesign.txt](https://github.com/Gemeente-Delft/Gemeentelijk-Gegevensmodel/blob/master/UML%20XMI%20import%20Bizzdesign.txt) in de query-editor. Sla eventueel het script op in het model.

![Selecteer het UML-model][Bizzdesign_stap2]

5\. Voer het script uit via de Execute-knop van de query-editor, en kies het XMI-bestand 'Gemeentelijk Gegevensmodel XMI2.1.2' dat je net hebt gedownload. De inhoud wordt geïmporteerd in het geselecteerde UML-model. Zorg dat het uitvoertype op “Geen output” of “Tabel” staat en niet op “Tekstbestand”. Tijdens het uitvoeren van het script kun je waarschuwingen krijgen, die kun je negeren.  

6\. Even wachten….

7\. Succes!

## Installatie in Blue Dolphin

Hieronder staan de stappen voor het laden van het AMEFF-bestand in Blue Dolphin. Bij vragen contacteer jouw ValueBlue account- of customersuccess-manager.

1\. Download het [AMEFF-bestand](https://github.com/VNG-Realisatie/GEMMA-GGM-Archi-repository/blob/develop/AMEFF%20export/GGM.xml) uit de GEMMA-repository 

2\. Als BlueDolphin gebruiker met Beheerderrol kun je AMEFF-bestanden uploaden. Zie hiervoor de [handleiding: AMEFF bestanden importeren](https://support.valueblue.nl/hc/nl/articles/360013407860-AMEFF-bestanden-importeren-naar-BlueDolphin)

3\. Succes!


[Bizzdesign_stap1]: image/Bizzdesign_stap1.png "Open een nieuw modelpackage"
[Bizzdesign_stap2]: image/Bizzdesign_stap2.png "Selecteer het UML-model"

[importXMI]: image/ImportPackage.png "Import XMI via tabblad Publish"
[selectFilename]: image/SelectFilename.png "Select Filename"
[importPackage]: image/ImportPackage.png "Import Package"
[openDiagram]: image/OpenDiagram.png "Open Diagram"
