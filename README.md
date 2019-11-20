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

![Gelaagdheid Domeinen][gelaagdheidDomeinen | width=300]

Het gegevensmodel is uitgewerkt in een aantal verticale beleidsdomeinen en 4 horizontale beleidsdomeinen. De horizontale delen (Kern, Financiën, ICT en Dienstverlening) vormen de basis van het gegevensmodel, waarop de verticale delen voortbouwen. De Kern bestaat uit RSGB en RGBZ, die de gegevensdefinities bevatten die zoals die gelden voor de basisregistraties (RSGB) en zaakgericht werken (RGBZ).  
Er is ontkoppeling tussen de verschillende (sub)domeinen nagestreefd, doordat in de gegevensdefinities van het gegevensmodel (sub)domeinen alleen definities uit onderliggende (sub)domeinen gebruiken. Zo gebruiken alle (sub)domeinen gegevensdefinities uit Kern en kunnen alle verticale (sub)domeinen gegevensdefinities gebruiken uit de 4 horizontale modellen.


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

Het GGM is ontworpen op aan de hand van interviews met domeinexperts, de in Delft gebruikte applicaties en op basis van landelijke informatiestandaarden. Dit om tot een gegevensmodel te komen dat goede verankering kent met de Delftse situatie. Aangezien alle Nederlandse gemeenten in principe dezelfde wettelijke taken hebben gaan we ervanuit dat de onderliggende informatiemodellen sterk op elkaar lijken. 

Uitgangspunt van de inventarisatie waren: 

1. De lijst met Delftse applicaties en de inventarisatie hiervan waarbij onderscheid is gemaakt tussen authentieke bronnen en overige applicaties
2. De set beleidsdomeinen waar de gemeente haar taakgebied heeft 
3. Landelijk vastgestelde standaarden voor gegevensuitwisseling en landelijk vastgestelde informatiemodellen  

De inventarisatie in de volgende stappen uitgevoerd:

1. Interviews met experts uit de verschillen de Beleidsdomeinen: per beleidsdomein is er m.b.v. gesprekken met experts van de informatievoorziening binnen de beleidsdomeinen een inventarisatie gemaakt van de gebruikte applicaties, de betrokken gebruikers, de interactie tussen de applicaties en de gebruikers, en welke gegvens daarbij gebruikt worden.
2. Applicaties en gegevens: door in de gesprekken en uit de analyse de authentieke bronnen  van gegevens te identificeren, door in de gesprekken in te zoomen op de gebruikte gegevens en door de inventarisatie van de applicaties en gegevens te hanteren zijn de gegevens binnen de authentieke bronnen geïdentificeerd.
3. Gegevensmodel: het gegevensmodel wordt opgebouwd door de in de vorige stap gevonden gegevens te vertalen naar objecttypen (gegevenssoorten). Landelijke standaarden dienen hier zoveel mogelijk als uitgangspunt. Veel van de gebruikte applicaties ondersteunen deze landelijke standaarden, waardoor compatibiliteit zo goed mogelijk wordt gegarandeerd. 
4. Databaseschema: er is generator gerealiseerd waarmee op basis van de definities in het gegevensmodel met ‘een druk op de knop’ databasetabellen gegenereerd kunnen worden. Hiermee is het mogelijk de basis te leggen voor een datawarehouse en is het mogelijk gegevens uit de applicaties te laden waardoor confrontatie van het model met de data mogelijk is.

![Aanpak GGM][aanpakGGM]


## Work in Progress

[importXMI]: https://github.com/brienen/Gemeentelijk-Gegevensmodel/blob/master/image/ImportPackage.png "Import XMI via tabblad Publish"
[selectFilename]: https://github.com/brienen/Gemeentelijk-Gegevensmodel/blob/master/image/SelectFilename.png "Select Filename"
[importPackage]: https://github.com/brienen/Gemeentelijk-Gegevensmodel/blob/master/image/ImportPackage.png "Import Package"
[openDiagram]: https://github.com/brienen/Gemeentelijk-Gegevensmodel/blob/master/image/OpenDiagram.png "Open Diagram"
[gelaagdheidDomeinen]: https://github.com/brienen/Gemeentelijk-Gegevensmodel/blob/master/image/GelaagdheidDomeinen.jpg "Gelaagdheid Domeinen"
[aanpakGGM]: https://github.com/brienen/Gemeentelijk-Gegevensmodel/blob/master/image/AanpakGGM.jpg | width=300 "Aanpak GGM"