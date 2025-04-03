# Model Jeugd en Wmo Generiek
## Inleiding
> **Definitie Model Jeugd en Wmo Generiek:** 
>
> Alle generieke objecttypen die zowel voor de Wmo als voor uitvoering van de jeugdwet worden gebruikt

Het model 'Model Jeugd en Wmo Generiek' kent de volgende objecttypen:

* **AOM_AanvraagWmoJeugd**: <Geen Definities>
* **AOMMeldingWMOJeugd**: <Geen Definities>
* **Beperking**: Een stoornis of conditie ï¿½ lichamelijk, zintuiglijk en-of geestelijk ï¿½ die een normaal maatschappelijk functioneren belemmert en nadelige sociale gevolgen met zich meebrengt.
* **Beperkingscategorie**: Een categorisering van beperkingen
* **Beperkingscore**: Getalsmatige duiding van een beperking
* **Beperkingscoresoort**: Typering van beperkingscores
* **Beschikking**: In het bestuursrecht: Een beslissing van een overheidsorgaan in een concreet geval, bijvoorbeeld het verlenen van een bouwvergunning. In het civiele recht: een rechterlijke uitspraak in een procedure die begint met een verzoekschrift.
* **Beschikkingsoort**: Typering van een beschikking
* **Beschikte Voorziening**: Een voorziening waarover een beschikking is gedaan.
* **Budgetuitputting**: Overzicht van de te verwachte inkomsten en uitgaven over een bepaalde periode
* **Declaratie**: Een opgave van te vergoeden kosten.
* **Declaratieregel**: <Geen Definities>
* **Leefgebied**: Gebied waarin alle activiteiten van een inwoner zich kunnen afspelen
* **Levering**: Levering van zorg door leverancier. Is in het geval van resultaatverplichting steeds: 1 stuk<br><br>In PxQ uren maal tarief
* **Leveringsvorm**: Zorg die onder de Wlz, de Zvw-Wijkverpleging of de Wmo 2015 valt, kan aan personen als zorg in natura (zin) worden geleverd of bekostigd worden uit een persoonsgebonden budget (pgb).
* **Melding Eigen bijdrage**: Aangifte van de evetuele eigen bijdrage
* **PGB-Toekenning**: Betreft alleen toegekende voorzieningen met als leveringsvorm PGB<br>Opgebouwd op basis van het TKB (Toekenninsgbericht) aan het SVB, en het BAB-bericht (budgetafsluiting). zie: https://istandaarden.nl/istandaarden/ipgb
* **Score**: Het aantal behaalde punten
* **Scoresoort**: Typologie van score
* **Tarief**: Hoogte van een bedrag voor een bepaald product of dient
* **Team**: Een groep personen die door middel van samenwerking een gezamenlijk doel nastreeft, waarbij de teamleden afhankelijk van elkaar zijn om het doel te bereiken.
* **Toewijzing**: Toewijzing die door gemeente aan zorgaanbieder wordt gestuurd. zie https://informatiemodel.istandaarden.nl/2019/views/view_274300.html
* **Verplichting WMO Jeugd**: <Geen Definities>
* **Verzoek om Toewijzing**: Verzoek tot toewijzing dat vanuit leverancier (via H10-portal) aan de gemeente wordt gestuurd. Zie https://informatiemodel.istandaarden.nl/2019/views/view_274300.html
* **Voorziening**: Middel om services/maatregelen in te vullen.
* **Voorzieningsoort**: Typering van een voorziening
* **Zelfredzaamheidmatrix**: Een geordend systeem waarbij aan elf domeinen van het dagelijks leven (zoals inkomen en dagbesteding; zie figuur) een waarde voor zelfredzaamheid wordt toegekend.


Het model 'Model Jeugd en Wmo Generiek' heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | Model Jeugd en Wmo Generiek |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.5 |
| created | 2018-05-15 16:29:14 |
| modified | 2025-03-27 15:28:35 |
| id | EAPK_B3B8C80B_FA8A_4058_8731_00B21A9EFE76 |


## Objecttypen Model Jeugd en Wmo Generiek


### AOM_AanvraagWmoJeugd
> **Definitie AOM_AanvraagWmoJeugd:** 
>
> Geen Definitie

| Eigenschap | Waarde |
| :--- | :------ |
| name | AOM_AanvraagWmoJeugd |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | aashkpour |
| version | 1.3 |
| created | 2021-12-15 14:49:37 |
| modified | 2025-03-26 16:14:36 |
| id | EAID_BE7C28C6_0922_4c6a_A953_3D598D991AB5 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | AOMAanvraagWMOJeugd |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-3545eb93-e19a-4b1f-b3f2-03b79b30b200](https://gemmaonline.nl/index.php/GEMMA/id-3545eb93-e19a-4b1f-b3f2-03b79b30b200) |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype AOM_AanvraagWmoJeugd

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| clientReactie | AN100 |  |
| datumBeschikking | Date |  |
| datumEersteAfspraak | Date | De datum van de eerste afspraak in het<br>proces. |
| datumPlanVastgesteld | Date | De datum waarop het plan is vastgesteld in de melding. |
| datumStartAanvraag | Date | Start van het proces=start vd aanvraag |
| datumEinde | Date | De daadwerkelijke einddatum van de<br>gekozen doorlooptijd. Dit is datum plan, datum beschikking, datum afsluiten proces of niet van toepassing. Deze einddatum is afhankelijk van de gekozen doorloopmethodiek |
| deskundigheid | AN50 |  |
| doorloopmethodiek | AN50 |  |
| maximaleDoorlooptijd | AN20 | Het aantal dagen tussen de startdatum en de einddatum van de doorloopmethodiek ten tijde van het aanmaken van het proces. Dit veld geeft daarmee aan hoe lang men over een proces zou mogen doen. |
| redenAfsluiting | AN50 |  |



### AOMMeldingWMOJeugd
> **Definitie AOMMeldingWMOJeugd:** 
>
> Geen Definitie

| Eigenschap | Waarde |
| :--- | :------ |
| name | AOMMeldingWMOJeugd |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | aashkpour |
| version | 1.3 |
| created | 2021-12-15 14:38:21 |
| modified | 2025-03-26 16:14:36 |
| id | EAID_0FA25A4F_DF7F_4feb_9460_19D054E874F8 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype AOMMeldingWMOJeugd

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| aanmelder | AN100 |  |
| aanmeldingDoor | AN100 |  |
| aanmeldingDoorLandelijk | AN100 |  |
| aanmeldwijze | AN80 |  |
| redenAfsluiting | AN80 |  |
| isClientOpDeHoogte | AN50 |  |
| deskundigheid | AN80 |  |
| vervolg | AN50 |  |
| onderzoekswijze | AN50 |  |
| verwezen | AN50 |  |



### Beperking
> **Definitie Beperking:** 
>
> Een stoornis of conditie ï¿½ lichamelijk, zintuiglijk en-of geestelijk ï¿½ die een normaal maatschappelijk functioneren belemmert en nadelige sociale gevolgen met zich meebrengt.

| Eigenschap | Waarde |
| :--- | :------ |
| name | Beperking |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.5 |
| created | 2018-03-21 15:32:51 |
| modified | 2025-03-26 16:14:36 |
| id | EAID_F110608E_9C6A_4d66_BDCB_F4B2465E3CFD |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Beperking |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-b883410b-ba90-45a0-a9f0-f16b8e1fa9ac](https://gemmaonline.nl/index.php/GEMMA/id-b883410b-ba90-45a0-a9f0-f16b8e1fa9ac) |
| gemma_definitie | Een stoornis of conditie ï¿½ lichamelijk, zintuiglijk en-of geestelijk ï¿½ die een normaal maatschappelijk functioneren belemmert en nadelige sociale gevolgen met zich meebrengt. |
| gemma_toelichting |  |


Attributen van objecttype Beperking

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| duur | int |  |
| categorie | int |  |
| commentaar | int |  |
| wet | Enumeratie: "Wet" |  |



### Beperkingscategorie
> **Definitie Beperkingscategorie:** 
>
> Een categorisering van beperkingen

| Eigenschap | Waarde |
| :--- | :------ |
| name | Beperkingscategorie |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | crossover |
| version | 1.5 |
| created | 2018-04-23 14:41:29 |
| modified | 2025-03-26 16:14:36 |
| id | EAID_4E835898_6623_457f_99B4_C688D465F720 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Beperkingscategorie

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| code | AN8 |  |
| wet | Enumeratie: "Wet" |  |



### Beperkingscore
> **Definitie Beperkingscore:** 
>
> Getalsmatige duiding van een beperking

| Eigenschap | Waarde |
| :--- | :------ |
| name | Beperkingscore |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.5 |
| created | 2018-03-21 15:33:15 |
| modified | 2025-03-26 16:14:36 |
| id | EAID_5EDE0349_8865_4b90_9A18_235C5AA660C4 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Beperkingscore |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-8d15d21d-4e39-4dcb-b9f7-be128f6b324a](https://gemmaonline.nl/index.php/GEMMA/id-8d15d21d-4e39-4dcb-b9f7-be128f6b324a) |
| gemma_definitie | Getalsmatige duiding van een beperking |
| gemma_toelichting |  |


Attributen van objecttype Beperkingscore

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| score | int |  |
| commentaar | AN200 |  |
| wet | Enumeratie: "Wet" |  |



### Beperkingscoresoort
> **Definitie Beperkingscoresoort:** 
>
> Typering van beperkingscores

| Eigenschap | Waarde |
| :--- | :------ |
| name | Beperkingscoresoort |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | crossover |
| version | 1.5 |
| created | 2018-04-23 14:41:43 |
| modified | 2025-03-26 16:14:36 |
| id | EAID_6B63630A_8A30_454d_B8C4_252D4C30A3BF |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Beperkingscoresoort

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| vraag | AN200 |  |
| wet | Enumeratie: "Wet" |  |



### Beschikking
> **Definitie Beschikking:** 
>
> In het bestuursrecht: Een beslissing van een overheidsorgaan in een concreet geval, bijvoorbeeld het verlenen van een bouwvergunning. In het civiele recht: een rechterlijke uitspraak in een procedure die begint met een verzoekschrift.

| Eigenschap | Waarde |
| :--- | :------ |
| name | Beschikking |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.5 |
| created | 2018-04-23 16:56:03 |
| modified | 2025-03-26 16:14:36 |
| id | EAID_71D7E96D_641A_4b6a_A325_DED07C3B5836 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Beschikking |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-c481e8b8-f7d7-4979-b767-ebf2a9b04712](https://gemmaonline.nl/index.php/GEMMA/id-c481e8b8-f7d7-4979-b767-ebf2a9b04712) |
| gemma_definitie | In het bestuursrecht: Een beslissing van een overheidsorgaan in een concreet geval, bijvoorbeeld het verlenen van een bouwvergunning. In het civiele recht: een rechterlijke uitspraak in een procedure die begint met een verzoekschrift. |
| gemma_toelichting |  |


Attributen van objecttype Beschikking

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| datumAfgifte | Datum |  |
| code | AN20 |  |
| grondslagen | int |  |
| commentaar | AN200 |  |
| wet |  |  |



### Beschikkingsoort
> **Definitie Beschikkingsoort:** 
>
> Typering van een beschikking

| Eigenschap | Waarde |
| :--- | :------ |
| name | Beschikkingsoort |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.5 |
| created | 2018-06-13 14:01:26 |
| modified | 2025-03-26 16:14:36 |
| id | EAID_FD14E04F_26A1_42ba_8E47_5F43AF539877 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Beschikkingsoort

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Beschikte Voorziening
> **Definitie Beschikte Voorziening:** 
>
> Een voorziening waarover een beschikking is gedaan.

| Eigenschap | Waarde |
| :--- | :------ |
| name | Beschikte Voorziening |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.5 |
| created | 2018-06-13 13:58:33 |
| modified | 2025-03-26 16:14:36 |
| id | EAID_975C3DA3_930A_49d8_B54F_2A560DC2AD5A |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | BeschikteVoorziening |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-38610e76-2c3e-429a-b30b-1fd21f05c8fc](https://gemmaonline.nl/index.php/GEMMA/id-38610e76-2c3e-429a-b30b-1fd21f05c8fc) |
| gemma_definitie | Een voorziening waarover een beschikking is gedaan. |
| gemma_toelichting |  |


Attributen van objecttype Beschikte Voorziening

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| omvang | int |  |
| eenheid | Enumeratie: "Eenheid" |  |
| frequentie | Enumeratie: "Frequentie" |  |
| wet | Enumeratie: "Wet" |  |
| code | AN20 |  |
| datumStart | Date |  |
| datumEinde | Date |  |
| leveringsvorm | Enumeratie: "Leveringsvorm" |  |
| status | AN50 |  |
| redenEinde | AN100 |  |
| datumEindeOorspronkelijk | Date |  |



### Budgetuitputting
> **Definitie Budgetuitputting:** 
>
> Overzicht van de te verwachte inkomsten en uitgaven over een bepaalde periode

| Eigenschap | Waarde |
| :--- | :------ |
| name | Budgetuitputting |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.5 |
| created | 2019-09-09 13:49:43 |
| modified | 2025-03-26 16:14:36 |
| id | EAID_679162ED_0B45_4fb2_B16E_421C25A107F5 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Budgetuitputting

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| datum | Date |  |
| uitgenutBedrag | Bedrag |  |



### Declaratie
> **Definitie Declaratie:** 
>
> Een opgave van te vergoeden kosten.

| Eigenschap | Waarde |
| :--- | :------ |
| name | Declaratie |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | aashkpour |
| version | 1.5 |
| created | 2021-11-15 14:24:21 |
| modified | 2025-03-26 16:14:36 |
| id | EAID_5E542F35_E413_49c4_8FB7_335B6BE9667A |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Declaratie |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-645ed017-feb5-40b0-82ae-990745bdb549](https://gemmaonline.nl/index.php/GEMMA/id-645ed017-feb5-40b0-82ae-990745bdb549) |
| gemma_definitie | Een opgave van te vergoeden kosten. |
| gemma_toelichting |  |


Attributen van objecttype Declaratie

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| declaratieBedrag | int |  |
| datumDeclaratie | int |  |
| declaratieStatus | int |  |



### Declaratieregel
> **Definitie Declaratieregel:** 
>
> Geen Definitie

| Eigenschap | Waarde |
| :--- | :------ |
| name | Declaratieregel |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.3 |
| created | 2018-06-12 15:34:16 |
| modified | 2025-03-26 16:14:36 |
| id | EAID_F73F6BFE_9CFE_4497_80E3_CADAA344CF69 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Declaratieregel

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| code | AN20 |  |
| bedrag | Bedrag |  |
| datumStart | Date |  |
| datumEinde | Date |  |



### Leefgebied
> **Definitie Leefgebied:** 
>
> Gebied waarin alle activiteiten van een inwoner zich kunnen afspelen

| Eigenschap | Waarde |
| :--- | :------ |
| name | Leefgebied |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.5 |
| created | 2018-05-23 15:34:35 |
| modified | 2025-03-26 16:14:36 |
| id | EAID_C55180D9_A5C3_4859_BD88_7686F5384157 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Leefgebied |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-c80348b6-b173-41ab-9bf6-3a1a780d0fb3](https://gemmaonline.nl/index.php/GEMMA/id-c80348b6-b173-41ab-9bf6-3a1a780d0fb3) |
| gemma_definitie | Gebied waarin alle activiteiten van een inwoner zich kunnen afspelen |
| gemma_toelichting |  |


Attributen van objecttype Leefgebied

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| naam | AN80 |  |



### Levering
> **Definitie Levering:** 
>
> Levering van zorg door leverancier. Is in het geval van resultaatverplichting steeds: 1 stuk<br><br>In PxQ uren maal tarief

| Eigenschap | Waarde |
| :--- | :------ |
| name | Levering |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | crossover |
| version | 1.5 |
| created | 2018-04-23 14:46:17 |
| modified | 2025-03-26 16:14:36 |
| id | EAID_F0CE97B6_3004_4424_A0AA_5034BC0144D1 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Levering |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-cc667191-bb35-45a0-a231-504b663b70f1](https://gemmaonline.nl/index.php/GEMMA/id-cc667191-bb35-45a0-a231-504b663b70f1) |
| gemma_definitie | Levering van zorg door leverancier. Is in het geval van resultaatverplichting steeds: 1 stuk<br><br>In PxQ uren maal tarief |
| gemma_toelichting |  |


Attributen van objecttype Levering

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| eenheid | Enumeratie: "Eenheid" |  |
| frequentie | Enumeratie: "Frequentie" |  |
| omvang | int |  |
| code | AN20 |  |
| datumStart | Date |  |
| datumStop | Date |  |
| stopreden | Text |  |



### Leveringsvorm
> **Definitie Leveringsvorm:** 
>
> Zorg die onder de Wlz, de Zvw-Wijkverpleging of de Wmo 2015 valt, kan aan personen als zorg in natura (zin) worden geleverd of bekostigd worden uit een persoonsgebonden budget (pgb).

| Eigenschap | Waarde |
| :--- | :------ |
| name | Leveringsvorm |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | crossover |
| version | 1.5 |
| created | 2018-04-23 16:43:06 |
| modified | 2025-03-26 16:14:36 |
| id | EAID_F35DA519_FA0C_48ae_9EFC_C4EBEC4BF144 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Leveringsvorm

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| naam | AN3 |  |
| wet | Enumeratie: "Wet" |  |
| leveringsvormCode | An20 |  |



### Melding Eigen bijdrage
> **Definitie Melding Eigen bijdrage:** 
>
> Aangifte van de evetuele eigen bijdrage

| Eigenschap | Waarde |
| :--- | :------ |
| name | Melding Eigen bijdrage |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.5 |
| created | 2019-09-09 13:33:02 |
| modified | 2025-03-26 16:14:36 |
| id | EAID_A9D093FB_B3D1_46e5_B263_6C4D61F0C5D1 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | MeldingEigenBijdrage |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-57035c38-5be2-432e-88aa-ba59029c984c](https://gemmaonline.nl/index.php/GEMMA/id-57035c38-5be2-432e-88aa-ba59029c984c) |
| gemma_definitie | Aangifte van de evetuele eigen bijdrage |
| gemma_toelichting |  |


Attributen van objecttype Melding Eigen bijdrage

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| datumStart | Date |  |
| datumStop | Date |  |



### PGB-Toekenning
> **Definitie PGB-Toekenning:** 
>
> Betreft alleen toegekende voorzieningen met als leveringsvorm PGB<br>Opgebouwd op basis van het TKB (Toekenninsgbericht) aan het SVB, en het BAB-bericht (budgetafsluiting). zie: https://istandaarden.nl/istandaarden/ipgb

| Eigenschap | Waarde |
| :--- | :------ |
| name | PGB-Toekenning |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.5 |
| created | 2019-09-09 13:42:53 |
| modified | 2025-03-26 16:14:36 |
| id | EAID_84FE9B56_158D_4b65_BCC1_5FE29D071FCC |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | PGBToekenning |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-2cc8ad38-97f9-4462-83af-cb5556bffd88](https://gemmaonline.nl/index.php/GEMMA/id-2cc8ad38-97f9-4462-83af-cb5556bffd88) |
| gemma_definitie | Betreft alleen toegekende voorzieningen met als leveringsvorm PGB<br>Opgebouwd op basis van het TKB (Toekenninsgbericht) aan het SVB, en het BAB-bericht (budgetafsluiting). zie: https://istandaarden.nl/istandaarden/ipgb |
| gemma_toelichting |  |


Attributen van objecttype PGB-Toekenning

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| datumToekenning | Date |  |
| budget | Bedrag |  |
| datumEinde | Date |  |



### Score
> **Definitie Score:** 
>
> Het aantal behaalde punten

| Eigenschap | Waarde |
| :--- | :------ |
| name | Score |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.5 |
| created | 2018-05-23 15:40:08 |
| modified | 2025-03-26 16:14:36 |
| id | EAID_5A367DA9_DE05_4b3b_954D_24271FD4FB76 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Score |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-75a56fd7-b2b2-4a08-9b09-8235d4592cae](https://gemmaonline.nl/index.php/GEMMA/id-75a56fd7-b2b2-4a08-9b09-8235d4592cae) |
| gemma_definitie | Het aantal behaalde punten |
| gemma_toelichting |  |


Attributen van objecttype Score

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| datum | date |  |



### Scoresoort
> **Definitie Scoresoort:** 
>
> Typologie van score

| Eigenschap | Waarde |
| :--- | :------ |
| name | Scoresoort |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.5 |
| created | 2018-05-23 15:34:03 |
| modified | 2025-03-26 16:14:36 |
| id | EAID_653EA248_1547_4f8b_B026_B44FEEC711B2 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Scoresoort

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| niveau | N1 |  |



### Tarief
> **Definitie Tarief:** 
>
> Hoogte van een bedrag voor een bepaald product of dient

| Eigenschap | Waarde |
| :--- | :------ |
| name | Tarief |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.5 |
| created | 2018-06-13 14:26:29 |
| modified | 2025-03-26 16:14:36 |
| id | EAID_57F01465_EE56_4c33_9BD9_8DB351A2C530 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Tarief |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-a842e972-764b-4dd8-ad79-f537d4e68565](https://gemmaonline.nl/index.php/GEMMA/id-a842e972-764b-4dd8-ad79-f537d4e68565) |
| gemma_definitie | Hoogte van een bedrag voor een bepaald product of dient |
| gemma_toelichting |  |


Attributen van objecttype Tarief

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| datumStart | Date |  |
| datumEinde | Date |  |
| bedrag | Bedrag |  |
| wet | Enumeratie: "Wet" |  |
| eenheid | Enumeratie: "Eenheid" |  |



### Team
> **Definitie Team:** 
>
> Een groep personen die door middel van samenwerking een gezamenlijk doel nastreeft, waarbij de teamleden afhankelijk van elkaar zijn om het doel te bereiken.

| Eigenschap | Waarde |
| :--- | :------ |
| name | Team |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.5 |
| created | 2018-06-13 11:54:40 |
| modified | 2025-03-26 16:14:36 |
| id | EAID_909A4134_4697_481e_9110_6386D0F6CAAD |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Team |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-016ea33a-4ba2-45d7-ae45-616eeedcc567](https://gemmaonline.nl/index.php/GEMMA/id-016ea33a-4ba2-45d7-ae45-616eeedcc567) |
| gemma_definitie | Een groep personen die door middel van samenwerking een gezamenlijk doel nastreeft, waarbij de teamleden afhankelijk van elkaar zijn om het doel te bereiken. |
| gemma_toelichting |  |


Attributen van objecttype Team

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| naam | AN80 |  |
| omschrijving | text |  |



### Toewijzing
> **Definitie Toewijzing:** 
>
> Toewijzing die door gemeente aan zorgaanbieder wordt gestuurd. zie https://informatiemodel.istandaarden.nl/2019/views/view_274300.html

| Eigenschap | Waarde |
| :--- | :------ |
| name | Toewijzing |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.5 |
| created | 2018-04-23 16:56:03 |
| modified | 2025-03-26 16:14:36 |
| id | EAID_01ECE551_A7B0_4b99_B6E7_F654D6AC15D5 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Toewijzing |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-53cc8281-81c1-40c8-901d-2751e34ea367](https://gemmaonline.nl/index.php/GEMMA/id-53cc8281-81c1-40c8-901d-2751e34ea367) |
| gemma_definitie | Toewijzing die door gemeente aan zorgaanbieder wordt gestuurd. zie https://informatiemodel.istandaarden.nl/2019/views/view_274300.html |
| gemma_toelichting |  |


Attributen van objecttype Toewijzing

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| toewijzingnummer | N9 |  |
| datumToewijzing | Date |  |
| datumStartToewijzing | Date |  |
| datumEindeToewijzing | Date |  |
| redenWijziging | int |  |
| omvang | N8 |  |
| commentaar | Text |  |
| eenheid | Enumeratie: "Eenheid" |  |
| frequentie | Enumeratie: "Frequentie" |  |
| datumAanschaf | Date |  |
| code | AN20 |  |
| wet | Enumeratie: "Wet" |  |



### Verplichting WMO Jeugd
> **Definitie Verplichting WMO Jeugd:** 
>
> Geen Definitie

| Eigenschap | Waarde |
| :--- | :------ |
| name | Verplichting WMO Jeugd |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | aashkpour |
| version | 1.3 |
| created | 2023-07-27 15:34:06 |
| modified | 2025-03-26 16:14:36 |
| id | EAID_EC0FB9CB_B407_49b4_8FCF_8837E7A72DA9 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Verplichting WMO Jeugd |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-7c5fd54e-88dd-4738-95ec-5164d6c6af35](https://gemmaonline.nl/index.php/GEMMA/id-7c5fd54e-88dd-4738-95ec-5164d6c6af35) |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Verplichting WMO Jeugd

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| budgetsoortgroep | int |  |
| Budgetsoort | int |  |
| Feitelijke Einddatum | int |  |
| verplichtingsoort | int |  |
| Periodiciteit | int |  |
| Einddatumgepland | int |  |
| Jaar | int |  |



### Verzoek om Toewijzing
> **Definitie Verzoek om Toewijzing:** 
>
> Verzoek tot toewijzing dat vanuit leverancier (via H10-portal) aan de gemeente wordt gestuurd. Zie https://informatiemodel.istandaarden.nl/2019/views/view_274300.html

| Eigenschap | Waarde |
| :--- | :------ |
| name | Verzoek om Toewijzing |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.5 |
| created | 2019-09-09 11:59:36 |
| modified | 2025-03-26 16:14:37 |
| id | EAID_9F392B0B_1654_4b4e_9261_F0A90DA1F7BD |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | VerzoekOmToewijzing |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-e643dc04-a205-421d-ab23-c6da046b1642](https://gemmaonline.nl/index.php/GEMMA/id-e643dc04-a205-421d-ab23-c6da046b1642) |
| gemma_definitie | Verzoek tot toewijzing dat vanuit leverancier (via H10-portal) aan de gemeente wordt gestuurd. Zie https://informatiemodel.istandaarden.nl/2019/views/view_274300.html |
| gemma_toelichting |  |


Attributen van objecttype Verzoek om Toewijzing

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| referentieAanbieder | AN40 |  |
| beschikkingsnummer | AN40 |  |
| datumIngangBeschikking | Date |  |
| datumIngangToewijzing | Date |  |
| datumEindeToewijzing | Date |  |
| volume | int |  |
| eenheid | Enumeratie: "Eenheid" |  |
| frequentie | Enumeratie: "Frequentie" |  |
| verwijzer | AN200 |  |
| raamcontract | boolean |  |
| commentaar | text |  |
| datumOntvangst | Date |  |
| soortVerwijzer | Enumeratie: "Soort Verwijzer" |  |



### Voorziening
> **Definitie Voorziening:** 
>
> Middel om services/maatregelen in te vullen.

| Eigenschap | Waarde |
| :--- | :------ |
| name | Voorziening |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.5 |
| created | 2018-04-23 16:56:03 |
| modified | 2025-03-26 16:14:37 |
| id | EAID_EAAF2F59_6BC0_4243_B126_A8E604B32C5E |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Voorziening |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-8ffe8caf-2af7-47e5-acc5-c4e6fd5f38b1](https://gemmaonline.nl/index.php/GEMMA/id-8ffe8caf-2af7-47e5-acc5-c4e6fd5f38b1) |
| gemma_definitie | Middel om services/maatregelen in te vullen. |
| gemma_toelichting |  |


Attributen van objecttype Voorziening

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| productcode | AN5 |  |
| naam | AN80 |  |
| omschrijving | text |  |
| wet | Enumeratie: "Wet" |  |
| code | AN20 |  |
| afhandelwijze | AN200 |  |



### Voorzieningsoort
> **Definitie Voorzieningsoort:** 
>
> Typering van een voorziening

| Eigenschap | Waarde |
| :--- | :------ |
| name | Voorzieningsoort |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.5 |
| created | 2018-06-13 14:31:08 |
| modified | 2025-03-26 16:14:37 |
| id | EAID_462E3982_56C3_4442_BE2F_2C23A7ED6015 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Voorzieningsoort

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| naam | AN80 |  |
| omschrijving | text |  |
| wet | Enumeratie: "Wet" |  |
| code | An20 |  |
| productcode | AN20 |  |
| productcategoriecode | An20 |  |
| productcategorie | AN200 |  |



### Zelfredzaamheidmatrix
> **Definitie Zelfredzaamheidmatrix:** 
>
> Een geordend systeem waarbij aan elf domeinen van het dagelijks leven (zoals inkomen en dagbesteding; zie figuur) een waarde voor zelfredzaamheid wordt toegekend.

| Eigenschap | Waarde |
| :--- | :------ |
| name | Zelfredzaamheidmatrix |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.5 |
| created | 2018-05-23 15:20:43 |
| modified | 2025-03-26 16:14:37 |
| id | EAID_6C27D3D1_FBCE_4504_AF1E_48B4A4CB02EA |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | ZelfredzaamheidMatrix |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-4f3a28d3-464a-42c3-97e1-39231e5f7bf1](https://gemmaonline.nl/index.php/GEMMA/id-4f3a28d3-464a-42c3-97e1-39231e5f7bf1) |
| gemma_definitie | Een geordend systeem waarbij aan elf domeinen van het dagelijks leven (zoals inkomen en dagbesteding; zie figuur) een waarde voor zelfredzaamheid wordt toegekend. |
| gemma_toelichting |  |


Attributen van objecttype Zelfredzaamheidmatrix

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| naam | AN80 |  |
| omschrijving | text |  |
| datumStartGeldigheid | date |  |
| datumEindeGeldigheid | date |  |






## Enumeraties Model Jeugd en Wmo Generiek


### Doelgroep
Geen Definitie

Het enumeratie Doelgroep kent de volgende waarden:

* **Asielstatushouder**: <Geen Definities>
* **Gezinsvormer**: <Geen Definities>
* **Gezinshereniger**: <Geen Definities>
* **Geestelijk bedienaar**: <Geen Definities>
* **Gezinsvormer met Asielstatushouder**: <Geen Definities>
* **Gezinshereniger met Asielstatushouder**: <Geen Definities>
* **Overig**: <Geen Definities>


De enumeratie Doelgroep heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | Doelgroep |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author |  |
| version | 1.4 |
| created | 2025-03-26 11:12:49 |
| modified | 2025-03-26 16:14:37 |
| id | EAID_A9985186_A6B8_4414_8334_A2CA12D5AC94 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |



### Eenheid
Geen Definitie

Het enumeratie Eenheid kent de volgende waarden:

* **Minuut**: <Geen Definities>
* **Uur**: <Geen Definities>
* **Etmaal**: <Geen Definities>
* **Dagdeel (4 uur)**: <Geen Definities>
* **Stuks**: <Geen Definities>
* **Euros**: <Geen Definities>
* **Onbekend**: <Geen Definities>
* **Leeg**: <Geen Definities>


De enumeratie Eenheid heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | Eenheid |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author |  |
| version | 1.4 |
| created | 2025-03-26 11:12:49 |
| modified | 2025-03-26 16:14:37 |
| id | EAID_838B4669_4F50_4835_ABA8_03E3FCE48184 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |



### Frequentie
Geen Definitie

Het enumeratie Frequentie kent de volgende waarden:

* **Per dag**: <Geen Definities>
* **Per week**: <Geen Definities>
* **Per 4 weken**: <Geen Definities>
* **Per maand**: <Geen Definities>
* **Per jaar**: <Geen Definities>
* **Binnen geldigheid Beschikking**: Frequentie bij beschikking conform iWmo 2.0 zie https://www.istandaarden.nl/ibieb/functionele-uitwerking-release-iwmo-20
* **Leeg**: <Geen Definities>
* **Onbekend**: <Geen Definities>


De enumeratie Frequentie heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | Frequentie |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author |  |
| version | 1.4 |
| created | 2025-03-26 11:12:49 |
| modified | 2025-03-26 16:14:37 |
| id | EAID_8640ED99_341B_4f10_A335_9324459F19B3 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |



### Leveringsvorm
Geen Definitie

Het enumeratie Leveringsvorm kent de volgende waarden:

* **ZIN**: <Geen Definities>
* **PGB**: <Geen Definities>
* **Onbekend**: <Geen Definities>
* **Leeg**: <Geen Definities>


De enumeratie Leveringsvorm heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | Leveringsvorm |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author |  |
| version | 1.4 |
| created | 2025-03-26 11:12:49 |
| modified | 2025-03-26 16:14:37 |
| id | EAID_DC1D1F90_E28B_4fb7_A5E1_C2F76132BE12 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |



### Soort Verwijzer
Geen Definitie

Het enumeratie Soort Verwijzer kent de volgende waarden:

* **Gemeente**: <Geen Definities>
* **Huisarts**: <Geen Definities>
* **Jeugdarts**: <Geen Definities>
* **Gecertificeerde instelling**: <Geen Definities>
* **Medisch specialist**: <Geen Definities>
* **Zelfverwijzer / geen verwijzer**: <Geen Definities>
* **Rechter, Officier van Justitie, functionaris Justitiï¿½le jeugdinrichting**: <Geen Definities>
* **Leeg**: <Geen Definities>
* **Onbekend**: <Geen Definities>


De enumeratie Soort Verwijzer heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | Soort Verwijzer |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author |  |
| version | 1.4 |
| created | 2025-03-26 11:12:49 |
| modified | 2025-03-26 16:14:37 |
| id | EAID_44194E25_4676_4eb2_9E97_F44196438F4B |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |



### Wet
Geen Definitie

Het enumeratie Wet kent de volgende waarden:

* **Niet van toepassing**: <Geen Definities>
* **Wmo**: <Geen Definities>
* **Jeugdwet**: dere
* **Andere wet**: <Geen Definities>
* **Leeg**: <Geen Definities>
* **Onbekend**: <Geen Definities>
* **Participatiewet PW-I**: <Geen Definities>
* **I.O.A.W./I.O.A.Z.**: <Geen Definities>
* **Bijzondere Bijstand**: <Geen Definities>


De enumeratie Wet heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | Wet |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author |  |
| version | 1.4 |
| created | 2025-03-26 11:12:49 |
| modified | 2025-03-26 16:14:37 |
| id | EAID_3CDE785E_E631_4f94_A1A3_67F721140B1C |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |




