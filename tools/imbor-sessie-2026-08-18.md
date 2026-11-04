# IMBOR in het GGM: reconstructie van de sessie van 18 augustus 2026

Reconstructie van 4 november 2026, op basis van drie bronnen:

1. **Het oorspronkelijke gesprek.** Dit is de Cowork-taak *IMBOR database optimization* op claude.ai:
   <https://claude.ai/cowork/cse_01HBrzEW74r6c8zVAeUCzKkc>. De taak draaide via Claude Desktop
   (macOS) in een Linux-sandbox. Daarom staat er geen lokaal transcript in `~/.claude`, en is
   `IMBOR 2025 geoptimaliseerd.qea` geschreven met SQLite 3.45.1. De sandbox kan maximaal 20 MB per
   bestand naar de Mac schrijven en de chat neemt maximaal 30 MB per bestand. Dat verklaart de
   transportdelen `_to_delete/mixdeel_aa` t/m `ac`. De opdrachten en scripts zelf staan ingeklapt in de
   stappen van die taak; ze zijn niet uitgelezen.
2. **Een tweede chat van dezelfde dag**, *IMBOR overerving en klassenconflicten*
   (<https://claude.ai/chat/94132c7a-ea22-49e0-9a84-f91a63553dc4>). Daarin staat de mail aan Michiel
   over overerving en conflicten. Zie §7.
3. **De opgeleverde bestanden** in
   `~/kDrive/Projecten/Delft/Delft Gemeentelijk Gegevensmodel/Ontwikkeling/IMBOR/`. De cijfers zijn
   opnieuw op de .qea-bestanden nageteld en kloppen met het gesprek.

## 1. Aanleiding

| Datum | Gebeurtenis | Bron |
|---|---|---|
| 13 nov 2025 | Overleg *IMBOR en MIM* met Michiel: de deploy wordt MIM-compliant. Actie: een GGM-deploytaak die automatisch "verMIMt" (afgerond 2 dec 2025). | Obsidian, `IMBOR en MIM Vergadering GGM-13 November 2025` |
| 21 jan 2026 | Gezamenlijke vergadering: "Michiel met IMBOR", focus april/mei. | Obsidian |
| 5 aug 2026 | Michiel levert `IMBOR Michiel.qea` (126 MB) en daarna `IMBOR Michiel v2.qea` (118 MB). Het mergen in het GGM lukte niet. | bestandsdatums, gesprek |
| 12 aug 2026 | 23e expertgroep: IMBOR is circa 112 MB, ruim twee keer het GGM. Comprimeren met enumeraties is opnieuw kandidaat. Release 3.0.0 schuift naar oktober. | Obsidian, `2026-08-12, 23e GGM-expertgroep online` |

## 2. Het gesprek, vraag voor vraag

De vragen staan hieronder zoals je ze in het gesprek stelde (typfouten verbeterd), met de kern van het antwoord.

| # | Jouw vraag | Kern van het antwoord | Opgeleverd |
|---|---|---|---|
| 1 | Je mail aan Michiel met de doorlichting: 126 MB, waarvan 83 procent in `t_attributetag`; 2.295 classes, 49.479 attributen, 441.850 tags. Je vermoeden: geërfde attributen staan fysiek herhaald. Daarbij: "Doe me 3 voorstellen om de database kleiner en efficiënter te maken en te laten passen bij het huidige GGM. Ik denk aan het algemeen houden van objecttypen die geen verschillende attributen hebben en onderscheid aan te maken via enumeraties […] Het is wel belangrijk dat de juiste EA_GUIDs worden gebruikt […] Werk de meest efficiënte oplossing uit in een nieuwe versie van een IMBOR-project, maar integreer het nog niet met het GGM." | CROW publiceert de hiërarchie zelf (`imbor2025-kern.ttl`, 2.591 `subClassOf`); 1.838 van de 1.856 classes matchen, met nul conflicten. Drie voorstellen; voorstel 2 (overerving plus enumeraties) is uitgewerkt: 126 → 15,6 MB, verliesvrij. Nieuwe klasse `Functie`; de naam `soort` volgt het GGM, terwijl IMBOR `verschijningsvorm` gebruikt. | `IMBOR 2025 geoptimaliseerd.qea`, notitie en mapping-Excel (12:31) |
| 2 | "Matchen de EA_GUIDs van de IMBOR-objecttypen met de objecttypen uit het GGM?" | Deels. 46 van de 58 classes in `Model IMBOR` matchen op GUID en naam. De 115 enumeraties hebben nul overlap (`enum_<Attribuut>` tegenover `enum_<Klasse><Attribuut>`). Van de attributen delen er 80 een naam. 12 GGM-classes komen uit een oudere IMBOR-generatie, en er zijn 30 naamconflicten met andere domeinen. | `GGM-IMBOR GUID-vergelijking.xlsx` (13:02) |
| 3 | "Kun je een voorstel doen voor reparatie van de enums, de attributen en de objecttypen?" | Koppelen in betrouwbaarheidsklassen A t/m D; klasse A doorgevoerd. Eerste versie: IMBOR nam GUID **en naam** over uit het GGM. Claude was het daar niet mee eens en stelde voor: GUID uit het GGM, naam uit IMBOR, zodat de terminologie naar de actuele CROW-publicatie gaat. | reparatievoorstel, mappingtabellen, uitgelijnd model |
| 4 | **"Ik wil GUID uit het GGM en naam uit IMBOR"** | Omgezet. Op 52 elementen staan nu de tags `Herkomst IMBOR EA_GUID` en `GGM-naam`. EA ziet de naamverschillen bij de merge als hernoeming in het GGM. | idem |
| 5 | "Wij hebben enumeraties geïntroduceerd om het aantal objecttypen terug te dringen, dat hadden we eerder ook al gedaan. Deze enumeraties moeten we ook matchen" | "Ik heb iets belangrijks gevonden voordat ik verder ga": de GUIDs met dubbele accolades. | – |
| 6 | "Repareer hier ook de dubbele quotes" | De 115 `{{…}}`-GUIDs zijn genormaliseerd in de GGM-werkkopie en in de release `v3.0.0`, elk als kopie `… - GUIDs gerepareerd.qea` naast het origineel. Ook gevonden: `enum_Type` (414) en `enum_TypePlus` (539) worden door niets gebruikt. 126 waarden daaruit hebben de GGM-GUID overgenomen; 117 elders alleen gesignaleerd. Gedeelde attribuut-GUIDs: 101 → 227. Volgorde: eerst repareren, dan mergen. | idem, plus de twee gerepareerde GGM-bestanden (13:31) |
| 7 | "Wat is het verschil tussen de map met 00 Klassen en 99 Objecttypen?" | 00 bevat abstracte klassen, 99 concrete objecttypen (CROW-modelleerregel R0044). De scheiding is niet zuiver: 48 objecttypen hebben subklassen en 20 klassen hangen onder een objecttype. De mapnaam is een slechte gids; de generalisaties bepalen het. CROW bespreekt dit zelf in issue 1432. | – |
| 8 | "Klopt het dat het Objecttype Aanleginrichting via overerving alle attributen heeft zoals hier in de screenprint staan?" (screenprint) | Ja, 30 om 30, van dezelfde klassen. In het model zijn het er 31, door het nieuwe `soort` op `Infrastructureel kunstwerk`. Let op: `ReëelObject` (NEN 2660) en `Reëel object` (NEN 3610-2022) zijn twee verschillende klassen. | – |
| 9–10 | "En de aansluitput?" en "En beugel?" (screenprints) | Beide 27 om 27. `Aansluitput` bleef class (subklassen, en hij staat in 00 Klassen). `Beugel` werd een waarde in `enum_StraatmeubilairSoort`. **Daarbij gevonden:** 93 van de 137 classes met `soort` hebben een voorouder die ook een `soort` heeft. Dat is een schaduwing, bijvoorbeeld drie keer `soort` in de keten `Deksel` → `Afdekking` → `Constructieonderdeel`. Claude stelde voor de diepere te hernoemen (`Aansluitput.aansluitputsoort`) en vroeg: "Zal ik de eerste variant doorvoeren?" **Die vraag is niet beantwoord.** | – |
| 11 | "IMBOR is opgebouwd door gebruik te maken van multiple inheritance. Ze kennen Klassen, die de rol van Mixins vervullen, en objecttypen die zijn opgebouwd uit 1 of meer mixins. […] Maak voor mij een nieuw Enterprise Architect project […] De attributen van alle objecttypen zouden dan moeten kloppen met het nu geoptimaliseerde project" (met de twee Excel-exports, 14:30) | Mixin-model gebouwd. Van de 1.857 vergelijkbare objecttypen hebben er 1.848 dezelfde effectieve attribuutset; de 9 afwijkingen komen door een fout in de bron rond `Overbrugging`. Eerste versie: alleen de transitieve reductie, 2.465 generalisaties. | mixin-model, overzicht, notitie |
| 12 | "Volgens mij heb je de multiple inheritance van de Objecttypen niet goed meegenomen. Verbeter dat" | Terecht. `Lichtmast` had alleen `Paal` als supertype, terwijl de bron er zeven noemt. Nu staan alle 11.948 relaties erin: 2.465 `mixin` en 9.483 `mixin (afgeleid)`, de relaties die transitief al volgen. Het bestand werd 24,6 MB en is in twee delen overgezet. | idem |
| 13 | "Wat is mixdeel_aa en ab?" | Transportdelen, omdat de sandbox maximaal 20 MB per bestand schrijft. Op de Mac weer samengevoegd, met gecontroleerde checksum. Claude kan zelf niets wissen, alleen verplaatsen; vandaar `_to_delete`. | – |
| 14 | "Is hij nu ook goed uitgelijnd met het GGM? Komen de EA_GUIDs dus zo goed mogelijk overeen?" | 66 object-GUIDs, net als het platgeslagen model. Attribuut-GUIDs eerst 85, na 22 extra overnames 101. Het verschil van 126 met 227 hoort bij de modelkeuze: daar zijn de `enum_Type`-waarden classes. 6 attributen kregen de tag `GGM-duplicaten van dit attribuut`. | mixin-model, notitie |
| 15 | "Ik heb de linkeddata varianten van IMBOR ook neergezet. Kun je bij de entiteiten in het qea-model ook de referenties naar de linkeddata versies opnemen. Wat mij betreft in de vorm van sameAs, en dan de officiële RDF/OWL-manier" (LD-zip, 15:51) | `owl:sameAs` is alleen juist voor de domeinwaarden (individuen). Voor classes en lijsten is het `owl:equivalentClass`, voor attribuutsoorten `owl:equivalentProperty`. Daarnaast `rdfs:seeAlso` naar het begrip in de begrippenlijst. Het bestand werd 30,9 MB, in drie delen. | idem |
| 16 | "Wat mij betreft mogen rdfs:seeAlso en owl:equivalentProperty eruit" | 11.585 tags verwijderd. Over blijven `owl:equivalentClass` (2.839) en `owl:sameAs` (5.719). Het bestand werd 27,4 MB. | `IMBOR 2025 mixin-model.qea` (16:33) |

Daarna is `IMBOR 2025 mixin-model.qea` nog in EA geopend en bewaard: de bestandsdatum is 27 aug, met de SQLite-versie van EA. Ook het uitgelijnde model is op 18 aug om 14:21 in EA bewaard. `Archief.zip` (13:38, een Finder-archief) bevat ronde 2 en is vermoedelijk naar Michiel gestuurd.

## 3. Ronde 1: IMBOR compacter maken

**Diagnose.** `IMBOR Michiel v2.qea` bevat nul relaties. Daardoor is elk geërfd attribuut gekopieerd:
49.479 attributen op basis van 671 unieke namen. Geen enkel attribuut heeft een `Classifier`; de
enumeratie staat alleen in de naam `enum_<Klasse><Attribuut>`.

**Werkwijze.** De hiërarchie komt uit CROW's `imbor2025-kern.ttl`. Een attribuut wordt alleen verwijderd
als naam, type, multipliciteit, notitie en alle tags gelijk zijn aan die van de dichtstbijzijnde
superklasse. In 408 gevallen bleef daardoor een lokale override staan. Bestaande GUIDs blijven staan;
nieuwe GUIDs zijn deterministisch (UUIDv5).

**Correctie (4 nov).** Die 408 "overrides met afwijkende definitie" zijn geen afwijkende definities.
Het zijn **lege kopieën**, zonder type, definitie of tags, op 18 classes die al in de bron leeg waren,
zoals `Viaduct`, `Ecoduct`, `Flyover`, `Boom` en `Kademuur`. Ze schermen de volledige geërfde definitie af.
Zie `IMBOR snoeien - notitie.md`, onder "Controle tegen de bron".

**De drie voorstellen:**

1. Alleen overerving: 16,1 MB.
2. Overerving plus enumeraties: 15,6 MB. **Uitgevoerd.** 1.141 objecttypen zijn opgegaan in
   137 `enum_<Klasse>Soort`-lijsten, via een attribuut `soort` (0..1). De oude GUID staat als tag
   `Herkomst EA_GUID objecttype` op de enumeratiewaarde.
3. Aansluiten op de GGM- en MIM-conventies: een EA-`Enumeration`, overal een `Classifier`,
   standaardtags naar packageniveau en GGM-tagnamen. **Niet uitgevoerd.**

**Nageteld:**

| | `IMBOR Michiel v2` | `geoptimaliseerd` |
|---|---|---|
| Bestand | 118,2 MB | 16,3 MB (15,6 MiB) |
| Objecttypen + enumeraties | 1.857 + 438 | 717 + 575 |
| Attributen incl. enumeratiewaarden | 49.479 | 9.305 (2.445 + 6.860) |
| Attribuuttags | 441.850 | 39.753 |
| Generalisaties | 0 | 701 |

## 4. Ronde 2: uitlijnen op het GGM

**Uitgangspunt, door jou gekozen in vraag 4:** de GUID komt uit het GGM, de naam uit IMBOR.

| Laag | A (doorgevoerd) | B | C | D / overig |
|---|---|---|---|---|
| Enumeraties (gekoppeld op waardenlijst, niet op naam) | 15 | 23 | 14 | 63 geen match |
| Attributen (46 gedeelde classes, effectieve set) | 35 | 14 | – | 66 al gelijk, 609 alleen IMBOR, 325 alleen GGM |
| Objecttypen uit de oude GGM-tak | 2 (`Overbrugging`, `Solitaire plant`) | 5 | 12 | 18 homoniemen gescheiden houden |
| Waarden uit `enum_Type` en `enum_TypePlus` | 126 | – | – | 117 alleen gesignaleerd |

**Nageteld:** gedeelde object-GUIDs gingen van 49 naar 66 en gedeelde attribuut-GUIDs van 80 naar 227.
De GGM-werkkopie had 115 GUIDs met `{{`; de gerepareerde kopie heeft er nul. De gerepareerde
v3.0.0-kopie staat niet meer in `v3.0.0/`. De reparatie is op 23 okt alsnog in de release zelf
doorgevoerd (zie §6).

## 5. Ronde 3: het mixin-model

Bijzonderheden van de bron: 555 klassen hebben eigen attributen, waarvan er 117 echt als mixin worden
hergebruikt. De mixinsets zijn gesloten: als K een mixin van X is, zijn alle mixins van K dat ook,
zonder uitzondering bij alle 11.948 combinaties.

Elk objecttype heeft de tags `IMBOR-rol`, `IMBOR-niveau` en `Samengesteld uit`. Elke generalisatie
heeft de tag `IMBOR-samenstelling` (`direct` of `afgeleid`).

**Nageteld:**

| | platgeslagen (uitgelijnd) | mixin-model |
|---|---|---|
| Objecttypen | 717 | 2.406 |
| Enumeraties | 575 | 460, waarvan 21 leeg |
| Attributen op classes | 2.445 | 1.733 |
| Enumeratiewaarden | 6.860 | 5.719 |
| Generalisaties | 701 | 11.948 (2.465 + 9.483) |
| Gedeelde object- / attribuut-GUIDs met het GGM | 66 / 227 | 66 / 101 |
| LD-verwijzingen | – | 2.839 × `owl:equivalentClass`, 5.719 × `owl:sameAs` |
| Bestand | 16,5 MB | 28,8 MB (27,4 MiB) |

De verschillende bestandsgroottes in de stukken (24,6, 30,9 en 27,4 MB) horen bij de opeenvolgende
versies uit vraag 12, 15 en 16.

## 6. Wat er daarna gebeurde

| Datum | Gebeurtenis | Vastgesteld in |
|---|---|---|
| 18 aug (datum volgens claude.ai) | Chat *IMBOR overerving en klassenconflicten*: je concept-mail aan Michiel, zijn vragen en een persoonlijke mail als antwoord. Zie §7. | claude.ai |
| 26 aug | De sessie *IMBOR mixin-model gaps analysis* gebruikt het mixin-model als voorbeeld van een ontwerpparadigma in de promotie-proposal. | Claude Code-sessie `local_304308e6` |
| 27 aug | `IMBOR 2025 mixin-model.qea` voor het laatst bewaard, in EA. | bestandsdatum |
| 13 sep | Michiel voegt het mixin-model samen in `v3.0.0` (`a4d2c709`, "TODO: diagrammen bijwerken"). Het bestand groeit van 60,7 naar 80,7 MB. Er komen 2.361 objecttypen en 460 enumeraties mee, maar **maar 1.184 van de 11.948 generalisaties** (496 `mixin`, 688 `mixin (afgeleid)`). `enum_Type`/`enum_TypePlus` verdwijnen. | `git show a4d2c709` |
| 25 sep | Michiel draait de samenvoeging terug (`0d5b9ab0`). De commit noemt geen reden. | git |
| 23 okt | In `b08e3f89` ("Diverse aanpassingen") worden de 115 `{{`-GUIDs in `v3.0.0` gerepareerd. | git, nageteld |

**Stand van `v3.0.0` op 4 november (nageteld).** De IMBOR-tak is nog de oude, gedeeltelijke import:
`Model IMBOR` met 58 classes, `Enumeratiesoort` met 115 enumeraties, en `enum_Type` en
`enum_TypePlus` zonder gebruikers. De coderingsfout `OriÃ«ntatie` staat nog in 2 objecten en
13 attributen. Alleen de `{{`-reparatie is doorgevoerd.

## 7. De mail aan Michiel over overerving en conflicten

Je concept stelde: "Als er conflicten zijn dan wint de mixin die er het laatste bijkwam, en overschrijft
properties met dezelfde naam." Claude legde uit waarom dat niet klopt. In RDFS en OWL is overerving
monotoon: superklassen hebben geen volgorde en niets wordt overschreven. Hetzelfde attribuut dat via
twee paden binnenkomt (bijv. `Object` via `ReëelObject` en via `Geo-object`) telt één keer.

Echte dubbelingen ontstaan op twee andere plekken:

- twee verschillende mixins die elk een eigen attribuut met dezelfde naam definiëren;
- conflicterende restricties, zoals een andere kardinaliteit of waardenlijst, die niemand oplost.

Michiel vroeg of het om directe of indirecte overerving gaat, met als voorbeeld zijn tabel bij
`Aalpijp`, en wat `mixin (afgeleid)` betekent. Het antwoord: overerving is transitief, en zijn tabel is
de uitgeschreven closure. De mail bevat een SQL-query op de .qea die per objecttype laat zien uit welke
mixin elk attribuut komt.

**Correctie op de mail.** Daarin staat: "'Afgeleid' betekent dat ik die generalisatie uit de RDF heb
gegenereerd". Volgens het bouwgesprek (vraag 12) betekent `mixin (afgeleid)` iets anders: een relatie
die transitief al volgt uit de essentiële `mixin`-relaties. De bron is de Excel, niet de RDF. De mail
bevatte op die plek een blokhaak om dit nog te controleren. Als de mail zo is verstuurd, verdient dit
punt een correctie aan Michiel. Het verklaart mogelijk ook zijn verwarring over de 1.184 generalisaties
in zijn merge.

## 8. Bijbehorende standaarden

| Standaard | Versie | Waarom relevant |
|---|---|---|
| MIM, Metamodel Informatiemodellering (Geonovum) | 1.2, vastgesteld 13 juni 2024 | Het GGM is een MIM-model: meervoudige overerving (§2.3.3.1), metagegeven `Mixin` (§2.4.3.41), naamgeving (§5.15), lijstsoorten (§2.3.4), `Begrip` (§2.4.3.3) |
| GGM Cookbook (`docs/cookbook`) | v3.0.0 | ontwerpregels p1 (Stacked Dependency), p2 (overerving) en m1–m7, ondersteunde datatypes en lijstsoorten |
| *Voorstel naamgevingsconventies Gemeentelijk Gegevensmodel* | 25 juli 2023 | MIM-alternatief 2 (UpperCamelCase voor objecttypen, lowerCamelCase voor attributen), geen accenten, `soort` en `type` naast elkaar |
| *UML naamgeving- en tekenconventies datamodelleren* (Utrecht) | 0.2, 23 okt 2020 | datatypes, enumeratie versus referentielijst en codelijst, IMBOR als bronmodel |
| IMBOR 2025 (Stichting CROW, GitHub `Stichting-CROW/imbor`) | linked-databestanden van 2 juli 2025 | hiërarchie, domeinwaarden, URI's; modelleerregel R0044 (klassen tegenover objecttypen), issue 1432; hergebruik van NEN 2660-2, NEN 3610 en GWSW |
| OWL 2 / RDFS (W3C) | – | `owl:sameAs` alleen voor individuen, `owl:equivalentClass` voor klassen; monotone overerving zonder override |
| UUID, versie 5 | RFC 9562 | deterministische GUIDs voor nieuwe elementen |
| Enterprise Architect | 16+ | `.qea` is SQLite; merge koppelt op `ea_guid`; formaat `{8-4-4-4-12}` |

## 9. Toetsing aan de standaarden

Machinaal nageteld op het uitgelijnde platgeslagen model en het mixin-model.

| Regel | Platgeslagen | Mixin | Oordeel |
|---|---|---|---|
| m1 definitie bij objecttype en enumeratie | 47 objecttypen en 438 enumeraties zonder definitie | 91 objecttypen zonder definitie; enumeraties volledig | Mixin is veel beter. De ontbrekende definities moeten uit de CROW-bron komen. |
| m3 datatype uit de ondersteunde lijst | 1.140 attributen zonder datatype en zonder classifier; 4× `DATUMTime` | 12 afwijkend: `geo:wktLiteral` (4), `DATUMTime` (4), `xsd:anyURI` (3), `xsd:duration` (1) | Mixin is bijna schoon. Vertaal naar `GM_…`, `DateTime` en `URI`; voor `xsd:duration` is er geen GGM-type. |
| m4 minstens één attribuut, ook geërfd | 0 overtredingen | 0 overtredingen | In orde. |
| m5 minstens één enumeratiewaarde | 0 | **21 lege enumeraties**, waarvoor CROW geen waarden publiceert | Overtreding. Navragen bij CROW, of tijdelijk vervangen door een vrij tekstattribuut. |
| Eenduidige attribuutnamen langs een keten | **93 van de 137 `soort`-attributen schaduwen een geërfde `soort`** (vraag 10, onbeantwoord) | geen `soort` | Alleen een probleem in het platgeslagen model. Kies tussen hernoemen (`aansluitputsoort`) of één `soort` per keten. |
| p1 Stacked Dependency | IMBOR-`Object` heeft dekking 1,0 met `Object` in Model Kern RGBZ | idem | Laat het IMBOR-`Object` aansluiten op de onderliggende laag. Houd de 18 homoniemen in andere domeinen gescheiden. |
| p2 geen te diepe of brede hiërarchie | tot 12 niveaus diep, tot 2 supertypes | tot 10 niveaus, tot 10 supertypes per objecttype, 11.948 generalisaties | Spanning met p2. Neem in het GGM hooguit de essentiële laag op (2.465). |
| MIM §2.3.3.1 meervoudige overerving | n.v.t. | toegestaan | In orde. |
| MIM §2.4.3.41 metagegeven `Mixin` | n.v.t. | eigen stereotypen `mixin` en `mixin (afgeleid)`; geen MIM-tag `Mixin`, geen stereotype «Generalisatie» zoals het GGM (304 keer) | Zet om naar «Generalisatie» met tag `Mixin`. Let op: in MIM betekent `Mixin = Ja` dat de superklasse niet in de implementatie voorkomt. Dat past bij de IMBOR-klassen uit 00 Klassen, maar niet bij objecttypen met subklassen, zoals `Gebouw` en `Kunstwerk` (R0044). |
| MIM §5.15.4 en GGM-naamgeving 2023: alternatief 2 voor logische modellen | 685 van 2.468 attribuutnamen en 92 objecttypnamen met spatie | 569 van 1.733 attribuutnamen en 617 van 2.406 objecttypnamen met spatie | Botst met je keuze in vraag 4. Zie §10.1. |
| GGM-naamgeving: geen accenten | 24 attribuutnamen, 6 objecttypnamen, 4 enumeraties | 19, 39 en 5 (bijv. `ReëelObject`, `enum_KunstwerkOriëntatie`) | Accenten horen in de alias, niet in de naam. |
| Cookbook: alleen «Enumeratie», geen referentielijst of codelijst | `Referentie` 122×, `Enumeratie` 533×, bewaard als tag | idem | Een MIM-referentielijst past bij `Referentie`, maar het GGM ondersteunt die niet. Voorlopig enumeratie, en navragen bij CROW. |
| GGM-vorm van enumeraties | Class met stereotype `Enumeratie` | idem | Het GGM gebruikt het EA-element `Enumeration` (388). Dit is voorstel 3 uit ronde 1 en nog niet gedaan. |
| MIM `Begrip` en `Herkomst` (§2.4.3.3–4) | – | `owl:equivalentClass` en `owl:sameAs` als tags; `rdfs:seeAlso` naar de begrippen is op jouw verzoek weggehaald | Juist volgens OWL 2. MIM vraagt daarnaast `Herkomst` (bijv. "IMBOR 2025, CROW"). De begrip-URI's (`data.crow.nl/imbor/term/…`) zouden het MIM-metagegeven `Begrip` vullen; dat is een andere rol dan `rdfs:seeAlso`. |
| EA-GUID-formaat | 48 objecten met een GUID die één hexteken te kort is (37 tekens); 6.085 attribuut-GUIDs in kleine letters | 48 objecten te kort; 5.672 attribuut-GUIDs in kleine letters | **Nieuw, niet in het gesprek.** De te korte GUIDs komen uit Michiels bestand. Daar gaat het om 46 classes, precies de classes die IMBOR met het GGM deelt. In `v3.0.0` hebben alle 58 classes in `Model IMBOR` en 2.042 waarden in `Enumeratiesoort` zo'n GUID. Het "schoon mergen" van die 46 berust dus op twee kanten met dezelfde kapotte GUID. Repareer dit in beide bestanden tegelijk, zoals bij `{{`. |

## 10. Bijstellingen

1. **Naamgeving.** In vraag 4 koos je, op voorstel van Claude, voor de IMBOR-naam. De onderbouwing was
   dat het GGM geen naamgevingsconventie heeft ("2.281 van de 8.880 attributen met spatie"). Die telling
   bevat de enumeratiewaarden: 2.023 van de 2.281. Van de 4.618 echte attribuutsoorten heeft
   5,6 procent een spatie, en in `Model IMBOR` geen enkele. Bovendien volgt de conventie uit 2023
   MIM-alternatief 2, en MIM §5.15.4 schrijft dat voor logische modellen voor.

   Het advies is daarom: houd de GUID uit het GGM, houd de naam volgens alternatief 2
   (`gewichtLeeg`, `SolitairePlant`) en neem de IMBOR-naam op als `Alias` (MIM §2.4.3.2). De koppeling
   met CROW blijft via `owl:equivalentClass`. Dat betekent je eigen besluit herzien, dus het is een
   beslispunt en geen correctie.
2. **Bestandsgrootte.** De 126 MB uit je mail hoort bij `IMBOR Michiel.qea`, het eerste bestand, dat
   niet meer in de map staat. `IMBOR Michiel v2.qea` is 118 MB (112,7 MiB, de "112 MB" uit de expertgroep).
3. **"Mixin (afgeleid)" in de mail aan Michiel** betekent "volgt transitief", niet "gegenereerd uit de
   RDF". Zie §7.

## 11. Open beslissingen

1. **Welk model gaat het GGM in?** Het mixin-model (trouw aan CROW) of het platgeslagen model
   (GGM-patroon)? Een middenweg: het mixin-model met alleen de essentiële generalisaties.
2. **Heel IMBOR, of alleen wat Delft beheert?**
3. **Naamgeving:** de IMBOR-naam leidend (besluit van 18 aug), of alternatief 2 met de IMBOR-naam als
   alias (advies, §10.1).
4. **Geschaduwde `soort`-attributen** in het platgeslagen model (93 van 137): hernoemen of per keten één
   `soort`. Deze vraag staat nog open in het gesprek.
5. **`soort` versus `verschijningsvorm` of `type`:** afstemmen met CROW.
6. **`Referentie` (122) versus `Enumeratie` (533)**, en de 21 lege enumeraties (m5).
7. **Beslislijst ronde 2:** 23 enumeraties (B), 14 (C), 14 attributen op superklassen, 10 objecttypen uit
   de oude tak, 30 naamconflicten (waarvan 18 homoniemen, voorstel `<naam> (IMBOR)`) en 117 gesignaleerde
   waarden.
8. **Aandachtspunten ronde 1:** 18 classes die niet in IMBOR-2025 voorkomen en 22 zonder superklasse. Na
   ronde 3 hebben nog 6 classes geen linked-data-tegenhanger.
9. **De merge van 13 september:** waarom is die teruggedraaid, en waarom kwamen maar 1.184 van de
   11.948 generalisaties mee? Navragen bij Michiel, samen met de correctie uit §7.
10. **GUID-reparatie** van de te korte GUIDs, vóór een nieuwe merge.
11. **Coderingsfout** `OriÃ«ntatie` en verwanten in het GGM.

## 12. Kan het werk opnieuw worden gedaan?

De invoer is er nog:

- `IMBOR Michiel v2.qea`;
- `IMBOR-2025 (LinkedData zipfile).zip`;
- de twee CROW-exports;
- de GGM-werkkopie.

Elke beslissing staat per element in de mapping-Excels.

**De scripts staan sinds 4 november in `IMBOR/scripts/`:** 20 scripts (`00`–`19`) plus een `README.md`.
Dat gebeurde op jouw verzoek door de oorspronkelijke Cowork-taak. Die taak draaide in een cloud-sandbox
(`/home/claude`) die inmiddels is opgeruimd. Daarom zijn het **reconstructies** uit het verloop van de
taak: de definitieve versies, met de correcties die onderweg zijn gemaakt, maar geen byte-identieke
kopieën.

Ze zijn niet opnieuw gedraaid. Werk daarom altijd op een kopie. De losse SQL-verkenningsqueries zijn
niet opgenomen; de taak bood aan die als `analyse.py` toe te voegen.

Op 4 november gecontroleerd:

- Alle Python- en shellscripts zijn syntactisch geldig.
- Buiten `scripts/` is niets gewijzigd.
- De UUIDv5-namespace is **`6f1b0d3e-9c2a-4f77-9a1e-1b2c3d4e5f60`**. Samen met de sleutelvorm uit de
  scripts (`class|Functie`, `enum|enum_GebouwSoort`, `attr|Gebouw|soort`, …) levert die exact de GUIDs
  op die in de bestanden van 18 augustus staan: 8 van 8 steekproeven, in het geoptimaliseerde model en
  in het mixin-model. Een herbouw levert dus dezelfde GUIDs op.

De volgorde in het kort:

| Scripts | Onderdeel |
|---|---|
| 00–03 | linked data ophalen en uitlezen |
| 04 | de verworpen heuristische eerste poging |
| 05–07 | de optimalisatie |
| 08 | de GUID-vergelijking |
| 09–11 | reparatie en uitlijning |
| 12–13 | GUID-normalisatie |
| 14–16 | de mixin-bouw |
| 17–18 | de linked-data-koppeling |
| 19 | het splitsen van bestanden groter dan 20 MB |
