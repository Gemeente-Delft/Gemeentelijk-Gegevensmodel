# Parkeren

Gegevensdefinities rond parkeren concentreren zich rond het ‘Parkeerrecht’. In een parkeerrecht staat vastgelegd in welke ‘Parkeerzone’ een bepaald ‘Voertuig’ mag parkeren en in welke periode. Parkeerrechten worden afgegeven door een ‘Belprovider’ of komen voort uit een ‘Parkeervergunning’. Een en ander is uitgewerkt in de volgende figuur.

![Gegevensmodel parekeren][parkeren]

Parkeervergunningen zijn van een bepaald ‘Productsoort’ en een ‘Productgroep’. Deze zijn als voorbeeld inzichtelijk in de volgende figuur. Een ‘Parkeervergunning’ wordt afgegeven aan een ‘Rechtspersoon’ als houder. Parkeervergunningen en bijbehorende rechten gelden voor een bepaalde ‘Parkeerzone’. Parkeerzones kennen een aantal parkeerplaatsen en zaken als tarief en de tijden dat het parkeertarief geldt. Parkeergarages zijn ook vormgegeven als ‘Parkeerzone’. Parkeerzones kunnen een aantal straatsecties bevatten, welke op hun beurt weer parkeervlakken kennen. Een ‘Parkeervlak’ heeft een GPS-locatie in de vorm van een vlak en er is aangegeven of het tarief fiscaal afgerekend wordt.
Het controleren van de geparkeerde voertuigen verloopt met een scanauto of een handheld. Het scanvoertuig scant het kenteken en het parkeervlak waar het voertuig staat. Aan de hand hiervan kan het controleren of het voertuig een recht heeft voor dit vlak.
De handheld scant hat kenteken en de medewerker krijgt alle rechten terug die aan dit kenteken zijn verstrekt. De medewerker interpreteert deze info en besluit of er een naheffingsaanslag wordt opgelegd. 

![Productgroepen parkeren][productgroepenparkeren]

[parkeren]: image/EAID_84B6B75B_2B58_455d_B019_C9B1E71717C2.gif "Gegevensmodel parekeren"
[productgroepenparkeren]: image/productgroepenparkeren.png "Productgroepen parkeren"
