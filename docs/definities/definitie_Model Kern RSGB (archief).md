# Model Kern RSGB
## Inleiding
> **Definitie Model Kern RSGB:** 
>
> Het subdomein dat gegevens omvat over gemeentelijke basisgegevens, gebaseerd op het Referentiemodel Stelsel van Gemeentelijke Basisgegevens (RSGB) v2.0.2, aangevuld met specifieke uitbreidingen voor lokaal gebruik en aanvullingen uit RSGB v3.0.

??? info "Kenmerken Model Model Kern RSGB"

    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | Model Kern RSGB |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Verho\_M |
    | version | 1.1 |
    | created | 2025-01-08 09:20:40 |
    | modified | 2025-12-22 15:27:02 |
    | id | EAPK\_9506A6D8\_5471\_4596\_B8DA\_D5CFFD50EEBA |
    

Het model 'Model Kern RSGB' kent de volgende objecttypen:

* **Nummeraanduiding**: Een door het bevoegde gemeentelijke orgaan als zodanig toegekende aanduiding van een VERBLIJFSOBJECT, een STANDPLAATS of een LIGPLAATS.
* **BenoemdObject**: Een GEBOUWD OBJECT of een BENOEMD TERREIN
* **BenoemdTerrein**: Een STANDPLAATS, LIGPLAATS, of een OVERIG BENOEMD TERREIN.
* **Buurt**: Een aaneengesloten gedeelte van een wijk, waarvan de grenzen zo veel mogelijk gebaseerd zijn op topografische elementen.
* **GebouwdObject**: Een VERBLIJFSOBJECT of een OVERIG GEBOUWD OBJECT
* **Gemeente**: Een gedeelte van het grondgebied van Nederland, ingesteld op basis van artikel 123 van de Grondwet.
* **Ligplaats**: 
> Definitie
> Een ligplaats is een door het bevoegde gemeentelijke orgaan als zodanig aangewezen plaats in het water al dan niet aangevuld met een op de oever aanwezig terrein of een gedeelte daarvan, die bestemd is voor het permanent afmeren van een voor woon-, bedrijfsmatige of recreatieve doeleinden geschikt drijvend object
> Beschrijving
> Een plaats in het water met soms ook een (deel van een) terrein op de oever. Deze plaats moet kunnen worden gebruikt door een drijvend object dat langere tijd daar wordt vastgemaakt. Het drijvende object moet geschikt zijn om in te wonen, om een bedrijf in te hebben of om voor plezier in te verblijven. Bijvoorbeeld een woonboot. De gemeente mag zeggen of er voor de BAG ergens een ligplaats komt.
* **AdresseerbaarObjectAanduiding**: Een door het bevoegde gemeentelijke orgaan als zodanig toegekende aanduiding van een VERBLIJFSOBJECT, een STANDPLAATS of een LIGPLAATS.
* **OpenbareRuimte**: Een door het bevoegde gemeentelijke orgaan als zodanig aangewezen en van een naam voorziene buitenruimte die binnen één woonplaats is gelegen
* **Pand**: De kleinste bij de totstandkoming functioneel en bouwkundig-constructief zelfstandige eenheid die direct en duurzaam met de aarde is verbonden en betreedbaar en afsluitbaar is.
* **Standplaats**: Een door het bevoegde gemeentelijke orgaan als zodanig aangewezen terrein of gedeelte daarvan dat bestemd is voor het permanent plaatsen van een niet direct en niet duurzaam met de aarde verbonden en voor woon -, bedrijfsmatige, of recreatieve doeleinden geschikte ruimte.
* **Verblijfsobject**: De kleinste binnen één of meer panden gelegen en voor woon -, bedrijfsmatige, of recreatieve doeleinden geschikte eenheid van gebruik die ontsloten wordt via een eigen afsluitbare toegang vanaf de openbare weg, een erf of een gedeelde verkeersruimte, onderwerp kan zijn van goederenrechtelijke rechtshandelingen en in functioneel opzicht zelfstandig is.
* **Wijk**: Een aaneengesloten gedeelte van het grondgebied van een gemeente, waarvan de grenzen zo veel mogelijk zijn gebaseerd op sociaal-geografische kenmerken.
* **Woonplaats**: Een door het bevoegde gemeentelijke orgaan als zodanig aangewezen en van een naam voorzien gedeelte van het grondgebied van de gemeente.


## Objecttypen Model Kern RSGB


### Nummeraanduiding
> **Definitie Nummeraanduiding:** 
>
> Een door het bevoegde gemeentelijke orgaan als zodanig toegekende aanduiding van een VERBLIJFSOBJECT, een STANDPLAATS of een LIGPLAATS.

??? info "Kenmerken Model Nummeraanduiding"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Nummeraanduiding |
    | toelichting | Het betreft de verzameling van, tot de BAG behorende, officieel vastgestelde nummeraanduidingen (van verblijfsobjecten, stand- en ligplaatsen, in de BAG gezamenlijk aangeduid als adresseerbare objecten) en overige, eveneens officieel door de gemeente vastgestelde, nummeraanduidingen van overige gebouwde objecten en overige benoemde terreinen. De Adresseerbaar object aanduiding heeft dus betrekking op alle 'benoemde objecten', d.w.z. naast de specialisaties van het Adresseerbaar object (Verblijfsobject, Ligplaats en Standplaats) ook op Overig gebouwd object en op Overig benoemd terrein!<br>Het betreft een generalisatie van twee objecttypen (de specialisaties) waarbij de attributen en relaties die op beide specialisaties van toepassing zijn, bij dit objecttype worden gespecificeerd. |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | mante\_h |
    | version | 1.14.0 |
    | created | 2010-07-05 13:31:04 |
    | modified | 2025-12-22 15:44:36 |
    | id | EAID\_31A87864\_6CE0\_4e93\_A493\_ECD0FBDD4461 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Nummeraanduiding |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-403c547f-8d7e-4235-99d9-d155063c6085](https://gemmaonline.nl/index.php/GEMMA/id-403c547f-8d7e-4235-99d9-d155063c6085) |
    | gemma_definitie | Een door het bevoegde gemeentelijke orgaan als zodanig toegekende aanduiding van een VERBLIJFSOBJECT, een STANDPLAATS of een LIGPLAATS. |
    | gemma_toelichting |  |
    

Attributen van objecttype Nummeraanduiding

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| huisletter | AN1 | Een door of namens het bevoegd gemeentelijk orgaan ten aanzien van een adresseerbaar object toegekende toevoeging aan een huisnummer in de vorm van een alfanumeriek teken. |
| huisnummer | N5 | Een door of namens het bevoegd gemeentelijk orgaan ten aanzien van een adresseerbaar object toegekende nummering. |
| huisnummertoevoeging | AN4 | Een door of namens het bevoegd gemeentelijk orgaan ten aanzien van een adresseerbaar object toegekende nadere toevoeging aan een huisnummer of een combinatie van huisnummer en huisletter. |
| postcode | AN6 | De door PostNL vastgestelde code behorende bij een bepaalde combinatie van een naam van een woonplaats, naam van een openbare ruimte en een huisnummer |
| datumBeginGeldigheidNummeraanduiding | DATUM | De datum waarop de ADRESSEERBAAR OBJECT AANDUIDING formeel is vastgesteld. |
| DatumEindeGeldigheidNummeraanduiding | DATUM | De datum waarop de ADRESSEERBAAR OBJECT AANDUIDING formeel is ingetrokken. |
| status | statusNummeraanduiding |  |
| geconstateerd | boolean |  |
| identificatie | BAGObjectnummering |  |
| typeAdresseerbaarObject | TypeAdresseerbaarObject |  |
| inOnderzoek | boolean | Een aanduiding waarmee wordt aangegeven dat een onderzoek wordt uitgevoerd naar de juistheid van een of meerdere gegevens van het betreffende object. |



### BenoemdObject
> **Definitie BenoemdObject:** 
>
> Een GEBOUWD OBJECT of een BENOEMD TERREIN

??? info "Kenmerken Model BenoemdObject"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | BenoemdObject |
    | toelichting | Het objecttype betreft alle objecten die van een, al dan niet authentieke, nummeraanduiding voorzien worden. Anders gezegd, alle objecten ‘met een adres’. Het is aldus de generalisatie van zowel GEBOUWD OBJECT en BENOEMD TERREIN en daarmee tevens van alle specialisaties van deze objecttypen, met name VERBLIJFSOBJECT, OVERIG BOUWWERK, STANDPLAATS, LIGPLAATS en OVERIG BENOEMD TERREIN. |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | mante\_h |
    | version | 1.14.0 |
    | created | 2010-07-04 23:09:31 |
    | modified | 2025-12-22 15:44:36 |
    | id | EAID\_3E9E08B7\_574E\_43dc\_8D93\_251BFA8F8D75 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | BenoemdObject |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-13ad6d22-52ce-4439-9eed-200245c3a498](https://gemmaonline.nl/index.php/GEMMA/id-13ad6d22-52ce-4439-9eed-200245c3a498) |
    | gemma_definitie | Een GEBOUWD OBJECT of een BENOEMD TERREIN |
    | gemma_toelichting |  |
    

Attributen van objecttype BenoemdObject

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| identificatie | AN100 |  |
| datumBeginGeldigheid | Date |  |
| datumEindeGeldigheid | Date |  |
| geometriePunt | Point |  |
| geometrieVlak | Surface |  |



### BenoemdTerrein
> **Definitie BenoemdTerrein:** 
>
> Een STANDPLAATS, LIGPLAATS, of een OVERIG BENOEMD TERREIN.

??? info "Kenmerken Model BenoemdTerrein"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | BenoemdTerrein |
    | toelichting | Een benoemd terrein is de groepering van de authentieke stand- en ligplaatsen en de overige benoemde terreinen en modelleert daarmee de terreinen op het niveau van stand- en ligplaatsen en daarmee vergelijkbare onbe- en ongebouwde objecten voor zover dat door de gemeente als relevant wordt gezien. Het gaat daarbij om terreinen met een verblijfsfunctie, naar analogie van de stand- en ligplaatsen, zijnde geen stand- en ligplaatsen en waarvan de vindbaarheid in het maatschappelijk verkeer op basis van een officieel adres dringend gewenst is.<br>De minimale verzameling is die van de stand- en ligplaatsen; een gemeente kan daaraan toevoegen andere (overige) benoemde terreinen. Een BENOEMD TERREIN is een specialisatie van BENOEMD OBJECT. |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | mante\_h |
    | version | 1.14.0 |
    | created | 2010-07-04 23:25:38 |
    | modified | 2025-12-22 15:44:36 |
    | id | EAID\_73F1C4A1\_481E\_4052\_A372\_1A0895ED1295 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | BenoemdTerrein |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-c0361a4b-968e-477e-b81c-ee26a5aa0543](https://gemmaonline.nl/index.php/GEMMA/id-c0361a4b-968e-477e-b81c-ee26a5aa0543) |
    | gemma_definitie | Een STANDPLAATS, LIGPLAATS, of een OVERIG BENOEMD TERREIN. |
    | gemma_toelichting |  |
    

Attributen van objecttype BenoemdTerrein

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| identificatie | AN100 |  |



### Buurt
> **Definitie Buurt:** 
>
> Een aaneengesloten gedeelte van een wijk, waarvan de grenzen zo veel mogelijk gebaseerd zijn op topografische elementen.

??? info "Kenmerken Model Buurt"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Buurt |
    | toelichting | Het betreft hier de in overleg met het CBS bepaalde indeling van wijken in buurten. |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | mante\_h |
    | version | 1.14.0 |
    | created | 2010-07-05 14:39:50 |
    | modified | 2025-12-22 15:44:36 |
    | id | EAID\_67CC2144\_6B88\_433c\_853D\_07379C66D6CF |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Buurt |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-8772e7a6-24c8-454f-ab54-7d12c1849e97](https://gemmaonline.nl/index.php/GEMMA/id-8772e7a6-24c8-454f-ab54-7d12c1849e97) |
    | gemma_definitie | Een aaneengesloten gedeelte van een wijk, waarvan de grenzen zo veel mogelijk gebaseerd zijn op topografische elementen. |
    | gemma_toelichting |  |
    

Attributen van objecttype Buurt

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| buurtcode | AN2 | De code behorende bij de naam van de buurt. |
| identificatieIMGeoBRT | NEN3610ID | De unieke identificatie van de buurt zoals is toegekend in de IMGeo administratie |
| buurtnaam | AN40 | De naam van de buurt, zoals die door het CBS wordt gebruikt. |
| buurtgeometrie | MultiSurface | De tweedimensionale geometrische representatie van de omtrekken van de buurt. |
| datumBeginGeldigheidBuurt | DATUM | De datum waarop de buurt is gecreëerd. |
| datumEindeGeldigheidBuurt | DATUM | De datum waarop een buurt is komen te vervallen. |
| identificatie | AN100 |  |



### GebouwdObject
> **Definitie GebouwdObject:** 
>
> Een VERBLIJFSOBJECT of een OVERIG GEBOUWD OBJECT

??? info "Kenmerken Model GebouwdObject"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | GebouwdObject |
    | toelichting | Een gebouwd object is de groepering van de authentieke verblijfsobjecten en de overige bouwwerken en modelleert daarmee de gebouwde omgeving op het niveau van het verblijfsobject en daarmee vergelijkbare objecten voor zover dat door de gemeente als relevant wordt gezien. Het gaat daarbij primair om objecten met een verblijfsfunctie, naar analogie van de verblijfsobjecten, zijnde geen verblijfsobjecten en waarvan de vindbaarheid in het maatschappelijk verkeer op basis van een officieel adres dringend gewenst is.<br>De minimale verzameling is die van de verblijfsobjecten; een gemeente kan daaraan toevoegen andere (overige) bouwwerken.<br>Een GEBOUWD OBJECT is een specialisatie van BENOEMD OBJECT. |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | mante\_h |
    | version | 1.14.0 |
    | created | 2010-07-05 00:32:55 |
    | modified | 2025-12-22 15:44:36 |
    | id | EAID\_752621CC\_D5CA\_4f4c\_A937\_AF6C84E6ADED |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | GebouwdObject |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-f048185d-8eb4-447b-ade2-6160df1dedb3](https://gemmaonline.nl/index.php/GEMMA/id-f048185d-8eb4-447b-ade2-6160df1dedb3) |
    | gemma_definitie | Een VERBLIJFSOBJECT of een OVERIG GEBOUWD OBJECT |
    | gemma_toelichting |  |
    

Attributen van objecttype GebouwdObject

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| bouwkundigeBestemmingActueel | bouwkundigeBestemming | Zoals vastgelegd in de bouwvergunning of een toetsing van een melding bouwvoornemen dan wel vastgelegd in een zogenaamde herbeschrijving van een bestemming. |
| statusVoortgangBouw | statusVoortgangBouw | De fase van de bouw, verbouw of sloop waarin het betreffende GEBOUWD OBJECT zich bevindt. |
| brutoInhoud | N6 | Aanduiding in kubieke meters van de bruto inhoud van het GEBOUWD OBJECT |
| oppervlakteObject | N6 | De gebruiksoppervlakte van een VERBLIJFSOBJECT of het OVERIG BOUWWERK |
| inwinningOppervlakte | inwinningsmethodeOppervlakte | De wijze waarop de gebruiksoppervlakte van het GEBOUWD OBJECT verkregen is |
| identificatie | AN100 |  |



### Gemeente
> **Definitie Gemeente:** 
>
> Een gedeelte van het grondgebied van Nederland, ingesteld op basis van artikel 123 van de Grondwet.

??? info "Kenmerken Model Gemeente"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Gemeente |
    | toelichting | De gemeente fungeert in het model als geo-object. Door de relatie van gemeente met andere objecttypen kan achterhaald worden welke gemeente verantwoordelijk is voor het beheer van de hieraan gerelateerde objecten en gegevens. |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | mante\_h |
    | version | 1.14.0 |
    | created | 2010-07-05 14:31:43 |
    | modified | 2025-12-22 15:44:36 |
    | id | EAID\_B0D9792B\_46E7\_4b88\_B267\_C72691616733 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Gemeente |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-9f1ea854-eb45-47a0-98f4-4043b4a69be0](https://gemmaonline.nl/index.php/GEMMA/id-9f1ea854-eb45-47a0-98f4-4043b4a69be0) |
    | gemma_definitie | Een gedeelte van het grondgebied van Nederland, ingesteld op basis van artikel 123 van de Grondwet. |
    | gemma_toelichting |  |
    

Attributen van objecttype Gemeente

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| gemeentecode | AN4 | Een numerieke aanduiding waarmee een Nederlandse gemeente uniek wordt aangeduid |
| gemeentenaam | AN80 | De officiële door de gemeente vastgestelde gemeentenaam. |
| gemeentenaamNEN | AN24 | De officieel vastgestelde en waar nodig ingekorte naam van de gemeente |
| gemeenteGeometrie | Surface | De tweedimensionale geometrische representatie van de omtrekken van het grondgebied van een gemeente. |
| datumBeginGeldigheidGemeente | DATUM | De datum waarop de gemeente is ontstaan. |
| datumEindeGeldigheidGemeente | DATUM | De datum waarop de gemeente is opgeheven. |
| identificatie | AN100 |  |



### Ligplaats
> **Definitie Ligplaats:** 
>
> 
> Definitie
> Een ligplaats is een door het bevoegde gemeentelijke orgaan als zodanig aangewezen plaats in het water al dan niet aangevuld met een op de oever aanwezig terrein of een gedeelte daarvan, die bestemd is voor het permanent afmeren van een voor woon-, bedrijfsmatige of recreatieve doeleinden geschikt drijvend object
> Beschrijving
> Een plaats in het water met soms ook een (deel van een) terrein op de oever. Deze plaats moet kunnen worden gebruikt door een drijvend object dat langere tijd daar wordt vastgemaakt. Het drijvende object moet geschikt zijn om in te wonen, om een bedrijf in te hebben of om voor plezier in te verblijven. Bijvoorbeeld een woonboot. De gemeente mag zeggen of er voor de BAG ergens een ligplaats komt.

??? info "Kenmerken Model Ligplaats"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Ligplaats |
    | toelichting | Een ligplaats maakt in de BAG-terminologie deel uit van de groep adresseerbare objecten.<br>Hier maakt het, gezamenlijk met de STANDPLAATS en het OVERIG BENOEMD TERREIN deel uit van de groep BENOEMD TERREIN. |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | mante\_h |
    | version | 1.14.0 |
    | created | 2010-07-05 00:21:01 |
    | modified | 2025-12-22 15:44:36 |
    | id | EAID\_F4978264\_32A5\_4e70\_97A8\_D142B64400A8 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Ligplaats

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| ligplaatsidentificatie | BAGObjectnummering | De unieke aanduiding van een LIGPLAATS |
| indicatieGeconstateerdeLigplaats | boolean | Een aanduiding waarmee kan worden aangegeven dat een object in de registratie is opgenomen als gevolg van een feitelijke constatering, zonder dat er op het moment van opname sprake is van een formele grondslag voor deze opname. |
| ligplaatsstatus | StatLigplaatsStandplaats | De fase van de levenscyclus van een LIGPLAATS waarin de betreffende LIGPLAATS zich bevindt. |
| inOnderzoek | boolean | BRK gegeven |
| datumDocument | Date | De datum waarop het brondocument is vastgesteld op basis waarvan een opname, mutatie of een verwijdering van gegevens ten aanzien van een object heeft plaatsgevonden. |
| documentNummer | int | De unieke aanduiding van het brondocument op basis waarvan een opname, mutatie of een verwijdering van gegevens ten aanzien van een woonplaats heef plaatsgevonden binnen een gemeente. |



### AdresseerbaarObjectAanduiding
> **Definitie AdresseerbaarObjectAanduiding:** 
>
> Een door het bevoegde gemeentelijke orgaan als zodanig toegekende aanduiding van een VERBLIJFSOBJECT, een STANDPLAATS of een LIGPLAATS.

??? info "Kenmerken Model AdresseerbaarObjectAanduiding"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | AdresseerbaarObjectAanduiding |
    | toelichting | Zie de toelichting in de Catalogus BAG. In aanvulling hierop het volgende. Het betreft alle gegevens en relaties van de NUMMERAANDUIDING zoals deze in de BAG gedefinieerd zijn. NUMMERAANDUIDING is gemodelleerd als een specialisatie van ADRESSEERBAAR OBJECT AANDUIDING. Daar bij overige (officieel vastgestelde) adressen deels vergelijkbare gegevens en relaties van toepassing zijn, zijn desbetreffende gegevens gemodelleerd bij ADRESSEERBAAR OBJECT AANDUIDING, de verzameling van nummeraanduidingen en overige adresseerbaar object aanduidingen. |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | mante\_h |
    | version | 1.14.0 |
    | created | 2010-07-06 13:40:09 |
    | modified | 2025-12-22 15:44:36 |
    | id | EAID\_BA35A5E2\_5A1D\_4328\_91CD\_D51694ED5FBA |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | AdresseerbaarObjectAanduiding |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-cc3c2d8f-cb2f-4e39-a220-bff533892688](https://gemmaonline.nl/index.php/GEMMA/id-cc3c2d8f-cb2f-4e39-a220-bff533892688) |
    | gemma_definitie | Een door het bevoegde gemeentelijke orgaan als zodanig toegekende aanduiding van een VERBLIJFSOBJECT, een STANDPLAATS of een LIGPLAATS. |
    | gemma_toelichting |  |
    

Attributen van objecttype AdresseerbaarObjectAanduiding

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| identificatie | AN100 | De unieke aanduiding van een NUMMERAANDUIDING. |



### OpenbareRuimte
> **Definitie OpenbareRuimte:** 
>
> Een door het bevoegde gemeentelijke orgaan als zodanig aangewezen en van een naam voorziene buitenruimte die binnen één woonplaats is gelegen

??? info "Kenmerken Model OpenbareRuimte"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | OpenbareRuimte |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | mante\_h |
    | version | 1.14.0 |
    | created | 2010-07-05 14:05:00 |
    | modified | 2025-12-22 15:44:36 |
    | id | EAID\_FB13857C\_C695\_4b53\_8060\_BACFA0E16950 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | OpenbareRuimte |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-bb6b6dd2-7b6a-4146-afc0-c5647256ef11](https://gemmaonline.nl/index.php/GEMMA/id-bb6b6dd2-7b6a-4146-afc0-c5647256ef11) |
    | gemma_definitie | Een door het bevoegde gemeentelijke orgaan als zodanig aangewezen en van een naam voorziene buitenruimte die binnen één woonplaats is gelegen |
    | gemma_toelichting |  |
    

Attributen van objecttype OpenbareRuimte

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| IdentificatiecodeOpenbareRuimte | BAGObjectnummering | De unieke aanduiding van een OPENBARE RUIMTE. |
| identificatieIMGeoOPR | NEN3610ID | De unieke identificatie van de openbare ruimte zoals is toegekend in de IMGeo administratie |
| statusOpenbareRuimte | statusOpenbareRuimte | De fase van de levenscyclus van een OPENBARE RUIMTE, waarin de betreffende OPENBARE RUIMTE zich bevindt |
| naamOpenbareRuimte | AN80 | Een door het bevoegde gemeentelijke orgaan aan een OPENBARE RUIMTE toegekende benaming |
| indicatieGeconstateerdeOpenbareRuimte | INDIC | Een aanduiding waarmee kan worden aangegeven dat een object in de registratie is opgenomen als gevolg van een feitelijke constatering, zonder dat er op het moment van opname sprake is van een formele grondslag voor deze opname |
| typeOpenbareRuimte | typeringOpenbareRuimte | De aard van de als zodanig benoemde OPENBARE<br>RUIMTE. |
| straatnaam | AN24 | De officiële straatnaam zoals door het bevoegd gemeentelijk orgaan is vastgesteld, zo nodig ingekort conform de specificaties van de NEN 5825. |
| huisnummerrangeEvenNummers | AN11 | Het laagste en het hoogste huisnummer, zijnde even getallen, van de objecten waaraan NUMMERAANDUIDINGen zijn toegekend die gerelateerd zijn aan de OPENBARE RUIMTE en die gelegen zijn aan één van beide zijden van de OPENBARE RUIMTE. |
| HuisnummerrangeOnevenNummers | AN11 | Het laagste en het hoogste huisnummer, zijnde oneven getallen, van de objecten waaraan NUMMERAANDUIDINGen zijn toegekend die gerelateerd zijn aan de OPENBARE RUIMTE en die gelegen zijn aan één van beide zijden van de OPENBARE RUIMTE. |
| huisnummerrangeEvenEnOnevenNummers | AN11 | Het laagste en het hoogste huisnummer van de objecten waaraan NUMMERAANDUIDINGen zijn toegekend die gerelateerd zijn aan de OPENBARE RUIMTE in die gevallen dat aan één of beide zijden van de OPENBARE RUIMTE zowel even als oneven huisnummers voorkomen dan wel dat even en/of oneven huisnummers aan beide zijden van de openbare ruimte voorkomen. |
| labelNaamOpenbareRuimte | TypeLabel | Bevat de naam van de openbare ruimte ten behoeve van visualisatie. |
| openbareRuimteGeometrie | MultiSurface | De tweedimensionale geometrische representatie van de omtrekken van de openbare ruimte. |
| wegsegment | Curve | De geometrische representatie van de openbare ruimte als een lijn. |
| datumBeginGeldigheidOpenbareRuimte | DATUM | De datum waarop de OPENBARE RUIMTE formeel is benoemd. |
| datumEindeGeldigheidOpenbareRuimte | DATUM | De datum waarop formeel is besloten de OPENBARE RUIMTE niet langer te laten bestaan. |
| inOnderzoek | boolean | uit de BRK |



### Pand
> **Definitie Pand:** 
>
> De kleinste bij de totstandkoming functioneel en bouwkundig-constructief zelfstandige eenheid die direct en duurzaam met de aarde is verbonden en betreedbaar en afsluitbaar is.

??? info "Kenmerken Model Pand"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Pand |
    | toelichting | Objecttype PAND is het equivalent van het city gml objecttype BUILDING PART. |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | mante\_h |
    | version | 1.14.0 |
    | created | 2010-07-05 14:45:48 |
    | modified | 2025-12-22 15:44:36 |
    | id | EAID\_26D1113F\_F7B3\_4bdd\_9AAE\_EA14CC9F3C3F |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Pand |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-1affb298-091d-452a-83bd-29638650afb5](https://gemmaonline.nl/index.php/GEMMA/id-1affb298-091d-452a-83bd-29638650afb5) |
    | gemma_definitie | De kleinste bij de totstandkoming functioneel en bouwkundig-constructief zelfstandige eenheid die direct en duurzaam met de aarde is verbonden en betreedbaar en afsluitbaar is. |
    | gemma_toelichting |  |
    

Attributen van objecttype Pand

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| pandidentificatie | BAGObjectnummering | De unieke aanduiding van een PAND |
| pandstatus | statusPand | De fase van de levenscyclus van een PAND, waarin het betreffende PAND zich bevindt. |
| statusVoortgangBouw | statusVoortgangBouw | De fase van de bouw, verbouw of sloop waarin het betreffende PAND zich bevindt |
| oorspronkelijkBouwjaarPand | N4 | De aanduiding van het jaar waarin een PAND oorspronkelijk als bouwkundig gereed is of wordt opgeleverd. |
| oppervlaktePand | N6 | De gebruiksoppervlakte van een PAND in gehele vierkante meters. |
| brutoInhoudPand | N6 | Aanduiding in kubieke meters van de bruto inhoud van het PAND. |
| indicatieGeconstateerdPand | boolean | Een aanduiding waarmee kan worden aangegeven dat een object in de registratie is opgenomen als gevolg van een feitelijke constatering, zonder dat er op het moment van opname sprake is van een formele grondslag voor deze opname. |
| hoogsteBouwlaagPand | N3 | De ligging van de hoogste bouwlaag van het pand gerekend ten opzichte van het straatpeil. |
| laagsteBouwlaagPand | N3 | De ligging van de laagste bouwlaag van het pand gerekend ten opzichte van het straatpeil. |
| pandgeometrieBovenaanzicht | Surface | De minimaal tweedimensionale geometrische representatie van het bovenaanzicht van de omtrekken van een PAND |
| inwinningGeometrieBovenaanzicht | inwinningsmethodeGeometrie | De wijze waarop de geometrie van het bovenaanzicht van het PAND verkregen is |
| pandgeometrieMaaiveld | MultiSurface | De tweedimensionale geometrische representatie van de omtrekken van een PAND op maaiveldniveau |
| inwinningGeometrieMaaiveld | inwinningsmethodeGeometrie | De wijze waarop de geometrie van het PAND op maaiveldniveau verkregen is |
| relatieveHoogteliggingPand | N2 | Aanduiding voor de relatieve hoogte van het pand |
| LOD1GeometriePand | Object | De geometrische representatie van een pand als in 3D op level of detail 1. |
| LOD2GeometriePand | Object | De geometrische representatie van een pand in 3D op level of detail 2. |
| lod3GeometriePand | Object | De geometrische representatie van een pand in 3D op level of detail 3. |
| identificatieBGTPND | NEN3610ID | Verwijzing naar de unieke identificatie van het pand zoals is toegekend in de BGT/IMGeo administratie. |
| indicatiePlanobject | boolean | Een aanduiding dat de verwijzing naar het pandobject in de BGT een geplande geometriewijziging van een bestaand pandobject betreft. |
| labelNummeraanduidingreeks | TypeLabel | Bevat de reeks nummeraanduidingen behorend bij het pand ten behoeve van visualisatie. |
| datumBeginGeldigheidPand | DATUM | De datum waarop van gemeentewege is vastgesteld dat de bouwwerkzaamheden betreffende de oprichting van een PAND conform de vergunning, de melding of de aanschrijving zijn uitgevoerd. |
| datumEindeGeldigheidPand | DATUM | De datum waarop het pand is gesloopt volgens de sloopgereedmelding. |
| geometriePunt | Point |  |



### Standplaats
> **Definitie Standplaats:** 
>
> Een door het bevoegde gemeentelijke orgaan als zodanig aangewezen terrein of gedeelte daarvan dat bestemd is voor het permanent plaatsen van een niet direct en niet duurzaam met de aarde verbonden en voor woon -, bedrijfsmatige, of recreatieve doeleinden geschikte ruimte.

??? info "Kenmerken Model Standplaats"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Standplaats |
    | toelichting | Een standplaats maakt in de BAG-terminologie deel uit van de groep adresseerbare objecten. Hier maakt het, gezamenlijk met de LIGPLAATS en het OVERIG BENOEMD TERREIN deel uit van de groep BENOEMD TERREIN. |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | mante\_h |
    | version | 1.14.0 |
    | created | 2010-07-05 00:11:57 |
    | modified | 2025-12-22 15:44:36 |
    | id | EAID\_B1C6CA45\_49C9\_45f0\_8B14\_A721AD505C50 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Standplaats

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| standplaatsidentificatie | BAGObjectnummering | De unieke aanduiding van een STANDPLAATS. |
| indicatieGeconstateerdeStandplaats | boolean | Een aanduiding waarmee kan worden aangegeven dat een object in de registratie is opgenomen als gevolg van een feitelijke constatering, zonder dat er op het moment van opname sprake is van een formele grondslag voor deze opname. |
| standplaatsstatus | StatLigplaatsStandplaats | De fase van de levenscyclus van een STANDPLAATS waarin de betreffende STANDPLAATS zich bevindt. |



### Verblijfsobject
> **Definitie Verblijfsobject:** 
>
> De kleinste binnen één of meer panden gelegen en voor woon -, bedrijfsmatige, of recreatieve doeleinden geschikte eenheid van gebruik die ontsloten wordt via een eigen afsluitbare toegang vanaf de openbare weg, een erf of een gedeelde verkeersruimte, onderwerp kan zijn van goederenrechtelijke rechtshandelingen en in functioneel opzicht zelfstandig is.

??? info "Kenmerken Model Verblijfsobject"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Verblijfsobject |
    | toelichting | Zie de catalogus BAG. |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | mante\_h |
    | version | 1.14.0 |
    | created | 2010-07-05 00:38:12 |
    | modified | 2025-12-22 15:44:36 |
    | id | EAID\_A33151CE\_37B2\_4026\_B0AF\_B541687B5B7C |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Verblijfsobject |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-67a1d348-4663-4a34-8b6a-06b3ea888a9d](https://gemmaonline.nl/index.php/GEMMA/id-67a1d348-4663-4a34-8b6a-06b3ea888a9d) |
    | gemma_definitie | De kleinste binnen één of meer panden gelegen en voor woon -, bedrijfsmatige, of recreatieve doeleinden geschikte eenheid van gebruik die ontsloten wordt via een eigen afsluitbare toegang vanaf de openbare weg, een erf of een gedeelde verkeersruimte, onde |
    | gemma_toelichting |  |
    

Attributen van objecttype Verblijfsobject

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| verblijfsobjectidentificatie | BAGObjectnummering | De unieke identificatie van een VERBLIJFSOBJECT. |
| verblijfsobjectstatus | statusVerblijfsobject | De fase van de levenscyclus van een VERBLIJFSOBJECT, waarin het betreffende VERBLIJFSOBJECT zich bevindt. |
| indicatieGeconstateerdVerblijfsobject | INDIC | Een aanduiding waarmee kan worden aangegeven dat een object in de registratie is opgenomen als gevolg van een feitelijke constatering, zonder dat er op het moment van opname sprake is van een formele grondslag voor deze opname. |
| hoogsteBouwlaagVerblijfsobject | N3 | De ligging van de hoogste bouwlaag van het verblijfsobject gerekend ten opzichte van het straatpeil. |
| laagsteBouwlaagVerblijfsobject | N3 | De ligging van de laagste bouwlaag van het verblijfsobject gerekend ten opzichte van het straatpeil. |
| toegangBouwlaagVerblijfsobject | N3 | De ligging van de bouwlaag van het verblijfsobject, gerekend ten opzichte van het straatpeil, waarop zich de hoofdtoegang tot het verblijfsobject bevindt. |
| soortWoonobject | soortWoonobject | Indeling van woonverblijven volgens het CBS. |
| aantalKamers | N2 | Het aantal kamers van het Verblijfsobject in de situatie tijdens de bouw. |
| inOnderzoek | boolean | Een aanduiding waarmee wordt aangegeven dat een onderzoek wordt uitgevoerd naar de juistheid van een of meerdere gegevens van het betreffende object. |
| ontsluitingVerdieping | ontsluitingswijzeVerdieping | Aanduiding van de manier waarop de desbetreffende bouwlaag van een object toegankelijk is gemaakt. |



### Wijk
> **Definitie Wijk:** 
>
> Een aaneengesloten gedeelte van het grondgebied van een gemeente, waarvan de grenzen zo veel mogelijk zijn gebaseerd op sociaal-geografische kenmerken.

??? info "Kenmerken Model Wijk"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Wijk |
    | toelichting | Het betreft hier de in overleg met het CBS bepaalde indeling van de gemeente in wijken. |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | mante\_h |
    | version | 1.14.0 |
    | created | 2010-07-05 14:35:18 |
    | modified | 2025-12-22 15:44:36 |
    | id | EAID\_2F759BC4\_7E3C\_4ce9\_94FF\_33A4106A6E5A |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Wijk |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-fd33a9fa-9c73-43a1-8e22-8cff15dc84d9](https://gemmaonline.nl/index.php/GEMMA/id-fd33a9fa-9c73-43a1-8e22-8cff15dc84d9) |
    | gemma_definitie | Een aaneengesloten gedeelte van het grondgebied van een gemeente, waarvan de grenzen zo veel mogelijk zijn gebaseerd op sociaal-geografische kenmerken. |
    | gemma_toelichting |  |
    

Attributen van objecttype Wijk

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| wijkcode | AN2 | De code behorende bij de naam van de wijk. |
| identificatieIMGeoWYK | NEN3610ID | De unieke identificatie van de wijk zoals is toegekend in de IMGeo administratie |
| wijknaam | AN40 | De naam van de wijk, zoals die door het CBS wordt gebruikt. |
| geometrieWijk | MultiSurface | De tweedimensionale geometrische representatie van de omtrekken van de wijk. |
| datumBeginGeldigheidWijk | DATUM | De datum waarop de wijk is gecreëerd. |
| datumEindeGeldigheidWijk | DATUM | De datum waarop een wijk is komen te vervallen. |
| identificatie | AN100 |  |



### Woonplaats
> **Definitie Woonplaats:** 
>
> Een door het bevoegde gemeentelijke orgaan als zodanig aangewezen en van een naam voorzien gedeelte van het grondgebied van de gemeente.

??? info "Kenmerken Model Woonplaats"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Woonplaats |
    | toelichting | In incidentele gevallen komt het voor dat een woonplaats (in de zin van het gebied dat in de praktijk aangeduid wordt met dezelfde woonplaatsnaam) doorsneden wordt door een gemeentegrens. Volgens de definitie zou dit niet kunnen c.q. is een woonplaats anders gedefinieerd en dus afgebakend: “gedeelte van het gemeentelijk grondgebied”. Vooralsnog wordt uitgegaan van de BAG-insteek en wordt afgewacht hoe dit opgelost wordt in de landelijk te specificeren woonplaatsentabel. |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | mante\_h |
    | version | 1.14.0 |
    | created | 2010-07-05 14:23:09 |
    | modified | 2025-12-22 15:44:36 |
    | id | EAID\_039AFF88\_F5F7\_4c1a\_B7E4\_1BDFC495F67A |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam | Woonplaats |
    | gemma_type | business-object |
    | gemma_url | [https://gemmaonline.nl/index.php/GEMMA/id-c063970e-27f6-45a2-88e8-0105dbbce716](https://gemmaonline.nl/index.php/GEMMA/id-c063970e-27f6-45a2-88e8-0105dbbce716) |
    | gemma_definitie | Een door het bevoegde gemeentelijke orgaan als zodanig aangewezen en van een naam voorzien gedeelte van het grondgebied van de gemeente. |
    | gemma_toelichting |  |
    

Attributen van objecttype Woonplaats

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| woonplaatsIdentificatie | AN4 | De unieke aanduiding van een WOONPLAATS, zoals opgenomen in de landelijke woonplaatsentabel. |
| woonplaatsNaam | AN80 | De door het bevoegde gemeentelijke orgaan aan een WOONPLAATS toegekende benaming. |
| woonplaatsNaamNEN | AN24 | De officiële plaatsnaam conform NEN |
| indicatieGeconstateerdeWoonplaats | INDIC | Een aanduiding waarmee kan worden aangegeven dat een object in de registratie is opgenomen als gevolg van een feitelijke constatering, zonder dat er op het moment van opname sprake is van een formele grondslag voor deze opname. |
| woonplaatsStatus | statusWoonplaats | De fase van de levenscyclus van een WOONPLAATS, waarin de betreffende WOONPLAATS zich bevindt. |
| geometrieWoonplaats | Surface | De tweedimensionale geometrische representatie van het vlak dat wordt gevormd door de omtrekken van een woonplaats. |
| datumBeginGeldigheidWoonplaats | DATUM | De datum waarop de woonplaats is ontstaan. |
| datumEindeGeldigheidWoonplaats | DATUM | De datum waarop de woonplaats is komen te vervallen. |
| inOnderzoek | boolean |  |




