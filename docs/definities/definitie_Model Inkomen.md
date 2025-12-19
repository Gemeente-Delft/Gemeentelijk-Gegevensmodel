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
    | author | Arjen Brienen |
    | version | 1.8.0 |
    | created | 2025-03-27 11:31:16 |
    | modified | 2025-12-18 15:38:53 |
    | id | EAPK\_7A13550B\_AC75\_4783\_BD16\_A9ED6E86172A |
    

Het model 'Model Inkomen' kent de volgende objecttypen:

* **Component**: Een *inkomenscomponent* is een afzonderlijk onderdeel of bron van inkomen, zoals loon, winst uit onderneming, uitkeringen of andere inkomensbronnen, die samen het totale inkomen van een persoon of huishouden vormen.
* **ComponentSoort**: *ComponentSoort* is de classificatie of het type van een inkomenscomponent binnen een inkomen- of financiële administratie, waarmee wordt bepaald welke categorie of soort een specifieke component behoort.
* **Huisvestingsoort**: Als de dienst een uitkering betreft die periodiek wordt uitgekeerd, kan om redenen de betaling worden geblokkeerd. Reden toevoeging: Geeft de reden van blokkering van de uitkering aan. Als de dienst een uitkering betreft, die periodiek wordt uitgekeerd, kan om redenen de betaling worden geblokkeerd. De betalingsblokkade wordt opgenomen bij de dienst, die wordt genoten door de client en partner van de client. Nodig voor diepere analyse van stand van uitkeringen. Hoeveel uitkleringen hebben we geblokkeerd op dit moment omdat we de uitkering gaan beindigen.
* **Inkomensvoorziening**: Een regeling die zorg draag voor een inkomen confom de landelijke wetgeving
* **Inkomensvoorzieningsoort**: Typering van een inkomensvoorziening
* **RedenBlokkering**: Als de dienst een uitkering betreft die periodiek wordt uitgekeerd, kan om redenen de betaling worden geblokkeerd. Reden toevoeging: Geeft de reden van blokkering van de uitkering aan. Als de dienst een uitkering betreft, die periodiek wordt uitgekeerd, kan om redenen de betaling worden geblokkeerd. De betalingsblokkade wordt opgenomen bij de dienst, die wordt genoten door de client en partner van de client. Nodig voor diepere analyse van stand van uitkeringen. Hoeveel uitkleringen hebben we geblokkeerd op dit moment omdat we de uitkering gaan beindigen.
* **RedenInstroom**: De reden waarom de persoon de uitkering heeft gekregen. Geeft de reden van aanvraag van uitkering weer. Nodig voor diepere analyse van stand van uitkeringen. Omdat we willen weten waarom mensen nstromen. Bv geen werk meer og geen andere uitkering, verhuizing.
* **RedenUitstroom**: De reden waarom de uitkering aan een persoon is beeindgd. Reden toevoeging: Geeft de reden van uitstroom aan. Waarom is de uitkering beëindigd. Nodig voor diepere analyse van stand. Meet of je beleid of het lukt om mensen naar werk te laten stromen. van uitkeringen.
* **Regeling**: Een Regeling is gekoppeld aan een ingeschreven persoon (client) en beschrijft de specifieke afspraken of voorwaarden waaronder inkomensondersteuning wordt verleend. Een regeling heeft altijd een relatie met een RegelingSoort, die het type regeling specificeert.
* **Regelingsoort**: Typologie van een regeling
* **UitkeringsRun**: Een *UitkeringsRun* is een geautomatiseerde verwerking in een financieel of administratief systeem waarbij **een groep uitkeringen of betalingen tegelijk wordt berekend en uitgevoerd** als onderdeel van een periodieke batch-verwerking.


## Objecttypen Model Inkomen


### Component
> **Definitie Component:** 
>
> Een *inkomenscomponent* is een afzonderlijk onderdeel of bron van inkomen, zoals loon, winst uit onderneming, uitkeringen of andere inkomensbronnen, die samen het totale inkomen van een persoon of huishouden vormen.

??? info "Kenmerken Model Component"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Component |
    | toelichting | In inkomensstatistiek wordt inkomen vaak opgebouwd uit verschillende componenten (zoals arbeid, uitkeringen, kapitaalinkomen, etc.), waarbij elke component een \*\*bron of type inkomen\*\* vertegenwoordigt. Door inkomens te decomponeren in componenten kan worden geanalyseerd welke bronnen bijdragen aan het totaalinkomen en hoe deze bijdragen variëren tussen personen of groepen. Dit wordt bijvoorbeeld gebruikt bij de berekening van inkomensdistributies en armoedestatistieken. |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Ashkan Ashkpour |
    | version | 1.10.0 |
    | created | 2022-06-08 14:19:54 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_F4FD02F2\_9FFA\_4a35\_BA32\_B4CDE4002E7A |
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
| eindatumBetrekkingop | Date |  |
| debetCredit | CharacterString |  |
| rekeningNummer | CharacterString |  |
| grootboekcode | CharacterString |  |
| grootboekomschrijving | CharacterString |  |
| kostenplaats | CharacterString |  |
| groep | CharacterString |  |
| omschrijving | CharacterString |  |
| toelichting | CharacterString |  |
| groepcode | CharacterString |  |



### ComponentSoort
> **Definitie ComponentSoort:** 
>
> *ComponentSoort* is de classificatie of het type van een inkomenscomponent binnen een inkomen- of financiële administratie, waarmee wordt bepaald welke categorie of soort een specifieke component behoort.

??? info "Kenmerken Model ComponentSoort"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | ComponentSoort |
    | toelichting | In gegevensmodellen zoals het \*\*Gemeentelijk Gegevensmodel (GGM)\*\* maakt \*ComponentSoort\* het mogelijk inkomens- of financiële componenten verder te categoriseren. Dit helpt bij het structureren, analyseren en rapporteren van verschillende inkomensposten of kosten- en opbrengstelementen binnen inkomensvoorzieningen. \*ComponentSoort\* bevat onder meer codes en omschrijvingen die aangeven \*\*wat voor soort component\*\* het is (bijvoorbeeld een bepaalde soort inkomen of uitgave binnen een dienst- of inkomensadministratie). |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Ashkan Ashkpour |
    | version | 1.10.0 |
    | created | 2022-06-08 14:20:08 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_3372192D\_4773\_46b2\_BDA5\_C98B220F8954 |
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
| regelingcode | CharacterString |  |
| regeling | CharacterString |  |
| kolom | CharacterString |  |
| kolomcode | CharacterString |  |
| componentcode | CharacterString |  |
| omschrijving | CharacterString |  |



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
    | author | Arjen Brienen |
    | version | 1.10.0 |
    | created | 2025-04-23 16:21:20 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_8D999BE8\_96AB\_8418\_B94F\_289754CE1336 |
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
    | author | Arjen Brienen |
    | version | 1.10.0 |
    | created | 2018-04-23 11:53:14 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_07784236\_3AA6\_45e5\_8253\_7D088C4020B0 |
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
| ingangsdatum | Date |  |
| einddatum | Date |  |
| toekenningsdatum | Date |  |
| bedrag | Bedrag |  |
| eenmalig | Boolean |  |
| groep | CharacterString |  |
| administratieveEinddatum | Date |  |
| administratieveStartdatum | Date |  |
| betalingsmomentcode | CharacterString |  |
| code | CharacterString |  |
| datumToekenning | Date |  |
| indicatieBlokkering | Boolean |  |
| indicatieStudietoeslag | Boolean |  |
| indicatieUitkeringSplitsen | Boolean |  |
| indicatieUitkeringsspecificatie | Boolean |  |
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
    | author | Arjen Brienen |
    | version | 1.10.0 |
    | created | 2018-04-23 11:53:23 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_AF18E7D3\_279D\_4323\_B785\_6C75B4701430 |
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
| naam | CharacterString |  |
| omschrijving | CharacterString |  |
| wet | Enumeratie: "Wet" |  |
| vergoeding | CharacterString |  |
| vergoedingscode | CharacterString |  |
| regeling | CharacterString |  |
| regelingscode | CharacterString |  |
| code | CharacterString |  |



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
    | author | Arjen Brienen |
    | version | 1.10.0 |
    | created | 2025-04-23 16:14:37 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_88B0A7AB\_53E6\_4bc1\_8D99\_9BE896AB8418 |
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
    | author | Arjen Brienen |
    | version | 1.10.0 |
    | created | 2025-04-23 16:16:48 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_8D999BE8\_96AB\_8418\_99A2\_CB86335AFB97 |
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
| omschrijving | CharacterString |  |
| redenInstroomCode | CharacterString |  |
| CBS-code | CharacterString |  |
| CBS-omschrijving | CharacterString |  |



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
    | author | Arjen Brienen |
    | version | 1.10.0 |
    | created | 2025-04-23 16:18:22 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_99A2CB86\_335A\_FB97\_9C8F\_47170B1699EC |
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
| omschrijving | CharacterString |  |
| redenUitstroomCode | CharacterString |  |
| CBS-code | CharacterString |  |
| CBS-omschrijving | CharacterString |  |



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
    | author | Arjen Brienen |
    | version | 1.10.0 |
    | created | 2018-04-23 11:56:16 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_C25455F3\_FEB0\_4c6d\_9AA4\_3B027718BEE3 |
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
| startdatum | Date |  |
| einddatum | Date |  |
| toekenningsdatum | Date |  |
| omschrijving | CharacterString |  |



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
    | author | Arjen Brienen |
    | version | 1.10.0 |
    | created | 2018-04-23 11:56:27 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_14D3C960\_5EF2\_433c\_8E1C\_B493974280E2 |
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
> Een *UitkeringsRun* is een geautomatiseerde verwerking in een financieel of administratief systeem waarbij **een groep uitkeringen of betalingen tegelijk wordt berekend en uitgevoerd** als onderdeel van een periodieke batch-verwerking.

??? info "Kenmerken Model UitkeringsRun"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | UitkeringsRun |
    | toelichting | In financiële systemen en salaris-/uitkeringsadministraties verwijst een \*run\* naar het \*\*proces van uitvoeren van een set berekeningen en betalingen\*\* op een gepland moment (bijv. maandelijks of wekelijks). Een \*uitkeringsrun\* omvat normaliter:<br>- het verzamelen van de gegevens van de uitkeringsgerechtigden;<br>- het toepassen van berekeningsregels (zoals hoogte, inhoudingen en rechten);<br>- het genereren van betaalopdrachten of journaling in het financiële systeem;<br>- en het klaarmaken of uitvoeren van de daadwerkelijke betaling.<br>Dit is vergelijkbaar met \*\*betaling- of payroll runs\*\* in financiële systemen waarmee organisaties periodiek meerdere betalingen bundelen en verwerken. |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Ashkan Ashkpour |
    | version | 1.10.0 |
    | created | 2022-06-08 14:20:23 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_F787184D\_3AA8\_4132\_96C4\_23A363C3C1B7 |
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
| periodeRun | CharacterString |  |
| soortRun | CharacterString |  |
| frequentie | CharacterString |  |






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
    | version | 1.10.0 |
    | created | 2025-03-26 11:12:49 |
    | modified | 2025-12-16 10:28:45 |
    | id | EAID\_25740629\_b165\_4552\_b924\_bc712190d540 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    


