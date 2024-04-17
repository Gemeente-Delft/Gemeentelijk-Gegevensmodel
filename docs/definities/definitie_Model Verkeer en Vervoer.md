# Model Verkeer en Vervoer
## Inleiding
> **Definitie Model Verkeer en Vervoer:** 
>
> Geen definitie

Het model 'Model Verkeer en Vervoer' kent de volgende objecttypen:

* **Stremming**: Situatie waarbij de doorstroming van het (vaar)wegverkeer plaatselijk is geblokkeerd als gevolg van een incident
* **Strooidag**: Dag waarop op wegen gestrooid wordt ter voorkoming van gladheid
* **Strooiroute**: Traject waarop het strooien plaatsvindt
* **StrooirouteUitvoering**: De route die uiteindelijk is gevolgd voor het strooien 
* **Verkeersbesluit**: Een besluit van een wegbeheerder om een bepaald verkeersteken te plaatsen, te wijzigen of in te trekken of een bepaalde fysieke maatregel te treffen. 
* **Verkeerstelling**: Een onderzoek om inzicht te krijgen in het verkeer, in de hoeveelheid verkeer, de verdeling en de gereden snelheid.
* **VLogInfo**: V-log is een open standaard voor datalogging van een verkeersregelinstallatie.


Het model 'Model Verkeer en Vervoer' heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | Model Verkeer en Vervoer |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2018-03-21 11:47:02 |
| modified | 2019-02-13 13:34:21 |
| id | EAPK_13DD932C_4F69_4c62_B2D5_6676B5E5E24A |


## Objecttypen Model Verkeer en Vervoer


### Stremming
> **Definitie Stremming:** 
>
> Situatie waarbij de doorstroming van het (vaar)wegverkeer plaatselijk is geblokkeerd als gevolg van een incident

| Eigenschap | Waarde |
| :--- | :------ |
| name | Stremming |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2018-11-12 14:25:17 |
| modified | 2024-04-17 13:34:25 |
| id | EAID_999725EE_737F_410e_906B_9865EBED3597 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Stremming |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA2/0.9/id-563fd27c-7299-4311-8f40-60a95b9da4b5](https://gemmaonline.nl/index.php/GEMMA2/0.9/id-563fd27c-7299-4311-8f40-60a95b9da4b5) |
| gemma_definitie | Situatie waarbij de doorstroming van het (vaar)wegverkeer plaatselijk is geblokkeerd als gevolg van een incident |
| gemma_toelichting |  |


Attributen van objecttype Stremming

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| aantalGehinderden | Enumeratie: "Aantal Gehinderden" |  |
| datumAanmelding | DateTime |  |
| datumEinde | DateTime |  |
| datumStart | DateTime |  |
| datumWijziging | DateTime |  |
| delenToegestaan | boolean |  |
| geschiktVoorPublicatie | boolean |  |
| hinderklasse | Enumeratie: "Hinderklasse" |  |
| locatie | Point |  |
| naam | AN250 |  |
| status | Enumeratie: "Stremmingstatus" |  |




### Strooidag
> **Definitie Strooidag:** 
>
> Dag waarop op wegen gestrooid wordt ter voorkoming van gladheid

| Eigenschap | Waarde |
| :--- | :------ |
| name | Strooidag |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2018-11-21 10:32:27 |
| modified | 2024-04-17 13:34:25 |
| id | EAID_E2448A6D_3AE0_4884_AD5C_215A9E7166DE |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Strooidag

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| datum | Date |  |
| maximumtemperatuur | double |  |
| minimumtemperatuur | double |  |
| tijdMaximumtemperatuur | Time |  |
| tijdMinimumtemperatuur | Time |  |




### Strooiroute
> **Definitie Strooiroute:** 
>
> Traject waarop het strooien plaatsvindt

| Eigenschap | Waarde |
| :--- | :------ |
| name | Strooiroute |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2018-11-21 10:31:32 |
| modified | 2024-04-17 13:34:25 |
| id | EAID_73090FF8_12FD_471e_80FD_DBFB2FF97D7B |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Strooiroute |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA2/0.9/id-8d6c2c57-1e18-4257-a894-5f5d751279ea](https://gemmaonline.nl/index.php/GEMMA2/0.9/id-8d6c2c57-1e18-4257-a894-5f5d751279ea) |
| gemma_definitie | Traject waarop het strooien plaatsvindt |
| gemma_toelichting |  |


Attributen van objecttype Strooiroute

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| route | MultiCurve |  |




### StrooirouteUitvoering
> **Definitie StrooirouteUitvoering:** 
>
> De route die uiteindelijk is gevolgd voor het strooien 

| Eigenschap | Waarde |
| :--- | :------ |
| name | StrooirouteUitvoering |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2018-11-21 10:32:13 |
| modified | 2024-04-17 13:34:25 |
| id | EAID_B825D33A_6DCE_4263_A031_E6E92C4EE86B |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype StrooirouteUitvoering

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| geplandEinde | DateTime |  |
| geplandStart | DateTime |  |
| route | MultiCurve |  |
| werkelijkEinde | DateTime |  |
| werkelijkeStart | DateTime |  |
| None | Class: "Strooiroute" |  |
| None | Class: "Strooidag" |  |




### Verkeersbesluit
> **Definitie Verkeersbesluit:** 
>
> Een besluit van een wegbeheerder om een bepaald verkeersteken te plaatsen, te wijzigen of in te trekken of een bepaalde fysieke maatregel te treffen. 

| Eigenschap | Waarde |
| :--- | :------ |
| name | Verkeersbesluit |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2019-03-06 14:05:18 |
| modified | 2024-04-17 13:34:25 |
| id | EAID_3F83DAA3_C37F_42b2_8D35_D75B840172F8 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Verkeersbesluit |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA2/0.9/id-833312cc-f7d8-4b4c-9e79-b21c8e7597cb](https://gemmaonline.nl/index.php/GEMMA2/0.9/id-833312cc-f7d8-4b4c-9e79-b21c8e7597cb) |
| gemma_definitie | Een besluit van een wegbeheerder om een bepaald verkeersteken te plaatsen, te wijzigen of in te trekken of een bepaalde fysieke maatregel te treffen. |
| gemma_toelichting |  |


Attributen van objecttype Verkeersbesluit

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| datumBesluit | Date |  |
| datumEinde | Datetime |  |
| datumStart | Datetime |  |
| huisnummer | AN40 |  |
| postcode | AN6 |  |
| referentienummer | AN80 |  |
| straat | An200 |  |
| titel | AN250 |  |
| None | Class: "DOCUMENT" |  |




### Verkeerstelling
> **Definitie Verkeerstelling:** 
>
> Een onderzoek om inzicht te krijgen in het verkeer, in de hoeveelheid verkeer, de verdeling en de gereden snelheid.

| Eigenschap | Waarde |
| :--- | :------ |
| name | Verkeerstelling |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2018-11-21 13:11:36 |
| modified | 2024-04-17 13:34:25 |
| id | EAID_DBE739FD_EBC4_4650_8A2B_714294A63A73 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Verkeerstelling |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA2/0.9/id-cb656c23-5e43-4f7d-9c06-ff5351911fdb](https://gemmaonline.nl/index.php/GEMMA2/0.9/id-cb656c23-5e43-4f7d-9c06-ff5351911fdb) |
| gemma_definitie | Een onderzoek om inzicht te krijgen in het verkeer, in de hoeveelheid verkeer, de verdeling en de gereden snelheid. |
| gemma_toelichting |  |


Attributen van objecttype Verkeerstelling

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| aantal | int |  |
| tijdTot | DateTime |  |
| tijdVanaf | DateTime |  |
| None |  |  |




### VLogInfo
> **Definitie VLogInfo:** 
>
> V-log is een open standaard voor datalogging van een verkeersregelinstallatie.

| Eigenschap | Waarde |
| :--- | :------ |
| name | VLogInfo |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2018-11-21 13:24:06 |
| modified | 2024-04-17 13:34:25 |
| id | EAID_E4EEBD4D_A41E_4c9d_8099_CDA45BFF0056 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype VLogInfo

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| detectieVerkeer | int |  |
| eindegroen | boolean |  |
| snelheid | int |  |
| startgroen | boolean |  |
| tijdstip | DateTime |  |
| verkeerWilGroen | boolean |  |
| wachttijd | int |  |
| None |  |  |
| None |  |  |
| None |  |  |







## Enumeraties Model Verkeer en Vervoer


### Aantal Gehinderden
Geen Definitie

Het enumeratie Aantal Gehinderden kent de volgende waarden:

* **minder dan 1000**: <Geen Definities>
* **1.000 tot 10.000**: <Geen Definities>
* **10.000 tot 100.000**: <Geen Definities>
* **100.000 tot 1.000.000**: <Geen Definities>
* **meer dan 1.000.000**: <Geen Definities>


De enumeratie Aantal Gehinderden heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | Aantal Gehinderden |
| toelichting | None |
| synoniemen | None |
| uri | None |
| bron | None |
| author | None |
| version | None |
| created | None |
| modified | None |
| id | EAID_C00A2866_8F7D_4be3_A676_794C9A477556 |
| domein_iv3 | None |
| domein_dcat | None |
| gemma_naam | None |
| gemma_type | None |
| gemma_url | None |
| gemma_definitie | None |
| gemma_toelichting | None |



### Hindercategorie
Geen Definitie

Het enumeratie Hindercategorie kent de volgende waarden:

* **A**: <Geen Definities>
* **B**: <Geen Definities>
* **C**: <Geen Definities>
* **D**: <Geen Definities>
* **E**: <Geen Definities>


De enumeratie Hindercategorie heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | Hindercategorie |
| toelichting | None |
| synoniemen | None |
| uri | None |
| bron | None |
| author | None |
| version | None |
| created | None |
| modified | None |
| id | EAID_A1A8B6C1_3607_4c64_92CC_364470368C3E |
| domein_iv3 | None |
| domein_dcat | None |
| gemma_naam | None |
| gemma_type | None |
| gemma_url | None |
| gemma_definitie | None |
| gemma_toelichting | None |



### Hinderklasse
Geen Definitie

Het enumeratie Hinderklasse kent de volgende waarden:

* **Klasse 0: Geen hinder**: <Geen Definities>
* **Klasse 1: Kleine hinder**: <Geen Definities>
* **Klasse 2: Matige hinder**: <Geen Definities>
* **Klasse 3: Grote hinder**: <Geen Definities>
* **Klasse 4: Zeer grote hinder**: <Geen Definities>


De enumeratie Hinderklasse heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | Hinderklasse |
| toelichting | None |
| synoniemen | None |
| uri | None |
| bron | None |
| author | None |
| version | None |
| created | None |
| modified | None |
| id | EAID_9387D652_A431_4f4c_9F35_4DB0A102B1EF |
| domein_iv3 | None |
| domein_dcat | None |
| gemma_naam | None |
| gemma_type | None |
| gemma_url | None |
| gemma_definitie | None |
| gemma_toelichting | None |



### Stremmingstatus
Geen Definitie

Het enumeratie Stremmingstatus kent de volgende waarden:

* **Afgerond**: <Geen Definities>
* **In Uitvoering**: <Geen Definities>
* **Gepulbliceerd**: <Geen Definities>
* **Aangemeld**: <Geen Definities>
* **Plan Afhandelen**: <Geen Definities>


De enumeratie Stremmingstatus heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | Stremmingstatus |
| toelichting | None |
| synoniemen | None |
| uri | None |
| bron | None |
| author | None |
| version | None |
| created | None |
| modified | None |
| id | EAID_94230A7B_8876_4a0b_B660_424E397045B2 |
| domein_iv3 | None |
| domein_dcat | None |
| gemma_naam | None |
| gemma_type | None |
| gemma_url | None |
| gemma_definitie | None |
| gemma_toelichting | None |




