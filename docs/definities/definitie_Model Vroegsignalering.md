# Model Vroegsignalering
## Inleiding
> **Definitie Model Vroegsignalering:** 
>
> Geen definitie

Het model 'Model Vroegsignalering' kent de volgende objecttypen:

* **Contactpoging**: <font color="#0e0e0e">Een Contactpoging is de actie die de gemeente onderneemt om in contact te treden met de inwoner naar aanleiding van een vroegsignaal. Een contactpoging maakt onderdeel uit van de vroegsignaalzaak en kan verschillende vormen aannemen, zoals een telefoongesprek, huisbezoek, brief of digitaal bericht. Van elke contactpoging wordt vastgelegd wanneer deze is gedaan, op welke wijze, met welk doel en wat het resultaat was (bijvoorbeeld: geen gehoor, gesprek gevoerd, brief retour ontvangen).</font>
* **Signaalpartner**: <font color="#0e0e0e"><i>Een signaalpartner is een organisatie die op grond van artikel 2.2.1 van de Wet gemeentelijke schuldhulpverlening (Wgs) bevoegd is om signalen van betalingsachterstanden door te geven aan de gemeente met het doel vroegtijdige hulpverlening bij schulden mogelijk te maken. Signaalpartners zijn dienstverleners met een maatschappelijk belang, zoals zorgverzekeraars, energieleveranciers, drinkwaterbedrijven en woningverhuurders.</i></font> <font color="#0e0e0e"><i> </i></font><font color="#0e0e0e"><i>Een signaalpartner verstrekt een vroegsignaal aan de gemeente wanneer bij een klant of huurder sprake is van een betalingsachterstand die voldoet aan de wettelijke en/of contractuele criteria voor signalering.</i></font>
* **Vroegsignaal**: <font color="#0e0e0e">Een Vroegsignaal is een bericht dat door een signaalpartner (zoals een zorgverzekeraar, energieleverancier of verhuurder) aan de gemeente wordt verstrekt, met als doel de gemeente te informeren over een mogelijk beginnende schuldsituatie van een inwoner. Het vroegsignaal vormt het startpunt van het gemeentelijk proces van vroegsignalering van schulden.</font> <font color="#0e0e0e"> </font><font color="#0e0e0e"><i>De juridische grondslag voor het ontvangen en verwerken van vroegsignalen is vastgelegd in artikel 2.2.1 van de </i></font><font color="#0e0e0e"><i>Wet gemeentelijke schuldhulpverlening (Wgs)</i></font><font color="#0e0e0e"><i>. Deze wet verplicht gemeenten om vroegtijdig signalen van betalingsachterstanden te ontvangen en op basis daarvan inwoners passende hulp aan te bieden.</i></font>
* **Vroegsignaalzaak**: <font color="#0e0e0e">Een Vroegsignaalzaak is procesmatige eenheid binnen de gemeentelijke organisatie waarin de behandeling van &#233;&#233;n of meerdere vroegsigna(a)len is/zijn ondergebracht. De vroegsignaalzaak omvat alle handelingen die de gemeente verricht naar aanleiding van het ontvangen vroegsignaal, zoals het vastleggen van het signaal, het uitvoeren van een eerste beoordeling, het leggen van contact met de inwoner, het registreren van contactpogingen en -resultaten, en het eventueel toeleiden naar schuldhulpverlening of andere passende ondersteuning.</font>


Het model 'Model Vroegsignalering' heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | Model Vroegsignalering |
| toelichting |  |
| synoniemen |  |
| uri |  |
| bron |  |
| author | arjen |
| version | 1.0 |
| created | 2025-04-23 15:37:33 |
| modified | 2025-04-23 15:43:22 |
| id | EAPK_BB7B01A9_44F5_4e0f_B158_0DDAA5B6593D |


## Objecttypen Model Vroegsignalering


### Contactpoging
> **Definitie Contactpoging:** 
>
> <font color="#0e0e0e">Een Contactpoging is de actie die de gemeente onderneemt om in contact te treden met de inwoner naar aanleiding van een vroegsignaal. Een contactpoging maakt onderdeel uit van de vroegsignaalzaak en kan verschillende vormen aannemen, zoals een telefoongesprek, huisbezoek, brief of digitaal bericht. Van elke contactpoging wordt vastgelegd wanneer deze is gedaan, op welke wijze, met welk doel en wat het resultaat was (bijvoorbeeld: geen gehoor, gesprek gevoerd, brief retour ontvangen).</font>

| Eigenschap | Waarde |
| :--- | :------ |
| name | Contactpoging |
| toelichting | <memo> |
| synoniemen |  |
| uri |  |
| bron |  |
| author | arjen |
| version | 1.0 |
| created | 2025-04-09 16:07:30 |
| modified | 2025-04-23 15:38:19 |
| id | EAID_C7000EFD_826C_4e47_BD80_075A6EF4E558 |
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
| dagdeel | int | Ochtend, middag of avond |




### Signaalpartner
> **Definitie Signaalpartner:** 
>
> <font color="#0e0e0e"><i>Een signaalpartner is een organisatie die op grond van artikel 2.2.1 van de Wet gemeentelijke schuldhulpverlening (Wgs) bevoegd is om signalen van betalingsachterstanden door te geven aan de gemeente met het doel vroegtijdige hulpverlening bij schulden mogelijk te maken. Signaalpartners zijn dienstverleners met een maatschappelijk belang, zoals zorgverzekeraars, energieleveranciers, drinkwaterbedrijven en woningverhuurders.</i></font>
> <font color="#0e0e0e"><i>
> </i></font><font color="#0e0e0e"><i>Een signaalpartner verstrekt een vroegsignaal aan de gemeente wanneer bij een klant of huurder sprake is van een betalingsachterstand die voldoet aan de wettelijke en/of contractuele criteria voor signalering.</i></font>

| Eigenschap | Waarde |
| :--- | :------ |
| name | Signaalpartner |
| toelichting | <memo> |
| synoniemen |  |
| uri |  |
| bron |  |
| author | arjen |
| version | 1.0 |
| created | 2025-04-09 16:16:46 |
| modified | 2025-04-23 15:38:11 |
| id | EAID_3643CF44_EFAA_4939_9AEB_ACA8D8EE11F9 |
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
> <font color="#0e0e0e">Een Vroegsignaal is een bericht dat door een signaalpartner (zoals een zorgverzekeraar, energieleverancier of verhuurder) aan de gemeente wordt verstrekt, met als doel de gemeente te informeren over een mogelijk beginnende schuldsituatie van een inwoner. Het vroegsignaal vormt het startpunt van het gemeentelijk proces van vroegsignalering van schulden.</font>
> <font color="#0e0e0e">
> </font><font color="#0e0e0e"><i>De juridische grondslag voor het ontvangen en verwerken van vroegsignalen is vastgelegd in artikel 2.2.1 van de </i></font><font color="#0e0e0e"><i>Wet gemeentelijke schuldhulpverlening (Wgs)</i></font><font color="#0e0e0e"><i>. Deze wet verplicht gemeenten om vroegtijdig signalen van betalingsachterstanden te ontvangen en op basis daarvan inwoners passende hulp aan te bieden.</i></font>

| Eigenschap | Waarde |
| :--- | :------ |
| name | Vroegsignaal |
| toelichting | <memo> |
| synoniemen |  |
| uri |  |
| bron |  |
| author | arjen |
| version | 1.0 |
| created | 2025-04-09 16:03:55 |
| modified | 2025-04-23 15:37:59 |
| id | EAID_C6DA2586_C0E3_4868_93E8_64AF6D118092 |
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
| crisissignaal | boolean | Betreft het een crisis?
 |
| warmeOverdracht | boolean | Er is al contact met persoon. Betreft verzoek deze persoon op te pakken in het kader van vroegsignalering.  |
| bedrag | bedrag |  |
| ontstaansdatum | Date |  |
| signaaldatum | Date | Datum waarop de signaalpartner het signaal heeft verstuurd. |
| status | Enumeratie: "EnumSignaalstatus" |  |
| None | Class: "Signaalpartner" |  |
| None | Class: "Vroegsignaalzaak" |  |
| None | Class: "Client" |  |




### Vroegsignaalzaak
> **Definitie Vroegsignaalzaak:** 
>
> <font color="#0e0e0e">Een Vroegsignaalzaak is procesmatige eenheid binnen de gemeentelijke organisatie waarin de behandeling van &#233;&#233;n of meerdere vroegsigna(a)len is/zijn ondergebracht. De vroegsignaalzaak omvat alle handelingen die de gemeente verricht naar aanleiding van het ontvangen vroegsignaal, zoals het vastleggen van het signaal, het uitvoeren van een eerste beoordeling, het leggen van contact met de inwoner, het registreren van contactpogingen en -resultaten, en het eventueel toeleiden naar schuldhulpverlening of andere passende ondersteuning.</font>

| Eigenschap | Waarde |
| :--- | :------ |
| name | Vroegsignaalzaak |
| toelichting | <memo> |
| synoniemen |  |
| uri |  |
| bron |  |
| author | arjen |
| version | 1.0 |
| created | 2025-04-09 16:05:23 |
| modified | 2025-04-23 15:38:04 |
| id | EAID_1AA67F0D_3B94_48a3_A037_A2ACC6D61CF0 |
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
| matchingsdatum | Date |  |
| startdatum_matchtingperiode | Date |  |
| datum_opgepakt | Date |  |
| einddatum_matchingperiode | Date |  |
| None | Class: "Gemeente" |  |
| None | Class: "Contactpoging" |  |







## Enumeraties Model Vroegsignalering


### EnumContactsoort
Enumeratie met daarin de soorten onderscheiden contactsoorten bij een contactpoging.

Het enumeratie EnumContactsoort kent de volgende waarden:

* **Mail**: <Geen Definities>
* **Brief**: <Geen Definities>
* **SMS/Whatsapp**: <Geen Definities>
* **Telefoon**: <Geen Definities>
* **Huisbezoek**: <Geen Definities>
* **Kaartje**: <Geen Definities>
* **Overige**: <Geen Definities>


De enumeratie EnumContactsoort heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | EnumContactsoort |
| toelichting | <memo> |
| synoniemen | None |
| uri | None |
| bron | None |
| author | arjen |
| version | 1.0 |
| created | 2025-04-09 16:10:41 |
| modified | 2025-04-23 15:38:57 |
| id | EAID_7BA37694_65C5_4cfb_8804_D7EB6CE344FB |
| domein_iv3 | None |
| domein_dcat | None |
| gemma_naam | None |
| gemma_type | None |
| gemma_url | None |
| gemma_definitie | None |
| gemma_toelichting | None |



### EnumEindresultaat
Enumeratie met de soorten Eindresultaten van een Vroegsignaalzaak.

Het enumeratie EnumEindresultaat kent de volgende waarden:

* **Succesvol**: <Geen Definities>
* **Niet Succesvol**: <Geen Definities>
* **Geen Actie**: <Geen Definities>


De enumeratie EnumEindresultaat heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | EnumEindresultaat |
| toelichting | <memo> |
| synoniemen | None |
| uri | None |
| bron | None |
| author | arjen |
| version | 1.0 |
| created | 2025-04-09 16:10:26 |
| modified | 2025-04-23 15:38:52 |
| id | EAID_B78A9A0E_65B0_4c4b_AA01_99CFA196D740 |
| domein_iv3 | None |
| domein_dcat | None |
| gemma_naam | None |
| gemma_type | None |
| gemma_url | None |
| gemma_definitie | None |
| gemma_toelichting | None |



### EnumSignaalpartner
Enumeratie met de soorten te onderscheiden Signaalpartners.

Het enumeratie EnumSignaalpartner kent de volgende waarden:

* **energie**: <Geen Definities>
* **huur**: <Geen Definities>
* **hypotheek**: <Geen Definities>
* **CAK_Zorgverzekeringen**: Als de zorgverzekering meer dan 6 maanden niet is betaald, wordt deze door CAK overgenomen.

* **zorg**: <Geen Definities>
* **water**: <Geen Definities>
* **DUO**: <Geen Definities>
* **Belastingdienst**: <Geen Definities>
* **CAK_EigenBijdrage**: Achterstand bij het betalen van de Eigen bijdrage in het kader van WLZ, en WMO. Zie convenant CAK Wmo en WLZ.

* **Overige**: <Geen Definities>


De enumeratie EnumSignaalpartner heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | EnumSignaalpartner |
| toelichting | <memo> |
| synoniemen | None |
| uri | None |
| bron | None |
| author | arjen |
| version | 1.0 |
| created | 2025-04-09 16:29:45 |
| modified | 2025-04-23 15:38:45 |
| id | EAID_ACE0EA25_898C_4de3_8196_49AD3AE5481F |
| domein_iv3 | None |
| domein_dcat | None |
| gemma_naam | None |
| gemma_type | None |
| gemma_url | None |
| gemma_definitie | None |
| gemma_toelichting | None |



### EnumSignaalstatus
Geen Definitie

Het enumeratie EnumSignaalstatus kent de volgende waarden:



De enumeratie EnumSignaalstatus heeft de volgende kenmerken:

| Kenmerk | Waarde |
| :--- | :------ |
| name | EnumSignaalstatus |
| toelichting | None |
| synoniemen | None |
| uri | None |
| bron | None |
| author | arjen |
| version | 1.0 |
| created | 2025-05-07 11:25:56 |
| modified | 2025-05-07 11:26:54 |
| id | EAID_568499A3_3FE7_4342_B1B4_36A01AEAC1C9 |
| domein_iv3 | None |
| domein_dcat | None |
| gemma_naam | None |
| gemma_type | None |
| gemma_url | None |
| gemma_definitie | None |
| gemma_toelichting | None |




