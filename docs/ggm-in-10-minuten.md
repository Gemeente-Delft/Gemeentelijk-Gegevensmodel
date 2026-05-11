# Ontdek het GGM in 10 minuten

> **Begrijp de kracht van één taal voor de hele gemeente.**

Welkom! Je hebt geen technische achtergrond nodig om te begrijpen waarom het Gemeentelijk Gegevensmodel (GGM) essentieel is voor jouw gemeente. In 10 minuten leggen we de essentie uit.

## Het probleem: De digitale spraakverwarring
Gemeenten maken gebruik van een groot aantal verschillende applicaties, ketens en databronnen. 
Het gevolg? Data over dezelfde inwoner of hetzelfde gebouw staat overal anders gedefinieerd, mappings moeten per project opnieuw ontworpen worden en rapportages en beleidsanalyses zijn niet eenduidig en moeilijk reproduceerbaar. Dit maakt datagedreven werken traag, foutgevoelig en duur.

## De oplossing: Eén blauwdruk
Het GGM is de 'universele stekkerdoos'. Het is een afspraak over hoe we informatie benoemen en met elkaar verbinden. Het vormt één semantisch vertrekpunt: een gemeenschappelijke set definities en relaties die domeinoverstijgend en herbruikbaar is, en die aansluit bij bestaande standaarden.

Het GGM biedt een uniforme datastructuur die onafhankelijk is van de organisatorische inrichting van een gemeente. 
Of taken nu intern worden uitgevoerd of zijn uitbesteed, het model zorgt voor eenduidige definities en uitwisselbaarheid van gegevens. De indeling van beleidsterreinen is gebaseerd op de [IV3-taakvelden](https://www.rijksoverheid.nl/onderwerpen/financien-gemeenten-en-provincies/uitwisseling-financiele-gegevens-met-sisa-en-iv3/informatie-voor-derden-iv3).

> Belangrijk: het GGM biedt een **logisch** model. Jij vertaalt dit naar de gewenste **technische** implementatie (zoals tabellen, JSON Schema, API’s of RDF) passend bij jouw toepassing.

### Opbouw Gemeentelijk Gegevensmodel

Het GGM kent een gelaagde opbouw, waarbij verschillende objecttypen over beleidsdomeinen heen zoveel mogelijk zijn ontkoppeld. Alleen objecttypen in de onderste lagen van het model worden gebruikt door de bovenliggende onderdelen.

<p>
  <img src="/docs/image/GelaagdheidDomeinen.jpg" alt="gelaagdheid_domeinen" />
</p>


Het gegevensmodel is uitgewerkt in een aantal verticale beleidsdomeinen en 4 horizontale beleidsdomeinen. 
De horizontale delen (Kern, Financiën, ICT en Dienstverlening) vormen de basis van het gegevensmodel, waarop de verticale delen voortbouwen. De Kern bestaat uit **RSGB en RGBZ**, die de gegevensdefinities bevatten die zoals die gelden voor de basisregistraties (RSGB) en zaakgericht werken (RGBZ).  

Er is **ontkoppeling** tussen de verschillende (sub)domeinen nagestreefd, doordat in de gegevensdefinities van het gegevensmodel (sub)domeinen alleen definities uit onderliggende (sub)domeinen gebruiken. Zo gebruiken alle (sub)domeinen gegevensdefinities uit Kern en kunnen alle verticale (sub)domeinen gegevensdefinities gebruiken uit de 4 horizontale modellen.

Waar relevant worden **domein- en ketenstandaarden** toegepast (bijv. iWmo/iJw, IMBOR, Suwi en omgevingswet- standaarden). Het GGM positioneert deze standaarden zodanig dat begrippen **traceerbaar** zijn naar bronkaders en dat hergebruik maximaal is.

### Wat levert het jou op? 

| *Voordeel* | *Impact* |
|----------|--------|
| **Interoperabiliteit** | Alle systemen kunnen direct integreren op één standaard |
| **Eenduiding** | Dezelfde gegevensdefinitie overal, geen conflicten |
| **Data-gedreven beleid** | Snelle rapportage en inzichten in plaats van handmatig werk |
| **Vendor onafhankelijkheid** | Leverancierwisseling zonder dataverlies of miljoenen migratiekosten |
| **Toekomstvast** | Nieuwe systemen aansluiten kost maanden, niet jaren |
| **Semantische verbanden** | Automatische koppeling tussen gerelateerde gegevens |
| **Snellere inzichten** | Geen weken meer wachten op een data-analist die handmatig tabelletjes koppelt. |
| **Lagere kosten** | Doordat we standaarden delen met 150+ gemeenten, hoeven we het wiel niet 342 keer uit te vinden. |

## De volgende stap
- **Ben je een besluitvormer of beleidsadviseur?** Bekijk dan onze [Praktijkvoorbeelden]() uit andere gemeenten. 
- **Ben je degene die de knoppen moet bedienen?** Ga dan direct naar [Snel van start](snel-van-start.md).