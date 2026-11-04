# Memo Domein Financiën in POHV en GGM (Invest-NL): status en verwerkingsvoorstel voor v3.0.0

Notitie van 4 november 2026. Getoetst is `memoUitwerkingFinancienVeraGgm_1.pdf` (memo *Domein Financiën in POHV &
GGM*, Michiel van Wezel, Invest-NL / Ruimte-OK / Programma Onderwijshuisvesting, 26 november 2025, 21 pagina's)
tegen `v3.0.0/Gemeentelijk Gegevensmodel.qea`, het GGM Cookbook (ontwerpregels m1 tot m7 en p1, p2, lijst
ondersteunde modelelementen en datatypes), de naamgevingsconventies van het GGM (2023, MIM-alternatief 2) en de
notities van de overleggen met POHV (12 november 2025 en 6 oktober 2026).

## Samenvatting

- **Besloten, niet uitgevoerd.** De RFC financiën van POHV is sinds februari 2026 in openbare consultatie geweest,
  akkoord bevonden en op de expertgroep van 12 augustus 2026 ("financiën en onderwijshuisvesting worden in de
  volgende release meegenomen") en in het overleg met POHV van 6 oktober 2026 ("gaat mee in de eerstvolgende
  GGM-release") toegezegd voor de volgende release. In de .qea staat niets ervan: Model Financien kent geen
  Verbijzondering, Verbijzonderingsoort, verdeelsleutel, hulpkostenplaats of RGS-element; `Mutatie` heeft nog
  alleen `datum` en `bedrag`. Geen GitHub-issue, geen commit.
- **Opmerkingen in Obsidian** (overleggen 12 november 2025 en 6 oktober 2026, expertgroep 12 augustus 2026,
  kennisnotities RGS en POHV, en sinds 4 november 2026 de mails van Inge van Creij-Maas van 4 februari, 22 en 29 april
  2026): geen inhoudelijke opmerkingen op de modelstructuur. De expertgroep adviseerde in februari om ook de
  RGS-verwijzing door te voeren; de gearceerde aanbevelingen uit bijlage E zijn in april ter kennisgeving aangenomen. Michiel van Wezel noemt het RFC-model
  "volledig dekkend"; Arjen dacht op 6 oktober dat het al was doorgevoerd, Ashkan meldde dat het op de lijst voor de
  volgende release staat. Drie punten werken door in de keuzes: de vraag van Arjen uit november 2025 of het GGM
  een grootboekschema kan voorschrijven, de wens van alle partijen om referentiedata machineleesbaar te
  publiceren (RGS staat in Excel), en de open vraag of Centric, AFAS en Exact RGS en verbijzonderingen leveren.
  Zie hoofdstuk 3.
- **Wat de memo vraagt** (vier eisen): kostensoorten conform het Referentie Grootboekschema (RGS); kostenplaatsen
  met typen (bestaat al); boekingsverbijzonderingen bij een mutatie (6S-laag van Stewart Brand, NL/SfB-code,
  componentomschrijving, geplande vervangingsdatum), naar het voorbeeld van VERA; verdeelsleutels met hoofd- en
  hulpkostenplaatsen. De memo tekent daarvoor vijf nieuwe entiteiten rond de bestaande `Kostenplaats`,
  `Hoofdrekening` en `Mutatie`.
- **Vertaling naar het GGM:** zeven nieuwe objecttypen in `Model Financien` (`Referentiegrootboekrekening`,
  `Verbijzondering`, `Verbijzonderingsoort`, `Verdeelsleutel`, `Verdeelkenmerk`, `Verdeelregel` en, als keuze,
  geen aparte hulpkostenplaats maar een indicatie op `Kostenplaats`), tien relaties en twee attributen op
  bestaande objecttypen, met MIM-datatypes. De technische sleutels en de tekstuele verwijzing `kenmerkNaam` uit de
  memo worden relaties. De MIM-constructie *referentielijst* die de memo voor RGS voorstelt, ondersteunt het GGM
  niet (cookbook); RGS wordt daarom, net als `Taakveld` (IV3) en `CPV-code`, een objecttype met de RGS-code als
  functionele sleutel.
- **Bijvangst.** Het proposal *Inkooporderregels* (Centric, februari 2026, ook in consultatie) is evenmin
  verwerkt: er is geen `Inkooporderregel` in het model. Dat is een apart proposal en valt buiten deze notitie.

## 1. Wat is gecontroleerd

| Bron | Zoekactie | Uitkomst |
|---|---|---|
| `t_object`, `t_attribute`, `t_connector` (Model Financien, 2326) | 24 objecttypen, hun attributen en relaties; namen met *Verbijzonder*, *Verdeel*, *Grootboek*, *RGS*, *Kostensoort* | niets van de memo aanwezig |
| `t_diagram` | diagrammen van Financiën | vier: Verwerken Mutaties (1886), Personen, Verplichtingen en Facturen, Begroting en Budgetverantwoordelijkheid |
| GitHub-issues | *RGS*, *POHV*, *verbijzondering*, *financien* | niets |
| Obsidian | overleggen met POHV | 12 november 2025 (memo besproken, wens: RGS en hulpkostenplaatsen in het GGM); 6 oktober 2026 (RFC akkoord, mee in de eerstvolgende release; vraag of leveranciers RGS en verbijzonderingen ondersteunen) |
| `~/Downloads` | eerdere versie | `memoUitwerkingFinancienVeraGgm (1).pdf` van 18 februari 2026 is dezelfde memo (consultatieversie) |

## 2. Huidige situatie in het model

- `Kostenplaats` (14219): `naam`, `omschrijving`, `kostenplaatssoortCode`, `kostenplaatssoortOmschrijving`,
  `kostenplaatstypeCode`, `kostenplaatstypeOmschrijving`, `BTWCode`, `BTWOmschrijving`. Eis 2 (kostenplaatsen met
  typen) is daarmee gedekt.
- `Hoofdrekening` (14216, definitie "is kostensoort"): `nummer`, `naam`, `omschrijving`, `subcode`,
  `subcodeOmschrijving`, `PIAHoofdcategorieCode`, `PIAHoofcategorieOmschrijving`; hiërarchie via `valt binnen`
  (Hoofdrekening 1 – 0..*); `heeft` Kostenplaats 1..* – 0..*; `heeft` Subrekening.
- `Mutatie` (14220, definitie "Wijziging van een situatie"): `datum : date`, `bedrag : Bedrag`; relaties `van`
  en `naar` Hoofdrekening (0..* – 1), `heeft betrekking op` Kostenplaats (0..* – 1); wordt gevoed door
  Factuurregel, Batchregel en Bankafschriftregel.
- Geen referentielijsten: het cookbook ondersteunt *Referentielijst* en *Codelijst* uit MIM niet; externe
  waardelijsten staan als objecttype in het model (`Taakveld` voor IV3, `CPV-code` in Model Inkoop).

## 3. Wat er in Obsidian over is gezegd

Doorzocht op 4 november 2026: de hele kluis op *verbijzondering*, *verdeelsleutel*, *hulpkostenplaats*, *RGS*,
*referentiegrootboek*, *POHV*, *Invest-NL* en *van Wezel*. Treffers buiten de GGM-notities (Edustandaard, IGM,
Evernote-import) gaan over andere betekenissen van die woorden.

| Bron | Opmerking | Gevolg voor dit voorstel |
|---|---|---|
| 12 november 2025, *Definitief GGM & POHV Financien* (eerste bespreking van de memo) | Wensen van POHV: MIM-referentielijsten en het referentie grootboekschema onderdeel van het GGM maken; hulp- en hoofdkostenplaatsen toevoegen. Eigen vraag van Arjen: "Kunnen we grootboekschema's in het GGM opnemen en zelfs benoemen welk schema gehanteerd moet worden?" Actie: voorstel op de agenda van de expertgroep (afgerond 1 december 2025). | keuze 7: wel of niet in de definitie van `Referentiegrootboekrekening` vastleggen dat RGS het te hanteren schema is; `versieRGS` als attribuut |
| memo zelf, *Vervolgstappen* | "Beheergroep 20251202, nieuwe versie notitie"; de versie van 18 februari 2026 in `~/Downloads` is byte voor byte gelijk aan de versie van vandaag | er is geen latere versie van de memo; van de beheergroep van 2 december 2025 staat geen verslag in Obsidian |
| 4 februari 2026, expertgroep | "proposal financien": welke eigenschappen moet de inkooporderregel hebben, koppeling aan factuurregel; mail aan Jetse van Tilborg (Centric) | betreft het proposal Inkooporderregels, niet deze memo |
| 4 februari 2026, reactie expertgroep (mail Inge van Creij-Maas, met Victor van der Kloet en Arjan de Bruin; in Obsidian sinds 4 november 2026) | Verdeelsleutel en Verbijzondering zijn erg nuttig; Leiden werkte aan een eigen verbijzonderingsproposal, niet strijdig. RGS-codes worden binnen gemeenten weinig gebruikt (verantwoording zit als export in de applicatie), maar de verwijzing is een kleine wijziging zonder nadelen: advies om ook RGS door te voeren. Bijlage E nog niet bekeken. Arjen heeft dit kort daarna aan Michiel van Wezel gemaild, met de aankondiging van de openbare consultatie. | het advies van februari was RGS wél op te nemen; het besluit van Arjen van 4 november 2026 om de definities van RGS nog niet op te nemen wijkt daarvan af en blijft een open keuze (keuze 1); het proposal van Leiden is nergens teruggevonden |
| 22 april 2026, mail Inge | De gearceerde aanbevelingen in bijlage E (GGM in lijn brengen met POHV en RIO) worden ter kennisgeving aangenomen en niet opgepakt: geen was-wordt-toelichting, te specifiek onderdeel, andere proposals hebben meer impact. Arjen zet de conclusie door naar Michiel van Wezel. | bijlage E blijft buiten dit voorstel (was al zo); of de conclusie bij Michiel is aangekomen is niet geverifieerd |
| 29 april 2026, afstemmingsoverleg (samenvatting Inge per mail) | Het proposal mag in openbare consultatie als *Onderwijshuisvesting*, zonder de gearceerde delen van bijlage E; *Financiën inkooporderregels* (Centric) is apart gereed voor consultatie; alle proposals samen in één keer, aankondiging door Arjen op de Pleio. | lost de vraag hieronder op: de consultatie *onderwijshuisvesting* van 12 augustus is deze memo, *financiën* is Inkooporderregels |
| 12 augustus 2026, 23e expertgroep | Ashkan: "openbare consultaties samenwerkingsomgeving, inkooporders, financiën en onderwijshuisvesting worden in de volgende release meegenomen" | *onderwijshuisvesting* is deze memo, *financiën* en *inkooporders* betreffen het proposal Inkooporderregels van Centric |
| 6 oktober 2026, POHV-overleg (Michiel van Wezel, Jacques Oosterveen, Ahmed Ibrahim, Ashkan, Arjen) | RFC sinds februari in consultatie, akkoord, op de lijst voor de eerstvolgende release. Arjen: "volgens mij hebben we hem doorgevoerd"; Ashkan: staat op de lijst, nog niet van de consultatiepagina gehaald. Michiel: het RFC-model is "volledig dekkend voor onze behoefte"; de verdieping bestaat uit de boekingsverbijzonderingen ("meerdere plakkertjes op een boeking") en de verwijzing naar RGS; voor de meeste leveranciers implementeerbaar, behalve de RGS-koppeling. Jacques vroeg om opmerkingen; Arjen: geen, akkoord, gaat in de volgende versie. Gedeelde wens: standaarden, referentiedata en enumeraties machineleesbaar publiceren (RGS staat in Excel bij de NBA). Contact Centric: Ron Bartels. Besluit: de RFC gaat mee in de eerstvolgende GGM-release. | bevestigt dat het model nog niet is aangepast; keuze 8: de RGS-codes als data meeleveren; de leveranciersvraag blijft bij Ashkan (actie 16 oktober) |
| kennisnotities *RGS* en *POHV* (6 oktober 2026) | RGS wordt gepubliceerd in Excel, niet machineleesbaar; open vraag in hoeverre financiële pakketten bij gemeenten RGS ondersteunen | idem |
| 30 juni 2026, kennismaking basisdata onderwijshuisvesting | gaat over het handboek en de databaseblauwdruk, niet over de financiënmemo | geen |

Inhoudelijke opmerkingen op de modelstructuur (namen, kardinaliteiten, keuze voor referentielijst of
objecttype) zijn nergens vastgelegd. De vertaling in hoofdstuk 5 is dus niet eerder besproken en moet aan Michiel
van Wezel worden voorgelegd.

## 4. Toetsing van de memo aan cookbook en conventies

| Regel | Bevinding in de memo | Gevolg voor opname |
|---|---|---|
| geen technische sleutels | `kenmerkId`, `regelID`, `hulpkostenplaatsId` | vervallen; `hulpkostenplaatsId` wordt een relatie naar `Kostenplaats` |
| relaties in plaats van tekstuele verwijzingen | `kenmerkNaam` komt in twee entiteiten voor en koppelt ze op naam | verdeelsleutel wordt een eigen objecttype `Verdeelsleutel` waarnaar beide verwijzen |
| m1 definities | de memo geeft doel en velden per entiteit, geen formele definities | definities in hoofdstuk 5 opgesteld; door Michiel van Wezel te bevestigen |
| m3 datatypes | geen datatypes in het ER-diagram | MIM-datatypes toegekend: `CharacterString` met `Lengte`, `Decimal`, `Date`, `Integer`; `Bedrag` blijft het GGM-datatype |
| m7 kardinaliteit | aanwezig in (min,max)-notatie | overgenomen in UML-notatie |
| naamgeving objecttypen PascalCase, attributen camelCase, `datumXxx` | `KostenPlaatsVerdeelKenmerk`, `KostenVerdeelRegel`, `datumGeldigVan`, `datumGeldigTot` | `Verdeelkenmerk`, `Verdeelregel`, `datumBeginGeldigheid`, `datumEindeGeldigheid` (de meest gebruikte vorm in het model) |
| ondersteunde modelelementen | RGS als MIM-referentielijst, VERA-"referentiedata" voor verbijzonderingsoort | objecttypen; de waardelijsten voor 6S en NL/SfB als enumeraties, zie keuze 3 |
| p1 gelaagdheid | alleen verwijzingen binnen Model Financien | in orde; Financiën is een horizontaal model, dus de uitbreiding is voor alle verticale domeinen bruikbaar |

## 5. Vertaling van de memo naar het GGM

### 5.1 Nieuwe objecttypen in Model Financien

| Objecttype | Definitie | Attributen (naam : datatype, lengte) | Herkomst in de memo |
|---|---|---|---|
| `Referentiegrootboekrekening` | Rekening uit het Referentie Grootboekschema (RGS), de landelijke standaardindeling van grootboekrekeningen waarmee kostensoorten eenduidig worden geclassificeerd en waarop de SBR-rapportage aansluit. | `referentiecode : CharacterString` (20, bijvoorbeeld WBedHuiVgo), `referentiegrootboeknummer : CharacterString` (20), `omschrijving : CharacterString` (300), `omslagcode : CharacterString` (20), `niveau : Integer`, `versieRGS : CharacterString` (10) | RGS:Grootboekrekening |
| `Verbijzonderingsoort` | Soort kenmerk waarmee een mutatie nader wordt geclassificeerd, zoals de 6S-laag, de NL/SfB-code, de componentomschrijving of de geplande vervangingsdatum. | `code : CharacterString` (20), `naam : CharacterString` (80), `omschrijving : CharacterString`, `waardelijst : URI` (verwijzing naar de externe lijst, bijvoorbeeld NL/SfB) | Financien_VerbijzonderingSoort, VERA VERBIJZONDERINGSSOORT |
| `Verbijzondering` | Kenmerk dat aan een mutatie is toegekend om deze vanuit een extra perspectief te kunnen rapporteren, zonder het grootboekschema te verfijnen. | `waarde : CharacterString` (200), `omschrijving : CharacterString` | Financien_Verbijzondering, VERA Verbijzondering |
| `Verdeelsleutel` | Maatstaf waarmee de kosten van een hulpkostenplaats over andere kostenplaatsen worden verdeeld, zoals vierkante meters, fte of leerlingaantal. | `naam : CharacterString` (80), `omschrijving : CharacterString`, `eenheid : CharacterString` (20) | `kenmerkNaam` in beide entiteiten |
| `Verdeelkenmerk` | Waarde van een verdeelsleutel voor een kostenplaats in een periode, zoals 1.200 m² voor een school in een multifunctionele accommodatie. | `waarde : Decimal`, `datumBeginGeldigheid : Date`, `datumEindeGeldigheid : Date` | Financien_KostenPlaatsVerdeelKenmerk |
| `Verdeelregel` | Regel die bepaalt dat de kosten van een hulpkostenplaats volgens een verdeelsleutel worden verdeeld over de kostenplaatsen die een waarde voor die sleutel hebben. | `omschrijving : CharacterString`, `datumBeginGeldigheid : Date`, `datumEindeGeldigheid : Date` | Financien_KostenVerdeelRegel |

### 5.2 Wijzigingen op bestaande objecttypen

| Objecttype | Wijziging | Motivering |
|---|---|---|
| `Kostenplaats` | attribuut `indicatieHulpkostenplaats : Boolean` | eis 4: onderscheid hoofd- en hulpkostenplaatsen; de memo lost dit op via de verdeelregel, de indicatie maakt het ook zonder regel zichtbaar |
| `Kostenplaats` | relatie `valt onder` Kostenplaats 0..* – 0..1 (keuze 2) | "relaties tussen kostenplaatsen" uit de eisen; getrapte doorbelasting loopt al via de verdeelregel |
| `Mutatie` | definitie aanscherpen tot "Boeking van een bedrag van de ene hoofdrekening naar de andere op een datum, toegeschreven aan een kostenplaats" | de huidige definitie "Wijziging van een situatie" zegt niets; de memo bouwt op de mutatie als boeking |
| `Hoofdrekening` | geen attributen; relatie naar `Referentiegrootboekrekening` | eis 1 |

### 5.3 Relaties

| Bron | Relatie | Doel | Kardinaliteit | Opmerking |
|---|---|---|---|---|
| Hoofdrekening | is van soort | Referentiegrootboekrekening | 0..* – 0..1 | memo: "is van soort" (1,n)–(0,1); optioneel zolang niet elke gemeente RGS voert |
| Mutatie | heeft | Verbijzondering | 1 – 0..* | memo: Mutatie heeft (1,1)–(0,n) Verbijzondering |
| Verbijzondering | is van soort | Verbijzonderingsoort | 0..* – 1 | memo: (1,1)–(0,n) |
| Kostenplaats | heeft verdeelkenmerk | Verdeelkenmerk | 1 – 0..* | memo: "heeft kenmerk" |
| Verdeelkenmerk | van verdeelsleutel | Verdeelsleutel | 0..* – 1 | vervangt `kenmerkNaam` |
| Verdeelregel | verdeelt kosten van | Kostenplaats | 0..* – 1 | vervangt `hulpkostenplaatsId`; de bron is een hulpkostenplaats |
| Verdeelregel | volgens verdeelsleutel | Verdeelsleutel | 0..* – 1 | vervangt `kenmerkNaam` |
| Verdeelregel | verdeelt naar | Kostenplaats | 0..* – 0..* | memo: "verdeeld naar"; alleen nodig als de doelverzameling expliciet moet zijn in plaats van "alle kostenplaatsen met een waarde voor de sleutel" (keuze 4) |
| Kostenplaats | valt onder | Kostenplaats | 0..* – 0..1 | keuze 2 |

De bijlagen B en C van de memo (energiekosten in een MFA, vervanging van een cv-ketel) zijn als voorbeeld
bruikbaar in de toelichting van `Verdeelregel` en `Verbijzondering`.

### 5.4 Enumeraties voor 6S en NL/SfB (keuze 3)

De memo noemt de waardelijsten uit tabel 1. Als het GGM ze wil vastleggen, dan als enumeraties
`Laag6S` (Site, Structure, Skin, Services, Space plan, Stuff) en `HoofdgroepNLSfB` (10 Funderingen, 20 Ruwbouw,
30 Afbouw, 40 Afwerkingen, 50 Installaties werktuigbouwkundig, 60 Installaties elektrotechniek, 70 Vaste
voorzieningen, 80 Losse inventaris, 90 Terrein). Omdat `Verbijzondering.waarde` generiek is, zouden die
enumeraties geen attribuut hebben dat ernaar verwijst; het alternatief is twee extra attributen op `Mutatie`
(`laag6S : Laag6S`, `hoofdgroepNLSfB : HoofdgroepNLSfB`) naast de generieke verbijzondering. Dat is dubbelop en
wijkt af van wat is geconsulteerd; aanbevolen is de lijsten alleen te noemen in de toelichting van
`Verbijzonderingsoort` en via `waardelijst` naar de bron te verwijzen.

## 6. Uitvoering

Uitgevoerd op 4 november 2026 met `tools/add_financien_pohv.py`, in twee stappen. Eerst zonder RGS, na het besluit
van Arjen om de definities van RGS nog niet op te nemen; later die dag, na het lezen van de mails van 4 februari
2026 (advies van de expertgroep om RGS wél door te voeren), alsnog met `Referentiegrootboekrekening` (zes
attributen) en de relatie `Hoofdrekening` `is van soort` 0..* – 0..1, ook op het diagram *Financien Verwerken
Mutaties* (backup `.qea.backup-2026-11-04-voor-rgs-inkooporderregels`). De eerste stap omvatte: vijf objecttypen (`Verbijzonderingsoort`, `Verbijzondering`, `Verdeelsleutel`,
`Verdeelkenmerk`, `Verdeelregel`), `indicatieHulpkostenplaats` op `Kostenplaats`, de nieuwe definitie van `Mutatie`,
zes relaties, twee elementen en twee lijnen op *Financien Verwerken Mutaties* en het nieuwe diagram *Financien
Kostenverdeling*. Niet opgenomen: de hiërarchie `valt onder` (keuze 2), de enumeraties voor 6S en NL/SfB (keuze 3) en de relatie
`verdeelt naar` (keuze 4). RGS is als objecttype in Model Financien opgenomen (keuze 1) zonder voorschrift welk
schema gehanteerd moet worden (keuze 7) en zonder de RGS-codes als data (keuze 8). Backup: `.qea.backup-2026-11-04-voor-financien-pohv`.

1. **Afstemmen met de indiener.** Michiel van Wezel (en Jacques Oosterveen, financiële kant POHV) de vertaling
   in hoofdstuk 5 en de definities laten bevestigen; vragen welke RGS-versie en welke attributen van RGS zij
   minimaal nodig hebben voor de SBR-keten.
2. **GitHub-issue** aanmaken, *Proposal Financiën POHV: RGS, verbijzonderingen en verdeelsleutels*, labels
   `Proposal` en `Expertgroep`, met verwijzing naar de consultatie en de besluiten van 12 augustus en 6 oktober 2026.
3. **Model aanpassen** op `v3.0.0/Gemeentelijk Gegevensmodel.qea` na een kopie, met een script naar het patroon
   van `tools/add_samenwerkomgeving.py` (objecttypen, attributen, relaties, diagram) en `tools/fix_proposal_mor.py`
   (attributen op bestaande klassen): zes objecttypen, twee attributen, een definitie en negen of tien relaties in
   `Model Financien`. Diagrammen: `Verbijzondering`, `Verbijzonderingsoort` en `Referentiegrootboekrekening` op
   *Financien Verwerken Mutaties* (1886, rechts van `Mutatie` en `Hoofdrekening`); `Verdeelsleutel`,
   `Verdeelkenmerk` en `Verdeelregel` op een nieuw diagram *Financien Kostenverdeling* met `Kostenplaats`.
4. **Documentatie.** Paragraaf in `docs/domeinen/financien.md` na de alinea over mutaties (verbijzonderingen en
   RGS) en een paragraaf over kostenverdeling, met de diagrambeelden; daarna `task generate:docs`,
   `task publish:local`, DDL, `task generate:lod` en `task generate:translations`.
5. **Afronden.** Issue sluiten met de commit, POHV informeren; de vraag of Centric, AFAS en Exact RGS en
   verbijzonderingen leveren (open punt van 6 oktober) blijft bij Ashkan.

## 7. Keuzes bij Arjen

1. **RGS als objecttype** `Referentiegrootboekrekening` in Model Financien (aanbevolen, zoals `Taakveld`), of
   een apart package `RGS` onder Financiën zodat het schema als geheel is te laden en te versioneren.
2. **Hiërarchie van kostenplaatsen** (`valt onder`) wel of niet opnemen naast de verdeelregel.
3. **Enumeraties voor 6S en NL/SfB** niet opnemen (aanbevolen), of als extra attributen op `Mutatie`.
4. **Relatie `verdeelt naar`** weglaten (aanbevolen: de doelverzameling volgt uit de verdeelkenmerken) of
   opnemen zoals in de memo.
5. **Verdeelsleutel als objecttype** (aanbevolen) of de memo letterlijk volgen met `kenmerkNaam` als tekst in
   `Verdeelkenmerk` en `Verdeelregel`.
6. **Volgorde.** Dit proposal samen met het proposal Inkooporderregels (Centric) oppakken, omdat beide
   Model Financien en het diagram Verplichtingen en Facturen raken, of apart.
7. **RGS voorschrijven.** In de definitie en toelichting van `Referentiegrootboekrekening` vastleggen dat het
   GGM RGS als het te hanteren grootboekschema aanwijst (vraag van Arjen, 12 november 2025), met `versieRGS`
   als attribuut, of RGS alleen als optionele verwijzing opnemen.
8. **RGS-codes als data.** De RGS-lijst (Excel van de NBA) omzetten naar een machineleesbaar bestand bij het
   GGM, bijvoorbeeld als Linked Data naast de ontologie, zodat gemeenten en leveranciers dezelfde lijst laden;
   of dat aan POHV laten (gedeelde wens van 6 oktober 2026).
