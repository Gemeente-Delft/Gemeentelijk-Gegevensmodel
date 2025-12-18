# Model Vroegsignalering
## Inleiding
> **Definitie Model Vroegsignalering:** 
>
> Alle objecttypen die voortkomen uit de processen rond vroegsignalering. In het kader van het programma DDAS (Data Delen Armoede en Schulden) opgesteld.

??? info "Kenmerken Model Model Vroegsignalering"

    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | Model Vroegsignalering |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.1.0 |
    | created | 2025-04-23 15:37:33 |
    | modified | 2025-12-18 15:38:53 |
    | id | EAPK\_BB7B01A9\_44F5\_4e0f\_B158\_0DDAA5B6593D |
    

Het model 'Model Vroegsignalering' kent de volgende objecttypen:

* **AanleverendeOrganisatie**: Organisatie de data aanlevert aan het CBS. Het kan hier gaan om de gemeente zelf, of een partij die namens de gemeente uitvoering geeft aan de afhandeling van vroegsignalen.
* **Contactpersoon**: Contactpersoon bij de aanleverende organisatie.
* **Contactpoging**: Een Contactpoging is de actie die de gemeente onderneemt om in contact te treden met de inwoner naar aanleiding van een vroegsignaal. Een contactpoging maakt onderdeel uit van de vroegsignaalzaak en kan verschillende vormen aannemen, zoals een telefoongesprek, huisbezoek, brief of digitaal bericht. Van elke contactpoging wordt vastgelegd wanneer deze is gedaan, op welke wijze, met welk doel en wat het resultaat was (bijvoorbeeld: geen gehoor, gesprek gevoerd, brief retour ontvangen).
* **Signaalpartner**: 
> Een signaalpartner is een organisatie die op grond van artikel 2.2.1 van de Wet gemeentelijke schuldhulpverlening (Wgs) bevoegd is om signalen van betalingsachterstanden door te geven aan de gemeente met het doel vroegtijdige hulpverlening bij schulden mogelijk te maken. Signaalpartners zijn dienstverleners met een maatschappelijk belang, zoals zorgverzekeraars, energieleveranciers, drinkwaterbedrijven en woningverhuurders.
> Een signaalpartner verstrekt een vroegsignaal aan de gemeente wanneer bij een klant of huurder sprake is van een betalingsachterstand die voldoet aan de wettelijke en/of contractuele criteria voor signalering.
* **Vroegsignaal**: 
> Een Vroegsignaal is een bericht dat door een signaalpartner (zoals een zorgverzekeraar, energieleverancier of verhuurder) aan de gemeente wordt verstrekt, met als doel de gemeente te informeren over een mogelijk beginnende schuldsituatie van een inwoner. Het vroegsignaal vormt het startpunt van het gemeentelijk proces van vroegsignalering van schulden.
> De juridische grondslag voor het ontvangen en verwerken van vroegsignalen is vastgelegd in artikel 2.2.1 van de Wet gemeentelijke schuldhulpverlening (Wgs). Deze wet verplicht gemeenten om vroegtijdig signalen van betalingsachterstanden te ontvangen en op basis daarvan inwoners passende hulp aan te bieden.
* **Vroegsignaalzaak**: Een Vroegsignaalzaak is procesmatige eenheid binnen de gemeentelijke organisatie waarin de behandeling van één of meerdere vroegsigna(a)len is/zijn ondergebracht. De vroegsignaalzaak omvat alle handelingen die de gemeente verricht naar aanleiding van het ontvangen vroegsignaal, zoals het vastleggen van het signaal, het uitvoeren van een eerste beoordeling, het leggen van contact met de inwoner, het registreren van contactpogingen en -resultaten, en het eventueel toeleiden naar schuldhulpverlening of andere passende ondersteuning.


## Objecttypen Model Vroegsignalering


### AanleverendeOrganisatie
> **Definitie AanleverendeOrganisatie:** 
>
> Organisatie de data aanlevert aan het CBS. Het kan hier gaan om de gemeente zelf, of een partij die namens de gemeente uitvoering geeft aan de afhandeling van vroegsignalen.

??? info "Kenmerken Model AanleverendeOrganisatie"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | AanleverendeOrganisatie |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.9.0 |
    | created | 2025-07-10 14:53:49 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_3109FEF3\_A1CB\_4f50\_800B\_376A18465F9F |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype AanleverendeOrganisatie

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| naam | AN200 |  |
| kvk-nummer | AN80 |  |



### Contactpersoon
> **Definitie Contactpersoon:** 
>
> Contactpersoon bij de aanleverende organisatie.

??? info "Kenmerken Model Contactpersoon"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Contactpersoon |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.9.0 |
    | created | 2025-07-10 14:51:54 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_A629ED5F\_E919\_6316\_A279\_92891F2325BB |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Contactpersoon

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| naam | AN200 |  |
| telefoonnummer | AN200 |  |
| email | email |  |
| functietitel | AN200 |  |



### Contactpoging
> **Definitie Contactpoging:** 
>
> Een Contactpoging is de actie die de gemeente onderneemt om in contact te treden met de inwoner naar aanleiding van een vroegsignaal. Een contactpoging maakt onderdeel uit van de vroegsignaalzaak en kan verschillende vormen aannemen, zoals een telefoongesprek, huisbezoek, brief of digitaal bericht. Van elke contactpoging wordt vastgelegd wanneer deze is gedaan, op welke wijze, met welk doel en wat het resultaat was (bijvoorbeeld: geen gehoor, gesprek gevoerd, brief retour ontvangen).

??? info "Kenmerken Model Contactpoging"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Contactpoging |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.9.0 |
    | created | 2025-04-09 16:07:30 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_C7000EFD\_826C\_4e47\_BD80\_075A6EF4E558 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Contactpoging

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| soort | Enumeratie: "EnumContactsoort" |  |
| bereikt | boolean | Er is succesvol contact met de client gemaakt. |
| datum | Date |  |
| dagdeel | Enumeratie: "EnumDagdeel" | Ochtend, middag of avond |



### Signaalpartner
> **Definitie Signaalpartner:** 
>
> 
> Een signaalpartner is een organisatie die op grond van artikel 2.2.1 van de Wet gemeentelijke schuldhulpverlening (Wgs) bevoegd is om signalen van betalingsachterstanden door te geven aan de gemeente met het doel vroegtijdige hulpverlening bij schulden mogelijk te maken. Signaalpartners zijn dienstverleners met een maatschappelijk belang, zoals zorgverzekeraars, energieleveranciers, drinkwaterbedrijven en woningverhuurders.
> Een signaalpartner verstrekt een vroegsignaal aan de gemeente wanneer bij een klant of huurder sprake is van een betalingsachterstand die voldoet aan de wettelijke en/of contractuele criteria voor signalering.

??? info "Kenmerken Model Signaalpartner"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Signaalpartner |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.9.0 |
    | created | 2025-04-09 16:16:46 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_3643CF44\_EFAA\_4939\_9AEB\_ACA8D8EE11F9 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Signaalpartner

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| type | Enumeratie: "EnumSignaalpartner" |  |



### Vroegsignaal
> **Definitie Vroegsignaal:** 
>
> 
> Een Vroegsignaal is een bericht dat door een signaalpartner (zoals een zorgverzekeraar, energieleverancier of verhuurder) aan de gemeente wordt verstrekt, met als doel de gemeente te informeren over een mogelijk beginnende schuldsituatie van een inwoner. Het vroegsignaal vormt het startpunt van het gemeentelijk proces van vroegsignalering van schulden.
> De juridische grondslag voor het ontvangen en verwerken van vroegsignalen is vastgelegd in artikel 2.2.1 van de Wet gemeentelijke schuldhulpverlening (Wgs). Deze wet verplicht gemeenten om vroegtijdig signalen van betalingsachterstanden te ontvangen en op basis daarvan inwoners passende hulp aan te bieden.

??? info "Kenmerken Model Vroegsignaal"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Vroegsignaal |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.9.0 |
    | created | 2025-04-09 16:03:55 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_C6DA2586\_C0E3\_4868\_93E8\_64AF6D118092 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Vroegsignaal

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| crisissignaal | boolean | Betreft het een crisis? |
| warmeOverdracht | boolean | Er is al contact met persoon. Betreft verzoek deze persoon op te pakken in het kader van vroegsignalering. |
| bedrag | bedrag |  |
| ontstaansdatum | Date |  |
| signaaldatum | Date | Datum waarop de signaalpartner het signaal heeft verstuurd. |
| status | Enumeratie: "EnumSignaalstatus" |  |



### Vroegsignaalzaak
> **Definitie Vroegsignaalzaak:** 
>
> Een Vroegsignaalzaak is procesmatige eenheid binnen de gemeentelijke organisatie waarin de behandeling van één of meerdere vroegsigna(a)len is/zijn ondergebracht. De vroegsignaalzaak omvat alle handelingen die de gemeente verricht naar aanleiding van het ontvangen vroegsignaal, zoals het vastleggen van het signaal, het uitvoeren van een eerste beoordeling, het leggen van contact met de inwoner, het registreren van contactpogingen en -resultaten, en het eventueel toeleiden naar schuldhulpverlening of andere passende ondersteuning.

??? info "Kenmerken Model Vroegsignaalzaak"

    | Eigenschap | Waarde |
    | :--- | :------ |
    | name | Vroegsignaalzaak |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.9.0 |
    | created | 2025-04-09 16:05:23 |
    | modified | 2025-12-18 15:38:52 |
    | id | EAID\_1AA67F0D\_3B94\_48a3\_A037\_A2ACC6D61CF0 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    

Attributen van objecttype Vroegsignaalzaak

| Attribute | Datatype | Description |
| :--- | :--- | :--- |
| resultaat | Enumeratie: "EnumEindresultaat" |  |
| matchingsdatum | Date | De datum waarop de matching wordt uitgevoerd. |
| startdatum_matchtingperiode | Date | De matchingperiode is het tijdvak waarover de matching plaatsvindt. Hier de startdatum van de matching, die binnen de matchingsperiode valt. |
| datum_opgepakt | Date | De datum waarop de gemeente de zaak heeft opgepakt. |
| einddatum_matchingperiode | Date | De matchingperiode is het tijdvak waarover de matching plaatsvindt. Hier de einddatum van de matching, die binnen de matchingsperiode valt. |






## Enumeraties Model Vroegsignalering


### EnumContactsoort
Enumeratie met daarin de soorten onderscheiden contactsoorten bij een contactpoging.

Het enumeratie EnumContactsoort kent de volgende waarden:

* **Mail**: Contact via e-mail, vaak gebruikt voor laagdrempelige informatievoorziening of opvolging.
* **Brief**: Een fysieke brief, vaak met uitleg over de achterstand en het hulpaanbod, verzonden per post.
* **SMS/Whatsapp**: Een tekstbericht verstuurd via sms, WhatsApp of andere digitale berichtendienst.
* **Telefoon**: Telefonisch contact, waarbij direct met de inwoner wordt gesproken of een voicemail wordt ingesproken.
* **Huisbezoek**: Een persoonlijke contactpoging aan huis, al dan niet aangekondigd, om direct met de inwoner in gesprek te gaan.
* **Kaartje**: Een informatief of uitnodigend kaartje dat bij de inwoner thuis wordt achtergelaten, bijvoorbeeld bij een gemist huisbezoek.
* **Administratief**: Administratieve afhandeling zonder contact
* **Afspraak op locatie**: Het contact heeft op locatie van de uitvoerder plaatsgevonden, bijv. op het gemeentekantoor, het kantoor van het sociaal team of op het kantoor van een welzijnsorganisatie.


De enumeratie EnumContactsoort heeft de volgende kenmerken:

??? info "Kenmerken Model EnumContactsoort"

    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | EnumContactsoort |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.9.0 |
    | created | 2025-04-09 16:10:41 |
    | modified | 2025-12-18 15:38:53 |
    | id | EAID\_7BA37694\_65C5\_4cfb\_8804\_D7EB6CE344FB |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    


### EnumDagdeel
Geen Definitie

Het enumeratie EnumDagdeel kent de volgende waarden:

* **Ochtend**: Tot 12:00 uur
* **Middag**: Tussen 12:00 en 18:00
* **Avond**: 18:00 uur of later


De enumeratie EnumDagdeel heeft de volgende kenmerken:

??? info "Kenmerken Model EnumDagdeel"

    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | EnumDagdeel |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.9.0 |
    | created | 2025-05-26 09:07:14 |
    | modified | 2025-12-18 15:38:53 |
    | id | EAID\_3860D42A\_481D\_42cd\_86F9\_79B5D6230A58 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    


### EnumEindresultaat
Enumeratie met de soorten Eindresultaten van een Vroegsignaalzaak.

Het enumeratie EnumEindresultaat kent de volgende waarden:

* **Niet opgepakt: herhaalde melding**: 
> Een signaal dat niet wordt opgepakt, omdat er recent al een signaal is ontvangen en opgepakt over dezelfde betalingsachterstand van dezelfde vastelastenpartner. De betalingsachterstand is niet hoger geworden. Als de achterstand wel hoger is geworden, moet deze wel worden opgepakt.
> Dit eindresultaat wordt teruggekoppeld aan de vastelastenpartner.
* **Niet opgepakt: onterecht signaal**: 
> Een signaal dat niet wordt opgepakt, omdat:
>
> * de gemelde achterstand lager is dan het drempelbedrag dat de gemeente hanteert, of;
> * het aantal dagen achterstand te hoog of te laag is.
>
> Dit eindresultaat wordt teruggekoppeld aan de vastelastenpartner.
* **Inwoner is overleden**: 
> Inwoner is overleden, hierbij kan het nodig zijn om aan het achtergebleven huishouden/de erven een hulpaanbod te doen. Dit is bijvoorbeeld relevant als nabestaanden nog op het adres wonen en afsluiting van water of energie ongewenst is.
> Al contact met nabestaanden? Registreer desondanks dit resultaat. Zo wordt de vastelastenpartner op de hoogte gebracht.
* **Persoon is geen inwoner (meer) in de gemeente**: 
> Wanneer de inwoner in een andere gemeente staat ingeschreven, geef de melding dan dit eindresultaat. De vastelastenpartner wordt hierdoor automatisch vanuit het systeem geïnformeerd dat de aangemelde klant geen inwoner (meer) is van de gemeente.
> Deel het signaal – waar mogelijk – vanuit vroegsignalering met de gemeente waar de inwoner **wél** staat ingeschreven. Doe dit telefonisch en/of per (beveiligde) e-mail.
>
> * **Al contact gehad met inwoner**: Is de inwoner niet meer woonachtig in de gemeente, maar is er wel (telefonisch) contact geweest? Registreer dan alsnog dit als eindresultaat. Zo wordt de vastelastenpartner op de hoogte gebracht.
> * **Verhuizing binnen de gemeente**: Woont de persoon niet meer op het adres dat bij het signaal staat, maar nog wel binnen de gemeente? Pak de melding dan op. Het eindresultaat hangt dan af van de uitkomst van het contact.
* **Niet opgepakt: andere reden**: 
> Als er een andere reden is dan de hierboven genoemde redenen waarom de melding niet wordt opgepakt. Vastelastenpartners mogen hierbij alleen weten dat de melding niet is opgepakt, maar de specifieke reden daarvoor niet. De gemeente kunnen de redenen voor zichzelf wel bijhouden.
> Mogelijke redenen om een melding **niet** op te pakken:
>
> * Inwoner verblijft onrechtmatig in Nederland volgens de BRP
> * Inwoner zit in detentie
> * De melding is bedoeld voor een rechtspersoon (bijv. een BV) in plaats van voor een ondernemer die een natuurlijk persoon is (eenmanszaak, VOF, CV of maatschap).
> * De melding is voor een inwoner die op een uitsluitingslijst van de gemeente, waarbij het onveilig is voor de vroegsignaleerder om contact te leggen. Bijvoorbeeld als sprake is van agressief gedrag of toegangsbeperking bij het gemeentehuis.
> * Als het vanwege een tekort aan personeel niet lukt om een melding op te pakken en contact te leggen met een inwoner.
> * Als een persoon niet meer op het adres woont en het is onbekend waar diegene wel woont
>
> **Verhuizing binnen de gemeente**: woont de persoon niet meer op het adres dat bij het signaal staat, maar nog wel binnen de gemeente? Pak de melding dan in principe op. Als onbekend is waar ieHet eindresultaat hangt dan af van de uitkomst van het contact.
* **Inwoner al bekend bij schuldhulpverlening**: Een inwoner is al bekend bij schuldhulpverlening (als particulier of als (ex-)ondernemer). Vanuit vroegsignalering is er contact geweest met de betrokken schuldhulpverlener. Deze neemt contact op met de schuldeiser en inwoner.
* **Inwoner heeft al een ander lopend traject**: 
> Uit eerder contact met de inwoner is bekend dat de inwoner al hulpverlening ontvangt, anders dan schuldhulpverlening. Dit kan zijn bij een externe netwerkpartner of bij een ander onderdeel van het sociaal domein.
> Wanneer de betrokken hulpverlener het signaal overneemt en verdere opvolging doet, wordt de melding binnen vroegsignalering afgesloten met het resultaat: *‘inwoner heeft al een ander lopend traject’.*
> **Voorwaarde: afstemming tussen vroegsignalering en betrokken hulpverlener**
> Vroegsignalering neemt contact op de betrokken hulpverlener. Zij spreken af wie de opvolging doet:
>
> * **Optie 1:** De betrokken hulpverlener neemt contact op met de inwoner en eventueel de schuldeiser.
>   De vroegsignalering blijft niet actief betrokken en ontvangt mogelijk alleen een terugkoppeling.
>   → Eindresultaat: *Inwoner heeft al een ander lopend traject.*
> * **Optie 2:** De vroegsignalering neemt zelf contact op met de inwoner over de betalingsachterstand. De betrokken hulpverlener speelt hierin geen actieve rol.
>   → Eindresultaat: afhankelijk van de uitkomst van het contact. In de notities kan worden vermeld dat de inwoner ook andere hulp ontvangt, maar het resultaat is **niet** *‘inwoner heeft al een ander lopend traject’.*
>
> **Let op:** Een bewindvoerder wordt niet beschouwd als betrokken hulpverlener, maar als een verlengde van de inwoner zelf.
* **Definitief geen contact kunnen krijgen**: Als het voor het afsluiten van de melding niet is gelukt om in contact te komen met de inwoner. De inwoner reageert niet op de contactpoging(en).
* **Geen reactie na eerder contact**: 
> Er is in eerste instantie contact is met de inwoner. Vervolgens lukt het niet meer om contact te krijgen.
> Bijvoorbeeld: de inwoner komt niet op de afspraak, is telefonisch onbereikbaar of reageert niet op e-mails of WhatsApp-berichten.
* **Inwoner hoeft geen hulp vanuit vroegsignalering**: 
> Er is contact geweest met de inwoner. Tijdens dit contactmoment geeft de inwoner aan geen hulp nodig te hebben en/of hier geen behoefte aan te hebben.
> Dit kan verschillende redenen hebben, zoals:
>
> * De inwoner geeft tijdens het contactmoment aan de betalingsachterstand zelf op te gaan lossen. Bijvoorbeeld door zelf een betalingsregeling te treffen en/of contact op te nemen met de schuldeiser.
> * De inwoner geeft aan niet te wachten op bemoeienis vanuit de gemeente en/of hulpverleningsorganisaties.
> * De inwoner heeft zelf naasten, een bewindvoerder en/of een hulpverleningsorganisatie die (kunnen) gaan helpen.
>
> Er kan tijdens dit contactmoment wat algemene informatie zijn verstrekt en/of tips gegeven, waar de inwoner zelf mee aan de slag gaat.
* **Inwoner heeft zelf al betaald/betalingsregeling getroffen**: Wanneer de inwoner al een oplossing blijkt te hebben voor de betalingsachterstand op het moment dat ervan uit vroegsignalering contact is met de inwoner. Hij/zij heeft al betaald of een betalingsregeling getroffen.
* **(Budget)advies en/of quick fix**: 
> Er is contact (geweest) met de inwoner en er is zodanige hulp geboden dat de inwoner binnen 30 dagen na hulpacceptatie (zelf) de betalingsachterstanden op kan lossen.
> Voorbeelden van ‘quick fixes’:
>
> * Hulp bij het maken van betalingsregeling/ betalingsafspraken;
> * Een gesprek over de mogelijkheden om de betalingsachterstanden op te lossen;
> * Hulp bij het ordenen van de administratie;
> * Het voeren van een budgetadviesgesprek;
> * Het geven van informatie en advies over het zelfstandig bereiken van duurzaam financieel evenwicht (zonder gebruik te maken van schuldhulpverlening of andere vormen van financiële dienstverlening);
> * Hulp bij het aanvragen van toeslagen en andere inkomensondersteunende voorzieningen;
> * Berekening van de beslagvrije voet.
* **Vervolghulp en/of verwijzing financieel**: 
> Hiervan is sprake als er een langer hulptraject wordt ingezet na (afronding van) de vroegsignalering. De vervolghulp en/of doorverwijzing is financieel: schuldhulpverlening, budgetcoaching of bewindvoering, etc.
> De vervolghulp kan binnen de eigen organisatie zijn (zelfs door dezelfde persoon) of een doorverwijzing naar een externe organisatie betekenen. Dit hangt af van wie en welke organisatie de vroegsignalering uitvoert en de beschikbare expertises binnen de organisatie.
* **Verwijzing zonder contact**: Wanneer bij vroegsignalering een inwoner wordt aangemeld bij een andere instantie, zonder dat de inwoner hiervan op de hoogte is of hiervoor toestemming heeft gegeven. Dit gebeurt alleen in uiterste gevallen, wanneer zorg noodzakelijk lijkt. Een voorbeeld hiervan is een aanmelding bij bemoeizorg.
* **Vervolghulp en/of verwijzing niet financieel**: 
> Hiervan is sprake als er een langer hulptraject wordt ingezet na (afronding van) de vroegsignalering. De vervolghulp en/of doorverwijzing is niet-financieel: maatschappelijk werk, verslavingszorg of gezinszorg etc.
> De vervolghulp kan binnen de eigen organisatie zijn (zelfs door dezelfde persoon) of een doorverwijzing naar een externe organisatie betekenen. Dit hangt af van wie en welke organisatie de vroegsignalering uitvoert en de beschikbare expertises binnen de organisatie.


De enumeratie EnumEindresultaat heeft de volgende kenmerken:

??? info "Kenmerken Model EnumEindresultaat"

    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | EnumEindresultaat |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.9.0 |
    | created | 2025-04-09 16:10:26 |
    | modified | 2025-12-18 15:38:53 |
    | id | EAID\_B78A9A0E\_65B0\_4c4b\_AA01\_99CFA196D740 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    


### EnumSignaalpartner
Enumeratie met de soorten te onderscheiden Signaalpartners.

Het enumeratie EnumSignaalpartner kent de volgende waarden:

* **Energie**: Inzake de energierekening (elektriciteit, gas en/of warmte) vanaf 30 dagen
* **Huur**: Inzake de huur vanaf 30 dagen.
* **Hypotheek**: Inzake hypotheek
* **CAK Zorgverzekeringen**: Als de zorgverzekering meer dan 6 maanden niet is betaald, wordt deze door CAK overgenomen.
* **Zorg**: Inzake de zorgverzekeringspremie inclusief premie voor aanvullende verzekering, eigen risico en eigen bijdragen van 30 tot 100 dagen.
* **Water**: Inzake de drinkwaterrekening vanaf 30 dagen
* **DUO**: Inzake schulden bij DUO
* **Belastingdienst**: Mensen die na een aanmaning hun belasting niet hebben betaald of terugbetaald.
* **CAK Eigen bijdrage**: 
> Achterstand bij het betalen van de Eigen bijdrage in het kader van WLZ, en WMO. De doelgroep voldoet aan deze drie voorwaarden:
>
> * Inwoners van de Gemeenten die het incassotraject hebben doorlopen (schriftelijke herinnering, aanmaning, minnelijk deurwaarders traject en telefonische poging tot persoonlijk contact). Het betreft hier achterstanden op gebied van eigen bijdrage Wmo of Wlz, geïncasseerd door het CAK. Het gaat hierbij specifiek om de groep die terugkeert van een minnelijk deurwaarderstraject.
> * Er is nog geen sprake van een gerechtelijke dwangmaatregel. De vroegsignalering gaat vooraf aan de inzet van een gerechtelijke procedure (doorgaans wordt die ingezet bij vorderingen > € 100,= achterstand).
> * Het lukt CAK niet om contact te krijgen of een betaalafspraak te maken met de klant.
* **Overige**: Overige partijen
* **Dienst Toeslagen**: Mensen die na een aanmaning te veel ontvangen toeslag niet hebben betaald of terugbetaald.


De enumeratie EnumSignaalpartner heeft de volgende kenmerken:

??? info "Kenmerken Model EnumSignaalpartner"

    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | EnumSignaalpartner |
    | toelichting |  |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.9.0 |
    | created | 2025-04-09 16:29:45 |
    | modified | 2025-12-18 15:38:53 |
    | id | EAID\_ACE0EA25\_898C\_4de3\_8196\_49AD3AE5481F |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    


### EnumSignaalstatus
Geen Definitie

Het enumeratie EnumSignaalstatus kent de volgende waarden:

* **Nog niet opgepakt**: De gemeente heeft het signaal nog niet opgepakt.
* **Niet opgepakt: onterecht signaal**: 
> Een signaal dat niet wordt opgepakt, omdat:
>
> * de gemelde achterstand lager is dan het drempelbedrag dat de gemeente hanteert, of;
> * het aantal dagen achterstand te hoog of te laag is.
>
> Dit eindresultaat wordt teruggekoppeld aan de vastelastenpartner.
* **Inwoner is overleden**: Inwoner is overleden, hierbij kan het nodig zijn om aan het achtergebleven huishouden/de erven een hulpaanbod te doen. Dit is bijvoorbeeld relevant als nabestaanden nog op het adres wonen en afsluiting van water of energie ongewenst is.
* **Persoon is geen inwoner (meer) in de gemeente**: 
> Wanneer de inwoner in een andere gemeente staat ingeschreven, geef de melding dan dit eindresultaat. De vastelastenpartner wordt hierdoor automatisch vanuit het systeem geïnformeerd dat de aangemelde klant geen inwoner (meer) is van de gemeente.
> Deel het signaal – waar mogelijk – vanuit vroegsignalering met de gemeente waar de inwoner **wél** staat ingeschreven. Doe dit telefonisch en/of per (beveiligde) e-mail.
>
> * **Al contact gehad met inwoner**: is de inwoner niet meer woonachtig in de gemeente, maar is er wel (telefonisch) contact geweest? Registreer dan alsnog dit als eindresultaat. Zo wordt de vastelastenpartner op de hoogte gebracht.
> * **Verhuizing binnen de gemeente**: woont de persoon niet meer op het adres dat bij het signaal staat, maar nog wel binnen de gemeente? Pak de melding dan op. Het eindresultaat hangt dan af van de uitkomst van het contact.
* **Niet opgepakt: herhaalde melding**: 
> Een signaal dat niet wordt opgepakt, omdat er recent al een signaal is ontvangen en opgepakt over dezelfde betalingsachterstand van dezelfde vastelastenpartner. De betalingsachterstand is niet hoger geworden. Als de achterstand wel hoger is geworden, moet deze wel worden opgepakt.
> Dit eindresultaat wordt teruggekoppeld aan de vastelastenpartner.
* **Niet opgepakt: andere reden**: 
> Als er een andere reden is dan de hierboven genoemde redenen waarom de melding niet wordt opgepakt. Vastelastenpartners mogen hierbij alleen weten dat de melding niet is opgepakt, maar de specifieke reden daarvoor niet. De gemeente kunnen de redenen voor zichzelf wel bijhouden.
> Mogelijke redenen om een melding **niet** op te pakken:
>
> * Inwoner verblijft onrechtmatig in Nederland volgens de BRP
> * Inwoner zit in detentie
> * De melding is bedoeld voor een rechtspersoon (bijv. een BV) in plaats van voor een ondernemer die een natuurlijk persoon is (eenmanszaak, VOF, CV of maatschap).
> * De melding is voor een inwoner die op een uitsluitingslijst van de gemeente, waarbij het onveilig is voor de vroegsignaleerder om contact te leggen. Bijvoorbeeld als sprake is van agressief gedrag of toegangsbeperking bij het gemeentehuis.
> * Als het vanwege een tekort aan personeel niet lukt om een melding op te pakken en contact te leggen met een inwoner.
> * Als een persoon niet meer op het adres woont en het is onbekend waar diegene wel woont
>
> **Verhuizing binnen de gemeente**
> Woont de persoon niet meer op het adres dat bij het signaal staat, maar nog wel binnen de gemeente? Pak de melding dan in principe op. Als onbekend is waar ieHet eindresultaat hangt dan af van de uitkomst van het contact.


De enumeratie EnumSignaalstatus heeft de volgende kenmerken:

??? info "Kenmerken Model EnumSignaalstatus"

    | Kenmerk | Waarde |
    | :--- | :------ |
    | name | EnumSignaalstatus |
    | toelichting | #NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. |
    | synoniemen |  |
    | uri |  |
    | bron |  |
    | author | Arjen Brienen |
    | version | 1.9.0 |
    | created | 2025-05-07 11:25:56 |
    | modified | 2025-12-18 15:38:53 |
    | id | EAID\_568499A3\_3FE7\_4342\_B1B4\_36A01AEAC1C9 |
    | domein_iv3 |  |
    | domein_dcat |  |
    | gemma_naam |  |
    | gemma_type |  |
    | gemma_url |  |
    | gemma_definitie |  |
    | gemma_toelichting |  |
    


