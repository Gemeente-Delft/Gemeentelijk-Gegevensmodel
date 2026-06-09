# Common Ground en het Gemeentelijk Gegevensmodel (GGM)

Binnen de gezamenlijke vernieuwing van het gemeentelijke informatielandschap werken de Vereniging van Nederlandse Gemeenten (VNG), gemeenten en leveranciers intensief samen aan een toekomstbestendige informatievoorziening. Binnen dit brede digitaliseringsdomein vormen **Common Ground (CG)** en het **Gemeentelijk Gegevensmodel (GGM)**  belangrijke bouwstenen.  

Waar Common Ground de architectonische principes, standaarden en technische randvoorwaarden voorschrijft voor een modern stelsel van componenten, levert het GGM de inhoudelijke, semantische invulling. Om de samenhang te versterken, dubbelingen te voorkomen en de gezamenlijke doorontwikkeling te versnellen, zijn het GGM en Common Ground nauwer gepositioneerd binnen **één samenhangend kader**. 

Hierbij is het GGM officieel erkend als de semantische standaard die de gegevensarchitectuur van Common Ground ondersteunt, terwijl Common Ground de randvoorwaarden biedt om de toepassing van het GGM te versnellen. De toekomstige regieorganisatie zal hierin fungeren als één centraal loket waar gemeenten terecht kunnen voor alle vragen over CG, GGM en andere collectieve digitaliseringsoplossingen.

---

## 1. De kern van de relatie: Structuur ontmoet Inhoud

De relatie tussen Common Ground en het GGM laat zich het best omschrijven als de relatie tussen de "hoe" en de "wat":

* **Common Ground** richt zich op de gezamenlijke ontwikkeling, standaardisatie en implementatie van een stelsel van softwarecomponenten, informatiemodellen en API’s. Het definieert *hoe* we met gegevens omgaan (loskoppelen van data en applicaties, bevragen bij de bron via API's).
* **Het GGM** vervult hierin een specialistische rol: het biedt een generiek, herbruikbaar open-source gegevensmodel dat structuur geeft aan gemeentelijke gegevens en domeinoverstijgend toepasbaar is. Het definieert *wat* die gegevens precies betekenen.

Als semantische standaard vormt het GGM de basis van de datalaag binnen Common Ground. Zonder Common Ground blijft het GGM een theoretisch model dat op traditionele wijze (in silo's) wordt geïmplementeerd. Zonder het GGM mist Common Ground de uniforme, gemeenschappelijke taal om de data-uitwisseling tussen applicaties en gemeenten vlekkeloos te laten verlopen.

---

## 2. Strategische Analyse: GGM vs. Common Ground

Hoewel beide initiatieven in elkaars verlengde liggen en elkaar versterken, zijn er specifieke accentverschillen in scope en opzet waar in de uitvoering rekening mee wordt gehouden:

| Aspect | Gemeentelijk Gegevensmodel (GGM) | Common Ground (CG) | Synthese & Analyse |
| :--- | :--- | :--- | :--- |
| **Doel** | Ontwikkelen van een generiek gemeentelijk gegevensmodel. | Realiseren van een stelsel van componenten en standaarden op basis van een gedeeld gegevensmodel. | Liggen in elkaars verlengde en sluiten uitstekend aan. |
| **Scope** | **Breder:** Alle gegevens binnen het gemeentelijk taakveld, inclusief bedrijfsvoering (Financiën, HR). | Gericht op gemeentespecifieke digitalisering. Bedrijfsvoering valt buiten de primaire scope. Focus ligt eerst op het domein dienstverlening. | Er is gerichte aandacht nodig voor de bredere scope van het GGM binnen het CG-stelsel. |
| **Doelgroepen** | Gemeenten, softwareleveranciers, architecten, data-analisten. | Gemeenten, softwareleveranciers, architecten, koploper-communities. | Sterke overlap in doelgroepen; GGM reikt door de bredere scope wel verder in de interne gemeentelijke organisatie. |
| **Architectuur** | Niet platformgebonden. | Vijf-laags CG-architectuur. | Het GGM vormt de logische en dragende invulling van de datalaag (Laag 2 en 3) van CG. |
| **Community** | Brede, operationeel actieve community met een hoge adoptiegraad. | Koploper-communities, primair gericht op het realiseren van concrete functionaliteit. | De samenhang tussen de functionele CG-communities en de GGM-community wordt actief versterkt. |
| **Implementatie** | Getrokken door de Expertgroep GGM, de community en softwareleveranciers. | Werkt aan een landelijke aansluitstrategie ondersteund door een centraal implementatieteam. | Overlappende strategieën bieden kansen voor directe, wederzijdse versterking. |
| **Timing** | Doel CvD: Landelijke toepassing bij alle gemeenten in ca. 2,5 jaar. | Doel programma: Implementatie platform dienstverlening bij alle gemeenten binnen 3 jaar. | Beide programma’s lopen synchroon en hanteren een vergelijkbaar, strak tijdspad. |

---

## 3. GGM binnen de Karakterisering van Componenten

Binnen de Common Ground-architectuur worden softwarecomponenten gecategoriseerd op basis van hun functie, herbruikbaarheid en positie in het stelsel (de *Karakterisering van de componenten*). Het GGM is de semantische standaard die de gegevensarchitectuur ondersteunt en zorgt voor de noodzakelijke structuur over deze verschillende componenten heen:

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

## 4. Doelstelling en Operationalisering

De gedeelde doelstelling is om gemeenten en leveranciers optimaal te ondersteunen bij de implementatie en verankering van Common Ground-initiatieven, met het GGM als centrale semantische standaard. Dit wordt gerealiseerd via drie concrete resultaten:
1. **Uitvoeren en vastleggen van een nulmeting** bij deelnemende gemeenten om de beginsituatie, ambities en specifieke knelpunten scherp te bepalen.
2. **Ontwikkelen van compacte, direct toepasbare hulpmiddelen** zoals richtlijnen en een praktische toolkit voor de praktijk.
3. **Borgen van de aansluiting** van het GGM op Common Ground-initiatieven, waaronder de platformdienstverlening en de karakterisering van componenten.

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