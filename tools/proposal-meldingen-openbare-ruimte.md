# Proposal Meldingen Openbare Ruimte (Katwijk en Land van Cuijk): status en verwerkingsvoorstel voor v3.0.0

Notitie van 4 november 2026. Getoetst is `Voorstel_wijziging_GGM_Meldingen_Openbare_Ruimte_Katwijk_Land_van_Cuijk.docx`
(versie 0.1, 1 mei 2026; primair gemeente Katwijk met Fixi, secundair gemeente Land van Cuijk met Buitenbeter en
Binnenbeter; gereviewd door Inge van Creij-Maas op 18 augustus 2026) tegen `v3.0.0/Gemeentelijk Gegevensmodel.qea`,
het GGM Cookbook (ontwerpregels, lijst ondersteunde primitieve datatypes), de naamgevingsconventies van het GGM
(2023, MIM-alternatief 2) en het Utrechtse *Conventiedocument datamodelleren* v0.2.

## Samenvatting

- **Besloten, niet uitgevoerd.** De 23e expertgroep van 12 augustus 2026 besloot: "voor de release het proposal
  melding openbare ruimte met concrete invulling toepassen; DIDO in combinatie met het bezet-patroon (RGBJ)
  apart agenderen richting een generieke oplossing" (actie Michiel en Mark voor 7 oktober). In de .qea is niets
  gewijzigd: `MOR-AanvraagOfMelding` (Model Dienstverlening, Object_ID 14307) heeft nog de vier attributen
  `locatie`, `locatieOmschrijving`, `meldingOmschrijving`, `meldingTekst`; `AanvraagOfMelding` (14298) kent geen
  behandelaar, team, eerste reactie, prioriteit, normtijd of resultaat. Geen issue, geen commit.
- **Klein en recht-toe-recht-aan.** Negen velden uit het voorstel worden in GGM-termen vijf attributen en twee
  relaties op `AanvraagOfMelding` en drie attributen op `MOR-AanvraagOfMelding`, alle met MIM-datatypes. Het
  adres gaat via de groepattribuutsoort `Adresaanduiding` (Model Kern RSGB), die het model al zeven keer als
  attribuuttype gebruikt; `Adres_Toelichting` en `Geometrie` zijn al gedekt door `locatieOmschrijving` en
  `locatie`.
- **Conventies.** De veldnamen uit het voorstel (snake_case met hoofdletters, `Behandelaar_ID`, `Is_Anoniem`)
  worden camelCase-attribuutsoorten; technische sleutels worden relaties naar `Medewerker` en
  `OrganisatorischeEenheid` (Model Kern RGBZ); ja/nee-velden worden `indicatieXxx : Boolean`; tijdstippen
  `datumXxx : DateTime`; tekst `CharacterString` met het metagegeven `Lengte`.
- **Bijvangst, apart op te pakken.** (a) `MORAanvraagOfMelding` in Model VTH (13058) is een kopie van
  `MOR-AanvraagOfMelding` met één extra attribuut `CROW`. (b) `AanvraagOfMelding` (horizontaal, Dienstverlening)
  verwijst naar `Indiener` en `AOMStatus` in Model VTH (verticaal), tegen ontwerpregel p1. (c) MOR staat niet op
  de domeinpagina Dienstverlening; de indieners zochten het daarom tevergeefs en kwamen uit bij *schouwen en
  meldingen* in Beheer Openbare Ruimte, dat iets anders is.

## 1. Wat is gecontroleerd

| Bron | Zoekactie | Uitkomst |
|---|---|---|
| `t_object`, `t_attribute`, `t_connector` | `MOR-AanvraagOfMelding`, `AanvraagOfMelding` en alle klassen met *Melding* | geen van de voorgestelde velden aanwezig; 11 specialisaties van `AanvraagOfMelding` |
| `t_diagram`, `t_package` | diagram met `MOR-AanvraagOfMelding` | `MOR 2.0` (Diagram_ID 1866) staat in het package `8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing` › `Meldingen Openbare Ruimte` › `Diagram`; dat package bevat verder niets, de klassen zelf staan in `Model Dienstverlening` |
| `docs/domeinen/dienstverlening.md`, `ruimteAlgemeen.md` | *MOR*, *openbare ruimte* | MOR niet beschreven in Dienstverlening; *schouwen en meldingen* in Beheer Openbare Ruimte gaat over `Melding` (14029) aan beheerobjecten |
| git-historie, GitHub-issues | *melding*, *Katwijk*, *Fixi* | niets |
| Obsidian (`01_Projects/GGM`) | expertgroep | besluit 12 augustus 2026; geen verslag van een expertgroep op 7 oktober 2026 gevonden |

## 2. Huidige situatie in het model

`AanvraagOfMelding` (Model Dienstverlening, definitie "Komt overeen met een VJV"): `identificatie : AN40`,
`soort : AN80`, `kanaal : AN80`, `onderwerp : AN200`, `onderwerpcode : AN80`, `hoofdcategorie : AN80`,
`hoofdcategoriecode : AN80`, `categorie : AN200`, `categoriecode : AN80`, `subcategorie : AN200`,
`subcategoriecode : AN80`, `status : AN80`, `statuscode : AN80`, `statusVolgorde : AN80`, `datumAanmaak : Date`,
`datumBeginStatus : Date`, `datumEindeStatus : Date`, `datumAfhandeling : Date`, `afgehandeld : Boolean`.
Relaties: `melder` → Rechtspersoon 0..1, `ingediend door` → Indiener 1, `heeft` → AOMStatus 1..*,
`heeft documenten` → Document, `kan leiden tot` → Zaak, `betreft` → Onderwerp, `heeft data` → Aanvraagdata,
`aanvraag met` → Formuliersoort; Klantcontact `kan leiden tot` AanvraagOfMelding.

`MOR-AanvraagOfMelding` (specialisatie, definitie "Bericht van een inwoner over een gebrek of opvallendheid in de
openbare ruimte"): `locatie : Punt`, `locatieOmschrijving : AN300`, `meldingOmschrijving : AN40`,
`meldingTekst : AN4000`.

De bestaande attributen gebruiken nog de oudere GGM-varianten (`AN80`, `Punt`). Het cookbook accepteert die als
varianten van de MIM-primitieven; de nieuwe attributen krijgen de MIM-namen. Zie keuze 5 voor het gelijktrekken
van de bestaande attributen.

## 3. Vertaling van het voorstel naar het GGM

Datatypes volgen de MIM-primitieven uit `docs/cookbook/modelelementen.md`: `CharacterString` (lengte als
metagegeven `Lengte`), `Boolean`, `DateTime`. Het adres is de groepattribuutsoort `Adresaanduiding`; geometrie
blijft het bestaande `locatie` (`Punt`, MIM-extensie `GM_Point`).

| Veld in het voorstel | Beoogde tabel | GGM-element | Naam : datatype | Motivering |
|---|---|---|---|---|
| Behandelaar_ID | AANVRAAGOFMELDING | relatie `AanvraagOfMelding` *behandelaar* → `Medewerker` (Model Kern RGBZ) | 0..* – 0..1 | geen technische sleutel in het model; de DDL-generator maakt er een verwijzende kolom van, waarin de behandelaar-ID van Fixi of Binnenbeter als `medewerkerIdentificatie` landt; `Medewerker` kent al `extern`. Alternatief: `behandelaar : CharacterString` (200) met alleen de naam, zoals de voetnoot van de indieners voorstelt |
| Team / Behandelaar_Groep | AANVRAAGOFMELDING | relatie *behandelend team* → `OrganisatorischeEenheid` (Model Kern RGBZ) | 0..* – 0..1 | zelfde redenering; `Team` uit Jeugd en Wmo is verticaal en niet bereikbaar (p1). Alternatief: `behandelendTeam : CharacterString` (200) |
| Datum_Eerste_Reactie | AANVRAAGOFMELDING | attribuut | `datumEersteReactie : DateTime` | conventie `datumXxx`; datum en tijd volgens de omschrijving |
| Hoge_Prioriteit | AANVRAAGOFMELDING | attribuut | `indicatieHogePrioriteit : Boolean` | conventie `indicatieXxx : Boolean` |
| Normtijd | AANVRAAGOFMELDING | attribuut | `datumNormAfhandeling : DateTime` | het is een tijdstip ("waarop redelijkerwijs verwacht mag worden dat een melding is behandeld"), dus `datumXxx`; alternatief `normtijd` |
| Resultaat | AANVRAAGOFMELDING | attribuut | `resultaat : CharacterString` (80) | gelijk aan `status`; waardelijst verschilt per gemeente en applicatie, enumeratie later als de expertgroep een lijst wil |
| Adres, Straatnaam, Huisnummer, Postcode, Stad | MOR_AANVRAAGOFMELDING | attribuut met groepattribuutsoort | `adres : Adresaanduiding` | `Adresaanduiding` (Model Kern RSGB, groepattribuutsoort) bevat `straatnaam`, `gemeentenaam`, `huisnummer`, `huisletter`, `huisnummertoevoeging`, `postcode`, `BAGID`; de generator vouwt dit uit tot losse kolommen (Utrechts conventiedocument, stereotype Adresaanduiding). Alternatief: relatie naar `Nummeraanduiding` (Model BAG), strenger maar niet passend bij vrije adresinvoer in meldapps |
| Adres_Toelichting | MOR_AANVRAAGOFMELDING | bestaand | `locatieOmschrijving` | dekt "op de stoep"; geen nieuw attribuut |
| Geometrie | MOR_AANVRAAGOFMELDING | bestaand | `locatie` (`Punt`, MIM-extensie `GM_Point`) | geen nieuw attribuut; de generator levert lat/long en RD-kolommen |
| Datum_Ingepland | MOR_AANVRAAGOFMELDING | attribuut | `datumIngepland : DateTime` | |
| Is_Anoniem | MOR_AANVRAAGOFMELDING | attribuut | `indicatieAnoniem : Boolean` | `melder` 0..1 bestaat al; de indicatie legt vast dát het anoniem is, ook als er wel een melder bekend is bij de applicatie |

Definities voor de nieuwe attributen komen uit de kolom *Beschrijving* van het voorstel; die zijn bruikbaar.
`datumAanmaak`, `datumAfhandeling` en `status` blijven zoals ze zijn.

## 4. Uitvoering

1. **GitHub-issue** aanmaken, *Proposal Meldingen Openbare Ruimte (Katwijk, Land van Cuijk)*, labels `Proposal`
   en `Expertgroep`, met het besluit van 12 augustus 2026 en de vertaling uit hoofdstuk 3.
2. **Model aanpassen** op `v3.0.0/Gemeentelijk Gegevensmodel.qea`, na een kopie zoals bij issue 53 en 57.
   Twee routes:
   - *Script* `tools/fix_proposal_mor.py` naar het patroon van `tools/fix_issues_50_49_13.py`: de acht
     attributen invoegen via een sjabloonrij uit dezelfde klasse (met `t_attributetag`, waaronder `Lengte`, en
     `t_xref`), de twee relaties naar `Medewerker` en `OrganisatorischeEenheid` als `t_connector` met
     kardinaliteiten. Daarna in EA openen, diagram `MOR 2.0` bijwerken (Medewerker en OrganisatorischeEenheid
     erop) en de EA-check doen.
   - *Handmatig in EA*: acht attributen en twee relaties, ongeveer een half uur.
   Uitgevoerd op 4 november 2026 met `tools/fix_proposal_mor.py` (zeven attributen, twee relaties, diagram
   `MOR 2.0` bijgewerkt).
3. **Documentatie.** Paragraaf *Meldingen openbare ruimte* in `docs/domeinen/dienstverlening.md` met het
   diagram `MOR 2.0`, zodat MOR vindbaar is; daarna `task generate:docs` en `task publish:local`. DDL opnieuw
   genereren (`AANVRAAGOFMELDING`, `MOR_AANVRAAGOFMELDING`), Linked Data met `task generate:lod`, vertalingen
   met `task generate:translations`.
4. **Afronden.** Issue sluiten met de commit, Katwijk en Inge van Creij-Maas informeren, wiewatstatus bijwerken.
5. **Apart issue** voor de bijvangst: de kopie `MORAanvraagOfMelding` in Model VTH en de verwijzingen van
   `AanvraagOfMelding` naar Model VTH (`Indiener`, `AOMStatus`). Dat past bij de todo *dubbele voorkomens
   objecttypen* en hoort niet in dit proposal.

## 5. Keuzes bij Arjen

1. **Behandelaar en team** als relaties naar `Medewerker` en `OrganisatorischeEenheid` (aanbevolen) of als
   tekstattributen met alleen een naam, zoals de indieners in hun voetnoot overwegen.
2. **Adres** als `Adresaanduiding` (aanbevolen), als relatie naar `Nummeraanduiding`, of als losse
   tekstattributen zoals in het voorstel.
3. **Resultaat** nu als `CharacterString`, of meteen een enumeratie met een landelijke waardelijst.
4. **Naam** `datumNormAfhandeling` of `normtijd`.
5. **Bestaande attributen gelijktrekken.** Alleen de nieuwe attributen in MIM-namen (aanbevolen voor dit
   proposal), of in dezelfde wijziging ook `AN..`, `Punt` en `Date` van de twee klassen omzetten naar
   `CharacterString` met `Lengte`, `GM_Point` en `Date`/`DateTime`.
6. **Script of handwerk** voor de modelwijziging.
7. **DIDO en bezet-patroon** blijven buiten dit proposal; de stand sinds 7 oktober is in de notities niet terug
   te vinden.
