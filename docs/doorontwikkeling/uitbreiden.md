# Een uitbreiding maken


In dit onderdeel wordt met voorbeelden getoond hoe je uitbreidingen aan het GGM kunt maken. Om te illustreren hoe je de uitbreiding moet aanpakken wordt gewerkt met het voorbeeld `Deelmodel Begraafplaats`.

### Voorbeeldcasus: Deelmodel Begraafplaats

Als voorbeeld wordt het (vereenvoudigde) **deelmodel Begraafplaats** gebruikt. Dit deelmodel richt zich op de kernbegrippen die in vrijwel elke gemeentelijke context voorkomen. Een **begraafplaats** omvat meerdere **graven**, die ieder gekoppeld zijn aan een of meer **overledenen**. Rondom deze kern zijn verschillende actoren en objecten relevant. Zo speelt de **begrafenisondernemer** een rol bij het aanvragen en organiseren van de uitvaart. Daarnaast zijn er vaak aanvullende entiteiten nodig, zoals:

- **Nabestaande** – de contactpersoon of rechthebbende die verantwoordelijk is voor het graf en de administratie.  
- **Grafrecht** – de juridische relatie tussen een rechthebbende en een graf, inclusief looptijd en voorwaarden.  
- **Begraafplaatsbeheerder** – de gemeentelijke of particuliere organisatie die het onderhoud en de administratie van de begraafplaats verzorgt.  

Met dit vereenvoudigde model wordt duidelijk hoe verschillende objecttypen en relaties in een praktijkcasus kunnen worden gemodelleerd en op het GGM aangesloten.

## Begraafplaats Modelleren

Onder modelleren wordt verstaan het aanpassen van een bestaand model of het realiseren van een nieuw deelmodel. 

### Model Begraafplaats Correct

Het model is op hoofdlijnen in de volgende afbeelding uitgewerkt. Je ziet dat Objecttypes ook als Objecttype zijn aangeduid en dat ze gezamenlijk onderdeel uitmaken van `Model Begraafplaats`.

![Model Begraafplaats op hoofdlijnen](../image/Begraafplaats%20hoofdlijnen.jpg)

In onderstaande diagram zijn ook de details van het ontwerp weergegeven.

![Model Begraafplaats in detail](../image/Begraafplaats%20details.jpg)

Je ziet in het model de volgende (correcte) invulling:

1. Alle objecttypen hebben attributen
2. De datatypes van de attributen zijn [ondersteunde datatypes](../modelelementen/#ondersteunde-datatypes), als het primitieven betreft staan ze in de lijst [ondersteunde primitieve datatypes](../modelelementen/#ondersteunde-primitieve-datatypes)
3. De Enumeratie `Grafsoort` bestaat uit een lijst met meer dan één waarde
4. Alle Objecttypen en Enumeraties zijn voorzien van een definitie (zie onderstaande afbeelding)

![Objecttypes met definitie](../image/Objecttype%20met%20definitie.png)

### Veel gemaakte fouten

Bij het aanbieden van deelmodellen aan het GGM is er een aantal fouten dat veel wordt gemaakt. Deze zijn in onderstaande figuur weergegeven.

![Veel gemaakte fouten](../image/Begraafplaats%20fouten.jpg)

het betreft de volgende fouten:

1. Er is een ID opgenomen: technische sleutels passen niet in een conceptueel model. Alleen sleutelgegevens met een functionele betekenis worden in een model opgenomen, zoals BSN
2. Enum() is een datatype dat niet wordt ondersteund. Hier wordt een enumeratie mee bedoeld, maar neem dan de verwijzing naar deze enumeratie op
3. locatie heeft geen datatype, deze is verplicht
4. Het Objecttype `Begraafplaatsbeheerder` heeft geen attributen, deze is verplicht
5. De enumeratie `Grafsoort` heeft geen waardenlijst

## Een model koppelen aan het GGM 

Speciale aandacht vraagt het ontwikkelen van een informatiemodel dat koppelbaar is aan het bestaande GGM. Sommige deelmodellen worden immers buiten het GGM ontwikkeld, waarna ze aan het GGM gekoppeld worden. Hiervoor is het belangrijk dat duidelijk is welke objecttypen uit het GGM gebruikt worden binnen het nieuw te ontwikkelen model. Daarnaast hebben alle relaties kardinaliteit, een label en een richting voor de leesbaarheid. 

