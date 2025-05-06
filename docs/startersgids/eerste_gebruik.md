# GGM Startersgids: Eerste Gebruik
## Werken met het GGM
Na de installatie van het GGM en Enterprise Architect ben je klaar om de eerste stappen te zetten in het daadwerkelijk gebruiken van het model. Dit document begeleidt je bij de eerste toepassingen van het GGM.

## Van informatievraag naar implementatie
Om het GGM effectief te gebruiken, is het belangrijk om te begrijpen hoe je van een informatievraag naar een implementatie komt. Laten we een concreet voorbeeld nemen:

### Casus: Het aantal lopende uitkeringen per maand
Voor uitkeringen moeten we kijken naar het model voor Participatie binnen het GGM. Een uitkering wordt in het GGM gedefinieerd als een 'InkomensVoorziening' - een regeling die zorg draagt voor een inkomen conform de landelijke wetgeving[3].

#### Stap 1: Identificeer de relevante GGM-entiteiten
In ons voorbeeld hebben we de volgende logische entiteiten nodig:
- InkomensVoorziening
- InkomensVoorzieningSoort
- Client[3]

#### Stap 2: Begrijp de attributen en relaties
Bijvoorbeeld, een InkomensVoorziening heeft attributen zoals:
- Startdatum
- Einddatum
- Soort uitkering
- Soort uitkeringregeling[3]

#### Stap 3: Mapping naar brongegevens
Je moet identificeren waar in je brondata (bijvoorbeeld Suite voor Sociaal Domein van Centric of Civision van PinkRoccade) deze gegevens worden opgeslagen[3].

De bron bevat attributen zoals datum van start en einde van de uitkering, soort uitkering, soort uitkeringregeling, etc. Deze moeten gemapped worden naar het GGM[3].

## Mappings maken of hergebruiken
Een cruciale stap bij het implementeren van het GGM is het maken van mappings: het vertalen van de gegevens uit je bronapplicaties naar de structuur van het GGM[3].

### Opties voor het verkrijgen van mappings:
#### Optie 1: Vraag leverancier om een mapping
Met name bij de aanschaf van nieuwe software heb je de mogelijkheid om richting een leverancier wensen en zelfs eisen te stellen. Er zijn al gemeenten die bij een marktconsultatie vragen naar de mogelijkheden om de data aan te leveren conform het GGM[3].

Vanuit de GGM expertgroep hebben we ook contact gehad met diverse leveranciers die geïnteresseerd zijn om hun data te gaan aanleveren in de vorm van het GGM. Dus ook al heb je geen aanbesteding, mogelijk kan je bestaande leverancier de data in de toekomst ook aanleveren conform het GGM[3].

#### Optie 2: Kijk of collega-gemeenten een mapping hebben
Op de Pleio pagina van het GGM vind je een mapje 'Mappings'. Hierin zit een bestand 'wie, wat, status'. Hierin kan je opzoeken welke gemeente bezig is geweest met het maken van een mapping van welke applicatie[3].

> LET OP: Elke gemeente doet uiteraard zijn best om de mapping zo goed mogelijk te doen. Maar wij gaan wel uit van het principe 'samen sta je sterker'. Er worden geen garanties gegeven over de juistheid van de mappings. Maar bovenal worden gemeenten die van de mappings gebruik maken van harte uitgenodigd (en voel dit ook gerust als een verplichting) om aanvullingen of verbeteringen terug te koppelen aan de aanleverende gemeente[3].

#### Optie 3: Mapping zelf maken
Als er nog geen mapping voorhanden is dan kan je zelf aan de slag. Er zijn dan twee scenario's[3]:

1. **Het onderwerp/domein is in het GGM opgenomen**  
   Op Pleio is in de map 'mappings' een bestand opgenomen dat heet 'Mapping-Template'. We willen iedereen verzoeken om dit bestand te gebruiken om je eigen mapping in vast te leggen. Op deze manier kan je andere gemeenten ook weer vooruit helpen in de toekomst[3].

2. **Het onderwerp is niet in het GGM opgenomen**  
   Mocht je een onderwerp hebben dat nog niet in het GGM is opgenomen, en je hebt er over nagedacht hoe dit wel in het GGM zou kunnen passen, stuur het naar de GGM expertgroep. Dan kijken wij hoe het opgenomen kan worden[3].

## Van GGM naar rapporten en dashboards
Na het implementeren van het GGM kunnen de gegevens worden gebruikt voor rapportages en dashboards[3].

### Architectuur opties:
#### Simpele oplossing
De meest simpele manier zou kunnen zijn om de transformatie van brondatamodel naar de tabellen van het GGM te doen in de brondatabase. Dat zou bijvoorbeeld kunnen met views. Deze views zou dan weer input kunnen zijn in een BI-tool. In de BI-tool transformeer je die input weer naar een stermodel[3].

#### Complexere oplossing
Een wat complexere oplossing is natuurlijk de inzet van een datawarehouse of dataplatform. Hier zijn vele verschillende technieken en structuren mogelijk. De meest klassieke vorm heeft drie lagen (STG, ODS, DM) waarbij in de middelste laag ook historie wordt opgebouwd. In de context van het GGM zou bijvoorbeeld ook de Operational datastore gevormd kunnen zijn volgens Het GGM[3].

Voor de opbouw van een datawarehouse zijn vele varianten denkbaar:
- ODS kan ook een DataVault zijn
- STG kan ook historie opslaan
- Er zijn ook vele manieren en tools voor Datawarehouse Automation
- Het GGM kan ook tot uiting komen in een extra laag[3]
