# Model Inkoop
## Inleiding
> **Definitie Model Inkoop:** 
>
> Geen definitie

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
* **Gunning**: Gunning van een (enkel of meervoudige) onderhandse aanbesteding, of een nationale of Europese aanbesteding  Of voor levering personeel
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


Het model 'Model Inkoop' heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | Model Inkoop |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2018-04-04 15:09:45 |
| modified | 2019-11-27 10:56:23 |
| id | EAPK_254CDF37_3AAB_4e0b_9F3C_2B46AAEBE2E9 |


## Objecttypen Model Inkoop


### Aanbesteding
> **Definitie Aanbesteding:** 
>
> Kan een (enkel of meervoudige) onderhandse aanbesteding, of een nationale of Europese aanbesteding 

| Eigenschap | Waarde |
| :--- | :------ |
| name | Aanbesteding |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | abrienen |
| version | 1.0 |
| created | 2019-11-26 15:10:12 |
| modified | 2024-04-17 13:34:45 |
| id | EAID_44EC6082_2682_43c7_A52E_0AD05B06A046 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Aanbesteding |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA2/0.9/id-bc6f065d-05c9-454d-a18d-1c0c2a2dfe15](https://gemmaonline.nl/index.php/GEMMA2/0.9/id-bc6f065d-05c9-454d-a18d-1c0c2a2dfe15) |
| gemma_definitie | Kan een (enkel of meervoudige) onderhandse aanbesteding, of een nationale of Europese aanbesteding |
| gemma_toelichting |  |


Attributen van objecttype Aanbesteding

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| datumPublicatie | DateTime |  |
| datumStart | Date |  |
| digitaal | Boolean |  |
| naam | AN200 |  |
| procedure | Enumeratie: "Aanbestedingsoort" |  |
| referentienummer | AN80 |  |
| scoreMaximaal | int |  |
| status | AN80 |  |
| tendernedKenmerk | AN80 |  |
| type | Enumeratie: "Opdrachtcategorie" |  |
| volgendeSluiting | DateTime |  |
| None | Class: "MEDEWERKER" |  |
| None | Class: "ZAAK" |  |
| None | Class: "Gunning" |  |
| None | Class: "CPV-code" |  |




### Aanbesteding Inhuur
> **Definitie Aanbesteding Inhuur:** 
>
> Aanbesteding voor inhuur van personen of diensten

| Eigenschap | Waarde |
| :--- | :------ |
| name | Aanbesteding Inhuur |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | abrienen |
| version | 1.0 |
| created | 2019-11-26 15:14:45 |
| modified | 2024-04-17 13:34:45 |
| id | EAID_01D90490_C76A_444a_BFCE_355AFC5FB012 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Aanbesteding Inhuur |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA2/0.9/id-686c0af1-67b2-42a4-8690-060705617c13](https://gemmaonline.nl/index.php/GEMMA2/0.9/id-686c0af1-67b2-42a4-8690-060705617c13) |
| gemma_definitie | Aanbesteding voor inhuur van personen of diensten |
| gemma_toelichting |  |


Attributen van objecttype Aanbesteding Inhuur

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| aanvraagGesloten | DateTime |  |
| aanvraagnummer | AN80 |  |
| datumCreatie | DateTime |  |
| datumOpeningKluis | DateTime |  |
| datumSluiting | DateTime |  |
| datumSluiting | DateTime |  |
| datumVerzending | DateTime |  |
| fase | AN80 |  |
| hoogsteTarief | bedrag |  |
| laagsteTarief | bedrag |  |
| omschrijving | text |  |
| perceel | AN80 |  |
| procedure | AN80 |  |
| projectnaam | AN200 |  |
| projectreferentie | AN40 |  |
| publicatie | AN80 |  |
| referentie | AN80 |  |
| status | AN80 |  |
| titel | AN200 |  |
| type | Enumeratie: "Opdrachtcategorie" |  |
| None | Class: "Gunning" |  |
| None | Class: "CPV-code" |  |
| None | Class: "MEDEWERKER" |  |
| None | Class: "Categorie" |  |




### Aankondiging
> **Definitie Aankondiging:** 
>
> Aankondiging van een Nationale of Europese aanbesteding

| Eigenschap | Waarde |
| :--- | :------ |
| name | Aankondiging |
| toelichting |  |
| synoniemen | Kennisgeving, Bekendmaking |
| uri |  |
| bron |  |
| author | abrienen |
| version | 1.0 |
| created | 2019-11-26 15:09:54 |
| modified | 2024-04-17 13:34:45 |
| id | EAID_BB135B0E_A2C2_4681_BD91_30863F8B3D70 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Aankondiging |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA2/0.9/id-11a5fd2d-0237-4e70-b859-d1e26456553b](https://gemmaonline.nl/index.php/GEMMA2/0.9/id-11a5fd2d-0237-4e70-b859-d1e26456553b) |
| gemma_definitie | Aankondiging van een Nationale of Europese aanbesteding |
| gemma_toelichting |  |


Attributen van objecttype Aankondiging

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| beschrijving | text |  |
| categorie | Enumeratie: "Opdrachtcategorie" |  |
| datum | DateTime |  |
| naam | An200 |  |
| type | Enumeratie: "Aanbestedingsoort" |  |
| None | Class: "Aanbesteding" |  |




### Aanvraag Inkooporder
> **Definitie Aanvraag Inkooporder:** 
>
> het betreft hier het formulier 'Aanvraag Inkooporder'

| Eigenschap | Waarde |
| :--- | :------ |
| name | Aanvraag Inkooporder |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | abrienen |
| version | 1.0 |
| created | 2019-10-29 11:10:05 |
| modified | 2024-04-17 13:34:45 |
| id | EAID_33E5EA10_F43A_4966_B9C1_875F0E2C1B52 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Aanvraag Inkooporder |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA2/0.9/id-8d9233d7-dfb9-4b87-bab2-61631a632f95](https://gemmaonline.nl/index.php/GEMMA2/0.9/id-8d9233d7-dfb9-4b87-bab2-61631a632f95) |
| gemma_definitie | het betreft hier het formulier 'Aanvraag Inkooporder' |
| gemma_toelichting |  |


Attributen van objecttype Aanvraag Inkooporder

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| betalingOverMeerJaren | Boolean |  |
| correspondentienummer | int |  |
| inhuurAnders | AN80 |  |
| leveringOfDienst | Boolean |  |
| nettoTotaalBedrag | Bedrag |  |
| omschrijving | text |  |
| onderwerp | AN80 |  |
| reactie | Text |  |
| status | AN80 |  |
| wijzeVanInhuur | AN80 |  |
| None | Class: "ZAAK" |  |
| None | Class: "Leverancier" |  |
| None | Class: "ORGANISATORISCHE EENHEID" |  |
| None | Class: "Contract" |  |
| None | Class: "Inkooporder" |  |
| None | Class: "MEDEWERKER" |  |




### Categorie
> **Definitie Categorie:** 
>
> Categorie waarop leveranciers zich voor de levering van personeel voor kunnen kwalificeren

| Eigenschap | Waarde |
| :--- | :------ |
| name | Categorie |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | abrienen |
| version | 1.0 |
| created | 2019-11-26 15:16:32 |
| modified | 2024-04-17 13:34:45 |
| id | EAID_6CA060D0_C5AC_4b50_8B64_00DCAEA7EF48 |
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

| Eigenschap | Waarde |
| :--- | :------ |
| name | Contract |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | abrienen |
| version | 1.0 |
| created | 2019-10-29 10:34:40 |
| modified | 2024-04-17 13:34:46 |
| id | EAID_9FBF9FB8_B28D_4733_8443_607B8498F446 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Contract |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA2/0.9/id-f96af00f-2933-42d0-aacf-58ccb4a0ef52](https://gemmaonline.nl/index.php/GEMMA2/0.9/id-f96af00f-2933-42d0-aacf-58ccb4a0ef52) |
| gemma_definitie | Bindende overeenkomst |
| gemma_toelichting |  |


Attributen van objecttype Contract

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| autorisatiegroep | AN200 |  |
| beschrijving | text |  |
| categorie | AN80 |  |
| classificatie | AN80 |  |
| contractRevisie | int |  |
| datumCreatie | Date |  |
| datumEinde | Date |  |
| datumStart | Date |  |
| groep | AN80 |  |
| internContractID | AN40 |  |
| internContractRevisie | int |  |
| opmerkingen | text |  |
| status | AN80 |  |
| type | AN80 |  |
| voorwaarde | AN80 |  |
| zoekwoorden | AN300 |  |
| None | Class: "Tarief" |  |
| None | Class: "Contract" |  |
| None | Class: "Leverancier" |  |




### CPV-code
> **Definitie CPV-code:** 
>
> De Common Procurement Vocabulary (CPV-codes) is een gemeenschappelijke woordenlijst van de EU, alle mogelijke soorten overheidsopdrachten voor diensten, leveringen en werken hebben een eigen code gekregen. Aanbestedende diensten moeten bij Europese aanbestedingen dit classificatiesysteem toepassen.

| Eigenschap | Waarde |
| :--- | :------ |
| name | CPV-code |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | abrienen |
| version | 1.0 |
| created | 2019-11-27 14:11:20 |
| modified | 2024-04-17 13:34:46 |
| id | EAID_6A4CF470_3B0E_4141_9DB6_C9E8A525CB49 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | CPV-code |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA2/0.9/id-b6c26d6b-c773-4b50-ba03-a8463f23889a](https://gemmaonline.nl/index.php/GEMMA2/0.9/id-b6c26d6b-c773-4b50-ba03-a8463f23889a) |
| gemma_definitie | De Common Procurement Vocabulary (CPV-codes) is een gemeenschappelijke woordenlijst van de EU, alle mogelijke soorten overheidsopdrachten voor diensten, leveringen en werken hebben een eigen code gekregen. Aanbestedende diensten moeten bij Europese aanbestedingen dit classificatiesysteem toepassen. |
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

| Eigenschap | Waarde |
| :--- | :------ |
| name | FormulierInhuur |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | abrienen |
| version | 1.0 |
| created | 2019-11-18 15:32:41 |
| modified | 2024-04-17 13:34:46 |
| id | EAID_B598FF22_CDD0_486f_B528_99421D0FA608 |
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
| akkoordFinancieelAdviseur | Boolean |  |
| akkoordHRAdviseur | Boolean |  |
| datumIngangInhuur | Date |  |
| functienaamInhuur | AN200 |  |
| None | Class: "Kostenplaats" |  |
| None | Class: "Aanbesteding Inhuur" |  |
| None | Class: "MEDEWERKER" |  |




### FormulierVerlengingInhuur
> **Definitie FormulierVerlengingInhuur:** 
>
> Formulier ten behoeve van verlenging inhuur personeel

| Eigenschap | Waarde |
| :--- | :------ |
| name | FormulierVerlengingInhuur |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | abrienen |
| version | 1.0 |
| created | 2019-11-18 15:34:04 |
| modified | 2024-04-17 13:34:46 |
| id | EAID_1D87490A_9F07_424f_BE6F_5E9C11376B05 |
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
| indicatieRedenInhuurGewijzigd | Boolean |  |
| indicatieVerhogenInkooporder | Boolean |  |
| toelichting | text |  |
| None | Class: "MEDEWERKER" |  |
| None | Class: "Inkooporder" |  |
| None | Class: "Leverancier" |  |
| None | Class: "MEDEWERKER" |  |




### Gunning
> **Definitie Gunning:** 
>
> Gunning van een (enkel of meervoudige) onderhandse aanbesteding, of een nationale of Europese aanbesteding 
> Of voor levering personeel

| Eigenschap | Waarde |
| :--- | :------ |
| name | Gunning |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | abrienen |
| version | 1.0 |
| created | 2019-11-26 15:11:46 |
| modified | 2024-04-17 13:34:46 |
| id | EAID_3FB9B466_D147_42d7_99D1_2D14A007D16C |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Gunning |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA2/0.9/id-70e40543-6a99-433d-8a01-f4273e308410](https://gemmaonline.nl/index.php/GEMMA2/0.9/id-70e40543-6a99-433d-8a01-f4273e308410) |
| gemma_definitie | Gunning van een (enkel of meervoudige) onderhandse aanbesteding, of een nationale of Europese aanbesteding  Of voor levering personeel |
| gemma_toelichting |  |


Attributen van objecttype Gunning

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| bericht | AN300 |  |
| datumGunning | DateTime |  |
| datumPublicatie | DateTime |  |
| datumVoorlopigeGunning | DateTime |  |
| gegundePrijs | bedrag |  |
| None | Class: "Inschrijving" |  |
| None | Class: "Kandidaat" |  |
| None | Class: "Offerte" |  |
| None | Class: "MEDEWERKER" |  |




### Inkooppakket
> **Definitie Inkooppakket:** 
>
> Standaard indeling om de werken, diensten en leveringen die de aanbestedende dienst helpt bij het structureren van haar uitgaven. Samenhangende leveringen, diensten en producten zijn hierin gegroepeerd. 

| Eigenschap | Waarde |
| :--- | :------ |
| name | Inkooppakket |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | aashkpour |
| version | 1.0 |
| created | 2020-11-12 16:59:28 |
| modified | 2024-04-17 13:34:46 |
| id | EAID_170AF8F5_8952_407a_91C4_EAF910DE3304 |
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
| type | Enumeratie: "Opdrachtcategorie" |  |




### Inschrijving
> **Definitie Inschrijving:** 
>
> Inschrijving op een nationale of Europese aanbesteding 
> 

| Eigenschap | Waarde |
| :--- | :------ |
| name | Inschrijving |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | abrienen |
| version | 1.0 |
| created | 2019-11-26 15:11:11 |
| modified | 2024-04-17 13:34:46 |
| id | EAID_2902E8D6_FF16_45d6_A0A4_47E2857D2D19 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Inschrijving |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA2/0.9/id-e1c425c1-a3fe-4144-907d-13da8d9fb5cc](https://gemmaonline.nl/index.php/GEMMA2/0.9/id-e1c425c1-a3fe-4144-907d-13da8d9fb5cc) |
| gemma_definitie | Inschrijving op een nationale of Europese aanbesteding |
| gemma_toelichting |  |


Attributen van objecttype Inschrijving

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| datum | DateTime |  |
| prijs | Bedrag |  |
| score | int |  |
| None | Class: "Aanbesteding" |  |




### Kandidaat
> **Definitie Kandidaat:** 
>
> Iemand die een bepaalde baan of functie wil 

| Eigenschap | Waarde |
| :--- | :------ |
| name | Kandidaat |
| toelichting |  |
| synoniemen | Gegadigde |
| uri |  |
| bron |  |
| author | abrienen |
| version | 1.0 |
| created | 2019-11-27 10:37:40 |
| modified | 2024-04-17 13:34:46 |
| id | EAID_75B4E818_5ECD_45c5_98F9_66F57FC6117E |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Kandidaat |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA2/0.9/id-dc97ebf4-61ee-47f6-a108-af6bb4a276f7](https://gemmaonline.nl/index.php/GEMMA2/0.9/id-dc97ebf4-61ee-47f6-a108-af6bb4a276f7) |
| gemma_definitie | Iemand die een bepaalde baan of functie wil |
| gemma_toelichting |  |


Attributen van objecttype Kandidaat

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| datumIngestuurd | DateTime |  |
| None | Class: "NATUURLIJK PERSOON" |  |
| None | Class: "Aanbesteding Inhuur" |  |




### Kwalificatie
> **Definitie Kwalificatie:** 
>
> Kwalifificatie voor een nationale of europese aanbesteding

| Eigenschap | Waarde |
| :--- | :------ |
| name | Kwalificatie |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | abrienen |
| version | 1.0 |
| created | 2019-11-26 15:10:32 |
| modified | 2024-04-17 13:34:46 |
| id | EAID_AB2AED85_D2B0_45cf_9B1F_C6005E894494 |
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
| eindeGeldigheid | Date |  |
| startGeldigheid | Date |  |
| None | Class: "Aanbesteding" |  |




### Leverancier
> **Definitie Leverancier:** 
>
> Een niet-natuurlijk persoon die een product of dienst levert aan de organisatie

| Eigenschap | Waarde |
| :--- | :------ |
| name | Leverancier |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2018-05-29 13:54:06 |
| modified | 2024-04-17 13:34:46 |
| id | EAID_EA7FE08E_34F7_45d2_BE2E_E4E3B8333BF3 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Leverancier |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA2/0.9/id-113af80a-7e3e-41f6-8f79-8d0d48c4c257](https://gemmaonline.nl/index.php/GEMMA2/0.9/id-113af80a-7e3e-41f6-8f79-8d0d48c4c257) |
| gemma_definitie | Een niet-natuurlijk persoon die een product of dienst levert aan de organisatie |
| gemma_toelichting |  |


Attributen van objecttype Leverancier

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| naam | AN200 |  |
| nummer | AN40 |  |
| None | Class: "Inschrijving" |  |
| None | Class: "Kwalificatie" |  |
| None | Class: "Kandidaat" |  |
| None | Class: "Categorie" |  |




### Offerte
> **Definitie Offerte:** 
>
> Aanbod, aanbieding of voorstel van goederen of diensten waarin opgave is gedaan van de prijs. 

| Eigenschap | Waarde |
| :--- | :------ |
| name | Offerte |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | abrienen |
| version | 1.0 |
| created | 2019-11-27 13:29:18 |
| modified | 2024-04-17 13:34:46 |
| id | EAID_BF21FFA3_3EA6_410a_BC65_7BE5547646B6 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Offerte |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA2/0.9/id-6d31df7d-b7f9-4f50-be9f-eaf05c697f6e](https://gemmaonline.nl/index.php/GEMMA2/0.9/id-6d31df7d-b7f9-4f50-be9f-eaf05c697f6e) |
| gemma_definitie | Aanbod, aanbieding of voorstel van goederen of diensten waarin opgave is gedaan van de prijs. |
| gemma_toelichting |  |


Attributen van objecttype Offerte

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| datumOfferte | Date |  |
| naam | AN200 |  |
| omschrijving | text |  |
| prijs | bedrag |  |
| None | Class: "Leverancier" |  |
| None | Class: "Aanbesteding" |  |




### Offerteaanvraag
> **Definitie Offerteaanvraag:** 
>
> Aanbesteding bij inschrijving

| Eigenschap | Waarde |
| :--- | :------ |
| name | Offerteaanvraag |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | abrienen |
| version | 1.0 |
| created | 2019-11-26 15:22:25 |
| modified | 2024-04-17 13:34:46 |
| id | EAID_1EF1AC66_9563_4cdd_AE78_0878D651907A |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Offerteaanvraag |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA2/0.9/id-1b3c3c06-c7e9-40c0-8fa1-dbbc3c23152f](https://gemmaonline.nl/index.php/GEMMA2/0.9/id-1b3c3c06-c7e9-40c0-8fa1-dbbc3c23152f) |
| gemma_definitie | Aanbesteding bij inschrijving |
| gemma_toelichting |  |


Attributen van objecttype Offerteaanvraag

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| datumAanvraag | Date |  |
| datumSluiting | date |  |
| naam | AN80 |  |
| omschrijving | text |  |
| None | Class: "Aanbesteding" |  |
| None | Class: "Leverancier" |  |




### SelectietabelAanbesteding
> **Definitie SelectietabelAanbesteding:** 
>
> Gebaseerd op het procedureoverzicht inkoop. Hierin kan de tabel met drempelbedragen en bijbehorende procedures worden opgeslagen

| Eigenschap | Waarde |
| :--- | :------ |
| name | SelectietabelAanbesteding |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | abrienen |
| version | 1.0 |
| created | 2019-11-18 17:33:00 |
| modified | 2024-04-17 13:34:46 |
| id | EAID_B2BD6C5B_460E_4f2a_9B78_3E101DAD8D6B |
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
| aanbestedingsoort | Enumeratie: "Aanbestedingsoort" |  |
| drempelbedragTot | Bedrag |  |
| drempelbedragVanaf | Bedrag |  |
| opdrachtcategorie | Enumeratie: "Opdrachtcategorie" |  |
| openbaar | Boolean |  |




### StartformulierAanbesteden
> **Definitie StartformulierAanbesteden:** 
>
> Formulier voor het starten van een aanbeseding

| Eigenschap | Waarde |
| :--- | :------ |
| name | StartformulierAanbesteden |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | abrienen |
| version | 1.0 |
| created | 2019-11-18 15:32:13 |
| modified | 2024-04-17 13:34:46 |
| id | EAID_7694A657_22D8_4b00_AAE2_A78EF014B43A |
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
| beoogdeLooptijd | int |  |
| beoogdeTotaleOpdrachtwaarde | Bedrag |  |
| indicatieAanvullendeOpdrachtLeverancier | boolean |  |
| indicatieBeoogdeAanbestedingOnderhands | Boolean |  |
| indicatieBeoogdeProcKomtOvereen | boolean |  |
| indicatieEenmaligeLos | Boolean |  |
| indicatieMeerjarigeRaamovereenkomst | boolean |  |
| indicatieMeerjarigRepeterend | Boolean |  |
| indicatorOverkoepelendProject | Boolean |  |
| omschrijving | text |  |
| opdrachtcategorie | Enumeratie: "Opdrachtcategorie" |  |
| opdrachtsoort | Enumeratie: "Opdrachtsoort" |  |
| toelichtingAanvullendeOpdracht | text |  |
| toelichtingEenmaligOfRepeterend | text |  |
| None | Class: "ZAAK" |  |
| None | Class: "Aankondiging" |  |
| None | Class: "Aanbesteding" |  |




### Uitnodiging
> **Definitie Uitnodiging:** 
>
> Een verzoek om iets bij te wonen.

| Eigenschap | Waarde |
| :--- | :------ |
| name | Uitnodiging |
| toelichting |  |
| synoniemen | Invitatie |
| uri |  |
| bron |  |
| author | abrienen |
| version | 1.0 |
| created | 2019-11-27 14:27:00 |
| modified | 2024-04-17 13:34:46 |
| id | EAID_BB182A6F_6935_4702_ABEA_B96E32A40B02 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Uitnodiging |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA2/0.9/id-16b98915-5c5e-4933-bfc0-9db634c47acb](https://gemmaonline.nl/index.php/GEMMA2/0.9/id-16b98915-5c5e-4933-bfc0-9db634c47acb) |
| gemma_definitie | Een verzoek om iets bij te wonen. |
| gemma_toelichting |  |


Attributen van objecttype Uitnodiging

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| afgewezen | Boolean |  |
| datum | DateTime |  |
| geaccepteerd | Boolean |  |
| None | Class: "Leverancier" |  |
| None | Class: "Aanbesteding Inhuur" |  |







## Enumeraties Model Inkoop


### Aanbestedingsoort
Geen Definitie

Het enumeratie Aanbestedingsoort kent de volgende waarden:

* **Enkelvoudig onderhands**: <Geen Definities>
* **Meervoudig onderhands**: <Geen Definities>
* **Nationale aanbesteding**: <Geen Definities>
* **Europese aanbesteding**: <Geen Definities>


De enumeratie Aanbestedingsoort heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | Aanbestedingsoort |
| toelichting | None |
| synoniemen | None |
| uri | None |
| bron | None |
| author | None |
| version | None |
| created | None |
| modified | None |
| id | EAID_B8B79BCE_8F87_46f7_BB15_288266799E56 |
| domein_iv3 | None |
| domein_dcat | None |
| gemma_naam | None |
| gemma_type | None |
| gemma_url | None |
| gemma_definitie | None |
| gemma_toelichting | None |



### Inkooprol
Geen Definitie

Het enumeratie Inkooprol kent de volgende waarden:

* **Beheerder**: <Geen Definities>
* **Eigenaar**: <Geen Definities>
* **Inkoopadviseur**: <Geen Definities>


De enumeratie Inkooprol heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | Inkooprol |
| toelichting | None |
| synoniemen | None |
| uri | None |
| bron | None |
| author | None |
| version | None |
| created | None |
| modified | None |
| id | EAID_2C2791CB_EFCA_444f_A95E_F1EF6EE83594 |
| domein_iv3 | None |
| domein_dcat | None |
| gemma_naam | None |
| gemma_type | None |
| gemma_url | None |
| gemma_definitie | None |
| gemma_toelichting | None |



### Opdrachtcategorie
Geen Definitie

Het enumeratie Opdrachtcategorie kent de volgende waarden:

* **Leveringen**: <Geen Definities>
* **Diensten - regulier**: <Geen Definities>
* **Diensten - sociale of specifieke diensten**: <Geen Definities>
* **Werken**: <Geen Definities>


De enumeratie Opdrachtcategorie heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | Opdrachtcategorie |
| toelichting | None |
| synoniemen | None |
| uri | None |
| bron | None |
| author | None |
| version | None |
| created | None |
| modified | None |
| id | EAID_87322382_E60F_4d0e_93B0_6628D3CC964B |
| domein_iv3 | None |
| domein_dcat | None |
| gemma_naam | None |
| gemma_type | None |
| gemma_url | None |
| gemma_definitie | None |
| gemma_toelichting | None |



### Opdrachtsoort
Geen Definitie

Het enumeratie Opdrachtsoort kent de volgende waarden:

* **Opdracht voor levering, diensten of werken**: <Geen Definities>
* **Inhuur extern personeel**: <Geen Definities>
* **Subsidies**: <Geen Definities>


De enumeratie Opdrachtsoort heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | Opdrachtsoort |
| toelichting | None |
| synoniemen | None |
| uri | None |
| bron | None |
| author | None |
| version | None |
| created | None |
| modified | None |
| id | EAID_5D6461E2_0D66_4039_BBF4_B413322EF194 |
| domein_iv3 | None |
| domein_dcat | None |
| gemma_naam | None |
| gemma_type | None |
| gemma_url | None |
| gemma_definitie | None |
| gemma_toelichting | None |




