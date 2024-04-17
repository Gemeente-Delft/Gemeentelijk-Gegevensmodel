# Model Dienstverlening
## Inleiding
> **Definitie Model Dienstverlening:** 
>
> Geen definitie

Het model 'Model Dienstverlening' kent de volgende objecttypen:

* **Aanvraagdata**: Bron: GEN_REQ_DATA ID: REQ_DATA icm VELD_NAAM
* **AanvraagOfMelding**: Komt overeen met een VJV  Bron: GEM_VJV (Distinct op REQ_ID) ID: REQ_ID
* **Afspraakstatus**: <Geen Definities>
* **Artikel**: Tekst die is gemaakt om gepubliceerd te worden als een onafhankelijk deel van een tijdschrift, krant, encyclopedie of ander werk
* **Balieafspraak**: Balieafspraken zijn afspraken voor een klantcontact. Dit ongeacht of deze werkelijk heeft plaatsgevonden of gaat plaatsvinden, soms liggen deze in de toekomst of is iemand niet op komen dagen, of iets anders waardoor het klantcontact nog niet heeft plaatsgevonden.
* **ExterneBron**: Bron buiten de eigen organisatie
* **Formuliersoort**: Bron: GEM_FORM ID: FORM_ID
* **Formuliersoortveld**: Bron: GEM_VELD ID: FORM_ID en VELD_NAAM
* **Klantbeoordeling**: <Geen Definities>
* **Klantbeoordelingreden**: <Geen Definities>
* **MORAanvraagOfMelding**: <Geen Definities>
* **Onderwerp**: Bron: GEM_VJV_ONDERWERP ID: ONDERWERP_ID
* **ProductOfDienst**: Bron: QP_CALENDAR.CFM_SERVICES
* **Telefoononderwerp**: <Geen Definities>
* **Telefoonstatus**:   ABANDONEDALERTING: “Opgehangen tijdens overgaan telefoon”  DROPPEDCANCELED: “Opgehangen door systeem”  ABANDONEDQUEUED: “Opgehangen tijdens wachten, zonder boodschap. ”  CONNECTEDDIRECT: “Direct verbonden”  CONNECTEDQUEUEDANNOUNCE: “Verbonden na wachtrij met boodschap”  AbandonedQUEUEDANNOUNCE: “Opgehangen in wachtrij met boodschap”  DroppedBusy: “Opgehangen door systeem, te druk”  REJECTED: “Geweigerd door systeem”  Droppedoverload: “Opgehangen door systeem vanwege overbelasting” 
* **Telefoontje**: De telefoontjes zijn alle keren dat iemand naar de gemeente belt en het telefoonsysteem neemt deze telefoontjes aan. Ongeacht of iemand daarna ophangt, door het systeem uit de wachtrij wordt gezet, doorverbonden wordt met een derde partij of er werkelijk wordt opgenomen.     


Het model 'Model Dienstverlening' heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | Model Dienstverlening |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | crossover |
| version | 1.0 |
| created | 2018-04-16 13:48:36 |
| modified | 2018-06-07 09:58:07 |
| id | EAPK_7F780248_C88C_450f_8318_98C5020AB372 |


## Objecttypen Model Dienstverlening


### Aanvraagdata
> **Definitie Aanvraagdata:** 
>
> Bron: GEN_REQ_DATA
> ID: REQ_DATA icm VELD_NAAM

| Eigenschap | Waarde |
| :--- | :------ |
| name | Aanvraagdata |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | crossover |
| version | 1.0 |
| created | 2018-04-25 16:41:17 |
| modified | 2024-04-17 13:34:46 |
| id | EAID_1F68C981_7E16_4368_8867_CA00AEB08A04 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Aanvraagdata |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA2/0.9/id-6f15e2ca-531d-4879-b087-f43559d8c3fd](https://gemmaonline.nl/index.php/GEMMA2/0.9/id-6f15e2ca-531d-4879-b087-f43559d8c3fd) |
| gemma_definitie | Bron: GEN_REQ_DATA ID: REQ_DATA icm VELD_NAAM |
| gemma_toelichting |  |


Attributen van objecttype Aanvraagdata

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| data | Tekst |  |
| veld | AN40 |  |




### AanvraagOfMelding
> **Definitie AanvraagOfMelding:** 
>
> Komt overeen met een VJV
> 
> Bron: GEM_VJV (Distinct op REQ_ID)
> ID: REQ_ID

| Eigenschap | Waarde |
| :--- | :------ |
| name | AanvraagOfMelding |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2018-04-16 14:11:57 |
| modified | 2024-04-17 13:34:46 |
| id | EAID_8E6BAEF8_1878_400f_9244_23575BD41EAB |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | AanvraagOfMelding |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA2/0.9/id-f14fa1cf-f2c7-4bd6-862d-28ff1616a882](https://gemmaonline.nl/index.php/GEMMA2/0.9/id-f14fa1cf-f2c7-4bd6-862d-28ff1616a882) |
| gemma_definitie | Komt overeen met een VJV  Bron: GEM_VJV (Distinct op REQ_ID) ID: REQ_ID |
| gemma_toelichting |  |


Attributen van objecttype AanvraagOfMelding

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| afgehandeld | Boolean |  |
| categorie | AN200 |  |
| categoriecode | AN80 |  |
| datumAanmaak | Date |  |
| datumAfhandeling | Date |  |
| datumBeginStatus | Date |  |
| datumEindeStatus | Date |  |
| hoofdcategorie | AN80 |  |
| hoofdcategoriecode | AN80 |  |
| identificatie | AN40 |  |
| kanaal | AN80 |  |
| onderwerp | AN200 |  |
| onderwerpcode | AN80 |  |
| soort | AN80 |  |
| status | AN80 |  |
| statuscode | AN80 |  |
| statusVolgorde | AN80 |  |
| subcategorie | AN200 |  |
| subcategoriecode | AN80 |  |
| None | Class: "ZAAK" |  |




### Afspraakstatus
> **Definitie Afspraakstatus:** 
>
> Geen Definitie

| Eigenschap | Waarde |
| :--- | :------ |
| name | Afspraakstatus |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2018-10-31 10:59:24 |
| modified | 2024-04-17 13:34:46 |
| id | EAID_5AA9821A_A88A_480b_9950_70FE017593B3 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Afspraakstatus |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA2/0.9/id-93731fcf-2b7f-42f2-9f94-6f6f80ce0067](https://gemmaonline.nl/index.php/GEMMA2/0.9/id-93731fcf-2b7f-42f2-9f94-6f6f80ce0067) |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Afspraakstatus

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| status | AN40 |  |




### Artikel
> **Definitie Artikel:** 
>
> Tekst die is gemaakt om gepubliceerd te worden als een onafhankelijk deel van een tijdschrift, krant, encyclopedie of ander werk

| Eigenschap | Waarde |
| :--- | :------ |
| name | Artikel |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | crossover |
| version | 1.0 |
| created | 2018-04-16 13:48:36 |
| modified | 2024-04-17 13:34:46 |
| id | EAID_F38E71BC_DDA2_4a9c_A438_C486EC4C4646 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Artikel |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA2/0.9/id-1054f6c9-2c53-4bf9-ad9f-04851ce71a4a](https://gemmaonline.nl/index.php/GEMMA2/0.9/id-1054f6c9-2c53-4bf9-ad9f-04851ce71a4a) |
| gemma_definitie | Tekst die is gemaakt om gepubliceerd te worden als een onafhankelijk deel van een tijdschrift, krant, encyclopedie of ander werk |
| gemma_toelichting |  |


Attributen van objecttype Artikel

| Attribute | Datatype | Description |
| :--- | :--- | :--- |




### Balieafspraak
> **Definitie Balieafspraak:** 
>
> Balieafspraken zijn afspraken voor een klantcontact. Dit ongeacht of deze werkelijk heeft plaatsgevonden of gaat plaatsvinden, soms liggen deze in de toekomst of is iemand niet op komen dagen, of iets anders waardoor het klantcontact nog niet heeft plaatsgevonden.

| Eigenschap | Waarde |
| :--- | :------ |
| name | Balieafspraak |
| toelichting | Dit ongeacht of deze werkelijk heeft plaatsgevonden of gaat plaatsvinden, soms liggen deze in de toekomst of is iemand niet op komen dagen, of iets anders waardoor het klantcontact nog niet heeft plaatsgevonden. |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2018-10-31 10:43:28 |
| modified | 2024-04-17 13:34:46 |
| id | EAID_631FEEF1_88D3_4d18_ADB2_BF999068493E |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Balieafspraak |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA2/0.9/id-8fd2ff34-a208-4924-bec3-b5ee7e5e7a18](https://gemmaonline.nl/index.php/GEMMA2/0.9/id-8fd2ff34-a208-4924-bec3-b5ee7e5e7a18) |
| gemma_definitie | Balieafspraken zijn afspraken voor een klantcontact. Dit ongeacht of deze werkelijk heeft plaatsgevonden of gaat plaatsvinden, soms liggen deze in de toekomst of is iemand niet op komen dagen, of iets anders waardoor het klantcontact nog niet heeft plaatsgevonden. |
| gemma_toelichting | Dit ongeacht of deze werkelijk heeft plaatsgevonden of gaat plaatsvinden, soms liggen deze in de toekomst of is iemand niet op komen dagen, of iets anders waardoor het klantcontact nog niet heeft plaatsgevonden. |


Attributen van objecttype Balieafspraak

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| eindtijdGepland | Datetime |  |
| notitie | text |  |
| starttijdGepland | Datetime |  |
| tijdAangemaakt | Datetime |  |
| tijdsduurGepland | int |  |
| toelichting | text |  |
| wachttijdNaStartAfspraak | int |  |
| wachttijdTotaal | int |  |
| wachttijdVoorStartAfspraak | int |  |
| werkelijkeTijdsduur | int |  |
| None | Class: "Klantcontact" |  |




### ExterneBron
> **Definitie ExterneBron:** 
>
> Bron buiten de eigen organisatie

| Eigenschap | Waarde |
| :--- | :------ |
| name | ExterneBron |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2018-05-15 16:05:32 |
| modified | 2024-04-17 13:34:46 |
| id | EAID_841FC453_80B3_4389_A91F_9498FDC629CF |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype ExterneBron

| Attribute | Datatype | Description |
| :--- | :--- | :--- |




### Formuliersoort
> **Definitie Formuliersoort:** 
>
> Bron: GEM_FORM
> ID: FORM_ID

| Eigenschap | Waarde |
| :--- | :------ |
| name | Formuliersoort |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2018-04-25 16:31:00 |
| modified | 2024-04-17 13:34:46 |
| id | EAID_0567826D_81EE_4bbd_8D62_3073B74CDF11 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Formuliersoort

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| ingebruik | Boolean |  |
| naam | AN80 |  |
| onderwerp | AN80 |  |




### Formuliersoortveld
> **Definitie Formuliersoortveld:** 
>
> Bron: GEM_VELD
> ID: FORM_ID en VELD_NAAM

| Eigenschap | Waarde |
| :--- | :------ |
| name | Formuliersoortveld |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | crossover |
| version | 1.0 |
| created | 2018-04-26 16:48:10 |
| modified | 2024-04-17 13:34:46 |
| id | EAID_E512AEFD_85FB_4b57_82FE_709221307861 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Formuliersoortveld

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| helptekst | Text |  |
| isVerplicht | boolean |  |
| label | AN80 |  |
| maxLengte | int |  |
| veldnaam | AN40 |  |
| veldtype | AN40 |  |




### Klantbeoordeling
> **Definitie Klantbeoordeling:** 
>
> Geen Definitie

| Eigenschap | Waarde |
| :--- | :------ |
| name | Klantbeoordeling |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | aashkpour |
| version | 1.0 |
| created | 2024-02-05 15:32:39 |
| modified | 2024-04-17 13:34:46 |
| id | EAID_881F95F7_7096_49ab_B1CA_4D9FA93BB4A9 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Klantbeoordeling

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| beoordeling | AN10 |  |
| categorie | AN50 |  |
| contactOpnemen | boolean |  |
| ddBeoordeling | Date |  |
| kanaal | AN100 |  |
| onderwerp | AN50 |  |
| subCategorie | AN50 |  |
| None | Class: "Klantbeoordelingreden" |  |




### Klantbeoordelingreden
> **Definitie Klantbeoordelingreden:** 
>
> Geen Definitie

| Eigenschap | Waarde |
| :--- | :------ |
| name | Klantbeoordelingreden |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | aashkpour |
| version | 1.0 |
| created | 2024-02-05 15:32:50 |
| modified | 2024-04-17 13:34:46 |
| id | EAID_40394EFE_AD3E_4fd9_B9FC_AF73442AF625 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Klantbeoordelingreden

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| reden | AN100 |  |




### MORAanvraagOfMelding
> **Definitie MORAanvraagOfMelding:** 
>
> Geen Definitie

| Eigenschap | Waarde |
| :--- | :------ |
| name | MORAanvraagOfMelding |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | aashkpour |
| version | 1.0 |
| created | 2020-03-23 15:15:46 |
| modified | 2024-04-17 13:34:46 |
| id | EAID_A9B89FF7_BCED_49fc_97A4_2A98BCED5B17 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype MORAanvraagOfMelding

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| locatie | Punt |  |
| locatieOmschrijving | AN300 |  |
| meldingOmschrijving | AN40 |  |
| meldingTekst | AN4000 |  |




### Onderwerp
> **Definitie Onderwerp:** 
>
> Bron: GEM_VJV_ONDERWERP
> ID: ONDERWERP_ID

| Eigenschap | Waarde |
| :--- | :------ |
| name | Onderwerp |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2018-07-05 14:24:43 |
| modified | 2024-04-17 13:34:46 |
| id | EAID_8D758F67_6085_4ac7_BFDC_8D97AB632A93 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Onderwerp |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA2/0.9/id-bc793405-f822-4a23-a8dc-74206f1d45df](https://gemmaonline.nl/index.php/GEMMA2/0.9/id-bc793405-f822-4a23-a8dc-74206f1d45df) |
| gemma_definitie | Bron: GEM_VJV_ONDERWERP ID: ONDERWERP_ID |
| gemma_toelichting |  |


Attributen van objecttype Onderwerp

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| isActief | boolean |  |
| naam | AN80 |  |
| toelichting | text |  |




### ProductOfDienst
> **Definitie ProductOfDienst:** 
>
> Bron: QP_CALENDAR.CFM_SERVICES

| Eigenschap | Waarde |
| :--- | :------ |
| name | ProductOfDienst |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2018-07-05 14:22:55 |
| modified | 2024-04-17 13:34:47 |
| id | EAID_4B871112_CB41_4bfb_BD43_117C63D31BB4 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | ProductOfDienst |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA2/0.9/id-724f019e-158f-4404-8b57-3e1eae109fec](https://gemmaonline.nl/index.php/GEMMA2/0.9/id-724f019e-158f-4404-8b57-3e1eae109fec) |
| gemma_definitie | Bron: QP_CALENDAR.CFM_SERVICES |
| gemma_toelichting |  |


Attributen van objecttype ProductOfDienst

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| afhandeltijd | int |  |
| ingebruik | Boolean |  |
| naam | AN80 |  |
| None | Class: "Klantbeoordeling" |  |




### Telefoononderwerp
> **Definitie Telefoononderwerp:** 
>
> Geen Definitie

| Eigenschap | Waarde |
| :--- | :------ |
| name | Telefoononderwerp |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2018-11-22 16:24:16 |
| modified | 2024-04-17 13:34:47 |
| id | EAID_48FE13A9_2204_4631_BAEE_E2D3B10E9A2D |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Telefoononderwerp |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA2/0.9/id-c604ce01-282e-4d1a-ade9-d1a4c1938f4e](https://gemmaonline.nl/index.php/GEMMA2/0.9/id-c604ce01-282e-4d1a-ade9-d1a4c1938f4e) |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Telefoononderwerp

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| onderwerp | AN40 |  |




### Telefoonstatus
> **Definitie Telefoonstatus:** 
>
> 
>  ABANDONEDALERTING: “Opgehangen tijdens overgaan telefoon”
>  DROPPEDCANCELED: “Opgehangen door systeem”
>  ABANDONEDQUEUED: “Opgehangen tijdens wachten, zonder boodschap. ”
>  CONNECTEDDIRECT: “Direct verbonden”
>  CONNECTEDQUEUEDANNOUNCE: “Verbonden na wachtrij met boodschap”
>  AbandonedQUEUEDANNOUNCE: “Opgehangen in wachtrij met boodschap”
>  DroppedBusy: “Opgehangen door systeem, te druk”
>  REJECTED: “Geweigerd door systeem”
>  Droppedoverload: “Opgehangen door systeem vanwege overbelasting”
> 

| Eigenschap | Waarde |
| :--- | :------ |
| name | Telefoonstatus |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2018-11-22 16:22:06 |
| modified | 2024-04-17 13:34:47 |
| id | EAID_D8A82A45_03C3_44d5_AF32_3138A55B2E75 |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam |  |
| gemma_type |  |
| gemma_url |  |
| gemma_definitie |  |
| gemma_toelichting |  |


Attributen van objecttype Telefoonstatus

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| contactConnectionState | AN20 |  |
| status | AN20 |  |




### Telefoontje
> **Definitie Telefoontje:** 
>
> De telefoontjes zijn alle keren dat iemand naar de gemeente belt en het telefoonsysteem neemt deze telefoontjes aan. Ongeacht of iemand daarna ophangt, door het systeem uit de wachtrij wordt gezet, doorverbonden wordt met een derde partij of er werkelijk wordt opgenomen.     

| Eigenschap | Waarde |
| :--- | :------ |
| name | Telefoontje |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2018-11-21 16:33:33 |
| modified | 2024-04-17 13:34:47 |
| id | EAID_EEB60E10_C244_4176_AB68_F0E30759269F |
| domein_iv3 |  |
| domein_dcat |  |
| gemma_naam | Telefoontje |
| gemma_type | business-object |
| gemma_url | [https://gemmaonline.nl/index.php/GEMMA2/0.9/id-32052c54-e099-47e7-8ded-599537226dfa](https://gemmaonline.nl/index.php/GEMMA2/0.9/id-32052c54-e099-47e7-8ded-599537226dfa) |
| gemma_definitie | De telefoontjes zijn alle keren dat iemand naar de gemeente belt en het telefoonsysteem neemt deze telefoontjes aan. Ongeacht of iemand daarna ophangt, door het systeem uit de wachtrij wordt gezet, doorverbonden wordt met een derde partij of er werkelijk wordt opgenomen. |
| gemma_toelichting |  |


Attributen van objecttype Telefoontje

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| afhandeltijdNaGesprek | int |  |
| deltaISDNConnectie | int |  |
| eindtijd | DateTime |  |
| starttijd | DateTime |  |
| totaleOnHoldTijd | int |  |
| totaleSpreektijd | int |  |
| totaleWachttijd | int |  |
| totLateTijdsduur | int |  |
| trackID | AN20 |  |
| None | Class: "Klantcontact" |  |






