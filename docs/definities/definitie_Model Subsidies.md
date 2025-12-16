# Model Subsidies
## Inleiding
> **Definitie Model Subsidies:** 
>
> Het informatiedomein dat gegevens omvat over het proces van aanvragen, beoordelen, verstrekken, beheren en verantwoorden van subsidies door de organisatie, zowel in de rol van subsidieverstrekker als subsidieontvanger.

??? info "Kenmerken Model Model Subsidies"

    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | Model Subsidies |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.6 |
    | created | 2019-11-28 15:38:12 |
    | modified | 2025-03-27 15:28:35 |
    | id | EAPK\_702429CB\_A2F6\_4733\_BEB5\_341C672DF5EF |
    

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


## Objecttypen Model Subsidies


### Betaalmoment
> **Definitie Betaalmoment:** 
>
> Moment waarop er een bepaald deel van de subsidie betaald moet worden.

??? info "Kenmerken Model Betaalmoment"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Betaalmoment |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.11.0 |
    | created | 2023-07-24 10:36:30 |
    | modified | 2025-12-16 10:28:34 |
    | id | EAID\_E403A215\_A367\_4eef\_8716\_075AF54388D0 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

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

??? info "Kenmerken Model Rapportagemoment"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Rapportagemoment |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-11-28 15:40:55 |
    | modified | 2025-12-16 10:28:34 |
    | id | EAID\_20CA8283\_CE99\_455c\_BF4D\_EAE3DF41AE5B |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Rapportagemoment |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-0ae46688-6cc8-4553-adc7-04b2ed7b8b8f](https://gemmaonline.nl/index.php/GEMMA/id-0ae46688-6cc8-4553-adc7-04b2ed7b8b8f) |
    | gemma_definitie | Een vantevoren bepaald tijdstip waarom een gegevensanalyse wordt uitgevoerd |
    | gemma_toelichting |  |
    

Attributen van objecttype Rapportagemoment

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| datum | Date |  |
| naam | AN200 |  |
| omschrijving | text |  |
| termijn | int | Termijn in dagen |



### Sector
> **Definitie Sector:** 
>
> Sector is de verzameling van werkzaamheden, gericht op de productie van bepaalde goederen en diensten. Het gaat hierbij niet alleen om activiteiten van het bedrijfsleven, maar ook om activiteiten van niet op winst gerichte instellingen en de overheid.

??? info "Kenmerken Model Sector"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Sector |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-11-28 15:42:13 |
    | modified | 2025-12-16 10:28:34 |
    | id | EAID\_DA4F9850\_4CA0\_4508\_9D57\_F631BC30B360 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Sector |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-60596f8e-1454-4ca8-9a31-64e7fc554815](https://gemmaonline.nl/index.php/GEMMA/id-60596f8e-1454-4ca8-9a31-64e7fc554815) |
    | gemma_definitie | Sector is de verzameling van werkzaamheden, gericht op de productie van bepaalde goederen en diensten. Het gaat hierbij niet alleen om activiteiten van het bedrijfsleven, maar ook om activiteiten van niet op winst gerichte instellingen en de overheid. |
    | gemma_toelichting |  |
    

Attributen van objecttype Sector

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| naam | AN200 |  |
| omschrijving | Text |  |



### Subsidie
> **Definitie Subsidie:** 
>
> Aan derden toegekende financiele middelen, bestemd voor het uitvoeren van bepaalde activiteiten

??? info "Kenmerken Model Subsidie"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Subsidie |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-11-28 15:58:19 |
    | modified | 2025-12-16 10:28:34 |
    | id | EAID\_FD701A55\_6865\_44aa\_9A73\_C46E02481796 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Subsidie |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-1fe5c807-e9a7-4f44-a2b6-816341875d6e](https://gemmaonline.nl/index.php/GEMMA/id-1fe5c807-e9a7-4f44-a2b6-816341875d6e) |
    | gemma_definitie | Aan derden toegekende financiele middelen, bestemd voor het uitvoeren van bepaalde activiteiten |
    | gemma_toelichting |  |
    

Attributen van objecttype Subsidie

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| niveau | Enumeratie: "Subsidieniveau" |  |
| deadlineIndiening | Date |  |
| subsidiebedrag | Bedrag |  |
| coFinanciering | Bedrag |  |
| opmerkingen | Text |  |
| status | AN80 |  |
| accountantscontrole | Boolean |  |
| datumStart | Date |  |
| datumEinde | Date |  |
| datumVerzendingEindeafrekening | Date |  |
| gerealiseerdeProjectkosten | Date |  |
| hoogteSubsidie | Bedrag |  |
| datumBehandeltermijn | Date |  |
| datumSubsidievaststelling | Date |  |
| subsidievaststellingBedrag | Bedrag |  |
| ontvangenBedrag | Bedrag |  |
| datumBewaartermijn | Date |  |
| onderwerp | AN200 |  |
| subsidiesoort | AN80 |  |
| socialReturnVerplichting | Boolean |  |
| socialReturnNagekomen | Boolean |  |
| socialReturnBedrag | Bedrag |  |
| verantwoordenOp | Date |  |
| uitgaandeSubsidie | Boolean |  |
| prestatiesubsidie | Boolean | Als Nee dan is het een stimuleringssubsidie<br>Alleen bij uitgaande subsidies, anders NULL! |
| doelstelling | AN200 |  |
| opmerkingenVoorschotten | Text |  |



### Subsidieaanvraag
> **Definitie Subsidieaanvraag:** 
>
> Aanvraag voor een subsidie

??? info "Kenmerken Model Subsidieaanvraag"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Subsidieaanvraag |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-11-28 15:39:05 |
    | modified | 2025-12-16 10:28:34 |
    | id | EAID\_26C0D33A\_B15A\_4256\_A5BF\_5382A4E03539 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Subsidieaanvraag |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-4e5cd8a8-0110-4038-9b91-1f0562401398](https://gemmaonline.nl/index.php/GEMMA/id-4e5cd8a8-0110-4038-9b91-1f0562401398) |
    | gemma_definitie | Aanvraag voor een subsidie |
    | gemma_toelichting |  |
    

Attributen van objecttype Subsidieaanvraag

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| datumIndiening | Date |  |
| aangevraagdBedrag | Bedrag |  |
| ontvangstbevestiging | Date |  |
| verwachteBeschikking | Date |  |
| kenmerk | AN80 |  |



### Subsidiebeschikking
> **Definitie Subsidiebeschikking:** 
>
> Besluit over het al dan niet toekennen van een subsidie

??? info "Kenmerken Model Subsidiebeschikking"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Subsidiebeschikking |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-11-28 15:39:58 |
    | modified | 2025-12-16 10:28:34 |
    | id | EAID\_F8BD6D83\_D3F8\_4dd3\_B12E\_22A991D1A0A2 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Subsidiebeschikking |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-0cbc6488-2932-4634-b226-a741ba030a46](https://gemmaonline.nl/index.php/GEMMA/id-0cbc6488-2932-4634-b226-a741ba030a46) |
    | gemma_definitie | Besluit over het al dan niet toekennen van een subsidie |
    | gemma_toelichting |  |
    

Attributen van objecttype Subsidiebeschikking

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| beschiktBedrag | Bedrag |  |
| ontvangen | Date |  |
| kenmerk | AN80 |  |
| internKenmerk | AN80 |  |
| opmerkingen | text |  |
| besluit | AN80 |  |
| beschikkingsnummer | AN80 |  |



### Subsidiecomponent
> **Definitie Subsidiecomponent:** 
>
> Onderdeel van een subisidie met een eigen kostenplaats.

??? info "Kenmerken Model Subsidiecomponent"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Subsidiecomponent |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.11.0 |
    | created | 2023-07-24 10:16:34 |
    | modified | 2025-12-16 10:28:34 |
    | id | EAID\_DB093A73\_BE89\_462b\_8FBA\_19B2629072ED |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Subsidiecomponent

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| toegekendBedrag | Bedrag |  |
| gereserveerdBedrag | Bedrag |  |



### Subsidieprogramma
> **Definitie Subsidieprogramma:** 
>
> Programma waarin meerdere subsidies worden verleend vanuit een bepaalde samenhang

??? info "Kenmerken Model Subsidieprogramma"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Subsidieprogramma |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-11-28 15:41:40 |
    | modified | 2025-12-16 10:28:34 |
    | id | EAID\_8F1A719D\_C89A\_4194\_8FF4\_1F3E0F174D3D |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Subsidieprogramma |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-3c8f512f-33ab-4e24-8ea4-820796359003](https://gemmaonline.nl/index.php/GEMMA/id-3c8f512f-33ab-4e24-8ea4-820796359003) |
    | gemma_definitie | Programma waarin meerdere subsidies worden verleend vanuit een bepaalde samenhang |
    | gemma_toelichting |  |
    

Attributen van objecttype Subsidieprogramma

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| naam | AN200 |  |
| omschrijving | text |  |
| datumStart | Date |  |
| datumEinde | Date |  |
| programmabegroting | Bedrag |  |



### Taak
> **Definitie Taak:** 
>
> Een samenhangende set activiteiten in het kader van een subsidie.

??? info "Kenmerken Model Taak"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Taak |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-11-28 15:41:15 |
    | modified | 2025-12-16 10:28:34 |
    | id | EAID\_156C82B1\_2641\_40c8\_9E99\_60031643C29A |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Taak |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-020a5c18-9065-48d4-9cdd-5500cf5ce9ae](https://gemmaonline.nl/index.php/GEMMA/id-020a5c18-9065-48d4-9cdd-5500cf5ce9ae) |
    | gemma_definitie | Een samenhangende set activiteiten in het kader van een subsidie. |
    | gemma_toelichting |  |
    

Attributen van objecttype Taak

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| datumStart | Date |  |
| datumEinde | Date |  |
| termijn | int | Termijn in dagen |
| taakomschrijving | Text |  |






## Enumeraties Model Subsidies


### Subsidieniveau
Geen Definitie

Het enumeratie Subsidieniveau kent de volgende waarden:

* **Gemeente**: 
* **Provincie**: 
* **Nationaal**: 
* **Europees**: 
* **Regionaal**: 


De enumeratie Subsidieniveau heeft de volgende kenmerken:

??? info "Kenmerken Model Subsidieniveau"

    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | Subsidieniveau |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author |  |
    | version | 1.11.0 |
    | created | 2025-03-26 11:13:14 |
    | modified | 2025-12-16 10:28:45 |
    | id | EAID\_B4CF1D3E\_D000\_467d\_A9D5\_4519704F4A6D |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    


