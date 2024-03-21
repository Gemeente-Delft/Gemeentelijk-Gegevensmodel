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
* **Externe Bron**: Bron buiten de eigen organisatie
* **Formuliersoort**: Bron: GEM_FORM ID: FORM_ID
* **Formuliersoortveld**: Bron: GEM_VELD ID: FORM_ID en VELD_NAAM
* **MORAanvraagOfMelding**: <Geen Definities>
* **Onderwerp**: Bron: GEM_VJV_ONDERWERP ID: ONDERWERP_ID
* **ProductOfDienst**: Bron: QP_CALENDAR.CFM_SERVICES
* **Telefoononderwerp**: <Geen Definities>
* **Telefoonstatus**: <ul>  <li>ABANDONEDALERTING: “Opgehangen tijdens overgaan telefoon”</li>  <li>DROPPEDCANCELED: “Opgehangen door systeem”</li>  <li>ABANDONEDQUEUED: “Opgehangen tijdens wachten, zonder boodschap. ”</li>  <li>CONNECTEDDIRECT: “Direct verbonden”</li>  <li>CONNECTEDQUEUEDANNOUNCE: “Verbonden na wachtrij met boodschap”</li>  <li>AbandonedQUEUEDANNOUNCE: “Opgehangen in wachtrij met boodschap”</li>  <li>DroppedBusy: “Opgehangen door systeem, te druk”</li>  <li>REJECTED: “Geweigerd door systeem”</li>  <li>Droppedoverload: “Opgehangen door systeem vanwege overbelasting”</li> </ul>
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
| modified | 2023-10-12 16:27:26 |
| id | EAID_1F68C981_7E16_4368_8867_CA00AEB08A04 |
| domein-iv3 |  |
| domein-dcat |  |
| GEMMA-naam |  |
| GEMMA-type |  |
| GEMMA-url |  |


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
| bron | GEM_VJV |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2018-04-16 14:11:57 |
| modified | 2023-10-12 16:27:26 |
| id | EAID_8E6BAEF8_1878_400f_9244_23575BD41EAB |
| domein-iv3 |  |
| domein-dcat |  |
| GEMMA-naam |  |
| GEMMA-type |  |
| GEMMA-url |  |


Attributen van objecttype AanvraagOfMelding

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| aanmaakdatum | Date |  |
| afgehandeld | Boolean |  |
| afhandeldatum | Date |  |
| categorie | AN200 |  |
| categoriecode | AN80 |  |
| DatumBeginStatus | Date |  |
| DatumEindStatus | Date |  |
| hoofdcategorie | AN80 |  |
| hoofdcategoriecode | AN80 |  |
| identificatie | AN40 |  |
| kanaal | AN80 |  |
| onderwerp | AN200 |  |
| onderwerpcode | AN80 |  |
| soort | AN80 |  |
| status | AN80 |  |
| status volgorde | AN80 |  |
| statuscode | AN80 |  |
| sub categorie | AN200 |  |
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
| modified | 2023-10-12 16:27:26 |
| id | EAID_5AA9821A_A88A_480b_9950_70FE017593B3 |
| domein-iv3 |  |
| domein-dcat |  |
| GEMMA-naam |  |
| GEMMA-type |  |
| GEMMA-url |  |


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
| modified | 2023-10-12 16:27:26 |
| id | EAID_F38E71BC_DDA2_4a9c_A438_C486EC4C4646 |
| domein-iv3 |  |
| domein-dcat |  |
| GEMMA-naam |  |
| GEMMA-type |  |
| GEMMA-url |  |


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
| bron | QP_CALENDAR.APPOINTMENT |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2018-10-31 10:43:28 |
| modified | 2023-10-12 16:27:26 |
| id | EAID_631FEEF1_88D3_4d18_ADB2_BF999068493E |
| domein-iv3 |  |
| domein-dcat |  |
| GEMMA-naam |  |
| GEMMA-type |  |
| GEMMA-url |  |


Attributen van objecttype Balieafspraak

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| eindtijd_gepland | Datetime |  |
| notitie | text |  |
| starttijd_gepland | Datetime |  |
| tijdaangemaakt | Datetime |  |
| tijdsduur_gepland | int |  |
| toelichting | text |  |
| wachttijd_na_start_afspraak | int |  |
| wachttijd_totaal | int |  |
| wachttijd_voor_start_afspraak | int |  |
| werkelijke_tijdsduur | int |  |
| None | Class: "Klantcontact" |  |




### Externe Bron
> **Definitie Externe Bron:** 
>
> Bron buiten de eigen organisatie

| Eigenschap | Waarde |
| :--- | :------ |
| name | Externe Bron |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2018-05-15 16:05:32 |
| modified | 2023-10-12 16:27:26 |
| id | EAID_841FC453_80B3_4389_A91F_9498FDC629CF |
| domein-iv3 |  |
| domein-dcat |  |
| GEMMA-naam |  |
| GEMMA-type |  |
| GEMMA-url |  |


Attributen van objecttype Externe Bron

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
| bron | GEM_FORM |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2018-04-25 16:31:00 |
| modified | 2023-10-12 16:27:26 |
| id | EAID_0567826D_81EE_4bbd_8D62_3073B74CDF11 |
| domein-iv3 |  |
| domein-dcat |  |
| GEMMA-naam |  |
| GEMMA-type |  |
| GEMMA-url |  |


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
| modified | 2023-10-12 16:27:26 |
| id | EAID_E512AEFD_85FB_4b57_82FE_709221307861 |
| domein-iv3 |  |
| domein-dcat |  |
| GEMMA-naam |  |
| GEMMA-type |  |
| GEMMA-url |  |


Attributen van objecttype Formuliersoortveld

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| helptekst | Text |  |
| isverplicht | boolean |  |
| label | AN80 |  |
| maxlengte | int |  |
| veldnaam | AN40 |  |
| veldtype | AN40 |  |




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
| modified | 2023-10-12 16:27:26 |
| id | EAID_A9B89FF7_BCED_49fc_97A4_2A98BCED5B17 |
| domein-iv3 |  |
| domein-dcat |  |
| GEMMA-naam |  |
| GEMMA-type |  |
| GEMMA-url |  |


Attributen van objecttype MORAanvraagOfMelding

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| locatie | Punt |  |
| locatie omschrijving | AN300 |  |
| melding omschrijving | AN40 |  |
| melding tekst | AN4000 |  |




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
| bron | GEM_VJV_ONDERWERP |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2018-07-05 14:24:43 |
| modified | 2023-10-12 16:27:26 |
| id | EAID_8D758F67_6085_4ac7_BFDC_8D97AB632A93 |
| domein-iv3 |  |
| domein-dcat |  |
| GEMMA-naam |  |
| GEMMA-type |  |
| GEMMA-url |  |


Attributen van objecttype Onderwerp

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| isactief | boolean |  |
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
| bron | QP_CALENDAR.CFM_SERVICES |
| author | Arjen Brienen |
| version | 1.0 |
| created | 2018-07-05 14:22:55 |
| modified | 2023-10-12 16:27:26 |
| id | EAID_4B871112_CB41_4bfb_BD43_117C63D31BB4 |
| domein-iv3 |  |
| domein-dcat |  |
| GEMMA-naam |  |
| GEMMA-type |  |
| GEMMA-url |  |


Attributen van objecttype ProductOfDienst

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| afhandeltijd | int |  |
| ingebruik | Boolean |  |
| naam | AN80 |  |




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
| modified | 2023-10-12 16:27:26 |
| id | EAID_48FE13A9_2204_4631_BAEE_E2D3B10E9A2D |
| domein-iv3 |  |
| domein-dcat |  |
| GEMMA-naam |  |
| GEMMA-type |  |
| GEMMA-url |  |


Attributen van objecttype Telefoononderwerp

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| onderwerp | AN40 |  |




### Telefoonstatus
> **Definitie Telefoonstatus:** 
>
> <ul>
>  <li>ABANDONEDALERTING: “Opgehangen tijdens overgaan telefoon”</li>
>  <li>DROPPEDCANCELED: “Opgehangen door systeem”</li>
>  <li>ABANDONEDQUEUED: “Opgehangen tijdens wachten, zonder boodschap. ”</li>
>  <li>CONNECTEDDIRECT: “Direct verbonden”</li>
>  <li>CONNECTEDQUEUEDANNOUNCE: “Verbonden na wachtrij met boodschap”</li>
>  <li>AbandonedQUEUEDANNOUNCE: “Opgehangen in wachtrij met boodschap”</li>
>  <li>DroppedBusy: “Opgehangen door systeem, te druk”</li>
>  <li>REJECTED: “Geweigerd door systeem”</li>
>  <li>Droppedoverload: “Opgehangen door systeem vanwege overbelasting”</li>
> </ul>

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
| modified | 2023-10-12 16:27:26 |
| id | EAID_D8A82A45_03C3_44d5_AF32_3138A55B2E75 |
| domein-iv3 |  |
| domein-dcat |  |
| GEMMA-naam |  |
| GEMMA-type |  |
| GEMMA-url |  |


Attributen van objecttype Telefoonstatus

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| contactconnectionstate | AN20 |  |
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
| modified | 2023-10-12 16:27:26 |
| id | EAID_EEB60E10_C244_4176_AB68_F0E30759269F |
| domein-iv3 |  |
| domein-dcat |  |
| GEMMA-naam |  |
| GEMMA-type |  |
| GEMMA-url |  |


Attributen van objecttype Telefoontje

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| afhandeltijd_na_gesprek | int |  |
| delta_isdn_connectie | int |  |
| eindtijd | DateTime |  |
| starttijd | DateTime |  |
| totale_onholdtijd | int |  |
| totale_spreektijd | int |  |
| totale_wachttijd | int |  |
| totlate_tijdsduur | int |  |
| trackid | AN20 |  |
| None | Class: "Klantcontact" |  |






