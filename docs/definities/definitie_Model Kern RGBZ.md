# Model Kern RGBZ
## Inleiding
> **Definitie Model Kern RGBZ:** 
>
> Geen definitie

Het model 'Model Kern RGBZ' kent de volgende objecttypen:

* **Bedrijfsproces**: Reeks opeenvolgend uit te voeren activiteiten die bijdraagt aan een specifiek resultaat, zoals de levering van een product of product of dienst.
* **Bedrijfsprocestype**: soort Bedrijfsproces met bepaalde kenmerken
* **Besluit**: Een na overweging of beraadslaging vastgestelde beslissing voor een individueel of concreet geval.
* **Besluittype**: Generieke aanduiding van de aard van een besluit
* **Betaling**: het onderhandigen of overboeken van geld in ruil voor goed of dienst
* **Betrokkene**: Een SUBJECT, zijnde een NATUURLIJK PERSOON, NIET-NATUURLIJK PERSOON of VESTIGING, ORGANISATORISCHE EENHEID (binnen een vestiging van de zaak-behandelende niet-natuurlijk persoon), of MEDEWERKER (van die organisatorische eenheid) die een rol kan spelen bij een ZAAK.
* **Deelproces**: Een geordende reeks van processtappen die binnen één organisatorische eenheid binnen een organisatie wordt uitgevoerd met als doel een specifieke bijdrage (prestatie) te leveren aan een dienst die uiteindelijke zal worden geleverd aan een burger, een bedrijf of een andere organisatie. Voorheen 'werkproces' genoemd.
* **Deelprocestype**: soort Deelproces met bepaalde kenmerken
* **Document**: Geheel van gegevens met een eigen identiteit ongeacht zijn vorm, met de bijbehorende metadata ontvangen of opgemaakt door een natuurlijke en/of rechtspersoon bij de uitvoering van taken, zijnde een ENKELVOUDIG DOCUMENT of een SAMENGESTELD DOCUMENT.
* **Documenttype**: Aanduiding van de aard van een DOCUMENT zoals gehanteerd door de zaakbehandelende organisatie
* **EnkelvoudigDocument**: Een DOCUMENT waarvan aard, omvang en/of vorm aanleiding geven het als één geheel te behandelen en te beheren.
* **Heffing**: Een door de overheid opgelegde verplichting tot betaling
* **Identificatiekenmerk**: Nodig voor archivering om verschillende typen identificatie te kunnen onderscheiden:
* **Klantcontact**: Klantcontacten zijn contactmomenten die werkelijk hebben plaatsgevonden, terwijl Balieafspraken afspraken zijn voor een klantcontact. Dit ongeacht of deze werkelijk heeft plaatsgevonden, soms liggen deze in de toekomst of is iemand niet op komen dagen, of iets anders waardoor het klantcontact nog niet heeft plaatsgevonden.  Hetzelfde geldt voor de telefoontjes, de klantcontacten komen uit levelOneData, dat zijn alle telefoontjes die werkelijk met een medewerker (of een gedelegeerde) hebben plaatsgevonden (soms zelfs meerdere binnen 1 telefoontje). 
* **Medewerker**: Een medewerker van de organisatie die zaken behandelt uit hoofde van zijn of haar functie binnen een ORGANISATORISCHE EENHEID.
* **Object**: Het OBJECT waarop een ZAAK betrekking kan hebben zijnde één of meer voorkomens van de in het RSGB en het RGBZ onderscheiden objecttypen.
* **Offerte**: Aanbod, aanbieding of voorstel van goederen of diensten waarin opgave is gedaan van de prijs. 
* **OrganisatorischeEenheid**: Het deel van een functioneel afgebakend onderdeel binnen de organisatie dat haar activiteiten uitvoert binnen een VESTIGING VAN ZAAKBEHANDELENDE ORGANISATIE en die verantwoordelijk is voor de behandeling van zaken.
* **SamengesteldDocument**: Een DOCUMENT waarbinnen twee of meer ENKELVOUDIGe DOCUMENTen onderscheiden worden die vanwege gezamenlijke vervaardiging en/of ontvangst en/of vanwege aard en/of omvang als één geheel beschouwd moeten worden dan wel behandeld worden.,
* **Status**: Een aanduiding van de stand van zaken van een zaak op basis van betekenisvol behaald resultaat voor de initiator van de zaak.
* **Statustype**: Generieke aanduiding van de aard van een STATUS
* **VestigingVanZaakbehandelendeOrganisatie**: Een VESTIGING van een onderneming of rechtspersoon zijnde de zaakbehandelende organisatie.
* **Zaak**: Een samenhangende hoeveelheid werk met een welgedefinieerde aanleiding en een welgedefinieerd eindresultaat, waarvan kwaliteit en doorlooptijd bewaakt moeten worden.
* **ZAAK - Origineel**: Een samenhangende hoeveelheid werk met een welgedefinieerde aanleiding en een welgedefinieerd eindresultaat, waarvan kwaliteit en doorlooptijd bewaakt moeten worden.
* **Zaaktype**: Generieke aanduiding van de aard van een zaak


Het model 'Model Kern RGBZ' heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | Model Kern RGBZ |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | mante_h |
| version | 1.3 |
| created | 2010-10-19 17:21:37 |
| modified | 2024-11-21 08:38:15 |
| id | EAPK_2EDFFA95_0A05_4292_84C5_2A912A6B6718 |


## Objecttypen Model Kern RGBZ


### Bedrijfsproces
> **Definitie Bedrijfsproces:** 
>
> Reeks opeenvolgend uit te voeren activiteiten die bijdraagt aan een specifiek resultaat, zoals de levering van een product of product of dienst.

| Eigenschap | Waarde |
| :--- | :------ |
| name | Bedrijfsproces |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | aashkpour |
| version | 1.7 |
| created | 2023-05-15 13:27:23 |
| modified | 2025-03-26 16:14:50 |
| id | EAID_EDB5D3CD_CE4D_4317_81C6_C01CC7325148 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Bedrijfsproces |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-7e054df1-48a3-46c3-91a5-5ce10e326f9b](https://gemmaonline.nl/index.php/GEMMA/id-7e054df1-48a3-46c3-91a5-5ce10e326f9b) |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Bedrijfsproces

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| Omschrijving | AN200 |  |
| Datum_start | Date |  |
| Datum_eind | Date |  |
| Afgerond | Enumeratie: "Boolean" |  |
| Naam | AN200 |  |
| None | Class: "Zaak" |  |
| None | Class: "Bedrijfsprocestype" |  |




### Bedrijfsprocestype
> **Definitie Bedrijfsprocestype:** 
>
> soort Bedrijfsproces met bepaalde kenmerken

| Eigenschap | Waarde |
| :--- | :------ |
| name | Bedrijfsprocestype |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | aashkpour |
| version | 1.5 |
| created | 2023-05-15 13:29:43 |
| modified | 2025-03-26 16:14:50 |
| id | EAID_14E4AF23_21E9_412a_B78D_C208EE9F419D |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Bedrijfsprocestype

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| Omschrijving | AM200 |  |
| None | Class: "Producttype" |  |
| None | Class: "Zaaktype" |  |




### Besluit
> **Definitie Besluit:** 
>
> Een na overweging of beraadslaging vastgestelde beslissing voor een individueel of concreet geval.

| Eigenschap | Waarde |
| :--- | :------ |
| name | Besluit |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | mante_h |
| version | 1.5 |
| created | 2010-08-19 09:41:46 |
| modified | 2025-03-26 16:14:50 |
| id | EAID_AFB100D2_8C68_4488_8949_13E945D15920 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Besluit |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-10d36920-683f-4cb4-84bf-b00ac045674f](https://gemmaonline.nl/index.php/GEMMA/id-10d36920-683f-4cb4-84bf-b00ac045674f) |
| gemma_definitie | Een na overweging of beraadslaging vastgestelde beslissing voor een individueel of concreet geval. |
| gemma_toelichting |  |


Attributen van objecttype Besluit

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| besluitidentificatie | AN50 | <font color="#610e6a">Identificatie van het besluit.</font> |
| datumBesluit |  | <font color="#610e6a">De beslisdatum (AWB) van het besluit.</font> |
| besluittoelichting | AN1000 | <font color="#610e6a">Toelichting bij het besluit.</font> |
| datumStart |  | <font color="#610e6a">Ingangsdatum van de werkingsperiode van het besluit.</font> |
| datumVerval |  | <font color="#610e6a">Datum waarop de werkingsperiode van het besluit eindigt.</font> |
| redenVerval | X40 | <font color="#610e6a">De omschrijving die aangeeft op grond waarvan het besluit is of komt te vervallen.</font> |
| datumPublicatie |  | <font color="#610e6a">Datum waarop het besluit gepubliceerd wordt.</font> |
| datumVerzending |  | <font color="#610e6a">Datum waarop het besluit verzonden is.</font> |
| datumUiterlijkeReactie |  | <font color="#610e6a">De datum tot wanneer verweer tegen het besluit mogelijk is.</font> |
| besluit | AN200 |  |
| document | Class: "Document" |  |
| None | Class: "Document" |  |
| zaak | Class: "Zaak" |  |
| type | Class: "Besluittype" |  |




### Besluittype
> **Definitie Besluittype:** 
>
> Generieke aanduiding van de aard van een besluit

| Eigenschap | Waarde |
| :--- | :------ |
| name | Besluittype |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | mante_h |
| version | 1.5 |
| created | 2010-08-19 10:01:32 |
| modified | 2025-03-26 16:14:50 |
| id | EAID_922D3938_A0EA_42bf_9EFC_23A6A236AF9B |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Besluittype

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| besluittypeOmschrijving | AN80 | <font color="#610e6a">Omschrijving van de aard van BESLUITen van het BESLUITTYPE.</font> |
| besluittypeOmschrijvingGeneriek | AN80 | <font color="#610e6a">Algemeen gehanteerde omschrijving van de aard van BESLUITen van het BESLUITTYPE</font> |
| besluitcategorie | AN40 | <font color="#610e6a">Typering van de aard van BESLUITen van het BESLUITTYPE.</font> |
| reactietermijn | N3 | <font color="#610e6a">Het aantal dagen, gerekend vanaf de verzend- of publicatiedatum, waarbinnen verweer tegen een besluit van het besluittype mogelijk is.</font> |
| indicatiePublicatie | AN1 | <font color="#610e6a">Aanduiding of BESLUITen van dit BESLUITTYPE gepubliceerd moeten worden.</font> |
| publicatietekst | AN1000 | <font color="#610e6a">De generieke tekst van de publicatie van BESLUITen van dit BESLUITTYPE</font> |
| publicatietermijn | N3 | <font color="#610e6a">Het aantal dagen, gerekend vanaf de verzend- of publicatiedatum, dat BESLUITen van dit BESLUITTYPE gepubliceerd moeten blijven.</font> |
| datumBeginGeldigheidBesluittype | OnvolledigeDatum | <font color="#610e6a">De datum waarop het BESLUITTYPE is ontstaan.</font> |
| datumEindeGeldigheidBesluittype | OnvolledigeDatum | <font color="#610e6a">De datum waarop het BESLUITTYPE is opgeheven.</font> |




### Betaling
> **Definitie Betaling:** 
>
> het onderhandigen of overboeken van geld in ruil voor goed of dienst

| Eigenschap | Waarde |
| :--- | :------ |
| name | Betaling |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | crossover |
| version | 1.7 |
| created | 2018-04-23 11:51:28 |
| modified | 2025-03-26 16:14:50 |
| id | EAID_FC488929_8721_402f_A073_1DFDB76A816E |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Betaling |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-8cec89b8-6174-42ac-937f-9500bfb8901b](https://gemmaonline.nl/index.php/GEMMA/id-8cec89b8-6174-42ac-937f-9500bfb8901b) |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Betaling

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| bedrag | Bedrag |  |
| datumtijd | datetime |  |
| valuta | AN3 |  |
| omschrijving | AN200 |  |




### Betrokkene
> **Definitie Betrokkene:** 
>
> Een SUBJECT, zijnde een NATUURLIJK PERSOON, NIET-NATUURLIJK PERSOON of VESTIGING, ORGANISATORISCHE EENHEID (binnen een vestiging van de zaak-behandelende niet-natuurlijk persoon), of MEDEWERKER (van die organisatorische eenheid) die een rol kan spelen bij een ZAAK.

| Eigenschap | Waarde |
| :--- | :------ |
| name | Betrokkene |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | mante_h |
| version | 1.5 |
| created | 2010-08-19 10:58:19 |
| modified | 2025-03-26 16:14:50 |
| id | EAID_16FB8171_A9ED_4027_A663_C035509501C8 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Betrokkene |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-62c91622-cc32-4560-8427-d00101f4847e](https://gemmaonline.nl/index.php/GEMMA/id-62c91622-cc32-4560-8427-d00101f4847e) |
| gemma_definitie | Een SUBJECT, zijnde een NATUURLIJK PERSOON, NIET-NATUURLIJK PERSOON of VESTIGING, ORGANISATORISCHE EENHEID (binnen een vestiging van de zaak-behandelende niet-natuurlijk persoon), of MEDEWERKER (van die organisatorische eenheid) die een rol kan spelen bij |
| gemma_toelichting |  |


Attributen van objecttype Betrokkene

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| rol |  |  |
| naam | AN200 | <font color="#610e6a">De benaming van de BETROKKENE  indien dit een (NIET) NATUURLIJK PERSOON, VESTIGING of specialisatie daarvan is.</font> |
| identificatie | AN50 | <font color="#610e6a">De unieke identificatie van de BETROKKENE</font> |
| adresBinnenland |  | <font color="#610e6a">De aanduiding van het adres van de BETROKKENE indien dit adres in Nederland gelegen is.</font> |
| adresBuitenland |  | <font color="#610e6a">De aanduiding van het adres waar specialisaties van de BETROKKENE  zijnde een (NIET) NATUURLIJK PERSOON of VESTIGING dan wel een specialisatie daarvan, verblijft dan wel bereikbaar is in het buitenland.</font> |
| betrokkene | Class: "NatuurlijkPersoon" |  |
| organisatorische eenheid | Class: "OrganisatorischeEenheid" |  |
| None | Class: "Klantbeoordeling" |  |
| vestiging | Class: "NietNatuurlijkPersoon" |  |
| medewerker | Class: "Medewerker" |  |




### Deelproces
> **Definitie Deelproces:** 
>
> Een geordende reeks van processtappen die binnen één organisatorische eenheid binnen een organisatie wordt uitgevoerd met als doel een specifieke bijdrage (prestatie) te leveren aan een dienst die uiteindelijke zal worden geleverd aan een burger, een bedrijf of een andere organisatie. Voorheen 'werkproces' genoemd.

| Eigenschap | Waarde |
| :--- | :------ |
| name | Deelproces |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | aashkpour |
| version | 1.5 |
| created | 2023-05-15 13:30:05 |
| modified | 2025-03-26 16:14:50 |
| id | EAID_1B65D674_DC17_40e8_B663_85DA82FD7E94 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Deelproces

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| Datum_gepland | Date |  |
| Datum_afgehandeld | Date |  |
| None | Class: "Deelprocestype" |  |
| None | Class: "Bedrijfsproces" |  |




### Deelprocestype
> **Definitie Deelprocestype:** 
>
> soort Deelproces met bepaalde kenmerken

| Eigenschap | Waarde |
| :--- | :------ |
| name | Deelprocestype |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | aashkpour |
| version | 1.5 |
| created | 2023-05-15 13:30:19 |
| modified | 2025-03-26 16:14:50 |
| id | EAID_710A1D2B_3C7B_41cf_A947_727186C40A98 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Deelprocestype

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| Omschrijving | AN200 |  |
| None | Class: "Bedrijfsprocestype" |  |




### Document
> **Definitie Document:** 
>
> Geheel van gegevens met een eigen identiteit ongeacht zijn vorm, met de bijbehorende metadata ontvangen of opgemaakt door een natuurlijke en/of rechtspersoon bij de uitvoering van taken, zijnde een ENKELVOUDIG DOCUMENT of een SAMENGESTELD DOCUMENT.

| Eigenschap | Waarde |
| :--- | :------ |
| name | Document |
| toelichting | #NOTES#Een inhoudelijke toelichting op de toepassing van het informatie-element. |
| synoniemen |  |
| uri |  |
| bron |  |
| author | mante_h |
| version | 1.4 |
| created | 2010-08-19 12:15:35 |
| modified | 2025-03-26 16:14:50 |
| id | EAID_5641C50A_C0FA_4e71_B07B_26C7B1CE94ED |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Document |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-10eaa33f-03bf-42b4-9310-56add2cb5a7b](https://gemmaonline.nl/index.php/GEMMA/id-10eaa33f-03bf-42b4-9310-56add2cb5a7b) |
| gemma_definitie | Geheel van gegevens met een eigen identiteit ongeacht zijn vorm, met de bijbehorende metadata ontvangen of opgemaakt door een natuurlijke en/of rechtspersoon bij de uitvoering van taken, zijnde een ENKELVOUDIG DOCUMENT of een SAMENGESTELD DOCUMENT. |
| gemma_toelichting |  |


Attributen van objecttype Document

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| documentIdentificatie | AN40 | <font color="#610e6a">Een binnen een gegeven context ondubbelzinnige referentie naar het document.</font>
<font color="#610e6a">Bijvoorbeeld potsregistratienummer</font>
 |
| datumCreatieDocument |  | <font color="#610e6a">Een datum of een gebeurtenis in de levenscyclus van het document.</font> |
| datumOntvangstdocument |  | <font color="#610e6a">De datum waarop het DOCUMENT ontvangen is.</font> |
| documentTitel | AN200 | <font color="#610e6a">De naam waaronder het document formeel bekend is.</font> |
| cocumentBeschrijving | AN1000 | <font color="#610e6a">Een generieke beschrijving van de inhoud van het document.</font> |
| datumVerzendingDocument |  | <font color="#610e6a">De datum waarop het DOCUMENT verzonden is.</font> |
| vertrouwelijkAanduiding | AN20 | <font color="#610e6a">Aanduiding van de mate waarin het DOCUMENT voor de openbaarheid bestemd is.</font> |
| documentAuteur | AN200 | <font color="#610e6a">De persoon of organisatie die in de eerste plaats verantwoordelijk is voor het creëren van de inhoud van het document.</font> |
| type | Class: "Documenttype" |  |




### Documenttype
> **Definitie Documenttype:** 
>
> Aanduiding van de aard van een DOCUMENT zoals gehanteerd door de zaakbehandelende organisatie

| Eigenschap | Waarde |
| :--- | :------ |
| name | Documenttype |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | mante_h |
| version | 1.5 |
| created | 2010-08-19 11:30:39 |
| modified | 2025-03-26 16:14:50 |
| id | EAID_77C7D6B6_44DE_44c0_A662_8E1A0A226EA8 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Documenttype

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| documenttypeOmschrijving | AN80 | <font color="#610e6a">Omschrijving van de aard van DOCUMENTen van dit DOCUMENTTYPE.</font> |
| documenttypeOmschrijvingGeneriek | AN80 | <font color="#610e6a">Algemeen gehanteerde omschrijving van het DOCUMENTTYPE</font> |
| documentCategorie | AN80 | <font color="#610e6a">Typering van de aard van DOCUMENTen van dit DOCUMENTTYPE.</font> |
| documenttypeTrefwoord | AN30 | <font color="#610e6a">Trefwoord(en) waarmee DOCUMENTen van het DOCUMENTTYPE kunnen worden gekarakteriseerd.</font> |
| datumBeginGeldigheidDocumenttype | OnvolledigeDatum | <font color="#610e6a">De datum waarop het DOCUMENTTYPE is ontstaan.</font> |
| datumEindeGeldigheidDocumenttype | OnvolledigeDatum | <font color="#610e6a">De datum waarop het DOCUMENTTYPE is opgeheven.</font> |




### EnkelvoudigDocument
> **Definitie EnkelvoudigDocument:** 
>
> Een DOCUMENT waarvan aard, omvang en/of vorm aanleiding geven het als één geheel te behandelen en te beheren.

| Eigenschap | Waarde |
| :--- | :------ |
| name | EnkelvoudigDocument |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | mante_h |
| version | 1.5 |
| created | 2010-08-19 11:32:47 |
| modified | 2025-03-26 16:14:50 |
| id | EAID_547FD48D_F885_4816_BCFA_4048995C8D83 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype EnkelvoudigDocument

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| documentFormaat | AN10 | <font color="#610e6a">De digitale manifestatie van het ENKELVOUDIG DOCUMENT.</font> |
| documentTaal | AN20 | <font color="#610e6a">Een taal van de intellectuele inhoud van het ENKELVOUDIG DOCUMENT</font> |
| documentVersie | AN5 | <font color="#610e6a">Aanduiding van de bewerkingsfase van het ENKELVOUDIG DOCUMENT</font> |
| documentStatus | AN20 | <font color="#610e6a">Aanduiding van de stand van zaken van een ENKELVOUDIG DOCUMENTDOCUMENT.</font> |
| documentInhoud | Documentformaat | <font color="#610e6a">Datgene wat in een ENKELVOUDIG DOCUMENT wordt meegedeeld.</font> |
| documentLink | AN200 | <font color="#610e6a">De URL waarmee de documentinhoud op te vragen is.</font> |
| bestandsnaam | AN255 | <font color="#610e6a">De naam van het fysieke bestand waarin de documentinhoud is vastgelegd.</font> |




### Heffing
> **Definitie Heffing:** 
>
> Een door de overheid opgelegde verplichting tot betaling

| Eigenschap | Waarde |
| :--- | :------ |
| name | Heffing |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.7 |
| created | 2019-04-17 13:44:30 |
| modified | 2025-03-26 16:14:50 |
| id | EAID_B3371695_97AD_49d2_9AF1_15591B422007 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Heffing |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-ff9366e3-dd65-48ce-9051-9d6b01b2c6db](https://gemmaonline.nl/index.php/GEMMA/id-ff9366e3-dd65-48ce-9051-9d6b01b2c6db) |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Heffing

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| bedrag | bedrag |  |
| code | AN80 |  |
| inrekening | bedrag |  |
| gefactureerd | boolean |  |
| runnummer | int |  |
| datumIndiening | datum |  |
| nummer | int |  |
| None | Enumeratie: "Heffingsoort" |  |
| None | Class: "Heffinggrondslag" |  |




### Identificatiekenmerk
> **Definitie Identificatiekenmerk:** 
>
> Nodig voor archivering om verschillende typen identificatie te kunnen onderscheiden:

| Eigenschap | Waarde |
| :--- | :------ |
| name | Identificatiekenmerk |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.5 |
| created | 2018-07-02 10:30:07 |
| modified | 2025-03-26 16:14:50 |
| id | EAID_D73AFAEC_3BF1_4309_93FE_5354EF26DA51 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Identificatiekenmerk

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| kenmerk | AN20 |  |




### Klantcontact
> **Definitie Klantcontact:** 
>
> Klantcontacten zijn contactmomenten die werkelijk hebben plaatsgevonden, terwijl Balieafspraken afspraken zijn voor een klantcontact. Dit ongeacht of deze werkelijk heeft plaatsgevonden, soms liggen deze in de toekomst of is iemand niet op komen dagen, of iets anders waardoor het klantcontact nog niet heeft plaatsgevonden.
> 
> Hetzelfde geldt voor de telefoontjes, de klantcontacten komen uit levelOneData, dat zijn alle telefoontjes die werkelijk met een medewerker (of een gedelegeerde) hebben plaatsgevonden (soms zelfs meerdere binnen 1 telefoontje).
> 

| Eigenschap | Waarde |
| :--- | :------ |
| name | Klantcontact |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | crossover |
| version | 1.5 |
| created | 2018-04-25 14:49:05 |
| modified | 2025-03-26 16:14:50 |
| id | EAID_A3DAD553_0E55_4256_824B_CDB5E12CB545 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Klantcontact |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-a9cb919f-a224-4ab5-9825-40d54104f90d](https://gemmaonline.nl/index.php/GEMMA/id-a9cb919f-a224-4ab5-9825-40d54104f90d) |
| gemma_definitie | Klantcontacten zijn contactmomenten die werkelijk hebben plaatsgevonden, terwijl Balieafspraken afspraken zijn voor een klantcontact. Dit ongeacht of deze werkelijk heeft plaatsgevonden, soms liggen deze in de toekomst of is iemand niet op komen dagen, of |
| gemma_toelichting |  |


Attributen van objecttype Klantcontact

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| eindtijd | Datetime | Werkelijke eindtijd van het klantcontact. Het moment dat de conversatie ten einde is.
Bij digitaal klantcontact (het indienen van een webformulier) zijn start- en eindtijd aan elkaar gelijk

 |
| starttijd | Datetime | Werkelijke starttijd van het klantcontact, dus het moment dat klant en medewerker van de gemeente elkaar spreken.

Bij digitaal klantcontact (het indienen van een webformulier) zijn start- en eindtijd aan elkaar gelijk |
| tijdsduur | int | Werkelijke tijdsduur in seconden
 |
| wachttijdTotaal | int | De totale wachttijd voor de starttijd van het klantcontact. Dit inclusief eventueel te vroeg verschijnen op een afspraak |
| kanaal | AN20 |  |
| toelichting | text |  |
| notitie | text |  |
| None | Enumeratie: "Soorten Klantcontact" |  |




### Medewerker
> **Definitie Medewerker:** 
>
> Een medewerker van de organisatie die zaken behandelt uit hoofde van zijn of haar functie binnen een ORGANISATORISCHE EENHEID.

| Eigenschap | Waarde |
| :--- | :------ |
| name | Medewerker |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | mante_h |
| version | 1.5 |
| created | 2010-08-19 11:35:05 |
| modified | 2025-03-26 16:14:50 |
| id | EAID_16EB3936_03CB_4854_9CD8_9F0911EEA51B |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Medewerker |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-6cc6afe6-e4c6-4e2b-a359-f278b23700db](https://gemmaonline.nl/index.php/GEMMA/id-6cc6afe6-e4c6-4e2b-a359-f278b23700db) |
| gemma_definitie | Een medewerker van de organisatie die zaken behandelt uit hoofde van zijn of haar functie binnen een ORGANISATORISCHE EENHEID. |
| gemma_toelichting |  |


Attributen van objecttype Medewerker

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| medewerkerIdentificatie | AN24 | <font color="#610e6a">Een korte unieke aanduiding van de medewerker.</font> |
| achternaam | AN200 | <font color="#610e6a">De achternaam zoals de medewerker die in het dagelijkse verkeer gebruikt.</font> |
| datumUitDienst |  | <font color="#610e6a">Een aanduiding van de datum waarop de arbeidsplaatsvervulling eindigt.</font> |
| emailadres | AN254 | <font color="#610e6a">Elektronisch postadres waaronder de medewerker in de regel bereikbaar is.</font> |
| functie | AN50 | <font color="#610e6a">De aanduiding van de taken, rechten en plichten die de medewerker heeft of heeft gehad binnen de zaakbehandelende organisatie.</font> |
| geslachtsaanduiding | A1 | <font color="#610e6a">Een aanduiding die aangeeft of de persoon een man of een vrouw is, of dat het geslacht nog onbekend is.</font> |
| medewerkerToelichting | AN1000 | <font color="#610e6a">Toelichting bij en/of over de medewerker.</font> |
| roepnaam | AN30 | <font color="#610e6a">Naam waarmee de werknemer wordt aangesproken.</font> |
| telefoonnummer | AN20 | <font color="#610e6a">Telefoonnummer waaronder de medewerker in de regel bereikbaar is.</font> |
| voorletters | AN20 | <font color="#610e6a">De verzameling letters die gevormd wordt door de eerste letter van alle in volgorde voorkomende voornamen.</font> |
| voorvoegselAchternaam | AN10 | <font color="#610e6a">Dat deel van de geslachtsnaam dat voorkomt in Tabel 36 (GBA), voorvoegseltabel, en door een spatie van de geslachtsnaam is</font>
<font color="#610e6a">gescheiden.</font> |
| extern |  | Medewerker is een externe? |
| datumInDienst | Date |  |
| None | Class: "Leverancier" |  |
| None | Class: "StartformulierAanbesteden" |  |
| None | Class: "Aanvraag Inkooporder" |  |
| organisatorische eenheid | Class: "OrganisatorischeEenheid" |  |
| None | Class: "Proces-verbaal-MOOR-melding" |  |
| None | Class: "Subsidie" |  |
| organisatorische eenheid | Class: "OrganisatorischeEenheid" |  |
| None | Class: "Uitvoerende instantie" |  |
| None | Class: "OrganisatorischeEenheid" |  |




### Object
> **Definitie Object:** 
>
> Het OBJECT waarop een ZAAK betrekking kan hebben zijnde één of meer voorkomens van de in het RSGB en het RGBZ onderscheiden objecttypen.

| Eigenschap | Waarde |
| :--- | :------ |
| name | Object |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | mante_h |
| version | 1.5 |
| created | 2010-08-19 11:37:35 |
| modified | 2025-03-26 16:14:50 |
| id | EAID_91F9D39E_0322_42c6_AE7F_5027B36F3EC3 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Object |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-f08625cc-cc49-4664-91fa-823b217d333f](https://gemmaonline.nl/index.php/GEMMA/id-f08625cc-cc49-4664-91fa-823b217d333f) |
| gemma_definitie | Het OBJECT waarop een ZAAK betrekking kan hebben zijnde één of meer voorkomens van de in het RSGB en het RGBZ onderscheiden objecttypen. |
| gemma_toelichting |  |


Attributen van objecttype Object

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| identificatie | AN50 | <font color="#610e6a">De unieke identificatie van het OBJECT</font> |
| objecttype | AN3 | <font color="#610e6a">Het onderscheid van een OBJECT naar haar specialisatiies.</font>
<font color="#610e6a">De code voor de Objecttypering gevolgd door de unieke aanduiding van de specialisatie (van OBJECT):</font>
<font color="#610e6a">ADRESSEERBAAR OBJECT AANDUIDING, BENOEMD OBJECT, BESLUIT, BUURT, ENKELVOUDIG INFORMATIEOBJECT, GEMEENTE, GEMEENTELIJKE OPENBARE RUIMTE, HUISHOUDEN, INRICHTINGSELEMENT, KADASTRALE ONROERENDE ZAAK, KUNSTWERKDEEL, MAATSSCHAPPELIJKE ACTIVITEIT, MEDEWERKER, OPENBARE RUIMTE, SAMENGESTELD INFORMATIEOBJECT, ORGANISATORISCHE EENHEID, PAND, SPOORBAANDEEL, STATUS, SUBJECT, TERREINDEEL, WATERDEEL, WEGDEEL, WIJK, WOONPLAATS, WOZ- DEELOBJECT, WOZ-OBJECT, WOZ-WAARDE of</font>
<font color="#610e6a">ZAKELIJK RECHT (of afleidbare identificatie).</font> |
| naam | AN200 | <font color="#610e6a">De benaming van het OBJECT indien dit een SUBJECT of specialisatie daarvan is.</font> |
| adresBinnenland |  | <font color="#610e6a">De aanduiding van het adres van het OBJECT indien dit adres in Nederland gelegen is.</font> |
| adresBuitenland |  | <font color="#610e6a">De aanduiding van het adres waar specialisaties van het OBJECT zijnde een SUBJECT dan wel een specialisatie daarvan, verblijft dan wel bereikbaar is in het buitenland.</font> |
| kadastraleAanduiding | AN30 | <font color="#610e6a">De kadastrale aanduiding van het OBJECT</font> |
| geometrie | GML | <font color="#610e6a">De minimaal tweedimensionale geometrische representatie van het OBJECT.</font> |
| toelichting |  |  |
| domein | AN200 | Het toepassingsgebied of de sector DOMEIN waarbinnen handhaving op het object plaatsvindt |
| indicatieRisico |  | Indicatie van de risico's van (de uitvoering van activiteiten in) het handhavingsobject op gevolgen voor het handhavingsobject zelf, de daarin aanwezige personen, de omgeving van het handhavingsobject en/of de samenleving. |
| None | Class: "MaatschappelijkeActiviteit" |  |
| None | Class: "NietNatuurlijkPersoon" |  |
| None | Class: "Inrichtingselement" |  |
| huishouden | Class: "Huishouden" |  |
| None | Class: "Ligplaats" |  |
| None | Class: "Buurt" |  |
| None | Class: "Pand" |  |
| None | Class: "Waterdeel" |  |
| None | Class: "Standplaats" |  |
| None | Class: "KadastraalPerceel" |  |
| None | Class: "Vaartuig" |  |
| None | Class: "Ingezetene" |  |
| None | Class: "Standplaats" |  |
| None | Class: "KadastraleOnroerendeZaak" |  |
| None | Class: "Ligplaats" |  |
| None | Class: "Voertuig" |  |
| None | Class: "Kunstwerkdeel" |  |
| None | Class: "OpenbareRuimte" |  |
| None | Class: "OpenbareRuimte" |  |
| besluit | Class: "Besluit" |  |
| None | Class: "Pand" |  |
| None | Class: "Buurt" |  |
| None | Class: "NatuurlijkPersoon" |  |




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
| version | 1.5 |
| created | 2019-11-26 15:21:20 |
| modified | 2025-03-26 16:14:50 |
| id | EAID_B259BE5F_AC3A_4e0f_A149_D1F165277CC2 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Offerte |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-5d23eb2c-f115-4526-a1f7-5f2378666ffa](https://gemmaonline.nl/index.php/GEMMA/id-5d23eb2c-f115-4526-a1f7-5f2378666ffa) |
| gemma_definitie | Aanbod, aanbieding of voorstel van goederen of diensten waarin opgave is gedaan van de prijs. |
| gemma_toelichting |  |


Attributen van objecttype Offerte

| Attribute | Datatype | Description |
| :--- | :--- | :--- |




### OrganisatorischeEenheid
> **Definitie OrganisatorischeEenheid:** 
>
> Het deel van een functioneel afgebakend onderdeel binnen de organisatie dat haar activiteiten uitvoert binnen een VESTIGING VAN ZAAKBEHANDELENDE ORGANISATIE en die verantwoordelijk is voor de behandeling van zaken.

| Eigenschap | Waarde |
| :--- | :------ |
| name | OrganisatorischeEenheid |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | mante_h |
| version | 1.5 |
| created | 2010-08-19 13:30:16 |
| modified | 2025-03-26 16:14:50 |
| id | EAID_936A4E8B_3E5A_44b6_8A5D_EFB39F83FB6D |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | OrganisatorischeEenheid |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-02f66265-00ae-418d-8d0e-dcbaf36652bb](https://gemmaonline.nl/index.php/GEMMA/id-02f66265-00ae-418d-8d0e-dcbaf36652bb) |
| gemma_definitie | Het deel van een functioneel afgebakend onderdeel binnen de organisatie dat haar activiteiten uitvoert binnen een VESTIGING VAN ZAAKBEHANDELENDE ORGANISATIE en die verantwoordelijk is voor de behandeling van zaken. |
| gemma_toelichting |  |


Attributen van objecttype OrganisatorischeEenheid

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| organisatieIdentificatie | AN24 | <font color="#610e6a">Een korte identificatie van de organisatorische eenheid.</font> |
| datumOntstaan |  | <font color="#610e6a">De datum waarop de organisatorische eenheid is ontstaan.</font> |
| datumOpheffing |  | <font color="#610e6a">De datum waarop de organisatorische eenheid is opgeheven.</font> |
| emailadres | AN254 | <font color="#610e6a">Elektronisch postadres waaronder de organisatorische eenheid in de regel bereikbaar is.</font> |
| faxnummer | AN20 | <font color="#610e6a">Faxnummer waaronder de organisatorische eenheid in de regel bereikbaar is.</font> |
| naam | AN50 | <font color="#610e6a">De feitelijke naam van de organisatorische eenheid.</font> |
| naamVerkort | AN25 | <font color="#610e6a">Een verkorte naam voor de organisatorische eenheid.</font> |
| omschrijving | AN80 | <font color="#610e6a">Een omschrijving van de organisatorische eenheid.</font> |
| telefoonnummer | AN20 | <font color="#610e6a">Telefoonnummer waaronder de organisatorische eenheid in de regel bereikbaar is.</font> |
| toelichting | AN1000 | <font color="#610e6a">Toelichting bij de organisatorische eenheid.</font> |
| Formatie |  |  |
| None | Class: "Klantbeoordeling" |  |
| None | Class: "Kostenplaats" |  |
| vestiging | Class: "VestigingVanZaakbehandelendeOrganisatie" |  |
| zaaktype | Class: "Zaaktype" |  |
| None | Class: "OrganisatorischeEenheid" |  |
| None | Class: "Subsidieprogramma" |  |




### SamengesteldDocument
> **Definitie SamengesteldDocument:** 
>
> Een DOCUMENT waarbinnen twee of meer ENKELVOUDIGe DOCUMENTen onderscheiden worden die vanwege gezamenlijke vervaardiging en/of ontvangst en/of vanwege aard en/of omvang als één geheel beschouwd moeten worden dan wel behandeld worden.,

| Eigenschap | Waarde |
| :--- | :------ |
| name | SamengesteldDocument |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | mante_h |
| version | 1.5 |
| created | 2010-08-19 13:42:59 |
| modified | 2025-03-26 16:14:50 |
| id | EAID_47DA1FC8_F181_41bc_B16A_CE80D2CA13B1 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype SamengesteldDocument

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| document | Class: "EnkelvoudigDocument" |  |




### Status
> **Definitie Status:** 
>
> Een aanduiding van de stand van zaken van een zaak op basis van betekenisvol behaald resultaat voor de initiator van de zaak.

| Eigenschap | Waarde |
| :--- | :------ |
| name | Status |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | mante_h |
| version | 1.5 |
| created | 2010-08-19 13:44:49 |
| modified | 2025-03-26 16:14:50 |
| id | EAID_7C975D37_670B_405e_B825_924BCAFA74C7 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Status |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-138f7a81-f370-4e0c-9254-d6c7727a338c](https://gemmaonline.nl/index.php/GEMMA/id-138f7a81-f370-4e0c-9254-d6c7727a338c) |
| gemma_definitie | Een aanduiding van de stand van zaken van een zaak op basis van betekenisvol behaald resultaat voor de initiator van de zaak. |
| gemma_toelichting |  |


Attributen van objecttype Status

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| datumStatusGezet |  | <font color="#610e6a">De datum waarop de zaak de status heeft verkregen.</font> |
| statustoelichting | AN1000 | <font color="#610e6a">Een, voor de initiator van de zaak relevante, toelichting op de status van een zaak.</font> |
| indicatieIaatstGezetteStatus | AN1 | <font color="#610e6a">Aanduding of het de laatst bekende bereikte status betreft.</font> |
| type | Class: "Statustype" |  |




### Statustype
> **Definitie Statustype:** 
>
> Generieke aanduiding van de aard van een STATUS

| Eigenschap | Waarde |
| :--- | :------ |
| name | Statustype |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | mante_h |
| version | 1.5 |
| created | 2010-08-19 13:47:35 |
| modified | 2025-03-26 16:14:51 |
| id | EAID_AA496B7B_913C_40fd_943E_52F1A6E89440 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Statustype

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| statustypeOmschrijving | AN80 | <font color="#610e6a">Een korte, voor de initiator van de zaak relevante, omschrijving van de aard van de STATUS van zaken van een ZAAKTYPE.</font> |
| statustypeVolgnummer | N4 | <font color="#610e6a">Een volgnummer voor de status binnen een zaak.</font> |
| doorlooptijdStatus | N3 | <font color="#610e6a">De door de zaakbehandelende organisatie(s) gestelde norm voor de doorlooptijd voor het bereiken van STATUSsen van dit STATUSTYPE bij het desbetreffende ZAAKTYPE.</font> |
| statustypeOmschrijvingGeneriek | AN80 | <font color="#610e6a">Algemeen gehanteerde omschrijving van de aard van STATUSsen van het STATUSTYPE</font> |
| datumBeginGeldigheidStatustype | OnvolledigeDatum | <font color="#610e6a">De datum waarop het STATUSTYPE is ontstaan.</font> |
| datumEindeGeldigheidStatustype | OnvolledigeDatum | <font color="#610e6a">De datum waarop het STATUSTYPE is opgeheven.</font> |




### VestigingVanZaakbehandelendeOrganisatie
> **Definitie VestigingVanZaakbehandelendeOrganisatie:** 
>
> Een VESTIGING van een onderneming of rechtspersoon zijnde de zaakbehandelende organisatie.

| Eigenschap | Waarde |
| :--- | :------ |
| name | VestigingVanZaakbehandelendeOrganisatie |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | mante_h |
| version | 1.5 |
| created | 2010-08-19 11:03:44 |
| modified | 2025-03-26 16:14:51 |
| id | EAID_D8142B98_64CB_408e_9941_92423543F08A |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | VestigingVanZaakbehandelendeOrganisatie |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-bb257165-3229-4e5f-a24c-524966c748f5](https://gemmaonline.nl/index.php/GEMMA/id-bb257165-3229-4e5f-a24c-524966c748f5) |
| gemma_definitie | Een VESTIGING van een onderneming of rechtspersoon zijnde de zaakbehandelende organisatie. |
| gemma_toelichting |  |


Attributen van objecttype VestigingVanZaakbehandelendeOrganisatie

| Attribute | Datatype | Description |
| :--- | :--- | :--- |




### Zaak
> **Definitie Zaak:** 
>
> Een samenhangende hoeveelheid werk met een welgedefinieerde aanleiding en een welgedefinieerd eindresultaat, waarvan kwaliteit en doorlooptijd bewaakt moeten worden.

| Eigenschap | Waarde |
| :--- | :------ |
| name | Zaak |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | mante_h |
| version | 1.5 |
| created | 2010-08-19 13:48:52 |
| modified | 2025-04-09 16:59:38 |
| id | EAID_649EFD86_ED52_4293_8577_DBE5445845BF |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Zaak |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-7d5124d4-f23d-432d-ad5a-dc7c1b0fac44](https://gemmaonline.nl/index.php/GEMMA/id-7d5124d4-f23d-432d-ad5a-dc7c1b0fac44) |
| gemma_definitie | Een samenhangende hoeveelheid werk met een welgedefinieerde aanleiding en een welgedefinieerd eindresultaat, waarvan kwaliteit en doorlooptijd bewaakt moeten worden. |
| gemma_toelichting |  |


Attributen van objecttype Zaak

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| document |  |  |
| None |  |  |
| zaakidentificatie | AN40 | <font color="#610e6a">Een identificatie van de zaak.</font> |
| datumEinde |  | <font color="#610e6a">De datum waarop de uitvoering van de zaak afgerond is.</font> |
| datumEindeGepland |  | <font color="#610e6a">De datum waarop volgens de planning verwacht wordt dat de zaak afgerond wordt.</font> |
| omschrijving | AN80 | <font color="#610e6a">Een korte omschrijving van de zaak.</font> |
| omschrijvingResultaat | AN80 | <font color="#610e6a">Een korte omschrijving wat het resultaat van de zaak inhoudt.</font> |
| toelichtingResultaat | AN1000 | <font color="#610e6a">Een toelichting op wat het resultaat van de zaak inhoudt.</font> |
| datumStart |  | <font color="#610e6a">De datum waarop met de uitvoering van de zaak is gestart.</font> |
| toelichting | AN1000 | <font color="#610e6a">Een toelichting op de zaak.</font> |
| datumEindeUiterlijkeAfdoening |  | <font color="#610e6a">De laatste datum waarop volgens wet- en regelgeving de zaak afgerond dient te zijn.</font> |
| zaakniveau | N1 | <font color="#610e6a">Het niveau van een ZAAK in de hierarchie van hoofdzaak met deelzaken.</font> |
| indicatieDeelzaken | A1 | <font color="#610e6a">De aanduiding of een ZAAK behandeld wordt in deelzaken.</font> |
| datumRegistratie |  | <font color="#610e6a">De datum waarop de zaakbehandelende organisatie de ZAAK heeft geregistreerd</font> |
| datumPublicatie | datum | <font color="#610e6a">Datum waarop (het starten van) de zaak gepubliceerd is of wordt.</font> |
| archiefnominatie | AN1 | <font color="#610e6a">Indicatie of het zaakdossier (de ZAAK met alle bijbehorende DOCUMENTen) gearchiveerd dient te worden</font> |
| datumVernietigingDossier |  | <font color="#610e6a">De datum waarop het, al dan niet gearchiveerde, zaakdossier (de ZAAK met alle bijbehorende DOCUMENTen) vernietigd mag worden.</font> |
| indicatieBetaling | AN12 | <font color="#610e6a">Indicatie of de, met behandeling van de zaak gemoeide, kosten betaald zijn door de desbetreffende betrokkene.</font> |
| datumLaatsteBetaling |  | <font color="#610e6a">De datum waarop de meest recente betaling is verwerkt van kosten die gemoeid zijn met behandeling van de zaak.</font> |
| indicatieOpschorting | AN1 |  |
| duurVerlenging | N3 |  |
| redenOpschorting | AN200 |  |
| redenVerlenging | AN200 |  |
| vertrouwelijkheid | AN40 |  |
| leges | AN100 |  |
| None | Class: "Zaak" |  |
| type | Class: "Zaaktype" |  |
| None | Class: "Klantbeoordeling" |  |
| None | Class: "Medewerker" |  |
| None | Class: "Producttype" |  |
| None | Class: "Zaak" |  |
| None | Class: "Project" |  |
| None | Class: "Heffing" |  |
| status | Class: "Status" |  |
| None | Class: "Grondslag" |  |




### ZAAK - Origineel
> **Definitie ZAAK - Origineel:** 
>
> Een samenhangende hoeveelheid werk met een welgedefinieerde aanleiding en een welgedefinieerd eindresultaat, waarvan kwaliteit en doorlooptijd bewaakt moeten worden.

| Eigenschap | Waarde |
| :--- | :------ |
| name | ZAAK - Origineel |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | mante_h |
| version | 1.5 |
| created | 2018-05-28 13:18:59 |
| modified | 2025-03-26 16:14:51 |
| id | EAID_766265DF_56DD_4560_A55C_FF82E3B9751A |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | ZaakOrigineel |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-ce925d18-fde7-4bd6-9865-a7030a276a3c](https://gemmaonline.nl/index.php/GEMMA/id-ce925d18-fde7-4bd6-9865-a7030a276a3c) |
| gemma_definitie | Een samenhangende hoeveelheid werk met een welgedefinieerde aanleiding en een welgedefinieerd eindresultaat, waarvan kwaliteit en doorlooptijd bewaakt moeten worden. |
| gemma_toelichting |  |


Attributen van objecttype ZAAK - Origineel

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| zaakidentificatie | AN40 | <font color="#610e6a">Een identificatie van de zaak.</font> |
| datumEinde |  | <font color="#610e6a">De datum waarop de uitvoering van de zaak afgerond is.</font> |
| datumEindeGepland |  | <font color="#610e6a">De datum waarop volgens de planning verwacht wordt dat de zaak afgerond wordt.</font> |
| omschrijving | AN80 | <font color="#610e6a">Een korte omschrijving van de zaak.</font> |
| kenmerk |  |  |
| omschrijvingResultaat | AN80 | <font color="#610e6a">Een korte omschrijving wat het resultaat van de zaak inhoudt.</font> |
| toelichtingResultaat | AN1000 | <font color="#610e6a">Een toelichting op wat het resultaat van de zaak inhoudt.</font> |
| datumStart |  | <font color="#610e6a">De datum waarop met de uitvoering van de zaak is gestart.</font> |
| toelichting | AN1000 | <font color="#610e6a">Een toelichting op de zaak.</font> |
| datumEindeUiterlijkeAfdoening |  | <font color="#610e6a">De laatste datum waarop volgens wet- en regelgeving de zaak afgerond dient te zijn.</font> |
| zaakniveau | N1 | <font color="#610e6a">Het niveau van een ZAAK in de hierarchie van hoofdzaak met deelzaken.</font> |
| indicatieDeelzaken | A1 | <font color="#610e6a">De aanduiding of een ZAAK behandeld wordt in deelzaken.</font> |
| datumRegistratie |  | <font color="#610e6a">De datum waarop de zaakbehandelende organisatie de ZAAK heeft geregistreerd</font> |
| datumPublicatie | datum | <font color="#610e6a">Datum waarop (het starten van) de zaak gepubliceerd is of wordt.</font> |
| archiefnominatie | AN1 | <font color="#610e6a">Indicatie of het zaakdossier (de ZAAK met alle bijbehorende DOCUMENTen) gearchiveerd dient te worden</font> |
| datumVernietigingDossier |  | <font color="#610e6a">De datum waarop het, al dan niet gearchiveerde, zaakdossier (de ZAAK met alle bijbehorende DOCUMENTen) vernietigd mag worden.</font> |
| indicatieBetaling | AN12 | <font color="#610e6a">Indicatie of de, met behandeling van de zaak gemoeide, kosten betaald zijn door de desbetreffende betrokkene.</font> |
| datumLaatsteBetaling |  | <font color="#610e6a">De datum waarop de meest recente betaling is verwerkt van kosten die gemoeid zijn met behandeling van de zaak.</font> |
| opschorting |  |  |
| verlenging |  |  |
| anderZaakobject |  |  |
| None | Class: "ZAAK - Origineel" |  |
| None | Class: "ZAAK - Origineel" |  |




### Zaaktype
> **Definitie Zaaktype:** 
>
> Generieke aanduiding van de aard van een zaak

| Eigenschap | Waarde |
| :--- | :------ |
| name | Zaaktype |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | mante_h |
| version | 1.5 |
| created | 2010-08-19 13:54:55 |
| modified | 2025-03-26 16:14:51 |
| id | EAID_7210A379_17EE_4143_A106_ECD9414B2A0D |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Zaaktype

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| zaaktypeOmschrijving | AN80 | <font color="#610e6a">Omschrijving van de aard van ZAAKen van het ZAAKTYPE.</font> |
| zaaktypeOmschrijvingGeneriek | AN80 | <font color="#610e6a">Algemeen gehanteerde omschrijving van de aard van ZAAKen van het ZAAKTYPE</font> |
| trefwoord | AN30 | <font color="#610e6a">Een trefwoord waarmee ZAAKen van het ZAAKTYPE kunnen worden gekarakteriseerd.</font> |
| doorlooptijdBehandeling | N3 | <font color="#610e6a">De periode waarbinnen volgens wet- en regelgeving een ZAAk van het ZAAKTYPE afgerond dient te zijn.</font> |
| servicenormBehandeling | N3 | <font color="#610e6a">De periode waarbinnen verwacht wordt dat een ZAAk van het ZAAKTYPE afgerond wordt coform de geldende servicenormen van de zaakbehandelende organisatie(s).</font> |
| archiefcode | AN20 | <font color="#610e6a">De systematische identificatie van zaakdossiers van dit ZAAKTYPE overeenkomstig logisch gestructureerde conventies, methoden en procedureregels.</font> |
| vertrouwelijkAanduiding | AN20 | <font color="#610e6a">Aanduiding van de mate waarin zaakdossiers van ZAAKen van dit ZAAKTYPE voor de openbaarheid bestemd zijn.</font> |
| indicatiePublicatie | AN1 | <font color="#610e6a">Aanduiding of (het starten van) een ZAAK van dit ZAAKTYPE gepubliceerd moet worden.</font> |
| zaakcategorie | AN40 | <font color="#610e6a">Typering van de aard van ZAAKen van het ZAAKTYPE.</font> |
| publicatietekst | AN1000 | <font color="#610e6a">De generieke tekst van de publicatie van ZAAKen van dit ZAAKTYPE</font> |
| datumBeginGeldigheidZaaktype | OnvolledigeDatum | <font color="#610e6a">De datum waarop het ZAAKTYPE is ontstaan.</font> |
| datumEindeGeldigheidZaaktype | OnvolledigeDatum | <font color="#610e6a">De datum waarop het ZAAKTYPE is opgeheven.</font> |
| None | Class: "Heffinggrondslag" |  |
| statustype | Class: "Statustype" |  |
| None | Class: "Product" |  |







## Enumeraties Model Kern RGBZ


### Boolean
Geen Definitie

Het enumeratie Boolean kent de volgende waarden:

* **Ja**: <Geen Definities>
* **Nee**: <Geen Definities>
* **Onbekend**: <Geen Definities>
* **Leeg**: <Geen Definities>


De enumeratie Boolean heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | Boolean |
| toelichting | None |
| synoniemen | None |
| uri | None |
| bron | None |
| author | None |
| version | 1.4 |
| created | 2025-03-26 11:13:35 |
| modified | 2025-03-26 16:14:54 |
| id | EAID_6bb85136_e0ef_49f3_8aa4_487494219352 |
| domein_iv3 | None |
| domein_dcat | None |
| gemma_naam | None |
| gemma_type | None |
| gemma_url | None |
| gemma_definitie | None |
| gemma_toelichting | None |



### Heffingsoort
Geen Definitie

Het enumeratie Heffingsoort kent de volgende waarden:

* **leges**: <Geen Definities>
* **precario**: <Geen Definities>


De enumeratie Heffingsoort heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | Heffingsoort |
| toelichting | None |
| synoniemen | None |
| uri | None |
| bron | None |
| author | None |
| version | 1.5 |
| created | 2025-03-26 11:12:42 |
| modified | 2025-03-26 16:14:35 |
| id | EAID_84831614_34c2_44c8_922c_a080218c6fc7 |
| domein_iv3 | None |
| domein_dcat | None |
| gemma_naam | None |
| gemma_type | None |
| gemma_url | None |
| gemma_definitie | None |
| gemma_toelichting | None |



### Soorten Klantcontact
Geen Definitie

Het enumeratie Soorten Klantcontact kent de volgende waarden:

* **internet**: <Geen Definities>
* **balie**: <Geen Definities>
* **selfserviceloket**: <Geen Definities>
* **telefonisch**: <Geen Definities>
* **brief**: <Geen Definities>


De enumeratie Soorten Klantcontact heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | Soorten Klantcontact |
| toelichting | None |
| synoniemen | None |
| uri | None |
| bron | None |
| author | None |
| version | 1.5 |
| created | 2025-03-26 11:13:26 |
| modified | 2025-03-26 16:14:51 |
| id | EAID_36c4a83f_4118_401e_8d11_118ee9aa4bb5 |
| domein_iv3 | None |
| domein_dcat | None |
| gemma_naam | None |
| gemma_type | None |
| gemma_url | None |
| gemma_definitie | None |
| gemma_toelichting | None |




