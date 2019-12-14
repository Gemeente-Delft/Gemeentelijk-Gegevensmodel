# Archief

Hierna de verschillende entiteiten die betrokken zijn in het archief uitgewerkt.

![Gegevensdefinities Archief][archiefGegevensdefinities]

De centrale entiteit binnen Atlantis en TMS is ‘Archiefstuk’. Archiefstukken verwijzen naar documenten en andere zaken die fysiek in het archief zijn opgeslagen. Archiefstukken zijn terug te vinden op een ‘Vindplaats’ die altijd bestaat uit een ‘Depot’, een ‘Stelling’ binnen dat depot, en daarbinnen direct op een ‘Plank’ of in een ‘Kast’ en daarbinnen op een ‘Plank’. Allen met een eigen nummer, waardoor het archiefstuk is te traceren.
Een ‘Archiefstuk’ is afgeleid van een ‘Document’ uit de RGBZ, zodat het alle kenmerken van ‘Document’ ook heeft. Zo is eenduidigheid tussen documenten binnen processen van de gemeente en te archiveren documenten gewaarborgd. Aanvullend heeft een ‘Archiefstuk’ aanvullende kenmerken vwb: ‘Uitgever’, ‘Rechthebbende’ en ‘Auteur’, die ieder afgeleid zijn van persoonstypen uit de RSGB (zie hiervoor de volgende figuur).
Het entiteit ‘Document’ uit de RGBZ heeft attributen uit de Dublin Core , die nodig zijn voor het correct kunnen archiveren van documenten.
Archiefstukken zijn ondergebracht bij een ‘Collectie’ met eventuele subcollecties en stammen uit een bepaalde ‘Periode’.  

![Archief en bezoekers][archiefEnBezoekers]

In de voorgaande figuur is uitgewerkt dat bezoekers aanvragen kunnen doen en bezoeken kunnen afleggen.

![Archief, personen en documenten][archiefPersonenEnDocumenten]

In voorgaande figuur is uitgewerkt dat uitgevers en rechthebbenden zijn afgeleid van het Kern RSGB-type ‘Rechtspersoon’. Het kunnen immers natuurlijke en niet natuurlijke personen zijn. Bezoekers en auteurs zijn altijd natuurlijke personen en om die reden afgeleid van het  Kern RSGB-type ‘Natuurlijk Persoon’.
Aan het RGBZ-type ‘Document’ is een ‘Identificatiekenmerk’ toegevoegd, zodat verschillende soorten identificaties (zoals: URI, URI, Dot, ISBN) zijn ondersteund.
Archivering zal in de toekomst worden gedaan op basis van de Kern RGBZ-entiteit ‘Zaak’ en  verloopt dan via zaak.archiefnominatie. 

[archiefGegevensdefinities]: image/EAID_59241C4B_FD65_484b_88E5_83189334A510.gif "Gegevensdefinities Archief"
[archiefEnBezoekers]: image/EAID_8D468696_4B9D_40b4_92F0_3BED39502098.gif "Archief en bezoekers"
[archiefPersonenEnDocumenten]: image/EAID_EF872947_BE6B_4af5_8221_2A6AA2A0D4B7.gif "Archief, personen en documenten"
