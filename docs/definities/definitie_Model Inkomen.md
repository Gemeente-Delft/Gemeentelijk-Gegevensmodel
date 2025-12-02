# Model Inkomen
## Inleiding
> **Definitie Model Inkomen:** 
>
> Het informatiedomein dat gegevens omvat over inkomensvoorzieningen, -regelingen en financiële ondersteuning voor inwoners, gericht op het waarborgen van bestaanszekerheid en participatie in de samenleving.

??? info "Kenmerken Model Model Inkomen"
    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | Model Inkomen |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | arjen |
    | version | 1.1.0 |
    | created | 2025-03-27 11:31:16 |
    | modified | 2025-07-29 22:20:23 |
    | id | EAPK_7A13550B_AC75_4783_BD16_A9ED6E86172A |
    

Het model 'Model Inkomen' kent de volgende objecttypen:

* **Component**: 
* **ComponentSoort**: 
* **Huisvestingsoort**: Als de dienst een uitkering betreft die periodiek wordt uitgekeerd, kan om redenen de betaling worden geblokkeerd. Reden toevoeging: Geeft de reden van blokkering van de uitkering aan. Als de dienst een uitkering betreft, die periodiek wordt uitgekeerd, kan om redenen de betaling worden geblokkeerd. De betalingsblokkade wordt opgenomen bij de dienst, die wordt genoten door de client en partner van de client. Nodig voor diepere analyse van stand van uitkeringen. Hoeveel uitkleringen hebben we geblokkeerd op dit moment omdat we de uitkering gaan beindigen.
* **Inkomensvoorziening**: Een regeling die zorg draag voor een inkomen confom de landelijke wetgeving
* **Inkomensvoorzieningsoort**: Typering van een inkomensvoorziening
* **RedenBlokkering**: Als de dienst een uitkering betreft die periodiek wordt uitgekeerd, kan om redenen de betaling worden geblokkeerd. Reden toevoeging: Geeft de reden van blokkering van de uitkering aan. Als de dienst een uitkering betreft, die periodiek wordt uitgekeerd, kan om redenen de betaling worden geblokkeerd. De betalingsblokkade wordt opgenomen bij de dienst, die wordt genoten door de client en partner van de client. Nodig voor diepere analyse van stand van uitkeringen. Hoeveel uitkleringen hebben we geblokkeerd op dit moment omdat we de uitkering gaan beindigen.
* **RedenInstroom**: De reden waarom de persoon de uitkering heeft gekregen. Geeft de reden van aanvraag van uitkering weer. Nodig voor diepere analyse van stand van uitkeringen. Omdat we willen weten waarom mensen nstromen. Bv geen werk meer og geen andere uitkering, verhuizing.
* **RedenUitstroom**: De reden waarom de uitkering aan een persoon is beeindgd. Reden toevoeging: Geeft de reden van uitstroom aan. Waarom is de uitkering beëindigd. Nodig voor diepere analyse van stand. Meet of je beleid of het lukt om mensen naar werk te laten stromen. van uitkeringen.
* **Regeling**: Een Regeling is gekoppeld aan een ingeschreven persoon (client) en beschrijft de specifieke afspraken of voorwaarden waaronder inkomensondersteuning wordt verleend. Een regeling heeft altijd een relatie met een RegelingSoort, die het type regeling specificeert.
* **Regelingsoort**: Typologie van een regeling
* **UitkeringsRun**: 


## Objecttypen Model Inkomen


### Component
> **Definitie Component:** 
>
> Geen Definitie

??? info "Kenmerken Model Component"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Component |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | aashkpour |
    | version | 1.1.0 |
    | created | 2022-06-08 14:19:54 |
    | modified | 2025-08-06 14:19:41 |
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
| bedrag | Bedrag |  |
| begindatumBetrekkingop | Date |  |
| debetCredit | CharacterString |  |
| eindatumBetrekkingop | Date |  |
| groep | CharacterString |  |
| groepcode | CharacterString |  |
| grootboekcode | CharacterString |  |
| grootboekomschrijving | CharacterString |  |
| kostenplaats | CharacterString |  |
| omschrijving | CharacterString |  |
| rekeningNummer | CharacterString |  |
| toelichting | CharacterString |  |



### ComponentSoort
> **Definitie ComponentSoort:** 
>
> Geen Definitie

??? info "Kenmerken Model ComponentSoort"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | ComponentSoort |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | aashkpour |
    | version | 1.1.0 |
    | created | 2022-06-08 14:20:08 |
    | modified | 2025-08-06 14:19:41 |
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
| componentcode | CharacterString |  |
| kolom | CharacterString |  |
| kolomcode | CharacterString |  |
| omschrijving | CharacterString |  |
| regeling | CharacterString |  |
| regelingcode | CharacterString |  |



### Huisvestingsoort
> **Definitie Huisvestingsoort:** 
>
> Als de dienst een uitkering betreft die periodiek wordt uitgekeerd, kan om redenen de betaling worden geblokkeerd. Reden toevoeging: Geeft de reden van blokkering van de uitkering aan. Als de dienst een uitkering betreft, die periodiek wordt uitgekeerd, kan om redenen de betaling worden geblokkeerd. De betalingsblokkade wordt opgenomen bij de dienst, die wordt genoten door de client en partner van de client. Nodig voor diepere analyse van stand van uitkeringen. Hoeveel uitkleringen hebben we geblokkeerd op dit moment omdat we de uitkering gaan beindigen.

??? info "Kenmerken Model Huisvestingsoort"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Huisvestingsoort |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | arjen |
    | version | 1.1.0 |
    | created | 2025-04-23 16:21:20 |
    | modified | 2025-08-06 14:19:41 |
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
| omschrijving | CharacterString |  |
| soorthuisvestingCode | CharacterString |  |



### Inkomensvoorziening
> **Definitie Inkomensvoorziening:** 
>
> Een regeling die zorg draag voor een inkomen confom de landelijke wetgeving

??? info "Kenmerken Model Inkomensvoorziening"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Inkomensvoorziening |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | crossover |
    | version | 1.1.0 |
    | created | 2018-04-23 11:53:14 |
    | modified | 2025-08-06 14:19:41 |
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
| administratieveEinddatum | Date |  |
| administratieveStartdatum | Date |  |
| bedrag | Bedrag |  |
| betalingsmomentcode | CharacterString |  |
| code | CharacterString |  |
| datumToekenning | Date |  |
| eenmalig | Boolean |  |
| einddatum | Date |  |
| groep | CharacterString |  |
| indicatieBlokkering | Boolean |  |
| indicatieStudietoeslag | Boolean |  |
| indicatieUitkeringSplitsen | Boolean |  |
| indicatieUitkeringsspecificatie | Boolean |  |
| ingangsdatum | Date |  |
| toekenningsdatum | Date |  |
| versterkkingsvorm | CharacterString |  |
| verwerktTotEnMetDatum | Date |  |



### Inkomensvoorzieningsoort
> **Definitie Inkomensvoorzieningsoort:** 
>
> Typering van een inkomensvoorziening

??? info "Kenmerken Model Inkomensvoorzieningsoort"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Inkomensvoorzieningsoort |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | crossover |
    | version | 1.1.0 |
    | created | 2018-04-23 11:53:23 |
    | modified | 2025-08-06 14:19:41 |
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
| code | CharacterString |  |
| naam | CharacterString |  |
| omschrijving | CharacterString |  |
| regeling | CharacterString |  |
| regelingscode | CharacterString |  |
| vergoeding | CharacterString |  |
| vergoedingscode | CharacterString |  |
| wet | Enumeratie: "Wet" |  |



### RedenBlokkering
> **Definitie RedenBlokkering:** 
>
> Als de dienst een uitkering betreft die periodiek wordt uitgekeerd, kan om redenen de betaling worden geblokkeerd. Reden toevoeging: Geeft de reden van blokkering van de uitkering aan. Als de dienst een uitkering betreft, die periodiek wordt uitgekeerd, kan om redenen de betaling worden geblokkeerd. De betalingsblokkade wordt opgenomen bij de dienst, die wordt genoten door de client en partner van de client. Nodig voor diepere analyse van stand van uitkeringen. Hoeveel uitkleringen hebben we geblokkeerd op dit moment omdat we de uitkering gaan beindigen.

??? info "Kenmerken Model RedenBlokkering"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | RedenBlokkering |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | arjen |
    | version | 1.1.0 |
    | created | 2025-04-23 16:14:37 |
    | modified | 2025-08-06 14:19:41 |
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
| omschrijving | CharacterString |  |
| redenBlokkeringCode | CharacterString |  |



### RedenInstroom
> **Definitie RedenInstroom:** 
>
> De reden waarom de persoon de uitkering heeft gekregen. Geeft de reden van aanvraag van uitkering weer. Nodig voor diepere analyse van stand van uitkeringen. Omdat we willen weten waarom mensen nstromen. Bv geen werk meer og geen andere uitkering, verhuizing.

??? info "Kenmerken Model RedenInstroom"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | RedenInstroom |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | arjen |
    | version | 1.1.0 |
    | created | 2025-04-23 16:16:48 |
    | modified | 2025-08-06 14:19:41 |
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
| CBS-code | CharacterString |  |
| CBS-omschrijving | CharacterString |  |
| einddatumGeldigheid | Date |  |
| omschrijving | CharacterString |  |
| redenInstroomCode | CharacterString |  |



### RedenUitstroom
> **Definitie RedenUitstroom:** 
>
> De reden waarom de uitkering aan een persoon is beeindgd. Reden toevoeging: Geeft de reden van uitstroom aan. Waarom is de uitkering beëindigd. Nodig voor diepere analyse van stand. Meet of je beleid of het lukt om mensen naar werk te laten stromen. van uitkeringen.

??? info "Kenmerken Model RedenUitstroom"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | RedenUitstroom |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | arjen |
    | version | 1.1.0 |
    | created | 2025-04-23 16:18:22 |
    | modified | 2025-08-06 14:19:41 |
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
| CBS-code | CharacterString |  |
| CBS-omschrijving | CharacterString |  |
| einddatumGeldigheid | Date |  |
| omschrijving | CharacterString |  |
| redenUitstroomCode | CharacterString |  |



### Regeling
> **Definitie Regeling:** 
>
> Een Regeling is gekoppeld aan een ingeschreven persoon (client) en beschrijft de specifieke afspraken of voorwaarden waaronder inkomensondersteuning wordt verleend. Een regeling heeft altijd een relatie met een RegelingSoort, die het type regeling specificeert.

??? info "Kenmerken Model Regeling"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Regeling |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron | [https://www.begrippenxl.nl/dso/nl/page/Regeling](https://www.begrippenxl.nl/dso/nl/page/Regeling) |
    | author | crossover |
    | version | 1.1.0 |
    | created | 2018-04-23 11:56:16 |
    | modified | 2025-08-06 14:19:41 |
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
| einddatum | Date |  |
| omschrijving | CharacterString |  |
| startdatum | Date |  |
| toekenningsdatum | Date |  |



### Regelingsoort
> **Definitie Regelingsoort:** 
>
> Typologie van een regeling

??? info "Kenmerken Model Regelingsoort"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Regelingsoort |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | crossover |
    | version | 1.1.0 |
    | created | 2018-04-23 11:56:27 |
    | modified | 2025-08-06 14:19:41 |
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
| naam | CharacterString |  |
| omschrijving | CharacterString |  |



### UitkeringsRun
> **Definitie UitkeringsRun:** 
>
> Geen Definitie

??? info "Kenmerken Model UitkeringsRun"
    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | UitkeringsRun |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | aashkpour |
    | version | 1.1.0 |
    | created | 2022-06-08 14:20:23 |
    | modified | 2025-08-06 14:19:41 |
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
| frequentie | CharacterString |  |
| periodeRun | CharacterString |  |
| soortRun | CharacterString |  |






## Enumeraties Model Inkomen


### Wet
Geen Definitie

Het enumeratie Wet kent de volgende waarden:

* **Niet van toepassing**: 
* **Wmo**: 
* **Jeugdwet**: dere
* **Andere wet**: 
* **Leeg**: 
* **Onbekend**: 
* **Participatiewet PW-I**: 
* **I.O.A.W./I.O.A.Z.**: 
* **Bijzondere Bijstand**: 


De enumeratie Wet heeft de volgende kenmerken:

??? info "Kenmerken Model Wet"
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
    | id | EAID_917acd0d_ab0f_46cb_a47c_c694cbb79ea6 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    



