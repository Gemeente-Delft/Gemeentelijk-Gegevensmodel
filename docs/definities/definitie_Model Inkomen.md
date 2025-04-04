# Model Inkomen
## Inleiding
> **Definitie Model Inkomen:** 
>
> Het informatiedomein dat gegevens omvat over inkomensvoorzieningen, -regelingen en financiële ondersteuning voor inwoners, gericht op het waarborgen van bestaanszekerheid en participatie in de samenleving.

Het model 'Model Inkomen' kent de volgende objecttypen:

* **Component**: <Geen Definities>
* **ComponentSoort**: <Geen Definities>
* **Inkomensvoorziening**: Een regeling die zorg draag voor een inkomen confom de landelijke wetgeving
* **Inkomensvoorzieningsoort**: Typering van een inkomensvoorziening
* **Regeling**: Een Regeling is gekoppeld aan een ingeschreven persoon (client) en beschrijft de specifieke afspraken of voorwaarden waaronder inkomensondersteuning wordt verleend. Een regeling heeft altijd een relatie met een RegelingSoort, die het type regeling specificeert.
* **Regelingsoort**: Typologie van een regeling
* **UitkeringsRun**: <Geen Definities>


Het model 'Model Inkomen' heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | Model Inkomen |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | arjen |
| version | 1.0 |
| created | 2025-03-27 11:31:16 |
| modified | 2025-03-27 15:29:52 |
| id | EAPK_7A13550B_AC75_4783_BD16_A9ED6E86172A |


## Objecttypen Model Inkomen


### Component
> **Definitie Component:** 
>
> Geen Definitie

| Eigenschap | Waarde |
| :--- | :------ |
| name | Component |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | aashkpour |
| version | 1.0 |
| created | 2022-06-08 14:19:54 |
| modified | 2025-03-27 14:01:30 |
| id | EAID_F4FD02F2_9FFA_4a35_BA32_B4CDE4002E7A |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Component

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| bedrag | bedrag |  |
| begindatumBetrekkingop | Date |  |
| eindatumBetrekkingop | Date |  |
| debetCredit | AN50 |  |
| rekeningNummer | AN50 |  |
| grootboekcode | AN50 |  |
| grootboekomschrijving | AN100 |  |
| kostenplaats | AN50 |  |
| groep | AN50 |  |
| omschrijving | AN100 |  |
| toelichting | AN50 |  |
| groepcode | AN20 |  |



### ComponentSoort
> **Definitie ComponentSoort:** 
>
> Geen Definitie

| Eigenschap | Waarde |
| :--- | :------ |
| name | ComponentSoort |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | aashkpour |
| version | 1.0 |
| created | 2022-06-08 14:20:08 |
| modified | 2025-03-27 14:01:36 |
| id | EAID_3372192D_4773_46b2_BDA5_C98B220F8954 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype ComponentSoort

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| regelingcode | AN50 |  |
| regeling | AN100 |  |
| kolom | AN50 |  |
| kolomcode | AN50 |  |
| componentcode | AN50 |  |
| omschrijving | text |  |



### Inkomensvoorziening
> **Definitie Inkomensvoorziening:** 
>
> Een regeling die zorg draag voor een inkomen confom de landelijke wetgeving

| Eigenschap | Waarde |
| :--- | :------ |
| name | Inkomensvoorziening |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | crossover |
| version | 1.0 |
| created | 2018-04-23 11:53:14 |
| modified | 2025-03-27 14:01:49 |
| id | EAID_07784236_3AA6_45e5_8253_7D088C4020B0 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Inkomensvoorziening

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| ingangsdatum | date |  |
| einddatum | date |  |
| toekenningsdatum | date |  |
| bedrag | bedrag |  |
| eenmalig | boolean |  |
| groep | AN100 |  |



### Inkomensvoorzieningsoort
> **Definitie Inkomensvoorzieningsoort:** 
>
> Typering van een inkomensvoorziening

| Eigenschap | Waarde |
| :--- | :------ |
| name | Inkomensvoorzieningsoort |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | crossover |
| version | 1.0 |
| created | 2018-04-23 11:53:23 |
| modified | 2025-03-27 14:01:56 |
| id | EAID_AF18E7D3_279D_4323_B785_6C75B4701430 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Inkomensvoorzieningsoort

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| naam | AN80 |  |
| omschrijving | text |  |
| wet | Enumeratie: "Wet" |  |
| vergoeding | AN200 |  |
| vergoedingscode | AN20 |  |
| regeling | AN200 |  |
| regelingscode | AN20 |  |
| code | AN20 |  |



### Regeling
> **Definitie Regeling:** 
>
> Een Regeling is gekoppeld aan een ingeschreven persoon (client) en beschrijft de specifieke afspraken of voorwaarden waaronder inkomensondersteuning wordt verleend. Een regeling heeft altijd een relatie met een RegelingSoort, die het type regeling specificeert.

| Eigenschap | Waarde |
| :--- | :------ |
| name | Regeling |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron | [https://www.begrippenxl.nl/dso/nl/page/Regeling](https://www.begrippenxl.nl/dso/nl/page/Regeling) |
| author | crossover |
| version | 1.0 |
| created | 2018-04-23 11:56:16 |
| modified | 2025-03-27 14:09:02 |
| id | EAID_C25455F3_FEB0_4c6d_9AA4_3B027718BEE3 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Regeling

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| startdatum | date |  |
| einddatum | date |  |
| toekenningsdatum | date |  |
| omschrijving | text |  |



### Regelingsoort
> **Definitie Regelingsoort:** 
>
> Typologie van een regeling

| Eigenschap | Waarde |
| :--- | :------ |
| name | Regelingsoort |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | crossover |
| version | 1.0 |
| created | 2018-04-23 11:56:27 |
| modified | 2025-03-27 14:02:17 |
| id | EAID_14D3C960_5EF2_433c_8E1C_B493974280E2 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Regelingsoort

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| naam | AN80 |  |
| omschrijving | text |  |



### UitkeringsRun
> **Definitie UitkeringsRun:** 
>
> Geen Definitie

| Eigenschap | Waarde |
| :--- | :------ |
| name | UitkeringsRun |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | aashkpour |
| version | 1.0 |
| created | 2022-06-08 14:20:23 |
| modified | 2025-03-27 14:01:43 |
| id | EAID_F787184D_3AA8_4132_96C4_23A363C3C1B7 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype UitkeringsRun

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| datumRun | Date |  |
| periodeRun | AN20 |  |
| soortRun | AN50 |  |
| frequentie | AN20 |  |






## Enumeraties Model Inkomen


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
| id | EAID_1e1574a9_66d9_4e24_b202_f65c4aa0bae6 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |




