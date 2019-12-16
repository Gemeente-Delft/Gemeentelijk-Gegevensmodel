# Dienstverlening

De gegevensdefinities van dienstverlening draaien om het objecttype ‘Klantcontact’. Een ‘Klantcontact’ betreft een feitelijk contact van de gemeente met een burger of ondernemer. Het komt voort uit het RGBZ 2.0, wat de volgende definitie hiervoor kent:

* Persoonlijk contact: een gebeurtenis van een aaneengesloten tijdsspanne waarbij interactief informatie wordt uitgewisseld, tussen minimaal 2 partijen, waarvan tenminste 1 medewerker van een gemeente en tenminste 1 natuurlijk persoon, eventueel in de rol van medewerker van een niet-natuurlijk persoon of een vestiging.
* Anoniem klantcontact: een gebeurtenis van een aaneengesloten tijdsspanne waarbij interactief informatie wordt uitgewisseld tussen minimaal 2 partijen waarvan tenminste 1 medewerker van een gemeente en 1 of meer natuurlijke personen die niet zijn geïdentificeerd.
* Informatie-ontvangst: Een gebeurtenis waarbij op een bepaald moment voor de gemeente bestemde informatie wordt ontvangen door de Gemeente (ook al is de afzender bekend, bij de gebeurtenis is de afzender niet actief betrokken).
* Informatie-verzending: Een gebeurtenis waarbij op een bepaald moment voor een burger of bedrijf bestemde informatie wordt verzonden door de Gemeente (ook al is de geadresseerde bekend, bij de gebeurtenis is de geadresseerde niet actief betrokken).

In het GGM is het ’Klantcontact’ wat concreter ingevuld, zodat het goed gebruikt kan worden om statistiek op te bouwen over de dienstverlening. Het gaat hier om zaken als wachttijden, aantal opgehangen telefoontjes, bezetting. Klantcontacten kunnen voortkomen uit:

1. Een ‘Telefoontje’: als een burger of ondernemer (of andere partij) belt naar de gemeente. Als er een gesprek uit voortkomt is er sprake van een ‘Klantcontact’, als er vooraf wordt opgehangen is er wel sprake van een telefoontje, maar niet van een klantcontact.
2. Een ‘Balieafspraak’: als een burger of ondernemer (of andere partij) een afspraak heeft mondt deze uit in een ‘Klantcontact’ als de afspraak werkelijk plaatsvindt. In de andere gevallen worden de balieafspraken wel bijgehouden.
3. Een ‘AanvraagOfMelding’: in dit geval gaat het om een bericht dat een burger of ondernemer (of andere partij) naar de gemeente verstuurt, via een elektronisch formulier of anderszins. Als deze ontvangen wordt is er altijd sprake van een ‘Klantcontact’. Dit objecttype kan ook worden gebruikt voor uitgaande communicatie.

In de volgende figuur is ‘Klantcontact’ in relatie tot ‘Telefoontjes’ en ‘Balieafspraken’ te zien.
  
![Dienstverlening en Klantcontacten][klantcontact]

Een ‘Klantcontact’ kan betrekking hebben op een ‘ZAAK’, en kan plaatsvinden op een bepaalde ‘Vestiging’ van de gemeente (in het geval van elektronische is deze leeg) en kan betrekking hebben op meerdere ‘ProductOfDienst’.

Een ‘Telefoontje’ heeft een ‘Telefoonstatus’, zoals: vroegtijdig opgehangen, opgenomen, etc. Daarnaast kan een ‘Telefoontje’ een bepaald ‘Telefoononderwerp’ hebben. Als een ‘Telefoontje’ wordt doorverbonden kunnen er meerdere ‘Klantcontacten’ uit ontstaan.

Een ‘Balieafspraak’ is met een ‘Medewerker’ en kan meerdere ‘ProductOfDienst’ betreffen. Een ‘Afspraakstatus’ kent waarden als: ‘Wachtend’, ‘In behandeling’, ‘Niet gekomen’, afhankelijk van het gebruikte baliesysteem. Voor ‘Balieafspraken’ worden verschillende soorten wachttijden gehanteerd:

* Bruto-wachttijd, de tijd dat iemand werkelijk wacht nadat hij of zij zich heeft aangemeld. Dit onafhankelijk van het tijdstip dat is afgesproken. 
* Netto-wachttijd, de tijd dat iemand eerder of later wordt geholpen dan is afgesproken. Als iemand eerder wordt geholpen dan is afgesproken, krijg je een negatieve netto-wachttijd, als iemand later wordt geholpen een positieve wachttijd.

In de volgende figuur is de uitwerking voor een ‘AanvraagOfMelding’ te zien. Een ‘AanvraagOfMelding’ is een bericht dat een burger of ondernemer (of andere partij) aan de gemeente stuurt. Het kan hier gaan om een brief (gescand), een bericht via het meldingensysteem of website en ook om berichten van externe applicaties zoals Buitenbeter.

‘AanvraagOfMelding’ is flexibel gemodelleerd, het wordt ingediend met een formulier van een bepaald ‘Formuliersoort’ waarop een aantal velden is gedefinieerd als ‘Formuliersoortveld’. Zo ondersteunt het GGM willekeurige formulieren, ongeacht de velden die erop staan. Aan een ‘Formuliersoortveld’ en aan de ‘AanvraagOfMelding’ is ‘AanvraagData’ gekoppeld waar de werkelijke inhoud van de aanvraag wordt geplaatst. Een ‘AanvraagOfMelding’ heeft 1 of meer ‘Onderwerpen’, die op hun beurt hiërarchisch zijn vormgegeven.  

Bij de Gemeente Delft gebruiken wij Pivot-queries om de aanvragen en meldingen te vertalen naar specifieke formulieren.

![Objecttypen Aanvragen en meldingen][aanvraagEnMelding]

In de volgende figuur is de koppeling van ‘Klantcontact’ met ‘Zaak’ uit de RGBZ getoond. Hier is te zien dat een ‘Klantcontact’ betrekking kan hebben op een ‘Zaak’. Een ‘AanvraagOfMelding’ kan leiden tot een ‘Zaak’.

Ten opzichte van de RGBZ is het model uitgebreid met een ‘Betaling’ en ‘Heffing’, immers de gemeente legt voor veel producten en diensten een ‘Heffing’ op waarop een ‘Betaling’ plaats moet vinden.

![Klantcontact en Zaken][klantcontactEnZaak]

In de volgende figuur is de relatie van de ‘Betrokkene’ met het ‘Klantcontact’ en de ‘Zaak’ te zien.

![Dienstverlening en Betrokkene][dienstverleningEnBetrokkene]

[klantcontact]: image/EAID_282A4979_0BBC_4448_B71C_0CE64829083B.gif "Dienstverlening en Klantcontacten"
[aanvraagEnMelding]: image/EAID_5901286A_E9EF_4360_9CE6_32B6FDE1C970.gif "Objecttypen Aanvragen en meldingen"
[klantcontactEnZaak]: image/EAID_48B6C3F9_CCF1_4794_8252_FC6543409B78.gif "Klantcontact en Zaken"
[dienstverleningEnBetrokkene]: image/EAID_1D7802F4_3458_4bb4_8431_16C7F85473FC.gif "Dienstverlening en Betrokkene"
