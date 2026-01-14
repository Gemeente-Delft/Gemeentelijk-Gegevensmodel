# Model Generiek
## Inleiding
> **Definitie Model Generiek:** 
>
> Geen definitie

??? info "Kenmerken Model Model Generiek"

    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | Model Generiek |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.0 |
    | created | 2019-05-09 15:50:58 |
    | modified | 2019-05-09 15:51:05 |
    | id | EAPK\_1738C6AD\_81AA\_423a\_B053\_982B95D9468A |
    

Het model 'Model Generiek' kent de volgende objecttypen:

* **Foto**: Afbeelding op een plat vlak vervaardigd door middel van fotografie
* **Gebied**: Een aaneengesloten gedeelte van een wijk, waarvan de grenzen zo veel mogelijk gebaseerd zijn op topografische elementen.
* **Gebiedengroep**: Verzameling van gebieden
* **Lijn**: Denkbeeldige streep op de aardoppervlakte
* **Lijnengroep**: Verzameling van lijnen
* **Locatie**: De locatie beschrijft middels co√∂rdinaten de ruimtelijke dimensie of ruimtelijke afbakening van een regel of van een objecttype die in de regel beschreven wordt. (CIMOW)
* **Punt**: Plaats in de ruimte
* **Puntengroep**: Verzameling van punten
* **Video-opname**: Opnametechniek om bewegende beelden als een elektronisch signaal te registreren en weer te geven.


## Objecttypen Model Generiek


### Foto
> **Definitie Foto:** 
>
> Afbeelding op een plat vlak vervaardigd door middel van fotografie

??? info "Kenmerken Model Foto"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Foto |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-05-09 14:47:49 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_7FE4B466\_B051\_4068\_9ED1\_6E60C3B2DBAD |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Foto |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-b285df90-a239-4757-b78e-a281744f89cb](https://gemmaonline.nl/index.php/GEMMA/id-b285df90-a239-4757-b78e-a281744f89cb) |
    | gemma_definitie | Afbeelding op een plat vlak vervaardigd door middel van fotografie |
    | gemma_toelichting |  |
    

Attributen van objecttype Foto

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| bestandsnaam | AN200 |  |
| bestandstype | AN80 |  |
| datumtijd | DateTime |  |
| bestandsgrootte | int | Bestandsgrootte in bytes |
| pixelsX | int |  |
| pixelsY | int |  |
| locatie | Point |  |



### Gebied
> **Definitie Gebied:** 
>
> Een aaneengesloten gedeelte van een wijk, waarvan de grenzen zo veel mogelijk gebaseerd zijn op topografische elementen.

??? info "Kenmerken Model Gebied"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Gebied |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-10-22 09:39:03 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_0303A7A4\_EF51\_4262\_AEE0\_642FA5064807 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Gebied

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| gebiedsAanduiding | MultiSurface |  |



### Gebiedengroep
> **Definitie Gebiedengroep:** 
>
> Verzameling van gebieden

??? info "Kenmerken Model Gebiedengroep"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Gebiedengroep |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-10-22 09:40:17 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_85E3996B\_578D\_4313\_B078\_2773F98412D9 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Gebiedengroep

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Lijn
> **Definitie Lijn:** 
>
> Denkbeeldige streep op de aardoppervlakte

??? info "Kenmerken Model Lijn"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Lijn |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-10-22 09:38:52 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_FAB83AD1\_DC8C\_4f78\_B54F\_33466EB9B139 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Lijn

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| lijnLocatie | Lijn |  |



### Lijnengroep
> **Definitie Lijnengroep:** 
>
> Verzameling van lijnen

??? info "Kenmerken Model Lijnengroep"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Lijnengroep |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-10-22 09:40:05 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_CD06432A\_B69D\_4ab2\_A5B0\_C4C3092835A0 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Lijnengroep

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Locatie
> **Definitie Locatie:** 
>
> De locatie beschrijft middels co√∂rdinaten de ruimtelijke dimensie of ruimtelijke afbakening van een regel of van een objecttype die in de regel beschreven wordt. (CIMOW)

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
    | created | 2019-10-22 09:37:55 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_79284529\_B817\_4e3f\_BE51\_AEAFC60BDE44 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Locatie |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-f1220c91-e576-4a25-9cdb-0a2b991ae362](https://gemmaonline.nl/index.php/GEMMA/id-f1220c91-e576-4a25-9cdb-0a2b991ae362) |
    | gemma_definitie | De locatie beschrijft middels co√∂rdinaten de ruimtelijke dimensie of ruimtelijke afbakening van een regel of van een objecttype die in de regel beschreven wordt. (CIMOW) |
    | gemma_toelichting |  |
    

Attributen van objecttype Locatie

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| naam | AN200 |  |
| hoogte | int | Hoogte in meters. Negatief is onder het maaiveld en positief boven het maaiveld |
| NEN3610ID | AN80 |  |



### Punt
> **Definitie Punt:** 
>
> Plaats in de ruimte

??? info "Kenmerken Model Punt"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Punt |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-10-22 09:38:45 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_20437683\_6777\_4c7b\_B44B\_1E3A216239AA |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Punt

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| puntLocatie | Punt |  |



### Puntengroep
> **Definitie Puntengroep:** 
>
> Verzameling van punten

??? info "Kenmerken Model Puntengroep"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Puntengroep |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-10-22 09:39:56 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_4C0C5DDB\_E5BA\_42a0\_BA5B\_65E2D433B16C |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Puntengroep

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Video-opname
> **Definitie Video-opname:** 
>
> Opnametechniek om bewegende beelden als een elektronisch signaal te registreren en weer te geven.

??? info "Kenmerken Model Video-opname"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Video-opname |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.12.0 |
    | created | 2019-05-16 16:20:58 |
    | modified | 2025-12-18 15:38:51 |
    | id | EAID\_435883D2\_C399\_4590\_B4F5\_B07111103484 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | VideoOpname |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-1d49cf98-d059-42da-bdd4-d076f8ace453](https://gemmaonline.nl/index.php/GEMMA/id-1d49cf98-d059-42da-bdd4-d076f8ace453) |
    | gemma_definitie | Opnametechniek om bewegende beelden als een elektronisch signaal te registreren en weer te geven. |
    | gemma_toelichting |  |
    

Attributen van objecttype Video-opname

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| datumtijd | DateTime |  |
| lengte | int |  |
| videoformaat | AN80 |  |
| bestandsgrootte | int |  |




