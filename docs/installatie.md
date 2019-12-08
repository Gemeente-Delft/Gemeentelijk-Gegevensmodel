# Installatie Gemeentelijk Gegevensmodel

## Voorbeeldbestand gebruiken

Dit is de gemakkelijkste manier om te starten met het Gemeentelijk Gegevensmodel. Het werkt ook met de [viewer van Enterprise Architect](https://www.sparxsystems.eu/enterprise-architect/ea-lite-edition/).

1. Installeer Enterprise Architect of de viewer van Enterprise Architect. 
2. Download het bestand 'Gemeentelijk_Gegevensmodel.eap'.
3. Open 'Gemeentelijk_Gegevensmodel.eap' met de Enterprise Architect.


## XMI-bestand importeren in project

Het Gemeentelijk Gegevensmodel (GGM) kan als [XMI-vorm](https://www.omg.org/spec/XMI/About-XMI/) worden geïmporteerd in een bestaand project in [Enterprise Architect](https://sparxsystems.com). Deze optie werkt niet met de viewer van Enterprise Architect. 

Je kunt het ook importeren in een ander tool met UML-ondersteuning. Wij hebben nog geen ervaring met importeren in een ander tool, en feedback van gebruikers is welkom!

Hieronder de te nemen stappen om het in een nieuw of bestaand project binnen Enterprise Architect te importeren.

1. Download het bestand 'Gemeentelijk_Gegevensmodel.xml'
2. Start Enterprise Architect (of andere XMI-Compatible tooling)
3. (Optioneel) Maak nieuw project
4. Kies _"Import Package from XMI"_

![Import XMI][importXMI]

5. Selecteer bij ”Filename” het gedownloade bestand “Gemeentelijk Gegevensmodel.xml”

![Select Filename][selectFilename]

6. Laat de instellingen zoals ze staan en druk op _“Import”_

![Import Package][importPackage]

7. Even wachten….
8. Open het Model en je ziet de verschillende Beleidsdomeinen en de bijbehorende diagrammen

![Open Diagram][openDiagram]

9. Succes!

[importXMI]: image/ImportPackage.png "Import XMI via tabblad Publish"
[selectFilename]: image/SelectFilename.png "Select Filename"
[importPackage]: image/ImportPackage.png "Import Package"
[openDiagram]: image/OpenDiagram.png "Open Diagram"
