# Model Jeugdbescherming
## Inleiding
> **Definitie Model Jeugdbescherming:** 
>
> Dit informatiedomein bevat data over inburgeringsplichtigen, zoals persoonlijke gegevens, voortgang in het inburgeringstraject, behaalde resultaten en ondersteuning door gemeenten. Het domein faciliteert de samenwerking en gegevensuitwisseling tussen gemeenten, DUO, COA en andere ketenpartners. De structuur van dit domein is gebaseerd op het informatiemodel Inburgering van de VNG, dat zorgt voor gestandaardiseerde gegevensuitwisseling en procesvoering binnen de inburgeringsketen. Hierdoor wordt een efficiënte uitvoering van de Wet inburgering ondersteund.

??? info "Kenmerken Model Model Jeugdbescherming"

    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | Model Jeugdbescherming |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.2 |
    | created | 2024-04-22 15:35:55 |
    | modified | 2025-03-27 15:28:35 |
    | id | EAPK\_A5CFE1A5\_DE7F\_431a\_B809\_749E6D268B1F |
    

Het model 'Model Jeugdbescherming' kent de volgende objecttypen:

* **Informering**: 
* **Leefgebied**: Een Leefgebied in het kader van jeugdbescherming verwijst naar een specifiek domein binnen het leven van een kind of jongere waarin factoren van invloed zijn op diens veiligheid, welzijn en ontwikkeling. Voorbeelden van leefgebieden zijn gezinssituatie, onderwijs, sociale relaties, gezondheid, vrije tijd en financiën. Bij jeugdbescherming wordt elk leefgebied onderzocht om risico’s en beschermende factoren te identificeren, zodat er een integraal plan kan worden opgesteld om de veiligheid en het welzijn van het kind of de jongere te waarborgen. Leefgebieden vormen daarmee een leidraad voor een holistische benadering in de ondersteuning en interventies.
* **Zorgelijke Situatie**: Een zorgelijke situatie in de context van jeugdbescherming is een omstandigheid waarin de veiligheid, gezondheid, of ontwikkeling van een kind of jongere in het geding is door bijvoorbeeld verwaarlozing, mishandeling, huiselijk geweld, of andere risicofactoren. Deze situaties worden gekenmerkt door signalen van fysieke, emotionele of sociale schade of het ontbreken van een veilige en stabiele omgeving. Een zorgelijke situatie kan leiden tot interventie door jeugdbeschermingsorganisaties om de risico’s te verminderen en het kind of de jongere te beschermen en ondersteunen bij een gezonde en veilige ontwikkeling.
* **Zorgmelding**: Een Zorgmelding is een officiële melding bij een gemeente of jeugdhulporganisatie waarin zorgen worden geuit over de veiligheid, gezondheid, of ontwikkeling van een kind of jongere. Deze melding kan worden gedaan door professionals, zoals leraren, huisartsen of politie, maar ook door burgers of familieleden. Een zorgmelding bevat signalen of concrete aanwijzingen van mogelijke risico’s, zoals mishandeling, verwaarlozing, huiselijk geweld, of een onveilige thuissituatie. Het doel van een zorgmelding is om de situatie te laten beoordelen en, indien nodig, passende hulp of bescherming te organiseren om het welzijn van het kind of de jongere te waarborgen.


## Objecttypen Model Jeugdbescherming


### Informering
> **Definitie Informering:** 
>
> Geen Definitie

??? info "Kenmerken Model Informering"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Informering |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.8.0 |
    | created | 2024-04-22 14:43:24 |
    | modified | 2025-12-16 10:28:34 |
    | id | EAID\_ACC7A392\_9A16\_42a8\_A58E\_1E8E6826B2D0 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Informering

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| indicatieGeinformeerd | Boolean |  |
| redenNietGeinformeerd | Text |  |
| datum | Datum |  |
| reactie | Text |  |



### Leefgebied
> **Definitie Leefgebied:** 
>
> Een Leefgebied in het kader van jeugdbescherming verwijst naar een specifiek domein binnen het leven van een kind of jongere waarin factoren van invloed zijn op diens veiligheid, welzijn en ontwikkeling. Voorbeelden van leefgebieden zijn gezinssituatie, onderwijs, sociale relaties, gezondheid, vrije tijd en financiën. Bij jeugdbescherming wordt elk leefgebied onderzocht om risico’s en beschermende factoren te identificeren, zodat er een integraal plan kan worden opgesteld om de veiligheid en het welzijn van het kind of de jongere te waarborgen. Leefgebieden vormen daarmee een leidraad voor een holistische benadering in de ondersteuning en interventies.

??? info "Kenmerken Model Leefgebied"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Leefgebied |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.10.0 |
    | created | 2024-04-22 14:32:30 |
    | modified | 2025-12-16 10:28:34 |
    | id | EAID\_B061E420\_187A\_49dd\_B8DA\_2AF3FC5D860F |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Leefgebied

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| toelichting | Text |  |
| leefgebied | Enumeratie: "enum_Leefgebied" |  |



### Zorgelijke Situatie
> **Definitie Zorgelijke Situatie:** 
>
> Een zorgelijke situatie in de context van jeugdbescherming is een omstandigheid waarin de veiligheid, gezondheid, of ontwikkeling van een kind of jongere in het geding is door bijvoorbeeld verwaarlozing, mishandeling, huiselijk geweld, of andere risicofactoren. Deze situaties worden gekenmerkt door signalen van fysieke, emotionele of sociale schade of het ontbreken van een veilige en stabiele omgeving. Een zorgelijke situatie kan leiden tot interventie door jeugdbeschermingsorganisaties om de risico’s te verminderen en het kind of de jongere te beschermen en ondersteunen bij een gezonde en veilige ontwikkeling.

??? info "Kenmerken Model Zorgelijke Situatie"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Zorgelijke Situatie |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.10.0 |
    | created | 2024-04-11 14:09:56 |
    | modified | 2025-12-16 10:28:34 |
    | id | EAID\_AEF1825F\_C554\_4490\_975D\_93AEA24991A9 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Zorgelijke Situatie

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| sitiuatieschets | Text |  |
| nadereOmschrijving | Text |  |



### Zorgmelding
> **Definitie Zorgmelding:** 
>
> Een Zorgmelding is een officiële melding bij een gemeente of jeugdhulporganisatie waarin zorgen worden geuit over de veiligheid, gezondheid, of ontwikkeling van een kind of jongere. Deze melding kan worden gedaan door professionals, zoals leraren, huisartsen of politie, maar ook door burgers of familieleden. Een zorgmelding bevat signalen of concrete aanwijzingen van mogelijke risico’s, zoals mishandeling, verwaarlozing, huiselijk geweld, of een onveilige thuissituatie. Het doel van een zorgmelding is om de situatie te laten beoordelen en, indien nodig, passende hulp of bescherming te organiseren om het welzijn van het kind of de jongere te waarborgen.

??? info "Kenmerken Model Zorgmelding"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Zorgmelding |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.10.0 |
    | created | 2024-04-11 13:48:55 |
    | modified | 2025-12-16 10:28:34 |
    | id | EAID\_B852AF03\_A5E0\_4148\_AFC1\_108509FF8BBD |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Zorgmelding

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| zorgmeldingsoort | int |  |
| terugkoppelingGewenst | boolean |  |
| verzoek | Enumeratie: "enum_Verzoeksoort" |  |
| omschrijving | Text |  |
| nadereOmschrijving | Text |  |






## Enumeraties Model Jeugdbescherming


### Enum Sociale Groep
Geen Definitie

Het enumeratie Enum Sociale Groep kent de volgende waarden:



De enumeratie Enum Sociale Groep heeft de volgende kenmerken:

??? info "Kenmerken Model Enum Sociale Groep"

    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | Enum Sociale Groep |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author |  |
    | version | 1.10.0 |
    | created | 2025-03-26 11:12:50 |
    | modified | 2025-12-16 10:28:45 |
    | id | EAID\_B0D22469\_0013\_4e43\_BACF\_4A55A35A8696 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    


### Enum Sociale Relatie
Geen Definitie

Het enumeratie Enum Sociale Relatie kent de volgende waarden:



De enumeratie Enum Sociale Relatie heeft de volgende kenmerken:

??? info "Kenmerken Model Enum Sociale Relatie"

    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | Enum Sociale Relatie |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author |  |
    | version | 1.10.0 |
    | created | 2025-03-26 11:12:50 |
    | modified | 2025-12-16 10:28:45 |
    | id | EAID\_7BFE745C\_388E\_4b4f\_A420\_1F59372F8CD6 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    


### enum_Incidenttype
Geen Definitie

Het enumeratie enum_Incidenttype kent de volgende waarden:



De enumeratie enum_Incidenttype heeft de volgende kenmerken:

??? info "Kenmerken Model enum_Incidenttype"

    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | enum\_Incidenttype |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author |  |
    | version | 1.10.0 |
    | created | 2025-03-26 11:12:50 |
    | modified | 2025-12-16 10:28:45 |
    | id | EAID\_2296EC14\_B00D\_4836\_B553\_1CB1F48CFDB2 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    


### enum_Leefgebied
Geen Definitie

Het enumeratie enum_Leefgebied kent de volgende waarden:



De enumeratie enum_Leefgebied heeft de volgende kenmerken:

??? info "Kenmerken Model enum_Leefgebied"

    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | enum\_Leefgebied |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author |  |
    | version | 1.10.0 |
    | created | 2025-03-26 11:12:50 |
    | modified | 2025-12-16 10:28:45 |
    | id | EAID\_78D6A864\_04BD\_4d3f\_BB6A\_CC9840566D19 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    


### enum_Verzoeksoort
Geen Definitie

Het enumeratie enum_Verzoeksoort kent de volgende waarden:



De enumeratie enum_Verzoeksoort heeft de volgende kenmerken:

??? info "Kenmerken Model enum_Verzoeksoort"

    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | enum\_Verzoeksoort |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author |  |
    | version | 1.10.0 |
    | created | 2025-03-26 11:12:50 |
    | modified | 2025-12-16 10:28:45 |
    | id | EAID\_3D8D8ED8\_A382\_4ffb\_8608\_4846CFF95E28 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    


