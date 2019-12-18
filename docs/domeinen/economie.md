# Economie en Bedrijvigheid

De gegevensdefinities van Economie en bedrijvigheid concentreren zich ‘Vestigingen’ van bedrijven. Deze hebben een locatie in de stad en bepalen voor een belangrijk deel hoe er naar de lokale economie wordt aangekeken.

![Datamodel Economie en bedrijvigheid][economie]

Centraal staat ‘Vestiging’, wat een specialisatie kan hebben als ‘Verkooppunt’ (Winkel), of als ‘Hotel’. Van meer soorten bedrijven wordt er op dit geen specifieke informatie bijgehouden (generieke informatie wel). Een ‘Hotel’ kan ‘Hotelbezoeken’ (overnachtingen) hebben. Een ‘Vestiging’ voert een ‘Maatschappelijke Activiteit’ uit (bovenste relatie), en kan vanuit de ‘Maatschappelijke Activiteit’ een hoofdvestiging hebben. 

Per ‘Vestiging’ kan ‘Werkgelegenheid’ worden bijgehouden, zoals het aantal mannen en vrouwen wat er werkzaam is.

Een ‘Vestiging’ is verbonden aan een ‘Niet-Natuurlijk Persoon’: het bedrijf (of anderszins) waar de ‘Vestiging’ toe behoort. Van het bedrijf (of anderszins) worden de ‘Contactpersonen’ geadministreerd.

![Datamodel Economie en locaties][economieLocaties]

Het adres van een ‘Vestiging’ is vastgelegd via de ‘Adresseerbaar Object Aanduiding’, hiermee wordt de koppeling met de BAG gelegd. Een specialisatie van de ‘Adresseerbaar Object Aanduiding’ is de ‘Nummeraanduiding’. Veelal zal een ‘Vestiging’ voor het adres een ‘Nummeraanduiding’ hebben. Alleen in het geval van bijvoorbeeld een ‘Ligplaats’ is dit anders. Dit komt zo weinig voor dat het hier niet is gemodelleerd.

Van een ‘Gebouwd Object’ wordt het ‘Winkelvloeroppervlak’ bijgehouden. Deze informatie komt uit specifiek onderzoek. Ook wordt hier bijgehouden over er leegstand is. In het ‘Gebouwd Object’ wordt het aantal vierkante meters vloeroppervlak bijgehouden (Informatie uit de BAG). Op deze manier kunnen onderzoeksinformatie voor winkels en BAG-informatie vergeleken worden. Een ‘Gebouwd Object’ is een specialisatie van een ‘Verblijfsobject’, waaraan de ‘Nummeraanduiding’ is gekoppeld om het huisnummer van de straat te kunnen vastleggen.

Binnen een ‘Gebied’ liggen meerdere ‘Adresseerbare Objecten’. Een ‘Gebied’ kent verschillende soorten, zoals: winkelgebied en projectontwikkelgebied. Ook kunnen ‘Gebieden’ overeenkomen met een ‘Buurt’ die weer samen een ‘Wijk’ vormen. ‘Gebied’ is een toevoegingen aan de RSGB omdat er geen heldere manier is om ‘Buurt’ (en dus ook ‘Wijk’ en nog verdere woonplaats en gemeente) aan ‘Adresseerbare Objecten’ te koppelen.

[economie]: image/EAID_21D78104_E6EA_4d5c_9DBE_AB71F7DC99E7.gif "Datamodel Economie en bedrijvigheid"
[economieLocaties]: image/EAID_50085E67_46AC_4f54_B204_436786266EE2.gif "Economie en locaties"
