# Gemeentelijk Gegevensmodel

Het Gemeentelijk Gegevensmodel (GGM) is een logisch gegevensmodel met daarin vertegenwoordigd alle beleidsterreinen van de gemeente. Het GGM is ontwikkeld in opdracht van de Gemeente Delft ter ondersteuning van de visie op het gebied van informatiegestuurd werken. Onder andere wordt het GGM gebruikt als centraal datamodel in het datawarehouse. Hiertoe is een generator beschikbaar om het GGM te vertalen naar fysieke databasetabellen.

Het GGM omvat alle beleidsterreinen die onder de verantwoordelijkheid van de gemeente vallen. Dit ongeacht de organisatorische inrichting, zoals de afdelingen die de bijbehorende taken uitvoeren en uitbesteding aan derde partijen. Deze beleidsterreinen zijn afgeleid van de [IV3-taakvelden](https://www.rijksoverheid.nl/onderwerpen/financien-gemeenten-en-provincies/uitwisseling-financiele-gegevens-met-sisa-en-iv3/informatie-voor-derden-iv3).

Bij het GGM is een set _codegeneratietemplates_ ontwikkeld voor het genereren van fysieke datamodellen op basis van (onderdelen van) het GGM. Hiermee genereer je DDL voor Oracle en in ongeteste vorm voor MySQL. Het gaat hier om templates voor het [Code Template Framework](https://sparxsystems.com/enterprise_architect_user_guide/15.0/model_domains/codetemplates_2.html) van Enterprise Architect. Hiermee kan ook werkende DDL's worden gegenereerd voor andere databases.

## Winnaar Gemeentedelers 2022

Gemeente Delft is winnaar van de [GemeenteDelers](https://www.gemeentedelers.nl) competitie van VNG Realisatie. Delft deed mee in de categorie Informatietechnologie met het Gemeentelijk Gegevensmodel (GGM). Met het GGM bouwen we aan een gezamenlijk datafundament dat informatie gestuurd werken ondersteund. En het goede nieuws: ook andere gemeenten kunnen gebruik maken van dit open source model.

<a href="https://youtu.be/LMmv2rwSd6I" target="_blank"> <img src="https://github.com/Gemeente-Delft/Gemeentelijk-Gegevensmodel/blob/master/Gemeentedelers.jpg" width="600"></a>

## Goud-status Common Ground

De Expert Review Groep van de Common Ground heeft het initiatief GGM besproken en besloten het initiatief de classificatie Goud te geven op het [Common Ground portfolio](https://commonground.nl/page/view/b68441ec-e536-4f81-82d8-ce6f3d6606a9/portfolio). Deze classificatie is gerelateerd aan de toets op de architectuur en realisatie principes. We zijn tot deze conclusie gekomen op basis van de ontvangen antwoorden. 

## Beheer en doorontwikkeling

Beheer en doorontwikkeling van het GGM verloopt in samenwerking met diverse gemeenten in combinatie met andere overheden. Hiervoor is een gebruikersgroep ingericht die je kunt vinden op de volgende [Pleio-pagina](https://kennisnetwerkdata.pleio.nl/groups/view/1e7df5c5-e537-46cd-9d09-de2ef29beef8/gemeentelijk-gegevensmodel-ggm). Deze Pleio-pagina is het kanaal voor alle vragen, blogs en discussies over het GGM. Heb je een vraag of een toevoeging meld die dan via onze Pleio-pagina. Een aantal keer per jaar organiseren we mini-conferenties over onderdelen van het GGM, de agenda hiervoor vind je ook op PLeio. Voor het steeds beter maken van het GGM is er een expertgroep met daarin meerdere gemeenten en de VNG (Vereniging Nederlandse Gemeenten), die werk verdelen en zo gezamenlijk het GGM steeds beter maken.  

## Handleiding

**Voor gedetailleerde toelichting kijk in de [Handleiding](https://www.gemeentelijkgegevensmodel.nl/).**

## Installatie en gebruik

Het Gemeentelijk Gegevensmodel is beschikbaar in [XMI-vorm](https://www.omg.org/spec/XMI/About-XMI/), en is ontwikkeld in, en toegepast met [Enterprise Architect](https://sparxsystems.com). Een aantal gemeenten gebruikt het GGM inmiddels ook met [Bizzdesign EnterpriseStudio](https://bizzdesign.com), en ook met [Blue Dolphin](https://www.valueblue.com/bluedolphin).

Let op: gebruik je Enterprise Acrhitect versie 16 of 17 ? In dit geval moet je het bestand 'gemeentelijk gegevensmodel EA.qea' gebruiken. Gebruik je versie 15, laad dan het bestand 'xmi' bestand.

Let op: Het Gemeentetelijk Gegevensmodel is een [UML-model](http://www.uml.org) en bevat daarmee alle benodigde details zoals de attributen en bijbehorende datatypes. Er is ook een [Archimate-versie](https://prod.opengroup.org/archimate-forum/archimate-overview) beschikbaar die gebruikt wordt voor de GEMMA en die gebruikt kan worden voor Enterprise Architectuur; deze bevat echter niet alle details omdat Archimate niet hetzelfde detail kent als UML.    

### Installatie Gemeentelijk Gegevensmodel

Van het Gemeentelijk Gegevensmodel zijn verschillende versies beschikbaar: v1.0.3, v2.0.0, v2.1.0, v2.2.0 en de courante versie v2.3.0. Je vindt deze in de afzonderlijke versies van de repository. De hierna volgende uitleg betreft de laatste versie van het GGM. Hieronder vind je de installatiebeschrijving bij de verschillende ondersteunde tools:

1. [Enterprise Architect Viewer](https://sparxsystems.com/products/ea/downloads.html) of [Enterprise Architect versie 16 of 17](https://sparxsystems.com/products/ea/16.1/index.html): download hiervoor het bestand [QEA-bestand](./v2.2.0/) en open het in (de viewer van) Enterprise Architect.
2. [Enterprise Architect versie 16](https://sparxsystems.com/products/ea/16.0/): de EAPX van versie 15 wordt niet meer ondersteund in de nieuwe release. Wil je het GGM alsnog in versie 15 laden, dan kan dat via het XMI bestand.
3. Als [XMI-bestand in Enterprise Architect 16 en 17](./v2.2.0/Gemeentelijk%20Gegevensmodel%20XMI2.1.xml), om geladen te worden in een (nieuw) project in Enterprise Architect, of om geladen te worden in andere UML-tooling. Voor installatie-instructies kijk in de [handleiding](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/installatie/).
4. [Bizzdesign](https://bizzdesign.com): voor installatie-instructies kijk in de [handleiding laden in Bizzdesign](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/installatie/#installatie-gemeentelijk-gegevensmodel-in-bizzdesign) 
5. [Blue Dolphin](https://www.valueblue.com/bluedolphin): hiervoor gebruik je het [AMEFF-bestand](https://github.com/VNG-Realisatie/GEMMA-GGM-Archi-repository/blob/develop/exports/GEMMA-GGM%20AMEFF.xml) van het GGM uit de GEMMA-repository voor de Architectuur module van BlueDolphin. Als BlueDolphin gebruiker met Beheerderrol kun je AMEFF-bestanden uploaden. Zie hiervoor de [handleiding: AMEFF bestanden importeren](https://support.valueblue.nl/hc/nl/articles/360013407860-AMEFF-bestanden-importeren-naar-BlueDolphin). Bij vragen contacteer jouw ValueBlue account- of customersuccess-manager.

### Installatie Codegeneratietemplates

De installatie van de codegeneratietemplates staat [hier](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/generatie#installeren-codegeneratietemplates) beschreven. Voor verdere uitleg rond het gebruik van de codegeneratietemplates kijk [hier](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/generatie).

De codegeneratietemplates zijn alleen beschikbaar voor Enterprise Architect.

### Versies en gebruikte tooling

Het XMI-bestand van het Gemeentelijk Gegevensmodel is in theorie te gebruiken in andere tools naast Enterprise Architect, maar daar is geen ervaring mee. Ervaringen hierin zijn welkom!

Het Gemeentelijk Gegevensmodel is beschikbaar in:

* [XMI versie 2.1](https://www.omg.org/spec/XMI/About-XMI/)

Het is Getest en gebruikt in de volgende omgevingen:

* [Enterprise Architect versie 16](https://sparxsystems.com/products/ea/16.0/)
* [Enterprise Architect versie 17](https://sparxsystems.com/products/ea/17.0/)
* [Enterprise Architect Viewer](https://sparxsystems.com/products/ea/trial/request.html)
* [Bizzdesign EnterpriseStudio](https://bizzdesign.com)
* [Blue Dolphin](https://www.valueblue.com/bluedolphin)

## Opbouw Gemeentelijk Gegevensmodel

Het GGM kent een gelaagde opbouw, waarbij verschillende objecttypen over beleidsdomeinen heen zoveel mogelijk zijn ontkoppeld. Alleen objecttypen in de onderste lagen van het model worden gebruikt door de bovenliggende onderdelen.

![Gelaagdheid Domeinen][gelaagdheidDomeinen]

Het gegevensmodel is uitgewerkt in een aantal verticale beleidsdomeinen en 4 horizontale beleidsdomeinen. De horizontale delen (Kern, Financiën, ICT en Dienstverlening) vormen de basis van het gegevensmodel, waarop de verticale delen voortbouwen. De Kern bestaat uit RSGB en RGBZ, die de gegevensdefinities bevatten die zoals die gelden voor de basisregistraties (RSGB) en zaakgericht werken (RGBZ).  
Er is ontkoppeling tussen de verschillende (sub)domeinen nagestreefd, doordat in de gegevensdefinities van het gegevensmodel (sub)domeinen alleen definities uit onderliggende (sub)domeinen gebruiken. Zo gebruiken alle (sub)domeinen gegevensdefinities uit Kern en kunnen alle verticale (sub)domeinen gegevensdefinities gebruiken uit de 4 horizontale modellen.

### Beleidsdomeinen

Het gegevensmodel omvat de volgende op de gebaseerde [IV3-taakvelden](https://www.rijksoverheid.nl/onderwerpen/financien-gemeenten-en-provincies/uitwisseling-financiele-gegevens-met-sisa-en-iv3/informatie-voor-derden-iv3):

* **Bestuur, politiek en ondersteuning**: Domein dat gegevens bevat die worden vastgelegd bij en voortkomen uit bestuurlijke en politieke processen en  beleidsvorming en gegevens die in het kader van de gemeentelijke taak rond burgerzaklen worden vastgelegd. 
    * **[Burgerzaken](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/v2.3.0/domeinen/burgerzaken)**: Het informatiedomein dat gegevens omvat over de registratie en dienstverlening met betrekking tot de persoonlijke levenssfeer van inwoners, gericht op het vastleggen en verstrekken van officiële documenten en informatie.
    * [Griffie](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/v2.3.0/domeinen/griffie): Het informatiedomein dat gegevens omvat over de ondersteuning van de gemeenteraad en de organisatie van raadsprocessen, gericht op het faciliteren van besluitvorming en democratische controle.
* **Veiligheid en vergunningven**: Het informatiedomein dat gegevens omvat over het waarborgen van veiligheid, handhaving van regels en crisisbeheersing.
    * **[Openbare orde en veiligehid](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/v2.3.0/domeinen/vth/#brede-handhaving)**: Het informatiedomein dat gegevens omvat over de gemeentelijke taken op het gebied van openbare orde en veiligheid. Dit omvat onder andere toezicht en handhaving van de openbare orde, de inzet van BOA’s en stadswachten, de uitvoering van de Wet Bibob en de bestuurlijke aanpak van georganiseerde criminaliteit. Daarnaast omvat het domein gegevens over criminaliteitspreventie, de handhaving van de Algemene Plaatselijke Verordening (APV), vergunningverlening in het kader van onder andere evenementen en horeca, en beleid en toezicht op conventionele explosieven.
    * **[Bouwvergunningen](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/v2.3.0/domeinen/vth/#vergunningaanvragen)**: Het informatiedomein dat gegevens omvat over de aanvraag, beoordeling en afgifte van vergunningen voor bouwactiviteiten, zoals bouwen, verbouwen of slopen.
    * **[Overige gemeentelijke vergunningen](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/v2.3.0/domeinen/vth/#vergunningaanvragen)**: Het informatiedomein dat gegevens bevat over de aanvraag, beoordeling en voorwaarden van diverse gemeentelijke vergunningen voor activiteiten in de openbare ruimte.
* **Verkeer, vervoer en waterstaat**: Het informatiedomein dat gegevens omvat over infrastructuur, mobiliteit en waterbeheer ter ondersteuning van bereikbaarheid en transportefficiëntie.
    * **[Mobiliteit](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/v2.3.0/domeinen/mobiliteit)**: Het informatiedomein dat de structuur, definities en relaties van gegevens omvat met betrekking tot verkeer en vervoer van personen en goederen, gericht op het faciliteren van efficiënte en duurzame mobiliteit.
    * **[Parkeren](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/v2.3.0/domeinen/parkeren)**: Het informatiedomein dat gegevens omvat over het stilstaan van voertuigen op een daarvoor bestemde plaats, met als doel het reguleren van parkeerruimte en het bevorderen van leefbaarheid, bereikbaarheid en mobiliteit binnen de gemeente.
* **[Economie](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/v2.3.0/domeinen/economie)**: Het informatiedomein dat gegevens omvat over economische ontwikkeling, bedrijvigheid en innovatie.
* **Onderwijs**: Het informatiedomein dat gegevens omvat over onderwijsvoorzieningen, leerlingenstromen, taken in het onderwijsveld  en educatieve ondersteuning.
    * **[Leerplicht en Leerlingenvervoer](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/v2.3.0/domeinen/leerplicht)**: Het informatiedomein dat gegevens omvat over de naleving van de leerplichtwet en de organisatie van leerlingenvervoer, gericht op het waarborgen van toegang tot onderwijs voor alle kinderen en jongeren.
    * **[Onderwijs](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/v2.3.0/domeinen/onderwijs)**: Het informatiedomein dat gegevens omvat over het funderend onderwijs, gericht op het waarborgen van toegang tot en kwaliteit van primair en voortgezet onderwijs voor kinderen en jongeren.
* **Sport, Cultuur en Recreatie**: Het informatiedomein dat gegevens omvat over taken in het kader van erfgoed, sportieve activiteiten, culturele voorzieningen en recreatieve mogelijkheden.
    * **Erfgoed**
        * **[Archeologie](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/v2.3.0/domeinen/archeologie)**: Het informatiedomein dat gegevens omvat over archeologische opgravingen, onderzoeken en besluitvorming, gericht op het behoud, de bescherming en de ontsluiting van archeologisch erfgoed binnen de kaders van de Erfgoedwet.
        * **[Archief](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/v2.3.0/domeinen/archief)**: Het informatiedomein dat gegevens omvat over de vorming, het beheer, de toegankelijkheid en de duurzame bewaring van archieven, inclusief documenten en collecties van cultuurhistorische waarde.
        * **[Monumenten](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/v2.3.0/domeinen/monumenten)**: Het informatiedomein dat gegevens omvat over de aanwijzing, bescherming en instandhouding van monumenten, inclusief gebouwen, objecten en landschappen, die van cultuurhistorische, wetenschappelijke of esthetische waarde zijn.
    * **[Musea](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/v2.3.0/domeinen/musea)**: Het informatiedomein dat gegevens omvat over de verwerving, het beheer, het onderzoek en de presentatie van museale collecties en tentoonstellingen binnen een overheidsorganisatie.
    * **[Sport](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/v2.3.0/domeinen/sport)**: Het informatiedomein dat gegevens omvat over sportbeleid, sportaccommodaties en activiteiten gericht op het stimuleren van sport en bewegen, met als doel de gezondheid, sociale cohesie en participatie van inwoners te bevorderen.
* **Sociaal domein**: Het informatiedomein dat gegevens omvat over zorg en ondersteuning welzijn en maatschappelijke participatie ter ondersteuning van individuen of groepen.
    * **[Wmo](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/v2.3.0/domeinen/wmojeugd)**: Het informatiedomein dat gegevens omvat over de ondersteuning en zorg die gemeenten bieden aan burgers om hun zelfredzaamheid en participatie in de maatschappij te bevorderen in het kader van de WMO, met als doel mensen zo lang mogelijk zelfstandig thuis te laten wonen.
    * **[Jeugd](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/v2.3.0/domeinen/wmojeugd)**: Het informatiedomein dat gegevens omvat over de ondersteuning, hulp en bescherming van jeugdigen en hun gezinnen, gebaseerd op de Jeugdwet.
    * **[Inkomen](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/v2.3.0/domeinen/inkomen)**: Het informatiedomein dat gegevens omvat over inkomensvoorzieningen, -regelingen en financiële ondersteuning voor inwoners, gericht op het waarborgen van bestaanszekerheid en participatie in de samenleving.
    * **[Werk](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/v2.3.0/domeinen/werk)**: Het informatiedomein dat gegevens omvat over de ondersteuning van mensen bij het vinden en behouden van werk, gebaseerd op de Participatiewet en gericht op het bevorderen van arbeidsparticipatie.
    * **[Schuldhulpverlening](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/v2.3.0/domeinen/schuldhulp)**: Het informatiedomein dat gegevens omvat over de ondersteuning en begeleiding van inwoners met problematische schulden, gericht op het bevorderen van financiële stabiliteit en maatschappelijke participatie.
    * **[Sociale teams](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/v2.3.0/domeinen/socteam)**: Het informatiedomein dat gegevens omvat over de integrale ondersteuning en hulpverlening die sociale teams bieden aan inwoners, gericht op het bevorderen van zelfredzaamheid, participatie en het oplossen van complexe problemen.
    * **[Gemeentebegraffennissen](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/v2.3.0/domeinen/gemeentebegraven)**: Het informatiedomein dat gegevens omvat over gemeentelijke uitvaarten, uitgevoerd wanneer niemand anders in de lijkbezorging voorziet, zoals vastgelegd in de Wet op de lijkbezorging.
    * **[Dak- en thuislozen](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/v2.3.0/domeinen/dakloos)**: Het informatiedomein dat gegevens omvat over mensen zonder vaste woon- of verblijfplaats, gericht op het in kaart brengen van de omvang, kenmerken en ondersteuningsbehoeften van deze doelgroep.
    * **[Inburgering](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/v2.3.0/domeinen/inburgering)**: Het informatiedomein dat gegevens omvat over de uitvoering van de Wet inburgering, gericht op het ondersteunen van inburgeraars bij hun integratie en participatie in de Nederlandse samenleving.
    * **Jeugdbescherming en -reclassering**: Het informatiedomein dat gegevens omvat over de uitvoering van kinderbeschermingsmaatregelen, gericht op het waarborgen van een veilige ontwikkeling van kinderen en jongeren.
* **Volksgezondheid en milieu**: Het informatiedomein dat gegevens omvat over volksgezondheid, afvalbeheer en milieubescherming.
    * **[Afval](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/v2.3.0/domeinen/afval)**: Het informatiedomein dat gegevens bevat over de gemeentelijke taken ten aanzien van inzameling en verwerking van bedrijfs- en huishoudelijk afval
* **Volkshuisvesting, leefomgeving en stedelijke vernieuwing**: Het informatiedomein dat gegevens omvat over huisvesting, ruimtelijke inrichting en verbetering van de leefomgeving in stedelijke of landelijke gebieden. 
    * **[Openbare ruimte](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/v2.3.0/domeinen/ruimteAlgemeen)**: "Het informatiedomein dat gegevens omvat over: 1. De fysieke objecten in de publieke buitenruimte, inclusief hun kenmerken, locatie en conditie. 2. De processen en activiteiten gericht op het onderhouden, inrichten en beheren van deze objecten."
    * **[Bouwen en wonen](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/v2.3.0/domeinen/bouwenenwonen)**: Het informatiedomein dat gegevens omvat over de planning, ontwikkeling en uitvoering van woningbouwprojecten, gericht op het realiseren van voldoende, betaalbare en duurzame woningen.
    * **[Omgevingswet](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/v2.3.0/domeinen/omgevingswet)**: Het informatiedomein dat gegevens omvat over de uitvoering van de Omgevingswet, gericht op het integraal beheren en ontwikkelen van de fysieke leefomgeving.
    * **Melding openbare ruimte**: Het informatiedomein dat gegevens omvat over meldingen van inwoners of organisaties betreffende zaken die niet in orde zijn in de openbare ruimte, gericht op het in stand houden van een schone, hele en veilige leefomgeving.
* **Interne organisatie**: Het informatiedomein dat gegevens omvat over de interne processen en ondersteunende functies die bijdragen aan het functioneren van de interne organisatie.
    * **[ICT](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/v2.3.0/domeinen/ict)**: Het informatiesubdomein dat gegevens omvat over de informatietechnologie en communicatiesystemen die de interne processen en informatievoorziening van een organisatie ondersteunen.
    * **[Gemeentelijk Vastgoed](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/v2.3.0/domeinen/vastgoed)**: Het informatiedomein dat gegevens omvat over het beheer, onderhoud en de exploitatie van gebouwen en terreinen in eigendom van de organisatie.
    * **[Financiën](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/v2.3.0/domeinen/financien)**: Het informatiesubdomein dat gegevens omvat over de financiële processen, planning en control, en het financieel beheer van de organisatie.
    * **[HR](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/v2.3.0/domeinen/hr)**: Het informatiesubdomein dat gegevens omvat over het beheer en de ontwikkeling van personeel, gericht op het ondersteunen van de organisatie en haar medewerkers.
    * **[Inkoop](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/v2.3.0/domeinen/inkoop)**: Het informatiesubdomein dat gegevens omvat over het proces van het verwerven van goederen, diensten en werken door een organisatie.
    * **[Subsidies](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/v2.3.0/domeinen/subsidies)**: Het informatiedomein dat gegevens omvat over het proces van aanvragen, beoordelen, verstrekken, beheren en verantwoorden van subsidies door de organisatie, zowel in de rol van subsidieverstrekker als subsidieontvanger.
    * **Facilitair (_nog in ontwikkeling_)**: Het informatiedomein dat gegevens omvat over de ondersteunende diensten en voorzieningen die bijdragen aan een optimale werkomgeving voor medewerkers en bezoekers van de organisatie.
    * **Control (_nog in ontwikkeling_)**: Het informatiedomein dat gegevens omvat over de interne beheersing en sturing van de organisatie, gericht op het waarborgen van de realisatie van organisatiedoelstellingen.
    * **Organisatie-indeling**: Het informatiedomein dat gegevens omvat over de structuur en indeling van een organisatie, inclusief de inrichting en uitvoering van programma’s en projecten.
* **[Dienstverlening](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/v2.3.0/domeinen/dienstverlening)**: Het informatiedomein dat gegevens omvat over meldingen, aanvragen, baliecontacten, telefonische afhandeling en digitale interacties die faciliterend zijn voor andere domeinen.

Naast bovengenoemde beleidsterreinen kent het GGM het onderdeel 'Kern', waarin alle gedeelde objecttypen zijn te vinden. Kern is afgeleid van het [Informatiemodel Basis- en Kerngegevens (RSGB)](https://www.gemmaonline.nl/index.php/Informatiemodel_Basis-_en_Kerngegevens_(RSGB)) en [Informatiemodel Zaken (RGBZ)](https://www.gemmaonline.nl/index.php/Informatiemodel_Zaken_(RGBZ)) (beiden onderdeel [GEMMA: Gemeentelijke Modelarchitectuur](https://www.gemmaonline.nl/index.php/Gemeentelijke_Model_Architectuur_(GEMMA))), aangevuld met een aantal generieke objecttypen. 

### Toegepaste Landelijke standaarden

Nederland kent op dit moment een lappendeken aan standaarden voor gegevensuitwisseling en informatiemodellen. Samenhang tussen deze standaarden en is beperkt. Relevante standaarden  zoveel mogelijk in samenhang binnen de afzonderlijke domeinen in het GGM opgenomen. Het stelsel van basisregistraties, en het daarop gerichte RSGB geven hiervoor wel enige houvast. In het GGM heeft het RSGB daarom een centrale plek.

De volgende standaarden zijn gebruikt bij de totstandkoming van het GGM en maken onderdeel uit van het GGM:

* [Informatiemodel Basis- en Kerngegevens (RSGB)](https://vng-realisatie.github.io/RSGB/) versie 2.0.2. Het RSGB is as-is gebruikt in het onderdeel _Kern_ van het GGM.
* [Informatiemodel Zaken (RGBZ)](https://www.gemmaonline.nl/wiki/GEMMA/id-bc302841-8db0-11e3-67ab-0050568a6153) versie 1.0. Het RGBZ is as-is gebruikt in het onderdeel _Kern_ van het GGM.  
* [iWmo](https://www.istandaarden.nl/iwmo) versie 2.3. iWmo is een berichtenstandaard voor het uitwisselen van gegevens tussen zorgaanbieders en gemeenten met achterliggend informatiemodel. Dit informatiemodel vormt samen met de iJw-standaard de basis voor het Jeugd- en Wmo-deel van het beleidsdomein _Sociaal Domein_. Deze zijn in de uitwerking aangevuld met diverse objecttypen.
* [iJw](https://www.istandaarden.nl/ijw) versie 2.3. Zie iWmo.
* [iPgb](https://www.istandaarden.nl/ipgb) versie 1.0. Hiervan zijn de informatiemodellen van  toekenningsbericht (TKB) en het budgetafsluitbericht (BAB) toegepast.
* [Suwi Gegevensregister (SGR)](https://bkwi.nl/standaarden/suwi-gegevensregister-sgr) versie 4.0. Het SGR is een gegevensmodel uit de keten van Werk en Inkomen dat dient als een gemeenschappelijk gedragen kader waarop de berichten uit het [SuwiML](https://bkwi.nl/standaarden/suwi-gegevensregister-sgr) zijn gebaseerd. Er is gebruik gemaakt van het berichtenschema (XSD's) op basis waarvan de relevante objecttypen zijn afgeleid.
* [Informatiemodel Beheer Openbare Ruimte (IMBOR)](https://www.crow.nl/thema-s/management-openbare-ruimte/imbor) versie 1.2.04. Het (IMBOR) bevat de afspraken over de benamingen en definities van de beheergegevens die aan de objecten in de openbare ruimte gekoppeld kunnen worden. Dit inclusief de samenhang tussen deze gegevens. De objecttypen uit de Basisregistratie Grootschalige Topografie (BGT) en het Informatiemodel geografie (IMGeo) vormen de basis. Beiden maken onderdeel uit van het RSGB. In het GGM is een koppeling gemaakt tussen de objecten uit het RSGB en IMBOR.
* [Standaard- en informatiemodel toepasbare regels (STTR en IMTR)](https://aandeslagmetdeomgevingswet.nl/digitaal-stelsel/technisch-aansluiten/koppelvlakken/toepasbare-regels/standaard/) versie 1.02. In het kader van de omgevingswet zijn toepasbare regels uitgewerkt conform STTR en IMTR. Deze worden toegepast om vragenbomen in het Omgevingsloket te laten zien. Deze is vanwege de beperkte rijkwijdte slechts beperkt overgenomen.
* [Standaard en informatiemodel aanvragen en meldingen (STAM en IMAM)](https://aandeslagmetdeomgevingswet.nl/digitaal-stelsel/technisch-aansluiten/koppelvlakken/vergunningen/standaard/) versie 0.9. De Standaard aanvragen en meldingen (STAM) en het bijbehorende informatiemodel (IMAM) helpen bij het afleveren van een vergunningaanvraag of melding in het kader van de omgevingswet bij overheden.
* [Standaard officiële publicaties (STOP/TPOD)](https://aandeslagmetdeomgevingswet.nl/digitaal-stelsel/technisch-aansluiten/koppelvlakken/omgevingsdocumenten/standaard-officiele/) Versie 0.98beta. Voor het valideren en publiceren van omgevingswetbesluiten. Vanwege de beperkte rijkweidte is deze slechts beperkt overgenomen.  
* [Conceptueel Informatiemodel Omgevingswet CIMOW](https://geonovum.github.io/TPOD/CIMOW/IMOW_v2.0.2.pdf) Versie CIMOW v0.98-kern. Het Conceptueel Informatiemodel voor de Omgevingswet (CIMOW) beschrijft het domein van de Omgevingswet. Dit beperkt zich tot de informatie die in dit domein wordt vastgelegd en vastgesteld en in ketens wordt uitgewisseld ten behoeve van het digitaal stelsel van de Omgevingswet (DSO).
* [GML (Geography Markup Language)](https://www.geonovum.nl/geo-standaarden/geography-markup-language-gml/gml-encoding-standard-321), GML beschrijft hoe geografische locaties, lijnen, vlakken en combinaties daartussen vastgelegd en uitgewisseld dienen te worden. GML 3.2.1 is gestandaardiseerd bij het OGC en, daar OGC en ISO met elkaar samenwerken, tevens gestandaardiseerd als ISO 19136:2007. De ISO variant is opgenomen als nationale standaard in de Pas-toe-of-leg-uit-lijst van het Forum Standaardisatie.
* [NEN3610: 2011 (Basismodel geo-informatie)](https://www.geonovum.nl/geo-standaarden/nen-3610-basismodel-voor-informatiemodellen). Het Basismodel geo-informatie. Het bevat de termen, definities, relaties en algemene regels voor de uitwisseling van informatie over ruimtelijke objecteninformatiemodellen). De standaard NEN3610 staat op de Pas-toe-of-leg-uit-lijst van het Forum Standaardisatie.
* [IMBGT/IMGeo: (Informatiemodel Basisregistratie grootschalige Topografie/ Informatiemodel Geo)](https://www.geonovum.nl/geo-standaarden/bgt-imgeo/gegevenscatalogus-imgeo-versie-211). De kern van dit model (BGT) definieert informatie zoals die via de BGT beschikbaar is, en als basis/ondergrond dient voor de overige modellen.
* [IMBAG: (Gegevenscatalogus Basisregistratie Adressen en Gebouwen)](https://www.geonovum.nl/geo-standaarden/informatiemodellen-nen3610-familie/gegevenscatalogus-basisregistratie-adressen-en). De Basisregistraties Adressen en Gebouwen (BAG) bevatten gegevens van alle adressen en gebouwen in Nederland. In de Gegevenscatalogus BAG zijn de afspraken vastgelegd om digitale uitwisseling mogelijk te maken. Het informatiemodel voor de BAG is geënt op de principes van NEN3610.
* [MIM (Metamodel voor Informatiemodellen)](https://www.geonovum.nl/geo-standaarden/metamodel-informatiemodellering-mim). Deze is toegepast in de uitwerking van het ICT-deel. Het GGM is echter (nog) niet MIM-compliant.
* [RiHA: (Gegevensmodel toezicht en handhaven)](https://samenwerken.pleio.nl/groups/view/8b832827-e91b-476c-bb4f-c228b8e5e934/standaardisatie-toezicht-handhaving-milieu/wiki/view/2b38214e-cfc7-42ff-9d5d-eaf069671c42/riha-referentieinformatiemodel-handhaving). Toegepast in de uitwerking van Vergunningverlening, toezicht en handhaving.
* [GBI: Gemeentelijke Basisprocessen Inkomen](https://vngr-gbi.gitlab.io/ontologie-inkomen/). De GBI- ontologie Inkomen beschrijft concepten en hun relaties welke een rol spelen binnen het inkomensdomein. Ontologie is een datastructuur die alle relevante entiteiten en hun onderlinge relaties en regels binnen dit domein bevat. Deze is toegepast voor het inkomensdeel van het sociaal domein.


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

## Tooling voor het manipuleren van het GGM

Het tooling-package bevat [Jupyter Notebooks](https://jupyter.org) voor het manipuleren van de database van het GGM. Hiermee kunnen bijvoorbeeld uitwisselingen met derde partijen worden vormgegeven, wordt de migratie naar MIM bewerkstelligd of kan worden ingezet om JSON-LD of databaseschema's te genereren. 

Voor meer informatie ga naar: [Informatiepagina Jupyter-tooling](tools/README.md)

[importXMI]: docs/image/ImportPackage.png "Import XMI via tabblad Publish"
[selectFilename]: docs/image/SelectFilename.png "Select Filename"
[importPackage]: docs/image/ImportPackage.png "Import Package"
[openDiagram]: docs/image/OpenDiagram.png "Open Diagram"
[gelaagdheidDomeinen]: docs/image/GelaagdheidDomeinen.jpg "Gelaagdheid Domeinen"
[aanpakGGM]: docs/image/AanpakGGM.jpg "Aanpak GGM"
[importRefData]: docs/image/ImportRefData.png "Import Referencedata"
[kiesTemplates]: docs/image/KiesTemplates.png "Kies templates"
[gebruikTemplates]: docs/image/GebruikTemplates.png "Gebruik templates"

## Citatie

Als je verwijst naar het Gemeentelijk Gegevensmodel (GGM) in wetenschappelijke publicaties, beleidsstukken of technische documentatie, gebruik dan bij voorkeur de volgende bronvermelding:

### APA 7-stijl

Brienen, A., & Ashkpour, A. (2025). *Gemeentelijk Gegevensmodel (GGM)*. Gemeente Delft. https://github.com/Gemeente-Delft/Gemeentelijk-Gegevensmodel

### BibTeXGebruik bij wetenschappelijke of technische verwijzingen bij voorkeur de volgende BibTeX-entry:

```bibtex
@misc{brienenAshkpour2019ggm,
  author       = {Arjen Brienen and Ashkan Ashkpour},
  title        = {Gemeentelijk Gegevensmodel (GGM)},
  year         = {2019},
  url          = {https://github.com/Gemeente-Delft/Gemeentelijk-Gegevensmodel},
  note         = {Beschikbaar onder de EUPL v1.2 en CC-BY 4.0 licentie},
  institution  = {Gemeente Delft},
  howpublished = {\url{https://github.com/Gemeente-Delft/Gemeentelijk-Gegevensmodel}},
  keywords     = {information model, semantic interoperability, municipalities, open standards}
}
