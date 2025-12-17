# Model Normafwijking
## Inleiding
> **Definitie Model Normafwijking:** 
>
> Het onderdeel Normafwijking bricht zich op de registratie en afhandeling van situaties waarin een afwijking van de gestelde normen wordt geconstateerd bij inkomensvoorzieningen.

??? info "Kenmerken Model Model Normafwijking"

    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | Model Normafwijking |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | janbr |
    | version | 1.1 |
    | created | 2024-06-27 21:51:28 |
    | modified | 2025-03-27 15:33:40 |
    | id | EAPK\_2D091BA6\_1407\_C3BE\_D193\_3743D37AB694 |
    

Het model 'Model Normafwijking' kent de volgende objecttypen:

* **Afwijkende maatregel**: Een *afwijkende maatregel* is een maatregel die afwijkt van de standaardregel of wettelijke norm en die op basis van een wettelijke grondslag, beleidsregel of gemotiveerde beslissing in een concreet geval wordt toegepast.
* **Boete**: Een boete is de uitkomst van een onderzoek naar rechtmatigheid. Dit leidt in principe tot een terug te vorderen bedrag. Er is voor gekozen om dit als aparte klasse te modelleren en niet als typering van een vordering, omdat we dit gegeven ook willen gebruiken bij risicoprofilering. Als de vordering niet (meer) bestaat, zou dit gegeven daarmee niet beschikbaar zijn.Daarnaast kan dit ook helpen bij het vastleggen van een boete van een poging tot fraude (zonder financiele consequenties, waardoor geen vordering is ontstaan. (tijdig ondekte valsheid in geschifte e.d.).Bij bedragen hoger dan 50.000 euro, wordt aangifte van fraude gedaan en volgt strafrechtelijk onderzoek.Feitelijk is het uitgangspunt bij het opleggen van een boete dat er altijd sprake is van opzet. Daarom is een apart gegeven Fraude niet opgenomen.
* **Maatregel**: Een *maatregel* is een besluit of handeling waarmee een bestuursorgaan of rechter ingrijpt om een doel te bereiken, een probleem op te lossen of een regel te handhaven.
* **Maatregel op uitkering**: Een *maatregel op uitkering* is een sanctie van een uitvoerend orgaan (zoals een gemeente) waarbij de hoogte van een uitkering tijdelijk wordt verlaagd of aangepast omdat de uitkeringsgerechtigde niet heeft voldaan aan de aan de uitkering verbonden verplichtingen.
* **Normafwijking**: Een *normafwijking* (in het kader van bijstand) is het constateren dat een bijstandsgerechtigde **afwijkt van de normatieve verplichtingen** die verbonden zijn aan het recht op bijstand (bijv. arbeids- of inlichtingenplicht), wat aanleiding kan geven tot toepassing van een maatregel op de uitkering.


## Objecttypen Model Normafwijking


### Afwijkende maatregel
> **Definitie Afwijkende maatregel:** 
>
> Een *afwijkende maatregel* is een maatregel die afwijkt van de standaardregel of wettelijke norm en die op basis van een wettelijke grondslag, beleidsregel of gemotiveerde beslissing in een concreet geval wordt toegepast.

??? info "Kenmerken Model Afwijkende maatregel"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Afwijkende maatregel |
    | toelichting | In de bestuursrechtelijke en juridische context duidt een afwijkende maatregel op een \*uitzondering\* van de reguliere toepassing van een wettelijke regeling of standaardprocedure, waarbij een bestuursorgaan in bijzondere gevallen kiest voor een aangepaste aanpak, binnen de grenzen van de wet. Deze afwijking moet objectief worden gemotiveerd en steunen op een wettelijke grondslag of beleidskader, zodat rechtszekerheid en evenredigheid worden gewaarborgd. De term wordt in diverse beleids- en regelgevingsteksten gebruikt om aan te geven dat een maatregel op een specifiek punt anders wordt vormgegeven dan de hoofdregel, bijvoorbeeld bij maatwerk in bijstandsverordeningen of afwijkingsbevoegdheden in bestemmingsplannen. |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | janbr |
    | version | 1.14.0 |
    | created | 2024-03-07 12:33:22 |
    | modified | 2025-12-17 16:12:37 |
    | id | EAID\_1BD0DD3A\_888E\_945B\_4A20\_276CADAE4D4C |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Afwijkende maatregel

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Boete
> **Definitie Boete:** 
>
> Een boete is de uitkomst van een onderzoek naar rechtmatigheid. Dit leidt in principe tot een terug te vorderen bedrag. Er is voor gekozen om dit als aparte klasse te modelleren en niet als typering van een vordering, omdat we dit gegeven ook willen gebruiken bij risicoprofilering. Als de vordering niet (meer) bestaat, zou dit gegeven daarmee niet beschikbaar zijn.Daarnaast kan dit ook helpen bij het vastleggen van een boete van een poging tot fraude (zonder financiele consequenties, waardoor geen vordering is ontstaan. (tijdig ondekte valsheid in geschifte e.d.).Bij bedragen hoger dan 50.000 euro, wordt aangifte van fraude gedaan en volgt strafrechtelijk onderzoek.Feitelijk is het uitgangspunt bij het opleggen van een boete dat er altijd sprake is van opzet. Daarom is een apart gegeven Fraude niet opgenomen.

??? info "Kenmerken Model Boete"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Boete |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | janbr |
    | version | 1.14.0 |
    | created | 2024-03-07 12:33:22 |
    | modified | 2025-12-17 16:12:37 |
    | id | EAID\_05E49616\_803F\_4C1B\_9663\_262C4A191DF9 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Boete

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Maatregel
> **Definitie Maatregel:** 
>
> Een *maatregel* is een besluit of handeling waarmee een bestuursorgaan of rechter ingrijpt om een doel te bereiken, een probleem op te lossen of een regel te handhaven.

??? info "Kenmerken Model Maatregel"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Maatregel |
    | toelichting | In (bestuurs)recht en beleid duidt \*maatregel\* op een actie, handeling of besluit van een overheid of instantie dat gericht is op het beïnvloeden van gedrag, de toepassing van regels of de situatie van betrokkenen. Dit kan variëren van een administratieve beslissing in een individuele zaak tot een ingreep die een persoon, organisatie of situatie raakt. Een maatregel kan ook in een strafrechtelijke context worden opgelegd ter bescherming van de maatschappij, zoals een maatregel in plaats van of naast een straf. |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | janbr |
    | version | 1.14.0 |
    | created | 2024-03-07 12:33:22 |
    | modified | 2025-12-17 16:12:37 |
    | id | EAID\_0B63B508\_9F69\_A5D7\_4387\_2632D2C24782 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Maatregel

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Maatregel op uitkering
> **Definitie Maatregel op uitkering:** 
>
> Een *maatregel op uitkering* is een sanctie van een uitvoerend orgaan (zoals een gemeente) waarbij de hoogte van een uitkering tijdelijk wordt verlaagd of aangepast omdat de uitkeringsgerechtigde niet heeft voldaan aan de aan de uitkering verbonden verplichtingen.

??? info "Kenmerken Model Maatregel op uitkering"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Maatregel op uitkering |
    | toelichting | In het kader van bijstandsuitkeringen (Participatiewet/Wet werk en bijstand) kan een maatregel worden toegepast als iemand bijvoorbeeld niet of onvoldoende meewerkt aan verplichtingen zoals het zoeken naar werk of het voldoen aan informatieverplichtingen. De maatregel bestaat doorgaans uit een \*\*verlaging van de uitkering met een bepaald percentage voor één of meerdere maanden\*\*, afgestemd op de ernst van de gedraging en de mate van verwijtbaarheid. Gemeenten leggen deze maatregelen vast in een maatregelenverordening. |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | janbr |
    | version | 1.14.0 |
    | created | 2024-03-07 12:33:22 |
    | modified | 2025-12-17 16:12:37 |
    | id | EAID\_032C6459\_3922\_4AEF\_0D73\_262C4A138E25 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Maatregel op uitkering

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Normafwijking
> **Definitie Normafwijking:** 
>
> Een *normafwijking* (in het kader van bijstand) is het constateren dat een bijstandsgerechtigde **afwijkt van de normatieve verplichtingen** die verbonden zijn aan het recht op bijstand (bijv. arbeids- of inlichtingenplicht), wat aanleiding kan geven tot toepassing van een maatregel op de uitkering.

??? info "Kenmerken Model Normafwijking"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Normafwijking |
    | toelichting | In de uitvoering van de Participatiewet moet een bijstandsgerechtigde voldoen aan verschillende normen en verplichtingen (zoals het zoeken naar werk, voldoen aan inlichtingen- en medewerkingsplichten, of andere door de gemeente opgelegde verplichtingen). Wanneer deze verplichtingen niet of onvoldoende worden nagekomen, kan dit worden aangemerkt als een normafwijking die leidt tot \*\*sanctionering via maatregelen op de uitkering\*\* (zoals verlaging van de bijstandsuitkering). Maatregelen worden in gemeentelijke maatregelenverordeningen vastgelegd en zijn verbonden aan de wettelijke kaders van de Participatiewet. |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | janbr |
    | version | 1.14.0 |
    | created | 2024-03-07 12:33:22 |
    | modified | 2025-12-17 16:12:37 |
    | id | EAID\_167FF4C9\_6B66\_EEDA\_5189\_262C4A139258 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Normafwijking

| Attribute | Datatype | Description |
| :--- | :--- | :--- |




