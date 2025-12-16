# Model Archeologie
## Inleiding
> **Definitie Model Archeologie:** 
>
> Het informatiedomein dat gegevens omvat over archeologische opgravingen, onderzoeken en besluitvorming, gericht op het behoud, de bescherming en de ontsluiting van archeologisch erfgoed binnen de kaders van de Erfgoedwet.

??? info "Kenmerken Model Model Archeologie"

    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | Model Archeologie |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.4 |
    | created | 2018-06-06 14:59:46 |
    | modified | 2025-03-27 15:28:35 |
    | id | EAPK\_BB091186\_D934\_4ff7\_8B95\_F086954A45F5 |
    

Het model 'Model Archeologie' kent de volgende objecttypen:

* **Archeologiebesluit**: Een professioneel oordeel dat gebaseerd is op algemeen aanvaarde wetenschap ten aanzien van de archeologie
* **Artefact**: De benaming voor ieder verplaatsbaar object dat door de mens is vervaardigd, bewerkt en/of gebruikt.
* **Artefactsoort**: Typering van artefacten
* **boring**: 
> Een verticale grondmonstername binnen een project
> De gegevens over het geheel van activiteiten, voor zover relevant voor het onderzoek, dat tot doel heeft door boren een gat in de ondergrond te maken om monsters uit de ondergrond te nemen en/of metingen aan de ondergrond te doen.
> Een middel om door boren of steken toegang te krijgen tot de ondergrond om bijvoorbeeld geroerde en/of ongeroerde monsters aan de ondergrond te ontlenen voor nader onderzoek.
* **Doos**: Een afsluitbaar object waar iets in wordt opgeborgen of verpakt.
* **Kaart**: De geografische weergave van een gedeelte van het aardoppervlak
* **locatie**: Een specifieke plaats
* **Magazijnlocatie**: Locatie van een magazijn
* **Magazijnplaatsing**: Het ergens neerzetten van een object in een magazijn.
* **Project**: Geheel van activiteiten uitgevoerd in een tijdelijk samenwerkingsverband gericht op het binnen bepaalde randvoorwaarden (bv. tijd, geld) bereiken van een vooraf gedefinieerd resultaat.
* **Put**: Grondspoor, veelal verstevigd en gefundeerd aangelegd, bedoeld voor de tijdelijke opslag van danwel water (waterput) danwel uitwerpselen en afval (beerput).
* **Spoor**: Een blijk van eerdere aanwezigheid.
* **Stelling**: Een systeem om goederen op te slaan die worden vervoerd en opgeslagen op pallets, in bundels of per stuk.(Wikipedia)
* **Vindplaats**: Een plek waar men iets gevonden heeft.
* **Vlak**: Plat, oneindig oppervlak of variëteit zonder enige kromming.
* **Vondst**: Overblijfsel, voorwerp of ander spoor van menselijke aanwezigheid in het verleden afkomstig van een archeologisch monument
* **Vulling**: Dunne wegeringsplank gebruikt om de ruimte tussen de bovenste kimweger en de onderste balkweger op te vullen (Sopers, 1974).


## Objecttypen Model Archeologie


### Archeologiebesluit
> **Definitie Archeologiebesluit:** 
>
> Een professioneel oordeel dat gebaseerd is op algemeen aanvaarde wetenschap ten aanzien van de archeologie

??? info "Kenmerken Model Archeologiebesluit"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Archeologiebesluit |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.11.0 |
    | created | 2018-06-06 15:56:31 |
    | modified | 2025-12-16 10:28:33 |
    | id | EAID\_836E51BF\_65E9\_4482\_B555\_C9AB737D264D |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Archeologiebesluit |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-6df26100-0a75-447d-a8f1-5a87adeea7ef](https://gemmaonline.nl/index.php/GEMMA/id-6df26100-0a75-447d-a8f1-5a87adeea7ef) |
    | gemma_definitie | Een professioneel oordeel dat gebaseerd is op algemeen aanvaarde wetenschap ten aanzien van de archeologie |
    | gemma_toelichting |  |
    

Attributen van objecttype Archeologiebesluit

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Artefact
> **Definitie Artefact:** 
>
> De benaming voor ieder verplaatsbaar object dat door de mens is vervaardigd, bewerkt en/of gebruikt.

??? info "Kenmerken Model Artefact"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Artefact |
    | toelichting |  |
    | synoniemen | artefacten, voorwerp, voorwerpen |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.10.0 |
    | created | 2018-11-26 16:14:39 |
    | modified | 2025-12-16 10:28:33 |
    | id | EAID\_2C230EE7\_036D\_48be\_B82A\_FF45598170F7 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Artefact |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-7f936c4f-360e-47a3-a558-1682d8cfbf1a](https://gemmaonline.nl/index.php/GEMMA/id-7f936c4f-360e-47a3-a558-1682d8cfbf1a) |
    | gemma_definitie | De benaming voor ieder verplaatsbaar object dat door de mens is vervaardigd, bewerkt en/of gebruikt. |
    | gemma_toelichting |  |
    

Attributen van objecttype Artefact

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| projectCD | AN20 |  |
| putnummer | AN20 |  |
| vondstnummer | An20 |  |
| artefectnummer | AN20 |  |
| datering | AN40 |  |
| maten | AN80 |  |
| type | AN80 |  |
| beschrijving | text |  |
| determinatieniveau | AN40 |  |
| naam | AN40 |  |
| doosnummer | AN40 |  |
| tekeningnummer | AN200 |  |
| dianummer | AN200 |  |
| fotonummer | AN200 |  |
| restauratieWenselijk | boolean |  |
| exposabel | boolean |  |
| conserveren | boolean |  |
| key | AN40 |  |
| keyPut | AN40 |  |
| keyMagazijnplaatsing | AN40 |  |
| keyDoos | AN40 |  |
| dateringComplex | AN20 |  |
| opmerkingen | text |  |
| functie | AN80 |  |
| origine | An80 |  |
| literatuur | AN200 |  |
| herkomst | AN80 |  |
| keyVondst | An40 |  |



### Artefactsoort
> **Definitie Artefactsoort:** 
>
> Typering van artefacten

??? info "Kenmerken Model Artefactsoort"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Artefactsoort |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.11.0 |
    | created | 2018-06-06 15:02:51 |
    | modified | 2025-12-16 10:28:33 |
    | id | EAID\_67CF25EB\_EBB0\_4185\_8171\_1F9DD3B5D212 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Artefactsoort

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| code | AN8 |  |
| naam | AN200 |  |
| omschrijving | text |  |



### boring
> **Definitie boring:** 
>
> 
> Een verticale grondmonstername binnen een project
> De gegevens over het geheel van activiteiten, voor zover relevant voor het onderzoek, dat tot doel heeft door boren een gat in de ondergrond te maken om monsters uit de ondergrond te nemen en/of metingen aan de ondergrond te doen.
> Een middel om door boren of steken toegang te krijgen tot de ondergrond om bijvoorbeeld geroerde en/of ongeroerde monsters aan de ondergrond te ontlenen voor nader onderzoek.

??? info "Kenmerken Model boring"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | boring |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.13.0 |
    | created | 2018-06-06 15:17:02 |
    | modified | 2025-12-16 10:28:33 |
    | id | EAID\_E11FDCA7\_7538\_4353\_83FF\_72164D928452 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Boring |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-6897cf81-2661-4676-80b2-588cb1f4e42d](https://gemmaonline.nl/index.php/GEMMA/id-6897cf81-2661-4676-80b2-588cb1f4e42d) |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype boring

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Doos
> **Definitie Doos:** 
>
> Een afsluitbaar object waar iets in wordt opgeborgen of verpakt.

??? info "Kenmerken Model Doos"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Doos |
    | toelichting | Een doos bestaat meestal uit gevouwen karton, eventueel met lijm of plakband dichtgezet. In deze vorm heeft het vaak de vorm van een balk. Met een doos wordt meestal een grote kartonnen doos bedoeld, met geen andere functie dan verpakking of opslag. Voorb |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.11.0 |
    | created | 2018-11-21 22:07:15 |
    | modified | 2025-12-16 10:28:33 |
    | id | EAID\_703CAFCF\_FDC0\_4861\_AA76\_1692303DE7BE |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Doos

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| projectCD | AN40 |  |
| doosnummer | An40 |  |
| inhoud | text |  |
| herkomst | AN200 |  |
| key | AN40 |  |
| keyMagazijnlocatie | AN40 |  |



### Kaart
> **Definitie Kaart:** 
>
> De geografische weergave van een gedeelte van het aardoppervlak

??? info "Kenmerken Model Kaart"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Kaart |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.11.0 |
    | created | 2018-06-06 16:12:42 |
    | modified | 2025-12-16 10:28:33 |
    | id | EAID\_F28DDE36\_7BE4\_45f7\_A820\_FFF0261CAA4E |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Kaart |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-21a5d5b7-69f0-4501-98db-0655c44136b1](https://gemmaonline.nl/index.php/GEMMA/id-21a5d5b7-69f0-4501-98db-0655c44136b1) |
    | gemma_definitie | De geografische weergave van een gedeelte van het aardoppervlak |
    | gemma_toelichting |  |
    

Attributen van objecttype Kaart

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| naam | AN200 |  |
| omschrijving | text |  |
| kaart | BLOB |  |



### locatie
> **Definitie locatie:** 
>
> Een specifieke plaats

??? info "Kenmerken Model locatie"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | locatie |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.13.0 |
    | created | 2018-06-06 15:08:13 |
    | modified | 2025-12-16 10:28:33 |
    | id | EAID\_F25EE5A8\_2CF4\_498b\_8DAD\_8EEE48FAF3A5 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Locatie |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-ede94eee-d934-40f8-adcc-dc4b1703d333](https://gemmaonline.nl/index.php/GEMMA/id-ede94eee-d934-40f8-adcc-dc4b1703d333) |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype locatie

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| locatie | Point |  |



### Magazijnlocatie
> **Definitie Magazijnlocatie:** 
>
> Locatie van een magazijn

??? info "Kenmerken Model Magazijnlocatie"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Magazijnlocatie |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.11.0 |
    | created | 2019-02-05 16:18:27 |
    | modified | 2025-12-16 10:28:33 |
    | id | EAID\_4C1543FD\_250B\_4291\_9B23\_BC9D3D9C0C4A |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Magazijnlocatie |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-ba16f72b-26d0-4f28-be3d-68a3155dca65](https://gemmaonline.nl/index.php/GEMMA/id-ba16f72b-26d0-4f28-be3d-68a3155dca65) |
    | gemma_definitie | Locatie van een magazijn |
    | gemma_toelichting |  |
    

Attributen van objecttype Magazijnlocatie

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| vaknummer | AN8 |  |
| volgletter | AN8 |  |
| key | AN20 |  |
| stelling | AN8 |  |



### Magazijnplaatsing
> **Definitie Magazijnplaatsing:** 
>
> Het ergens neerzetten van een object in een magazijn.

??? info "Kenmerken Model Magazijnplaatsing"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Magazijnplaatsing |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.11.0 |
    | created | 2019-02-05 16:22:28 |
    | modified | 2025-12-16 10:28:33 |
    | id | EAID\_F954FB72\_AE88\_4a0e\_A3D8\_555FCF8D9C9F |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | MagazijnPlaatsing |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-b46a7928-928b-4ad4-9c27-f3d112073ea0](https://gemmaonline.nl/index.php/GEMMA/id-b46a7928-928b-4ad4-9c27-f3d112073ea0) |
    | gemma_definitie | Het ergens neerzetten van een object in een magazijn. |
    | gemma_toelichting |  |
    

Attributen van objecttype Magazijnplaatsing

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| uitgeleend | boolean |  |
| beschrijving | Text |  |
| datumGeplaatst | Date |  |
| key | AN40 |  |
| keyDoos | AN40 |  |
| keyMagazijnlocatie | AN40 |  |
| projectCD | An40 |  |
| herkomst | AN250 |  |



### Project
> **Definitie Project:** 
>
> Geheel van activiteiten uitgevoerd in een tijdelijk samenwerkingsverband gericht op het binnen bepaalde randvoorwaarden (bv. tijd, geld) bereiken van een vooraf gedefinieerd resultaat.

??? info "Kenmerken Model Project"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Project |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.11.0 |
    | created | 2018-06-06 15:00:39 |
    | modified | 2025-12-16 10:28:33 |
    | id | EAID\_E42A32F7\_262F\_4005\_9EB9\_4674B76E8825 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Project |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-8d356375-d2fe-4939-8ed7-f1403fa8c96e](https://gemmaonline.nl/index.php/GEMMA/id-8d356375-d2fe-4939-8ed7-f1403fa8c96e) |
    | gemma_definitie | Geheel van activiteiten uitgevoerd in een tijdelijk samenwerkingsverband gericht op het binnen bepaalde randvoorwaarden (bv. tijd, geld) bereiken van een vooraf gedefinieerd resultaat. |
    | gemma_toelichting |  |
    

Attributen van objecttype Project

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| projectCD | AN40 |  |
| naam | AN80 |  |
| datumStart | Date |  |
| datumEinde | Date |  |
| naamcode | AN40 |  |
| toponiem | AN80 |  |
| locatie | Point |  |
| coordinaten | Point |  |
| jaarVan | N4 |  |
| jaarTot | N4 |  |
| trefwoorden | AN250 |  |



### Put
> **Definitie Put:** 
>
> Grondspoor, veelal verstevigd en gefundeerd aangelegd, bedoeld voor de tijdelijke opslag van danwel water (waterput) danwel uitwerpselen en afval (beerput).

??? info "Kenmerken Model Put"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Put |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.11.0 |
    | created | 2018-06-06 15:01:44 |
    | modified | 2025-12-16 10:28:33 |
    | id | EAID\_17286CE1\_21F2\_454b\_95A6\_3E4C0C6E2453 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Put |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-6ace770c-ac42-4d79-bd84-145f77968360](https://gemmaonline.nl/index.php/GEMMA/id-6ace770c-ac42-4d79-bd84-145f77968360) |
    | gemma_definitie | Grondspoor, veelal verstevigd en gefundeerd aangelegd, bedoeld voor de tijdelijke opslag van danwel water (waterput) danwel uitwerpselen en afval (beerput). |
    | gemma_toelichting |  |
    

Attributen van objecttype Put

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| projectCD | AN40 |  |
| putnummer | AN40 |  |
| key | AN40 |  |



### Spoor
> **Definitie Spoor:** 
>
> Een blijk van eerdere aanwezigheid.

??? info "Kenmerken Model Spoor"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Spoor |
    | toelichting | In enge zin is het een afdruk in de grond, bijvoorbeeld van schoenen, voeten, poten of banden. Meer algemeen worden ook andere veranderingen op een locatie of route sporen genoemd, en, nog algemener, ook andere aanwijzingen voor te achterhalen informatie. |
    | synoniemen | Overblijfsel |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.10.0 |
    | created | 2018-06-06 15:02:07 |
    | modified | 2025-12-16 10:28:33 |
    | id | EAID\_14939C33\_2DCE\_41bf\_A2BE\_FF1EDD292FE7 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Spoor |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-3f6a41fd-293f-4f84-a449-1daa26b8a757](https://gemmaonline.nl/index.php/GEMMA/id-3f6a41fd-293f-4f84-a449-1daa26b8a757) |
    | gemma_definitie | Een blijk van eerdere aanwezigheid. |
    | gemma_toelichting | In enge zin is het een afdruk in de grond, bijvoorbeeld van schoenen, voeten, poten of banden. Meer algemeen worden ook andere veranderingen op een locatie of route sporen genoemd, en, nog algemener, ook andere aanwijzingen voor te achterhalen informatie. |
    

Attributen van objecttype Spoor

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| projectCD | AN40 |  |
| putnummer | AN40 |  |
| vlaknummer | AN40 |  |
| spoornummer | AN40 |  |
| hoogteBoven | AN20 |  |
| hoogteOnder | AN20 |  |
| aard | AN80 |  |
| datering | AN20 |  |
| datum | Date |  |
| vorm | AN20 |  |
| beschrijving | text |  |
| key | AN40 |  |
| keyVlak | AN40 |  |



### Stelling
> **Definitie Stelling:** 
>
> Een systeem om goederen op te slaan die worden vervoerd en opgeslagen op pallets, in bundels of per stuk.(Wikipedia)

??? info "Kenmerken Model Stelling"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Stelling |
    | toelichting |  |
    | synoniemen | Stellingkast |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.10.0 |
    | created | 2018-11-21 22:06:59 |
    | modified | 2025-12-16 10:28:33 |
    | id | EAID\_382D408F\_41A3\_49d2\_9F66\_DFFA6C75590D |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Stelling

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| stellingcode | AN2 |  |
| inhoud | text |  |



### Vindplaats
> **Definitie Vindplaats:** 
>
> Een plek waar men iets gevonden heeft.

??? info "Kenmerken Model Vindplaats"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Vindplaats |
    | toelichting |  |
    | synoniemen | Vindplaatsen |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.10.0 |
    | created | 2018-11-21 22:13:10 |
    | modified | 2025-12-16 10:28:33 |
    | id | EAID\_84DED9A9\_2D33\_4a77\_94F2\_29657024590F |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Vindplaats |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-d4ab4c0d-d752-4d86-ad6a-2ac25ec6af6b](https://gemmaonline.nl/index.php/GEMMA/id-d4ab4c0d-d752-4d86-ad6a-2ac25ec6af6b) |
    | gemma_definitie | Een plek waar men iets gevonden heeft. |
    | gemma_toelichting |  |
    

Attributen van objecttype Vindplaats

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| projectcode | AN20 |  |
| locatie | Point |  |
| vindplaats | AN40 |  |
| gemeente | AN40 |  |
| datering | AN40 |  |
| begindatering | AN40 |  |
| einddatering | AN40 |  |
| aard | AN20 |  |
| onderzoek | text |  |
| mobilia | AN40 |  |
| depot | AN40 |  |
| documentatie | AN200 |  |
| bibliografie | AN200 |  |
| beschrijving | text |  |



### Vlak
> **Definitie Vlak:** 
>
> Plat, oneindig oppervlak of variëteit zonder enige kromming.

??? info "Kenmerken Model Vlak"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Vlak |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.11.0 |
    | created | 2018-06-06 15:01:55 |
    | modified | 2025-12-16 10:28:33 |
    | id | EAID\_0644BD52\_8C2B\_462d\_94B9\_9C99908952F5 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Vlak |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-c74cb377-1926-4afd-a50d-14b2643b04b2](https://gemmaonline.nl/index.php/GEMMA/id-c74cb377-1926-4afd-a50d-14b2643b04b2) |
    | gemma_definitie | Plat, oneindig oppervlak of vari√´teit zonder enige kromming. |
    | gemma_toelichting |  |
    

Attributen van objecttype Vlak

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| projectCD | AN20 |  |
| putnummer | AN20 |  |
| vlaknummer | AN20 |  |
| diepteVan | N3 |  |
| diepteTot | N3 |  |
| key | AN40 |  |
| keyPut | AN40 |  |



### Vondst
> **Definitie Vondst:** 
>
> Overblijfsel, voorwerp of ander spoor van menselijke aanwezigheid in het verleden afkomstig van een archeologisch monument

??? info "Kenmerken Model Vondst"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Vondst |
    | toelichting |  |
    | synoniemen | Archeologische vondst |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.10.0 |
    | created | 2018-06-06 15:02:35 |
    | modified | 2025-12-16 10:28:33 |
    | id | EAID\_F8283401\_70F8\_41b8\_A97C\_32A9074AD4B1 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Vondst |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-fc805177-e231-40eb-8f59-0fb3bdc896a1](https://gemmaonline.nl/index.php/GEMMA/id-fc805177-e231-40eb-8f59-0fb3bdc896a1) |
    | gemma_definitie | Overblijfsel, voorwerp of ander spoor van menselijke aanwezigheid in het verleden afkomstig van een archeologisch monument |
    | gemma_toelichting |  |
    

Attributen van objecttype Vondst

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| projectCD | AN20 |  |
| vondstnummer | AN20 |  |
| putnummer | AN20 |  |
| vlaknummer | AN20 |  |
| spoornummer | AN20 |  |
| vullingnummer | AN20 |  |
| omstandigheden | text |  |
| omschrijving | text |  |
| key | AN40 |  |
| keyVulling | AN40 |  |
| datum | Date |  |
| XCoordinaat | int |  |
| YCoordinaat | int |  |



### Vulling
> **Definitie Vulling:** 
>
> Dunne wegeringsplank gebruikt om de ruimte tussen de bovenste kimweger en de onderste balkweger op te vullen (Sopers, 1974).

??? info "Kenmerken Model Vulling"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Vulling |
    | toelichting |  |
    | synoniemen | Vullingen (plank) |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.10.0 |
    | created | 2018-06-06 15:02:19 |
    | modified | 2025-12-16 10:28:33 |
    | id | EAID\_8417459E\_2193\_44a2\_A1AC\_38C39EA93CBF |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Vulling |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-f7d73677-6a8a-4921-acfc-590e3bf6cb26](https://gemmaonline.nl/index.php/GEMMA/id-f7d73677-6a8a-4921-acfc-590e3bf6cb26) |
    | gemma_definitie | Dunne wegeringsplank gebruikt om de ruimte tussen de bovenste kimweger en de onderste balkweger op te vullen (Sopers, 1974). |
    | gemma_toelichting |  |
    

Attributen van objecttype Vulling

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| projectCD | AN20 |  |
| putnummer | An20 |  |
| vlaknummer | AN20 |  |
| spoornummer | AN20 |  |
| vullingnummer | AN20 |  |
| grondsoort | AN80 |  |
| kleur | AN80 |  |
| structuur | AN80 |  |
| key | AN40 |  |
| keySpoor | AN40 |  |




