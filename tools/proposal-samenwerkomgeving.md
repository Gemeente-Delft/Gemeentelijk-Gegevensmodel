# Proposal Samenwerkomgeving ('s-Hertogenbosch): status en verwerkingsvoorstel voor v3.0.0

Notitie van 4 november 2026. Getoetst is `Proposal_Samenwerkomgeving.pdf` (Erik de Lepper, informatiearchitect
gemeente 's-Hertogenbosch, versie 01, januari/februari 2025, 17 objecttypen) tegen `v3.0.0/Gemeentelijk
Gegevensmodel.qea`, het GGM Cookbook (`docs/cookbook`, ontwerpregels m1 tot m7 en p1, p2, lijst ondersteunde
primitieve datatypes), de naamgevingsconventies van het GGM (*Naamgevingsconventies Gemeentelijk Gegevensmodel*,
2023: MIM-alternatief 2) en het Utrechtse *Conventiedocument datamodelleren* v0.2 (groepattribuutsoort
Adresaanduiding, naamgeving relaties).

## Samenvatting

- **Niet verwerkt.** In de .qea van v3.0.0 bestaat geen package en geen klasse Samenwerkomgeving. Geen van de
  17 voorgestelde objecttypen staat in het model. `Rol`, `Team` en `Taak` komen wel voor, maar als andere
  begrippen in Model Musea, Model HR, Model Jeugd en Wmo Generiek, Model Beheer Openbare Ruimte en Model
  Subsidies. Er is geen GitHub-issue, geen commit en geen documentatiepagina over het onderwerp.
- **Status in het proces.** Openbare consultatie van 13 mei tot 13 juni 2026 (infographic
  `~/Downloads/ggm-samenwerkomgeving.png`). In de 23e expertgroep van 12 augustus 2026 meldde Ashkan bij de
  openbare consultaties: "samenwerkingsomgeving, inkooporders, financiën en onderwijshuisvesting worden in de
  volgende release meegenomen". De reacties uit de consultatie staan niet in de repository en niet in de
  notities.
- **Inhoudelijk bruikbaar, in deze vorm niet opneembaar.** Elk objecttype heeft een technisch `ID`, de datatypes
  zijn geen MIM-datatypes (`char`, `int`, `float`, soms geen datatype), drie objecttypen hebben geen enkel
  attribuut, zes hebben geen definitie, namen staan in meervoud, de relatie `Lid is Werknemer` loopt horizontaal
  naar Model HR, en diagram en tekst lopen uiteen (`Samenwerkingsverband` tegenover `Team`, `Items` tegenover
  `Lijstitem`).
- **Voorstel.** Opnemen als eigen package `Samenwerkomgeving` onder `9 Interne Organisatie`, met 15 objecttypen
  en 1 enumeratie na de correcties uit hoofdstuk 3, met uitsluitend MIM-datatypes. Modelleren in Enterprise
  Architect (import van het package van Erik, daarna corrigeren), vervolgens documentatie, DDL en Linked Data
  opnieuw genereren. Geschat: 3 tot 5 uur modelleren en documenteren, los van de afstemming met de indiener.

## 1. Wat is gecontroleerd

| Bron | Zoekactie | Uitkomst |
|---|---|---|
| `v3.0.0/Gemeentelijk Gegevensmodel.qea` (`t_package`, `t_object`) | packages en klassen met *Samenwerk*, en de 17 namen uit het proposal | geen package; alleen naamgenoten `Rol` (Musea, HR), `Team` (Jeugd en Wmo Generiek), `Taak` (BOR, Subsidies) |
| `t_package` onder `9 Interne Organisatie` | de plek die het proposal noemt | `Organisatie-indeling` › `Model Organisatie` bevat alleen `Programma` en `Project` |
| `docs/`, `mkdocs.yml`, `tools/` | tekst *samenwerkomgeving*, *Teams*, *SharePoint* | niets |
| git-historie (alle branches) | commitboodschappen met *samenwerk* | niets |
| GitHub-issues (open en gesloten) | *samenwerkomgeving* | niets; eerdere proposals liepen via een issue met labels `Proposal` en `Expertgroep` (issue 4, Subsidies) |
| Obsidian (`01_Projects/GGM`) | consultatie, expertgroep | infographic 13 mei 2026; verslag 23e expertgroep 12 augustus 2026 |
| mail Inge van Creij-Maas, 29 april 2026 (in Obsidian sinds 4 november 2026) | afstemmingsoverleg | Erik de Lepper deelde in april 2026 "het bestand met de laatste versie" met Ashkan, die het nakeek en met Michiel Verhoef deelde; die versie is mogelijk nieuwer dan de PDF van januari 2025 die hier is verwerkt en moet ernaast worden gelegd |

## 2. Toetsing aan cookbook en conventies

| Regel | Bevinding in het proposal | Gevolg voor opname |
|---|---|---|
| m1 definities verplicht | ontbreken bij `Agenda-item`, `e-mail`, `Taak`; nietszeggend bij `Team` ("Team") en `Bestanden` ("Bestanden"); attribuut `Formaat` heeft als definitie "?" | definities opvragen bij de indiener of zelf opstellen |
| m3 datatypes uit de lijst ondersteunde datatypes | `char` zonder lengte, `int` voor een datum (`Chat.DatumCreatie`), `float` voor grootte, geen datatype bij `DatumCreatie`, `DatumLaatsteWijziging`, `DatumLaatstGebruikt`, `DatumMutatie` | vertalen naar de MIM-primitieven `CharacterString`, `Integer`, `Decimal`, `Boolean`, `Date`, `DateTime`, `URI`; lengte als metagegeven `Lengte` (zie 3.2) |
| m4 minstens één attribuut | `Agenda-item`, `e-mail` en `Taak` hebben geen attributen; `Chatbox` heeft alleen `ID` | attributen toevoegen of objecttype schrappen |
| m7 kardinaliteit verplicht | aanwezig aan beide zijden | in orde; leesrichting (`direction: Unspecified`) nog toevoegen |
| p1 alleen onderliggende modellen | `Lid is Werknemer` verwijst naar Model HR, een verticaal model op hetzelfde niveau | vervangen door `Medewerker` (Model Kern RGBZ); `Werknemer` is daar al een specialisatie van |
| geen technische sleutels (cookbook *uitbreiden*, veelgemaakte fout 1; besluit 17 december 2025 "ID weggooien") | elk objecttype heeft `ID: char` | alle `ID`-attributen vervallen; functionele sleutels (`URL`, `emailadres`, `naam`) blijven |
| naamgeving objecttypen: PascalCase, enkelvoud | `Bestanden`, `Items`, `e-mail`, `Agenda-item`, `Inhoudtype` | `Bestand`, `Lijstitem`, `Emailbericht`, `AgendaItem`, `Inhoudstype` |
| naamgeving attributen: camelCase, `datumXxx`, `indicatieXxx`, afkortingen in hoofdletters, geen spaties | `DatumCreatie`, `Hub site`, `Hoofdteam`, `URL`, `Type` | `datumCreatie`, `soort` (zie 3.2), `indicatieHoofdteam`, `URL`, `bestandstype` |
| naamgeving relaties: werkwoordsvorm in kleine letters, zoals in het model (`heeft verzuim`, `melder`) | `Aanmaker`, `heeft Site Collecties`, `is` | `aangemaakt door`, `heeft samenwerkomgevingen`, `is medewerker` |
| eenduidigheid diagram en tekst | diagram: `Samenwerkingsverband` (met `Hoofdteam`), `Items` (met bestandsattributen); tekst: `Team`, `Lijstitem` (met `Waarde`) | de tekst volgen, `indicatieHoofdteam` van het diagram meenemen |

## 3. Vertaling van het proposal naar het GGM

### 3.1 Package

`9 Interne Organisatie` › `Samenwerkomgeving` › `Diagram` en `Model Samenwerkomgeving`, met dezelfde tagged
values als de andere domeinpackages (`Release`, `Beheerder`, `Herkomst`, enzovoort) en stereotype
«Objecttype» op elke klasse. Het proposal wil het model onder `Organisatie-indeling`; zie keuze 1.

### 3.2 Datatypes

Alle attributen krijgen een MIM-datatype uit de lijst in `docs/cookbook/modelelementen.md`: `CharacterString`,
`Integer`, `Decimal`, `Boolean`, `Date`, `DateTime` en `URI`. De maximale lengte van een `CharacterString` komt
niet in de typenaam (dus geen `AN200`) maar in het MIM-metagegeven `Lengte`, zoals het model dat al doet bij de
klassen die `CharacterString` gebruiken (tagged value `Lengte` op het attribuut). Een enumeratie of
groepattribuutsoort wordt als type opgenomen door ernaar te verwijzen. Vertaling vanuit het proposal:

| Proposal | MIM |
|---|---|
| `char` (tekst) | `CharacterString`, met `Lengte` |
| `char` voor een webadres | `URI` |
| `int` of geen datatype bij een datum | `DateTime` (tijdstip) of `Date` (dag) |
| `float` (grootte in MB) | `Decimal` |
| `boolean` | `Boolean` |

### 3.3 Objecttypen en attributen

| Proposal | GGM | Attributen (naam : datatype, lengte) | Opmerking |
|---|---|---|---|
| Samenwerkomgeving | `Samenwerkomgeving` | `titel : CharacterString` (200), `beschrijving : CharacterString`, `URL : URI`, `datumCreatie : DateTime`, `datumLaatstGebruikt : Date`, `grootte : Decimal` (MB), `soort : CharacterString` (80) | `Hub site` is volgens de definitie "type samenwerkomgeving" en wordt `soort`; `Formaat` vervalt zolang de definitie "?" is; `ID` (site collectie) vervalt, `URL` is de functionele sleutel |
| Team / Samenwerkingsverband | `Team` | `naam : CharacterString` (200), `indicatieHoofdteam : Boolean`, `omschrijving : CharacterString` | naamgenoot in Model Jeugd en Wmo Generiek (zie keuze 2) |
| Kanaal | `Kanaal` | `naam : CharacterString` (200), `omschrijving : CharacterString` | |
| Chatbox | vervalt | | alleen `ID`; is 1-op-1 met `Kanaal` en met `Team`; `Chatbericht` hangt direct onder `Kanaal` (zie keuze 4) |
| Chat | `Chatbericht` | `datumCreatie : DateTime`, `datumLaatsteWijziging : DateTime`, `inhoud : CharacterString` | de definitie is "bericht van een teamlid", de naam volgt de definitie; `DatumCreatie : int` wordt `DateTime` |
| Lid | `Teamlid` | `naam : CharacterString` (200), `emailadres : CharacterString` (254), `organisatorischeEenheid : CharacterString` (200) | `Lid` alleen is te algemeen; `emailadres` is de functionele sleutel (de definitie van `ID` zegt dat al); lengte 254 zoals bij `Medewerker` |
| Rol | enumeratie `Teamrol` en objecttype `Teamlidmaatschap` | `Teamlidmaatschap`: `rol : Teamrol`, `datumToetreding : Date`; `Teamrol`: eigenaar, lid, gast | het proposal legt de rol los van de combinatie lid-team (twee n-op-m-relaties), waardoor niet vast te leggen is wie welke rol in welk team heeft; koppelobjecttype volgens het cookbook (relatieklasse als koppeltabelconstructie); zie keuze 3 |
| Mailbox | `Mailbox` | `emailadres : CharacterString` (254) | |
| e-mail | `Emailbericht` | `onderwerp : CharacterString` (200), `datumVerzonden : DateTime`, `afzender : CharacterString` (254) | geen attributen en geen definitie in het proposal |
| Agenda-item | `AgendaItem` | `onderwerp : CharacterString` (200), `datumTijdBegin : DateTime`, `datumTijdEinde : DateTime`, `locatie : CharacterString` (200) | idem |
| Taak | `Teamtaak` | `titel : CharacterString` (200), `status : CharacterString` (80), `datumGereed : Date` | idem; naamgenoot `Taak` in BOR en Subsidies (zie keuze 2) |
| Bibliotheek | `Bibliotheek` | `naam : CharacterString` (200) | |
| Bestanden | `Bestand` | `naam : CharacterString` (255), `bestandstype : CharacterString` (100, mimetype), `grootte : Decimal` (MB), `datumCreatie : DateTime`, `datumLaatsteWijziging : DateTime` | enkelvoud; `DatumMutatie` wordt `datumLaatsteWijziging`, gelijk aan `Chatbericht` |
| Lijst | `Lijst` | `naam : CharacterString` (200) | |
| Inhoudtype | `Inhoudstype` | `naam : CharacterString` (200) | Nederlandse spelling met tussen-s |
| Kolom | `Kolom` | `naam : CharacterString` (200), `datatype : CharacterString` (80) | |
| Lijstitem / Items | `Lijstitem` | `waarde : CharacterString` | tekst volgen; zie keuze 5 over de lijststructuur |

### 3.4 Relaties

| Bron | Relatie | Doel | Kardinaliteit | Opmerking |
|---|---|---|---|---|
| Team | heeft samenwerkomgevingen | Samenwerkomgeving | 0..1 – 1..* | was "heeft Site Collecties" |
| Team | heeft mailbox | Mailbox | 0..1 – 1 | |
| Samenwerkomgeving | heeft kanalen | Kanaal | 1 – 1..* | |
| Samenwerkomgeving | heeft bibliotheken | Bibliotheek | 1 – 0..* | |
| Samenwerkomgeving | heeft lijsten | Lijst | 1 – 0..* | |
| Kanaal | bevat chatberichten | Chatbericht | 1 – 0..* | vervangt Chatbox |
| Chatbericht | geschreven door | Teamlid | 0..* – 1 | was "schrijver" |
| Teamlidmaatschap | van teamlid | Teamlid | 0..* – 1 | vervangt Rol–Lid |
| Teamlidmaatschap | in team | Team | 0..* – 1 | vervangt Rol–Team |
| Teamlid | is medewerker | Medewerker (Model Kern RGBZ) | 0..1 – 0..1 | was `Werknemer` (Model HR); externe leden hebben geen medewerker |
| Mailbox | heeft emailberichten | Emailbericht | 1 – 0..* | |
| Mailbox | heeft agenda-items | AgendaItem | 1 – 0..* | |
| Mailbox | heeft taken | Teamtaak | 1 – 0..* | |
| Teamtaak | toegewezen aan | Teamlid | 0..* – 0..1 | nieuw, volgt uit de betekenis van een taak |
| Bibliotheek | heeft bestanden | Bestand | 1 – 0..* | |
| Bestand | aangemaakt door | Teamlid | 0..* – 1 | was "Aanmaker" |
| Bestand | gewijzigd door | Teamlid | 0..* – 0..1 | laatste wijziger kan ontbreken |
| Lijst | heeft inhoudstypen | Inhoudstype | 1..* – 1..* | |
| Lijst | heeft items | Lijstitem | 1 – 0..* | |
| Inhoudstype | heeft kolommen | Kolom | 0..* – 1..* | |
| Kolom | heeft waarden | Lijstitem | 1..* – 0..* | |

Optioneel: `Samenwerkomgeving` *ondersteund door* `Applicatie` (Model ICT, horizontaal) 0..* – 0..1, zodat de
omgeving (Teams, SharePoint, Nextcloud) aan de applicatieregistratie hangt. Zie keuze 6.

## 4. Uitvoering

Uitgevoerd op 4 november 2026 met `tools/fixes/add_samenwerkomgeving.py` volgens de aanbevolen keuzes uit hoofdstuk 5:
eigen package `Samenwerkomgeving` onder `9 Interne Organisatie`, enumeratie `Teamrol` met `Teamlidmaatschap`,
`Chatbox` vervallen, `Teamlid` met relatie naar `Medewerker`; 15 objecttypen, 21 relaties en het diagram
`Samenwerkomgeving`. De relatie naar `Applicatie` (keuze 6) is niet opgenomen. Stap 1 en 2 hieronder staan nog
open: de definities zijn door ons opgesteld en moeten door Erik worden bevestigd.

1. **Afstemmen met de indiener.** Eerst bij Ashkan de versie opvragen die Erik in april 2026 deelde en vergelijken met de verwerkte PDF (versie 01, januari 2025). Daarna Erik de Lepper vragen om (a) de ontbrekende definities en de betekenis van
   `Formaat` en `Hub site`, (b) een XMI-export van zijn EA-package `Model Samenwerkomgeving` (de PDF is uit EA
   gegenereerd, elementen aangemaakt 15 januari 2025), (c) akkoord op de vertaling in hoofdstuk 3.
2. **Reacties uit de consultatie** ophalen bij Ashkan en verwerken in deze notitie.
3. **GitHub-issue** aanmaken, *Proposal Samenwerkomgeving*, labels `Proposal` en `Expertgroep`, met verwijzing
   naar de consultatie en het besluit van 12 augustus 2026; de verwerking commit met `#nummer`.
4. **Modelleren in EA** op `v3.0.0/Gemeentelijk Gegevensmodel.qea`, met vooraf een kopie zoals bij issue 53 en
   57 (`.qea.backup-<datum>-voor-samenwerkomgeving`). XMI van Erik importeren in een tijdelijk package, naar
   `9 Interne Organisatie` verplaatsen en de correcties uit hoofdstuk 3 aanbrengen (namen, MIM-datatypes met
   `Lengte`, ID's weg, definities); zonder XMI handmatig opbouwen. Diagram `Samenwerkomgeving` in het package
   `Diagram`. Scripten via sqlite (zoals `tools/fixes/fix_issue_57.py`) is voor een nieuw package met diagram af te
   raden.
5. **Documentatie.** Domeinpagina `docs/domeinen/samenwerkomgeving.md` naar het voorbeeld van `ict.md` en
   `hr.md`; `mkdocs.yml` aanvullen onder *Interne organisatie* (domeinen en definities); daarna
   `task generate:docs` en `task publish:local`. DDL opnieuw genereren met de codegeneratietemplates; Linked Data
   met `task generate:lod`; vertalingen met `task generate:translations`.
6. **Afronden.** Issue sluiten, indiener en expertgroep informeren, wiewatstatus bijwerken.

## 5. Keuzes bij Arjen

1. **Plaats in de boom.** Eigen package `Samenwerkomgeving` naast ICT en HR (aanbevolen: elk domein heeft zo
   een eigen `Diagram` en `Model`-package, en de omgeving is geen organisatie-indeling), of onder
   `Organisatie-indeling` zoals het proposal en de consultatie het noemden.
2. **Naamgenoten.** `Team` en `Taak` bestaan al elders. Het model staat gelijknamige klassen in verschillende
   packages toe en de LOD-IRI's lopen langs het packagepad, maar de todo *dubbele voorkomens objecttypen* speelt
   nog. Voorstel: `Team` houden (het is de term van de indiener en van de software), `Taak` als `Teamtaak`,
   `Rol` als enumeratie `Teamrol`.
3. **Rol.** `Teamlidmaatschap` met enumeratie (aanbevolen) of het objecttype `Rol` met de twee relaties uit het
   proposal, waarmee rol per team niet vast te leggen is.
4. **Chatbox.** Schrappen (aanbevolen) of houden met een attribuut `naam`.
5. **Lijststructuur.** `Lijst`, `Inhoudstype`, `Kolom` en `Lijstitem` beschrijven het metamodel van
   SharePoint-lijsten, geen gemeentelijk gegeven. Overnemen zoals geconsulteerd, of terugbrengen tot `Lijst` met
   `Inhoudstype` en de rest aan de implementatie laten.
6. **Relatie naar Model ICT** (`Applicatie`) wel of niet opnemen.
7. **Release.** Opnemen in v3.0.0 als Erik de definities tijdig levert; anders v3.1.0. "De volgende release" uit
   het verslag van 12 augustus kan beide betekenen, bij Ashkan na te vragen.
