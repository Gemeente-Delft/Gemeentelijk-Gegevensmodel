# Model ICT
## Inleiding
> **Definitie Model ICT:** 
>
> Het informatiesubdomein dat gegevens omvat over de informatietechnologie en communicatiesystemen die de interne processen en informatievoorziening van een organisatie ondersteunen.

??? info "Kenmerken Model Model ICT"
    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | Model ICT |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.1 |
    | created | 2019-01-10 11:33:20 |
    | modified | 2025-03-27 15:28:35 |
    | id | EAPK_C45CFEC0_B841_4e3b_86BD_A4F3246E94D2 |
    

Het model 'Model ICT' kent de volgende objecttypen:

* **Aanvraag**: (officieel) verzoek, iets (officieel) vragen aan een bevoegde macht.
* **Applicatie**: Een applicatiecomponent die gericht is op het ondersteunen van eindgebruikers.
* **Attribuutsoort**: Attribuutsoort � Stereotype �Attribuutsoort�: De UML-representatie van een attribuutsoort, uitgedrukt in een stereotype van UML-Property3 (metaclass).<br>Er zijn verschillende modelelementen die gebaseerd zijn op UML-property, zoals aangegeven in �2.1.2. Wanneer een UML-property in het informatiemodel de betekenis heeft van een attribuut van een objecttype, dan heeft deze het stereotype �Attribuutsoort�.<br>Een attribuutsoort is een type van gelijksoortige attributen of gegevens. Daartoe kijken we eerst naar het begrip �gegeven�.
* **Classificatie**: Ordening van informatieobjecten in een logisch verband, zoals vastgelegd in een classificatieschema.
* **CMDB-item **: Item in een Configuratie Management DataBase
* **Database**: Een applicatiecomponent die een dataset bevat.
* **Datatype**: Attribuutsoort � Stereotype �Attribuutsoort�: De UML-representatie van een attribuutsoort, uitgedrukt in een stereotype van UML-Property3 (metaclass).<br>Er zijn verschillende modelelementen die gebaseerd zijn op UML-property, zoals aangegeven in �2.1.2. Wanneer een UML-property in het informatiemodel de betekenis heeft van een attribuut van een objecttype, dan heeft deze het stereotype �Attribuutsoort�.<br>Een attribuutsoort is een type van gelijksoortige attributen of gegevens. Daartoe kijken we eerst naar het begrip �gegeven�.
* **Dienst**: Het uitvoeren van werkzaamheden met een continu of periodiek karakter om waarde te realiseren voor een afnemer.
* **Domein/Taakveld**: Kennisgebied of activiteit gekarakteriseerd door een verzameling van concepten, begrippen en/of waarden
* **Externe Bron**: Bron buiten de eigen organisatie
* **Gegeven**: bekend feit waaruit je gevolgtrekkingen kunt maken
* **Generalisatie**: De typering van het hi�rarchische verband tussen een meer generiek object van een objecttype en een meer specifiek object van een ander objecttype waarbij het laatstgenoemde object eigenschappen van het eerstgenoemde object overerft.<br>Toelichting<br>Een generalisatierelatie geeft aan dat bepaalde eigenschappen van een objecttype (vaak attribuutsoorten en/of relatiesoorten) ook gelden voor de gerelateerde objecttypen, �n dat deze qua semantiek, structuur en syntax gelijk zijn. We spreken dan van een supertype met subtypen. De modelelementen die generiek gelden worden in een generiek objecttype, het supertype, gemodelleerd en deze worden overerft door elk subtype (minimaal twee) die de generalisatie relatie legt naar dit generieke objecttype.<br>Voorbeeld: PERCEEL is specialisatie van KADASTRAAL ONROERENDE ZAAK, APPARTEMENTSRECHT is specialisatie van KADASTRAAL ONROERENDE ZAAK. PERCEEL en APPARTEMENTSRECHT hebben beide �Kadastrale aanduiding� en een �relatie met ONROERENDE ZAAK FILIATIE�.
* **Hardware**: Alle fysieke componenten of onderdelen die in een computer een rol spelen.
* **Inventaris**: Een inboedel of een opsomming van voorwerpen op een bepaalde plaats, gemaakt volgens een vaste procedure.
* **Koppeling**: Verbinding tussen twee systemen
* **Licentie**: Een gebruiksrecht en autorisatie om van een product of dienst gebruik te maken binnen bepaalde voorwaarden
* **Linkbaar CMDB-item**: Niet opnemen
* **Log**: Registratie van gegevens.
* **Melding**: De betekenisvolle formulering van een waargenomen feit, waaraan een waarde kan worden toegekend
* **Nertwerkcomponent**: <Geen Definities>
* **Notitie**: Korte, zakelijke uiteenzetting op schrift
* **Objecttype**: De typering van een groep objecten (in de werkelijkheid) die binnen een domein relevant zijn en als gelijksoortig worden beschouwd.<br>Toelichting<br>Jan, Piet en Marie zijn mensen die vanuit het Burgerzaken-domein beschouwd worden als objecten van het type �natuurlijk persoon�. In een ander domein, �de volksmond�, noemen we dit �mens� wat ook een objecttype is. In weer een ander domein is Jan van het type �vergunninghouder� en Piet en Marie niet, omdat aan hen (nog) nooit een vergunning verleend is. Objecttypen zijn een abstractie van de werkelijkheid oftewel we beogen hiermee de werkelijkheid zo getrouw mogelijk te beschrijven, binnen de context van het domein. Dit staat geheel los van het vastleggen van gegevens over objecten van een type in een registratie. Daartoe is veelal een interpretatie nodig (van die werkelijkheid cq. die objecttypen) naar eenheden die in een registratie vastgelegd kunnen worden (records, entiteiten e.d.) op basis van andere overwegingen.
* **Onderwerp**: Op de meest karakteristieke elementen gebaseerde en in woord of eenvoudige zinstructuur samengevatte aanduiding van de inhoud van een document
* **Package**: Een samengesteld bestand of een directory die een aantal bestanden bevat, maar welke als ��n bestand aan de gebruiker getoond word
* **Prijzenboek**: Beschrijving van gangbare onderhoudsactiviteiten met de bijbehorende, actuele prijzen en normen voor de uitvoering.
* **Product**: Het resultaat van een proces dat in het economisch verkeer een waarde bezit.
* **Relatiesoort**: De typering van het structurele verband tussen een object van een objecttype en een (ander) object van een ander (of hetzelfde) objecttype.<br>Toelichting<br>Objecten hebben eigenschappen die gemodelleerd kunnen worden met attribuutsoorten maar ook met relatiesoorten naar andere objecttypen. Als het voor het desbetreffende domein van belang is om die eigenschap te modelleren als onderdeel van een ander objecttype, dan maakt de relatiesoort die eigenschap beschikbaar voor het eerstgenoemde objecttype. Bijvoorbeeld, een attribuutsoort van het objecttype PERSOON zou kunnen zijn �Naam geregistreerd partner� (naast de attribuutsoort �Naam� van PERSOON). De naam van de geregistreerde partner komt evenwel ook beschikbaar met een relatiesoort van PERSOON naar PERSOON: �heeft geregistreerd partnerschap met�. Zie ook het eerder genoemde voorbeeld van SCHIP en MOTOR.<br>Voorbeeld: relatiesoorten �VERBLIJFSOBJECT is gelegen in een PAND� en �SUBJECT heeft als correspondentieadres WOONPLAATS�, of korter, �gelegen in�, �postadres�.<br>Wanneer een relatie (UML-assocation) gebruikt wordt om objecten aan elkaar te verbinden, zonder dat er eigenschappen over deze relatie worden vastgelegd, dan heeft deze het stereotype �Relatiesoort�.
* **Server**: Computer die in een netwerk een ondersteunende taak vervult.
* **Software**: Een geheel van computerprogramma's met bijbehorende data, die bewerkingen en taken uitvoeren
* **Storing**: Verlies van de mogelijkheid om volgens een specificatie te werken of om het vereiste resultaat te leveren.
* **Telefoniegegevens**: Gegevens die worden bewaard van telefoongesprekken
* **Toegangsmiddel**: Een middel waarmee men zich toegang tot iets kan verschaffen.
* **Versie**: De versie-aanduiding van een object.
* **Vervoersmiddel**: Een voertuig dat zich over het land verplaatst.
* **Wijzigingsverzoek**: Een aanvraag voor wijziging


## Objecttypen Model ICT


### Aanvraag
> **Definitie Aanvraag:** 
>
> (officieel) verzoek, iets (officieel) vragen aan een bevoegde macht.

??? info "Kenmerken Model Aanvraag"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Aanvraag |
    | toelichting |  |
    | synoniemen | Verzoek |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.4 |
    | created | 2019-01-10 11:40:16 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_446E3931_B9F2_4b5c_80E7_5B240B8F816F |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Aanvraag |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-b8b3fe1a-ea07-49a3-8580-4291afa6f26d](https://gemmaonline.nl/index.php/GEMMA/id-b8b3fe1a-ea07-49a3-8580-4291afa6f26d) |
    | gemma_definitie | (officieel) verzoek, iets (officieel) vragen aan een bevoegde macht. |
    | gemma_toelichting |  |
    

Attributen van objecttype Aanvraag

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Applicatie
> **Definitie Applicatie:** 
>
> Een applicatiecomponent die gericht is op het ondersteunen van eindgebruikers.

??? info "Kenmerken Model Applicatie"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Applicatie |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.5 |
    | created | 2019-01-10 11:33:53 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_A8945FD7_EA20_418e_8E7F_18F13F16E338 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Applicatie |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-f5c91145-fba4-47cb-aaf9-bb9c64e19a21](https://gemmaonline.nl/index.php/GEMMA/id-f5c91145-fba4-47cb-aaf9-bb9c64e19a21) |
    | gemma_definitie | Een applicatiecomponent die gericht is op het ondersteunen van eindgebruikers. |
    | gemma_toelichting |  |
    

Attributen van objecttype Applicatie

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| naam | AN255 |  |
| categorie | Enumeratie: "Applicatiecategorie" |  |
| beheerstatus | int |  |
| packagingstatus | int |  |
| applicatieURL | AN255 |  |
| guid | guid |  |
| omschrijving | Text |  |
| beleidsdomein | AN255 |  |



### Attribuutsoort
> **Definitie Attribuutsoort:** 
>
> Attribuutsoort � Stereotype �Attribuutsoort�: De UML-representatie van een attribuutsoort, uitgedrukt in een stereotype van UML-Property3 (metaclass).<br>Er zijn verschillende modelelementen die gebaseerd zijn op UML-property, zoals aangegeven in �2.1.2. Wanneer een UML-property in het informatiemodel de betekenis heeft van een attribuut van een objecttype, dan heeft deze het stereotype �Attribuutsoort�.<br>Een attribuutsoort is een type van gelijksoortige attributen of gegevens. Daartoe kijken we eerst naar het begrip �gegeven�.

??? info "Kenmerken Model Attribuutsoort"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Attribuutsoort |
    | toelichting |  |
    | synoniemen | Attribuut |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.4 |
    | created | 2019-01-15 10:57:58 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_8D273DE5_3529_4652_BCA1_F86B28F26017 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Attribuutsoort

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| naam | AN80 |  |
| herkomst | AN80 | De registratie in wiens catalogus het objecttype is gespecificeerd (oftewel de registratie waar het objecttype deel van uitmaakt). Deze specificatie is toegevoegd omdat het wel duidelijk moet zijn in welke (basis)registratie of informatiemodel het objecttype voorkomt (indien van toepassing). |
| definitie | Text | De beschrijving van de betekenis van het objecttype zoals gespecificeerd in de catalogus van de desbetreffende (basis)registratie of informatiemodel. |
| herkomstDefinitie | AN80 |  |
| datumOpname | Date | De datum waarop het objecttype is opgenomen in het informatiemodel. |
| domein | AN80 | <i>Domein is zelf geen metadata aspect. Onder het kopje �domein� vallen een aantal metadata aspecten die gelden voor een waarde, oftewel de eisen waaraan een waarde van een attribuutsoort moet voldoen.</i> |
| lengte | AN40 | De aanduiding van de lengte van een gegeven. Getallen kunnen altijd positief of negatief zijn.<br><i>Bijvoorbeeld:</i><br><i>�1� als de lengte exact 1 is;</i><br><i>�1..2� als de lengte 1 tot en met 2 lang kan zijn; '�1,2� voor Decimale getallen met 1 cijfer voor de komma en 2 erna. </i>Dit is van -9,99 tot +9,99; |
| patroon | AN40 | Alleen van toepassing wanneer het type van het attribuutsoort een primitief datatype is.<br>De verzameling van waarden die gegevens van deze attribuutsoort kunnen hebben, dat wil zeggen het waardenbereik, uitgedrukt in een specifieke structuur. |
| toelichting | Text |  |
| indicatieMaterieleHistorie | boolean | Indicatie of de materi�le historie van de attribuutsoort te bevragen is. Materi�le historie geeft aan wanneer een verandering is opgetreden in de werkelijkheid die heeft geleid tot verandering van de attribuutwaarde. |
| kardinaliteit | AN40 | Deze indicatie geeft aan hoeveel keer waarden van deze attribuutsoort kunnen voorkomen bij een object van het betreffende objecttype, of bij het betreffende gegevensgroeptype:<br>0..1: is soms niet beschikbaar<br>1 : is altijd beschikbaar<br>0..*: is niet altijd beschikbaar, kan<br>meerdere malen voorkomen 1..*: is altijd beschikbaar, kan<br>meerdere malen voorkomen<br>Indien een attribuutsoort deel uit maakt van een gegevensgroeptype, dan wordt de kardinaliteit vermeld van het attribuutsoort binnen het gegevensgroeptype. Voor de uiteindelijke kardinaliteit van hoe vaak een gegeven voorkomt bij het object moet rekening gehouden worden met de kardinaliteit van de gegevensgroep en met de kardinaliteit van de attribuutsoort. |
| authentiek | boolean |  |
| indicatieAfleidbaar | boolean | Aanduiding dat gegeven afleidbaar is uit andere attribuut- en/of relatiesoorten. |
| mogelijkGeenWaarde | boolean |  |
| identificerend | boolean | Aanduiding dat attribuutsoort onderdeel uitmaakt van de unieke aanduiding van een object |
| id | int |  |
| stereotype | AN40 |  |
| precisie | int |  |
| ea_guid | guid |  |



### Classificatie
> **Definitie Classificatie:** 
>
> Ordening van informatieobjecten in een logisch verband, zoals vastgelegd in een classificatieschema.

??? info "Kenmerken Model Classificatie"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Classificatie |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.5 |
    | created | 2019-01-10 14:51:23 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_81F207D0_A071_48c7_8C4C_25F8D25A3DE8 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Classificatie

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| bevatPersoonsgegevens | Persoonsgegevens |  |
| id | guid |  |
| gerelateerdPersoonsgegevens | Persoonsgegevens |  |



### CMDB-item 
> **Definitie CMDB-item :** 
>
> Item in een Configuratie Management DataBase

??? info "Kenmerken Model CMDB-item "
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | CMDB-item |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.5 |
    | created | 2019-01-10 15:17:26 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_B027D022_41D9_4c63_A63D_8F5111689564 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | CMDBItem |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-f5365fcc-279e-42e5-bde4-e7b10700a8ed](https://gemmaonline.nl/index.php/GEMMA/id-f5365fcc-279e-42e5-bde4-e7b10700a8ed) |
    | gemma_definitie | Item in een Configuratie Management DataBase |
    | gemma_toelichting |  |
    

Attributen van objecttype CMDB-item 

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| naam | AN255 |  |
| beschrijving | Text |  |



### Database
> **Definitie Database:** 
>
> Een applicatiecomponent die een dataset bevat.

??? info "Kenmerken Model Database"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Database |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.5 |
    | created | 2019-01-10 11:48:48 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_FFD22E11_7A3A_459a_B575_928C67E8D1F3 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Database |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-d548564c-a918-47e4-ae60-697f0ed3e7aa](https://gemmaonline.nl/index.php/GEMMA/id-d548564c-a918-47e4-ae60-697f0ed3e7aa) |
    | gemma_definitie | Een applicatiecomponent die een dataset bevat. |
    | gemma_toelichting |  |
    

Attributen van objecttype Database

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| database | AN40 |  |
| omschrijving | AN80 |  |
| DBMS | AN40 |  |
| architectuur | AN40 |  |
| OTAP |  |  |
| databaseVersie | AN40 |  |
| vlan | AN40 |  |



### Datatype
> **Definitie Datatype:** 
>
> Attribuutsoort � Stereotype �Attribuutsoort�: De UML-representatie van een attribuutsoort, uitgedrukt in een stereotype van UML-Property3 (metaclass).<br>Er zijn verschillende modelelementen die gebaseerd zijn op UML-property, zoals aangegeven in �2.1.2. Wanneer een UML-property in het informatiemodel de betekenis heeft van een attribuut van een objecttype, dan heeft deze het stereotype �Attribuutsoort�.<br>Een attribuutsoort is een type van gelijksoortige attributen of gegevens. Daartoe kijken we eerst naar het begrip �gegeven�.

??? info "Kenmerken Model Datatype"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Datatype |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.5 |
    | created | 2019-01-15 15:05:26 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_7EFBF1CA_EC6E_4b8a_B97F_453CA32AB9A5 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Datatype

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| naam | AN255 |  |
| herkomst | AN255 | De registratie in wiens catalogus het objecttype is gespecificeerd (oftewel de registratie waar het objecttype deel van uitmaakt). Deze specificatie is toegevoegd omdat het wel duidelijk moet zijn in welke (basis)registratie of informatiemodel het objecttype voorkomt (indien van toepassing). |
| definitie | Text | De beschrijving van de betekenis van het objecttype zoals gespecificeerd in de catalogus van de desbetreffende (basis)registratie of informatiemodel. |
| datumOpname | Date | De datum waarop het objecttype is opgenomen in het informatiemodel. |
| domein | AN255 | <i>Domein is zelf geen metadata aspect. Onder het kopje �domein� vallen een aantal metadata aspecten die gelden voor een waarde, oftewel de eisen waaraan een waarde van een attribuutsoort moet voldoen.</i> |
| lengte | AN40 | De aanduiding van de lengte van een gegeven. Getallen kunnen altijd positief of negatief zijn.<br><i>Bijvoorbeeld:</i><br><i>�1� als de lengte exact 1 is;</i><br><i>�1..2� als de lengte 1 tot en met 2 lang kan zijn; '�1,2� voor Decimale getallen met 1 cijfer voor de komma en 2 erna. </i>Dit is van -9,99 tot +9,99; |
| patroon | AN40 | Alleen van toepassing wanneer het type van het attribuutsoort een primitief datatype is.<br>De verzameling van waarden die gegevens van deze attribuutsoort kunnen hebben, dat wil zeggen het waardenbereik, uitgedrukt in een specifieke structuur. |
| toelichting | Text |  |
| id | int |  |
| ea_guid | guid |  |
| kardinaliteit | AN40 | Deze indicatie geeft aan hoeveel keer waarden van deze attribuutsoort kunnen voorkomen bij een object van het betreffende objecttype, of bij het betreffende gegevensgroeptype:<br>0..1: is soms niet beschikbaar<br>1 : is altijd beschikbaar<br>0..*: is niet altijd beschikbaar, kan<br>meerdere malen voorkomen 1..*: is altijd beschikbaar, kan<br>meerdere malen voorkomen<br>Indien een attribuutsoort deel uit maakt van een gegevensgroeptype, dan wordt de kardinaliteit vermeld van het attribuutsoort binnen het gegevensgroeptype. Voor de uiteindelijke kardinaliteit van hoe vaak een gegeven voorkomt bij het object moet rekening gehouden worden met de kardinaliteit van de gegevensgroep en met de kardinaliteit van de attribuutsoort. |



### Dienst
> **Definitie Dienst:** 
>
> Het uitvoeren van werkzaamheden met een continu of periodiek karakter om waarde te realiseren voor een afnemer.

??? info "Kenmerken Model Dienst"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Dienst |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.5 |
    | created | 2019-02-07 14:51:15 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_45AFD4E2_9909_4c33_93CE_F2466B85CA0F |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Dienst |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-6cc63d39-c5a3-4d09-8eab-22e56384fe7e](https://gemmaonline.nl/index.php/GEMMA/id-6cc63d39-c5a3-4d09-8eab-22e56384fe7e) |
    | gemma_definitie | Het uitvoeren van werkzaamheden met een continu of periodiek karakter om waarde te realiseren voor een afnemer. |
    | gemma_toelichting |  |
    

Attributen van objecttype Dienst

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Domein/Taakveld
> **Definitie Domein/Taakveld:** 
>
> Kennisgebied of activiteit gekarakteriseerd door een verzameling van concepten, begrippen en/of waarden

??? info "Kenmerken Model Domein/Taakveld"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Domein/Taakveld |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.5 |
    | created | 2019-02-07 14:40:39 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_BEFEC56A_EF6C_49f0_9368_7E46F75D9562 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | DomeinOfTaakveld |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-a6ea9d59-4ac3-4aca-ba3f-1b52e741b56b](https://gemmaonline.nl/index.php/GEMMA/id-a6ea9d59-4ac3-4aca-ba3f-1b52e741b56b) |
    | gemma_definitie | Kennisgebied of activiteit gekarakteriseerd door een verzameling van concepten, begrippen en/of waarden |
    | gemma_toelichting |  |
    

Attributen van objecttype Domein/Taakveld

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Externe Bron
> **Definitie Externe Bron:** 
>
> Bron buiten de eigen organisatie

??? info "Kenmerken Model Externe Bron"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Externe Bron |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.5 |
    | created | 2019-01-10 14:50:29 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_144D1047_35BB_4926_9472_895D89DC2E0C |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | ExterneBron |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-c8645fb0-cd62-4940-9e68-306579d7dfd0](https://gemmaonline.nl/index.php/GEMMA/id-c8645fb0-cd62-4940-9e68-306579d7dfd0) |
    | gemma_definitie | Bron buiten de eigen organisatie |
    | gemma_toelichting |  |
    

Attributen van objecttype Externe Bron

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| guid | guid |  |
| naam | AN255 |  |



### Gegeven
> **Definitie Gegeven:** 
>
> bekend feit waaruit je gevolgtrekkingen kunt maken

??? info "Kenmerken Model Gegeven"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Gegeven |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.7 |
    | created | 2019-01-10 14:50:41 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_E846CC36_DF4A_4398_AE4C_122CAFEBAEAA |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Gegeven |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-38d8e66f-29f5-4387-b12f-1291ee266080](https://gemmaonline.nl/index.php/GEMMA/id-38d8e66f-29f5-4387-b12f-1291ee266080) |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Gegeven

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| id | int |  |
| naam | AN255 |  |
| alias | AN255 |  |
| toelichting | Text |  |
| stereotype | AN255 |  |
| ea_guid | guid |  |



### Generalisatie
> **Definitie Generalisatie:** 
>
> De typering van het hi�rarchische verband tussen een meer generiek object van een objecttype en een meer specifiek object van een ander objecttype waarbij het laatstgenoemde object eigenschappen van het eerstgenoemde object overerft.<br>Toelichting<br>Een generalisatierelatie geeft aan dat bepaalde eigenschappen van een objecttype (vaak attribuutsoorten en/of relatiesoorten) ook gelden voor de gerelateerde objecttypen, �n dat deze qua semantiek, structuur en syntax gelijk zijn. We spreken dan van een supertype met subtypen. De modelelementen die generiek gelden worden in een generiek objecttype, het supertype, gemodelleerd en deze worden overerft door elk subtype (minimaal twee) die de generalisatie relatie legt naar dit generieke objecttype.<br>Voorbeeld: PERCEEL is specialisatie van KADASTRAAL ONROERENDE ZAAK, APPARTEMENTSRECHT is specialisatie van KADASTRAAL ONROERENDE ZAAK. PERCEEL en APPARTEMENTSRECHT hebben beide �Kadastrale aanduiding� en een �relatie met ONROERENDE ZAAK FILIATIE�.

??? info "Kenmerken Model Generalisatie"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Generalisatie |
    | toelichting | Een generalisatierelatie geeft aan dat bepaalde eigenschappen van een objecttype (vaak attribuutsoorten en/of relatiesoorten) ook gelden voor de gerelateerde objecttypen, �n dat deze qua semantiek, structuur en syntax gelijk zijn. We spreken dan van een s |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.5 |
    | created | 2019-01-15 14:59:27 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_0CF1C34D_8AD5_4ac5_8538_87252E66A8C8 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Generalisatie

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| naam | AN255 |  |
| herkomst | AN255 | De registratie in wiens catalogus het objecttype is gespecificeerd (oftewel de registratie waar het objecttype deel van uitmaakt). Deze specificatie is toegevoegd omdat het wel duidelijk moet zijn in welke (basis)registratie of informatiemodel het objecttype voorkomt (indien van toepassing). |
| definitie | Text | De beschrijving van de betekenis van het objecttype zoals gespecificeerd in de catalogus van de desbetreffende (basis)registratie of informatiemodel. |
| herkomstDefinitie | AN255 |  |
| datumOpname | Date | De datum waarop het objecttype is opgenomen in het informatiemodel. |
| id | int |  |
| ea_guid | guid |  |
| toelichting | Text |  |
| indicatieMaterieleHistorie | boolean | Indicatie of de materi�le historie van de attribuutsoort te bevragen is. Materi�le historie geeft aan wanneer een verandering is opgetreden in de werkelijkheid die heeft geleid tot verandering van de attribuutwaarde. |



### Hardware
> **Definitie Hardware:** 
>
> Alle fysieke componenten of onderdelen die in een computer een rol spelen.

??? info "Kenmerken Model Hardware"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Hardware |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.5 |
    | created | 2019-01-10 11:35:52 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_6C92F0F8_BC92_428c_B729_1A10D515DAEF |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Hardware |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-acbda3e0-9767-49bb-8d4c-2b5ea0160056](https://gemmaonline.nl/index.php/GEMMA/id-acbda3e0-9767-49bb-8d4c-2b5ea0160056) |
    | gemma_definitie | Alle fysieke componenten of onderdelen die in een computer een rol spelen. |
    | gemma_toelichting |  |
    

Attributen van objecttype Hardware

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Inventaris
> **Definitie Inventaris:** 
>
> Een inboedel of een opsomming van voorwerpen op een bepaalde plaats, gemaakt volgens een vaste procedure.

??? info "Kenmerken Model Inventaris"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Inventaris |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.5 |
    | created | 2019-01-10 11:37:23 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_D0AB8CF6_F6CC_4337_BE07_DFE6B3CEFBB3 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Inventaris |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-41cea01b-de1c-4ee5-92c4-776fe8a17753](https://gemmaonline.nl/index.php/GEMMA/id-41cea01b-de1c-4ee5-92c4-776fe8a17753) |
    | gemma_definitie | Een inboedel of een opsomming van voorwerpen op een bepaalde plaats, gemaakt volgens een vaste procedure. |
    | gemma_toelichting |  |
    

Attributen van objecttype Inventaris

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Koppeling
> **Definitie Koppeling:** 
>
> Verbinding tussen twee systemen

??? info "Kenmerken Model Koppeling"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Koppeling |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.5 |
    | created | 2019-01-10 11:49:07 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_AB7CF266_388F_413a_92D0_B2FA67C75633 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Koppeling

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| direct | boolean |  |
| beschrijving | AN200 |  |
| toelichting | text |  |



### Licentie
> **Definitie Licentie:** 
>
> Een gebruiksrecht en autorisatie om van een product of dienst gebruik te maken binnen bepaalde voorwaarden

??? info "Kenmerken Model Licentie"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Licentie |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.5 |
    | created | 2019-01-10 11:36:55 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_2E5F9AF9_D1BA_4dc0_9621_4101D24B8ABD |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Licentie |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-764e6fdf-299f-4867-8257-7532f1e56ebf](https://gemmaonline.nl/index.php/GEMMA/id-764e6fdf-299f-4867-8257-7532f1e56ebf) |
    | gemma_definitie | Een gebruiksrecht en autorisatie om van een product of dienst gebruik te maken binnen bepaalde voorwaarden |
    | gemma_toelichting |  |
    

Attributen van objecttype Licentie

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Linkbaar CMDB-item
> **Definitie Linkbaar CMDB-item:** 
>
> Niet opnemen

??? info "Kenmerken Model Linkbaar CMDB-item"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Linkbaar CMDB-item |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.5 |
    | created | 2019-01-10 16:32:50 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_C0F1A08E_C6CD_4524_A2E0_0E5CA483DCFD |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | LinkbaarCMDBItem |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-5003634c-22b1-4f9a-bf73-8cdb4c42a8b4](https://gemmaonline.nl/index.php/GEMMA/id-5003634c-22b1-4f9a-bf73-8cdb4c42a8b4) |
    | gemma_definitie | Niet opnemen |
    | gemma_toelichting |  |
    

Attributen van objecttype Linkbaar CMDB-item

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Log
> **Definitie Log:** 
>
> Registratie van gegevens.

??? info "Kenmerken Model Log"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Log |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.5 |
    | created | 2019-01-10 11:49:38 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_5492ED6D_608E_465e_B975_BCADAAA3EE7F |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Log |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-faf0976b-5000-4eb1-976d-10a3d7edf2c5](https://gemmaonline.nl/index.php/GEMMA/id-faf0976b-5000-4eb1-976d-10a3d7edf2c5) |
    | gemma_definitie | Registratie van gegevens. |
    | gemma_toelichting |  |
    

Attributen van objecttype Log

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| tijd | DateTime |  |
| korteOmschrijving | AN80 |  |
| omschrijving | Text |  |



### Melding
> **Definitie Melding:** 
>
> De betekenisvolle formulering van een waargenomen feit, waaraan een waarde kan worden toegekend

??? info "Kenmerken Model Melding"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Melding |
    | toelichting |  |
    | synoniemen | Datapunt |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.4 |
    | created | 2019-01-10 11:38:45 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_6100B3C7_FBCE_434d_BA48_E067B9CF84A7 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Melding |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-fadba6bd-b55a-4d68-8136-096db8f3df5e](https://gemmaonline.nl/index.php/GEMMA/id-fadba6bd-b55a-4d68-8136-096db8f3df5e) |
    | gemma_definitie | De betekenisvolle formulering van een waargenomen feit, waaraan een waarde kan worden toegekend |
    | gemma_toelichting |  |
    

Attributen van objecttype Melding

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Nertwerkcomponent
> **Definitie Nertwerkcomponent:** 
>
> Geen Definitie

??? info "Kenmerken Model Nertwerkcomponent"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Nertwerkcomponent |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.3 |
    | created | 2019-01-10 11:35:05 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_DD277E82_0CA5_4460_918F_9178B5F01886 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Nertwerkcomponent |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-6a2e72c3-94f8-4dfd-a68c-03aab1279c75](https://gemmaonline.nl/index.php/GEMMA/id-6a2e72c3-94f8-4dfd-a68c-03aab1279c75) |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Nertwerkcomponent

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Notitie
> **Definitie Notitie:** 
>
> Korte, zakelijke uiteenzetting op schrift

??? info "Kenmerken Model Notitie"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Notitie |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.5 |
    | created | 2019-01-14 16:44:58 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_354E5545_D067_4b81_9D1D_C5F5FFB532C7 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Notitie |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-ca903c71-96d8-4db2-9aa9-52210dd02c1d](https://gemmaonline.nl/index.php/GEMMA/id-ca903c71-96d8-4db2-9aa9-52210dd02c1d) |
    | gemma_definitie | Korte, zakelijke uiteenzetting op schrift |
    | gemma_toelichting |  |
    

Attributen van objecttype Notitie

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| datum | Date |  |
| inhoud | Text |  |



### Objecttype
> **Definitie Objecttype:** 
>
> De typering van een groep objecten (in de werkelijkheid) die binnen een domein relevant zijn en als gelijksoortig worden beschouwd.<br>Toelichting<br>Jan, Piet en Marie zijn mensen die vanuit het Burgerzaken-domein beschouwd worden als objecten van het type �natuurlijk persoon�. In een ander domein, �de volksmond�, noemen we dit �mens� wat ook een objecttype is. In weer een ander domein is Jan van het type �vergunninghouder� en Piet en Marie niet, omdat aan hen (nog) nooit een vergunning verleend is. Objecttypen zijn een abstractie van de werkelijkheid oftewel we beogen hiermee de werkelijkheid zo getrouw mogelijk te beschrijven, binnen de context van het domein. Dit staat geheel los van het vastleggen van gegevens over objecten van een type in een registratie. Daartoe is veelal een interpretatie nodig (van die werkelijkheid cq. die objecttypen) naar eenheden die in een registratie vastgelegd kunnen worden (records, entiteiten e.d.) op basis van andere overwegingen.

??? info "Kenmerken Model Objecttype"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Objecttype |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.5 |
    | created | 2019-01-10 14:50:11 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_A2451674_6C19_4bf9_81F9_57CDE2F60144 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Objecttype

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| naam | AN255 |  |
| herkomst | AN255 | De registratie in wiens catalogus het objecttype is gespecificeerd (oftewel de registratie waar het objecttype deel van uitmaakt). Deze specificatie is toegevoegd omdat het wel duidelijk moet zijn in welke (basis)registratie of informatiemodel het objecttype voorkomt (indien van toepassing). |
| definitie | Text | De beschrijving van de betekenis van het objecttype zoals gespecificeerd in de catalogus van de desbetreffende (basis)registratie of informatiemodel. |
| herkomstDefinitie | AN255 |  |
| datumOpname | Date | De datum waarop het objecttype is opgenomen in het informatiemodel. |
| uniekeAanduiding | AN255 | Voor objecttypen die deel uitmaken van een (basis)registratie of informatiemodel betreft dit de wijze waarop daarin voorkomende objecten (van dit type) uniek in de registratie worden aangeduid. |
| populatie | Text | Voor objecttypen die deel uitmaken van een (basis)registratie betreft dit de beschrijving van de exemplaren van het gedefinieerde objecttype die in de desbetreffende (basis)- registratie voorhanden zijn. |
| kwaliteit | AN255 | Voor objecttypen die deel uitmaken van een registratie betreft dit de waarborgen voor de juistheid van de in de registratie opgenomen objecten van het desbetreffende type. |
| toelichting | Text |  |
| indicatieAbstract | boolean | Conceptueel model: indicatie dat het objecttype een generalisatie is,<br>waarvan een object als specialisatie altijd voorkomt in de hoedanigheid van een (en slechts ��n) van de specialisaties van het betreffende objecttype.<br>Logisch model: Indicatie dat er geen instanties (objecten) voor het betreffende objecttype mogen voorkomen. |
| id | int |  |
| stereotype | AN255 |  |
| ea_guid | guid |  |
| supertype | Class: "Generalisatie" |  |



### Onderwerp
> **Definitie Onderwerp:** 
>
> Op de meest karakteristieke elementen gebaseerde en in woord of eenvoudige zinstructuur samengevatte aanduiding van de inhoud van een document

??? info "Kenmerken Model Onderwerp"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Onderwerp |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.5 |
    | created | 2019-02-07 14:51:28 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_2AA9DB3B_D79C_490d_8776_DA1CB25E9B09 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Onderwerp

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Package
> **Definitie Package:** 
>
> Een samengesteld bestand of een directory die een aantal bestanden bevat, maar welke als ��n bestand aan de gebruiker getoond word

??? info "Kenmerken Model Package"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Package |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.5 |
    | created | 2019-01-14 16:49:18 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_ACE86CFF_D6D0_4cbd_8395_99BD763F1B37 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Package |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-16727428-b97d-498b-9d5a-91b71dd67dc1](https://gemmaonline.nl/index.php/GEMMA/id-16727428-b97d-498b-9d5a-91b71dd67dc1) |
    | gemma_definitie | Een samengesteld bestand of een directory die een aantal bestanden bevat, maar welke als ��n bestand aan de gebruiker getoond word |
    | gemma_toelichting |  |
    

Attributen van objecttype Package

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| naam | AN80 |  |
| status | AN40 |  |
| proces | AN40 |  |
| project | AN40 |  |
| toelichting | Text |  |



### Prijzenboek
> **Definitie Prijzenboek:** 
>
> Beschrijving van gangbare onderhoudsactiviteiten met de bijbehorende, actuele prijzen en normen voor de uitvoering.

??? info "Kenmerken Model Prijzenboek"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Prijzenboek |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.5 |
    | created | 2019-02-07 14:45:09 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_F1489610_1E50_4328_8CD8_F41E9CE0C0D8 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Prijzenboek

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Product
> **Definitie Product:** 
>
> Het resultaat van een proces dat in het economisch verkeer een waarde bezit.

??? info "Kenmerken Model Product"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Product |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.5 |
    | created | 2019-02-07 14:41:02 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_D5DD2F67_6A1F_46b0_972E_795ECC4B2E4F |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Product |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-3b8b01b0-7870-48fb-b4a7-6a5a593e4ea3](https://gemmaonline.nl/index.php/GEMMA/id-3b8b01b0-7870-48fb-b4a7-6a5a593e4ea3) |
    | gemma_definitie | Het resultaat van een proces dat in het economisch verkeer een waarde bezit. |
    | gemma_toelichting |  |
    

Attributen van objecttype Product

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Relatiesoort
> **Definitie Relatiesoort:** 
>
> De typering van het structurele verband tussen een object van een objecttype en een (ander) object van een ander (of hetzelfde) objecttype.<br>Toelichting<br>Objecten hebben eigenschappen die gemodelleerd kunnen worden met attribuutsoorten maar ook met relatiesoorten naar andere objecttypen. Als het voor het desbetreffende domein van belang is om die eigenschap te modelleren als onderdeel van een ander objecttype, dan maakt de relatiesoort die eigenschap beschikbaar voor het eerstgenoemde objecttype. Bijvoorbeeld, een attribuutsoort van het objecttype PERSOON zou kunnen zijn �Naam geregistreerd partner� (naast de attribuutsoort �Naam� van PERSOON). De naam van de geregistreerde partner komt evenwel ook beschikbaar met een relatiesoort van PERSOON naar PERSOON: �heeft geregistreerd partnerschap met�. Zie ook het eerder genoemde voorbeeld van SCHIP en MOTOR.<br>Voorbeeld: relatiesoorten �VERBLIJFSOBJECT is gelegen in een PAND� en �SUBJECT heeft als correspondentieadres WOONPLAATS�, of korter, �gelegen in�, �postadres�.<br>Wanneer een relatie (UML-assocation) gebruikt wordt om objecten aan elkaar te verbinden, zonder dat er eigenschappen over deze relatie worden vastgelegd, dan heeft deze het stereotype �Relatiesoort�.

??? info "Kenmerken Model Relatiesoort"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Relatiesoort |
    | toelichting | Objecten hebben eigenschappen die gemodelleerd kunnen worden met attribuutsoorten maar ook met relatiesoorten naar andere objecttypen. Als het voor het desbetreffende domein van belang is om die eigenschap te modelleren als onderdeel van een ander objectt |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.5 |
    | created | 2019-01-15 14:49:11 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_DFD2814E_7D36_45e2_B082_2ED574A409E1 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Relatiesoort

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| naam | AN80 |  |
| herkomst | AN80 | De registratie in wiens catalogus het objecttype is gespecificeerd (oftewel de registratie waar het objecttype deel van uitmaakt). Deze specificatie is toegevoegd omdat het wel duidelijk moet zijn in welke (basis)registratie of informatiemodel het objecttype voorkomt (indien van toepassing). |
| definitie | Text | De beschrijving van de betekenis van het objecttype zoals gespecificeerd in de catalogus van de desbetreffende (basis)registratie of informatiemodel. |
| herkomstDefinitie | AN80 |  |
| datumOpname | Date | De datum waarop het objecttype is opgenomen in het informatiemodel. |
| toelichting | Text |  |
| indicatieMaterieleHistorie | boolean | Indicatie of de materi�le historie van de attribuutsoort te bevragen is. Materi�le historie geeft aan wanneer een verandering is opgetreden in de werkelijkheid die heeft geleid tot verandering van de attribuutwaarde. |
| kardinaliteit | AN40 | Deze indicatie geeft aan hoeveel keer waarden van deze attribuutsoort kunnen voorkomen bij een object van het betreffende objecttype, of bij het betreffende gegevensgroeptype:<br>0..1: is soms niet beschikbaar<br>1 : is altijd beschikbaar<br>0..*: is niet altijd beschikbaar, kan<br>meerdere malen voorkomen 1..*: is altijd beschikbaar, kan<br>meerdere malen voorkomen<br>Indien een attribuutsoort deel uit maakt van een gegevensgroeptype, dan wordt de kardinaliteit vermeld van het attribuutsoort binnen het gegevensgroeptype. Voor de uiteindelijke kardinaliteit van hoe vaak een gegeven voorkomt bij het object moet rekening gehouden worden met de kardinaliteit van de gegevensgroep en met de kardinaliteit van de attribuutsoort. |
| authentiek | boolean |  |
| unidirectioneel | AN40 | Het gerelateerde objecttype (de target) waarvan het objecttype, die de eigenaar is van deze relatie (de source), kennis heeft.<br>Alle relaties zijn altijd gericht van het objecttype (source) naar het gerelateerde objecttype (target). |
| id | int |  |
| indicatieAfleidbaar | boolean | Aanduiding dat gegeven afleidbaar is uit andere attribuut- en/of relatiesoorten. |
| ea_guid | guid |  |
| mogelijkGeenWaarde | boolean |  |



### Server
> **Definitie Server:** 
>
> Computer die in een netwerk een ondersteunende taak vervult.

??? info "Kenmerken Model Server"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Server |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.5 |
    | created | 2019-01-10 11:34:53 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_3AFD7E5F_8061_4776_A332_334AF4125E7D |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Server |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-4694a321-36db-4a54-a7ab-6c3895a4e288](https://gemmaonline.nl/index.php/GEMMA/id-4694a321-36db-4a54-a7ab-6c3895a4e288) |
    | gemma_definitie | Computer die in een netwerk een ondersteunende taak vervult. |
    | gemma_toelichting |  |
    

Attributen van objecttype Server

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| serverID | AN20 |  |
| organisatie | AN80 |  |
| servertype | Enumeratie: "Servertypes" |  |
| IPAdres | AN40 |  |
| vlan | AN40 |  |
| serienummer | AN40 |  |
| locatie | AN40 |  |
| actief | boolean |  |



### Software
> **Definitie Software:** 
>
> Een geheel van computerprogramma's met bijbehorende data, die bewerkingen en taken uitvoeren

??? info "Kenmerken Model Software"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Software |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.5 |
    | created | 2019-01-10 11:36:22 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_0B3C37DD_42A1_4b6b_B534_CD276112FD3B |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Software |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-d35905fd-2aad-49e6-8ee5-5147c253a478](https://gemmaonline.nl/index.php/GEMMA/id-d35905fd-2aad-49e6-8ee5-5147c253a478) |
    | gemma_definitie | Een geheel van computerprogramma's met bijbehorende data, die bewerkingen en taken uitvoeren |
    | gemma_toelichting |  |
    

Attributen van objecttype Software

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Storing
> **Definitie Storing:** 
>
> Verlies van de mogelijkheid om volgens een specificatie te werken of om het vereiste resultaat te leveren.

??? info "Kenmerken Model Storing"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Storing |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.5 |
    | created | 2019-01-10 11:40:28 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_4E5F272E_00CA_481c_A51B_7D08B5E6B0A9 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Storing |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-ad9da532-d9a3-4c82-858d-e58a61ddf95f](https://gemmaonline.nl/index.php/GEMMA/id-ad9da532-d9a3-4c82-858d-e58a61ddf95f) |
    | gemma_definitie | Verlies van de mogelijkheid om volgens een specificatie te werken of om het vereiste resultaat te leveren. |
    | gemma_toelichting |  |
    

Attributen van objecttype Storing

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Telefoniegegevens
> **Definitie Telefoniegegevens:** 
>
> Gegevens die worden bewaard van telefoongesprekken

??? info "Kenmerken Model Telefoniegegevens"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Telefoniegegevens |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.5 |
    | created | 2019-01-10 11:37:09 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_DDD2167F_4A0F_468b_894E_6BB9ED9DA5E0 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Telefoniegegevens |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-e63e4e3c-ca45-4690-aa55-c38a1bc73d2c](https://gemmaonline.nl/index.php/GEMMA/id-e63e4e3c-ca45-4690-aa55-c38a1bc73d2c) |
    | gemma_definitie | Gegevens die worden bewaard van telefoongesprekken |
    | gemma_toelichting |  |
    

Attributen van objecttype Telefoniegegevens

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Toegangsmiddel
> **Definitie Toegangsmiddel:** 
>
> Een middel waarmee men zich toegang tot iets kan verschaffen.

??? info "Kenmerken Model Toegangsmiddel"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Toegangsmiddel |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.5 |
    | created | 2019-01-10 11:37:51 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_D67A4AC2_9A17_4cd0_82D7_732A89018FDA |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Toegangsmiddel |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-55c7fd37-4d03-45f4-b374-69aa690d1477](https://gemmaonline.nl/index.php/GEMMA/id-55c7fd37-4d03-45f4-b374-69aa690d1477) |
    | gemma_definitie | Een middel waarmee men zich toegang tot iets kan verschaffen. |
    | gemma_toelichting |  |
    

Attributen van objecttype Toegangsmiddel

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Versie
> **Definitie Versie:** 
>
> De versie-aanduiding van een object.

??? info "Kenmerken Model Versie"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Versie |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.5 |
    | created | 2019-01-14 16:36:00 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_39445166_1EAB_43f8_9F5C_89EA606605EE |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Versie |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-3d765f43-c4e8-4556-850b-bb886c528d5d](https://gemmaonline.nl/index.php/GEMMA/id-3d765f43-c4e8-4556-850b-bb886c528d5d) |
    | gemma_definitie | De versie-aanduiding van een object. |
    | gemma_toelichting |  |
    

Attributen van objecttype Versie

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| versienummer | AN8 |  |
| status | AN40 |  |
| datumEindeSupport | Date |  |
| licentie | AN40 |  |
| aantal | int |  |
| kosten | Bedrag |  |



### Vervoersmiddel
> **Definitie Vervoersmiddel:** 
>
> Een voertuig dat zich over het land verplaatst.

??? info "Kenmerken Model Vervoersmiddel"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Vervoersmiddel |
    | toelichting |  |
    | synoniemen | Voertuig |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.4 |
    | created | 2019-01-10 11:37:36 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_E8C75DAB_F9AE_4fe2_9114_870434F2EA80 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Vervoersmiddel |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-92104ecd-beda-441d-b5fd-b6d2296969d0](https://gemmaonline.nl/index.php/GEMMA/id-92104ecd-beda-441d-b5fd-b6d2296969d0) |
    | gemma_definitie | Een voertuig dat zich over het land verplaatst. |
    | gemma_toelichting |  |
    

Attributen van objecttype Vervoersmiddel

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Wijzigingsverzoek
> **Definitie Wijzigingsverzoek:** 
>
> Een aanvraag voor wijziging

??? info "Kenmerken Model Wijzigingsverzoek"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Wijzigingsverzoek |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.5 |
    | created | 2019-01-10 11:40:46 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_EFBF46D1_6A51_44fd_BAEA_47BCDFEEE27A |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Wijzigingsverzoek |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-3a602b01-9a08-4224-8caf-3cb58130fb30](https://gemmaonline.nl/index.php/GEMMA/id-3a602b01-9a08-4224-8caf-3cb58130fb30) |
    | gemma_definitie | Een aanvraag voor wijziging |
    | gemma_toelichting |  |
    

Attributen van objecttype Wijzigingsverzoek

| Attribute | Datatype | Description |
| :--- | :--- | :--- |






## Enumeraties Model ICT


### Applicatiecategorie
Geen Definitie

Het enumeratie Applicatiecategorie kent de volgende waarden:

* **Kernapplicatie**: <Geen Definities>
* **BBA**: <Geen Definities>
* **KA Extra**: <Geen Definities>
* **KA Basis**: <Geen Definities>
* **Beheer en systeem**: <Geen Definities>
* **Niet ingedeeld**: <Geen Definities>


De enumeratie Applicatiecategorie heeft de volgende kenmerken:

??? info "Kenmerken Model Applicatiecategorie"
    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | Applicatiecategorie |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author |  |
    | version | 1.4 |
    | created | 2025-03-26 11:13:13 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_A030D866_E2E7_4854_ACFD_C62DB3ABDA38 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    


### Beheerstatus
Geen Definitie

Het enumeratie Beheerstatus kent de volgende waarden:

* **Technisch ondersteunen**: <Geen Definities>
* **Volledig Beheer**: <Geen Definities>
* **Beschikbaar Stellen**: <Geen Definities>
* **Functioneel Ondersteunen**: <Geen Definities>
* **Intern Ontwikkeld**: <Geen Definities>
* **Niet ingedeeld**: <Geen Definities>


De enumeratie Beheerstatus heeft de volgende kenmerken:

??? info "Kenmerken Model Beheerstatus"
    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | Beheerstatus |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author |  |
    | version | 1.4 |
    | created | 2025-03-26 11:13:13 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_1FCBFA1B_2703_4ece_A496_EA668AEFCDCD |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    


### Gebruikerrol
Geen Definitie

Het enumeratie Gebruikerrol kent de volgende waarden:

* **Gebruiker**: <Geen Definities>
* **Eigenaar**: <Geen Definities>
* **Functioneel beheerder**: <Geen Definities>
* **Gegevensbeheerder**: <Geen Definities>
* **Superuser**: <Geen Definities>


De enumeratie Gebruikerrol heeft de volgende kenmerken:

??? info "Kenmerken Model Gebruikerrol"
    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | Gebruikerrol |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author |  |
    | version | 1.4 |
    | created | 2025-03-26 11:13:13 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_262A7A23_0CBB_4991_A1B2_D5D3E509549C |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    


### Packagingstatus
Geen Definitie

Het enumeratie Packagingstatus kent de volgende waarden:

* **Handmatig Installeren**: <Geen Definities>
* **Packagen en distribueren**: <Geen Definities>
* **Alleen Aanbieden**: <Geen Definities>
* **Niet aanbieden**: <Geen Definities>
* **API Mogelijk???**: <Geen Definities>
* **Niet ingedeeld**: <Geen Definities>


De enumeratie Packagingstatus heeft de volgende kenmerken:

??? info "Kenmerken Model Packagingstatus"
    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | Packagingstatus |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author |  |
    | version | 1.4 |
    | created | 2025-03-26 11:13:13 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_C0031024_173A_47d6_9BF4_F22941AA7807 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    


### Servertypes
Geen Definitie

Het enumeratie Servertypes kent de volgende waarden:

* **niet virtueel**: <Geen Definities>
* **virtueel**: <Geen Definities>


De enumeratie Servertypes heeft de volgende kenmerken:

??? info "Kenmerken Model Servertypes"
    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | Servertypes |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author |  |
    | version | 1.4 |
    | created | 2025-03-26 11:13:13 |
    | modified | 2025-03-26 16:14:46 |
    | id | EAID_BA2C3918_278E_49c7_A8C5_423F2D659450 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    



