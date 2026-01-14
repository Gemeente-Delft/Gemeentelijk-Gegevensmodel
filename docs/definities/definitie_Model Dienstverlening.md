# Model Dienstverlening
## Inleiding
> **Definitie Model Dienstverlening:** 
>
> Het informatiedomein dat gegevens omvat over meldingen, aanvragen, baliecontacten, telefonische afhandeling en digitale interacties die faciliterend zijn voor andere domeinen.

??? info "Kenmerken Model Model Dienstverlening"

    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | Model Dienstverlening |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.5 |
    | created | 2018-04-16 13:48:36 |
    | modified | 2025-03-27 15:28:35 |
    | id | EAPK\_7F780248\_C88C\_450f\_8318\_98C5020AB372 |
    

Het model 'Model Dienstverlening' kent de volgende objecttypen:

* **Aanvraagdata**: 
> Bron: GEN\_REQ\_DATA
> ID: REQ\_DATA icm VELD\_NAAM
* **AanvraagOfMelding**: 
> Komt overeen met een VJV
> Bron: GEM\_VJV (Distinct op REQ\_ID)
> ID: REQ\_ID
* **Afspraakstatus**: de toestand van de afspraak
* **Artikel**: Tekst die is gemaakt om gepubliceerd te worden als een onafhankelijk deel van een tijdschrift, krant, encyclopedie of ander werk
* **Balieafspraak**: Balieafspraken zijn afspraken voor een klantcontact. Dit ongeacht of deze werkelijk heeft plaatsgevonden of gaat plaatsvinden, soms liggen deze in de toekomst of is iemand niet op komen dagen, of iets anders waardoor het klantcontact nog niet heeft plaatsgevonden.
* **ExterneBron**: Bron buiten de eigen organisatie
* **Formuliersoort**: 
> Bron: GEM\_FORM
> ID: FORM\_ID
* **Formuliersoortveld**: 
> Bron: GEM\_VELD
> ID: FORM\_ID en VELD\_NAAM
* **Klantbeoordeling**: goed- of afkeurende uitspraak; = mening, opvatting
* **Klantbeoordelingreden**: Reden voor de beoordeling
* **MOR-AanvraagOfMelding**: Bericht van een inwoner over een gebrek of opvallendheid in de openbare ruimte
* **Onderwerp**: 
> Bron: GEM\_VJV\_ONDERWERP
> ID: ONDERWERP\_ID
* **ProductOfDienst**: Bron: QP_CALENDAR.CFM_SERVICES
* **Telefoononderwerp**: Onderwerp waarover het telefooncontact gaat
* **Telefoonstatus**: 
> ABANDONEDALERTING: “Opgehangen tijdens overgaan telefoon”
> DROPPEDCANCELED: “Opgehangen door systeem”
> ABANDONEDQUEUED: “Opgehangen tijdens wachten, zonder boodschap. ”
> CONNECTEDDIRECT: “Direct verbonden”
> CONNECTEDQUEUEDANNOUNCE: “Verbonden na wachtrij met boodschap”
> AbandonedQUEUEDANNOUNCE: “Opgehangen in wachtrij met boodschap”
> DroppedBusy: “Opgehangen door systeem, te druk”
> REJECTED: “Geweigerd door systeem”
> Droppedoverload: “Opgehangen door systeem vanwege overbelasting”
* **Telefoontje**: De telefoontgesprekken zijn alle keren dat iemand naar de gemeente belt en het telefoonsysteem neemt deze telefoongesprekken aan. Ongeacht of iemand daarna ophangt, door het systeem uit de wachtrij wordt gezet, doorverbonden wordt met een derde partij of er werkelijk wordt opgenomen.


## Objecttypen Model Dienstverlening


### Aanvraagdata
> **Definitie Aanvraagdata:** 
>
> 
> Bron: GEN\_REQ\_DATA
> ID: REQ\_DATA icm VELD\_NAAM

??? info "Kenmerken Model Aanvraagdata"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Aanvraagdata |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2018-04-25 16:41:17 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_1F68C981\_7E16\_4368\_8867\_CA00AEB08A04 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Aanvraagdata |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-6f15e2ca-531d-4879-b087-f43559d8c3fd](https://gemmaonline.nl/index.php/GEMMA/id-6f15e2ca-531d-4879-b087-f43559d8c3fd) |
<<<<<<< HEAD
    | gemma_definitie | 
> Bron: GEN\_REQ\_DATA
> ID: REQ\_DATA icm VELD\_NAAM |
=======
    | gemma_definitie | Bron: GEN\_REQ\_DATA<br>ID: REQ\_DATA icm VELD\_NAAM |
>>>>>>> origin/master
    | gemma_toelichting |  |
    

Attributen van objecttype Aanvraagdata

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| veld | AN40 |  |
| data | Tekst |  |



### AanvraagOfMelding
> **Definitie AanvraagOfMelding:** 
>
> 
> Komt overeen met een VJV
> Bron: GEM\_VJV (Distinct op REQ\_ID)
> ID: REQ\_ID

??? info "Kenmerken Model AanvraagOfMelding"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | AanvraagOfMelding |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2018-04-16 14:11:57 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_8E6BAEF8\_1878\_400f\_9244\_23575BD41EAB |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | AanvraagOfMelding |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-f14fa1cf-f2c7-4bd6-862d-28ff1616a882](https://gemmaonline.nl/index.php/GEMMA/id-f14fa1cf-f2c7-4bd6-862d-28ff1616a882) |
<<<<<<< HEAD
    | gemma_definitie | 
> Komt overeen met een VJV
> Bron: GEM\_VJV (Distinct op REQ\_ID)
> ID: REQ\_ID |
=======
    | gemma_definitie | Komt overeen met een VJV<br>Bron: GEM\_VJV (Distinct op REQ\_ID)<br>ID: REQ\_ID |
>>>>>>> origin/master
    | gemma_toelichting |  |
    

Attributen van objecttype AanvraagOfMelding

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| afgehandeld | Boolean |  |
| kanaal | AN80 |  |
| soort | AN80 | Sluit aan op soorten uit Suite4Omgevingsdiensten: aanvraag, melding.... |
| datumAfhandeling | Date |  |
| categorie | AN200 |  |
| identificatie | AN40 |  |
| onderwerp | AN200 |  |
| status | AN80 |  |
| subcategorie | AN200 |  |
| datumAanmaak | Date |  |
| categoriecode | AN80 |  |
| datumBeginStatus | Date |  |
| datumEindeStatus | Date |  |
| hoofdcategorie | AN80 |  |
| hoofdcategoriecode | AN80 |  |
| onderwerpcode | AN80 |  |
| statuscode | AN80 |  |
| statusVolgorde | AN80 |  |
| subcategoriecode | AN80 |  |



### Afspraakstatus
> **Definitie Afspraakstatus:** 
>
> de toestand van de afspraak

??? info "Kenmerken Model Afspraakstatus"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Afspraakstatus |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.14.0 |
    | created | 2018-10-31 10:59:24 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_5AA9821A\_A88A\_480b\_9950\_70FE017593B3 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Afspraakstatus |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-93731fcf-2b7f-42f2-9f94-6f6f80ce0067](https://gemmaonline.nl/index.php/GEMMA/id-93731fcf-2b7f-42f2-9f94-6f6f80ce0067) |
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

??? info "Kenmerken Model Artikel"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Artikel |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2018-04-16 13:48:36 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_F38E71BC\_DDA2\_4a9c\_A438\_C486EC4C4646 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Artikel |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-1054f6c9-2c53-4bf9-ad9f-04851ce71a4a](https://gemmaonline.nl/index.php/GEMMA/id-1054f6c9-2c53-4bf9-ad9f-04851ce71a4a) |
    | gemma_definitie | Tekst die is gemaakt om gepubliceerd te worden als een onafhankelijk deel van een tijdschrift, krant, encyclopedie of ander werk |
    | gemma_toelichting |  |
    

Attributen van objecttype Artikel

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Balieafspraak
> **Definitie Balieafspraak:** 
>
> Balieafspraken zijn afspraken voor een klantcontact. Dit ongeacht of deze werkelijk heeft plaatsgevonden of gaat plaatsvinden, soms liggen deze in de toekomst of is iemand niet op komen dagen, of iets anders waardoor het klantcontact nog niet heeft plaatsgevonden.

??? info "Kenmerken Model Balieafspraak"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Balieafspraak |
    | toelichting | Dit ongeacht of deze werkelijk heeft plaatsgevonden of gaat plaatsvinden, soms liggen deze in de toekomst of is iemand niet op komen dagen, of iets anders waardoor het klantcontact nog niet heeft plaatsgevonden. |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2018-10-31 10:43:28 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_631FEEF1\_88D3\_4d18\_ADB2\_BF999068493E |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Balieafspraak |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-8fd2ff34-a208-4924-bec3-b5ee7e5e7a18](https://gemmaonline.nl/index.php/GEMMA/id-8fd2ff34-a208-4924-bec3-b5ee7e5e7a18) |
    | gemma_definitie | Balieafspraken zijn afspraken voor een klantcontact. Dit ongeacht of deze werkelijk heeft plaatsgevonden of gaat plaatsvinden, soms liggen deze in de toekomst of is iemand niet op komen dagen, of iets anders waardoor het klantcontact nog niet heeft plaats |
    | gemma_toelichting | Dit ongeacht of deze werkelijk heeft plaatsgevonden of gaat plaatsvinden, soms liggen deze in de toekomst of is iemand niet op komen dagen, of iets anders waardoor het klantcontact nog niet heeft plaatsgevonden. |
    

Attributen van objecttype Balieafspraak

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| starttijdGepland | Datetime |  |
| tijdAangemaakt | Datetime |  |
| toelichting | text |  |
| tijdsduurGepland | int | Werkelijke tijdsduur in minuten |
| wachttijdTotaal | int | Wachttijd inclusief de tijd dat iemand te vroeg voor de afspraak verschijnt en de tijd dat iemand moet wachten na de geplande starttijd van de afspraak |
| eindtijdGepland | Datetime |  |
| wachttijdVoorStartAfspraak | int | Tijdsduur dat iemand te vroeg is voor de afspraak |
| wachttijdNaStartAfspraak | int | Tijdsduur die iemand moet wachten na de starttijd van de afspraak |
| werkelijkeTijdsduur | int |  |
| notitie | text |  |



### ExterneBron
> **Definitie ExterneBron:** 
>
> Bron buiten de eigen organisatie

??? info "Kenmerken Model ExterneBron"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | ExterneBron |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2018-05-15 16:05:32 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_841FC453\_80B3\_4389\_A91F\_9498FDC629CF |
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
> 
> Bron: GEM\_FORM
> ID: FORM\_ID

??? info "Kenmerken Model Formuliersoort"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Formuliersoort |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2018-04-25 16:31:00 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_0567826D\_81EE\_4bbd\_8D62\_3073B74CDF11 |
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
| naam | AN80 |  |
| onderwerp | AN80 |  |
| ingebruik | Boolean |  |



### Formuliersoortveld
> **Definitie Formuliersoortveld:** 
>
> 
> Bron: GEM\_VELD
> ID: FORM\_ID en VELD\_NAAM

??? info "Kenmerken Model Formuliersoortveld"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Formuliersoortveld |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2018-04-26 16:48:10 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_E512AEFD\_85FB\_4b57\_82FE\_709221307861 |
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
| veldnaam | AN40 |  |
| veldtype | AN40 |  |
| helptekst | Text |  |
| maxLengte | int |  |
| isVerplicht | boolean |  |
| label | AN80 |  |



### Klantbeoordeling
> **Definitie Klantbeoordeling:** 
>
> goed- of afkeurende uitspraak; = mening, opvatting

??? info "Kenmerken Model Klantbeoordeling"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Klantbeoordeling |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Ashkan Ashkpour |
    | version | 1.12.0 |
    | created | 2024-02-05 15:32:39 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_881F95F7\_7096\_49ab\_B1CA\_4D9FA93BB4A9 |
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
| ddBeoordeling | Date | datum en tijdstip van de klantbeoordeling |
| beoordeling | AN10 | cijfer voor de beoordeling (getal tussen 0 en 10) |
| contactOpnemen | boolean | of de klant het al dan niet goed vind dat naar aanleiding van zijn/haar beoordeling contact wordt opgenomen |
| categorie | AN50 |  |
| subCategorie | AN50 |  |
| onderwerp | AN50 |  |
| kanaal | AN100 | waar de beoordeling is uitgevoerd, te weten op de website, naar aanleiding van een webformulier of na schriftelijke uitvraag vanuit onze organisatie |



### Klantbeoordelingreden
> **Definitie Klantbeoordelingreden:** 
>
> Reden voor de beoordeling

??? info "Kenmerken Model Klantbeoordelingreden"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Klantbeoordelingreden |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Ashkan Ashkpour |
    | version | 1.12.0 |
    | created | 2024-02-05 15:32:50 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_40394EFE\_AD3E\_4fd9\_B9FC\_AF73442AF625 |
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



### MOR-AanvraagOfMelding
> **Definitie MOR-AanvraagOfMelding:** 
>
> Bericht van een inwoner over een gebrek of opvallendheid in de openbare ruimte

??? info "Kenmerken Model MOR-AanvraagOfMelding"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | MOR-AanvraagOfMelding |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Ashkan Ashkpour |
    | version | 1.13.0 |
    | created | 2020-03-23 15:15:46 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_A9B89FF7\_BCED\_49fc\_97A4\_2A98BCED5B17 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype MOR-AanvraagOfMelding

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| locatie | Punt |  |
| locatieOmschrijving | AN300 |  |
| meldingOmschrijving | AN40 |  |
| meldingTekst | AN4000 |  |



### Onderwerp
> **Definitie Onderwerp:** 
>
> 
> Bron: GEM\_VJV\_ONDERWERP
> ID: ONDERWERP\_ID

??? info "Kenmerken Model Onderwerp"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Onderwerp |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2018-07-05 14:24:43 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_8D758F67\_6085\_4ac7\_BFDC\_8D97AB632A93 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Onderwerp |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-bc793405-f822-4a23-a8dc-74206f1d45df](https://gemmaonline.nl/index.php/GEMMA/id-bc793405-f822-4a23-a8dc-74206f1d45df) |
<<<<<<< HEAD
    | gemma_definitie | 
> Bron: GEM\_VJV\_ONDERWERP
> ID: ONDERWERP\_ID |
=======
    | gemma_definitie | Bron: GEM\_VJV\_ONDERWERP<br>ID: ONDERWERP\_ID |
>>>>>>> origin/master
    | gemma_toelichting |  |
    

Attributen van objecttype Onderwerp

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| naam | AN80 |  |
| toelichting | text |  |
| isActief | boolean |  |



### ProductOfDienst
> **Definitie ProductOfDienst:** 
>
> Bron: QP_CALENDAR.CFM_SERVICES

??? info "Kenmerken Model ProductOfDienst"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | ProductOfDienst |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2018-07-05 14:22:55 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_4B871112\_CB41\_4bfb\_BD43\_117C63D31BB4 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | ProductOfDienst |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-724f019e-158f-4404-8b57-3e1eae109fec](https://gemmaonline.nl/index.php/GEMMA/id-724f019e-158f-4404-8b57-3e1eae109fec) |
    | gemma_definitie | Bron: QP\_CALENDAR.CFM\_SERVICES |
    | gemma_toelichting |  |
    

Attributen van objecttype ProductOfDienst

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| naam | AN80 |  |
| afhandeltijd | int | Standaard afhandeltijd in minuten |
| ingebruik | Boolean |  |



### Telefoononderwerp
> **Definitie Telefoononderwerp:** 
>
> Onderwerp waarover het telefooncontact gaat

??? info "Kenmerken Model Telefoononderwerp"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Telefoononderwerp |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.14.0 |
    | created | 2018-11-22 16:24:16 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_48FE13A9\_2204\_4631\_BAEE\_E2D3B10E9A2D |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Telefoononderwerp |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-c604ce01-282e-4d1a-ade9-d1a4c1938f4e](https://gemmaonline.nl/index.php/GEMMA/id-c604ce01-282e-4d1a-ade9-d1a4c1938f4e) |
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
> ABANDONEDALERTING: “Opgehangen tijdens overgaan telefoon”
> DROPPEDCANCELED: “Opgehangen door systeem”
> ABANDONEDQUEUED: “Opgehangen tijdens wachten, zonder boodschap. ”
> CONNECTEDDIRECT: “Direct verbonden”
> CONNECTEDQUEUEDANNOUNCE: “Verbonden na wachtrij met boodschap”
> AbandonedQUEUEDANNOUNCE: “Opgehangen in wachtrij met boodschap”
> DroppedBusy: “Opgehangen door systeem, te druk”
> REJECTED: “Geweigerd door systeem”
> Droppedoverload: “Opgehangen door systeem vanwege overbelasting”

??? info "Kenmerken Model Telefoonstatus"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Telefoonstatus |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2018-11-22 16:22:06 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_D8A82A45\_03C3\_44d5\_AF32\_3138A55B2E75 |
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
> De telefoontgesprekken zijn alle keren dat iemand naar de gemeente belt en het telefoonsysteem neemt deze telefoongesprekken aan. Ongeacht of iemand daarna ophangt, door het systeem uit de wachtrij wordt gezet, doorverbonden wordt met een derde partij of er werkelijk wordt opgenomen.

??? info "Kenmerken Model Telefoontje"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Telefoontje |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2018-11-21 16:33:33 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_EEB60E10\_C244\_4176\_AB68\_F0E30759269F |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Telefoontje |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-32052c54-e099-47e7-8ded-599537226dfa](https://gemmaonline.nl/index.php/GEMMA/id-32052c54-e099-47e7-8ded-599537226dfa) |
    | gemma_definitie | De telefoontjes zijn alle keren dat iemand naar de gemeente belt en het telefoonsysteem neemt deze telefoontjes aan. Ongeacht of iemand daarna ophangt, door het systeem uit de wachtrij wordt gezet, doorverbonden wordt met een derde partij of er werkelijk |
    | gemma_toelichting |  |
    

Attributen van objecttype Telefoontje

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| starttijd | DateTime | Het moment dat de telefooncentrale een telefoontje in behandeling neemt. Dit ligt voor de starttijd van het klantcontact |
| eindtijd | DateTime | Het moment dat de telefooncentrale het telefoontjes beeindigd |
| totaleTijdsduur | int | Tijd tussen start- en eindtijd van telefoontje |
| trackID | AN20 |  |
| totaleWachttijd | int | De tijd tussen de starttijd van het telefoontje en het moment dat het telefoontje voor het eerst wordt opgenomen, of het telefoontje wordt afgesloten |
| totaleSpreektijd | int | De totale tijd dat met een (of meer) medewerkers van de gemeente wordt gebeld. |
| totaleOnHoldTijd | int | De totale tijd dat een beller tussen klantcontacten "on hold" wordt gezet. |
| afhandeltijdNaGesprek | int | De tijd die de medewerker nodig heeft om het telefoontje af te handelen totdat hij/zij klaar is voor een volgend telefoontje |
| deltaISDNConnectie | int | De totale tijd dat er een teelfoonverbinding was minus totale wachttijd, spreektijd en on hold-tijd. |






## Enumeraties Model Dienstverlening


### Boolean
Geen Definitie

Het enumeratie Boolean kent de volgende waarden:

* **Ja**: 
* **Nee**: 
* **Onbekend**: 
* **Leeg**: 


De enumeratie Boolean heeft de volgende kenmerken:

??? info "Kenmerken Model Boolean"

    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | Boolean |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author |  |
    | version | 1.10.0 |
    | created | 2025-03-26 11:13:35 |
<<<<<<< HEAD
    | modified | 2025-03-26 16:14:54 |
    | id | EAID_4ae844b8_74d2_42ec_abed_70eb1ee41435 |
=======
    | modified | 2025-12-16 10:28:45 |
    | id | EAID\_be7848ec\_8a72\_4f19\_8888\_39493104f57f |
>>>>>>> origin/master
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    


