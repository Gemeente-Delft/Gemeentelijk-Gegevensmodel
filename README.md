# Gemeentelijk Gegevensmodel

Het Gemeentelijk Gegevensmodel (GGM) is een logisch gegevensmodel met daarin vertegenwoordigd alle beleidsterreinen van de gemeente. Het GGM is ontwikkeld in opdracht van de Gemeente Delft ter ondersteuning van de visie op het gebied van informatiegestuurd werken. Onder andere wordt het GGM gebruikt als centraal datamodel in het datawarehouse. Hiertoe is een generator beschikbaar om het GGM te vertalen naar fysieke databasetabellen.

Het GGM omvat alle beleidsterreinen die onder de verantwoordelijkeheid van de gemeente vallen. Dit ongeacht de organisatorische inrichting, zoals de afdelingen die de bijbehorende taken uitvoeren en uitbesteding aan derde partijen. Deze beleidsterreinen zijn afgeleid van de [IV3-taakvelden](https://www.rijksoverheid.nl/onderwerpen/financien-gemeenten-en-provincies/uitwisseling-financiele-gegevens-met-sisa-en-iv3/informatie-voor-derden-iv3). 

Bij het GGM is een set _codegeneratietemplates_ ontwikkeld voor het genereren van fysieke datamodellen op basis van (onderdelen van) het GGM. Hiermee genereer je DDL voor Oracle en in ongeteste vorm voor MySQL. Het gaat hier om templates voor het [Code Template Framework](https://sparxsystems.com/enterprise_architect_user_guide/15.0/model_domains/codetemplates_2.html) van Enterprise Architect. Hiermee kan ook werkende DDL worden gegenereerd voor andere databases.

## Winnaar Gemeentedelers 2022

Gemeente Delft is winnaars van de [GemeenteDelers](https://www.gemeentedelers.nl) competitie van VNG Realisatie. Delft deed mee in de categorie Informatietechnologie met het Gemeentelijk Gegevensmodel (GGM). Met het GGM bouwen we aan een gezamenlijk datafundament dat informatie gestuurd werken ondersteund. En het goede nieuws: ook andere gemeenten kunnen gebruik maken van dit open source model.

<a href="https://youtu.be/LMmv2rwSd6I" target="_blank"> <img src="https://github.com/Gemeente-Delft/Gemeentelijk-Gegevensmodel/blob/master/Gemeentedelers.jpg" width="600"></a>

## Handleiding

**Voor gedetailleerde toelichting kijk in de [Handleiding](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/).**

## Installatie en gebruik

Het Gemeentelijk Gegevensmodel is beschikbaar in [XMI-vorm](https://www.omg.org/spec/XMI/About-XMI/), en is ontwikkeld in, en toegepast met [Enterprise Architect](https://sparxsystems.com).

### Installatie Gemeentelijk Gegevensmodel

We bieden het GGM in twee vormen aan:

1. Als [EAP-bestand](gemeentelijk%20gegevensmodel.eap), te gebruiken voor de gratis [Enterprise Architect Viewer](https://www.sparxsystems.eu/enterprise-architect/ea-lite-edition/). En natuurlijk de overige versies van Enterprise Architect. Download hiervoor het bestand _gemeentelijk%20gegevensmodel.xml_ en open het in (de viewer van) Enterprise Architect.
2. Als [XMI-bestand](gemeentelijk%20gegevensmodel.xml), om geladen te worden in een (nieuw) project in Enterprise Architect, of om geladen te worden in andere UML-tooling. Voor installatie-instructies kijk in de [handleiding](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/installatie/).

### Installatie Codegeneratietemplates

De installatie van de codegeneratietemplates staat [hier](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/generatie#installeren-codegeneratietemplates) beschreven. Voor verdere uitleg rond het gebruik van de codegeneratietemplates kijk [hier](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/generatie).

### Versies en gebruikte tooling

Het XMI-bestand van het Gemeentelijk Gegevensmodel is in theorie te gebruiken in andere tools naast Enterprise Architect, maar daar is geen ervaring mee. Ervaringen hierin zijn welkom! 

Het Gemeentelijk Gegevensmodel is beschikbaar in:

* [XMI versie 1.1](https://www.omg.org/spec/XMI/About-XMI/) en
* [XMI versie 2.1](https://www.omg.org/spec/XMI/About-XMI/)

Het is Getest en gebruikt in de volgende omgevingen:

* [Enterprise Architect versie 14](https://sparxsystems.com/products/ea/14/index.html)
* [Enterprise Architect versie 15](https://sparxsystems.com/products/ea/15/index.html)
* [Enterprise Architect Viewer](https://www.sparxsystems.eu/enterprise-architect/ea-lite-edition/)

## Opbouw Gemeentelijk Gegevensmodel

Het GGM kent een gelaagde opbouw, waarbij verschillende objecttypen over beleidsdomeinen heen zoveel mogelijk zijn ontkoppeld. Alleen objecttypen in de onderste lagen van het model worden gebruikt door de bovenliggende onderdelen.

![Gelaagdheid Domeinen][gelaagdheidDomeinen]

Het gegevensmodel is uitgewerkt in een aantal verticale beleidsdomeinen en 4 horizontale beleidsdomeinen. De horizontale delen (Kern, Financiën, ICT en Dienstverlening) vormen de basis van het gegevensmodel, waarop de verticale delen voortbouwen. De Kern bestaat uit RSGB en RGBZ, die de gegevensdefinities bevatten die zoals die gelden voor de basisregistraties (RSGB) en zaakgericht werken (RGBZ).  
Er is ontkoppeling tussen de verschillende (sub)domeinen nagestreefd, doordat in de gegevensdefinities van het gegevensmodel (sub)domeinen alleen definities uit onderliggende (sub)domeinen gebruiken. Zo gebruiken alle (sub)domeinen gegevensdefinities uit Kern en kunnen alle verticale (sub)domeinen gegevensdefinities gebruiken uit de 4 horizontale modellen.

### Beleidsterreinen

Het gegevensmodel omvat de volgende op de gebaseerde [IV3-taakvelden](https://www.rijksoverheid.nl/onderwerpen/financien-gemeenten-en-provincies/uitwisseling-financiele-gegevens-met-sisa-en-iv3/informatie-voor-derden-iv3):

* [Burgerzaken](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/domeinen/burgerzaken/)
* [Economie](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/domeinen/economie/)
* [Griffie](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/domeinen/griffie/)
* [Leerplicht en Leerlingenvervoer](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/domeinen/leerplicht/)
* [Onderwijs](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/domeinen/onderwijs/)
* Ruimte
  * [Beheer Openbare Ruimte](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/domeinen/ruimteAlgemeen/)
  * [Omgevingswet](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/domeinen/omgevingswet/)
  * [Afval](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/domeinen/afval/)
* Sport, Cultuur en Recreatie
  * [Erfgoed, Archeologie](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/domeinen/archeologie/)
  * [Erfgoed, Archief](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/domeinen/archief/)
  * [Erfgoed, Monumenten](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/domeinen/monumenten/)
  * [Museum](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/domeinen/museum/)
  * [Sportbeleid](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/domeinen/sport/)
* Vergunningverlening, Toezicht en handhaving
  * [Brede Handhaving](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/domeinen/vth/#brede-handhaving)
  * [Bouwen en wonen](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/domeinen/vth/#vergunningaanvragen)
  * [Overige vergunningen](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/domeinen/vth/#vergunningaanvragen)
* Volksgezondheid en milieu _(nog in ontwikkeling)_
* Bestuur en ondersteuning
  * [ICT](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/domeinen/ict/)
  * [Gemeentelijk Vastgoed](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/domeinen/vastgoed/)
  * [Financiën](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/domeinen/financien/)
  * [HR](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/domeinen/hr/)
  * [Inkoop](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/domeinen/inkoop/)
  * [Subsidies](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/domeinen/subsidies/)
  * Facilitair (_nog in ontwikkeling_)
  * Communicatie (_nog in ontwikkeling_)
  * Control (_nog in ontwikkeling_)
* [Dienstverlening](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/domeinen/dienstverlening/)
* Sociaal domein
  * [Wmo](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/domeinen/wmojeugd/)
  * [Jeugd](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/domeinen/wmojeugd/)
  * [Participatie](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/domeinen/participatie/)
  * [Schuldhulpverlening](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/domeinen/schuldhulp/)
  * [Sociale teams](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/domeinen/socteam/)
  * [Gemeentebegraven](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/domeinen/gemeentebegraven/)
  * [Dak- en thuislozen](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/domeinen/participatie/#dak-en-thuislozen)
* Verkeer en vervoer
  * [Verkeer](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/domeinen/verkeer/)
  * [Parkeren](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/domeinen/parkeren/)

Naast bovengenoemde beleidsterreinen kent het GGM het onderdeel 'Kern', waarin alle gedeelde objecttypen zijn te vinden. Kern is afgeleid van het [Informatiemodel Basis- en Kerngegevens (RSGB)](https://www.gemmaonline.nl/index.php/Informatiemodel_Basis-_en_Kerngegevens_(RSGB)) en [Informatiemodel Zaken (RGBZ)](https://www.gemmaonline.nl/index.php/Informatiemodel_Zaken_(RGBZ)) (beiden onderdeel [GEMMA: Gemeentelijke Modelarchitectuur](https://www.gemmaonline.nl/index.php/Gemeentelijke_Model_Architectuur_(GEMMA))), aangevuld met een aantal generieke objecttypen.  

### Toegepaste Landelijke standaarden

Nederland kent op dit moment een lappendeken aan standaarden voor gegevensuitwisseling en informatiemodellen. Samenhang tussen deze standaarden en is beperkt. Relevante standaarden  zoveel mogelijk in samenhang binnen de afzonderlijke domeinen in het GGM opgenomen. Het stelsel van basisregistraties, en het daarop gerichte RSGB geven hiervoor wel enige houvast. In het GGM heeft het RSGB daarom een centrale plek.

De volgende standaarden zijn gebruikt bij de totstandkoming van het GGM, en maken onderdeel uit van het GGM:

* [Informatiemodel Basis- en Kerngegevens (RSGB)](https://www.gemmaonline.nl/index.php/Informatiemodel_Basis-_en_Kerngegevens_(RSGB)) versie 2.0.2. Het RSGB is as-is gebruikt in het onderdeel _Kern_ van het GGM. 
* [Informatiemodel Zaken (RGBZ)](https://www.gemmaonline.nl/index.php/Informatiemodel_Zaken_(RGBZ)) versie 1.0. Het RGBZ is as-is gebruikt in het onderdeel _Kern_ van het GGM.  
* [iWmo](https://istandaarden.nl/istandaarden/iwmo) versie 2.3. iWmo is een berichtenstandaard voor het uitwisselen van gegevens tussen zorgaanbieders en gemeenten met achterliggend informatiemodel. Dit informatiemodel vormt samen met de iJw-standaard de basis voor het Jeugd- en Wmo-deel van het beleidsdomein _Sociaal Domein_. Deze zijn in de uitwerking aangevuld met diverse objecttypen.
* [iJw](https://istandaarden.nl/istandaarden/ijw) versie 2.3. Zie iWmo.
* [iPgb](https://istandaarden.nl/istandaarden/ipgb/werken-met-ipgb-10) versie 1.0. Hiervan zijn de informatiemodellen van  toekenningsbericht (TKB) en het budgetafsluitbericht (BAB) toegepast.
* [Suwi Gegevensregister (SGR)](https://www.bkwi.nl/producten/suwinet-services/suwinet-standaarden/suwi-gegevensregister-sgr) versie 4.0. Het SGR is een gegevensmodel uit de keten van Werk en Inkomen dat dient als een gemeenschappelijk gedragen kader waarop de berichten uit het [SuwiML](https://www.bkwi.nl/producten/suwinet-services/suwinet-standaarden/suwi-gegevensregister-sgr/meer-informatie-over-suwiml) zijn gebaseerd. Er is gebruik gemaakt van het berichtenschema (XSD's) op basis waarvan de relevante objecttypen zijn afgeleid.
* [Informatiemodel Beheer Openbare Ruimte (IMBOR)](https://www.crow.nl/thema-s/management-openbare-ruimte/imbor) versie 1.2.04. Het (IMBOR) bevat de afspraken over de benamingen en definities van de beheergegevens die aan de objecten in de openbare ruimte gekoppeld kunnen worden. Dit inclusief de samenhang tussen deze gegevens. De objecttypen uit de Basisregistratie Grootschalige Topografie (BGT) en het Informatiemodel geografie (IMGeo) vormen de basis. Beiden maken onderdeel uit van het RSGB. In het GGM is een koppeling gemaakt tussen de objecten uit het RSGB en IMBOR.
* [Standaard- en informatiemodel toepasbare regels (STTR en IMTR)](https://aandeslagmetdeomgevingswet.nl/digitaal-stelsel/technisch-aansluiten/koppelvlakken/toepasbare-regels/standaard/) versie 1.02. In het kader van de omgevingswet zijn toepasbare regels uitgewerkt conform STTR en IMTR. Deze worden toegepast om vragenbomen in het Omgevingsloket te laten zien. Deze is vanwege de beperkte rijkwijdte slechts beperkt overgenomen.
* [Standaard en informatiemodel aanvragen en meldingen (STAM en IMAM)](https://aandeslagmetdeomgevingswet.nl/digitaal-stelsel/technisch-aansluiten/koppelvlakken/vergunningen/standaard/) versie 0.9. De Standaard aanvragen en meldingen (STAM) en het bijbehorende informatiemodel (IMAM) helpen bij het afleveren van een vergunningaanvraag of melding in het kader van de omgevingswet bij overheden.
* [Standaard officiële publicaties (STOP/TPOD)](https://aandeslagmetdeomgevingswet.nl/digitaal-stelsel/technisch-aansluiten/koppelvlakken/omgevingsdocumenten/standaard-officiele/) Versie 0.98beta. Voor het valideren en publiceren van omgevingswetbesluiten. Vanwege de beperkte rijkweidte is deze slechts beperkt overgenomen.  
* [Conceptueel Informatiemodel Omgevingswet CIMOW](https://www.geonovum.nl/over-geonovum/actueel/cimow-en-imow-versie-098-beta-beschikbaar) Versie CIMOW v0.98-kern. Het Conceptueel Informatiemodel voor de Omgevingswet (CIMOW) beschrijft het domein van de Omgevingswet. Dit beperkt zich tot de informatie die in dit domein wordt vastgelegd en vastgesteld en in ketens wordt uitgewisseld ten behoeve van het digitaal stelsel van de Omgevingswet (DSO).
* [GML 3.2.1. (Geography Markup Language)](https://www.geonovum.nl/geo-standaarden/geography-markup-language-gml/gml-encoding-standard-321), GML beschrijft hoe geografische locaties, lijnen, vlakken en combinaties daartussen vastgelegd en uitgewisseld dienen te worden. GML 3.2.1 is gestandaardiseerd bij het OGC en, daar OGC en ISO met elkaar samenwerken, tevens gestandaardiseerd als ISO 19136:2007. De ISO variant is opgenomen als nationale standaard in de Pas-toe-of-leg-uit-lijst van het Forum Standaardisatie.
* [NEN3610: 2011 (Basismodel geo-informatie)](https://www.geonovum.nl/geo-standaarden/nen-3610-basismodel-voor-informatiemodellen). Het Basismodel geo-informatie. Het bevat de termen, definities, relaties en algemene regels voor de uitwisseling van informatie over ruimtelijke objecteninformatiemodellen). De standaard NEN3610 staat op de Pas-toe-of-leg-uit-lijst van het Forum Standaardisatie.
* [IMBGT/IMGeo versie 2.1.1: (Informatiemodel Basisregistratie grootschalige Topografie/ Informatiemodel Geo)](https://www.geonovum.nl/geo-standaarden/bgt-imgeo/gegevenscatalogus-imgeo-versie-211). De kern van dit model (BGT) definieert informatie zoals die via de BGT beschikbaar is, en als basis/ondergrond dient voor de overige modellen. 
* [IMBAG versie 0.99: (Gegevenscatalogus Basisregistratie Adressen en Gebouwen)](https://www.geonovum.nl/geo-standaarden/informatiemodellen-nen3610-familie/gegevenscatalogus-basisregistratie-adressen-en). De Basisregistraties Adressen en Gebouwen (BAG) bevatten gegevens van alle adressen en gebouwen in Nederland. In de Gegevenscatalogus BAG zijn de afspraken vastgelegd om digitale uitwisseling mogelijk te maken. Het informatiemodel voor de BAG is geënt op de principes van NEN3610.
* [MIM (Metamodel voor Informatiemodellen)](https://www.geonovum.nl/geo-standaarden/metamodel-informatiemodellering-mim). Deze is toegepast in de uitwerking van het ICT-deel. Het GGM is echter (nog) niet MIM-compliant.
* [RiHA 2.0 (Gegevensmodel toezicht en handhaven)](https://www.pleio.nl/pages/view/52755822/riha-referentieinformatiemodel-handhaving). Toegepast in de uitwerking van Vergunningverlening, toezicht en handhaving.


## Totstandkoming Gemeentelijk Gegevensmodel

Het GGM is ontworpen op aan de hand van interviews met domeinexperts, de in Delft gebruikte applicaties en op basis van landelijke informatiestandaarden. Dit om tot een gegevensmodel te komen dat goede verankering kent met de Delftse situatie. Aangezien alle Nederlandse gemeenten in principe dezelfde wettelijke taken hebben gaan we ervanuit dat de onderliggende informatiemodellen sterk op elkaar lijken. 

Uitgangspunt van de inventarisatie waren: 

1. De lijst met Delftse applicaties en de inventarisatie hiervan waarbij onderscheid is gemaakt tussen authentieke bronnen en overige applicaties
2. De set beleidsdomeinen waar de gemeente haar taakgebied heeft 
3. Landelijk vastgestelde standaarden voor gegevensuitwisseling en landelijk vastgestelde informatiemodellen  

De inventarisatie in de volgende stappen uitgevoerd (voor een gedetailleerde uitleg: kijk in de [handleiding](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/totstandkoming/)):

1. Interviews met experts uit de verschillen de Beleidsdomeinen: per beleidsdomein is er m.b.v. gesprekken met experts van de informatievoorziening binnen de beleidsdomeinen een inventarisatie gemaakt van de gebruikte applicaties, de betrokken gebruikers, de interactie tussen de applicaties en de gebruikers, en welke gegevens daarbij gebruikt worden.
2. Applicaties en gegevens: door in de gesprekken en uit de analyse de authentieke bronnen  van gegevens te identificeren, door in de gesprekken in te zoomen op de gebruikte gegevens en door de inventarisatie van de applicaties en gegevens te hanteren zijn de gegevens binnen de authentieke bronnen geïdentificeerd.
3. Gegevensmodel: het gegevensmodel wordt opgebouwd door de in de vorige stap gevonden gegevens te vertalen naar objecttypen (gegevenssoorten). Landelijke standaarden dienen hier zoveel mogelijk als uitgangspunt. Veel van de gebruikte applicaties ondersteunen deze landelijke standaarden, waardoor compatibiliteit zo goed mogelijk wordt gegarandeerd. 
4. Databaseschema: er is generator gerealiseerd waarmee op basis van de definities in het gegevensmodel met ‘een druk op de knop’ databasetabellen gegenereerd kunnen worden. Hiermee is het mogelijk de basis te leggen voor een datawarehouse en is het mogelijk gegevens uit de applicaties te laden waardoor confrontatie van het model met de data mogelijk is.

![Aanpak GGM 1][aanpakGGM]

[importXMI]: docs/image/ImportPackage.png "Import XMI via tabblad Publish"
[selectFilename]: docs/image/SelectFilename.png "Select Filename"
[importPackage]: docs/image/ImportPackage.png "Import Package"
[openDiagram]: docs/image/OpenDiagram.png "Open Diagram"
[gelaagdheidDomeinen]: docs/image/GelaagdheidDomeinen.jpg "Gelaagdheid Domeinen"
[aanpakGGM]: docs/image/AanpakGGM.jpg "Aanpak GGM"
[importRefData]: docs/image/ImportRefData.png "Import Referencedata"
[kiesTemplates]: docs/image/KiesTemplates.png "Kies templates"
[gebruikTemplates]: docs/image/GebruikTemplates.png "Gebruik templates"
