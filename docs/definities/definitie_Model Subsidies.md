# Model Subsidies
## Inleiding
> **Definitie Model Subsidies:** 
>
> Geen definitie

Het model 'Model Subsidies' kent de volgende objecttypen:

* **Betaalmoment**: Moment waarop er een bepaald deel van de subsidie betaald moet worden.
* **Rapportagemoment**: Een vantevoren bepaald tijdstip waarom een gegevensanalyse wordt uitgevoerd
* **Sector**: Sector is de verzameling van werkzaamheden, gericht op de productie van bepaalde goederen en diensten. Het gaat hierbij niet alleen om activiteiten van het bedrijfsleven, maar ook om activiteiten van niet op winst gerichte instellingen en de overheid.
* **Subsidie**: Aan derden toegekende financiele middelen, bestemd voor het uitvoeren van bepaalde activiteiten
* **Subsidieaanvraag**: Aanvraag voor een subsidie
* **Subsidiebeschikking**: Besluit over het al dan niet toekennen van een subsidie
* **Subsidiecomponent**: Onderdeel van een subisidie met een eigen kostenplaats.
* **Subsidieprogramma**: Programma waarin meerdere subsidies worden verleend vanuit een bepaalde samenhang
* **Taak**: Een samenhangende set activiteiten in het kader van een subsidie.


Het model 'Model Subsidies' heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | Model Subsidies |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | abrienen |
| version | 1.1 |
| created | 2019-11-28 15:38:12 |
| modified | 2023-08-02 17:59:23 |
| id | EAPK_702429CB_A2F6_4733_BEB5_341C672DF5EF |


## Objecttypen Model Subsidies


### Betaalmoment
> **Definitie Betaalmoment:** 
>
> Moment waarop er een bepaald deel van de subsidie betaald moet worden.

| Eigenschap | Waarde |
| :--- | :------ |
| name | Betaalmoment |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | arjen |
| version | 1.1 |
| created | 2023-07-24 10:36:30 |
| modified | 2023-10-12 16:27:29 |
| id | EAID_E403A215_A367_4eef_8716_075AF54388D0 |
| domein-iv3 |  |
| domein-dcat |  |
| GEMMA-naam |  |
| GEMMA-type |  |
| GEMMA-url |  |


Attributen van objecttype Betaalmoment

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| bedrag | Bedrag |  |
| datum | Datum |  |
| voorschot | boolean |  |




### Rapportagemoment
> **Definitie Rapportagemoment:** 
>
> Een vantevoren bepaald tijdstip waarom een gegevensanalyse wordt uitgevoerd

| Eigenschap | Waarde |
| :--- | :------ |
| name | Rapportagemoment |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | abrienen |
| version | 1.1 |
| created | 2019-11-28 15:40:55 |
| modified | 2023-10-12 16:27:29 |
| id | EAID_20CA8283_CE99_455c_BF4D_EAE3DF41AE5B |
| domein-iv3 |  |
| domein-dcat |  |
| GEMMA-naam |  |
| GEMMA-type |  |
| GEMMA-url |  |


Attributen van objecttype Rapportagemoment

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| datum | Date |  |
| naam | AN200 |  |
| omschrijving | text |  |
| termijn | int |  |
| None | Class: "DOCUMENT" |  |




### Sector
> **Definitie Sector:** 
>
> Sector is de verzameling van werkzaamheden, gericht op de productie van bepaalde goederen en diensten. Het gaat hierbij niet alleen om activiteiten van het bedrijfsleven, maar ook om activiteiten van niet op winst gerichte instellingen en de overheid.

| Eigenschap | Waarde |
| :--- | :------ |
| name | Sector |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | abrienen |
| version | 1.1 |
| created | 2019-11-28 15:42:13 |
| modified | 2023-10-12 16:27:29 |
| id | EAID_DA4F9850_4CA0_4508_9D57_F631BC30B360 |
| domein-iv3 |  |
| domein-dcat |  |
| GEMMA-naam |  |
| GEMMA-type |  |
| GEMMA-url |  |


Attributen van objecttype Sector

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| naam | AN200 |  |
| omschrijving | Text |  |




### Subsidie
> **Definitie Subsidie:** 
>
> Aan derden toegekende financiele middelen, bestemd voor het uitvoeren van bepaalde activiteiten

| Eigenschap | Waarde |
| :--- | :------ |
| name | Subsidie |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron | https://aquo.begrippenxl.nl/aquo/nl/page/Id-255a35d2-ab3b-4281-b079-b12f750861a7 |
| author | abrienen |
| version | 1.1 |
| created | 2019-11-28 15:58:19 |
| modified | 2023-10-12 16:27:29 |
| id | EAID_FD701A55_6865_44aa_9A73_C46E02481796 |
| domein-iv3 |  |
| domein-dcat |  |
| GEMMA-naam |  |
| GEMMA-type |  |
| GEMMA-url |  |


Attributen van objecttype Subsidie

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| accountantscontrole | Boolean |  |
| behandeltermijn datum | Date |  |
| bewaartermijn datum | Date |  |
| co-financiering | Bedrag |  |
| deadline indiening | Date |  |
| doelstelling | AN200 |  |
| einddatum | Date |  |
| gerealiseerde projectkosten | Date |  |
| hoogte subsidie | Bedrag |  |
| niveau | Enumeratie: "Subsidieniveau" |  |
| onderwerp | AN200 |  |
| ontvangen bedrag | Bedrag |  |
| opmerking | Text |  |
| opmerking voorschotten | Text |  |
| prestatiesubsidie | Boolean |  |
| socialreturn bedrag | Bedrag |  |
| socialreturn nagekomen | Boolean |  |
| socialreturn verplichting | Boolean |  |
| startdatum | Date |  |
| status | AN80 |  |
| subsidiebedrag | Bedrag |  |
| subsidiesoort | AN80 |  |
| subsidievaststelling bedrag | Bedrag |  |
| subsidievaststelling datum | Date |  |
| uitgaande subsidie | Boolean |  |
| verantwoorden op | Date |  |
| verzenddatum eindafrekening | Date |  |
| None | Class: "MEDEWERKER" |  |
| None | Class: "RECHTSPERSOON" |  |
| None | Class: "Rapportagemoment" |  |
| None | Class: "Taak" |  |
| None | Class: "Kostenplaats" |  |
| None | Class: "Sector" |  |
| None | Class: "DOCUMENT" |  |
| None | Class: "ZAAK" |  |




### Subsidieaanvraag
> **Definitie Subsidieaanvraag:** 
>
> Aanvraag voor een subsidie

| Eigenschap | Waarde |
| :--- | :------ |
| name | Subsidieaanvraag |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | abrienen |
| version | 1.1 |
| created | 2019-11-28 15:39:05 |
| modified | 2023-10-12 16:27:29 |
| id | EAID_26C0D33A_B15A_4256_A5BF_5382A4E03539 |
| domein-iv3 |  |
| domein-dcat |  |
| GEMMA-naam |  |
| GEMMA-type |  |
| GEMMA-url |  |


Attributen van objecttype Subsidieaanvraag

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| aangevraagd bedrag | Bedrag |  |
| datum indiening | Date |  |
| kenmerk | AN80 |  |
| ontvangstbevestiging | Date |  |
| verwachtte beschikking | Date |  |
| None | Class: "Subsidie" |  |
| None | Class: "Subsidiebeschikking" |  |




### Subsidiebeschikking
> **Definitie Subsidiebeschikking:** 
>
> Besluit over het al dan niet toekennen van een subsidie

| Eigenschap | Waarde |
| :--- | :------ |
| name | Subsidiebeschikking |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | abrienen |
| version | 1.1 |
| created | 2019-11-28 15:39:58 |
| modified | 2023-10-12 16:27:29 |
| id | EAID_F8BD6D83_D3F8_4dd3_B12E_22A991D1A0A2 |
| domein-iv3 |  |
| domein-dcat |  |
| GEMMA-naam |  |
| GEMMA-type |  |
| GEMMA-url |  |


Attributen van objecttype Subsidiebeschikking

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| beschikkingsnummer | AN80 |  |
| beschikt bedrag | Bedrag |  |
| besluit | AN80 |  |
| intern kenmerk | AN80 |  |
| kenmerk | AN80 |  |
| ontvangen | Date |  |
| opmerkingen | text |  |
| None | Class: "Subsidie" |  |




### Subsidiecomponent
> **Definitie Subsidiecomponent:** 
>
> Onderdeel van een subisidie met een eigen kostenplaats.

| Eigenschap | Waarde |
| :--- | :------ |
| name | Subsidiecomponent |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | arjen |
| version | 1.1 |
| created | 2023-07-24 10:16:34 |
| modified | 2023-10-12 16:27:29 |
| id | EAID_DB093A73_BE89_462b_8FBA_19B2629072ED |
| domein-iv3 |  |
| domein-dcat |  |
| GEMMA-naam |  |
| GEMMA-type |  |
| GEMMA-url |  |


Attributen van objecttype Subsidiecomponent

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| gereserveerdbedrag | Bedrag |  |
| toegekendbedrag | Bedrag |  |
| None | Class: "Betaalmoment" |  |
| None | Class: "Kostenplaats" |  |




### Subsidieprogramma
> **Definitie Subsidieprogramma:** 
>
> Programma waarin meerdere subsidies worden verleend vanuit een bepaalde samenhang

| Eigenschap | Waarde |
| :--- | :------ |
| name | Subsidieprogramma |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | abrienen |
| version | 1.1 |
| created | 2019-11-28 15:41:40 |
| modified | 2023-10-12 16:27:29 |
| id | EAID_8F1A719D_C89A_4194_8FF4_1F3E0F174D3D |
| domein-iv3 |  |
| domein-dcat |  |
| GEMMA-naam |  |
| GEMMA-type |  |
| GEMMA-url |  |


Attributen van objecttype Subsidieprogramma

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| einddatum | Date |  |
| naam | AN200 |  |
| omschrijving | text |  |
| programmabegroting | Bedrag |  |
| startdatum | Date |  |
| None | Class: "Subsidie" |  |




### Taak
> **Definitie Taak:** 
>
> Een samenhangende set activiteiten in het kader van een subsidie.

| Eigenschap | Waarde |
| :--- | :------ |
| name | Taak |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | abrienen |
| version | 1.1 |
| created | 2019-11-28 15:41:15 |
| modified | 2023-10-12 16:27:29 |
| id | EAID_156C82B1_2641_40c8_9E99_60031643C29A |
| domein-iv3 |  |
| domein-dcat |  |
| GEMMA-naam |  |
| GEMMA-type |  |
| GEMMA-url |  |


Attributen van objecttype Taak

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| einddatum | Date |  |
| startdatum | Date |  |
| taakomschrijving | Text |  |
| termijn | int |  |







## Enumeraties Model Subsidies


### Subsidieniveau
Geen Definitie

Het enumeratie Subsidieniveau kent de volgende waarden:

* **Gemeente**: <Geen Definities>
* **Provincie**: <Geen Definities>
* **Nationaal**: <Geen Definities>
* **Europees**: <Geen Definities>
* **Regionaal**: <Geen Definities>


De enumeratie Subsidieniveau heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | Subsidieniveau |
| toelichting | None |
| synoniemen | None |
| uri | None |
| bron | None |
| author | None |
| version | None |
| created | None |
| modified | None |
| id | EAID_B4CF1D3E_D000_467d_A9D5_4519704F4A6D |
| domein-iv3 |  |
| domein-dcat |  |
| GEMMA-naam |  |
| GEMMA-type |  |
| GEMMA-url |  |




