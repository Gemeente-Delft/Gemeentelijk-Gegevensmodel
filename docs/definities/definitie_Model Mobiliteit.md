# Model Mobiliteit
## Inleiding
> **Definitie Model Mobiliteit:** 
>
> Het informatiedomein dat de structuur, definities en relaties van gegevens omvat met betrekking tot verkeer en vervoer van personen en goederen, gericht op het faciliteren van efficiënte en duurzame mobiliteit.

??? info "Kenmerken Model Model Mobiliteit"

    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | Model Mobiliteit |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.4 |
    | created | 2018-03-21 11:47:02 |
    | modified | 2025-03-27 15:28:35 |
    | id | EAPK\_13DD932C\_4F69\_4c62\_B2D5\_6676B5E5E24A |
    

Het model 'Model Mobiliteit' kent de volgende objecttypen:

* **Stremming**: Situatie waarbij de doorstroming van het (vaar)wegverkeer plaatselijk is geblokkeerd als gevolg van een incident
* **Strooidag**: Dag waarop op wegen gestrooid wordt ter voorkoming van gladheid
* **Strooiroute**: Traject waarop het strooien plaatsvindt
* **StrooirouteUitvoering**: De route die uiteindelijk is gevolgd voor het strooien
* **Verkeersbesluit**: Een besluit van een wegbeheerder om een bepaald verkeersteken te plaatsen, te wijzigen of in te trekken of een bepaalde fysieke maatregel te treffen.
* **Verkeerstelling**: Een onderzoek om inzicht te krijgen in het verkeer, in de hoeveelheid verkeer, de verdeling en de gereden snelheid.
* **VLogInfo**: V-log is een open standaard voor datalogging van een verkeersregelinstallatie.


## Objecttypen Model Mobiliteit


### Stremming
> **Definitie Stremming:** 
>
> Situatie waarbij de doorstroming van het (vaar)wegverkeer plaatselijk is geblokkeerd als gevolg van een incident

??? info "Kenmerken Model Stremming"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Stremming |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.11.0 |
    | created | 2018-11-12 14:25:17 |
    | modified | 2025-12-16 10:28:33 |
    | id | EAID\_999725EE\_737F\_410e\_906B\_9865EBED3597 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Stremming |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-563fd27c-7299-4311-8f40-60a95b9da4b5](https://gemmaonline.nl/index.php/GEMMA/id-563fd27c-7299-4311-8f40-60a95b9da4b5) |
    | gemma_definitie | Situatie waarbij de doorstroming van het (vaar)wegverkeer plaatselijk is geblokkeerd als gevolg van een incident |
    | gemma_toelichting |  |
    

Attributen van objecttype Stremming

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| naam | AN250 |  |
| datumStart | DateTime |  |
| datumEinde | DateTime |  |
| datumAanmelding | DateTime |  |
| status | Enumeratie: "Stremmingstatus" |  |
| datumWijziging | DateTime |  |
| geschiktVoorPublicatie | boolean |  |
| delenToegestaan | boolean |  |
| locatie | Point |  |
| hinderklasse | Enumeratie: "Hinderklasse" |  |
| aantalGehinderden | Enumeratie: "Aantal Gehinderden" |  |



### Strooidag
> **Definitie Strooidag:** 
>
> Dag waarop op wegen gestrooid wordt ter voorkoming van gladheid

??? info "Kenmerken Model Strooidag"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Strooidag |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.11.0 |
    | created | 2018-11-21 10:32:27 |
    | modified | 2025-12-16 10:28:33 |
    | id | EAID\_E2448A6D\_3AE0\_4884\_AD5C\_215A9E7166DE |
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
| minimumtemperatuur | double |  |
| tijdMinimumtemperatuur | Time |  |
| maximumtemperatuur | double |  |
| tijdMaximumtemperatuur | Time |  |



### Strooiroute
> **Definitie Strooiroute:** 
>
> Traject waarop het strooien plaatsvindt

??? info "Kenmerken Model Strooiroute"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Strooiroute |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.11.0 |
    | created | 2018-11-21 10:31:32 |
    | modified | 2025-12-16 10:28:33 |
    | id | EAID\_73090FF8\_12FD\_471e\_80FD\_DBFB2FF97D7B |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Strooiroute |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-8d6c2c57-1e18-4257-a894-5f5d751279ea](https://gemmaonline.nl/index.php/GEMMA/id-8d6c2c57-1e18-4257-a894-5f5d751279ea) |
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

??? info "Kenmerken Model StrooirouteUitvoering"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | StrooirouteUitvoering |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.11.0 |
    | created | 2018-11-21 10:32:13 |
    | modified | 2025-12-16 10:28:33 |
    | id | EAID\_B825D33A\_6DCE\_4263\_A031\_E6E92C4EE86B |
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
| route | MultiCurve |  |
| geplandStart | DateTime |  |
| geplandEinde | DateTime |  |
| werkelijkeStart | DateTime |  |
| werkelijkEinde | DateTime |  |



### Verkeersbesluit
> **Definitie Verkeersbesluit:** 
>
> Een besluit van een wegbeheerder om een bepaald verkeersteken te plaatsen, te wijzigen of in te trekken of een bepaalde fysieke maatregel te treffen.

??? info "Kenmerken Model Verkeersbesluit"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Verkeersbesluit |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.11.0 |
    | created | 2019-03-06 14:05:18 |
    | modified | 2025-12-16 10:28:33 |
    | id | EAID\_3F83DAA3\_C37F\_42b2\_8D35\_D75B840172F8 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Verkeersbesluit |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-833312cc-f7d8-4b4c-9e79-b21c8e7597cb](https://gemmaonline.nl/index.php/GEMMA/id-833312cc-f7d8-4b4c-9e79-b21c8e7597cb) |
    | gemma_definitie | Een besluit van een wegbeheerder om een bepaald verkeersteken te plaatsen, te wijzigen of in te trekken of een bepaalde fysieke maatregel te treffen. |
    | gemma_toelichting |  |
    

Attributen van objecttype Verkeersbesluit

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| referentienummer | AN80 |  |
| datumBesluit | Date |  |
| datumStart | Datetime |  |
| titel | AN250 |  |
| straat | An200 |  |
| postcode | AN6 |  |
| huisnummer | AN40 |  |
| datumEinde | Datetime |  |



### Verkeerstelling
> **Definitie Verkeerstelling:** 
>
> Een onderzoek om inzicht te krijgen in het verkeer, in de hoeveelheid verkeer, de verdeling en de gereden snelheid.

??? info "Kenmerken Model Verkeerstelling"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Verkeerstelling |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.11.0 |
    | created | 2018-11-21 13:11:36 |
    | modified | 2025-12-16 10:28:33 |
    | id | EAID\_DBE739FD\_EBC4\_4650\_8A2B\_714294A63A73 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Verkeerstelling |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-cb656c23-5e43-4f7d-9c06-ff5351911fdb](https://gemmaonline.nl/index.php/GEMMA/id-cb656c23-5e43-4f7d-9c06-ff5351911fdb) |
    | gemma_definitie | Een onderzoek om inzicht te krijgen in het verkeer, in de hoeveelheid verkeer, de verdeling en de gereden snelheid. |
    | gemma_toelichting |  |
    

Attributen van objecttype Verkeerstelling

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| tijdVanaf | DateTime |  |
| tijdTot | DateTime |  |
| aantal | int |  |



### VLogInfo
> **Definitie VLogInfo:** 
>
> V-log is een open standaard voor datalogging van een verkeersregelinstallatie.

??? info "Kenmerken Model VLogInfo"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | VLogInfo |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.11.0 |
    | created | 2018-11-21 13:24:06 |
    | modified | 2025-12-16 10:28:33 |
    | id | EAID\_E4EEBD4D\_A41E\_4c9d\_8099\_CDA45BFF0056 |
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
| tijdstip | DateTime |  |
| snelheid | int |  |
| startgroen | boolean |  |
| eindegroen | boolean |  |
| verkeerWilGroen | boolean |  |
| wachttijd | int |  |
| detectieVerkeer | int |  |






## Enumeraties Model Mobiliteit


### Aantal Gehinderden
Geen Definitie

Het enumeratie Aantal Gehinderden kent de volgende waarden:

* **minder dan 1000**: 
* **1.000 tot 10.000**: 
* **10.000 tot 100.000**: 
* **100.000 tot 1.000.000**: 
* **meer dan 1.000.000**: 


De enumeratie Aantal Gehinderden heeft de volgende kenmerken:

??? info "Kenmerken Model Aantal Gehinderden"

    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | Aantal Gehinderden |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author |  |
    | version | 1.10.0 |
    | created | 2025-03-26 11:12:43 |
    | modified | 2025-12-16 10:28:45 |
    | id | EAID\_C00A2866\_8F7D\_4be3\_A676\_794C9A477556 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    


### Hindercategorie
Geen Definitie

Het enumeratie Hindercategorie kent de volgende waarden:

* **A**: 
* **B**: 
* **C**: 
* **D**: 
* **E**: 


De enumeratie Hindercategorie heeft de volgende kenmerken:

??? info "Kenmerken Model Hindercategorie"

    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | Hindercategorie |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author |  |
    | version | 1.10.0 |
    | created | 2025-03-26 11:12:43 |
    | modified | 2025-12-16 10:28:45 |
    | id | EAID\_A1A8B6C1\_3607\_4c64\_92CC\_364470368C3E |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    


### Hinderklasse
Geen Definitie

Het enumeratie Hinderklasse kent de volgende waarden:

* **Klasse 0: Geen hinder**: 
* **Klasse 1: Kleine hinder**: Geen file: vertraging < 5 minuten
* **Klasse 2: Matige hinder**: 5 tot 10 minuten vertraging door file of omrijden
* **Klasse 3: Grote hinder**: 10 tot 30 minuten vertraging door file of omrijden
* **Klasse 4: Zeer grote hinder**: > 30 minuten vertraging door file of omrijden


De enumeratie Hinderklasse heeft de volgende kenmerken:

??? info "Kenmerken Model Hinderklasse"

    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | Hinderklasse |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author |  |
    | version | 1.10.0 |
    | created | 2025-03-26 11:12:43 |
    | modified | 2025-12-16 10:28:45 |
    | id | EAID\_9387D652\_A431\_4f4c\_9F35\_4DB0A102B1EF |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    


### Stremmingstatus
Geen Definitie

Het enumeratie Stremmingstatus kent de volgende waarden:

* **Afgerond**: 
* **In Uitvoering**: 
* **Gepulbliceerd**: 
* **Aangemeld**: 
* **Plan Afhandelen**: 


De enumeratie Stremmingstatus heeft de volgende kenmerken:

??? info "Kenmerken Model Stremmingstatus"

    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | Stremmingstatus |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author |  |
    | version | 1.10.0 |
    | created | 2025-03-26 11:12:43 |
    | modified | 2025-12-16 10:28:45 |
    | id | EAID\_94230A7B\_8876\_4a0b\_B660\_424E397045B2 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    


