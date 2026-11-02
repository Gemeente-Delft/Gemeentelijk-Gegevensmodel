# Werk

Het subdomein **Werk** bevat de gegevens die gemeenten vastleggen bij de begeleiding van inwoners naar werk, in het kader van de Participatiewet. Het beschrijft wat iemand meebrengt naar de arbeidsmarkt, zoals opleiding, werkervaring, taalbeheersing en arbeidsvermogen, welke voorkeuren, beperkingen en verplichtingen er zijn, en welke bemiddeling en voorzieningen de gemeente inzet.

Het model is in versie 2.4.0 opgenomen op basis van een proposal van de gemeente Utrecht, dat voortbouwt op het Thomas-model van de gemeente Rotterdam en het Utrechtse datamodel CommUtr. Het sluit aan op *Sociaal Domein Generiek*: een **Werkzoekende** is een specialisatie van de **Client** uit dat model. Inhoudelijk ligt het dicht bij de subdomeinen *Inkomen* en *Inburgering*.

![Gegevensmodel Werk][werk]

[werk]: image/EAID_F93A23D7_BF68_46e0_A6D4_96508ACED81E.jpg "Gegevensmodel Werk"

## Uitleg afbeelding

Centraal staat het objecttype **Werkzoekende**: het werkprofiel van een persoon, met de periode waarin iemand als werkzoekende geldt. De meeste objecttypen hangen rechtstreeks aan de werkzoekende, enkele via een tussenliggend objecttype. Ze vallen in vier groepen.

### Bemiddeling en re-integratie

* **Bemiddelingsactiviteit**: één concreet bemiddelingscontact, waarbij de gemeente of uitvoeringsinstantie een werkzoekende in contact brengt met een werkgever of werkplek, bijvoorbeeld door verwijzing naar een vacature. Legt het soort contact, de status, het resultaat en een eventuele plaatsing vast. Dit komt overeen met *BemiddelingsActiviteit* in het Thomas-model.
* **Reintegratievoorziening**: een voorziening of dienst die de kansen op werk vergroot, met toekenning, looptijd en type.
* **DoelReintegratievoorziening**: het beoogde effect van de ingezette voorzieningen, zoals toeleiding naar werk of maatschappelijke participatie.
* **Loonkostensubsidie**: een tegemoetkoming aan een werkgever bij verminderde loonwaarde, gekoppeld aan een re-integratievoorziening.
* **Bemiddelingsberoep**: het beroep waarnaar iemand wordt bemiddeld.
* **BeschikbaarVoorBemiddeling**: of iemand direct bemiddelbaar is, en tot wanneer.

Een participatie- of re-integratietraject als geheel en de tegenprestatie hebben in dit model geen eigen objecttype.

### Beschikbaarheid, voorkeuren en verplichtingen

* **BeschikbaarVoorArbeid**: vanaf wanneer, op welke dagen en hoeveel uur per week iemand beschikbaar is, met een eventuele opzegtermijn.
* **Flexibiliteit**: de bereidheid om buiten de beroepswens, onder niveau, zwaar of onregelmatig te werken.
* **Mobiliteit**: maximale reistijd, vervoermiddel en de bereidheid te verhuizen.
* **Voorkeur**: wensen over branche, soort baan, soort werk en werklocatie.
* **Ontheffing**: een formele ontheffing van verplichtingen rond arbeidsparticipatie, met aanvraag, besluit en eventuele herziening.
* **VrijstellingArbeidsplicht**: of en waarom iemand tijdelijk of structureel is vrijgesteld van de arbeidsplicht.
* **Doelgroepenregister**: opname in het landelijke doelgroepenregister, het advies van UWV en de baanafspraak.

### Werk en werkervaring

* **Arbeidsverhouding**, met een of meer **Arbeidsperiodes**: huidige en eerdere dienstverbanden, met functie en uren.
* **Werkervaring**: ervaring in een beroep en het aantal jaren.
* **Werkzaamheden anders dan in arbeidsverhouding**: werk zonder arbeidsovereenkomst, zoals vrijwilligerswerk of werk als zelfstandige of freelancer. **Werkzaamheden als mantelzorger** is daar een specialisatie van.

### Kwalificaties en vermogen

* **Opleidingsniveau** en **Opleiding**: het opleidingsniveau en de gevolgde opleidingen. De **Opleidingsnaam** is gecodeerd (**OpleidingsnaamGecodeerd**, met synoniemen) of vrije tekst (**OpleidingsnaamOngecodeerd**).
* **Taalbeheersing** en **TaalbeheersingNederlands**: de taalvaardigheid per taal, en voor het Nederlands in het bijzonder.
* **Rijbewijs /Certificaat**: rijbewijzen en certificaten.
* **Arbeidsmarktkwalificaties**: de klanttypering, het werk- en denkniveau en de taalbeheersing zoals die voor bemiddeling wordt ingeschat.
* **Vaardigheidsvaststelling**: de laatst vastgestelde mate van een vaardigheid.
* **Arbeidsvermogen**: een inschatting van wat iemand aan arbeid kan verrichten, bijvoorbeeld onder het wettelijk minimumloon of zelfstandig daarboven.
* **ZelfredzaamheidScore**: de zelfredzaamheid per levensdomein volgens de Zelfredzaamheid-Matrix.

Enumeraties leggen de toegestane waarden vast, zoals beroepscategorieën volgens SETU, opleidingsniveaus, taalvaardigheid, soorten ontheffing en het kanaal van een contactmoment. Daarmee blijven registratie en gegevensuitwisseling tussen systemen eenduidig.
