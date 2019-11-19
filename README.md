# Gemeentelijk Gegevensmodel

Het Gemeentelijk Gegevensmodel (GGM) is een logisch gegevensmodel met daarin vertegenwoodigd alle beleidsterreinen van de gemeente. Het GGM is ontwikkeld in opdracht van de Gemeente Delft ter ondersteuning van de visie op het gebied van informatiegestuurd werken. Onder andere wordt het GGM gebruikt als centraal datamodel in het datawarehouse. Hiertoe is een generator beschikbaar om het GGM te vertalen naar fysieke databasetabellen.

Het GGM omvat alle beleidsterreinen die onder de verantwoordelijkeheid van de gemeente vallen. Dit ongeacht de organisatorische inrichting, zoals de afdelingen die de bijbehorende taken uitvoeren en uitbesteding aan derde partijen. Deze beleidsterreinen zijn afgeleid van de [IV3-taakvelden](https://www.rijksoverheid.nl/onderwerpen/financien-gemeenten-en-provincies/uitwisseling-financiele-gegevens-met-sisa-en-iv3/informatie-voor-derden-iv3). 

## Installatie en gebruik

Het Gemeentelijk Gegevensmodel is beschikbaar in [XMI-vorm](https://www.omg.org/spec/XMI/About-XMI/), en is ontwikkeld in, en toegepast met [Enterprise Architect](https://sparxsystems.com).

### Installatie

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

### Versies en gebruikte tooling

Het XMI-bestand van het Gemeentelijk Gegevensmodel is in theorie te gebruiken in andere tools naast Enterprise Architect, maar daar is geen ervaring mee. Ervaringen hierin zijn welkom! 

Het Gemeentelijk Gegevensmodel is beschikbaar in:

* XMI versie 1.1

Het is Getest en gebruikt in de volgende omgevingen:

* Enterprise Architect versie 14
* Enterprise Architect versie 15

## Opbouw Gemeentelijk Gegevensmodel
Het GGM kent een gelaagde opbouw, waarbij verschillende objecttypen over beleidsdomeinen heen zoveel mogelijk zijn ontkoppeld. Alleen objecttypen in de onderste lagen van het model worden gebruikt door de bovenliggende onderdelen.

### Beleidsterreinen
Het gegevensmodel omvat de volgende op de gebaseerde [IV3-taakvelden](https://www.rijksoverheid.nl/onderwerpen/financien-gemeenten-en-provincies/uitwisseling-financiele-gegevens-met-sisa-en-iv3/informatie-voor-derden-iv3):

* Burgerzaken
* Economie
* Griffie
* Leerplicht en Leerlingenvervoer
* Onderwijs
* Ruimte
  * Beheer Openbare Ruimte
  * Omgevingswet
  * Afval 
* Sport, Cultuur en Recreattie
  * Erfgoed, Archeologie
  * Erfgoed, Archief
  * Erfgoed, Monumenten
  * Museum
  * Sport
* Vergunningverlening, Toezicht en handhaving
  * Brede Handhaving
  * Bouwen en wonen
  * Overige vergunningen
* Volksgezonheid en milieu _(nog in ontwikkeling)_
* Bestuur en ondersteuning
  * ICT
  * Vastgoed
  * Financien
  * HR
  * Inkoop (_nog in ontwikkeling_)
  * Subsidies (_nog in ontwikkeling_)
  * Facilitair (_nog in ontwikkeling_)
  * Communicatie (_nog in ontwikkeling_)
  * Control (_nog in ontwikkeling_)
  * Organisatie Algemeen
* Dienstverlening
* Sociaal domein
  * Wmo
  * Jeugd
  * Participatie
  * Schuldhulpverlening
  * Sociale teams
  * Gemeentebegrafenissen
  * Dak- en thuislozen
* Verkeer en vervoer
  * Verkeer
  * Parkeren

Naast bovengenoemde beleidsterreinen kent het GGM het onderdeel 'Kern', waarin alle gedeelde objecttypen zijn te vinden. Kern is afgeleid van het [Informatiemodel Basis- en Kerngegevens (RSGB)](https://www.gemmaonline.nl/index.php/Informatiemodel_Basis-_en_Kerngegevens_(RSGB)) en [Informatiemodel Zaken (RGBZ)](https://www.gemmaonline.nl/index.php/Informatiemodel_Zaken_(RGBZ)) (beiden onderdeel [GEMMA: Gemeentelijke Modelarchitectuur](https://www.gemmaonline.nl/index.php/Gemeentelijke_Model_Architectuur_(GEMMA))), aangevuld met een aantal generieke objecttypen.  

## Totstandkoming Gemeentelijk Gegevensmodel

## Work in Progress

[importXMI]: https://github.com/brienen/Gemeentelijk-Gegevensmodel/blob/master/image/ImportPackage.png "Import XMI via tabblad Publish"
[selectFilename]: https://github.com/brienen/Gemeentelijk-Gegevensmodel/blob/master/image/SelectFilename.png "Select Filename"
[importPackage]: https://github.com/brienen/Gemeentelijk-Gegevensmodel/blob/master/image/ImportPackage.png "Import Package"
[openDiagram]: https://github.com/brienen/Gemeentelijk-Gegevensmodel/blob/master/image/OpenDiagram.png "Open Diagram"