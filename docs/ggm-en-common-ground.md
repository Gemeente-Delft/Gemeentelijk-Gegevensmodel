# Common Ground en het Gemeentelijk Gegevensmodel (GGM)

Binnen de gezamenlijke vernieuwing van het gemeentelijke informatielandschap werken de Vereniging van Nederlandse Gemeenten (VNG), gemeenten en leveranciers intensief samen aan een toekomstbestendige informatievoorziening. Binnen dit brede digitaliseringsdomein vormen **Common Ground (CG)** en het **Gemeentelijk Gegevensmodel (GGM)**  belangrijke bouwstenen.  

Waar Common Ground de architectonische principes, standaarden en technische randvoorwaarden voorschrijft voor een modern stelsel van componenten, levert het GGM de inhoudelijke, semantische invulling. Om de samenhang te versterken, dubbelingen te voorkomen en de gezamenlijke doorontwikkeling te versnellen, zijn het GGM en Common Ground nauwer gepositioneerd binnen **één samenhangend kader**. 

Hierbij is het GGM officieel erkend als de semantische standaard die de gegevensarchitectuur van Common Ground ondersteunt, terwijl Common Ground de randvoorwaarden biedt om de toepassing van het GGM te versnellen. De toekomstige regieorganisatie zal hierin fungeren als één centraal loket waar gemeenten terecht kunnen voor alle vragen over CG, GGM en andere collectieve digitaliseringsoplossingen.

---

## 1. Context en Ambitie: Richting een Verplichte Standaard

Het GGM heeft inmiddels een stevig fundament gelegd binnen de gemeentelijke wereld. Met een vertegenwoordiging van ruim 63% van alle Nederlandse gemeenten binnen de community – waaronder meer dan 88% van de grote en middelgrote gemeenten – en actieve toepassing door meer dan 100 gemeenten, is het model een bewezen succes. Ook softwareleveranciers omarmen het GGM als referentie voor datalevering.

Vanwege dit succes heeft het College van Dienstverleningszaken (CvD) het GGM voorgedragen als een **‘pas toe of leg uit’**-standaard. De strategische ambitie is helder en ambitieus:

* **Opschaling:** Binnen 2,5 jaar moet het gebruik van het GGM worden uitgebreid naar *alle* Nederlandse gemeenten.

* **Statusverhoging:** Het CvD beoogt de status van het GGM binnen deze periode te verhogen naar **'verplicht'**, waarmee ook de gegevenslaag van Common Ground definitief wordt verstevigd.

* **Wederzijdse versnelling:** De brede toepassing en naamsbekendheid van het GGM worden actief benut om de landelijke uitrol van Common Ground te versnellen, aangezien het programma Common Ground een vergelijkbaar tijdspad hanteert om binnen 3 jaar het platform dienstverlening bij alle gemeenten te implementeren.

---

## 2. Inbedding in de Common Ground Data-architectuur

Om te begrijpen hoe het GGM functioneert binnen Common Ground, moeten we kijken naar de fundamenten van de **Common Ground Data-architectuur**. Common Ground breekt met het traditionele model waarbij data en applicatielogica met elkaar verweven zijn in gesloten silo's. De data-architectuur rust op drie leidende principes waarin het GGM de operationele invulling vormt:

### Scheiding van Data en Applicatie
Binnen Common Ground bezitten applicaties geen eigen, afgesloten database meer voor gedeelde gegevens. Data leeft in onafhankelijke bronregistraties.

* **De rol van het GGM:** Om te voorkomen dat elke losgekoppelde database een eigen dialect spreekt, fungeert het GGM als het universele, logische datamodel. Het dwingt een uniforme structuur af voor deze losgekoppelde databronnen, zodat applicaties moeiteloos bovenop verschillende databronnen kunnen functioneren.

### Bevragen bij de Bron (Geen data-duplicatie)
Gegevens worden niet langer gekopieerd, gesynchroniseerd of via zware ETL-pipelines (Extract, Transform, Load) overgezet naar datawarehouses voor dagelijks gebruik. Applicaties bevragen de data realtime en direct bij de rechthebbende bron via API's.

* **De rol van het GGM:** Het GGM levert het gestandaardiseerde informatiemodel (de semantiek) voor deze API-koppelingen. Wanneer een applicatie via een API een 'geboortedatum' of 'vastgoedobject' opvraagt, zorgt het GGM ervoor dat de structuur en betekenis van deze velden overal exact gelijk zijn. Het elimineert de noodzaak voor complexe datatransformaties tussen systemen.

### Gegevensminimalisatie en Privacy-by-Design
Applicaties krijgen via fijnmazige autorisatie alleen toegang tot de specifieke data-attributen die strikt noodzakelijk zijn voor de uitvoering van hun specifieke processtap.

* **De rol van het GGM:** Omdat het GGM data op een sterk gestructureerde, genormaliseerde manier modelleert (opgedeeld in duidelijke entiteiten en attributen), stelt het API-ontwikkelaars in staat om zeer fijnmazige (attribuut-niveau) filters en autorisaties in te richten. Men vraagt niet langer een heel dossier op, maar puur het specifieke GGM-attribuut dat nodig is.

---

## 3. GGM en de Karakterisering van Componenten

Binnen de Common Ground-architectuur worden softwarecomponenten gecategoriseerd op basis van hun functie, herbruikbaarheid en positie in het stelsel (de *Karakterisering van de componenten*). Het GGM is de semantische standaard die deze gegevensarchitectuur ondersteunt en zorgt voor de noodzakelijke structuur over deze verschillende componenten heen:

### Kerncomponenten (Generieke functies)
Dit zijn de landelijke of gemeenschappelijke basiscomponenten (zoals Open Zaak of Haal Centraal API's) die procesonafhankelijk zijn en puur gericht zijn op data-opslag en -ontsluiting bij de bron (Laag 2 en 3). 

* **De GGM-link:** Het GGM levert voor deze kerncomponenten de gestandaardiseerde definities voor objecten en attributen. Hierdoor sluiten de API-specificaties van verschillende kerncomponenten naadloos op elkaar aan.

### Specifieke Toepassingscomponenten (Taakveld-applicaties)
Dit zijn de applicaties aan de 'buitenkant' van de architectuur (Laag 4 en 5) waarmee ambtenaren of inwoners werken, specifiek ingericht voor één taakveld. Omdat het GGM een *domeinoverstijgende* scope heeft, dekt het ook taakvelden af die (nog) buiten de directe focus van het CG-platform dienstverlening vallen (zoals interne bedrijfsvoering).

* **De GGM-link:** Dankzij het brede karakter van het GGM kunnen ook specifieke toepassingen buiten het primaire CG-domein via gestandaardiseerde koppelvlakken communiceren met de kerncomponenten, zonder dat zij een eigen, afwijkende datastructuur hoeven af te dwingen.

### Koppelcomponenten en Integratiediensten
Componenten die zorgen voor de veilige routering en transformatie van gegevensstromen tussen bronnen en afnemers (bijvoorbeeld binnen de platformdienstverlening).

* **De GGM-link:** Het GGM biedt de universele taal. Koppelcomponenten gebruiken het GGM als referentiekader om data van legacy-systemen te vertalen naar moderne Common Ground-API's.

---

## 4. Strategische Analyse: GGM vs. Common Ground

Hoewel beide initiatieven in elkaars verlengde liggen en elkaar versterken, zijn er specifieke accentverschillen in scope en opzet waar in de uitvoering rekening mee wordt gehouden:

| Aspect | Gemeentelijk Gegevensmodel (GGM) | Common Ground (CG) | Synthese & Analyse |
| :--- | :--- | :--- | :--- |
| **Doel** | Ontwikkelen van een generiek gemeentelijk gegevensmodel. | Realiseren van een stelsel van componenten en standaarden op basis van een gedeeld gegevensmodel. | Liggen in elkaars verlengde en sluiten uitstekend aan. |
| **Scope** | **Breder:** Alle gegevens binnen het gemeentelijk taakveld, inclusief bedrijfsvoering (Financiën, HR). | Gericht op gemeentespecifieke digitalisering. Bedrijfsvoering valt buiten de primaire scope. Focus ligt eerst op het domein dienstverlening. | Er is gerichte aandacht nodig voor de bredere scope van het GGM binnen het CG-stelsel. |
| **Doelgroepen** | Gemeenten, softwareleveranciers, architecten, data-analisten. | Gemeenten, softwareleveranciers, architecten, koploper-communities. | Sterke overlap in doelgroepen; GGM reikt door de bredere scope wel verder in de interne gemeentelijke organisatie. |
| **Architectuur** | Niet platformgebonden. | Vijf-laags CG-architectuur (met focus op ontkoppelde data-architectuur). | Het GGM vormt de logische en dragende invulling van de datalaag (Laag 2 en 3) van CG. |
| **Community** | Brede, operationeel actieve community met een hoge adoptiegraad. | Koploper-communities, primair gericht op het realiseren van concrete functionaliteit. | De samenhang tussen de functionele CG-communities en de GGM-community wordt actief versterkt. |
| **Implementatie** | Getrokken door de Expertgroep GGM, de community en softwareleveranciers. | Werkt aan een landelijke aansluitstrategie ondersteund door een centraal implementatieteam. | Overlappende strategieën bieden kansen voor directe, wederzijdse versterking. |
| **Timing** | Doel CvD: Landelijke toepassing bij alle gemeenten in ca. 2,5 jaar. | Doel programma: Implementatie platform dienstverlening bij alle gemeenten binnen 3 jaar. | Beide programma’s lopen synchroon en hanteren een vergelijkbaar, strak tijdspad. |

---

> **Conclusie:** De inhoudelijke overlap en de synergie in aanpak tussen het GGM en Common Ground zijn groot. Door deze krachten te bundelen binnen één samenhangend kader, verhogen we de eenduidigheid in de markt, voorkomen we verwarring en versnellen we de realisatie van een modern, interoperabel gemeentelijk informatielandschap.

--- 

## 5. De Voordelen van de Synergie

Wanneer gemeenten en leveranciers deze samenhangende aanpak omarmen, levert dit directe strategische en operationele voordelen op:

* **Geen vendor lock-in:** Omdat het datamodel (GGM) openbaar, leverancieronafhankelijk en gestandaardiseerd is, kunnen gemeenten eenvoudiger wisselen van applicatieleverancier. De data blijft immers gestructureerd volgens de open standaard en is toegankelijk via Common Ground API's.
* **Eenmalige opslag, meervoudig gebruik:** Het GGM brengt data uit verschillende gemeentelijke domeinen logisch met elkaar in verband. Common Ground zorgt ervoor dat deze data veilig en direct bij de bron aangeroepen kan worden, zonder dat er onnodige kopieën of schaduwadministraties ontstaan.
* **Snellere innovatie:** Ontwikkelaars die applicaties bouwen voor gemeenten hoeven niet telkens zelf het wiel uit te vinden wat betreft de datastructuur. Het GGM levert de kant-en-klare semantiek, Common Ground levert de integratiestandaarden en de platformdienstverlening.

---

> **Kortom:** Het GGM geeft de concrete, inhoudelijke en specialistische invulling aan de Common Ground-filosofie. Door de krachten te bundelen in duidelijke richtlijnen, een gedeelde toolkit en gerichte actielijnen, bouwen gemeenten en leveranciers samen aan een solide fundament voor gegevensuitwisseling. Dit stelt gemeenten in staat om daadwerkelijk de regie op hun eigen data te pakken.
