# Model Parkeren
## Inleiding
> **Definitie Model Parkeren:** 
>
> Geen definitie

Het model 'Model Parkeren' kent de volgende objecttypen:

* **Belprovider**: Leverancier of dienstverlener van modiele beldiensten
* **MulderFeit**: <Geen Definities>
* **Naheffing**: Het achteraf vorderen van te weinig betaalde belasting 
* **Parkeergarage**: Open constructie die geheel of gedeeltelijk in gebruik is als voorziening voor het parkeren van voertuigen
* **Parkeerrecht**: Het onder bepaalde voorwaarden (zoals betaling parkeerbelasting of parkeergeld) ontstane recht om een voertuig gedurende een bepaalde of onbepaalde periode op een daartoe benoemde parkeerplaats of in/op een daartoe benoemde parkeervoorziening te parkeren.
* **Parkeerscan**: Waarneming van een parkeeractie door een scanauto
* **Parkeervergunning**: Officiele toestemming dat je op een bepaalde plek mag parkeren
* **Parkeervlak**: Parkeergelegenheid bestemd voor het parkeren van een of meerdere voertuigen direct langs de doorgaande weg gelegen.
* **Perkeerzone**: <Geen Definities>
* **Productgroep**: Groepering van producten
* **Productsoort**: Typologie van een product
* **Straatsectie**: Gedeelte van een straat
* **Voertuig**: Vervoermiddel bestemd voor het verkeer over wegen


Het model 'Model Parkeren' heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | Model Parkeren |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2019-02-13 13:34:38 |
| modified | 2019-02-13 13:34:38 |
| id | EAPK_13EDB396_DEDA_41f8_B4D8_68EBB2D5EF64 |


## Objecttypen Model Parkeren


### Belprovider
> **Definitie Belprovider:** 
>
> Leverancier of dienstverlener van modiele beldiensten

| Eigenschap | Waarde |
| :--- | :------ |
| name | Belprovider |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2019-02-13 15:52:28 |
| modified | 2024-04-17 13:34:24 |
| id | EAID_6C283ABA_C1A3_465b_B267_39E75D06E41F |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Belprovider |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA2/0.9/id-59bf814b-1020-4906-978b-ca22af2eecc0](https://gemmaonline.nl/index.php/GEMMA2/0.9/id-59bf814b-1020-4906-978b-ca22af2eecc0) |
| gemma_definitie | Leverancier of dienstverlener van modiele beldiensten |
| gemma_toelichting |  |


Attributen van objecttype Belprovider

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| code | AN40 |  |




### MulderFeit
> **Definitie MulderFeit:** 
>
> Geen Definitie

| Eigenschap | Waarde |
| :--- | :------ |
| name | MulderFeit |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2019-02-18 14:18:39 |
| modified | 2024-04-17 13:34:24 |
| id | EAID_4EA4D754_FAD7_4caf_8060_342689EC16FE |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype MulderFeit

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| bedrag | Bedrag |  |
| bezwaarAfgehandeld | Date |  |
| bezwaarIngetrokken | Date |  |
| bezwaarToegewezen | Date |  |
| bonnummer | int |  |
| datumBetaling | Date |  |
| datumBezwaar | Date |  |
| datumGeseponeerd | Date |  |
| datumIndiening | Date |  |
| dienstCD | AN40 |  |
| organisatie | AN200 |  |
| overtreding | AN80 |  |
| parkeertarief | Bedrag |  |
| redenSeponeren | AN300 |  |
| vorderingnummer | int |  |
| None | Class: "Voertuig" |  |




### Naheffing
> **Definitie Naheffing:** 
>
> Het achteraf vorderen van te weinig betaalde belasting 

| Eigenschap | Waarde |
| :--- | :------ |
| name | Naheffing |
| toelichting |  |
| synoniemen | Navordering |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2019-02-13 16:05:29 |
| modified | 2024-04-17 13:34:24 |
| id | EAID_4957AC99_3F36_4959_A210_9EC6759B87F8 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Naheffing |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA2/0.9/id-d10d2101-2e16-4f56-bcce-43783fd256be](https://gemmaonline.nl/index.php/GEMMA2/0.9/id-d10d2101-2e16-4f56-bcce-43783fd256be) |
| gemma_definitie | Het achteraf vorderen van te weinig betaalde belasting |
| gemma_toelichting |  |


Attributen van objecttype Naheffing

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| bedrag | Bedrag |  |
| bezwaarAfgehandeld | Date |  |
| bezwaarIngetrokken | Date |  |
| bezwaarToegewezen | Date |  |
| bonnummer | int |  |
| datumBetaling | Date |  |
| datumBezwaar | Date |  |
| datumGeseponeerd | Date |  |
| datumIndiening | Date |  |
| dienstCD | AN40 |  |
| fiscaal | boolean |  |
| organisatie | AN200 |  |
| overtreding | AN80 |  |
| parkeertarief | Bedrag |  |
| redenSeponeren | AN300 |  |
| vorderingnummer | int |  |




### Parkeergarage
> **Definitie Parkeergarage:** 
>
> Open constructie die geheel of gedeeltelijk in gebruik is als voorziening voor het parkeren van voertuigen

| Eigenschap | Waarde |
| :--- | :------ |
| name | Parkeergarage |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2019-02-14 16:11:43 |
| modified | 2024-04-17 13:34:24 |
| id | EAID_8F492648_6EF2_4f8a_87C9_2440230D4137 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Parkeergarage |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA2/0.9/id-3aed2196-8ba9-4441-a27f-15a1f76d3fda](https://gemmaonline.nl/index.php/GEMMA2/0.9/id-3aed2196-8ba9-4441-a27f-15a1f76d3fda) |
| gemma_definitie | Open constructie die geheel of gedeeltelijk in gebruik is als voorziening voor het parkeren van voertuigen |
| gemma_toelichting |  |


Attributen van objecttype Parkeergarage

| Attribute | Datatype | Description |
| :--- | :--- | :--- |




### Parkeerrecht
> **Definitie Parkeerrecht:** 
>
> Het onder bepaalde voorwaarden (zoals betaling parkeerbelasting of parkeergeld) ontstane recht om een voertuig gedurende een bepaalde of onbepaalde periode op een daartoe benoemde parkeerplaats of in/op een daartoe benoemde parkeervoorziening te parkeren.

| Eigenschap | Waarde |
| :--- | :------ |
| name | Parkeerrecht |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2019-02-13 14:32:45 |
| modified | 2024-04-17 13:34:24 |
| id | EAID_9E0936E5_6B50_4205_BA5D_FEB80486D6F1 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Parkeerrecht |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA2/0.9/id-ae658af8-46be-4d41-ba95-c5e24cec7598](https://gemmaonline.nl/index.php/GEMMA2/0.9/id-ae658af8-46be-4d41-ba95-c5e24cec7598) |
| gemma_definitie | Het onder bepaalde voorwaarden (zoals betaling parkeerbelasting of parkeergeld) ontstane recht om een voertuig gedurende een bepaalde of onbepaalde periode op een daartoe benoemde parkeerplaats of in/op een daartoe benoemde parkeervoorziening te parkeren. |
| gemma_toelichting |  |


Attributen van objecttype Parkeerrecht

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| aanmaaktijd | DateTime |  |
| bedragAankoop | Bedrag |  |
| bedragBTW | Bedrag |  |
| datumtijdEinde | DateTime |  |
| datumtijdStart | DateTime |  |
| productnaam | AN80 |  |
| productomschrijving | Text |  |
| None | Class: "Voertuig" |  |
| None | Class: "Perkeerzone" |  |




### Parkeerscan
> **Definitie Parkeerscan:** 
>
> Waarneming van een parkeeractie door een scanauto

| Eigenschap | Waarde |
| :--- | :------ |
| name | Parkeerscan |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2019-02-13 14:50:52 |
| modified | 2024-04-17 13:34:25 |
| id | EAID_653EEEA7_ED82_427d_BD72_86C847793AD6 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Parkeerscan |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA2/0.9/id-078d57f3-e8a0-485e-a175-c1b3de49eee0](https://gemmaonline.nl/index.php/GEMMA2/0.9/id-078d57f3-e8a0-485e-a175-c1b3de49eee0) |
| gemma_definitie | Waarneming van een parkeeractie door een scanauto |
| gemma_toelichting |  |


Attributen van objecttype Parkeerscan

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| codeGebruiker | AN40 |  |
| codeScanvoertuig | AN40 |  |
| coordinaten | GML |  |
| foto | BLOB |  |
| kenteken | AN12 |  |
| parkeerrecht | boolean |  |
| tijdstip | DateTime |  |
| transactieID | AN40 |  |
| None | Class: "MEDEWERKER" |  |
| None | Class: "Voertuig" |  |
| None | Class: "Parkeervlak" |  |
| None | Class: "Parkeerrecht" |  |




### Parkeervergunning
> **Definitie Parkeervergunning:** 
>
> Officiele toestemming dat je op een bepaalde plek mag parkeren

| Eigenschap | Waarde |
| :--- | :------ |
| name | Parkeervergunning |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2018-03-21 11:47:02 |
| modified | 2024-04-17 13:34:25 |
| id | EAID_FF448272_AB9D_4ec9_B4BE_E60E2552817A |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Parkeervergunning |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA2/0.9/id-1486de79-ad71-4dce-8473-f23f1e9c436c](https://gemmaonline.nl/index.php/GEMMA2/0.9/id-1486de79-ad71-4dce-8473-f23f1e9c436c) |
| gemma_definitie | Offici√´le toestemming dat je op een bepaalde plek mag parkeren |
| gemma_toelichting |  |


Attributen van objecttype Parkeervergunning

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| datumEindeGeldigheid | DateTime |  |
| datumReservering | Date |  |
| datumStart | DateTime |  |
| kenteken | AN12 |  |
| minutenAfgeschreven | int |  |
| minutenGeldig | int |  |
| minutenResterend | int |  |
| nummer | int |  |
| type | AN40 |  |
| None | Class: "Parkeerrecht" |  |
| None | Class: "Perkeerzone" |  |
| None | Class: "Productgroep" |  |
| None | Class: "Productsoort" |  |




### Parkeervlak
> **Definitie Parkeervlak:** 
>
> Parkeergelegenheid bestemd voor het parkeren van een of meerdere voertuigen direct langs de doorgaande weg gelegen.

| Eigenschap | Waarde |
| :--- | :------ |
| name | Parkeervlak |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2019-02-13 14:43:35 |
| modified | 2024-04-17 13:34:25 |
| id | EAID_5E5C58AD_1634_4656_A183_EBA00F18F30E |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Parkeervlak |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA2/0.9/id-30d7e3ac-081c-4ef6-a09e-90437b5a4349](https://gemmaonline.nl/index.php/GEMMA2/0.9/id-30d7e3ac-081c-4ef6-a09e-90437b5a4349) |
| gemma_definitie | Parkeergelegenheid bestemd voor het parkeren van √©√©n of meerdere voertuigen direct langs de doorgaande weg gelegen. |
| gemma_toelichting |  |


Attributen van objecttype Parkeervlak

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| aantal | int |  |
| coordinaten | GML |  |
| doelgroep | Enumeratie: "Doelgroepenplaatsen" |  |
| fiscaal | boolean |  |
| plaats | AN200 |  |
| vlakID | AN40 |  |




### Perkeerzone
> **Definitie Perkeerzone:** 
>
> Geen Definitie

| Eigenschap | Waarde |
| :--- | :------ |
| name | Perkeerzone |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2019-02-13 14:33:20 |
| modified | 2024-04-17 13:34:25 |
| id | EAID_27219A32_3B52_4f54_AA67_A972F4B7D9D0 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Perkeerzone |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA2/0.9/id-e5293eea-47b8-4091-8ac3-b28139a17c9f](https://gemmaonline.nl/index.php/GEMMA2/0.9/id-e5293eea-47b8-4091-8ac3-b28139a17c9f) |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Perkeerzone

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| aantalParkeervlakken | int |  |
| alleenDagtarief | boolean |  |
| dagtarief | Bedrag |  |
| eindedag | AN20 |  |
| eindtijd | int |  |
| gebruik | AN250 |  |
| geometrie | Multivlak |  |
| IPMCode | AN40 |  |
| IPMNaam | AN250 |  |
| naam | AN250 |  |
| parkeergarage | boolean |  |
| sectorcode | AN40 |  |
| soortCode | An40 |  |
| startdag | AN20 |  |
| starttarief | Bedrag |  |
| starttijd | int |  |
| typeCode | AN40 |  |
| typeNaam | AN250 |  |
| uurtarief | Bedrag |  |




### Productgroep
> **Definitie Productgroep:** 
>
> Groepering van producten

| Eigenschap | Waarde |
| :--- | :------ |
| name | Productgroep |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2019-02-14 14:26:09 |
| modified | 2024-04-17 13:34:25 |
| id | EAID_209ACADD_34C7_4dc8_90AD_C6B3E092FBFD |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Productgroep

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| beslisboom | AN250 |  |
| code | AN40 |  |
| omschrijving | AN250 |  |




### Productsoort
> **Definitie Productsoort:** 
>
> Typologie van een product

| Eigenschap | Waarde |
| :--- | :------ |
| name | Productsoort |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2019-02-14 15:08:29 |
| modified | 2024-04-17 13:34:25 |
| id | EAID_1CB4051D_B78A_48f0_AE3E_A98D997A5612 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Productsoort

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| code | AN40 |  |
| omschrijving | AN250 |  |
| tarief | Bedrag |  |
| tariefperiode | AN20 |  |




### Straatsectie
> **Definitie Straatsectie:** 
>
> Gedeelte van een straat

| Eigenschap | Waarde |
| :--- | :------ |
| name | Straatsectie |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2019-02-13 14:46:01 |
| modified | 2024-04-17 13:34:25 |
| id | EAID_339ACCD5_1D13_4a48_83DE_05A0A4A54C43 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Straatsectie

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| code | AN40 |  |
| omschrijving | AN500 |  |
| zoneCode | Enumeratie: "Zonesoort" |  |




### Voertuig
> **Definitie Voertuig:** 
>
> Vervoermiddel bestemd voor het verkeer over wegen

| Eigenschap | Waarde |
| :--- | :------ |
| name | Voertuig |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2019-02-13 14:31:44 |
| modified | 2024-04-17 13:34:25 |
| id | EAID_6AD98160_FFE6_4105_A724_5D5733C87CD8 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Voertuig |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA2/0.9/id-b083bd60-0137-40b0-ad72-4602b3c1d754](https://gemmaonline.nl/index.php/GEMMA2/0.9/id-b083bd60-0137-40b0-ad72-4602b3c1d754) |
| gemma_definitie | Vervoermiddel bestemd voor het verkeer over wegen |
| gemma_toelichting |  |


Attributen van objecttype Voertuig

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| kenteken | AN12 |  |
| kleur | AN200 |  |
| land | AN200 |  |
| merk | AN200 |  |
| type | AN200 |  |







## Enumeraties Model Parkeren


### Doelgroepenplaatsen
Geen Definitie

Het enumeratie Doelgroepenplaatsen kent de volgende waarden:

* **DP01**: <Geen Definities>
* **DP02**: <Geen Definities>
* **DP03**: <Geen Definities>
* **DP04**: <Geen Definities>
* **DP05**: <Geen Definities>
* **Leeg**: <Geen Definities>


De enumeratie Doelgroepenplaatsen heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | Doelgroepenplaatsen |
| toelichting | None |
| synoniemen | None |
| uri | None |
| bron | None |
| author | None |
| version | None |
| created | None |
| modified | None |
| id | EAID_F8ADD9AF_76C0_425c_B059_18BB0AA20D28 |
| domein_iv3 | None |
| domein_dcat | None |
| gemma_naam | None |
| gemma_type | None |
| gemma_url | None |
| gemma_definitie | None |
| gemma_toelichting | None |



### Zonesoort
Geen Definitie

Het enumeratie Zonesoort kent de volgende waarden:

* **GSM-Zone**: <Geen Definities>
* **Vergunninghouderzone**: <Geen Definities>


De enumeratie Zonesoort heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | Zonesoort |
| toelichting | None |
| synoniemen | None |
| uri | None |
| bron | None |
| author | None |
| version | None |
| created | None |
| modified | None |
| id | EAID_5DD4AE03_667C_45b9_A46A_320077AC2926 |
| domein_iv3 | None |
| domein_dcat | None |
| gemma_naam | None |
| gemma_type | None |
| gemma_url | None |
| gemma_definitie | None |
| gemma_toelichting | None |




