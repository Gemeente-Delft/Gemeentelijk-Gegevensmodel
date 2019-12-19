# ICT

De in de applicaties aanwezige gegevens zijn gestructureerd volgens bepaalde objecttypes. Deze zijn uitgewerkt in de in deze paragraaf uitgewerkte domeinmodellen.

![Applicaties en Gegevens][ictApplicatiesEnGegevens]

In bovenstaand figuur is te zien hoe objecttypes zijn uitgewerkt. Een objecttype representeert de definitie van een bepaald objecttype. Zo’n objecttype kan nul of meer attributen hebben, die ieder volgens een bepaald datatype zijn. Objecttypes kunnen relaties hebben met andere objecttypes, volgens een bepaald relatiesoort. Ook kunnen objecttypes een generalisatie zijn van een ander objecttype. Hiermee wordt aangegeven dat het ene objecttype attributen en relaties overerft van het andere objecttype. Bovenstaande definitie is gebaseerd op [MIM (Metamodel voor Informatiemodellen)](https://www.geonovum.nl/geo-standaarden/metamodel-informatiemodellering-mim). Hieruit zijn alle relevante definities afgeleid.

Naast de zaken die onderdeel zijn van MIM is er het type Gegeven dat wordt gedefinieerd door een Objecttype. Een Gegeven kan één of meer classificaties hebben. In het huidige model wordt gewerkt met classificatie van persoonsgegevens:

* Geen Persoonsgegevens
* Algemene Persoonsgegevens
* Gevoelige Persoonsgegevens
* Bijzondere Persoonsgegevens

Gegevens kunnen geclassificeerd zijn conform bovenstaande lijst. Dit voor de gegevens zelf en de relaties met andere gegevens.
In bovenstaand figuur is ook te zien dat een Gegeven een Applicatie als authentieke bron kan hebben of dat gegevens afkomstig zijn uit een externe bron.

![ICT Basismodel CMDB][ictBasismodelCMDB]

In voorgaande figuur is een uitwerking voor de CMDB-items gemaakt. Iedere CMDB-Item kan meerdere Log-items hebben waarbinnen aantekeningen worden gelogd. ‘Database’, ‘Server’ en ‘Applicatie’ zijn speciale Linkbare CMDB-items, en kunnen dus koppelingen hebben met andere Linkbare CMDB-Items. Applicaties en Servers kunnen een ‘Leverancier’ hebben.
Een ‘Applicatie’ kan daarnaast diverse medewerkers hebben gekoppeld met een eigen rol, zoals: functioneel beheerder, applicatie-eigenaar en superuser. Een Applicatie heeft één of meer versies en kan meerdere packages hebben. Daarnaast kunnen er documenten en notities zijn gekoppeld aan een ‘Applicatie’.

Naast de Linkbare CMDB-Items zijn er ook reguliere CMDB-Items (niet linkbaar aan andere CMDB-Items). Deze zijn uitgewerkt in

![ICT Overige CMDB][ictOverigeCMDB]

Het model kent naast de Linkbare CMDB-Items de volgende CMDB-Items die direct van CMDB-Item zijn afgeleid: ‘Licentie’, ‘Hardware’, ‘Vervoersmiddel’, ‘Netwerkcomponent’, ‘Toegangsmiddel’, ‘Inventaris’ en ‘Software’.

[ictApplicatiesEnGegevens]: image/EAID_A2831A97_91F6_4ed0_896E_3531219E69F0.gif "ICT Applicaties en Gegevens"
[ictApplicatiesEnGegevens]: image/EAID_A2831A97_91F6_4ed0_896E_3531219E69F0.gif "ICT Applicaties en Gegevens"
[ictBasismodelCMDB]: image/EAID_4F14E8D8_5502_4880_9E83_D912BE451EB1.gif "ICT Basismodel CMDB"
[ictOverigeCMDB]: image/EAID_A255BB0C_A1DB_43a5_88B1_C638F6E64B0B.gif "ICT Overige CMDB"
