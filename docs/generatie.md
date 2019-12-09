# Code genereren op basis van het Gemeentelijk Gegevensmodel

Bij het GGM is een set codegeneratietemplates die binnen Enterprise Architect gebruikt kunnen worden voor het genereren van [Data Definition Language (DDL)](https://nl.wikipedia.org/wiki/Data_definition_language). Hiermee kunnen direct tabellen in een RDMBS gegenereerd worden. Er zijn diverse templates beschikbaar waarmee tabellen voor databases gegeneerd kunnen worden, en ook programmacode voor bijvoorbeeld: Python, C# en Java. In principe werkt codegeneratie voor alle ondersteunde RDBMS'en, op wat specifieke zaken na zoals enumeraties. Deze hebben wij wel ontwikkeld voor: 

1. Oracle
2. MySQL (ongetest)
3. Wij nodigen ontwikkelaars van harte uit deze te gebruiken en verder geschikt te maken voor het GGM.

De geleverde codegeneratietemplates zijn uitbreidingen op de standaard templates van [Enterprise Architect](https://sparxsystems.com), als onderdeel van het [Code Template Framework](https://sparxsystems.com/enterprise_architect_user_guide/15.0/model_domains/codetemplates_2.html).

## Installeren codegeneratietemplates

1\. Download het bestand 'CodegeneratieTemplates.xml'
2\. Start Enterprise Architect
3\. (Optioneel) Maak nieuw project
4\. Kies _Import Reference Data_

![Import Reference Data][importRefData]

5\. Selecteer het zojuist gedownloade bestand 'CodegeneratieTemplates.xml', selecteer alle templates en druk op _Import_

![Import Templates][kiesTemplates]

6\. De templates zijn klaar voor gebruik en je vindt ze onder _Transform_

![Gebruik Templates][gebruikTemplates]

7\. Succes!

## Gebruiken Codegeneratietemplates

Het uitgenereren vanuit het GGM naar DDL bestaat uit twee stappen:

1. Transformeren logische model naar logische tabelrepresentatie.
2. Genereren van DDL uit logische tabelrepresentatie.

### Voordat je begint

Zorg allereerst dat er in je project naast het GGM ook een plek is waar je de tabellen heen kunt schrijven. Hiervoor gebruiken wij een aparte node naast de root node. In het voorbeeld is dat de map `<<DataModel>> Tables/Ruimte/Afval`.

![Maak een plek om tabellen uit te genereren][tablesAfval]

Zorg vervolgens dat je in Enterprise Architect het default RDBMS selecteert. Hiervoor ga je naar _Preferences_

![Ga naar Preferences om het default RDBMS te selecteren][kiesPreferences]

Kies vervolgens onder _Source Code Engineering/Code Editors_ de optie _Default Database_. In ons voorbeeld Oracle.

![Selecteer het default RDBMS dat je als doel hebt][selecteerDefaultRDBMS]

### Stappen voor genereren DDL

Voor het genereren naar DDL neem je de volgende stappen:

1\. Selecteer het onderdee van het model dat je wilt uitgenereren. In het voorbeeld de map`Gemeentelijk Gegevensmodel/Ruimte/Afval/Model`. je kunt ook in een diagram de gewenste objecttypen selecteren.

![Selecteer de map in het model][selecteerInModel]

2\. Voor de eerste stap in de generatie kies _Apply Transformation_

![Kies Apply Transformation][applyTransformation]

3\. Selecteer aan de rechterkant van het popup _Tables_ in het vlak _Transformations_. Zorg dat aan de linkerkant van de popup alle objecttypen geselecteerd zijn die uitgegenereerd moeten worden.

![Kies Tables onder Transformation][kiesTables]

4\. In het nieuwe popup _Select Target Package_ selecteer de plek die je hebt gemaakt om de tabellen heen te schrijven. In ons voorbeeld `<<DataModel>> Tables/Ruimte/Afval`. 

![Kies Target Package][selectTargetPackage]

5\. Om de eerste stap in de transformatie en generatie te starten click op _Do Transform_

![Kies Do Transform][selectDoTransform]

6\. Even wachten, en de eerste stap in de generatie is uitgevoerd: de tabellen in Enterprise Architect zijn aangemaakt. De eerste stap in het generatieproces is nu uitgevoerd. Er is een "logische" en RDBMS-onafhankelijke versie van de tabellen aangemaakt. 

![Even wachten... en de tabellen zijn aangemaakt][tabellenAangemaakt]

7\. In de volgende stap genereer je vanuit de "logische" en RDBMS-onafhankelijke versie van de tabellen de DDL waarmee je de tabellen in je database kunt maken. Selecteer de map met de tabellen die zojuist is gegenereerd.

![Selecteer de map met de tabellen die je wilt genereren][selecteerTabellen]

8\. Onder _Develop Datamodelling_ kies _Generate_

![Onder _Develop Datamodelling_ kies _Generate_][kiesGenerate]

9\. Vul een bestandsnaam en map in en druk op de knop _Generate_

![druk op de knop _Generate_][kiesGenerateDDL]

10\. Even wachten en de DDL staat klaar. Succes!

## Interne werking Codegeneratietemplates

### Objecttypes(Classes)

Bij het genereren van de tabelnamen geldt de volgende volgorde:

1. Alias
2. Naam objecttype

Als de map waar het objecttype in zit een Alias heeft wordt deze als prefix voor de tabelnaam gebruikt. Daarnaast worden bij iedere tabel twee kolommen toegevoegd:

1. M_Bronsysteem
2. M_DatumTijdGeladen

Als een objecttype een Stereotype heeft dan worden deze als volgt gebruikt:

* enumeration (Alleen Oracle en MySql): omgezet naar tabel met tabelnaam prefix _ENUM__. Tabel heeft altijd de volgende kolommen: ID, waarde en omschrijving. Daarbij worden de verschillende attributen omgezet naar INSERT-statements, zodat de tabel gevuld wordt. Hierbij worden de velden van de attributen als volgt gemapt:

    * ID: Attribuutveld _Alias_
    * waarde: Attribuutveld _Name_
    * omschrijving: Attribuutveld _Comment_  

* referentielijst: tabel met tabelnaam met prefix _LST__ 

### Attributen

Met behulp codegeneratietemplates worden de verschillende attributen van de objecttypes uit het GGM omgezet op basis van _Datatype_ en op basis van _Stereotype_. Het gaat hier om aanvullingen boven het [Code Template Framework](https://sparxsystems.com/enterprise_architect_user_guide/15.0/model_domains/codetemplates_2.html) van Enterprise Architect. Bij het genereren van de tabelnamen geldt de volgende volgorde:

1. Alias
2. Naam attribuut

Attributen worden als volgt op basis van hun datatype omgezet (niet case sensitive):

* Datumtijd of Datetime: attribuut met zowel datum als tijd (Voor Oracle DATE-veld).
* Datum of Date: attribuut met alleen datum.
* Tijd of Time: attribuut met alleen tijdstip.
* ANxxx: Tekstveld (Alphanumeriek) met lengte xxx. Als er geen lengte is weergegeven wordt teruggevallen op lengte 80.
Integer of Int: numeriek veld met alleen gehele getallen.
* Double: numerieke waarden met komma
* Bedrag: veld waar bedragen in worden bewaard (bedrag met maximaal 10 cijfers, waarvan 2 achter de komma)
* Tekst of Text: tekstveld voor lange memovelden.
* Boolean: Boolean-waarde (voor Oracle numeriek veld: ‘J’=1, ‘N’=2, ‘Overig’=-1, ‘Onbekend’=null)
* GUID: Tekstveld van 40 karakters
* GML of Punt: locatie, veld wordt opgesplitst in twee velden voor [WGS84-coördinaten](https://nl.wikipedia.org/wiki/WGS_84) ("veldnaam"_lat en "veldnaam"_long) en in twee velden voor [rijksdriehoekcoördinaten](https://zakelijk.kadaster.nl/rijksdriehoeksstelsel) ("veldnaam"_rdx en "veldnaam"_rdy). Alle velden zijn van het datatype double.

Attributen worden op basis van hun Stereotype omgezet:

* Adresaanduiding: veld wordt vervangen door de volgende velden: Naam Gemeente, Straatnaam, Huisnummer, Huisletter, Huisnummertoevoeging, Postcode en BAGID.
* enum: er wordt een referentie naar de enumeratie opgenomen.

[tablesAfval]: image/TablesAfval.png "Maak een plek om de tabellen uit te genereren"
[selecteerInModel]: image/SelecteerInModel.png "Selecteer de map in het model"
[applyTransformation]: image/ApplyTransformation.png "Kies Apply Transformation"
[kiesTables]: image/KiesTables.png "Kies Tables onder Transformation"
[selectTargetPackage]: image/SelectTargetPackage.png "Kies Target Package"
[selectDoTransform]: image/SelectDoTransform.png "Kies Do Transform"
[tabellenAangemaakt]: image/TabellenAangemaakt.png "Even wachten... en de tabellen zijn aangemaakt"
[kiesPreferences]: image/KiesPreferences.png "Ga naar Preferences om het default RDBMS te selecteren"
[selecteerDefaultRDBMS]: image/SelecteerDefaultRDBMS.png "Selecteer het default RDBMS dat je als doel hebt"
[selecteerTabellen]: image/SelecteerTabellen.png "Selecteer de tabellen die je wilt genereren"
[kiesGenerate]: image/KiesGenerate.png "Kies Generate"
[kiesGenerateDDL]: image/KiesGenerateDDL.png "Kies Generate"
[importRefData]: image/ImportRefData.png "Import Referencedata"
[kiesTemplates]: image/KiesTemplates.png "Kies templates"
[gebruikTemplates]: image/GebruikTemplates.png "Gebruik templates"

