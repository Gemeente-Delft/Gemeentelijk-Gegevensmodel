# Model Terug- en invordering
## Inleiding
> **Definitie Model Terug- en invordering:** 
>
> Het onderdeel Terug- en Invordering richt zich op de processen en gegevens rondom het terugvorderen en invorderen van onterecht verstrekte inkomensvoorzieningen. Dit model biedt een gestructureerde weergave van de objecttypen en hun onderlinge relaties die nodig zijn om deze financiële processen effectief te beheren.

??? info "Kenmerken Model Model Terug- en invordering"

    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | Model Terug- en invordering |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | janbr |
    | version | 1.1 |
    | created | 2024-06-27 21:51:28 |
    | modified | 2025-03-27 15:34:24 |
    | id | EAPK\_2D0F3F05\_1407\_C3BE\_D193\_374C10D6B694 |
    

Het model 'Model Terug- en invordering' kent de volgende objecttypen:

* **Aflossing**: Een aflossing is de betaling van een afgesproken of opgelegd bedrag op een vordering. Een aflos-sing gebeurt in het kader van een aflossingsafspraak gemaakt bij een vordering of wordt eenzijdig opgelegd. De aflossing wordt geadministreerd als een vorderingscomponent onder die vordering. Afgesproken is minnelijk maar kan ook opgelegd worden, bijv 5% verrekening of beslag op loon.
* **Aflossingsafspraak**: Een aflossingsafspraak is een onderdeel van het aflossingsplan. Het is een afspraak over hoe en wanneer het opgelegde bedrag wordt afgelost. Het opgelegde bedrag is het bedrag is de hele vordering of het bdrag na verrekening of beslag.Elke afspraak in het aflossingsplan bepaalt welk bedrag afgelost wordt op welke vordering vanaf een zekere startdatum per tijdseenheid (doorgaans een maand).
* **Aflossingsplan**: Een aflossingsplan bevat alle afspraken tussen de gemeente en de debiteur over op welke vordering hij/zij per wanneer welk bedrag aflost.Verder geldt dat er bijzondere afspraken kunnen worden vastgelegd, bijvoorbeeld Dwangbevel. In zulke gevallen wordt de gehele schuld in één keer weer opeisbaar gesteld.
* **Afschrijving**: De vordering blijkt oninbaar. Er is (nog) geen aflossingsmogelijkheid. Er wordt ook niet geacht dat er perspectief is tot invordering. Er wordt afscheid genomen van de vordering.Afscheid nemen van de vordering gebeurt via het afschrijven van de vordering. De reden daarvan wordt opgegeven.
* **Betaalcomponent**: Een rechtmaand kan door de tijd heen door correcties meerdere betaalcomponenten krijgen. Met de betaalcomponent leg je vast welk bedrag op welke boekingsdatum is betaald in het kader van de rechtmaand.Deze administratie is noodzakelijk omdat moet kunnen worden bepaald welk deel in de terugvordering bruto en welke netto moet worden teruggevorderd.
* **Boetevordering**: Een vordering is een eis op een persoon, zeg debiteur, die een zeker bedrag terug moet betalen aan de gemeente. Vorderingen die zijn ingesteld omdat er een boete vanwege een overtreding van de inlichtingenplicht is opgelegd.  De oorzaak van een vordering is velerlei, Zie daarvoor de categorie-indeling.Vorderingen kunnen uit meerdere componenten bestaan.Vorderingen kunnen ook onderling in relatie staan, bijvoorbeeld: Een opgelegde boete wegens het schenden van de inlichtingenplicht heeft een relatie met een verwijtbare vordering.Deze type vordering zijn als verbijzonderingen opgenomen, opdat deze relaties expliciet kunnen worden gelegd.
* **Conservatoir beslag**: In het Nederlands recht is een conservatoir beslag een beslaglegging op (een deel van) het vermogen van een schuldenaar ter verzekering van de betaling van een onbetaald gebleven vordering nog voordat de rechter uitspraak heeft gedaan over de juistheid van die vordering. De toestemming tot het leggen van dit beslag moet door een advocaat namens de schuldeiser aan de beslagrechter, ook wel "voorzieningenrechter", worden gevraagd. Door het leggen van het beslag ontstaat meer zekerheid dat het beslagen vermogen ter beschikking staat. De voorzieningenrechter is in Nederland over het algemeen snel geneigd toestemming voor het beslag te verlenen en dat zelfs zonder dat de schuldenaar van het verzoek op de hoogte is of daarover wordt gehoord.
* **Correctie**: Na nader inzicht corrigeren van het te vorderen bedrag met een zeker bedrag. Correcties worden geadministreerd onder de vordering.
* **Debiteur**: Binnen het domein van terug- en invorderen is een debiteur een persoon waarop de gemeente een of meerdere vorderingen heeft.
* **Incassokostenvordering**: AlgemeenEen vordering is een eis op een persoon, zeg debiteur, die een zeker bedrag terug moet betalen aan de gemeente.De oorzaak van een vordering is velerlei, Zie daarvoor de categorie-indeling.Vorderingen kunnen uit meerdere componenten bestaan.Vorderingen kunnen ook onderling in relatie staan, bijvoorbeeld: Een opgelegde boete wegens het schenden van de inlichtingenplicht heeft een relatie met een verwijtbare vordering.IncassokostenvorderingBij het invorderproces kunnen incassokosten ontstaan bij een bepaalde vordering. Bij incassokosten boven een drempel (instelbare referentiewaarde) kan een incassokostenvordering worden opgevoerd. De incassokostenvordering wordt gerelateerd aan de hoofdvordering. De incassokostenvordering is een zogenaamde accessoire vordering, die zijn titel ontleend aan de hoofdvordering.Dit type vordering is als verbijzondering opgenomen, opdat deze relatie expliciet kan worden gelegd.
* **Interventie**: De daadwerkelijke interventie, die wordt ondernomen naar aanleiding van een interventieverzoek.
* **Interventieverzoek**: In het geval van monitoring op aflossingsafspraken bij een vordering kan bij ongeregeldheden, zoals het achterwege blijven van aflossingen, een signaal worden gegeven om te interveneren. Dit gebeurt door een interventieverzoek. Interventies geschieden volgens een interventieladder. Altijd kan een medewerker daar gemotiveerd van afwijken, bijvoorbeeld na klantcontact. Dit betekent niet dat het interventieverzoek niet minder dwingend is.
* **Invorderingsbasis**: Een invordering is het innen van een schuld of een te veel uitbetaalde uitkeringssom, soms als gevolg van uitkeringsfraude. In de terugvorderingszaak wordt de vordering vastgesteld en beslist. In de invorderingszaak wordt die schuld vervolgens van de debiteur geïnd. Na betaling vervalt de vordering. Bij niet-betaling kan de vordering ook tenietgaan in de volgende situaties:bij verjaring (de verjaringstermijn werd niet op tijd gestuit)bij kwijtscheldingbij verrekeningbij overlijdenIndien geen verhaalsmogelijkheden aanwezig zijn en binnen afzienbare tijd niet te verwachten zijn, wordt de vordering oninbaar geleden. Dit betekent echter niet dat de vordering teniet gaat. Als nadat de vordering oninbaar is geleden verhaalsmogelijkheden bekend worden, kan daarop gewoon verhaal worden gehaald.Indien geen verhaalsmogelijkheden aanwezig en binnen afzienbare tijd niet te verwachten zijn, wordt de vordering oninbaar geleden. Dit betekent echter niet dat de vordering teniet gaat. Als nadat de vordering oninbaar is geleden verhaalsmogelijkheden bekend worden, kan daarop gewoon verhaal worden gehaald.Teruggaven blijven verrekend worden met oninbaar geleden vorderingen, zolang deze nog niet verjaard zijn.Basis voor het invorderen vormen drie grootheden:de invorderingsmogelijkheidde beslagvrije voetde aflossingscapacteit.In de tijd kunnen deze basisvariabelen wijzigen. Per wijziging worden deze basisvariabelen geadministreerd.De invorderingsbasis vormt dus de basis voor invorderen en derhalve voor het maken van de aflossingsafspraken in het aflossingsplan.Omdat de drie hiervoor genoemde grootheden debiteurafhankelijk zijn, is de invorderingsbasis direct gekoppeld aan de debiteur.Let op!Van de invorderingsbasis wordt alleen de actuele situatie geadministreerd. Historie kan worden vastgehouden in de zaak.
* **Krediethypotheek**: AlgemeenAls de bijstandsuitkering aan u geleend wordt, kan de gemeente u verplichten een hypotheek op de woning te vestigen. Dit wordt een krediethypotheek genoemd. Gemeenten doen dit om zekerheid te hebben dat de lening in de toekomst wordt afgelost. Bent u eigenaar van een woonwagen of een niet-geregistreerd woonschip? Dan kan de gemeente u verplichten een pandrecht te vestigen. Als de hypotheek of het pandrecht is gevestigd, kunt u gewoon in uw woning blijven wonen.De gemeente kan zelf bepalen of en wanneer zij overgaat tot het vestigen van pandrecht of hypotheek op uw huis, woonschip of woonwagen.Gevolgen krediethypotheekDoor het vestigen van een krediethypotheek gebruikt u de overwaarde van uw woning als onderpand voor uw leenbijstand. Onderpand wil zeggen dat de gemeente uw woning mag verkopen als u uw betalingsverplichtingen niet nakomt. Als u uw rente- en aflossingsverplichtingen niet nakomt, dan kan de gemeente uw woning verkopen en van de opbrengst uw rente– en aflossingsverplichtingen betalen. Als u zelf besluit om uw woning te verkopen, dan moet u (een deel van) de opbrengst gebruiken om uw leenbijstand af te lossen.Kosten krediethypotheekVoor de kosten die u eventueel maakt in verband met de taxatie van de woning en het vestigen van een krediethypotheek kunt u bijzondere bijstand ontvangen. U moet dan wel aan de voorwaarden voor het recht op bijzondere bijstand voldoen.Aflossing leningHieronder worden de situaties beschreven wanneer de lening moet worden afgelost.U stroomt uit de bijstand omdat u werk heeft gevonden. Als u uit de bijstand stroomt omdat u werk heeft gevonden moet u in principe de lening gaan aflossen. Wanneer dat het geval is, is afhankelijk van het gemeentelijke beleid.U moet opnieuw bijstand aanvragen. Is uw bijstand in de vorm van een geldlening geëindigd, maar doet u binnen een bepaalde periode opnieuw een beroep op bijstand? Dan kunt u mogelijk opnieuw bijstand in de vorm van een geldlening ontvangen. Informeer bij de gemeente.U verkoopt de woning. Verkoopt u de woning? Dan moet de lening meestal worden terugbetaald, mits de verkoop voldoende heeft opgebracht.U overlijdt. Als u overlijdt valt de woning in uw nalatenschap. Uw erfgenamen zullen de geldlening dan moeten terugbetalen uit de nalatenschap. De gemeente zal hierover met de erven corresponderen.OverzichtKrediethypotheek leidt dus niet meteen tot een vordering. Toch wordt een krediethypotheek gemeld aan Terug- en Invorderen. Met deze informatie kan beter maatwerk worden geleverd bij het bepalen van de aflossingsafspraken. Hetzelfde geldt voor de leenbijstand.
* **Krediethypotheekvordering**: AlgemeenEen vordering is een eis op een persoon, zeg debiteur, die een zeker bedrag terug moet betalen aan de gemeente.De oorzaak van een vordering is velerlei, Zie daarvoor de categorie-indeling.Vorderingen kunnen uit meerdere componenten bestaan.Relaties tussen vorderingenVorderingen kunnen ook onderling in relatie staan, bijvoorbeeld:Een opgelegde boete wegens het schenden van de inlichtingenplicht heeft een relatie met een verwijtbare vorderingIncassokostenvordering voor als er in het kader van een vordering incassokosten zijn gemaakt, die verhaald worden.Rentevordering als bij leningen of kredieten rente in rekening wordt gebracht.Al deze vorderingen zijn zelfstandige vorderingen gerelateerd aan de originele vordering. Zij verkrijgen automatisch dezelfde titel als de originele vordering.InterventieladderBij een terugvordering vanwege het aflossen op een krediethypotheek moet in de interventieladder na een aanmaning een grosse gehaald worden bij de rechter. Vervolgens kan pas doorgeescaleerd worden naar dwangbevel.
* **Kwijtschelding**: Het kwijtschelden van het restant van de vordering.RedenenDit kan om diverse redenen gebeuren, waaronder redenen uit het beleid.Als een debiteur zijn 36 maanden lang houdt aan de betaalafspraken, dan komt de debiteur in aanmerking voor kwijtschelding. Enkele noties hierbij:Het gaat hier om het houden van de afspraken.Hieronder vallen ook afspraken om tijdelijk niet af te lossen.In principe zal een enkele maand opschorten vanwege een maand niet betalen niet de betaaldiscipline verbreken, omdat de gemeente niet heeft ingegrepen via een interventie.Als de debiteur ineens de helft of meer aflost op de vordering.BedragHet bedrag in de kwijtschelding heeft die hoogte dat de totale restant van de vordering op nul komt.
* **Leenbijstand**: AlgemeenLeenbijstand is een lening aan de burger, die in termijnen moet worden terugbetaald.TerugbetalingAflossingen op leningen bedragen standaard 5% van de toepasselijke maandnorm inclusief vakantietoeslag (VT);De lening wordt in maximaal 36 termijnen terugbetaald. Het restant wordt afgeschreven. De gemeente vordert terug als iemand zich niet aan de verplichtingen van de leenovereenkomst houdt.Leenbijstand worden gemeld aan Terug- en Invorderen voor een 360-graden view op de debiteur. Dan kan hiermee rekening worden gehouden bij het maken van aflossingsafspraken.Leenbijstand wordt verrekend met de uitkering en zal in dergelijke gevallen niet leiden tot terugvorderenPas als de persoon uit de bijstand gaat, zal het voorliggende proces een terugvorderingsverzoek doen bij Terug- en Invorderen.De totaal gegeven leenbijstand wordt teruggevorderd. Hier is een CBS-categorie voor.Mogelijke gevallen (illustratief)Leenbijstand (in de vorm van Bijzondere Bijstand) is onder andere mogelijk in de volgende situaties:U moet een waarborgsom betalen bij het huren van een huis;U wacht op geld waarvan u kunt leven. Het is bijvoorbeeld mogelijk dat u lange tijd moet wachten op de uitbetaling van een erfenis;U moet door eigen toedoen bijstand aanvragen of eerder aanvragen dan nodig was;U hebt een koophuis, u hebt (redelijk) veel eigen vermogen in het huis zitten en geen of weinig inkomsten;U bent zelfstandige of u bent net gestart met uw eigen bedrijf of beroep.NB: U moet een lening altijd weer terugbetalen.
* **Leenbijstandvordering**: AlgemeenLeenbijstand is een lening aan de burger, die in termijnen moet worden terugbetaald. Zie: Leenbijstand.TerugbetalingAflossingen op leningen bedragen standaard 5% van de toepasselijke maandnorm inclusief vakantietoeslag (VT);De lening wordt in maximaal 36 termijnen terugbetaald. Het restant wordt afgeschreven. De gemeente vordert terug als iemand zich niet aan de verplichtingen van de leenovereenkomst houdt.Leenbijstand wordt verrekend met de uitkering en zal in dergelijke gevallen niet leiden tot terugvorderenPas als de persoon uit de bijstand gaat, zal het voorliggende proces een terugvorderingsverzoek doen bij Terug- en Invorderen.De totaal gegeven leenbijstand wordt teruggevorderd. Hier is een CBS-categorie voor.
* **Loonbeslagafspraak**: Een loonbeslagafspraak is een aflossingsafspraak.Tevens is het een afspraak tussen twee partijen (organisaties) om voor het aflossen van vorderingen. Hierbij zal de ene partij - de werkgever van de debiteur - een afgesproken bedrag in houden op het loon van de debiteur en het ingehouden bedrag overmaken naar crediteur.Aangezien Loonbeslag een Inkomstencomponent is (zie het inkomstenmodel) ligt er een impliciete relatie tussen de Loonbeslagafspraak en het Loonbeslag.
* **Rechtmaand**: Een vordering in het kader van de bijvoorbeeld de bijstand kan over meerdere kalendermaanden betreffen. In die maanden had de debiteur recht op die bijstand. Zo'n maand onder die vordering noemt men een rechtmaand.Rechtmaanden worden geadministreerd onder een vorderingscomponent bij de vordering. Als de vordering meerdere rechtmaanden bevat die of niet opvolgend zijn of een jaargrens passeren, dan worden die rechtmaanden opgesplitst in reeksen van opvolgende rechtmaanden binnen een jaar. Elke opsplitsing vormt dan een vorderingscomponent.
* **Rentevordering**: AlgemeenEen vordering is een eis op een persoon, zeg debiteur, die een zeker bedrag terug moet betalen aan de gemeente.De oorzaak van een vordering is velerlei, Zie daarvoor de categorie-indeling.Vorderingen kunnen uit meerdere componenten bestaan.Vorderingen kunnen ook onderling in relatie staan, bijvoorbeeld: Een opgelegde boete wegens het schenden van de inlichtingenplicht heeft een relatie met een verwijtbare vordering.RentevorderingBepaalde vorderingen zijn rentedragend. De rente wordt niet als aparte component opgevoerd bij de hoofdvordering, maar als een aparte vordering. De rentevordering wordt gerelateerd aan de hoofdvordering. De rentevordering is een zogenaamde accessoire vordering, die zijn titel ontleend aan de hoofdvordering.Dit type vordering is als verbijzondering opgenomen, opdat deze relatie expliciet kan worden gelegd.
* **Restitutie**: Restitutie is terugbetaling van te veel ontvangen aflossing. Restituties worden geadministreerd onder de vordering.
* **Terugvorderingsverzoek**: Het vorderingsverzoek is de handshake tussen een voorliggend proces en de bedrijfsfunctie Terug- en Invorderen. In het kader van een bepaalde regeling is geconstateerd dat een zeker bedrag terug moet worden gevorderd. Dit wordt her gemakshalve het voorliggende proces genoemd. Het voorliggende proces moet de juiste, noodzakelijke en voldoende gegevens toeleveren aan Terug- en invorderen opdat het verzoek tot terugvorderen in behandeling kan worden genomen.Het vorderingsverzoek start een terugvorderingszaak. Op basis van de voortgang van die zaak kan het verzoekende voorliggende proces op de hoogte worden gehouden van de voortgang via zaakstatusinformatie.
* **Uitstel aflossing**: Er kunnen redenen zijn om het aflossingsplan te pauseren. Zie de opties bij het attribuut Reden uitstel.Het volgende geldt:Uitstel van aflossing grijpt aan op alle afspraken in het aflossingsplan.Uitstel leidt tot termijnbewaking om de medewerker er op te attenderen of het uitstel nog aan de orde zou moeten zijn.De termijn in de termijnbewaking kan verschillen per reden van uitstel.
* **Vermindering terugvordering**: Vermindering terugvordering is het resultaat van een beslissing de terugvordering te verminderen met een zeker bedrag met zekere motivatie. De vermindering terugvordering wordt geadministreerd onder de vordering.
* **Verrekening**: Bij het vaststellen van de vordering wordt gekeken of de debiteur een uitkering geniet. Er zijn twee soorten situaties van verrekening. inkomstenverrekening waar de inkomsten 6 maanden wordt verrekend met de bijstandsuitkeringverrekening alias inhouding op een uitkering (een soort van loonbeslag) / verrekening in de zin van art. 60 lid 3 en 4 PW.Hier wordt de laatste bedoeld.Verrekening op grond van artikel 60 lid 3 en 4 Participatiewet door de gemeente gaat vóór beslag door een derde (artikel 60 lid 7 Participatiewet). Voor de praktijk betekent dit dat:Een lopend beslag wordt opgeschort zodra de gemeente (op grond van hun invorderingsbevoegdheid) een bedrag gaat verrekenen met de bijstandsuitkering. De beslaglegger wordt van de opschorting op de hoogte gesteld.De verrekening ongewijzigd wordt voortgezet indien nadien beslag door een derde wordt gelegd. De beslaglegger wordt medegedeeld dat het beslag niet uitvoerbaar is in verband met verrekening.Voorwaarde voor verrekening op grond van artikel 60 lid 3 en 4 Participatiewet is dat er een terugvorderingsbesluit of boetebesluit is genomen. Bij verstrekking van bijstand in de vorm van een geldlening kunnen echter de vastgestelde aflossingsbedragen direct worden verrekend op grond van artikel 48 lid 4 Participatiewet. Een terugvorderingsbesluit ingevolge artikel 58 lid 2 onderdeel b Participatiewet is dan dus niet noodzakelijk.Pseudo-verrekening gaat niet voor beslag.Pseudo-verrekening zoals bedoeld in artikel 60a Participatiewet gaat niet voor beslag door een derde onder een andere gemeente (of onder het Uitvoeringsinstituut werknemersverzekeringen of de Sociale verzekeringsbank).Een verrekening is verder te behandelen als een vordering, maar juridisch een ander ding.
* **Verwijtbare vordering**: Een vordering is een eis op een persoon, zeg debiteur, die een zeker bedrag terug moet betalen aan de gemeente. Het zijn vorderingen die zijn ingesteld vanwege het niet nakomen van de inlichtingen-plicht waardoor de uitkerende instantie ten onrechte heeft uitbetaald . De oorzaak van een vordering is velerlei, Zie daarvoor de categorie-indeling.Vorderingen kunnen uit meerdere componenten bestaan.Vorderingen kunnen ook onderling in relatie staan, bijvoorbeeld: Een opgelegde boete wegens het schenden van de inlichtingenplicht heeft een relatie met een verwijtbare vordering.Deze type vordering zijn als verbijzonderingen opgenomen, opdat deze relaties expliciet kunnen worden gelegd.
* **Vordering**: Een vordering is een eis op een persoon, zeg debiteur, die een zeker bedrag (terug) moet betalen aan de gemeente in het kader van de bijstand of een bijstandsgerelateerde uitkering.De oorzaak van een vordering is velerlei, Zie daarvoor de categorie-indeling.Vorderingen kunnen uit meerdere componenten bestaan.Vorderingen kunnen ook onderling in relatie staan, bijvoorbeeld: Een opgelegde boete wegens het schenden van de inlichtingenplicht heeft een relatie met een verwijtbare vordering.Deze type vordering zijn als verbijzonderingen opgenomen, opdat deze relaties expliciet kunnen worden vastgelegd.
* **Vorderingscomponent**: Vorderingen, die bestaan uit verschillende rechtmaanden, worden gesplitst in vorderingscomponenten alsde rechtmaanden niet aansluitend zijn ofals er tussen opvolgende rechtmaanden een jaarovergang zit.De een opeenvolgende reeks van rechtmaanden binnen een jaar wordt gekoppeld aan de vorderingscomponent. Dit gebeurt tijdens het vaststellen van de terugvordering.


## Objecttypen Model Terug- en invordering


### Aflossing
> **Definitie Aflossing:** 
>
> Een aflossing is de betaling van een afgesproken of opgelegd bedrag op een vordering. Een aflos-sing gebeurt in het kader van een aflossingsafspraak gemaakt bij een vordering of wordt eenzijdig opgelegd. De aflossing wordt geadministreerd als een vorderingscomponent onder die vordering. Afgesproken is minnelijk maar kan ook opgelegd worden, bijv 5% verrekening of beslag op loon.

??? info "Kenmerken Model Aflossing"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Aflossing |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | janbr |
    | version | 1.10.0 |
    | created | 2024-03-07 12:33:22 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_196161F4\_8372\_6334\_AF08\_263C236F7A38 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Aflossing

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Aflossingsafspraak
> **Definitie Aflossingsafspraak:** 
>
> Een aflossingsafspraak is een onderdeel van het aflossingsplan. Het is een afspraak over hoe en wanneer het opgelegde bedrag wordt afgelost. Het opgelegde bedrag is het bedrag is de hele vordering of het bdrag na verrekening of beslag.Elke afspraak in het aflossingsplan bepaalt welk bedrag afgelost wordt op welke vordering vanaf een zekere startdatum per tijdseenheid (doorgaans een maand).

??? info "Kenmerken Model Aflossingsafspraak"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Aflossingsafspraak |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | janbr |
    | version | 1.10.0 |
    | created | 2024-03-07 12:33:22 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_0F06241B\_EBEF\_4053\_33E4\_263C236F76FC |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Aflossingsafspraak

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Aflossingsplan
> **Definitie Aflossingsplan:** 
>
> Een aflossingsplan bevat alle afspraken tussen de gemeente en de debiteur over op welke vordering hij/zij per wanneer welk bedrag aflost.Verder geldt dat er bijzondere afspraken kunnen worden vastgelegd, bijvoorbeeld Dwangbevel. In zulke gevallen wordt de gehele schuld in één keer weer opeisbaar gesteld.

??? info "Kenmerken Model Aflossingsplan"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Aflossingsplan |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | janbr |
    | version | 1.10.0 |
    | created | 2024-03-07 12:33:22 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_234EB82E\_9EC6\_5904\_2634\_263C0A957ADF |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Aflossingsplan

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Afschrijving
> **Definitie Afschrijving:** 
>
> De vordering blijkt oninbaar. Er is (nog) geen aflossingsmogelijkheid. Er wordt ook niet geacht dat er perspectief is tot invordering. Er wordt afscheid genomen van de vordering.Afscheid nemen van de vordering gebeurt via het afschrijven van de vordering. De reden daarvan wordt opgegeven.

??? info "Kenmerken Model Afschrijving"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Afschrijving |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | janbr |
    | version | 1.10.0 |
    | created | 2024-03-07 12:33:22 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_c0026057\_03ab\_4e5b\_a021\_aa9175c4078c |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Afschrijving

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Betaalcomponent
> **Definitie Betaalcomponent:** 
>
> Een rechtmaand kan door de tijd heen door correcties meerdere betaalcomponenten krijgen. Met de betaalcomponent leg je vast welk bedrag op welke boekingsdatum is betaald in het kader van de rechtmaand.Deze administratie is noodzakelijk omdat moet kunnen worden bepaald welk deel in de terugvordering bruto en welke netto moet worden teruggevorderd.

??? info "Kenmerken Model Betaalcomponent"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Betaalcomponent |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | janbr |
    | version | 1.10.0 |
    | created | 2024-03-07 12:33:22 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_1D10018E\_888E\_945B\_4A20\_293102BE4D4C |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Betaalcomponent

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Boetevordering
> **Definitie Boetevordering:** 
>
> Een vordering is een eis op een persoon, zeg debiteur, die een zeker bedrag terug moet betalen aan de gemeente. Vorderingen die zijn ingesteld omdat er een boete vanwege een overtreding van de inlichtingenplicht is opgelegd.  De oorzaak van een vordering is velerlei, Zie daarvoor de categorie-indeling.Vorderingen kunnen uit meerdere componenten bestaan.Vorderingen kunnen ook onderling in relatie staan, bijvoorbeeld: Een opgelegde boete wegens het schenden van de inlichtingenplicht heeft een relatie met een verwijtbare vordering.Deze type vordering zijn als verbijzonderingen opgenomen, opdat deze relaties expliciet kunnen worden gelegd.

??? info "Kenmerken Model Boetevordering"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Boetevordering |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | janbr |
    | version | 1.10.0 |
    | created | 2024-03-07 12:33:22 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_173D0C11\_3C5E\_8344\_BE5E\_293122950DAC |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Boetevordering

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Conservatoir beslag
> **Definitie Conservatoir beslag:** 
>
> In het Nederlands recht is een conservatoir beslag een beslaglegging op (een deel van) het vermogen van een schuldenaar ter verzekering van de betaling van een onbetaald gebleven vordering nog voordat de rechter uitspraak heeft gedaan over de juistheid van die vordering. De toestemming tot het leggen van dit beslag moet door een advocaat namens de schuldeiser aan de beslagrechter, ook wel "voorzieningenrechter", worden gevraagd. Door het leggen van het beslag ontstaat meer zekerheid dat het beslagen vermogen ter beschikking staat. De voorzieningenrechter is in Nederland over het algemeen snel geneigd toestemming voor het beslag te verlenen en dat zelfs zonder dat de schuldenaar van het verzoek op de hoogte is of daarover wordt gehoord.

??? info "Kenmerken Model Conservatoir beslag"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Conservatoir beslag |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | janbr |
    | version | 1.10.0 |
    | created | 2024-03-07 12:33:22 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_1CE90960\_888E\_945B\_4A20\_28F9C71E4D4C |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Conservatoir beslag

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Correctie
> **Definitie Correctie:** 
>
> Na nader inzicht corrigeren van het te vorderen bedrag met een zeker bedrag. Correcties worden geadministreerd onder de vordering.

??? info "Kenmerken Model Correctie"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Correctie |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | janbr |
    | version | 1.10.0 |
    | created | 2024-03-07 12:33:22 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_1B73F18A\_888E\_945B\_4A20\_26E8FA774D4C |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Correctie

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Debiteur
> **Definitie Debiteur:** 
>
> Binnen het domein van terug- en invorderen is een debiteur een persoon waarop de gemeente een of meerdere vorderingen heeft.

??? info "Kenmerken Model Debiteur"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Debiteur |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | janbr |
    | version | 1.10.0 |
    | created | 2024-03-07 12:33:22 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_107E216A\_17F2\_DFCA\_EAFE\_263C7FFC912E |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Debiteur

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Incassokostenvordering
> **Definitie Incassokostenvordering:** 
>
> AlgemeenEen vordering is een eis op een persoon, zeg debiteur, die een zeker bedrag terug moet betalen aan de gemeente.De oorzaak van een vordering is velerlei, Zie daarvoor de categorie-indeling.Vorderingen kunnen uit meerdere componenten bestaan.Vorderingen kunnen ook onderling in relatie staan, bijvoorbeeld: Een opgelegde boete wegens het schenden van de inlichtingenplicht heeft een relatie met een verwijtbare vordering.IncassokostenvorderingBij het invorderproces kunnen incassokosten ontstaan bij een bepaalde vordering. Bij incassokosten boven een drempel (instelbare referentiewaarde) kan een incassokostenvordering worden opgevoerd. De incassokostenvordering wordt gerelateerd aan de hoofdvordering. De incassokostenvordering is een zogenaamde accessoire vordering, die zijn titel ontleend aan de hoofdvordering.Dit type vordering is als verbijzondering opgenomen, opdat deze relatie expliciet kan worden gelegd.

??? info "Kenmerken Model Incassokostenvordering"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Incassokostenvordering |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | janbr |
    | version | 1.10.0 |
    | created | 2024-03-07 12:33:22 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_a19a36c3\_66e1\_44c2\_b674\_6f3a3d98c5ea |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Incassokostenvordering

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Interventie
> **Definitie Interventie:** 
>
> De daadwerkelijke interventie, die wordt ondernomen naar aanleiding van een interventieverzoek.

??? info "Kenmerken Model Interventie"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Interventie |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | janbr |
    | version | 1.10.0 |
    | created | 2024-03-07 12:33:22 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_1BCE2533\_656D\_D59B\_6ECD\_28FC06D8D601 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Interventie

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Interventieverzoek
> **Definitie Interventieverzoek:** 
>
> In het geval van monitoring op aflossingsafspraken bij een vordering kan bij ongeregeldheden, zoals het achterwege blijven van aflossingen, een signaal worden gegeven om te interveneren. Dit gebeurt door een interventieverzoek. Interventies geschieden volgens een interventieladder. Altijd kan een medewerker daar gemotiveerd van afwijken, bijvoorbeeld na klantcontact. Dit betekent niet dat het interventieverzoek niet minder dwingend is.

??? info "Kenmerken Model Interventieverzoek"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Interventieverzoek |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | janbr |
    | version | 1.10.0 |
    | created | 2024-03-07 12:33:22 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_0897E8F8\_77FF\_DE35\_D40E\_28FC069F6910 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Interventieverzoek

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Invorderingsbasis
> **Definitie Invorderingsbasis:** 
>
> Een invordering is het innen van een schuld of een te veel uitbetaalde uitkeringssom, soms als gevolg van uitkeringsfraude. In de terugvorderingszaak wordt de vordering vastgesteld en beslist. In de invorderingszaak wordt die schuld vervolgens van de debiteur geïnd. Na betaling vervalt de vordering. Bij niet-betaling kan de vordering ook tenietgaan in de volgende situaties:bij verjaring (de verjaringstermijn werd niet op tijd gestuit)bij kwijtscheldingbij verrekeningbij overlijdenIndien geen verhaalsmogelijkheden aanwezig zijn en binnen afzienbare tijd niet te verwachten zijn, wordt de vordering oninbaar geleden. Dit betekent echter niet dat de vordering teniet gaat. Als nadat de vordering oninbaar is geleden verhaalsmogelijkheden bekend worden, kan daarop gewoon verhaal worden gehaald.Indien geen verhaalsmogelijkheden aanwezig en binnen afzienbare tijd niet te verwachten zijn, wordt de vordering oninbaar geleden. Dit betekent echter niet dat de vordering teniet gaat. Als nadat de vordering oninbaar is geleden verhaalsmogelijkheden bekend worden, kan daarop gewoon verhaal worden gehaald.Teruggaven blijven verrekend worden met oninbaar geleden vorderingen, zolang deze nog niet verjaard zijn.Basis voor het invorderen vormen drie grootheden:de invorderingsmogelijkheidde beslagvrije voetde aflossingscapacteit.In de tijd kunnen deze basisvariabelen wijzigen. Per wijziging worden deze basisvariabelen geadministreerd.De invorderingsbasis vormt dus de basis voor invorderen en derhalve voor het maken van de aflossingsafspraken in het aflossingsplan.Omdat de drie hiervoor genoemde grootheden debiteurafhankelijk zijn, is de invorderingsbasis direct gekoppeld aan de debiteur.Let op!Van de invorderingsbasis wordt alleen de actuele situatie geadministreerd. Historie kan worden vastgehouden in de zaak.

??? info "Kenmerken Model Invorderingsbasis"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Invorderingsbasis |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | janbr |
    | version | 1.10.0 |
    | created | 2024-03-07 12:33:22 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_0A9D7FDF\_4271\_2DBE\_58D2\_28F9CE6C00A4 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Invorderingsbasis

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Krediethypotheek
> **Definitie Krediethypotheek:** 
>
> AlgemeenAls de bijstandsuitkering aan u geleend wordt, kan de gemeente u verplichten een hypotheek op de woning te vestigen. Dit wordt een krediethypotheek genoemd. Gemeenten doen dit om zekerheid te hebben dat de lening in de toekomst wordt afgelost. Bent u eigenaar van een woonwagen of een niet-geregistreerd woonschip? Dan kan de gemeente u verplichten een pandrecht te vestigen. Als de hypotheek of het pandrecht is gevestigd, kunt u gewoon in uw woning blijven wonen.De gemeente kan zelf bepalen of en wanneer zij overgaat tot het vestigen van pandrecht of hypotheek op uw huis, woonschip of woonwagen.Gevolgen krediethypotheekDoor het vestigen van een krediethypotheek gebruikt u de overwaarde van uw woning als onderpand voor uw leenbijstand. Onderpand wil zeggen dat de gemeente uw woning mag verkopen als u uw betalingsverplichtingen niet nakomt. Als u uw rente- en aflossingsverplichtingen niet nakomt, dan kan de gemeente uw woning verkopen en van de opbrengst uw rente– en aflossingsverplichtingen betalen. Als u zelf besluit om uw woning te verkopen, dan moet u (een deel van) de opbrengst gebruiken om uw leenbijstand af te lossen.Kosten krediethypotheekVoor de kosten die u eventueel maakt in verband met de taxatie van de woning en het vestigen van een krediethypotheek kunt u bijzondere bijstand ontvangen. U moet dan wel aan de voorwaarden voor het recht op bijzondere bijstand voldoen.Aflossing leningHieronder worden de situaties beschreven wanneer de lening moet worden afgelost.U stroomt uit de bijstand omdat u werk heeft gevonden. Als u uit de bijstand stroomt omdat u werk heeft gevonden moet u in principe de lening gaan aflossen. Wanneer dat het geval is, is afhankelijk van het gemeentelijke beleid.U moet opnieuw bijstand aanvragen. Is uw bijstand in de vorm van een geldlening geëindigd, maar doet u binnen een bepaalde periode opnieuw een beroep op bijstand? Dan kunt u mogelijk opnieuw bijstand in de vorm van een geldlening ontvangen. Informeer bij de gemeente.U verkoopt de woning. Verkoopt u de woning? Dan moet de lening meestal worden terugbetaald, mits de verkoop voldoende heeft opgebracht.U overlijdt. Als u overlijdt valt de woning in uw nalatenschap. Uw erfgenamen zullen de geldlening dan moeten terugbetalen uit de nalatenschap. De gemeente zal hierover met de erven corresponderen.OverzichtKrediethypotheek leidt dus niet meteen tot een vordering. Toch wordt een krediethypotheek gemeld aan Terug- en Invorderen. Met deze informatie kan beter maatwerk worden geleverd bij het bepalen van de aflossingsafspraken. Hetzelfde geldt voor de leenbijstand.

??? info "Kenmerken Model Krediethypotheek"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Krediethypotheek |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | janbr |
    | version | 1.10.0 |
    | created | 2024-03-07 12:33:22 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_d3335b08\_9b4b\_4e55\_b507\_0e1d481f1409 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Krediethypotheek

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Krediethypotheekvordering
> **Definitie Krediethypotheekvordering:** 
>
> AlgemeenEen vordering is een eis op een persoon, zeg debiteur, die een zeker bedrag terug moet betalen aan de gemeente.De oorzaak van een vordering is velerlei, Zie daarvoor de categorie-indeling.Vorderingen kunnen uit meerdere componenten bestaan.Relaties tussen vorderingenVorderingen kunnen ook onderling in relatie staan, bijvoorbeeld:Een opgelegde boete wegens het schenden van de inlichtingenplicht heeft een relatie met een verwijtbare vorderingIncassokostenvordering voor als er in het kader van een vordering incassokosten zijn gemaakt, die verhaald worden.Rentevordering als bij leningen of kredieten rente in rekening wordt gebracht.Al deze vorderingen zijn zelfstandige vorderingen gerelateerd aan de originele vordering. Zij verkrijgen automatisch dezelfde titel als de originele vordering.InterventieladderBij een terugvordering vanwege het aflossen op een krediethypotheek moet in de interventieladder na een aanmaning een grosse gehaald worden bij de rechter. Vervolgens kan pas doorgeescaleerd worden naar dwangbevel.

??? info "Kenmerken Model Krediethypotheekvordering"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Krediethypotheekvordering |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | janbr |
    | version | 1.10.0 |
    | created | 2024-03-07 12:33:22 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_0238113B\_1577\_D45C\_C5E9\_293122B2568D |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Krediethypotheekvordering

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Kwijtschelding
> **Definitie Kwijtschelding:** 
>
> Het kwijtschelden van het restant van de vordering.RedenenDit kan om diverse redenen gebeuren, waaronder redenen uit het beleid.Als een debiteur zijn 36 maanden lang houdt aan de betaalafspraken, dan komt de debiteur in aanmerking voor kwijtschelding. Enkele noties hierbij:Het gaat hier om het houden van de afspraken.Hieronder vallen ook afspraken om tijdelijk niet af te lossen.In principe zal een enkele maand opschorten vanwege een maand niet betalen niet de betaaldiscipline verbreken, omdat de gemeente niet heeft ingegrepen via een interventie.Als de debiteur ineens de helft of meer aflost op de vordering.BedragHet bedrag in de kwijtschelding heeft die hoogte dat de totale restant van de vordering op nul komt.

??? info "Kenmerken Model Kwijtschelding"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Kwijtschelding |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | janbr |
    | version | 1.10.0 |
    | created | 2024-03-07 12:33:22 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_1127D07A\_473D\_2912\_29AE\_2ABDF0E8A586 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Kwijtschelding

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Leenbijstand
> **Definitie Leenbijstand:** 
>
> AlgemeenLeenbijstand is een lening aan de burger, die in termijnen moet worden terugbetaald.TerugbetalingAflossingen op leningen bedragen standaard 5% van de toepasselijke maandnorm inclusief vakantietoeslag (VT);De lening wordt in maximaal 36 termijnen terugbetaald. Het restant wordt afgeschreven. De gemeente vordert terug als iemand zich niet aan de verplichtingen van de leenovereenkomst houdt.Leenbijstand worden gemeld aan Terug- en Invorderen voor een 360-graden view op de debiteur. Dan kan hiermee rekening worden gehouden bij het maken van aflossingsafspraken.Leenbijstand wordt verrekend met de uitkering en zal in dergelijke gevallen niet leiden tot terugvorderenPas als de persoon uit de bijstand gaat, zal het voorliggende proces een terugvorderingsverzoek doen bij Terug- en Invorderen.De totaal gegeven leenbijstand wordt teruggevorderd. Hier is een CBS-categorie voor.Mogelijke gevallen (illustratief)Leenbijstand (in de vorm van Bijzondere Bijstand) is onder andere mogelijk in de volgende situaties:U moet een waarborgsom betalen bij het huren van een huis;U wacht op geld waarvan u kunt leven. Het is bijvoorbeeld mogelijk dat u lange tijd moet wachten op de uitbetaling van een erfenis;U moet door eigen toedoen bijstand aanvragen of eerder aanvragen dan nodig was;U hebt een koophuis, u hebt (redelijk) veel eigen vermogen in het huis zitten en geen of weinig inkomsten;U bent zelfstandige of u bent net gestart met uw eigen bedrijf of beroep.NB: U moet een lening altijd weer terugbetalen.

??? info "Kenmerken Model Leenbijstand"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Leenbijstand |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | janbr |
    | version | 1.10.0 |
    | created | 2024-03-07 12:33:22 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_18090A2C\_CED1\_0A51\_0DFD\_294370D99076 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Leenbijstand

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Leenbijstandvordering
> **Definitie Leenbijstandvordering:** 
>
> AlgemeenLeenbijstand is een lening aan de burger, die in termijnen moet worden terugbetaald. Zie: Leenbijstand.TerugbetalingAflossingen op leningen bedragen standaard 5% van de toepasselijke maandnorm inclusief vakantietoeslag (VT);De lening wordt in maximaal 36 termijnen terugbetaald. Het restant wordt afgeschreven. De gemeente vordert terug als iemand zich niet aan de verplichtingen van de leenovereenkomst houdt.Leenbijstand wordt verrekend met de uitkering en zal in dergelijke gevallen niet leiden tot terugvorderenPas als de persoon uit de bijstand gaat, zal het voorliggende proces een terugvorderingsverzoek doen bij Terug- en Invorderen.De totaal gegeven leenbijstand wordt teruggevorderd. Hier is een CBS-categorie voor.

??? info "Kenmerken Model Leenbijstandvordering"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Leenbijstandvordering |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | janbr |
    | version | 1.10.0 |
    | created | 2024-03-07 12:33:22 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_ed7f7a0f\_bef9\_4532\_94ad\_f36418629141 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Leenbijstandvordering

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Loonbeslagafspraak
> **Definitie Loonbeslagafspraak:** 
>
> Een loonbeslagafspraak is een aflossingsafspraak.Tevens is het een afspraak tussen twee partijen (organisaties) om voor het aflossen van vorderingen. Hierbij zal de ene partij - de werkgever van de debiteur - een afgesproken bedrag in houden op het loon van de debiteur en het ingehouden bedrag overmaken naar crediteur.Aangezien Loonbeslag een Inkomstencomponent is (zie het inkomstenmodel) ligt er een impliciete relatie tussen de Loonbeslagafspraak en het Loonbeslag.

??? info "Kenmerken Model Loonbeslagafspraak"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Loonbeslagafspraak |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | janbr |
    | version | 1.10.0 |
    | created | 2024-03-07 12:33:22 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_1a6b9a31\_c4c7\_4b46\_92ef\_0dd7e31613ed |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Loonbeslagafspraak

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Rechtmaand
> **Definitie Rechtmaand:** 
>
> Een vordering in het kader van de bijvoorbeeld de bijstand kan over meerdere kalendermaanden betreffen. In die maanden had de debiteur recht op die bijstand. Zo'n maand onder die vordering noemt men een rechtmaand.Rechtmaanden worden geadministreerd onder een vorderingscomponent bij de vordering. Als de vordering meerdere rechtmaanden bevat die of niet opvolgend zijn of een jaargrens passeren, dan worden die rechtmaanden opgesplitst in reeksen van opvolgende rechtmaanden binnen een jaar. Elke opsplitsing vormt dan een vorderingscomponent.

??? info "Kenmerken Model Rechtmaand"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Rechtmaand |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | janbr |
    | version | 1.10.0 |
    | created | 2024-03-07 12:33:22 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_0DF4970C\_7D69\_27D9\_7976\_263C0A6C41DC |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Rechtmaand

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Rentevordering
> **Definitie Rentevordering:** 
>
> AlgemeenEen vordering is een eis op een persoon, zeg debiteur, die een zeker bedrag terug moet betalen aan de gemeente.De oorzaak van een vordering is velerlei, Zie daarvoor de categorie-indeling.Vorderingen kunnen uit meerdere componenten bestaan.Vorderingen kunnen ook onderling in relatie staan, bijvoorbeeld: Een opgelegde boete wegens het schenden van de inlichtingenplicht heeft een relatie met een verwijtbare vordering.RentevorderingBepaalde vorderingen zijn rentedragend. De rente wordt niet als aparte component opgevoerd bij de hoofdvordering, maar als een aparte vordering. De rentevordering wordt gerelateerd aan de hoofdvordering. De rentevordering is een zogenaamde accessoire vordering, die zijn titel ontleend aan de hoofdvordering.Dit type vordering is als verbijzondering opgenomen, opdat deze relatie expliciet kan worden gelegd.

??? info "Kenmerken Model Rentevordering"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Rentevordering |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | janbr |
    | version | 1.10.0 |
    | created | 2024-03-07 12:33:22 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_170B4422\_37F6\_8893\_2627\_293122D74F28 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Rentevordering

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Restitutie
> **Definitie Restitutie:** 
>
> Restitutie is terugbetaling van te veel ontvangen aflossing. Restituties worden geadministreerd onder de vordering.

??? info "Kenmerken Model Restitutie"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Restitutie |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | janbr |
    | version | 1.10.0 |
    | created | 2024-03-07 12:33:22 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_167B47ED\_CED1\_0A51\_0DFD\_2698932A9076 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Restitutie

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Terugvorderingsverzoek
> **Definitie Terugvorderingsverzoek:** 
>
> Het vorderingsverzoek is de handshake tussen een voorliggend proces en de bedrijfsfunctie Terug- en Invorderen. In het kader van een bepaalde regeling is geconstateerd dat een zeker bedrag terug moet worden gevorderd. Dit wordt her gemakshalve het voorliggende proces genoemd. Het voorliggende proces moet de juiste, noodzakelijke en voldoende gegevens toeleveren aan Terug- en invorderen opdat het verzoek tot terugvorderen in behandeling kan worden genomen.Het vorderingsverzoek start een terugvorderingszaak. Op basis van de voortgang van die zaak kan het verzoekende voorliggende proces op de hoogte worden gehouden van de voortgang via zaakstatusinformatie.

??? info "Kenmerken Model Terugvorderingsverzoek"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Terugvorderingsverzoek |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | janbr |
    | version | 1.10.0 |
    | created | 2024-03-07 12:33:22 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_101157F7\_7852\_102E\_7547\_2698B55B6FF8 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Terugvorderingsverzoek

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Uitstel aflossing
> **Definitie Uitstel aflossing:** 
>
> Er kunnen redenen zijn om het aflossingsplan te pauseren. Zie de opties bij het attribuut Reden uitstel.Het volgende geldt:Uitstel van aflossing grijpt aan op alle afspraken in het aflossingsplan.Uitstel leidt tot termijnbewaking om de medewerker er op te attenderen of het uitstel nog aan de orde zou moeten zijn.De termijn in de termijnbewaking kan verschillen per reden van uitstel.

??? info "Kenmerken Model Uitstel aflossing"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Uitstel aflossing |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | janbr |
    | version | 1.10.0 |
    | created | 2024-03-07 12:33:22 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_74e47f85\_a936\_43c0\_8ef2\_1605bdb5efed |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Uitstel aflossing

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Vermindering terugvordering
> **Definitie Vermindering terugvordering:** 
>
> Vermindering terugvordering is het resultaat van een beslissing de terugvordering te verminderen met een zeker bedrag met zekere motivatie. De vermindering terugvordering wordt geadministreerd onder de vordering.

??? info "Kenmerken Model Vermindering terugvordering"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Vermindering terugvordering |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | janbr |
    | version | 1.10.0 |
    | created | 2024-03-07 12:33:22 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_1A6E0A2E\_9431\_0F7A\_1EAA\_263C1D239DF6 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Vermindering terugvordering

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Verrekening
> **Definitie Verrekening:** 
>
> Bij het vaststellen van de vordering wordt gekeken of de debiteur een uitkering geniet. Er zijn twee soorten situaties van verrekening. inkomstenverrekening waar de inkomsten 6 maanden wordt verrekend met de bijstandsuitkeringverrekening alias inhouding op een uitkering (een soort van loonbeslag) / verrekening in de zin van art. 60 lid 3 en 4 PW.Hier wordt de laatste bedoeld.Verrekening op grond van artikel 60 lid 3 en 4 Participatiewet door de gemeente gaat vóór beslag door een derde (artikel 60 lid 7 Participatiewet). Voor de praktijk betekent dit dat:Een lopend beslag wordt opgeschort zodra de gemeente (op grond van hun invorderingsbevoegdheid) een bedrag gaat verrekenen met de bijstandsuitkering. De beslaglegger wordt van de opschorting op de hoogte gesteld.De verrekening ongewijzigd wordt voortgezet indien nadien beslag door een derde wordt gelegd. De beslaglegger wordt medegedeeld dat het beslag niet uitvoerbaar is in verband met verrekening.Voorwaarde voor verrekening op grond van artikel 60 lid 3 en 4 Participatiewet is dat er een terugvorderingsbesluit of boetebesluit is genomen. Bij verstrekking van bijstand in de vorm van een geldlening kunnen echter de vastgestelde aflossingsbedragen direct worden verrekend op grond van artikel 48 lid 4 Participatiewet. Een terugvorderingsbesluit ingevolge artikel 58 lid 2 onderdeel b Participatiewet is dan dus niet noodzakelijk.Pseudo-verrekening gaat niet voor beslag.Pseudo-verrekening zoals bedoeld in artikel 60a Participatiewet gaat niet voor beslag door een derde onder een andere gemeente (of onder het Uitvoeringsinstituut werknemersverzekeringen of de Sociale verzekeringsbank).Een verrekening is verder te behandelen als een vordering, maar juridisch een ander ding.

??? info "Kenmerken Model Verrekening"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Verrekening |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | janbr |
    | version | 1.10.0 |
    | created | 2024-03-07 12:33:22 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_1EA8771B\_DB7F\_17D8\_8AB8\_26A1BD8F6A56 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Verrekening

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Verwijtbare vordering
> **Definitie Verwijtbare vordering:** 
>
> Een vordering is een eis op een persoon, zeg debiteur, die een zeker bedrag terug moet betalen aan de gemeente. Het zijn vorderingen die zijn ingesteld vanwege het niet nakomen van de inlichtingen-plicht waardoor de uitkerende instantie ten onrechte heeft uitbetaald . De oorzaak van een vordering is velerlei, Zie daarvoor de categorie-indeling.Vorderingen kunnen uit meerdere componenten bestaan.Vorderingen kunnen ook onderling in relatie staan, bijvoorbeeld: Een opgelegde boete wegens het schenden van de inlichtingenplicht heeft een relatie met een verwijtbare vordering.Deze type vordering zijn als verbijzonderingen opgenomen, opdat deze relaties expliciet kunnen worden gelegd.

??? info "Kenmerken Model Verwijtbare vordering"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Verwijtbare vordering |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | janbr |
    | version | 1.10.0 |
    | created | 2024-03-07 12:33:22 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_11F2FF40\_D317\_92C3\_C4DB\_2931225D4B40 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Verwijtbare vordering

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Vordering
> **Definitie Vordering:** 
>
> Een vordering is een eis op een persoon, zeg debiteur, die een zeker bedrag (terug) moet betalen aan de gemeente in het kader van de bijstand of een bijstandsgerelateerde uitkering.De oorzaak van een vordering is velerlei, Zie daarvoor de categorie-indeling.Vorderingen kunnen uit meerdere componenten bestaan.Vorderingen kunnen ook onderling in relatie staan, bijvoorbeeld: Een opgelegde boete wegens het schenden van de inlichtingenplicht heeft een relatie met een verwijtbare vordering.Deze type vordering zijn als verbijzonderingen opgenomen, opdat deze relaties expliciet kunnen worden vastgelegd.

??? info "Kenmerken Model Vordering"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Vordering |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | janbr |
    | version | 1.10.0 |
    | created | 2024-03-07 12:33:22 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_14116EEA\_C461\_0DB2\_97AB\_263C0A4777FC |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Vordering

| Attribute | Datatype | Description |
| :--- | :--- | :--- |



### Vorderingscomponent
> **Definitie Vorderingscomponent:** 
>
> Vorderingen, die bestaan uit verschillende rechtmaanden, worden gesplitst in vorderingscomponenten alsde rechtmaanden niet aansluitend zijn ofals er tussen opvolgende rechtmaanden een jaarovergang zit.De een opeenvolgende reeks van rechtmaanden binnen een jaar wordt gekoppeld aan de vorderingscomponent. Dit gebeurt tijdens het vaststellen van de terugvordering.

??? info "Kenmerken Model Vorderingscomponent"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Vorderingscomponent |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | janbr |
    | version | 1.10.0 |
    | created | 2024-03-07 12:33:22 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_1A979E6B\_841E\_392B\_952F\_29311D13BF9F |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Vorderingscomponent

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| Priotype | Date |  |






## Enumeraties Model Terug- en invordering


### Verwerkingsstatus
Geen Definitie

Het enumeratie Verwerkingsstatus kent de volgende waarden:



De enumeratie Verwerkingsstatus heeft de volgende kenmerken:

??? info "Kenmerken Model Verwerkingsstatus"

    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | Verwerkingsstatus |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | janbr |
    | version | 1.1.0 |
    | created | 2024-03-07 12:33:22 |
    | modified | 2025-08-06 14:19:42 |
    | id | EAID\_3d294c89\_52a2\_4589\_ae22\_a0ce7b1f4964 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    


