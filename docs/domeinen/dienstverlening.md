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

Een bijzondere vorm van ‘AanvraagOfMelding’ is de ‘MOR-AanvraagOfMelding’: de melding openbare ruimte (MOR), een bericht van een inwoner over een gebrek of opvallendheid in de openbare ruimte, zoals een losse stoeptegel of een kapotte lantaarnpaal, meestal gedaan via een meldapp als Fixi of Buitenbeter. Naast de gegevens van ‘AanvraagOfMelding’ legt de ‘MOR-AanvraagOfMelding’ de locatie vast als punt en als ‘Adresaanduiding’, met een omschrijving van de plek, de datum waarop de behandeling is ingepland en of de melding anoniem is gedaan. Voor de sturing op de afhandeling kent ‘AanvraagOfMelding’ de behandelaar (een ‘Medewerker’) en het behandelend team (een ‘OrganisatorischeEenheid’), de datum van de eerste reactie, een indicatie voor hoge prioriteit, de normtijd voor afhandeling en het resultaat. Deze uitbreiding komt uit het voorstel van de gemeenten Katwijk en Land van Cuijk (2026). Het diagram ‘MOR 2.0’ staat in Enterprise Architect in het package ‘Meldingen Openbare Ruimte’ onder ‘Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing’; de objecttypen zelf horen bij ‘Model Dienstverlening’. Meldingen die beheerders zelf doen over beheerobjecten, zoals schouwmeldingen, staan in [Beheer openbare ruimte](ruimteAlgemeen.md#schouwen-en-meldingen).

![Melding openbare ruimte][meldingOpenbareRuimte]

In de volgende figuur is de koppeling van ‘Klantcontact’ met ‘Zaak’ uit de RGBZ getoond. Hier is te zien dat een ‘Klantcontact’ betrekking kan hebben op een ‘Zaak’. Een ‘AanvraagOfMelding’ kan leiden tot een ‘Zaak’.

Ten opzichte van de RGBZ is het model uitgebreid met een ‘Betaling’ en ‘Heffing’, immers de gemeente legt voor veel producten en diensten een ‘Heffing’ op waarop een ‘Betaling’ plaats moet vinden.

![Klantcontact en Zaken][klantcontactEnZaak]

In de volgende figuur is de relatie van de ‘Betrokkene’ met het ‘Klantcontact’ en de ‘Zaak’ te zien.

![Dienstverlening en Betrokkene][dienstverleningEnBetrokkene]

[klantcontact]: image/EAID_282A4979_0BBC_4448_B71C_0CE64829083B.jpg "Dienstverlening en Klantcontacten"
[aanvraagEnMelding]: image/EAID_5901286A_E9EF_4360_9CE6_32B6FDE1C970.jpg "Objecttypen Aanvragen en meldingen"
[meldingOpenbareRuimte]: image/EAID_B3CC7874_57AA_4aeb_BF3F_98A64E9D76E5.jpg "Melding openbare ruimte (MOR 2.0)"
[klantcontactEnZaak]: image/EAID_48B6C3F9_CCF1_4794_8252_FC6543409B78.jpg "Klantcontact en Zaken"
[dienstverleningEnBetrokkene]: image/EAID_1D7802F4_3458_4bb4_8431_16C7F85473FC.jpg "Dienstverlening en Betrokkene"
