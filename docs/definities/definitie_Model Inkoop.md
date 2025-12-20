# Model Inkoop
## Inleiding
> **Definitie Model Inkoop:** 
>
> Dit subdomein bevat data over personeelsadministratie, werving en selectie, arbeidsvoorwaarden, opleidingen, verzuimregistratie en loopbaanontwikkeling. Het ondersteunt de organisatie bij het aantrekken, behouden en ontwikkelen van medewerkers en faciliteert processen zoals functioneringsgesprekken, personeelsplanning en compliance met arbeidswetgeving.

??? info "Kenmerken Model Model Inkoop"

    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | Model Inkoop |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.1 |
    | created | 2018-04-04 15:09:45 |
    | modified | 2025-03-27 15:28:35 |
    | id | EAPK\_254CDF37\_3AAB\_4e0b\_9F3C\_2B46AAEBE2E9 |
    

Het model 'Model Inkoop' kent de volgende objecttypen:

* **Aanbesteding**: Kan een (enkel of meervoudige) onderhandse aanbesteding, of een nationale of Europese aanbesteding
* **Aanbesteding Inhuur**: Aanbesteding voor inhuur van personen of diensten
* **Aankondiging**: Aankondiging van een Nationale of Europese aanbesteding
* **Aanvraag Inkooporder**: het betreft hier het formulier 'Aanvraag Inkooporder'
* **Categorie**: Categorie waarop leveranciers zich voor de levering van personeel voor kunnen kwalificeren
* **Contract**: Bindende overeenkomst
* **CPV-code**: De Common Procurement Vocabulary (CPV-codes) is een gemeenschappelijke woordenlijst van de EU, alle mogelijke soorten overheidsopdrachten voor diensten, leveringen en werken hebben een eigen code gekregen. Aanbestedende diensten moeten bij Europese aanbestedingen dit classificatiesysteem toepassen.
* **FormulierInhuur**: Formulier ten behoeve van inhuur personeel
* **FormulierVerlengingInhuur**: Formulier ten behoeve van verlenging inhuur personeel
* **Gunning**: 
> Gunning van een (enkel of meervoudige) onderhandse aanbesteding, of een nationale of Europese aanbesteding
> Of voor levering personeel
* **Inkooppakket**: Standaard indeling om de werken, diensten en leveringen die de aanbestedende dienst helpt bij het structureren van haar uitgaven. Samenhangende leveringen, diensten en producten zijn hierin gegroepeerd.
* **Inschrijving**: Inschrijving op een nationale of Europese aanbesteding
* **Kandidaat**: Iemand die een bepaalde baan of functie wil
* **Kwalificatie**: Kwalifificatie voor een nationale of europese aanbesteding
* **Leverancier**: Een niet-natuurlijk persoon die een product of dienst levert aan de organisatie
* **Offerte**: Aanbod, aanbieding of voorstel van goederen of diensten waarin opgave is gedaan van de prijs.
* **Offerteaanvraag**: Aanbesteding bij inschrijving
* **SelectietabelAanbesteding**: Gebaseerd op het procedureoverzicht inkoop. Hierin kan de tabel met drempelbedragen en bijbehorende procedures worden opgeslagen
* **StartformulierAanbesteden**: Formulier voor het starten van een aanbeseding
* **Uitnodiging**: Een verzoek om iets bij te wonen.


## Objecttypen Model Inkoop


### Aanbesteding
> **Definitie Aanbesteding:** 
>
> Kan een (enkel of meervoudige) onderhandse aanbesteding, of een nationale of Europese aanbesteding

??? info "Kenmerken Model Aanbesteding"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Aanbesteding |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-11-26 15:10:12 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_44EC6082\_2682\_43c7\_A52E\_0AD05B06A046 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Aanbesteding |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-bc6f065d-05c9-454d-a18d-1c0c2a2dfe15](https://gemmaonline.nl/index.php/GEMMA/id-bc6f065d-05c9-454d-a18d-1c0c2a2dfe15) |
    | gemma_definitie | Kan een (enkel of meervoudige) onderhandse aanbesteding, of een nationale of Europese aanbesteding |
    | gemma_toelichting |  |
    

Attributen van objecttype Aanbesteding

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| naam | AN200 |  |
| tendernedKenmerk | AN80 |  |
| status | AN80 |  |
| datumStart | Date |  |
| volgendeSluiting | DateTime |  |
| type | Opdrachtcategorie |  |
| procedure | Aanbestedingsoort |  |
| digitaal | Boolean |  |
| referentienummer | AN80 |  |
| datumPublicatie | DateTime |  |
| scoreMaximaal | int |  |



### Aanbesteding Inhuur
> **Definitie Aanbesteding Inhuur:** 
>
> Aanbesteding voor inhuur van personen of diensten

??? info "Kenmerken Model Aanbesteding Inhuur"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Aanbesteding Inhuur |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-11-26 15:14:45 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_01D90490\_C76A\_444a\_BFCE\_355AFC5FB012 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | AanbestedingInhuur |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-686c0af1-67b2-42a4-8690-060705617c13](https://gemmaonline.nl/index.php/GEMMA/id-686c0af1-67b2-42a4-8690-060705617c13) |
    | gemma_definitie | Aanbesteding voor inhuur van personen of diensten |
    | gemma_toelichting |  |
    

Attributen van objecttype Aanbesteding Inhuur

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| datumVerzending | DateTime |  |
| status | AN80 |  |
| titel | AN200 |  |
| type | Opdrachtcategorie |  |
| publicatie | AN80 |  |
| perceel | AN80 |  |
| datumSluiting | DateTime |  |
| aanvraagnummer | AN80 |  |
| omschrijving | text |  |
| hoogsteTarief | bedrag |  |
| laagsteTarief | bedrag |  |
| datumOpeningKluis | DateTime |  |
| datumCreatie | DateTime |  |
| referentie | AN80 |  |
| procedure | AN80 |  |
| projectreferentie | AN40 |  |
| projectnaam | AN200 |  |
| aanvraagGesloten | DateTime |  |
| fase | AN80 |  |



### Aankondiging
> **Definitie Aankondiging:** 
>
> Aankondiging van een Nationale of Europese aanbesteding

??? info "Kenmerken Model Aankondiging"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Aankondiging |
    | toelichting |  |
    | synoniemen | Kennisgeving, Bekendmaking |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.11.0 |
    | created | 2019-11-26 15:09:54 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_BB135B0E\_A2C2\_4681\_BD91\_30863F8B3D70 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Aankondiging |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-11a5fd2d-0237-4e70-b859-d1e26456553b](https://gemmaonline.nl/index.php/GEMMA/id-11a5fd2d-0237-4e70-b859-d1e26456553b) |
    | gemma_definitie | Aankondiging van een Nationale of Europese aanbesteding |
    | gemma_toelichting |  |
    

Attributen van objecttype Aankondiging

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| datum | DateTime |  |
| naam | An200 |  |
| beschrijving | text |  |
| type | Aanbestedingsoort |  |
| categorie | Opdrachtcategorie |  |



### Aanvraag Inkooporder
> **Definitie Aanvraag Inkooporder:** 
>
> het betreft hier het formulier 'Aanvraag Inkooporder'

??? info "Kenmerken Model Aanvraag Inkooporder"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Aanvraag Inkooporder |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-10-29 11:10:05 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_33E5EA10\_F43A\_4966\_B9C1\_875F0E2C1B52 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | AanvraagInkooporder |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-8d9233d7-dfb9-4b87-bab2-61631a632f95](https://gemmaonline.nl/index.php/GEMMA/id-8d9233d7-dfb9-4b87-bab2-61631a632f95) |
    | gemma_definitie | het betreft hier het formulier 'Aanvraag Inkooporder' |
    | gemma_toelichting |  |
    

Attributen van objecttype Aanvraag Inkooporder

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| correspondentienummer | int |  |
| onderwerp | AN80 |  |
| omschrijving | text |  |
| leveringOfDienst | Boolean | Bij levering of dienst is waarde: TRUE, bij een werk is waarde: FALSE |
| wijzeVanInhuur | AN80 |  |
| inhuurAnders | AN80 |  |
| betalingOverMeerJaren | Boolean |  |
| nettoTotaalBedrag | Bedrag |  |
| reactie | Text |  |
| status | AN80 |  |



### Categorie
> **Definitie Categorie:** 
>
> Categorie waarop leveranciers zich voor de levering van personeel voor kunnen kwalificeren

??? info "Kenmerken Model Categorie"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Categorie |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-11-26 15:16:32 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_6CA060D0\_C5AC\_4b50\_8B64\_00DCAEA7EF48 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Categorie

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| code | AN80 |  |
| omschrijving | AN300 |  |



### Contract
> **Definitie Contract:** 
>
> Bindende overeenkomst

??? info "Kenmerken Model Contract"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Contract |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-10-29 10:34:40 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_9FBF9FB8\_B28D\_4733\_8443\_607B8498F446 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Contract |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-f96af00f-2933-42d0-aacf-58ccb4a0ef52](https://gemmaonline.nl/index.php/GEMMA/id-f96af00f-2933-42d0-aacf-58ccb4a0ef52) |
    | gemma_definitie | Bindende overeenkomst |
    | gemma_toelichting |  |
    

Attributen van objecttype Contract

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| contractRevisie | int |  |
| internContractID | AN40 |  |
| internContractRevisie | int |  |
| status | AN80 |  |
| groep | AN80 |  |
| type | AN80 |  |
| categorie | AN80 |  |
| classificatie | AN80 |  |
| voorwaarde | AN80 |  |
| beschrijving | text |  |
| zoekwoorden | AN300 |  |
| autorisatiegroep | AN200 |  |
| opmerkingen | text |  |
| datumStart | Date |  |
| datumEinde | Date |  |
| datumCreatie | Date |  |



### CPV-code
> **Definitie CPV-code:** 
>
> De Common Procurement Vocabulary (CPV-codes) is een gemeenschappelijke woordenlijst van de EU, alle mogelijke soorten overheidsopdrachten voor diensten, leveringen en werken hebben een eigen code gekregen. Aanbestedende diensten moeten bij Europese aanbestedingen dit classificatiesysteem toepassen.

??? info "Kenmerken Model CPV-code"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | CPV-code |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-11-27 14:11:20 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_6A4CF470\_3B0E\_4141\_9DB6\_C9E8A525CB49 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | CPVCode |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-b6c26d6b-c773-4b50-ba03-a8463f23889a](https://gemmaonline.nl/index.php/GEMMA/id-b6c26d6b-c773-4b50-ba03-a8463f23889a) |
    | gemma_definitie | De Common Procurement Vocabulary (CPV-codes) is een gemeenschappelijke woordenlijst van de EU, alle mogelijke soorten overheidsopdrachten voor diensten, leveringen en werken hebben een eigen code gekregen. Aanbestedende diensten moeten bij Europese aanbes |
    | gemma_toelichting |  |
    

Attributen van objecttype CPV-code

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| code | AN80 |  |
| omschrijving | AN300 |  |



### FormulierInhuur
> **Definitie FormulierInhuur:** 
>
> Formulier ten behoeve van inhuur personeel

??? info "Kenmerken Model FormulierInhuur"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | FormulierInhuur |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-11-18 15:32:41 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_B598FF22\_CDD0\_486f\_B528\_99421D0FA608 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype FormulierInhuur

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| functienaamInhuur | AN200 |  |
| datumIngangInhuur | Date |  |
| akkoordHRAdviseur | Boolean |  |
| akkoordFinancieelAdviseur | Boolean |  |



### FormulierVerlengingInhuur
> **Definitie FormulierVerlengingInhuur:** 
>
> Formulier ten behoeve van verlenging inhuur personeel

??? info "Kenmerken Model FormulierVerlengingInhuur"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | FormulierVerlengingInhuur |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-11-18 15:34:04 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_1D87490A\_9F07\_424f\_BE6F\_5E9C11376B05 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype FormulierVerlengingInhuur

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| datumEindeNieuw | Date |  |
| indicatieVerhogenInkooporder | Boolean |  |
| indicatieRedenInhuurGewijzigd | Boolean |  |
| toelichting | text |  |



### Gunning
> **Definitie Gunning:** 
>
> 
> Gunning van een (enkel of meervoudige) onderhandse aanbesteding, of een nationale of Europese aanbesteding
> Of voor levering personeel

??? info "Kenmerken Model Gunning"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Gunning |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-11-26 15:11:46 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_3FB9B466\_D147\_42d7\_99D1\_2D14A007D16C |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Gunning |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-70e40543-6a99-433d-8a01-f4273e308410](https://gemmaonline.nl/index.php/GEMMA/id-70e40543-6a99-433d-8a01-f4273e308410) |
    | gemma_definitie | Gunning van een (enkel of meervoudige) onderhandse aanbesteding, of een nationale of Europese aanbesteding<br>Of voor levering personeel |
    | gemma_toelichting |  |
    

Attributen van objecttype Gunning

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| datumGunning | DateTime |  |
| bericht | AN300 |  |
| datumVoorlopigeGunning | DateTime |  |
| gegundePrijs | bedrag |  |
| datumPublicatie | DateTime |  |



### Inkooppakket
> **Definitie Inkooppakket:** 
>
> Standaard indeling om de werken, diensten en leveringen die de aanbestedende dienst helpt bij het structureren van haar uitgaven. Samenhangende leveringen, diensten en producten zijn hierin gegroepeerd.

??? info "Kenmerken Model Inkooppakket"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Inkooppakket |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Ashkan Ashkpour |
    | version | 1.12.0 |
    | created | 2020-11-12 16:59:28 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_170AF8F5\_8952\_407a\_91C4\_EAF910DE3304 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Inkooppakket

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| code | AN80 |  |
| naam | AN200 |  |
| type | Opdrachtcategorie |  |



### Inschrijving
> **Definitie Inschrijving:** 
>
> Inschrijving op een nationale of Europese aanbesteding

??? info "Kenmerken Model Inschrijving"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Inschrijving |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-11-26 15:11:11 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_2902E8D6\_FF16\_45d6\_A0A4\_47E2857D2D19 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Inschrijving |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-e1c425c1-a3fe-4144-907d-13da8d9fb5cc](https://gemmaonline.nl/index.php/GEMMA/id-e1c425c1-a3fe-4144-907d-13da8d9fb5cc) |
    | gemma_definitie | Inschrijving op een nationale of Europese aanbesteding |
    | gemma_toelichting |  |
    

Attributen van objecttype Inschrijving

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| datum | DateTime |  |
| prijs | Bedrag |  |
| score | int |  |



### Kandidaat
> **Definitie Kandidaat:** 
>
> Iemand die een bepaalde baan of functie wil

??? info "Kenmerken Model Kandidaat"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Kandidaat |
    | toelichting |  |
    | synoniemen | Gegadigde |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.11.0 |
    | created | 2019-11-27 10:37:40 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_75B4E818\_5ECD\_45c5\_98F9\_66F57FC6117E |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Kandidaat |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-dc97ebf4-61ee-47f6-a108-af6bb4a276f7](https://gemmaonline.nl/index.php/GEMMA/id-dc97ebf4-61ee-47f6-a108-af6bb4a276f7) |
    | gemma_definitie | Iemand die een bepaalde baan of functie wil |
    | gemma_toelichting |  |
    

Attributen van objecttype Kandidaat

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| datumIngestuurd | DateTime |  |



### Kwalificatie
> **Definitie Kwalificatie:** 
>
> Kwalifificatie voor een nationale of europese aanbesteding

??? info "Kenmerken Model Kwalificatie"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Kwalificatie |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-11-26 15:10:32 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_AB2AED85\_D2B0\_45cf\_9B1F\_C6005E894494 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Kwalificatie

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| startGeldigheid | Date |  |
| eindeGeldigheid | Date |  |



### Leverancier
> **Definitie Leverancier:** 
>
> Een niet-natuurlijk persoon die een product of dienst levert aan de organisatie

??? info "Kenmerken Model Leverancier"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Leverancier |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2018-05-29 13:54:06 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_EA7FE08E\_34F7\_45d2\_BE2E\_E4E3B8333BF3 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Leverancier |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-113af80a-7e3e-41f6-8f79-8d0d48c4c257](https://gemmaonline.nl/index.php/GEMMA/id-113af80a-7e3e-41f6-8f79-8d0d48c4c257) |
    | gemma_definitie | Een niet-natuurlijk persoon die een product of dienst levert aan de organisatie |
    | gemma_toelichting |  |
    

Attributen van objecttype Leverancier

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| naam | AN200 |  |
| nummer | AN40 |  |



### Offerte
> **Definitie Offerte:** 
>
> Aanbod, aanbieding of voorstel van goederen of diensten waarin opgave is gedaan van de prijs.

??? info "Kenmerken Model Offerte"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Offerte |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-11-27 13:29:18 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_BF21FFA3\_3EA6\_410a\_BC65\_7BE5547646B6 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Offerte |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-6d31df7d-b7f9-4f50-be9f-eaf05c697f6e](https://gemmaonline.nl/index.php/GEMMA/id-6d31df7d-b7f9-4f50-be9f-eaf05c697f6e) |
    | gemma_definitie | Aanbod, aanbieding of voorstel van goederen of diensten waarin opgave is gedaan van de prijs. |
    | gemma_toelichting |  |
    

Attributen van objecttype Offerte

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| prijs | bedrag |  |
| datumOfferte | Date |  |
| naam | AN200 |  |
| omschrijving | text |  |



### Offerteaanvraag
> **Definitie Offerteaanvraag:** 
>
> Aanbesteding bij inschrijving

??? info "Kenmerken Model Offerteaanvraag"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Offerteaanvraag |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-11-26 15:22:25 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_1EF1AC66\_9563\_4cdd\_AE78\_0878D651907A |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Offerteaanvraag |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-1b3c3c06-c7e9-40c0-8fa1-dbbc3c23152f](https://gemmaonline.nl/index.php/GEMMA/id-1b3c3c06-c7e9-40c0-8fa1-dbbc3c23152f) |
    | gemma_definitie | Aanbesteding bij inschrijving |
    | gemma_toelichting |  |
    

Attributen van objecttype Offerteaanvraag

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| datumAanvraag | Date |  |
| datumSluiting | date |  |
| naam | AN80 |  |
| omschrijving | text |  |



### SelectietabelAanbesteding
> **Definitie SelectietabelAanbesteding:** 
>
> Gebaseerd op het procedureoverzicht inkoop. Hierin kan de tabel met drempelbedragen en bijbehorende procedures worden opgeslagen

??? info "Kenmerken Model SelectietabelAanbesteding"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | SelectietabelAanbesteding |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-11-18 17:33:00 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_B2BD6C5B\_460E\_4f2a\_9B78\_3E101DAD8D6B |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype SelectietabelAanbesteding

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| opdrachtcategorie | Opdrachtcategorie |  |
| drempelbedragVanaf | Bedrag |  |
| drempelbedragTot | Bedrag |  |
| aanbestedingsoort | Aanbestedingsoort |  |
| openbaar | Boolean |  |



### StartformulierAanbesteden
> **Definitie StartformulierAanbesteden:** 
>
> Formulier voor het starten van een aanbeseding

??? info "Kenmerken Model StartformulierAanbesteden"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | StartformulierAanbesteden |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-11-18 15:32:13 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_7694A657\_22D8\_4b00\_AAE2\_A78EF014B43A |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype StartformulierAanbesteden

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| omschrijving | text |  |
| indicatorOverkoepelendProject | Boolean |  |
| opdrachtsoort | Opdrachtsoort |  |
| opdrachtcategorie | Opdrachtcategorie |  |
| indicatieEenmaligeLos | Boolean |  |
| indicatieMeerjarigRepeterend | Boolean |  |
| indicatieMeerjarigeRaamovereenkomst | boolean |  |
| toelichtingEenmaligOfRepeterend | text |  |
| indicatieAanvullendeOpdrachtLeverancier | boolean |  |
| toelichtingAanvullendeOpdracht | text | Zijn er mogelijk nog aanvullende of gerelateerde opdrachten, die je ook wilt verstrekken aan de beoogde opdrachtnemer? |
| beoogdeLooptijd | int | Beoogde looptijd in jaren |
| beoogdeTotaleOpdrachtwaarde | Bedrag |  |
| indicatieBeoogdeAanbestedingOnderhands | Boolean | Welke aanbestedingsprocedure ben je voornemens te volgen?<br>1. 1-op-1 (enkelvoudig onderhands) of 3 tot 5 offertes (meervoudig onderhands)<br>2. Nationale of Europese aanbesteding |
| indicatieBeoogdeProcKomtOvereen | boolean | Komt - op basis van de hierboven genoemde totale opdrachtwaarde - de beoogde aanbestedings-procedure overeen met de voorgeschreven procedure uit het Procedure-overzicht en/of het 'groene' gedeelte in de kleurentabel uit de gids proportionaliteit? |



### Uitnodiging
> **Definitie Uitnodiging:** 
>
> Een verzoek om iets bij te wonen.

??? info "Kenmerken Model Uitnodiging"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Uitnodiging |
    | toelichting |  |
    | synoniemen | Invitatie |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.11.0 |
    | created | 2019-11-27 14:27:00 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_BB182A6F\_6935\_4702\_ABEA\_B96E32A40B02 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Uitnodiging |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-16b98915-5c5e-4933-bfc0-9db634c47acb](https://gemmaonline.nl/index.php/GEMMA/id-16b98915-5c5e-4933-bfc0-9db634c47acb) |
    | gemma_definitie | Een verzoek om iets bij te wonen. |
    | gemma_toelichting |  |
    

Attributen van objecttype Uitnodiging

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| datum | DateTime |  |
| afgewezen | Boolean |  |
| geaccepteerd | Boolean |  |






## Enumeraties Model Inkoop


### Aanbestedingsoort
Geen Definitie

Het enumeratie Aanbestedingsoort kent de volgende waarden:

* **Enkelvoudig onderhands**: 
* **Meervoudig onderhands**: 
* **Nationale aanbesteding**: 
* **Europese aanbesteding**: 


De enumeratie Aanbestedingsoort heeft de volgende kenmerken:

??? info "Kenmerken Model Aanbestedingsoort"

    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | Aanbestedingsoort |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author |  |
    | version | 1.10.0 |
    | created | 2025-03-26 11:13:19 |
    | modified | 2025-12-16 10:28:45 |
    | id | EAID\_B8B79BCE\_8F87\_46f7\_BB15\_288266799E56 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    


### Inkooprol
Geen Definitie

Het enumeratie Inkooprol kent de volgende waarden:

* **Beheerder**: 
* **Eigenaar**: 
* **Inkoopadviseur**: 


De enumeratie Inkooprol heeft de volgende kenmerken:

??? info "Kenmerken Model Inkooprol"

    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | Inkooprol |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author |  |
    | version | 1.10.0 |
    | created | 2025-03-26 11:13:19 |
    | modified | 2025-12-16 10:28:45 |
    | id | EAID\_2C2791CB\_EFCA\_444f\_A95E\_F1EF6EE83594 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    


### Opdrachtcategorie
Geen Definitie

Het enumeratie Opdrachtcategorie kent de volgende waarden:

* **Leveringen**: 
* **Diensten - regulier**: 
* **Diensten - sociale of specifieke diensten**: 
* **Werken**: 


De enumeratie Opdrachtcategorie heeft de volgende kenmerken:

??? info "Kenmerken Model Opdrachtcategorie"

    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | Opdrachtcategorie |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author |  |
    | version | 1.10.0 |
    | created | 2025-03-26 11:13:19 |
    | modified | 2025-12-16 10:28:45 |
    | id | EAID\_87322382\_E60F\_4d0e\_93B0\_6628D3CC964B |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    


### Opdrachtsoort
Geen Definitie

Het enumeratie Opdrachtsoort kent de volgende waarden:

* **Opdracht voor levering, diensten of werken**: 
* **Inhuur extern personeel**: 
* **Subsidies**: 


De enumeratie Opdrachtsoort heeft de volgende kenmerken:

??? info "Kenmerken Model Opdrachtsoort"

    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | Opdrachtsoort |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author |  |
    | version | 1.10.0 |
    | created | 2025-03-26 11:13:19 |
    | modified | 2025-12-16 10:28:45 |
    | id | EAID\_5D6461E2\_0D66\_4039\_BBF4\_B413322EF194 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    


