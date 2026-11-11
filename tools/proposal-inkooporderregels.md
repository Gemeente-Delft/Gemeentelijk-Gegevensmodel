# Proposal Inkooporderregels (Rotterdam en expertgroep): status en verwerking in v3.0.0

Notitie van 4 november 2026. Getoetst zijn `Proposal-inkooporder-regels.pdf` (versie 0.1, februari 2026; sjabloon van de
expertgroep met inleiding, aanleiding en twee diagrammen) en de consultatie-infographic `ggm-proposal-inkooporder.png`
(indieners Bart van den Bos, gemeente Rotterdam, en Arjen Brienen; reageren tot en met 13 juni 2026) tegen
`v3.0.0/Gemeentelijk Gegevensmodel.qea`, het GGM Cookbook en de naamgevingsconventies (MIM-alternatief 2).

## Samenvatting

- **Besloten, niet uitgevoerd.** De expertgroep besprak het proposal op 4 februari 2026 (welke eigenschappen moet een
  inkooporderregel hebben; koppeling aan de factuurregel; Michiel Verhoef vond datamodellen ter onderbouwing), op
  29 april 2026 werd het gereed verklaard voor openbare consultatie (in de verslagen *financiën* of *inkooporders*
  genoemd) en op 12 augustus 2026 toegezegd voor de volgende release. In de .qea bestaat geen `Inkooporderregel`;
  `Inkooporder` (Model Financien) is nog één objecttype met twaalf attributen, waaronder `artikelcode` en
  `goederencode` die eigenlijk bij een regel horen.
- **Wat het proposal vraagt.** `Inkooporder` splitsen in een orderkop en een of meer `Inkooporderregels`, naar analogie
  van `Factuur` en `Factuurregel`: de kop houdt ordernummer, leverancier, besteldatum, status en totaalbedrag; de regel
  krijgt artikelcode, omschrijving, hoeveelheid, stuksprijs en btw. Het proposal zelf bevat geen attributenlijst;
  die is hier opgesteld uit de infographic, de aanleiding ("artikelcodes, omschrijvingen, aantallen, stuksprijs,
  eventueel btw") en de bestaande `Factuurregel`.
- **Vertaling naar het GGM.** Eén nieuw objecttype `Inkooporderregel` in Model Financien met negen attributen, vier
  relaties (`Inkooporder` heeft regels, regel wordt geschreven op `Hoofdrekening` en `Kostenplaats`, `Factuurregel`
  betreft regel) en plaatsing op het diagram *Financien Verplichtingen en Facturen*. De bestaande attributen van
  `Inkooporder` blijven staan (keuze 2).
- **Uitgevoerd op 4 november 2026** met `tools/fixes/add_inkooporderregels.py`; zie hoofdstuk 5.

## 1. Wat is gecontroleerd

| Bron | Zoekactie | Uitkomst |
|---|---|---|
| `t_object`, `t_attribute`, `t_connector` | `Inkooporder`, `Factuur`, `Factuurregel`, namen met *orderregel* | geen `Inkooporderregel`; `Inkooporder` heeft 12 attributen en 10 relaties; `Factuurregel` heeft `nummer`, `omschrijving`, `aantal`, `bedragExBTW`, `bedragBTW`, `BTWPercentage` |
| `t_diagram` | diagrammen met `Inkooporder` | *Financien Verplichtingen en Facturen* (1888); `Factuurregel` staat alleen op *Financien Verwerken Mutaties* |
| Obsidian | expertgroep, afstemming | 4 februari 2026 (eigenschappen, koppeling factuurregel, mail aan Jetse van Tilborg van Centric); 29 april 2026 (gereed voor consultatie); 12 augustus 2026 (volgende release) |
| `~/Downloads` | proposal en consultatie | `Proposal-inkooporder-regels.docx` (4 februari 2026) en `.pdf` (13 mei 2026) zijn inhoudelijk gelijk; `ggm-proposal-inkooporder.png` (13 mei 2026) |

## 2. Toetsing aan cookbook en conventies

| Regel | Bevinding | Gevolg |
|---|---|---|
| m1 definities | het proposal geeft geen definitie van de regel | definitie opgesteld: "Regel van een inkooporder voor één artikel of dienst, met aantal, prijs en btw" |
| m3 datatypes | geen datatypes in het proposal | MIM-datatypes: `Integer`, `CharacterString` met `Lengte`, `Decimal`, `Date`; bedragen in het GGM-datatype `Bedrag`, zoals bij `Factuurregel` |
| m4 attributen | n.v.t. | negen attributen |
| m7 kardinaliteit | infographic: "één inkooporder bevat één of meerdere inkooporderregels" | `Inkooporder` 1 – `Inkooporderregel` 1..* |
| naamgeving | `Inkooporderregel` PascalCase; attributen camelCase | de btw-attributen volgen de bestaande `Factuurregel` (`bedragExBTW`, `bedragBTW`, `BTWPercentage`) zodat beide regelsoorten gelijk zijn te mappen (keuze 1) |
| p1 gelaagdheid | alleen verwijzingen binnen Model Financien | in orde; geen relatie naar `Artikel` in Model Dienstverlening (horizontaal naast Financiën), `artikelcode` blijft een attribuut |

## 3. Vertaling naar het GGM

### 3.1 Objecttype `Inkooporderregel` (Model Financien)

Definitie: "Regel van een inkooporder voor één artikel of dienst, met het bestelde aantal, de prijs en de btw. Een
inkooporder bestaat uit een of meer inkooporderregels; de kop bevat de algemene ordergegevens."

| Attribuut | Datatype | Definitie |
|---|---|---|
| `regelnummer` | `Integer` | Volgnummer van de regel binnen de inkooporder. |
| `artikelcode` | `CharacterString` (80) | Code van het bestelde artikel of de dienst. |
| `omschrijving` | `CharacterString` (200) | Omschrijving van het bestelde artikel of de dienst. |
| `aantal` | `Decimal` | Bestelde hoeveelheid. |
| `eenheid` | `CharacterString` (20) | Eenheid van de hoeveelheid, zoals stuks, uur of m2. |
| `prijsPerEenheid` | `Bedrag` | Prijs per eenheid exclusief btw. |
| `bedragExBTW` | `Bedrag` | Bedrag van de regel exclusief btw. |
| `bedragBTW` | `Bedrag` | Btw-bedrag van de regel. |
| `BTWPercentage` | `Decimal` | Btw-percentage dat op de regel van toepassing is. |
| `datumLevering` | `Date` | Afgesproken of verwachte leverdatum van de regel. |
| `status` | `CharacterString` (80) | Status van de regel, zoals besteld, geleverd of gefactureerd. |

### 3.2 Relaties

| Bron | Relatie | Doel | Kardinaliteit | Opmerking |
|---|---|---|---|---|
| Inkooporder | heeft | Inkooporderregel | 1 – 1..* | infographic |
| Inkooporderregel | wordt geschreven op | Hoofdrekening | 0..* – 0..1 | kostensoort per regel; de kop houdt `wordt geschreven op` Hoofdrekening 1..* |
| Inkooporderregel | heeft | Kostenplaats | 0..* – 0..1 | kostenplaats per regel, naast de kop |
| Factuurregel | betreft | Inkooporderregel | 0..* – 0..1 | koppeling uit de expertgroep van 4 februari 2026 |

### 3.3 Diagram

`Inkooporderregel` en `Factuurregel` op *Financien Verplichtingen en Facturen*, rechts van `Inkooporder` en
`Leverancier`, met de vier relaties en de bestaande relatie `Factuur` heeft `Factuurregel`.

## 4. Keuzes bij Arjen

1. **Naamgeving btw-attributen.** Gelijk aan `Factuurregel` (`bedragExBTW`, gedaan) of volgens de conventie voluit
   (`bedragExclusiefBTW`), dan ook `Factuurregel` aanpassen.
2. **Attributen van de kop.** `artikelcode` en `goederencode` op `Inkooporder` laten staan (gedaan, achterwaarts
   compatibel) of verwijderen nu ze op de regel staan.
3. **Status als enumeratie** in plaats van `CharacterString`, als de expertgroep een vaste lijst wil.
4. **Relatie naar `Artikel`** (Model Dienstverlening) in plaats van `artikelcode`, als de gelaagdheid dat toelaat.

## 5. Uitvoering

Uitgevoerd op 4 november 2026 met `tools/fixes/add_inkooporderregels.py` (objecttype, elf attributen, vier relaties,
diagram), na een kopie van de .qea. Nog te doen: diagrambeeld exporteren, `task generate:docs`, DDL en Linked Data,
GitHub-issue, de indieners en Jetse van Tilborg (Centric) informeren.
