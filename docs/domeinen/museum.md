# Museum

De gegevensdefinitie van de gegevens binnen het Prinsenhof zijn opgedeeld in de volgende drie deelgebieden:

1. Collectie
2. Events en Relaties
3. Verkoop

Daarnaast wordt er voorgebouwd op generieke gegevensdefinities uit erfgoed, zodat gegevens uitgewisseld kunnen worden. Het gegevensmodel van het museum maakt gebruik van de generieke erfgoed objecttypen.

## Collectie

Binnen de ‘Collectie’ staan de objecten die bij het museum horen centraal. Deze zijn ‘Museumobject’ genoemd. Museumobjecten hebben een ‘Standplaats’ en kunnen in bruikleen zijn, in dit geval hebben zij een ‘Bruikleen’-object aan zich gekoppeld. In het geval van een bruikleen is er een ‘Lener’ aan gekoppeld. Dit kan zowel het Museum Prinsenhof zelf zijn (het is uitgeleend), als een externe lener (het wordt geleend van). Leners zijn een ‘Rechtspersoon’: een natuurlijk persoon of een niet-natuurlijk persoon. Daarnaast kunnen museumobjecten een ‘Belanghebbende’ hebben. In dit geval heeft deze belanghebbende altijd een bepaalde rol tov het museumobject. 
Naast de collectie worden de tentoonstellingen geadministreerd, met daaraan gekoppeld de gebruikte zalen en de samenstellers van de tentoonstelling. Bij de tentoonstellingen wordt bijgehouden welke museumobjecten onderdeel uitmaken van de tentoonstelling.
Ook worden historische personen geadministreerd, en hun relatie tot museumobjecten via de Rol. Daarnaast worden incidenten geadministreerd en zijn deze gekoppeld aan de museumobjecten.
Voorgaande is uitgewerkt in de volgden figuur.

![Gegevensmodel Collectie][museumCollectie]

## Events en Relaties

Hierbij staan activiteiten binnen programma’s voor museumrelaties centraal. Een ‘Programma’ bestaat uit 0 of meer activiteiten. Iedere ‘Activiteit’ kan weer uit 0 of sub-activiteiten bestaan. Een ‘Activiteit’ is van een ‘Activiteitsoort’. Hetzelfde geldt voor een programma, deze is van een ‘Programmasoort’. Aan een ‘Activiteit’ kunnen reserveringen zijn gekoppeld. Het kan hier gaan om reserveringen voor: zalen, voorzieningen en productie-eenheden. Dit is uitgebeeld met een koppeling vanuit ‘Reservering’ naar 0 of meer objecttypes ‘Zaal’, naar 0 of meer objecttypes ‘Productie-eenheid’ en 0 of meer objecttypes ‘Voorziening’. Een ‘Productie-eenheid’ kan een externe leverancier zijn, in dit geval is er een koppeling met ‘Leverancier’. Aan een ‘Activiteit’ kan een ‘Rondleiding’ zijn gekoppeld, die weer aan en ‘Tentoonstelling’ kan zijn gekoppeld. 
Een ‘Programma’ kent een kostenplaats waarmee het is gekoppeld aan een ‘Kostenplaats’ en de koppeling met de financiële administratie is geborgd.
Binnen het datamodel van het Prinsenhof worden relaties (personen, bedrijven en instellingen) vormgegeven in het objecttype ‘Museumrelatie’. Een ‘Museumrelatie’ is afgeleid van een ‘Rechtspersoon’, waarmee alle benodigde kenmerken, zoals naam, adres en kvk-nummer zijn geborgd. Aan museumrelaties worden mailings gestuurd, hierom is het objecttype ‘Mailing’ aan ‘Museumrelatie’ gekoppeld.
Voorgaande is uitgewerkt in de volgende figuur.

![Museum Events en Relaties][museumEventsEnRelaties]

## Winkelverkoop

In het gegevensmodel Verkoop staat het te verkopen ‘Product’ centraal. Een ‘Entreekaart’ is een afgeleide van product, en is gemodelleerd als iets dat net als de andere producten verkocht kan worden. Alle producten hebben 0 of meer productgroepen en omzetgroepen. Daarnaast kan een ‘Product’ een ‘Leverancier’ hebben. Een ‘Product’ kan een ‘Voorraaditem’ hebben, waarin het aantal op voorraad is vastgelegd. Producten kunnen meerdere ‘Balieverkoop’ hebben, waarmee wordt aangegeven hoeveel en wanneer er van een bepaald product is verkocht. Een ‘Balieverkoop Entreekaart’ is een afgeleide van een ‘Balieverkoop’ en biedt de mogelijkheid om specifieke zaken van een entreekaart vast te leggen, zoals de moment en de duur van de geldigheid.  
Voorgaande is uitgewerkt in de volgende figuur.

![Museum Verkoop in de winkel][museumVerkoop]

[museumVerkoop]: image/EAID_3913ADF8_4B30_48c0_A0AE_59BAAC281EF2.gif "Museum Verkoop in de winkel"
[museumCollectie]: image/EAID_B2D890F1_6B7C_45df_9A70_8C40CE1B3611.gif "Gegevensmodel Collectie"
[museumEventsEnRelaties]: image/EAID_22110445_1906_4602_8004_6BA4D6C063D0.gif "Museum Events en Relaties"
