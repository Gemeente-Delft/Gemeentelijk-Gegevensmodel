# Installatie Gemeentelijk Gegevensmodel

## Voorbeeldbestand gebruiken

Dit is de gemakkelijkste manier om te starten met het Gemeentelijk Gegevensmodel. Het werkt ook met de [viewer van Enterprise Architect](https://sparxsystems.com/enterprise_architect_user_guide/17.0/getting_started/ea_lite.html).

1. Installeer Enterprise Architect of de viewer van Enterprise Architect. 
2. Download het bestand 'Gemeentelijk_Gegevensmodel.qea'.
3. Open 'Gemeentelijk_Gegevensmodel.qua' met de Enterprise Architect.

## XMI-bestand importeren in project

Het Gemeentelijk Gegevensmodel (GGM) kan als [XMI-vorm](https://www.omg.org/spec/XMI/About-XMI/) worden geïmporteerd in een bestaand project in [Enterprise Architect](https://sparxsystems.com). Deze optie werkt niet met de viewer van Enterprise Architect. 

Je kunt het ook importeren in een ander tool met UML-ondersteuning. Wij hebben nog geen ervaring met importeren in een ander tool, en feedback van gebruikers is welkom!

Hieronder de te nemen stappen om het in een nieuw of bestaand project binnen Enterprise Architect te importeren.

1. Download het bestand [GGM XMI-bestand geschikt voor Enterprise Architect 15, 16 en 17](https://github.com/Gemeente-Delft/Gemeentelijk-Gegevensmodel/blob/master/v3.0.0/Gemeentelijk%20Gegevensmodel%20XMI2.1.xml) en sla deze lokaal op
2. Start Enterprise Architect (of andere XMI-Compatible tooling) 
3. (Optioneel) Maak nieuw project
4. Kies _"Import Package from XMI"_

![Import XMI][importXMI]

5\. Selecteer bij ”Filename” het gedownloade bestand “Gemeentelijk Gegevensmodel XMI2.1.xml”

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

1\. Download het bestand [Gemeentelijk Gegevensmodel XMI2.1](https://github.com/Gemeente-Delft/Gemeentelijk-Gegevensmodel/blob/master/v3.0.0/Gemeentelijk%20Gegevensmodel%20XMI2.1.xml)

2\. Start Bizzdesign

3\. Open een nieuw modelpackage met een leeg UML-model, of voeg een leeg UML-model toe aan een bestaand modelpackage

![Open een nieuw modelpackage][Bizzdesign_stap1]

4\. Selecteer het UML-model, en open de query-editor met ctrl-Q. Kopieer de inhoud van het scriptbestand [UML XMI import Bizzdesign.txt](https://github.com/Gemeente-Delft/Gemeentelijk-Gegevensmodel/blob/master/UML%20XMI%20import%20Bizzdesign.txt) in de query-editor. Sla eventueel het script op in het model.

![Selecteer het UML-model][Bizzdesign_stap2]

5\. Voer het script uit via de Execute-knop van de query-editor, en kies het XMI-bestand 'Gemeentelijk Gegevensmodel XMI2.1' dat je net hebt gedownload. De inhoud wordt geïmporteerd in het geselecteerde UML-model. Zorg dat het uitvoertype op “Geen output” of “Tabel” staat en niet op “Tekstbestand”. Tijdens het uitvoeren van het script kun je waarschuwingen krijgen, die kun je negeren.  

6\. Even wachten….

7\. Succes!

## Installatie in Blue Dolphin

Hieronder staan de stappen voor het laden van het AMEFF-bestand in Blue Dolphin. Bij vragen contacteer jouw ValueBlue account- of customersuccess-manager.

1\. Download het [AMEFF-bestand](https://github.com/VNG-Realisatie/GEMMA-GGM-Archi-repository/blob/develop/exports/GEMMA-GGM%20AMEFF.xml) uit de GEMMA-repository 

2\. Als BlueDolphin gebruiker met Beheerderrol kun je AMEFF-bestanden uploaden. Zie hiervoor de [handleiding: AMEFF bestanden importeren](https://support.valueblue.nl/hc/nl/articles/360013407860-AMEFF-bestanden-importeren-naar-BlueDolphin)

3\. Succes!

## Linked Data

Het GGM is ook beschikbaar als Linked Data, in [Turtle](https://www.w3.org/TR/turtle/). Daarvoor heb je geen Enterprise Architect nodig. Alle bestanden staan per versie in de map [`ttl`](https://github.com/Gemeente-Delft/Gemeentelijk-Gegevensmodel/tree/master/v3.0.0/ttl):

| Bestand | Inhoud |
|---------|--------|
| [Gemeentelijk Gegevensmodel Linked Data.ttl](https://github.com/Gemeente-Delft/Gemeentelijk-Gegevensmodel/blob/master/v3.0.0/ttl/Gemeentelijk%20Gegevensmodel%20Linked%20Data.ttl) | Het hele model als ontologie (RDFS/OWL), met de metagegevens volgens [MIM 1.2](https://docs.geostandaarden.nl/mim/mim/). Enumeratiewaarden zijn ook SKOS-begrippen. |
| [Gemeentelijk Gegevensmodel Linked Data-shapes.ttl](https://github.com/Gemeente-Delft/Gemeentelijk-Gegevensmodel/blob/master/v3.0.0/ttl/Gemeentelijk%20Gegevensmodel%20Linked%20Data-shapes.ttl) | De [SHACL](https://www.w3.org/TR/shacl/)-shapes waarmee je data aan het model toetst. Ze importeren de ontologie. |
| `<domein>/.../<diagram>.ttl` | Per diagram een deelmodel, bijvoorbeeld `kern/bag/onderzoek.ttl`: de klassen op dat diagram met hun attributen, relaties en enumeraties. |

Je kunt het model ook online bekijken op [lod.gemeentelijkgegevensmodel.nl](https://lod.gemeentelijkgegevensmodel.nl). Elke klasse, elk attribuut en elke waarde heeft een eigen IRI die je direct kunt opvragen, bijvoorbeeld <https://lod.gemeentelijkgegevensmodel.nl/kern/bag/pand>. De deelmodellen staan daar als named graphs onder `https://lod.gemeentelijkgegevensmodel.nl/v3.0.0/`. Je bevraagt ze met SPARQL via <https://lod.gemeentelijkgegevensmodel.nl/sparql>.


[Bizzdesign_stap1]: image/Bizzdesign_stap1.png "Open een nieuw modelpackage"
[Bizzdesign_stap2]: image/Bizzdesign_stap2.png "Selecteer het UML-model"

[importXMI]: image/ImportPackage.png "Import XMI via tabblad Publish"
[selectFilename]: image/SelectFilename.png "Select Filename"
[importPackage]: image/ImportPackage.png "Import Package"
[openDiagram]: image/OpenDiagram.png "Open Diagram"
