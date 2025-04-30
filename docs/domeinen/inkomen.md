# Inkomen

Dit deeldomein is gebaseerd op het [GBI (Generieke Basisprocessen Inkomen)](https://vngr-gbi.gitlab.io/ontologie-inkomen/), waarvan een aantal onderdelen zijn opgenomen in het GGM. Het betreft hier de volgende onderdelen:

1. Normafwijking: gaat rechtmatigheid, dus over maatregelen en boetes bij afwijkingen;
2. Terug- en invordering: gedetailleerd model met daarin alle vorderingen en andere correcties op personen;
3. Reden aanvraag: geeft de achterliggende reden voor de aanvraag van een inkomensvoorziening;
3. Dienstenmodel: generiek model waarmee diensten op het gebied van inkomen kunnen worden vormgegeven.

De basis van dit deeldomein gevormd door `Inkomen (Basis objecttypen)`, aan te vullen met de GBI-deelmodellen. Deze worden in de volgende paragrafen beschreven. 

!!! danger "Observatie"

    Het Dienstenmodel van GBI is geen concreet model. Dit dienstenmodel heeft aanvullend invulling nodig voor specifieke gemeentelijke inkomensdiensten, zoals: IOAW, IOAZ, Bijstand, Bijzondere bijstand. Deze maken nu geen onderdeel uit van de GBI-ontologie. Het GGM heeft dat wel, maar op een minder geavanceerde manier. Deze zijn uitgewerkt in het subdomein Inkomen (Basis objecttypen), deze kunnen zonder nadere invulling worden gebruikt. Normafwijking en Terug- en invordering zijn wel concrete modellen, die zonder nadere invulling toegepast kunnen worden. 

## Inkomen (Basis objecttypen)

Het informatiemodel *Inkomen* biedt een gestructureerde weergave van de gegevens en relaties die relevant zijn binnen het sociaal domein, specifiek gericht op inkomensvoorzieningen. Het model is ontworpen om de administratieve processen rondom uitkeringen en inkomensondersteuning te ondersteunen. Het informatiemodel is net als de andere modellen binnen het sociaal domein opgebouwd rond het [objecttype ‘Client’](socdomeingeneriek.md). Deze kan 1 of meer inkomensvoorzieningen hebben, zoals een bijstandsuitkering, bijzondere bijstand of IOAZ.

![Basismodel Inkomen][inkomenbasis]

### Belangrijkste Entiteiten
1. **UitkeringsRun**  
   Dit object representeert een proces waarbij uitkeringen worden berekend en uitgekeerd. Een *UitkeringsRun* bevat meerdere componenten die samen de uitkering vormen.

2. **Component**  
   Een *Component* is een bouwsteen van een uitkering en kan verschillende soorten bevatten, zoals toeslagen of inhoudingen. Elke component heeft een relatie met een *ComponentSoort*, die het type van de component specificeert.

3. **ComponentSoort**  
   Dit object definieert het type van een component, bijvoorbeeld een basisuitkering of een specifieke toeslag.

4. **Inkomensvoorziening**  
   Dit is het centrale object dat inkomensondersteuning vertegenwoordigt, zoals bijstand, bijzondere bijstand, IOAW of IOAZ. Een *Inkomensvoorziening* is opgebouwd uit één of meerdere componenten en heeft een relatie met een *InkomensvoorzieningSoort*, die het type voorziening aangeeft.

5. **InkomensvoorzieningSoort**  
   Dit object beschrijft de verschillende soorten inkomensvoorzieningen, zoals hierboven genoemd.

6. **Regeling**  
   Een *Regeling* is gekoppeld aan een ingeschreven persoon (client) en beschrijft de specifieke afspraken of voorwaarden waaronder inkomensondersteuning wordt verleend. Een regeling heeft altijd een relatie met een *RegelingSoort*, die het type regeling specificeert.

7. **RegelingSoort**  
   Dit object definieert het type van de regeling, bijvoorbeeld algemene bijstand of specifieke ondersteuning.

8. **Ingeschreven Persoon (Client)**  
   Dit object vertegenwoordigt de persoon die recht heeft op inkomensondersteuning en mogelijk ook schuldhulpverlening ontvangt.

### **Relaties Tussen Entiteiten**
- Een *UitkeringsRun* bestaat uit één of meerdere *Componenten*.
- Een *Component* heeft altijd een *ComponentSoort*, die aangeeft wat voor soort bouwsteen het betreft.
- Een *Inkomensvoorziening* is opgebouwd uit één of meerdere *Componenten* en heeft altijd een relatie met één soort voorziening (*InkomensvoorzieningSoort*).
- Een ingeschreven persoon (client) heeft recht op één of meerdere regelingen (*Regeling*) binnen het sociaal domein.
- Elke regeling heeft een specifieke soort (*RegelingSoort*).

### Toepassing
Het informatiemodel ondersteunt gemeenten bij het uitvoeren van hun taken binnen de Participatiewet. Het biedt inzicht in hoe inkomensvoorzieningen worden opgebouwd, beheerd en gekoppeld aan cliënten, inclusief de administratieve processen rondom uitkeringen en regelingen. Hierdoor wordt consistente en efficiënte gegevensverwerking mogelijk gemaakt.

### Voorbeelden van Inkomensvoorzieningen
Het model omvat diverse inkomensvoorzieningen zoals:
- Bijstand
- Bijzondere bijstand
- IOAW (Wet inkomensvoorziening oudere en gedeeltelijk arbeidsongeschikte werkloze werknemers)
- IOAZ (Wet inkomensvoorziening oudere en gedeeltelijk arbeidsongeschikte zelfstandigen)

## GBI (Generieke Basisprocessen Inkomen)

Het [GBI (Generieke Basisprocessen Inkomen)](https://vngr-gbi.gitlab.io/ontologie-inkomen/) is een gestandaardiseerde set van processen en bijbehorende informatiestromen die binnen de Nederlandse sociale zekerheid wordt gebruikt om de uitvoering van inkomensregelingen te ondersteunen. De GBI-ontologie biedt een semantisch raamwerk waarin de relevante concepten, entiteiten en hun onderlinge relaties zijn vastgelegd. Dit zorgt ervoor dat verschillende systemen en processen binnen gemeenten op een uniforme manier kunnen communiceren en samenwerken. De ontologie van GBI is gericht op het structureren en standaardiseren van de informatie-uitwisseling, waardoor het beheer van inkomensprocessen efficiënter en consistenter verloopt. Dit maakt het mogelijk om gegevens uit verschillende bronnen te integreren en te hergebruiken, wat bijdraagt aan een hogere kwaliteit van dienstverlening. Het GBI is een ontologie die is vertaald naar een informatiemodel. Dit informatiemodel is in het GGM opgenomen, en gekoppeld aan generieke objecttypen zoals: personen, organisaties en zaken.

### GBI en GGM

Om de objecttypen en sub-domeinen voor Inkomen een plek te geven voor in de Sociaal domein een sub-domein ‘Inkomen’ aangemaakt. In dit sub-domein worden de volgende GBI-sub-domeinen opgenomen:

1.	Normafwijking;
2.	Reden aanvraag;
3.	Terug- en invordering;
4.	Diensten.

Deze sub-domeinen worden als volgt aan het GGM gekoppeld:

![Relatie tussen GBI en GGM][gbienggm]

### Normafwijking

Het onderdeel *Normafwijking* bricht zich op de registratie en afhandeling van situaties waarin een afwijking van de gestelde normen wordt geconstateerd bij inkomensvoorzieningen. De bijgevoegde afbeelding visualiseert de structuur van dit model en toont de relaties tussen verschillende objecttypen die betrokken zijn bij normafwijkingen. Hieronder volgt een gedetailleerde beschrijving van de elementen en hun onderlinge relaties.

![Normafwijking][normafwijking]

#### Objecttypen en Relaties
1. **Normafwijking**  
   Dit objecttype vormt het centrale punt in het model. Het representeert een situatie waarin een afwijking van een norm is vastgesteld. Een *Normafwijking* kan leiden tot één of meerdere maatregelen (*Maatregel*), afhankelijk van de aard en ernst van de afwijking.

2. **Maatregel**  
   Een *Maatregel* is een actie die wordt genomen naar aanleiding van een normafwijking. Het model onderscheidt verschillende soorten maatregelen:
   - **Afwijkende maatregel**: Dit is een specifieke maatregel die afwijkt van standaardprocedures.
   - **Maatregel op uitkering**: Dit type maatregel heeft direct invloed op de uitkering van de cliënt, zoals een inhouding of aanpassing.

   Elke maatregel heeft een directe relatie met een normafwijking, waarbij één normafwijking kan leiden tot maximaal één maatregel (*0..1*). Daarnaast generaliseert een maatregel zowel *Boete* als *Afwijkende maatregel*.

3. **Boete**  
   Een *Boete* is een specifieke vorm van maatregel die wordt opgelegd als sanctie voor een normafwijking. Dit kan bijvoorbeeld het gevolg zijn van fraude of het niet voldoen aan verplichtingen.

4. **Afwijkende maatregel**  
   Dit objecttype representeert maatregelen die niet standaard zijn en specifiek worden toegepast in uitzonderlijke situaties. Een afwijkende maatregel verwijst altijd naar een *Maatregel op uitkering*, waarmee het direct gekoppeld is aan de financiële aspecten van inkomensvoorzieningen.

5. **Maatregel op uitkering**  
   Dit objecttype beschrijft maatregelen die direct betrekking hebben op de uitkering zelf, zoals een korting of inhouding. Het heeft een 1-op-1-relatie met zowel *Afwijkende maatregel* als algemene maatregelen.

#### Relaties in het Model
De afbeelding toont duidelijk hoe de objecttypen met elkaar verbonden zijn:

- Een *Normafwijking* leidt tot maximaal één *Maatregel*.
- Een *Maatregel* generaliseert zowel *Boete* als *Afwijkende maatregel*, wat betekent dat deze objecttypen specifieke vormen van maatregelen zijn.
- Een *Afwijkende maatregel* verwijst altijd naar een *Maatregel op uitkering*, waarmee het verband tussen afwijkingen en financiële acties wordt gelegd.

### Reden aanvraag

Het onderdeel *Reden aanvraag* richt zich op de registratie en categorisatie van redenen waarom een cliënt een inkomensvoorziening aanvraagt. Dit model biedt een overzicht van de verschillende soorten redenen en hun onderlinge relaties, waardoor gemeenten deze informatie gestructureerd kunnen vastleggen en verwerken. Hieronder volgt een gedetailleerde beschrijving van de elementen zoals weergegeven in de bijgevoegde afbeelding.

![Reden aanvraag][redenaanvraag]

#### Objecttypen en Relaties

1. **Reden aanvraag**  
   Het centrale objecttype in het model is *Reden aanvraag*. Dit objecttype representeert de algemene reden voor een inkomensaanvraag. Het fungeert als een overkoepelend concept dat verschillende specifieke subtypen generaliseert.

2. **Levensonderhoud**  
    Dit subtype van *Reden aanvraag* beschrijft situaties waarin een cliënt inkomensondersteuning aanvraagt vanwege een gebrek aan middelen voor levensonderhoud. Het generaliseert meerdere specifieke redenen, zoals:

    1. **Gestopt betaald werk**: De cliënt heeft geen werk meer en vraagt inkomensondersteuning aan.  
    2. **Gestopte detentie**: De cliënt is vrijgekomen uit detentie en heeft behoefte aan ondersteuning.  
    3. **Gestopte uitkering**: Een eerdere uitkering is beëindigd, waardoor er opnieuw ondersteuning nodig is.  
    4. **Verbroken relatie**: De cliënt heeft te maken met een beëindiging van een relatie, wat financiële gevolgen heeft.  
    5. **Overleden partner**: Het overlijden van een partner leidt tot financiële nood.

3. **Ingang bijstandsuitkering**  
   Dit objecttype beschrijft de start van een bijstandsuitkering en bevat specifieke redenen die hieraan ten grondslag liggen.

4. **Reden afwijkende startdatum**  
    Dit objecttype representeert situaties waarin de startdatum van een uitkering afwijkt van het standaardproces. Het generaliseert specifieke gevallen zoals:

    1. **Wachten beslissing instantie**: De cliënt wacht op een besluit van een instantie.
    2. **Opname instelling**: De cliënt is opgenomen in een instelling, wat invloed heeft op de startdatum.
    3. **Wachten DigiD**: Er is vertraging door het ontbreken of activeren van DigiD.

5. **Andere reden verzoek**  
   Dit objecttype omvat overige redenen die niet onder de standaardcategorieën vallen, zoals vertrek uit een asielzoekerscentrum.

#### Relaties in het Model
De afbeelding toont hoe deze objecttypen met elkaar verbonden zijn:

- *Reden aanvraag* fungeert als generalisatie voor meerdere subtypen, waaronder *Levensonderhoud*, *Ingang bijstandsuitkering*, en *Reden afwijkende startdatum*.
- Elk subtype bevat specifieke redenen die verder gedetailleerd zijn, zoals gestopt werk, detentie of relatiebreuk.
- *Reden afwijkende startdatum* heeft relaties met specifieke procesgerelateerde situaties, zoals wachten op beslissingen of technische vertragingen.

### Terug- en invordering

Het onderdeel *Terug- en Invordering* richt zich op de processen en gegevens rondom het terugvorderen en invorderen van onterecht verstrekte inkomensvoorzieningen. Dit model biedt een gestructureerde weergave van de objecttypen en hun onderlinge relaties die nodig zijn om deze financiële processen effectief te beheren. Hieronder volgt een gedetailleerde beschrijving van de elementen zoals weergegeven in de bijgevoegde afbeelding.

![Terug- en invordering][terug]

#### Objecttypen en Relaties
1. **Vordering**  
   Het centrale objecttype in het model is *Vordering*. Dit representeert een financieel bedrag dat door de gemeente wordt teruggevorderd van een cliënt. Een vordering kan voortkomen uit verschillende situaties, zoals onterecht ontvangen uitkeringen of overtredingen van verplichtingen.

   - Een vordering bevat meerdere componenten, zoals *Rechtshandeling* en *Betaalcomponent*, die samen de administratieve afhandeling ondersteunen.
   - Daarnaast generaliseert een vordering specifieke subtypen, zoals *Verrekening*, *Afkoopsomvordering*, en *Rentvordering*.

2. **Rechtshandeling**  
   Dit objecttype beschrijft de juridische basis voor de vordering. Het kan bijvoorbeeld gaan om besluiten of overeenkomsten die de terugvordering rechtvaardigen.

3. **Betaalcomponent**  
   Een betaalcomponent is gekoppeld aan een vordering en beschrijft de betalingsspecificaties, zoals termijnen of bedragen.

4. **Verrekening**  
   Een vorm van vordering waarbij het verschuldigde bedrag wordt verrekend met andere financiële rechten van de cliënt, zoals toekomstige uitkeringen.

5. **Afkoopsomvordering**  
   Dit subtype representeert een vordering die wordt afgehandeld via een afkoopsom, waarbij een cliënt een overeengekomen bedrag betaalt om verdere verplichtingen af te kopen.

6. **Rentevordering**  
   Rentevorderingen worden toegepast wanneer rente verschuldigd is over het openstaande bedrag van de vordering.

7. **Krediethypotheekovereenkomst**  
   Dit objecttype beschrijft een overeenkomst waarbij een krediethypotheek wordt afgesloten als zekerheid voor terugbetaling van een vordering.

8. **Aflossingsplan**  
   Het aflossingsplan geeft aan hoe en wanneer een cliënt het verschuldigde bedrag zal terugbetalen. Het kan gekoppeld zijn aan meerdere vorderingen.

9. **Interventieverzoek**  
   Een interventieverzoek wordt ingediend wanneer aanvullende maatregelen nodig zijn om een vordering te innen, zoals juridische stappen.

10. **Debiteur**  
    De persoon (cliënt) die verantwoordelijk is voor het terugbetalen van de vordering wordt aangeduid als *Debiteur*. Dit objecttype legt relaties tussen de debiteur en alle relevante financiële processen.

#### Relaties in het Model
De afbeelding toont hoe deze objecttypen met elkaar verbonden zijn:

- Een *Vordering* bevat meerdere componenten, zoals *Rechtshandeling* en *Betalcomponent*.
- Subtypen zoals *Verrekening*, *Afkoopsomvordering*, en *Rentvordering* worden gegeneraliseerd door het centrale objecttype *Vordering*.
- Het aflossingsplan is gekoppeld aan zowel interventieverzoeken als specifieke betalingsafspraken.
- De debiteur heeft directe relaties met krediethypotheekovereenkomsten en aflossingsplannen.

### Dienstenmodel

Het *Dienstenmodel* biedt een gestructureerde weergave van de processen en objecttypen die betrokken zijn bij het leveren van diensten binnen het sociaal domein. Het model richt zich op de relaties tussen aanvragen, besluiten, rechten en voorwaarden die de basis vormen voor het verstrekken van voorzieningen. Hieronder volgt een gedetailleerde beschrijving van de elementen zoals weergegeven in de bijgevoegde afbeelding.

![Dienstenmodel][diensten]

#### Objecttypen en Relaties
1. **Aanvraag**  
    Het objecttype *Aanvraag* vormt het startpunt van het proces. Het representeert een verzoek van een cliënt om een dienst of voorziening te ontvangen. Een aanvraag leidt altijd tot een besluit.

2. **Besluit**  
    Een *Besluit* is het resultaat van een aanvraag en bevat informatie over de goedkeuring of afwijzing van een dienst. Het besluit initieert vervolgens een beschikking.

3. **Beschikking**  
    De *Beschikking* is een formeel document waarin het besluit wordt vastgelegd. Het bevat details over de toegekende rechten en voorwaarden.

4. **Recht**  
    Dit objecttype beschrijft het recht dat voortvloeit uit een beschikking. Het recht is gebaseerd op voorwaarden en vormt de grondslag voor het leveren van voorzieningen.

5. **Voorwaarde**  
    Een *Voorwaarde* specificeert de criteria waaraan voldaan moet worden om aanspraak te maken op een dienst. Voorwaarden kunnen bestaan uit uitsluitingsgronden, voorafgaande voorzieningen, of andere restricties.

6. **Leveringscomponent**  
    Dit objecttype beschrijft hoe een dienst wordt geleverd. Het omvat specifieke componenten zoals:
    1. **Leveringsspecificatie**: Details over hoe de voorziening wordt verstrekt.
    2. **Leveringsopdracht**: De opdracht voor het leveren van de dienst.

7. **Regeling**  
    De *Regeling* definieert de context waarin diensten worden verleend, zoals bijstand of bijzondere bijstand.

8. **Verstrekkingsvorm**  
    Dit objecttype beschrijft hoe een dienst wordt verstrekt, bijvoorbeeld in natura of als financiële ondersteuning.

9. **Uitsluitingsgrond**  
    Een uitsluitingsgrond is een specifieke voorwaarde die bepaalt wanneer iemand geen aanspraak kan maken op een voorziening.

10. **Voorafgaande voorziening**  
    Dit objecttype beschrijft eerder verleende voorzieningen die invloed hebben op het recht op nieuwe diensten.

#### Relaties in het Model
De afbeelding toont hoe deze objecttypen met elkaar verbonden zijn:

- Een *Aanvraag* leidt tot een *Besluit*, dat vervolgens resulteert in een *Beschikking*.
- Een beschikking bevat rechten, die gebaseerd zijn op voorwaarden.
- Voorwaarden generaliseren uitsluitingsgronden en voorafgaande voorzieningen.
- Leveringscomponenten, zoals leveringsspecificaties en opdrachten, zijn gekoppeld aan diensten en verstrekkingsvormen.
- Regelingen vormen de juridische basis voor het verstrekken van diensten.

[terug]: image/EAID_CE436DEE_AB15_4f23_B191_FA8A63FB488D.jpg "Terug- en invordering"
[gbienggm]: image/EAID_FD4BAB10_5D3E_4d14_8949_24CA09AC42A7.jpg "Relatie tussen GBI en GGM"
[normafwijking]: image/EAID_1818B773_1463_43c7_BACA_FEE391FE27CD.jpg "Normafwijking"
[redenaanvraag]: image/EAID_B87D7E99_417E_4b99_BEC1_B319BE85AECA.jpg "Reden aanvraag"
[diensten]: image/EAID_49670B34_2BC4_4972_BC7C_3F5793B27A73.jpg "Dienstenmodel"
[inkomenbasis]: image/EAID_9CEE3C86_9B9F_472f_A104_61FFC01DAC5A.jpg "Basismodel Inkomen"
