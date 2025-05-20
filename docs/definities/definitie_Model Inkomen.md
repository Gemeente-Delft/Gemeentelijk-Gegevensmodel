# Model Inkomen
## Inleiding
> **Definitie Model Inkomen:** 
>
> Het informatiedomein dat gegevens omvat over inkomensvoorzieningen, -regelingen en financi&#235;le ondersteuning voor inwoners, gericht op het waarborgen van bestaanszekerheid en participatie in de samenleving.
> 

Het model 'Model Inkomen' kent de volgende objecttypen:

* **Component**: <Geen Definities>
* **ComponentSoort**: <Geen Definities>
* **Huisvestingsoort**: Als de dienst een uitkering betreft die periodiek wordt uitgekeerd, kan om redenen de betaling worden geblokkeerd. Reden toevoeging: Geeft de reden van blokkering van de uitkering aan. Als de dienst een uitkering betreft, die periodiek wordt uitgekeerd, kan om redenen de betaling worden geblokkeerd. De betalingsblokkade wordt opgenomen bij de dienst, die wordt genoten door de client en partner van de client. Nodig voor diepere analyse van stand van uitkeringen. Hoeveel uitkleringen hebben we geblokkeerd op dit moment omdat we de uitkering gaan beindigen.  
* **Inkomensvoorziening**: Een regeling die zorg draag voor een inkomen confom de landelijke wetgeving
* **Inkomensvoorzieningsoort**: Typering van een inkomensvoorziening
* **RedenBlokkering**: Als de dienst een uitkering betreft die periodiek wordt uitgekeerd, kan om redenen de betaling worden geblokkeerd. Reden toevoeging: Geeft de reden van blokkering van de uitkering aan. Als de dienst een uitkering betreft, die periodiek wordt uitgekeerd, kan om redenen de betaling worden geblokkeerd. De betalingsblokkade wordt opgenomen bij de dienst, die wordt genoten door de client en partner van de client. Nodig voor diepere analyse van stand van uitkeringen. Hoeveel uitkleringen hebben we geblokkeerd op dit moment omdat we de uitkering gaan beindigen.  
* **RedenInstroom**: De reden waarom de persoon de uitkering heeft gekregen. Geeft de reden van aanvraag van uitkering weer. Nodig voor diepere analyse van stand van uitkeringen. Omdat we willen weten waarom mensen nstromen. Bv geen werk meer og geen andere uitkering, verhuizing. 
* **RedenUitstroom**: De reden waarom de uitkering aan een persoon is beeindgd. Reden toevoeging: Geeft de reden van uitstroom aan. Waarom is de uitkering be&#235;indigd. Nodig voor diepere analyse van stand. Meet of je beleid of het lukt om mensen naar werk te laten stromen. van uitkeringen. 
* **Regeling**: Een Regeling is gekoppeld aan een ingeschreven persoon (client) en beschrijft de specifieke afspraken of voorwaarden waaronder inkomensondersteuning wordt verleend. Een regeling heeft altijd een relatie met een RegelingSoort, die het type regeling specificeert.
* **Regelingsoort**: Typologie van een regeling
* **UitkeringsRun**: <Geen Definities>


Het model 'Model Inkomen' heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | Model Inkomen |
| toelichting | <memo> |
| synoniemen |  |
| uri |  |
| bron |  |
| author | arjen |
| version | 1.0 |
| created | 2025-03-27 11:31:16 |
| modified | 2025-04-23 15:22:26 |
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




### Huisvestingsoort
> **Definitie Huisvestingsoort:** 
>
> Als de dienst een uitkering betreft die periodiek wordt uitgekeerd, kan om redenen de betaling worden geblokkeerd. Reden toevoeging: Geeft de reden van blokkering van de uitkering aan. Als de dienst een uitkering betreft, die periodiek wordt uitgekeerd, kan om redenen de betaling worden geblokkeerd. De betalingsblokkade wordt opgenomen bij de dienst, die wordt genoten door de client en partner van de client. Nodig voor diepere analyse van stand van uitkeringen. Hoeveel uitkleringen hebben we geblokkeerd op dit moment omdat we de uitkering gaan beindigen. 
> 

| Eigenschap | Waarde |
| :--- | :------ |
| name | Huisvestingsoort |
| toelichting | <memo> |
| synoniemen |  |
| uri |  |
| bron |  |
| author | arjen |
| version | 1.0 |
| created | 2025-04-23 16:21:20 |
| modified | 2025-04-23 16:21:56 |
| id | EAID_8D999BE8_96AB_8418_B94F_289754CE1336 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Huisvestingsoort

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| begindatumGeldigheid | Date |  |
| einddatumGeldigheid | Date |  |
| omschrijving | Text |  |
| soorthuisvestingCode | AN4 |  |




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
| modified | 2025-04-23 16:14:30 |
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
| administratieveEinddatum | Date |  |
| administratieveStartdatum | Date |  |
| betalingsmomentcode | AN4 |  |
| code | AN4 |  |
| datumToekenning | Date |  |
| indicatieBlokkering | Boolean |  |
| indicatieStudietoeslag | Boolean |  |
| indicatieUitkeringSplitsen | Boolean |  |
| indicatieUitkeringsspecificatie | Boolean |  |
| versterkkingsvorm | AN200 |  |
| verwerktTotEnMetDatum | Date |  |
| None | Class: "RedenUitstroom" |  |
| None | Class: "RedenInstroom" |  |
| None | Class: "RedenBlokkering" |  |
| None | Class: "Huisvestingsoort" |  |




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




### RedenBlokkering
> **Definitie RedenBlokkering:** 
>
> Als de dienst een uitkering betreft die periodiek wordt uitgekeerd, kan om redenen de betaling worden geblokkeerd. Reden toevoeging: Geeft de reden van blokkering van de uitkering aan. Als de dienst een uitkering betreft, die periodiek wordt uitgekeerd, kan om redenen de betaling worden geblokkeerd. De betalingsblokkade wordt opgenomen bij de dienst, die wordt genoten door de client en partner van de client. Nodig voor diepere analyse van stand van uitkeringen. Hoeveel uitkleringen hebben we geblokkeerd op dit moment omdat we de uitkering gaan beindigen. 
> 

| Eigenschap | Waarde |
| :--- | :------ |
| name | RedenBlokkering |
| toelichting | <memo> |
| synoniemen |  |
| uri |  |
| bron |  |
| author | arjen |
| version | 1.0 |
| created | 2025-04-23 16:14:37 |
| modified | 2025-04-23 16:16:23 |
| id | EAID_88B0A7AB_53E6_4bc1_8D99_9BE896AB8418 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype RedenBlokkering

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| begindatumGeldigheid | Date |  |
| einddatumGeldigheid | Date |  |
| omschrijving | Text |  |
| redenBlokkeringCode | AN4 |  |




### RedenInstroom
> **Definitie RedenInstroom:** 
>
> De reden waarom de persoon de uitkering heeft gekregen. Geeft de reden van aanvraag van uitkering weer. Nodig voor diepere analyse van stand van uitkeringen. Omdat we willen weten waarom mensen nstromen. Bv geen werk meer og geen andere uitkering, verhuizing.
> 

| Eigenschap | Waarde |
| :--- | :------ |
| name | RedenInstroom |
| toelichting | <memo> |
| synoniemen |  |
| uri |  |
| bron |  |
| author | arjen |
| version | 1.0 |
| created | 2025-04-23 16:16:48 |
| modified | 2025-05-01 09:26:14 |
| id | EAID_8D999BE8_96AB_8418_99A2_CB86335AFB97 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype RedenInstroom

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| begindatumGeldigheid | Date |  |
| einddatumGeldigheid | Date |  |
| omschrijving | Text |  |
| redenInstroomCode | AN4 |  |
| CBS-code | AN4 |  |
| CBS-omschrijving | text |  |




### RedenUitstroom
> **Definitie RedenUitstroom:** 
>
> De reden waarom de uitkering aan een persoon is beeindgd. Reden toevoeging: Geeft de reden van uitstroom aan. Waarom is de uitkering be&#235;indigd. Nodig voor diepere analyse van stand. Meet of je beleid of het lukt om mensen naar werk te laten stromen. van uitkeringen.
> 

| Eigenschap | Waarde |
| :--- | :------ |
| name | RedenUitstroom |
| toelichting | <memo> |
| synoniemen |  |
| uri |  |
| bron |  |
| author | arjen |
| version | 1.0 |
| created | 2025-04-23 16:18:22 |
| modified | 2025-05-01 09:26:34 |
| id | EAID_99A2CB86_335A_FB97_9C8F_47170B1699EC |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype RedenUitstroom

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| begindatumGeldigheid | Date |  |
| einddatumGeldigheid | Date |  |
| omschrijving | Text |  |
| redenUitstroomCode | AN4 |  |
| CBS-code | AN4 |  |
| CBS-omschrijving | text |  |




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
| toelichting | None |
| synoniemen | None |
| uri | None |
| bron | None |
| author | None |
| version | 1.4 |
| created | 2025-03-26 11:12:49 |
| modified | 2025-03-26 16:14:37 |
| id | EAID_e750e59e_0d63_4f51_81f8_32fd66af6856 |
| domein_iv3 | None |
| domein_dcat | None |
| gemma_naam | None |
| gemma_type | None |
| gemma_url | None |
| gemma_definitie | None |
| gemma_toelichting | None |




