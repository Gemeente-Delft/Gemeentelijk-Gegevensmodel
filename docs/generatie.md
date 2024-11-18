# Code genereren op basis van het Gemeentelijk Gegevensmodel

Bij het GGM is een set codegeneratietemplates die binnen Enterprise Architect gebruikt kunnen worden voor het genereren van [Data Definition Language (DDL)](https://nl.wikipedia.org/wiki/Data_definition_language). Hiermee kunnen direct tabellen in een RDMBS gegenereerd worden. Er zijn diverse templates beschikbaar waarmee tabellen voor databases gegeneerd kunnen worden, en ook programmacode voor bijvoorbeeld: Python, C# en Java. In principe werkt codegeneratie voor alle ondersteunde RDBMS'en, op wat specifieke zaken na zoals enumeraties. Deze hebben wij wel ontwikkeld voor: 

1. Oracle
2. MySQL (ongetest)
3. Wij nodigen ontwikkelaars van harte uit deze te gebruiken en verder geschikt te maken voor het GGM.

De geleverde codegeneratietemplates zijn uitbreidingen op de standaard templates van [Enterprise Architect](https://sparxsystems.com), als onderdeel van het [Code Template Framework](https://sparxsystems.com/enterprise_architect_user_guide/15.0/model_domains/codetemplates_2.html).

## Installeren codegeneratietemplates

1. Download het bestand 'CodegeneratieTemplates.xml'
2. Start Enterprise Architect
3. (Optioneel) Maak nieuw project
4. Kies _Import Reference Data_

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

1\. Selecteer het onderdeel van het model dat je wilt uitgenereren. In het voorbeeld de map`Gemeentelijk Gegevensmodel/Ruimte/Afval/Model`. je kunt ook in een diagram de gewenste objecttypen selecteren.

![Selecteer de map in het model][selecteerInModel]

2\. Voor de eerste stap in de generatie kies _Apply Transformation_

![Kies Apply Transformation][applyTransformation]

3\. Selecteer aan de rechterkant van het popup _Tables_ in het vlak _Transformations_. Zorg dat aan de linkerkant van de pop-up alle objecttypen geselecteerd zijn die uitgegenereerd moeten worden.

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

## Interne werking

De mogelijkheden die de codegeneratietemplates bieden is beperkend voor de mogelijkheden bij het modelleren in het Gemeentelijk Gegevensmode. Immers datatypes en relaties die niet worden ondersteund door de codegeneratietemplates kun je niet (automatisch) omzetten naar tabellen, en niet goed gebruiken als je het tabel toepast. Daarom is hier beschreven wat je in het logisch model kunt gebruiken en hoe dit transformeert naar tabellen.

### Objecttypes(Classes)

Bij het genereren van de tabelnamen geldt de volgende volgorde (alle namen worden ingekort tot maximaal 30 karakters):

1. Alias
2. Naam objecttype

Als de map waar het objecttype in zit een Alias heeft wordt deze als prefix voor de tabelnaam gebruikt. Daarnaast worden bij iedere tabel twee kolommen toegevoegd (bedoeld om van waarden te voorzien tijdens het vullen van het datawarehouse):

1. DWH_Bronsysteem (Naam van het bronsysteem waarvandaan data is geladen)
2. DWH_DatumTijdGeladen (Systeemdatum(tijd) waarop data is geladen)
3. DWH_DatumTijdGeldigVanaf (Voor opbouw van historie: datum en tijd **vanaf** welke record geldig is)
4. DWH_DatumTijdGeldigTotMet (Voor opbouw van historie: datum en tijd **tot en met** welke record geldig is)

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
* enumeration: er wordt een referentie naar de enumeratie opgenomen. Zie hiervoor [Voorbeeld D](#Voorbeeld-D)

### Relaties

De vertalen van relaties in het logisch model is niet altijd recht-toe-rechtaan. Met name voor de naamgeving van de [foreignkeys](https://en.wikipedia.org/wiki/Foreign_key) en de [foreignkey-constraints](https://www.w3schools.com/sql/sql_foreignkey.asp). Hierom is dit hier in 3 voorbeelden beschreven.

#### Voorbeeld A

In het eerste voorbeeld zijn 4 objecttypes/classes te zien met drie relaties

1. Relatie A: 1:N-relatie
2. Relatie B: N:M-relatie
3. Generalisatie van Class A t.o.v. Child Class A  

![Voorbeeld A voor uitgeneren naar tabellen][voorbeeldA]

Deze relaties vertalen zich na transformeren naar tabellen als volgt:

1. Relaties A: kolom _ClassAID_ in tabel _ClassB_ met foreignkey naar tabel _ClassA_
2. Relatie B: de koppeltabel KP_classa_classc, met foreignkey-relaties naar tabel _ClassA_ en tabel _ClassB_
3. Generalisatie van Class A t.o.v. Child Class A: dit blijven twee aparte tabellen, kolommen worden niet overgenomen in het _child_. Er wordt een reguliere 1:N-relatie gemaakt, zoals Relatie A.

![Voorbeeld A na uitgeneren naar tabellen][voorbeeldATabellen]

#### Voorbeeld B

De naamgeving van de foreignkeys, foreignkey-constraints en koppeltabellen kan worden beïnvloed door het gebruik van relatienamen en aliassen. Hiermee zorg je dat er geen dubbele constraints worden gemaakt en er geen onleesbare of te lange namen ontstaan. Voor naamgeving wordt de volgende volgorde gebruikt (in volgorde van prioriteit):

1. Alias van Source/Target
2. Alias van relatie
3. Relatienaam
4. Concatenering namen Source en Target

In het voorbeeld zijn de volgende relaties uitgewerkt:

1. Relatie Class A en Class B: relatienaam = "Relatienaam"
2. Relatie Class C en Class D: relatie heeft Alias "Aliasnaam"
3. Relatie Class E en Class F: zowel Source als Target van relatie hebben eigen alias 
4. Relatie Class G en Class H: relatie heeft geen naam en geen aliassen
5. Relatie Class I en Class J: relatie zonder naam en aliassen, maar Source en Target omgedraaid t.o.v. het vorige voorbeeld.

![Voorbeeld B voor uitgeneren naar tabellen][voorbeeldB]

Na transformeren naar tabellen als volgt:

1. Eerste voorbeeld: tabel ClassA krijgt kolom ClassBID (met index) en foreignkey-constraint (met in de naam relatienaam) op de relatie met tabel ClassB.  
2. Tweede voorbeeld: tabel ClassC krijgt kolom ClassCID (met index) en foreignkey-constraint (met in de naam alias) op de relatie met tabel ClassC. 
3. Derde voorbeeld: tabel ClassE krijgt kolom AliasSourceCID (met index) en foreignkey-constraint (met in de naam de aliassen van source en target) op de relatie met tabel ClassF. 
4. Vierde voorbeeld: tabel ClassG krijgt kolom ClassHID (met index) en foreignkey-constraint (met in de namen van de tabellen) op de relatie met tabel ClassH.
5. Vijfde voorbeeld: tabel ClassI krijgt kolom ClassJID (met index) en foreignkey-constraint (met in de namen van de tabellen) op de relatie met tabel ClassJ (zelfde als 4e voorbeeld).

![Voorbeeld B na uitgeneren naar tabellen][voorbeeldBTabellen]

#### Voorbeeld C

Voorbeelden die speciale aandacht nodig hebben, omdat het transformatieproces anders fouten oplevert:

1. [Relaties met jezelf](https://www.365dagensuccesvol.nl/nl/nieuws/zeg-hoe-goed-is-de-relatie-met-jezelf-eigenlijk/143/) ;) (Varkensoortje)
2. Meervoudige relaties tussen objecttypes.

![Voorbeeld C voor uitgeneren naar tabellen][voorbeeldC]

Om deze in het transformatieproces goed te laten werken moet een een Alias opvoeren bij de Source van de betreffende relatie. In het voorbeeld getoond voor het varkensoortje. Deze kun je ook voor meervoudige relaties gebruiken. Vanwege de interne werking van Enterprise Architect is het belangrijk dat de cardinaliteit 0..1 of 1 aan de source-kant van de relatie zit, anders wordt de relatie niet goed uitgegenereerd.

![Voer een alias in in de Source van het varkensoortje][varkensoortje]

Als je het logisch model hebt getransformeerd naar tabellen zie je dat de Aliasnaam wordt gebruikt voor de foreignkeys en de foreignkey-constraints. Zo kun je zorgen dat er unieke namen worden gebruikt.

![Voorbeeld C na uitgeneren naar tabellen][voorbeeldCTabellen]

#### Voorbeeld D

Als laatste een voorbeeld met het gebruik van enumeraties:

[Enumeraties](https://nl.wikipedia.org/wiki/Enumeratie_(datatype)) is een opsomming van mogelijke waarden van een bepaald attribuut. Hiermee kun je binnen het GGM de waarden van attributen binnen een bepaalde reeks laten vallen.
Om deze in het transformatieproces goed te laten werken moet een een Alias opvoeren bij de Source van de betreffende relatie. In het voorbeeld getoond voor het varkensoortje. Deze kun je ook voor meervoudige relaties gebruiken. Hieronder is weergegeven hoe je een enumeratie definieert. 

![Voorbeeld Enumeratie][voorbeeldD]

Te zien is dat deze enumeratie twee mogelijke waarden kent: Optie 1 en Optie 2, en dat het attribuut B verwijst naar deze enumeratie.

![Enumeratie koppelen][voorbeeldDStereotype]

Hierboven is te zien hoe je een attribuut koppelt aan een enumeratie. Belangrijk is het stereotype de waarde "enumeration" te geven.

![Waardenlijsten van enumeraties maken][voorbeeldDAtt]

In bovenstaande figuur is te zien hoe je imn Enterprise Architect de waardelijsten van een enumeratie definieert. In het voorbeeld bestaat de waardelijst uit twee waarden: Optie 1 en Optie 2. Deze zijn als attributen van de Class 'Enumeration A' gedefinieerd. Je vult deze als volgt in:

1. Naam: in Name-veld van attribuut (Altijd waarde invullen om fouten te voorkomen)
2. Index: in Alias-veld van attribuut (Altijd unieke integerwaarde invullen om fouten te voorkomen)
3. Omschrijving: in Notes-veld van attribuut  
4. Geen bij Stereotype altijd waarde 'enum' op

Als je het logisch model hebt getransformeerd naar tabellen zie je dat er van de Class een tabel ie gemaakt, en ook van de enumeratie. Beiden zijn gekoppeld via een foreignkey constraint.

![Enumeraties uitgenereren][voorbeeldDTabellen]

In het uitgegenereerde model is te zien dat in de enumeratie de waardelijsten nog als attributen zijn opgenomen. Pas bij het genereren naar fysieke databaseschema's worden de waardelijsten omgezet naar waardelijsten in de tabel.

## Zelf templates aanpassen

Nadat je de templates in Enterprise Architect hebt geladen kun je ze binnen je eigen omgeving aanpassen om het gedrag aan te passen naar je eigen wensen. Het is belangrijk te zien dat de generatie naar DDL in twee stappen verloopt, en dat je dus op twee niveau aanpassingen kunt maken.

1. Eerste generatiestap: Aanpassen templates die database-onafhankelijke tabellen genereren
2. Tweede generatiestap: Aanpassen generatie van database-onafhankelijke tabbellen naar DDL

### Eerste generatiestap

Ga hiervoor als eerste naar het onderdeel Transform templates. Zie hieronder.

![Templates aanpassen stap 1][templatesAanpassenStap1]

Kies nadat je deze hebt geopend voor de 'language' Tables. Deze verzameing templates gebruiken we voor de omzetting naar tabellen. Alle voor generatie gebruikte template-onderdelen staan weergegeven. Op de volgende afdeling is de omzetting vanaf Class te zien. 

![Templates aanpassen stap 2][templatesAanpassenStap2]

Je bent nu klaar om je egen aanpassingen te doen. Zie voor meer toelichting de [toelichting](https://sparxsystems.com/enterprise_architect_user_guide/16.1/modeling_fundamentals/transformationtemplates.html) op de website van Sparx Enterprise Architect. 

### Tweede generatiestap

Om de templates aan te passen die de database-onafhankelijke tabellen omzetten naar DDL voor specifieke databases kies je op het tabblad Design voor de optie Templates. Als je deze hebt geopend kun je verschillende typen databases kiezen. In onderstaande afbeelding kiezen we voor Oracle en zie je de scripts waarmee de DDL wordt gegenereerd.

![Templates voor generatie naar DDL][ddlgeneratieaanpassen]

Wij hebben de standaard werking van Enterprise Architect aangepast voor Oracle en MySql.   


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
[voorbeeldB]: image/EAID_6FCF9303_410D_4ff2_A577_C323F426A500.gif "Voorbeeld B voor Uitgeneren naar tabellen"
[voorbeeldCTabellen]: image/EAID_15C4CFF6_5DC6_456a_AE2B_0298FA9CDB6F.gif "Voorbeeld C na uitgeneren tabellen"
[voorbeeldC]: image/EAID_135DA4FB_69A6_4191_84A3_3B9F16641289.gif "Voorbeeld C voor Uitgeneren naar tabellen"
[voorbeeldBTabellen]: image/EAID_0435B59E_F272_4227_BE64_F7A8FC9A30EE.gif "Voorbeeld B na uitgeneren tabellen"
[voorbeeldATabellen]: image/EAID_9259B8B6_DD2F_4632_9CAE_8A0D9F30DF1F.gif "Voorbeeld A na uitgeneren tabellen"
[voorbeeldA]: image/EAID_E7F774F3_E0B3_438e_80DC_4B2F2CD3C60B.gif "Voorbeeld A voor uitgeneren naar tabellen"
[varkensoortje]: image/Varkensoortje.png
[voorbeeldD]: image/VoorbeeldD.png "Voorbeeld D Enumeraties gebruiken"
[voorbeeldDAtt]: image/VoorbeeldD_EnumAttributen.png "Voorbeeld D Attributen van Enumeraties"
[voorbeeldDTabellen]: image/VoorbeeldD_Tables.png "Voorbeeld D genereren van tabellen"
[voorbeeldDStereotype]: image/VoorbeeldD_Stereotype.png "Voorbeeld D stereotype gebruiken"
[templatesAanpassenStap1]: image/templatesaanpassen_stap1.png "Templates aanpassen stap 1"
[templatesAanpassenStap2]: image/templatesaanpassen_stap2.png "Templates aanpassen stap 2"
[ddlgeneratieaanpassen]: image/ddlgeneratieaanpassen.png "Templates DDL-generatie aanpassen"