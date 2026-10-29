# IRI's met een volgnummer in de LOD: analyse, modelacties en keuzes

Notitie van 29 oktober 2026, naar aanleiding van de toetsing *IRI-opbouw MIM-publicatie BAG: toetsing aan de
afgesproken regel*. Getoetst op de gegenereerde LOD van v3.0.0 (crunch_uml 0.8.6), op `v3.0.0/Gemeentelijk
Gegevensmodel.qea` en op de IRI-code in crunch_uml (`crunch_uml/renderers/lodrenderer.py`, `propertyUris`).

## Samenvatting

- De toetsing is in de uitkomst terecht: twee IRI's in de BAG-view eindigen op `-2`, Standplaats wijkt af in de
  naamgeving van de geldigheidsattributen, en er is geen vastlegging van IRI's per modelelement.
- De oorzaak is een andere dan het document stelt. De `-2` is geen teller van de generator, maar het gevolg van
  dubbele relaties. Tien BAG-klassen staan ook in het archiefpakket `RSGB Model › archief › Model Kern RSGB`, en
  25 relaties uit het hele GGM wijzen naar allebei de versies. Daardoor hebben 25 relaties in de hele ontologie
  een volgnummer, niet alleen de twee in BAG.
- Drie van de vijf afgekeurde IRI's volgen de regel zoals crunch_uml die documenteert: gelijknamige relaties
  vanuit één klasse krijgen de doelklasse als achtervoegsel. Die stap ontbreekt in de regel waaraan het document
  toetst.
- Voorstel: de dubbele relaties uit het model halen, de geldigheidsattributen in Model BAG gelijk benoemen, de
  achtervoegselregel in de afspraak opnemen, over het archiefpakket beslissen, en crunch_uml per EA-GUID laten
  melden welke IRI's veranderen. Beslissen vóór de release van v3.0.0: 10 IRI's veranderen dan eenmalig en 16
  verdwijnen.

## 1. Hoe een property-IRI tot stand komt

De regel staat in de handleiding van crunch_uml (`docs/handleiding/export.md`, onderdeel *Linked Data*). Een
attribuut of relatie krijgt `{pad}/{klasse}/{naam}`, waarbij de naam een slug wordt: kleine letters, spaties en
leestekens naar `-`, haakjes weg. Attributen en uitgaande relaties van een klasse delen één naamruimte. Dan zijn er
drie stappen:

1. **Geen botsing:** `{klasse}/{naam}`, bijvoorbeeld `kern/bag/buurt/ligt-in`.
2. **Botsing binnen de klasse:** gelijknamige relaties krijgen de doelklasse als achtervoegsel
   (`nummeraanduiding/ligt-in-buurt`, `nummeraanduiding/ligt-in-woonplaats`); gelijknamige attributen hun datatype
   of doelklasse; naamloze relaties heten `{rol of relatie}-{doelklasse}`.
3. **Botsing na stap 2:** een volgnummer `-2`, `-3`. De volgorde is die van de EA-GUID's van de relaties
   (alfabetisch): willekeurig, maar bij elke generatie gelijk zolang het model niet verandert.

Stap 2 meldt crunch_uml in één waarschuwing (in het GGM: 106 klassen met gelijknamige relaties). Stap 3 meldt het
niet, en juist die gevallen hadden moeten opvallen.

De regel in het document (`{base}/kern/bag/{klasse}/{naam}`, uniek binnen de klasse, eenmalig afgeleid en vast)
kent stap 2 en 3 niet. Zonder stap 2 kunnen twee relaties die allebei *Ligt in* heten nooit allebei een IRI
krijgen. Óf de afspraak krijgt die stap erbij, óf het model krijgt unieke relatienamen per klasse (keuze 1).

## 2. De vijf afgekeurde IRI's

| IRI in de BAG-view | Wat er in het model staat | Oordeel |
|------------------------------|--------------------------------------------------|------------------|
| `nummeraanduiding/ligt-in-buurt` | *Ligt in* naar Buurt én naar Woonplaats (en *ligt in* naar Gebied in RSGB) | Stap 2, volgens de regel |
| `nummeraanduiding/ligt-in-woonplaats` | idem | Stap 2, volgens de regel |
| `openbareruimte/ligt-in-woonplaats` | *Ligt in* naar Buurt én naar Woonplaats | Stap 2, volgens de regel |
| `openbareruimte/ligt-in-buurt-2` | twee relaties *Ligt in* naar een klasse Buurt: connector 11110 naar de Buurt in het archief, 11123 naar de Buurt in Model BAG | Stap 3, modelfout |
| `pand/zonder-verblijfsobject-ligt-in-buurt-2` | twee relaties *zonder verblijfsobject ligt in*: 11106 naar de archief-Buurt, 11122 naar de BAG-Buurt | Stap 3, modelfout |

Bij de laatste twee krijgen beide relaties het achtervoegsel `-buurt`; de GUID-volgorde geeft hier de relatie naar
de archief-Buurt `ligt-in-buurt` en de relatie naar de BAG-Buurt `-2`. In de BAG-view staat alleen de
`-2`-variant, omdat de archief-Buurt niet op het diagram staat. Daardoor oogt het als een losse teller.

Drie beweringen in het document kloppen daarom niet:

- *"Het -2 is niet nodig voor uniciteit binnen de klasse"*: dat is het wel, er zijn twee relaties met dezelfde naam
  naar twee klassen die allebei Buurt heten.
- *"Bij Pand staat -buurt er wel in, terwijl daar niets te onderscheiden valt"*: ook Pand heeft twee relaties
  naar twee Buurt-klassen.
- *"Een -2 hangt af van een teller, die bij een volgende generatie bij een ander element kan terechtkomen"*: de
  volgorde ligt vast en verschuift alleen als een van de twee relaties verdwijnt. Dat is precies de ingreep die
  nodig is, dus de IRI verandert één keer.

## 3. De oorzaak: tien BAG-klassen staan ook in het archiefpakket

Onder `RSGB Model` staat een pakket `archief` met daarin een tweede `Model Kern RSGB`. Dat pakket bevat veertien
klassen: de tien BAG-objecttypen in hun oude RSGB 3.0-vorm, plus hun oude supertypen AdresseerbaarObjectAanduiding,
BenoemdObject, BenoemdTerrein en GebouwdObject.

| Klasse | Model BAG: attributen / op diagrammen / inkomende relaties | Archief: attributen / op diagrammen / inkomende relaties |
|------------------|----------------------------------------|----------------------------------------|
| Buurt | 11 / 15 / 6 | 7 / 0 / 6 |
| Gemeente | 11 / 13 / 5 | 7 / 1 / 5 |
| Ligplaats | 11 / 16 / 3 | 6 / 0 / 2 |
| Nummeraanduiding | 16 / 27 / 7 | 11 / 0 / 4 |
| OpenbareRuimte | 20 / 19 / 5 | 16 / 0 / 3 |
| Pand | 20 / 14 / 4 | 23 / 0 / 4 |
| Standplaats | 11 / 16 / 3 | 3 / 0 / 2 |
| Verblijfsobject | 19 / 18 / 3 | 10 / 0 / 2 |
| Wijk | 11 / 13 / 3 | 7 / 0 / 3 |
| Woonplaats | 17 / 19 / 11 | 9 / 0 / 8 |

De archiefklassen staan op geen enkel diagram, behalve de archief-Gemeente op het diagram *Inburgering*. Ze dragen
de attribuutnamen van RSGB 3.0 (`datumBeginGeldigheidPand`, `pandidentificatie`, `pandstatus`). De archief-Pand
heeft ook IMGeo/BGT-attributen die de BAG-Pand mist (LOD1/LOD2/LOD3-geometrie, bouwlagen,
`relatieveHoogteliggingPand`). Standplaats staat bovendien nog een keer in Model Musea, met 3 attributen; dat is
vermoedelijk een ander begrip en hoort niet in deze lijst.

Het archief gaat gewoon mee in de uitvoer. In de LOD zijn het tien klassen met een eigen IRI naast de BAG-klasse:
`kern/bag/pand` en `kern/rsgbplus/rsgb/archief/kern-rsgb/pand`, allebei `mim:Objecttype` met het label *Pand*. Ze
staan in de ontologie en in `ggm-geheel`, en door het diagram Inburgering staat de archief-Gemeente ook in die view.
In de documentatie is er een pagina *Model Kern RSGB (archief)* buiten de navigatie.

### De 25 dubbele relaties

Elke rij is één relatie die twee keer in het model staat: een keer naar de BAG-klasse, een keer naar de archiefklasse.
De kolom *-2 zit nu op* zegt welke van de twee het volgnummer draagt.

| Bron (model) | Relatie | Naar BAG-klasse | Naar archief | -2 zit nu op |
|------------------------------|------------------------------|---------|---------|----------|
| Adresaanduiding (Groepattribuutsoort) | verwijst naar Nummeraanduiding | 11128 | 11009 | BAG |
| Areaal (Beheer Openbare Ruimte) | ligt in Buurt | 11538 | 11536 | archief |
| Areaal (Beheer Openbare Ruimte) | valt binnen Wijk | 11537 | 11535 | archief |
| Asielstatushouder (Inburgering) | is gekoppeld aan Gemeente | 11947 | 11953 | BAG |
| Beschermde Status (Monumenten) | betreft OpenbareRuimte | 12079 | 12078 | archief |
| Binnenlocatie (Sport) | bedient Wijk | 12025 | 12022 | archief |
| Binnenlocatie (Sport) | is gevestigd in Verblijfsobject | 12026 | 12023 | archief |
| Briefadres (Kern RSGB) | (naamloos) naar Nummeraanduiding | 11131 | 11008 | archief |
| Gebied (Kern RSGB) | komt overeen Buurt | 11125 | 10999 | archief |
| GeboorteIngeschrevenNatuurlijkPersoon (Groepattribuutsoort) | heeft plaatsgevonden in Woonplaats | 11090 | 10980 | BAG |
| Huishouden (Sociaal Domein Generiek) | heeft als adres Nummeraanduiding | 11729 | 11728 | archief |
| Object (Kern RGBZ) | is Buurt | 11124 | 11031 | archief |
| Object (Kern RGBZ) | is Ligplaats | 11117 | 11034 | archief |
| Object (Kern RGBZ) | is OpenbareRuimte | 11108 | 11032 | BAG |
| Object (Kern RGBZ) | is Pand | 11103 | 11040 | BAG |
| Object (Kern RGBZ) | is Standplaats | 11100 | 11036 | archief |
| OntbindingHuwelijk/geregistreerdPartnerschap (Groepattribuutsoort) | is ontbonden in Woonplaats | 11093 | 10976 | archief |
| OpenbareRuimte (BAG) | Ligt in Buurt | 11123 | 11110 | BAG |
| Pand (BAG) | zonder verblijfsobject ligt in Buurt | 11122 | 11106 | BAG |
| Postadres (Groepattribuutsoort) | heeft als correspondentieadres postadres in Woonplaats | 11095 | 10979 | BAG |
| Schuldhulptraject (Schuldhulpverlening) | onder verantwoordelijkheid van Gemeente | 11756 | 11760 | BAG |
| SluitingOfAangaanHuwelijkOfGeregistreerdPartnerschap (Groepattribuutsoort) | is gesloten/aangegaan in Woonplaats | 11092 | 10975 | archief |
| VerblijfadresIngeschrevenNatuurlijkPersoon (Groepattribuutsoort) | verblijft in Verblijfsobject | 11098 | 10981 | BAG |
| VerblijfadresIngeschrevenNatuurlijkPersoon (Groepattribuutsoort) | verblijft op Ligplaats | 11118 | 10991 | archief |
| VerblijfadresIngeschrevenNatuurlijkPersoon (Groepattribuutsoort) | verblijft op Standplaats | 11101 | 10984 | archief |

In 10 van de 25 paren draagt de relatie naar de BAG-klasse het volgnummer, in 15 de relatie naar het archief. Bij
Asielstatushouder, Geboorte en Sluiting is de naam van de archiefvariant net anders (een spatie aan het eind), wat
in de slug wegvalt.

Drie gevallen hebben een andere oorzaak:

- **WOZ-object *bevat* KadastraleOnroerendeZaak** staat twee keer identiek in het model (connectors 10951 en
  10952), vandaar `woz-object/bevat-kadastraleonroerendezaak-2`.
- **IngeschrevenPersoon *Ouder 1* en *Ouder 2*** zijn echte namen; `ouder-1` en `ouder-2` zijn goed.
- **GebouwdObject (archief) *heeft*** wijst naar de enumeratie *gebruiksdoel* (10997) én naar de klasse
  *Gebruiksdoel* in Model Vastgoed (11363). Geen IRI-probleem; verdwijnt met het archief.

Ook de generalisatie *OverigeAdresseerbaarObjectAanduiding → Nummeraanduiding* staat drie keer: twee keer naar de
BAG-Nummeraanduiding (10918, 10919) en een keer naar de archiefversie (10920).

## 4. Wat het nu betekent voor de LOD

- 28 property-IRI's in de ontologie eindigen op een volgnummer; 25 door het archief, 1 door de dubbele
  WOZ-connector, 2 terecht (Ouder 1, Ouder 2).
- Een gebruiker ziet twee properties *ligt in* op Areaal, met als range `archief/kern-rsgb/buurt` en
  `kern/bag/buurt`, en kan niet zien welke bedoeld is. In de views staat alleen de `-2`-variant, zonder tegenhanger.
- Hetzelfde begrip heeft twee IRI's: `kern/bag/pand` en `kern/rsgbplus/rsgb/archief/kern-rsgb/pand`.

## 5. Wat er in het model moet gebeuren

**A. Dubbele relaties verwijderen.** Per paar in de tabel de connector naar het archief weghalen (25 connectors),
plus connector 10952 (WOZ-object) en generalisatie 10919. Daarna is elk volgnummer weg, behalve `ouder-1` en
`ouder-2`. Gevolg in de LOD: 10 IRI's verliezen hun `-2`, 16 IRI's verdwijnen.

**B. Namen in Model BAG gelijktrekken.** Negen klassen gebruiken `beginGeldigheid`, `eindGeldigheid`,
`datumIngang`, `datumEinde` en `documentdatum`. Afwijkend:

| Klasse | Nu | Wordt |
|----------------|--------------------------------------------|----------------------------------------|
| Standplaats | Datum Begin Geldigheid, Datum Einde Geldigheid, Datum Ingang, Datum Einde | beginGeldigheid, eindGeldigheid, datumIngang, datumEinde |
| Nummeraanduiding | eindeGeldigheid | eindGeldigheid |
| OpenbareRuimte | begingeldigheid | beginGeldigheid |

De laatste twee vallen in de IRI weg door de kleine letters, maar staan wel zo in `mim:naam` en het label. Verder
heet de relatie van OverlijdenIngeschrevenNatuurlijkPersoon naar Woonplaats *heeft plaatsegevonden in* (connector
11096, tikfout), wat de IRI `heeft-plaatsegevonden-in` oplevert.

**C. Het archief loskoppelen of opruimen** (keuze 2). Na A wijzen nog zes verbindingen van levende klassen naar het
archief: Vestiging *heeft als locatie-adres* Nummeraanduiding (11007), Vastgoedobject *betreft* Pand (11334),
Beschermde Status *betreft* Pand (12074), OverlijdenIngeschrevenNatuurlijkPersoon *heeft plaatsgevonden in*
Woonplaats (10977), VerblijfadresIngeschrevenNatuurlijkPersoon *verblijft op locatie in* Woonplaats (10978) en de
generalisatie 10920. Die horen naar de BAG-klasse te wijzen. Andersom wijst het archief naar levende klassen:
Wijk *ligt in* Woonplaats (BAG, 11091), Nummeraanduiding *ligt in* Gebied (11013), Nummeraanduiding → Object
(RGBZ), Pand → Geo-Object (Beheer Openbare Ruimte), GebouwdObject *heeft* Gebruiksdoel (11363). Wordt het archief
verwijderd, dan gaan die vanzelf mee. Blijft het staan, dan moeten ook die weg om er een eiland van te maken.

68 attributen bestaan alleen in het archief. Meestal zijn het RSGB 3.0-namen van iets dat de BAG-klasse ook heeft
(`datumBeginGeldigheidBuurt`, `buurtcode`), maar de archief-Pand heeft IMGeo/BGT-attributen die de BAG-Pand niet
heeft. Per attribuut beslissen: overnemen in Model BAG of laten vervallen.

## 6. Keuzes

**Keuze 1: de IRI-regel bij gelijknamige relaties.**
(a) De achtervoegselregel van crunch_uml officieel maken: doelklasse als achtervoegsel alleen bij een botsing, en
een volgnummer alleen als teken van een modelfout.
(b) Unieke relatienamen per klasse afdwingen in het model, zoals het document voorstelt (*ligt in buurt*, *ligt in
woonplaats*). Dat raakt 106 klassen in het GGM, verandert honderden IRI's en maakt de modelnamen langer.
Advies: (a). Een variant van (a) is de doelklasse altijd toevoegen, ook zonder botsing; dat is consequenter, maar
maakt elke relatie-IRI langer en verandert ze allemaal.

**Keuze 2: het archiefpakket.**
(a) Minimaal: alle verbindingen van levende klassen naar het archief weghalen (5A plus de zes uit 5C). Het archief
blijft dan als eiland in het model staan, en dus ook in de ontologie en `ggm-geheel`, met eigen IRI's voor Pand,
Buurt enzovoort.
(b) Het archiefpakket uit het model verwijderen. De oude versie blijft beschikbaar in git en in de releases v2.x.
Eerst de 68 archief-attributen nalopen (5C).
(c) Het archief laten staan en buiten de LOD en de docs houden. De views slaan het nu al over omdat er geen
diagram is, maar de ontologie en `ggm-geheel` nemen elk pakket mee; dit vraagt een nieuwe uitsluitoptie in
crunch_uml.
Advies: (a) nu, vóór v3.0.0; (b) als besluit voor de volgende release, met de attribuutlijst als werkvoorraad.

**Keuze 3: naamgeving van de geldigheidsattributen.** De conventie van de negen BAG-klassen (`beginGeldigheid`
enzovoort) aanhouden, zoals in de BAG-catalogus. Advies: ja, 5B uitvoeren.

**Keuze 4: stabiliteit van IRI's.** Dit is het open punt uit issue 53. De IRI volgt de naam, dus hernoemen is een
nieuwe IRI. Elke term in de ttl draagt al de EA-GUID als `dcterms:identifier`, ook relatiesoorten. Opties:
(a) Naam-IRI's houden en crunch_uml bij het genereren de nieuwe ttl naast de vorige publicatie laten leggen: per GUID
melden welke IRI veranderde. Het register is dan de vorige publicatie zelf.
(b) GUID-gebaseerde IRI's: stabiel, maar onleesbaar.
(c) Naam-IRI's plus een aliasgraph met `dcterms:replaces` voor hernoemde termen.
Advies: (a) nu bouwen; (c) erbij zodra de eerste hernoeming na publicatie zich voordoet.

**Keuze 5: moment.** Vóór de release van v3.0.0. Na 5A veranderen 10 IRI's sowieso; beter nu dan na het eerste
gebruik.

## 7. Controle na de ingreep

```bash
task --force import:model generate:lod
grep -o -E '<https://lod\.gemeentelijkgegevensmodel\.nl/[a-z0-9/-]+-[0-9]+> a (mim:Relatiesoort|mim:Attribuutsoort)' \
  "v3.0.0/Gemeentelijk Gegevensmodel Linked Data.ttl" | sort -u
```

Verwacht: alleen `ingeschrevenpersoon/ouder-1` en `ouder-2`. De waarschuwing over gelijknamige relaties blijft; die
gaat over stap 2 en is terecht.
