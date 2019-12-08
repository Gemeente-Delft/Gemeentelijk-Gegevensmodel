# Totstandkoming Gemeentelijk Gegevensmodel

## Overview

Het GGM is ontworpen op aan de hand van interviews met domeinexperts, de in Delft gebruikte applicaties en op basis van landelijke informatiestandaarden. Dit om tot een gegevensmodel te komen dat goede verankering kent met de Delftse situatie. De uitwerking van [Gemeentelijke Monumenten](./monumenten.md) is als voorbeeld in de handleiding opgenomen. Aangezien alle Nederlandse gemeenten in principe dezelfde wettelijke taken hebben gaan we ervanuit dat de onderliggende informatiemodellen sterk op elkaar lijken.

Uitgangspunt van de inventarisatie waren:

1. De lijst met Delftse applicaties en de inventarisatie hiervan waarbij onderscheid is gemaakt tussen authentieke bronnen en overige applicaties
2. De set beleidsdomeinen waar de gemeente haar taakgebied heeft 
3. Landelijk vastgestelde [standaarden](index.md#toegepaste-landelijke-standaarden) voor gegevensuitwisseling en landelijk vastgestelde informatiemodellen  

![Aanpak GGM 1][aanpakGGM]

De inventarisatie in de volgende stappen uitgevoerd:

1. **Applicaties en Beleidsdomeinen**: Interviews met experts uit de verschillen de Beleidsdomeinen: per beleidsdomein is er m.b.v. gesprekken met experts van de informatievoorziening binnen de beleidsdomeinen een inventarisatie gemaakt van de gebruikte applicaties, de betrokken gebruikers, de interactie tussen de applicaties en de gebruikers, en welke gegevens daarbij gebruikt worden.
2. **Applicaties en gegevens**: door in de gesprekken en uit de analyse de authentieke bronnen van gegevens te identificeren, en door in de gesprekken in te zoomen op de gebruikte gegevens en door de inventarisatie van de applicaties en gegevens te hanteren zijn de gegevens binnen de authentieke bronnen geïdentificeerd. Details van de gebruikte gegevens zijn hier geinventariseerd door foto's van de schermen van de gebruikte applicaties te maken en/of analyse van het achterliggende databaseschema.
3. **Gemeentelijk Gegevensmodel**: het gegevensmodel wordt opgebouwd door de in de vorige stap gevonden gegevens te vertalen naar objecttypen (gegevenssoorten). Landelijke standaarden dienen hier zoveel mogelijk als uitgangspunt, waarbij de nieuw gevonden gegevens woeden ingepast. Veel van de gebruikte applicaties ondersteunen deze landelijke standaarden, waardoor compatibiliteit zo goed mogelijk wordt gegarandeerd. 
4. **Databaseschema**: er is generator gerealiseerd waarmee op basis van de definities in het gegevensmodel met ‘een druk op de knop’ databasetabellen (DDL) gegenereerd kunnen worden. Hiermee is het mogelijk de basis te leggen voor een datawarehouse en is het mogelijk gegevens uit de applicaties te laden waardoor confrontatie van het model met de data mogelijk is.

## Informatieanalyse uitgelegd

Doel van de informatieanalyse is het vinden van de gegevens die binnen de verschillende [beleidsdomeinen](./index.md#beleidsdomeinen) worden gebruikt, het bepalen van de juiste gegevensdefinities (objecttypes), en het bepalen van de relaties tussen deze objecttypes. Ondanks dat je inventariseert welke taken in een beleidsdomein worden uitgevoerd beoog je geen complete procesanalyse, we zijn perslot op zoek naar gegevens. Per beleidsdomein doorloop je steeds de hier beschreven cyclus. Het is belangrijk dat tijdens de interviews een goede inventarisatie van de taken wordt gedaan en dat uitwerking zoveel mogelijk begrijpelijk is voor de geïnterviewde. Op deze manier kan de geïnterviewde toetsen of je inderdaad correct en compleet bent.

Hierna staan kort op conceptueel niveau de verschillende stappen in het analyseproces uitgelegd die je per beleidsdomein uitvoert. Daarbij is er een voorbeelduitwerking beschikbaar in de vorm van [Gemeentelijke Monumenten](./monumenten.md)

### Inventariseren Applicaties en Beleidsdomeinen

Doel van deze stap is het bepalen van een aantal zaken doormiddel van interviews, met als startpunt de reeds geinventariseerde applicaties voor dit domein:

1. Scope, doel en achtergrond van werkzaamheden binnen het beleidsdomein
2. De taken die (moeten) worden uitgevoerd binnen het beleidsdomein
3. De applicaties en andere administraties die worden gebruikt
4. De taken die met de applicaties worden uitgevoerd.

Voorbeeld uitwerking van deze fase is [hier](./monumenten.md#gemeentelijke-monumenten) en [hier](./monumenten.md#applicaties-en-beleidsdomeinen) te vinden (in twee delen uitgewerkt), en levert onder andere de volgende uitwerking.

![Applicaties Monumenten][applicatiesMonumenten]

### Inventariseren Applicaties en Gegevens

In de vorige stap is een limitatieve lijst van de gebruikte applicaties en de taken die met deze applicaties worden uitgevoerd. Doel van deze stap is te bepalen welke gegevens in deze applicaties worden geadministreerd en voor welke gegevens deze applicaties authentieke bron zijn. Zo ontstaat er een compleet beeld van de relevante gegevens binnen het domein.

Tijdens de interviews kun je foto's maken van de gebruikte applicaties, je kunt de achterliggende databaseschema's analyseren en gebruik maken van handleidingen bij de applicaties. Dit afhankelijke van de situatie en beschikbaarheid. De resultaten verwerk je in je analysedocument, zodat je dit kunt toetsen bij de geïnterviewden.

Voorbeeld uitwerking van deze fase is [hier](./monumenten.md#gegevensdefinities) te vinden, en levert onder andere de volgende uitwerking. Je ziet hierin de verschillende applicaties met daarin de gegevens.

![Applicaties en gegevens Monumenten][applicatiesEnGegevensMonumenten]

### Uitbreiden Gemeentelijk Gegevensmodel

In de vorige stap is geinventariseerd welke gegevens binnen het beleidsdomein worden gebruikt. In deze stap wordt deze inventarisatie gebruikt om een vertaling te maken naar objecttypes. Naast de geïnventariseerde gegevens bouw je hier zoveel mogelijk voort op (landelijke) gegevensstandaarden. De lijst met landelijke standaarden die in het Gemeentelijk Gegevensmodel zijn toegepast vind je [hier](./index.md#toegepaste-landelijke-standaarden). Als er een landelijke standaard voeg je die aan het model toe, door deze te importeren of deze met de hand over te nemen. Als je voortbouwt op een standaard die al in het model zit, hoeft dit uiteraard niet ;).

In deze stap maak je een uitbreiding op het Gemeentelijk Gegevensmodel door per gevonden gegeven een objecttype aan te maken, of her te gebruiken uit het reeds bestaande model. Let hierbij op dat je de [gelaagde opbouw](./index.md#opbouw-gemeentelijk-gegevensmodel) respecteert. Deze objecttypes en de daarbij horende relatie werk je uit in één of meer diagrammen.

Voorbeeld uitwerking van deze fase is [hier](./monumenten.md#applicaties-en-gegevens) te vinden, en levert onder andere de volgende uitwerking. 

![Uitwerking objecttypen Monumenten][gegevensdefinitiesMonumenten]

### Genereren Databaseschema

Om het net uitgebreide deel van het Gemeentelijk Gegevensmodel in een database te gebruiken kun je het genereren naar DDL. Selecteer og kopieer hiervoor het deel van het Gemeentelijk Gegevensmodel dat je naar DDL wilt genereren, en volg [deze](./generatie.md) handleiding.

## Uitwerking informatieanalyse met Enterprise Architect

Hoe Enterprise Architect is gebruikt bij de uitwerking van het GGM is hierna te lezen.

### Voor het modelleren

Voordat je start met modelleren moet je een aantal zaken ingericht hebben:

1. 

### Modelleren Applicaties en Beleidsdomeinen

Veel van het resultaat van deze stap is tekst, dat behoeft geen uitleg. 

[aanpakGGM]: image/AanpakGGM.jpg "Aanpak GGM"
[applicatiesMonumenten]: image/Applicaties_Monumenten.png "Applicaties Monumenten"
[applicatiesEnGegevensMonumenten]: image/ApplicatiesEnGegevensMonumenten.png "Monumenten Applicaties en Gegevens"
[gegevensdefinitiesMonumenten]: image/GegevensdefinitiesMonumenten.png "Monumenten Gegevensdefinities"