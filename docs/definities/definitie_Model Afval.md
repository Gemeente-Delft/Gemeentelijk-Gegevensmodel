# Model Afval
## Inleiding
> **Definitie Model Afval:** 
>
> Geen definitie

??? info "Kenmerken Model Model Afval"

    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | Model Afval |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.2.0 |
    | created | 2019-05-20 14:08:51 |
    | modified | 2025-12-20 22:33:35 |
    | id | EAPK\_02C80516\_57F8\_4cbe\_A629\_EC3CBBB8DD52 |
    

Het model 'Model Afval' kent de volgende objecttypen:

* **Categorie**: Categorie waarop leveranciers zich voor de levering van personeel voor kunnen kwalificeren
* **Container**: Container voor het gescheiden inzamelen van huishoudelijke afvalstoffen dwz afvalstoffen afkomstig uit particuliere huishoudens behoudens voor zover het ingezamelde bestanddelen van die afvalstoffen betreft die zijn aangewezen als gevaarlijke afvalstoffen
* **Containertype**: Typologie van container
* **Fractie**: Onderdeel, deeltje
* **Locatie**: Locaties die worden aangedaan tijdens het rijden van een route. Dit kunnen adressen zijn en/of GML-punten met een x- en y-coordinaat. Avalex hanteert op het moment van schrijven alleen adressen, ook voor de containers.
* **Melding**: De betekenisvolle formulering van een waargenomen feit, waaraan een waarde kan worden toegekend
* **Milieustraat**: Een locatie die specifiek bestemd is voor het brengen van gescheiden huishoudelijk afval en grofvuil.
* **Ophaalmoment**: Een stop die een vuilniswagen maakt tijdens het doen van een rit. Bijgehouden wordt de gewichtstoename van de lading
* **Pas**: klein kaartje met je naam en soms je foto erop, dat je toegang geeft tot bepaalde diensten
* **Prijsafspraak**: Overeenkomst tussen concurrenten met betrekking tot de prijs van goederen of diensten.
* **Prijsregel**: Een *prijsregel* is een **regel die aangeeft hoe de prijs van een product, dienst of prestatie wordt vastgesteld of toegepast**, bijvoorbeeld binnen een declaratie- of tariefstructuur.
* **Rit**: Verplaatsing van een wegvoertuig over een wegpad
* **Route**: 
> Routes die gereden worden om bepaalde fracties vuilnis op te halen. Routes gaan langs locaties, waar afhankelijk van de routesoort een containers, bepaalde plekken of adressen worden aangedaan.
> huis-aan-huis: er worden locaties met adressen aangedaan
> illegale dumping, grofvuil: er worden locaties aangedaan (evt met adres)
> containters: er worden locaties met containers aangedaan
* **Storting**: Activiteit, inhoudende a. het zich ontdoen van stoffen
* **Vuilniswagen**: Een vrachtwagen die gebruikt wordt om afval in te zamelen bij bedrijven en huishoudens (huisvuil)
* **Vulgraadmeting**: Mate waarin een (afval)container gevuld is


## Objecttypen Model Afval


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
    | created | 2019-05-20 16:51:23 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_9EC6B40B\_0C87\_4453\_B567\_E0D3572F86AF |
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
| code | int |  |
| naam | AN80 |  |
| omschrijving | Text |  |



### Container
> **Definitie Container:** 
>
> Container voor het gescheiden inzamelen van huishoudelijke afvalstoffen dwz afvalstoffen afkomstig uit particuliere huishoudens behoudens voor zover het ingezamelde bestanddelen van die afvalstoffen betreft die zijn aangewezen als gevaarlijke afvalstoffen

??? info "Kenmerken Model Container"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Container |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-05-20 14:10:13 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_7D3D98F0\_664C\_4605\_9D95\_F68C88ECBA9A |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Container |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-a9b50546-d72d-4e60-8da5-184a27a626c5](https://gemmaonline.nl/index.php/GEMMA/id-a9b50546-d72d-4e60-8da5-184a27a626c5) |
    | gemma_definitie | Container voor het gescheiden inzamelen van huishoudelijke afvalstoffen dwz afvalstoffen afkomstig uit particuliere huishoudens behoudens voor zover het ingezamelde bestanddelen van die afvalstoffen betreft die zijn aangewezen als gevaarlijke afvalstoffen |
    | gemma_toelichting |  |
    

Attributen van objecttype Container

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| sensorID | AN40 |  |
| containercode | AN40 |  |



### Containertype
> **Definitie Containertype:** 
>
> Typologie van container

??? info "Kenmerken Model Containertype"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Containertype |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-05-20 14:12:39 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_0A7769C7\_FE3E\_45eb\_A644\_22E5CB207B42 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Containertype

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| naam | AN80 |  |
| omschrijving | Text |  |



### Fractie
> **Definitie Fractie:** 
>
> Onderdeel, deeltje

??? info "Kenmerken Model Fractie"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Fractie |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-05-20 14:09:37 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_80A7D18F\_7C7E\_4ee6\_9F07\_055559BCEF9F |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Fractie |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-5b29c1f2-feeb-4e72-9b70-7a0a8bb374cc](https://gemmaonline.nl/index.php/GEMMA/id-5b29c1f2-feeb-4e72-9b70-7a0a8bb374cc) |
    | gemma_definitie | Onderdeel, deeltje |
    | gemma_toelichting |  |
    

Attributen van objecttype Fractie

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| naam | AN80 |  |
| omschrijving | Text |  |



### Locatie
> **Definitie Locatie:** 
>
> Locaties die worden aangedaan tijdens het rijden van een route. Dit kunnen adressen zijn en/of GML-punten met een x- en y-coordinaat. Avalex hanteert op het moment van schrijven alleen adressen, ook voor de containers.

??? info "Kenmerken Model Locatie"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Locatie |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-05-20 16:53:54 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_7F4E17A3\_0EC2\_4bee\_B4E0\_BFA26D653EB9 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Locatie |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-71b8f8f4-9789-4cab-9828-d508607188bf](https://gemmaonline.nl/index.php/GEMMA/id-71b8f8f4-9789-4cab-9828-d508607188bf) |
    | gemma_definitie | Locaties die worden aangedaan tijdens het rijden van een route. Dit kunnen adressen zijn en/of GML-punten met een x- en y-coordinaat. Avalex hanteert op het moment van schrijven alleen adressen, ook voor de containers. |
    | gemma_toelichting |  |
    

Attributen van objecttype Locatie

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| locatiePunt | Point |  |
| locatiecode | AN40 |  |
| adresaanduiding | Adresaanduiding |  |



### Melding
> **Definitie Melding:** 
>
> De betekenisvolle formulering van een waargenomen feit, waaraan een waarde kan worden toegekend

??? info "Kenmerken Model Melding"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Melding |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-05-20 16:45:08 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_8A02DCF5\_E568\_4d45\_96A2\_FD4FB53F414C |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Melding |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-e1029618-919b-4889-9989-e7f6ca9a16ea](https://gemmaonline.nl/index.php/GEMMA/id-e1029618-919b-4889-9989-e7f6ca9a16ea) |
    | gemma_definitie | De betekenisvolle formulering van een waargenomen feit, waaraan een waarde kan worden toegekend |
    | gemma_toelichting |  |
    

Attributen van objecttype Melding

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| illegaal | Boolean |  |
| 24uurs | Boolean |  |
| datumtijd | DateTime |  |
| omschrijving | Text |  |
| meldingnummer | AN40 |  |



### Milieustraat
> **Definitie Milieustraat:** 
>
> Een locatie die specifiek bestemd is voor het brengen van gescheiden huishoudelijk afval en grofvuil.

??? info "Kenmerken Model Milieustraat"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Milieustraat |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-05-20 14:39:16 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_1638F2AF\_F1E8\_4360\_BA47\_D975F2135168 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Milieustraat |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-0310645e-6873-4cb3-93ec-734f0ac3323e](https://gemmaonline.nl/index.php/GEMMA/id-0310645e-6873-4cb3-93ec-734f0ac3323e) |
    | gemma_definitie | Een locatie die specifiek bestemd is voor het brengen van gescheiden huishoudelijk afval en grofvuil. |
    | gemma_toelichting |  |
    

Attributen van objecttype Milieustraat

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| naam | AN80 |  |
| omschrijving | Text |  |
| adresaanduiding | Adresaanduiding |  |



### Ophaalmoment
> **Definitie Ophaalmoment:** 
>
> Een stop die een vuilniswagen maakt tijdens het doen van een rit. Bijgehouden wordt de gewichtstoename van de lading

??? info "Kenmerken Model Ophaalmoment"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Ophaalmoment |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-05-20 14:21:06 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_9079F098\_1084\_4484\_ACCC\_6C6C07043193 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Ophaalmoment |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-21e043b1-6d0c-4fd0-ac07-fd854ed8b9df](https://gemmaonline.nl/index.php/GEMMA/id-21e043b1-6d0c-4fd0-ac07-fd854ed8b9df) |
    | gemma_definitie | Een stop die een vuilniswagen maakt tijdens het doen van een rit. Bijgehouden wordt de gewichtstoename van de lading |
    | gemma_toelichting |  |
    

Attributen van objecttype Ophaalmoment

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| gewichtstoename | int |  |
| tijdstip | DateTime |  |



### Pas
> **Definitie Pas:** 
>
> klein kaartje met je naam en soms je foto erop, dat je toegang geeft tot bepaalde diensten

??? info "Kenmerken Model Pas"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Pas |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.14.0 |
    | created | 2019-05-20 14:41:09 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_F6D7A83B\_30BC\_44f4\_91E2\_74C04DCE87AE |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Pas |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-4f840a95-77ba-47ae-b554-a00db6f905b4](https://gemmaonline.nl/index.php/GEMMA/id-4f840a95-77ba-47ae-b554-a00db6f905b4) |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Pas

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| pasnummer | AN40 |  |
| adresaanduiding | Adresaanduiding |  |



### Prijsafspraak
> **Definitie Prijsafspraak:** 
>
> Overeenkomst tussen concurrenten met betrekking tot de prijs van goederen of diensten.

??? info "Kenmerken Model Prijsafspraak"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Prijsafspraak |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-05-20 14:11:29 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_21BBA828\_AAE0\_4785\_9E44\_45C1B866C882 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Prijsafspraak |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-343e027e-16c9-43d7-8b90-891aaf9c4b70](https://gemmaonline.nl/index.php/GEMMA/id-343e027e-16c9-43d7-8b90-891aaf9c4b70) |
    | gemma_definitie | Overeenkomst tussen concurrenten met betrekking tot de prijs van goederen of diensten. |
    | gemma_toelichting |  |
    

Attributen van objecttype Prijsafspraak

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| datumStart | Date |  |
| datumEinde | Date |  |
| titel | AN200 |  |



### Prijsregel
> **Definitie Prijsregel:** 
>
> Een *prijsregel* is een **regel die aangeeft hoe de prijs van een product, dienst of prestatie wordt vastgesteld of toegepast**, bijvoorbeeld binnen een declaratie- of tariefstructuur.

??? info "Kenmerken Model Prijsregel"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Prijsregel |
    | toelichting | In administratieve en financiële systemen geeft een \*prijsregel\* aan \*\*welke tarieven of prijsinstellingen\*\* gehanteerd moeten worden voor het berekenen van het te factureren bedrag bij een levering of prestatie. Het kan bijvoorbeeld de manier beschrijven waarop een tarief wordt bepaald binnen een declaratiesysteem (zoals in de zorg waar prestaties aan specifieke tarieven zijn gekoppeld) of hoe prijzen worden berekend op basis van volume-, tijds- of productcriteria. Prijsregels worden gebruikt om consistent en systematisch te kunnen berekenen wat er in rekening gebracht mag worden voor een geleverde prestatie. |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.10.0 |
    | created | 2019-05-20 14:11:42 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_E79C6C20\_3D05\_49fb\_96ED\_105B5CD0ABA5 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Prijsregel

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| bedrag | Bedrag |  |
| credit | Boolean |  |



### Rit
> **Definitie Rit:** 
>
> Verplaatsing van een wegvoertuig over een wegpad

??? info "Kenmerken Model Rit"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Rit |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-05-20 14:20:08 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_832DA9A0\_0E64\_4d41\_8266\_38418B095919 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Rit |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-892c2a19-8066-404b-8a04-268f9497dd1c](https://gemmaonline.nl/index.php/GEMMA/id-892c2a19-8066-404b-8a04-268f9497dd1c) |
    | gemma_definitie | Verplaatsing van een wegvoertuig over een wegpad |
    | gemma_toelichting |  |
    

Attributen van objecttype Rit

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| starttijd | DateTime |  |
| eindtijd | DateTime |  |
| ritcode | AN40 |  |



### Route
> **Definitie Route:** 
>
> 
> Routes die gereden worden om bepaalde fracties vuilnis op te halen. Routes gaan langs locaties, waar afhankelijk van de routesoort een containers, bepaalde plekken of adressen worden aangedaan.
> huis-aan-huis: er worden locaties met adressen aangedaan
> illegale dumping, grofvuil: er worden locaties aangedaan (evt met adres)
> containters: er worden locaties met containers aangedaan

??? info "Kenmerken Model Route"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Route |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-05-20 14:09:54 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_55A58838\_3877\_4e76\_B5BF\_26C68FAD463D |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Route |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-024bb42f-38cf-42ba-859d-184221eff16c](https://gemmaonline.nl/index.php/GEMMA/id-024bb42f-38cf-42ba-859d-184221eff16c) |
    | gemma_definitie | Routes die gereden worden om bepaalde fracties vuilnis op te halen. Routes gaan langs locaties, waar afhankelijk van de routesoort een containers, bepaalde plekken of adressen worden aangedaan.<br>huis-aan-huis: er worden locaties met adressen aangedaan |
    | gemma_toelichting |  |
    

Attributen van objecttype Route

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| routecode | AN40 |  |
| routesoort | Routesoort |  |
| geometrie | Point | Geometrie: lijnen die gezamenlijk de route bepalen. Nog onvoldoende ondersteund met GML. Ij dat geval leeglaten. |



### Storting
> **Definitie Storting:** 
>
> Activiteit, inhoudende a. het zich ontdoen van stoffen

??? info "Kenmerken Model Storting"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Storting |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-05-20 14:41:00 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_15910FE7\_D323\_45ff\_AA7F\_CE3C636CE953 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Storting |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-c7dda76d-bcdd-4b63-97dc-9d273b2f9092](https://gemmaonline.nl/index.php/GEMMA/id-c7dda76d-bcdd-4b63-97dc-9d273b2f9092) |
    | gemma_definitie | Activiteit, inhoudende a. het zich ontdoen van stoffen |
    | gemma_toelichting |  |
    

Attributen van objecttype Storting

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| datumtijd | DateTime |  |
| gewicht | int | Gewicht in kilo's |



### Vuilniswagen
> **Definitie Vuilniswagen:** 
>
> Een vrachtwagen die gebruikt wordt om afval in te zamelen bij bedrijven en huishoudens (huisvuil)

??? info "Kenmerken Model Vuilniswagen"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Vuilniswagen |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-05-20 14:10:41 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_9A422266\_783E\_4f48\_9B12\_F442C1B22A45 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Vuilniswagen |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-b8e3111b-1993-4490-bdf4-f8eca8add712](https://gemmaonline.nl/index.php/GEMMA/id-b8e3111b-1993-4490-bdf4-f8eca8add712) |
    | gemma_definitie | Een vrachtwagen die gebruikt wordt om afval in te zamelen bij bedrijven en huishoudens (huisvuil) |
    | gemma_toelichting |  |
    

Attributen van objecttype Vuilniswagen

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| code | AN40 |  |
| type | AN200 |  |
| kenteken | AN8 |  |



### Vulgraadmeting
> **Definitie Vulgraadmeting:** 
>
> Mate waarin een (afval)container gevuld is

??? info "Kenmerken Model Vulgraadmeting"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Vulgraadmeting |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-05-22 11:05:47 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_3650DB98\_AC7B\_46c0\_A607\_C54D69E38E42 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Vulgraadmeting

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| tijdstip | DateTime |  |
| vulgraad | int | Vulgraadpercentage |
| vullingGewicht | int | Gewicht vulling in kilo's |






## Enumeraties Model Afval


### Routesoort
Geen Definitie

Het enumeratie Routesoort kent de volgende waarden:

* **huis-aan-huis**: 
* **illegale dumping**: 
* **hot-spot-locaties**: 
* **vangnetregeling**: 
* **grofvuil**: 


De enumeratie Routesoort heeft de volgende kenmerken:

??? info "Kenmerken Model Routesoort"

    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | Routesoort |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author |  |
    | version | 1.10.0 |
    | created | 2025-03-26 11:12:56 |
    | modified | 2025-12-16 10:28:45 |
    | id | EAID\_0121B2BE\_F262\_4433\_8AA5\_49FC7866EF68 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    


