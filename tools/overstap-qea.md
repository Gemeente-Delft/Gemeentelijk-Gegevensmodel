# Overstap van import:model naar de .qea: vergelijking en testplan

Datum: 29 oktober 2026. Status: analyse, er is niets omgezet.

De pijplijn importeert nu `Gemeentelijk Gegevensmodel XMI2.1.xml` (EA-export van 21 januari 2026).
Het plan is `Gemeentelijk Gegevensmodel.qea` rechtstreeks te importeren en de XMI alleen nog als
download te bewaren. Beide bronnen zijn met crunch_uml 0.8.1 ingelezen in één database en, zoals
`import:model` doet, gekopieerd naar het wortelpakket (`transform -ttp copy -rt_pkg`). De vergelijking
staat in `tools/overstap-qea-bijlage-vergelijking.md`; hieronder de duiding en het testplan.

## Samenvatting

De structuur is gelijk: 296 pakketten, 304 generalisaties en 243 diagrammen komen één op één overeen,
963 van de 969 klassen en 4.533 attributen delen hun GUID. De overstap is dus geen herbouw. Wel zijn er
drie gaten in de qea-parser van crunch_uml die eerst dicht moeten, één daarvan blokkerend:

1. **Attribuuttypen gaan verloren na de kopie naar het wortelpakket (blokkerend).** De qea-parser legt
   het type van een attribuut alleen vast als verwijzing naar het classifier-element (3.627 attributen
   wijzen naar de datatypeklassen in *MIM11 Primitieve datatypen*, *GGM Datatypes* en *GML3*) en laat
   de typenaam leeg. Die pakketten liggen buiten het wortelpakket, de kopie neemt ze niet mee, en na de
   kopie hebben 3.623 attributen geen bruikbaar type meer (XMI: 16). Gevolg: in de documentatie is de
   typekolom leeg en de Linked Data telt 846 attribuutsoorten in plaats van 4.303. De `.qea` heeft de
   typenaam gewoon in `t_attribute.Type` (4.059 van 4.059); de parser moet die altijd overnemen.
2. **Codes van enumeratiewaarden worden niet gelezen.** De XMI-parser haalt de code (bijvoorbeeld `1`
   bij *Dagopleiding*) uit het `style`-element; in de `.qea` staat die in `t_attribute.Style` (780
   waarden). De qea-parser leest hem niet, dus `skos:notation` en `mim:code` verdwijnen uit de LOD.
3. **Rollen van associaties worden niet gelezen.** `t_connector.SourceRole`/`DestRole` zijn 11 en 32
   keer gevuld; de qea-parser slaat ze over. Naamloze associaties krijgen dan `relatie-...` als IRI
   en label in plaats van de rolnaam.

Daar staat tegenover dat de `.qea` rijker en actueler is: zes associatieklassen die de XMI-parser
overslaat (`uml:AssociationClass`: Gebruikerrol, Belangtype, Historische Rol, Rol, Aantal, Sport), twaalf
associaties, het stereotype *Relatiesoort* op alle relaties, kardinaliteit `*` in plaats van `-1`,
tagwaarden zonder de `#NOTES#`-ruis van de XMI, en de correcties van 28 oktober (issues 53, 50, 49, 13).
De XMI-parser levert daarentegen 656 associatie-einden als attribuut (`EAID_src…`/`EAID_dst…`) en 24
technische elementen (Boundary, ProxyConnector, Text) die bij de `.qea` vervallen. Dat is gewenst, maar
het verandert de documentatie en de LOD zichtbaar.

Los van de bron is er ruis die de pijplijn zelf maakt: de kopie naar het wortelpakket maakt van elke
enumeratie buiten scope een kopie per verwijzend pakket, met een willekeurig nieuw id (Boolean: 2 in de
bron, 21 na de kopie). Daardoor verschillen gegenereerde documenten bij elke run in hun id's en krijgen
enumeraties IRI's als `kern/bag/boolean`. Dat is een aandachtspunt voor crunch_uml, niet voor de overstap.

## Bevindingen in cijfers

| Onderdeel | XMI | .qea | Duiding |
|---|---|---|---|
| Pakketten, generalisaties, diagrammen | 296 / 304 / 243 | 296 / 304 / 243 | identiek |
| Klassen | 987 | 969 | 24 technische elementen alleen in XMI; 6 associatieklassen alleen in qea |
| Attributen | 5.189 | 4.542 | 656 associatie-einden alleen in XMI; 9 van de associatieklassen alleen in qea |
| Attributen zonder bruikbaar type na de kopie | 16 | 3.623 | gat 1 |
| Enumeratiewaarden met code | 779 | 0 | gat 2 |
| Associaties met rolnaam | 43 | 0 | gat 3 |
| Associaties | 1.073 | 1.083 | 2 ProxyConnector-relaties alleen in XMI; 12 nieuwe alleen in qea |
| Enumeraties | 601 | 598 | 388 gedeeld; de rest zijn kopieën met willekeurige id's (beide bronnen) |
| Klassen gewijzigd na 31 januari 2026 | n.v.t. | 21 | model-drift sinds de XMI-export |

Verschillen op gedeelde elementen die geen gat zijn: 40 klassen en 7 attributen met `#NOTES#`-ruis in de
XMI-tagwaarden (crunch_uml knipt die bij de LOD al weg), 9 definities, 2 klassenamen en 3 waardenamen
die op 28 oktober zijn gecorrigeerd, en 7 enumeraties die toen zijn hernoemd (`EnumLeefgebied`).

## Gevolgen per generator

- **generate:docs** (jinja2-markdown): 12.701 regels verschil tussen beide imports. Verwacht en gewenst:
  `modified`/`version` van de elementen, de associatie-einden verdwijnen als attribuut, de
  associatieklassen komen erbij. Ongewenst tot gat 1 dicht is: lege typekolommen. Altijd aanwezig:
  id-ruis van de enumeratiekopieën.
- **generate:lod**: met gat 1 dicht moet de export overeenkomen met de rechtstreekse qea-export van
  29 oktober (4.225 attribuutsoorten, 1.243 relatiesoorten, 135 views, dezelfde MIM-meldingengroepen).
  Rollen (gat 3) bepalen de IRI's van naamloze associaties; codes (gat 2) de `skos:notation`.
- **generate:excel**: zelfde kolommen; typekolom leeg zolang gat 1 open is.
- **generate:mim** (`earepo`-updater naar het MIM-draft-bestand): schrijft in een EA-bestand; alleen
  testen op een kopie.
- **generate:diff**: vergelijkt op id met de vorige versie, die uit de XMI van v2.5.0 komt. De
  enumeratiekopieën en de associatie-einden hebben per bron andere id's, dus de diff zal veel
  schijnwijzigingen tonen. Oplossing: de vorige versie ook uit een `.qea` importeren, of de diff
  beperken tot elementen met een echte EA-GUID.
- **generate:translations** (i18n): sleutels op id; dezelfde ruis als bij de diff voor de kopieën.

## Testplan

Elke stap heeft een acceptatiecriterium; pas door bij groen.

1. **crunch_uml aanpassen en uitbrengen (0.8.2).** qea-parser: `primitive` altijd uit `t_attribute.Type`
   (naast de classifier), `alias` van enumeratiewaarden uit `t_attribute.Style`, `src_role`/`dst_role` uit
   `SourceRole`/`DestRole`. Pariteitstest `test_40` uitbreiden met deze drie velden op de
   GGM-fixtures. Acceptatie: testsuite groen; op de GGM-database 0 attributen zonder type na de kopie,
   780 codes, 43 rollen.
2. **Verse XMI exporteren uit EA** en de vergelijking (`scratchpad`-scripts, bijlage) herhalen, zodat
   alleen parserverschillen overblijven. Acceptatie: de resterende verschillen zijn precies de bekende
   lijst (associatie-einden, technische elementen, `#NOTES#`, `-1` versus `*`, associatieklassen).
3. **Proefimport in een eigen database**: `task import:model` met de `.qea` naar een andere
   `CRUNCH_UML_DB`, en de vergelijking tegen de huidige database. Acceptatie: aantallen en
   gedeelde-elementverschillen zoals in stap 2, 0 attributen zonder type.
4. **Documentatie**: `generate:docs` op de proefdatabase, diff tegen de huidige `docs/definities`.
   Acceptatie: alleen de verwachte categorieën (`modified`/`version`, weggevallen associatie-einden,
   nieuwe associatieklassen, id-ruis van kopieën); geen lege typekolommen; steekproef van vijf
   domeinpagina's met de hand nagelezen, inclusief Inkomen (daar zitten de attributen zonder GUID).
5. **Linked Data**: `generate:lod` op de proefdatabase; `tools/validate_mim_lod.py` op ontologie en
   shapes; browser-harnas over de views; vergelijking per view met de huidige set op EA-GUID.
   Acceptatie: typeringen en aantallen gelijk aan de rechtstreekse qea-export, 135 views, geen
   relaties met `relatie-` waar EA een rol heeft, codes aanwezig.
6. **Overige generatoren**: `generate:excel` (typekolom gevuld), `generate:mim` op een kopie van het
   MIM-draft-bestand (geen fouten in de updater), `generate:diff` met besluit over de vorige versie,
   `generate:translations` alleen `UPDATE_I18N=True` (ontbrekende sleutels aanvullen, niets weggooien).
7. **Omzetten**: `import:model` op `-t qea` met `GGM_FILE` als bron, `sources` van de taak op het
   `.qea`-bestand, `CRUNCH_UML_VERSION` op 0.8.2; de XMI blijft in de release-map als download en
   verdwijnt uit de taken. Daarna `generate:lod`, `publish:lod`, live controle, `publish:local` als
   voorvertoning. Commit pas na stap 4 tot en met 6.

## Besluiten die hierbij horen

- De associatieklassen uit de `.qea` zijn in MIM-termen relatieklassen; crunch_uml typeert ze nu als
  objecttype. Als dat `mim:Relatieklasse` moet worden, is dat een aanvulling op de qea-parser.
- De enumeratiekopieën van de wortelkopie: deterministische id's (hash van bron-id en pakket) of
  één gedeelde kopie zou de id-ruis en de dubbele IRI's wegnemen. Los van de overstap te plannen.

## Resultaten stap 1, 3 en 4 (29 oktober 2026, crunch_uml 0.8.2)

Stap 1 is af: crunch_uml 0.8.2 dicht de drie gaten (typenaam altijd uit `t_attribute.Type`, code van
een enumeratiewaarde uit `t_attribute.Style`, rolnamen uit `SourceRole`/`DestRole`), met pariteitstests
in `test_40`. De GGM-TaskFile pint 0.8.2. Stap 3 en 4 zijn uitgevoerd met de pijplijn-crunch uit
`tools/.venv-crunch`, beide bronnen met de kopie naar het wortelpakket, in een losse database.

**Vergelijking na 0.8.2** (stap 3). Attributen zonder bruikbaar type na de kopie: 0 (was 3.623).
Verschillen in de typenaam op gedeelde attributen: 22 (was 4.049), allemaal gevallen waar de XMI geen
typenaam geeft en de `.qea` wel (`CharacterString`). Codes van enumeratiewaarden: 2 verschillen (was
779), waar de `.qea` de voorloopnul bewaart (`01` tegenover `1`). Rolnamen: geen verschil meer. De
restverschillen zijn precies de verwachte lijst: 656 associatie-einden en 24 technische elementen alleen
in de XMI, 6 associatieklassen en 12 associaties alleen in de `.qea`, `#NOTES#`-ruis en `-1` tegenover
`*` in de XMI, en de modelwijzigingen sinds januari. Eén extra bevinding: bij de klasse *Aanwezige
Deelnemer* geeft de XMI-import `gemma_naam = MaatschappelijkeActiviteit`, de `.qea` heeft
*Aanwezige Deelnemer*; de `.qea` is hier juist, dus de XMI-parser plaatst daar een tagwaarde verkeerd.

**Documentatie** (stap 4). Beide imports door hetzelfde sjabloon: 59 bestanden uit de `.qea`, 63 uit de
XMI (de vier extra zijn de technische pakketten *Diagram*, *Semantische relaties* en de twee *View*-
pakketten). Regels in de diff per categorie: id-ruis van kopieën ±200, `modified`/`version` ±2.000
(drift sinds januari), overig −1.539/+1.480. Dat "overig" bestaat uit: typekolommen die nu gevuld zijn
(`| indicatiePlusBRPopulatie | Boolean |`), lege `gemma_*`/`domein_*`-regels die de XMI-import als lege
tekst meegaf en wegvallen, de verwijderde klassen Deelplan/Veld en Fase/Oplevering (issue 53),
naamcorrecties (*Historisch Persoon* zonder spatie, *Flexibiliteit*, *Netwerkcomponent*), en hoofdletters
in typenamen (`Time` in plaats van `time`). Niets daarvan is een regressie.

**Linked Data** (stap 4). Ontologie uit de `.qea`: 155.050 triples tegenover 155.135 uit de XMI; 4.323
attribuutsoorten (XMI 4.303), 885 objecttypen (881), 352 enumeraties (355). MIM-validatie van ontologie
plus shapes: 37.261 meldingen in 13 groepen, hetzelfde beeld als de XMI-export (37.310 in 15); de
meldingen zijn de bekende data-gaten. Views: 135 tegenover 135, 1.345 klassen gedeeld, 2 alleen XMI (de
twee typo-namen), 11 alleen `.qea` (correcties en associatieklassen), 10.958 properties gedeeld, 234 alleen
XMI (associatie-einden), 73 alleen `.qea` (attributen die in de XMI geen type hadden). Browser-harnas over
de `.qea`-views: 135 modellen, 12 domeinen, alle grafiek-API's en pagina's in orde, attributen met
XSD-typen.

**Conclusie.** De overstap kan. Stap 2 (verse XMI) is optioneel geworden: de restverschillen zijn
verklaard. Voor stap 6 blijven drie besluiten over: de vorige versie voor `generate:diff` (XMI van v2.5.0
tegenover `.qea` van v3.0.0 geeft schijnwijzigingen op kopieën en associatie-einden), `generate:mim`
eerst op een kopie van het MIM-draft-bestand, en `generate:translations` alleen aanvullend
(`UPDATE_I18N=True`).

## Omzetting (stap 6 en 7, 29 oktober 2026)

`import:model` en `import:previous` lezen nu de `.qea` (`GGM` en `PREVIOUS_GGM`); de vertaaltaak volgt
de `.qea` als bron; de XMI in de release-map is alleen nog een download. Gedraaid en gecontroleerd:

- `generate:docs`: 59 definitiepagina's; de vier pagina's van technische pakketten (*Diagram*,
  *Semantische relaties*, de *View*-pakketten) vervallen.
- `generate:lod`: ontologie 155.050 triples, shapes 48.087, 135 views, geheel 132.696 triples;
  gepubliceerd met `publish:lod`, live 135 graphs, klassepagina's met EA-GUID en getypeerde attributen.
- `generate:excel`: 970 klassen, 4.543 attributen, 599 enumeraties.
- `generate:diff` (naar een losse map): slaagt. De richting stond in de TaskFile omgekeerd (`-sch` was
  de vorige versie), waardoor elke pijl nieuw → oud las; rechtgezet. Het rapport v2.5.0 → v3.0.0 toont
  de MIM-migratie van het model (4.135 attributen met classifier-type en stereotype, 966 relaties met
  stereotype) en de 2 verwijderde klassen uit issue 53. Ruis: 75/76 enumeraties "weg/nieuw" en 253
  waarden, dat zijn de kopieën van de wortelkopie met willekeurige id's.
- `generate:mim` op een kopie van het MIM-draft-bestand van v2.5.0 (v3.0.0 heeft dat bestand niet):
  slaagt zonder fouten.
- `publish:local`: documentatie uit de `.qea` op de lokale gh-pages (v3.0.0 zonder alias, latest en
  standaard ongewijzigd).

**Aandachtspunt voor crunch_uml: opgelost in 0.8.3 (29 oktober 2026).** De kopie naar het wortelpakket
gaf kopieën van enumeraties een willekeurig id; in werkelijkheid kreeg élk attribuut waarvan de enumeratie
buiten het pakket van de eigen klasse lag een eigen kopie met een uuid4, ook binnen scope (210
enumeraties en 1.905 waarden met per run een ander id). Daardoor verschilden 73 van de 135
view-bestanden bij elke `generate:lod` alleen in `dcterms:identifier`, verschilden de definitiepagina's
elke run in hun id's, en telde `generate:diff` die kopieën als verwijderd en toegevoegd. crunch_uml 0.8.3
laat enumeraties binnen scope met de boom meekomen, kopieert een enumeratie buiten scope één keer met
haar eigen id, en munt alleen nog een afgeleid id voor attributen die uit een superklasse worden
gematerialiseerd (niet gebruikt in deze pijplijn). Resultaat in deze pijplijn (geforceerde import,
twee runs): de kopie heeft 388 enumeraties, evenveel als de bron (was 598), en 2 Booleans (was 21);
views, definitiepagina's en ontologie zijn tussen twee runs byte-gelijk. Eenmalig veranderden daardoor
74 van de 135 views en 20 definitiepagina's: de tien Boolean-kopieën met IRI's als
`dienstverlening/boolean` zijn twee Booleans geworden, en een gedeelde enumeratie staat nog maar één
keer in de documentatie, bij haar eigen pakket. De diff-renderer kan daarnaast nog de typenaam tonen
waar de typeklasse buiten de scope valt (`<onbekend:EAID_…>`); dat staat nog open.

**Twee nieuwe aandachtspunten voor crunch_uml (gevonden bij de dubbele run).**

- Enumeraties in een pakket zonder klassen (de drie pakketten `Enumeratiesoort` onder RSGB, RGBZ en
  Basis IMBOR en de `Datatypes`-pakketten, samen 98 enumeraties) krijgen in de LOD de verzamel-IRI
  `enumeraties/<naam>` in plaats van het pad van hun pakket (`kern/rsgbplus/rsgb/enumeratiesoort/boolean`):
  de LOD-renderer neemt alleen pakketten met klassen als model, en de rest valt in de
  "wees"-namespace. Hetzelfde geldt voor de documentatie: de jinja2-renderer maakt alleen een pagina
  per pakket met klassen, dus de enumeraties van die pakketten staan nergens meer (de pagina Model
  Kern RSGB ging van 103 naar 47 enumeraties). Dat viel eerder niet op omdat elk model zijn eigen
  kopieën had en die wél documenteerde. In deze set zijn er geen naamsbotsingen, maar de IRI's volgen
  niet de pakketboom. Zolang dit open staat zijn de LOD en de documentatie van 0.8.3 niet gepubliceerd
  en niet gecommit; de TaskFile is wel op 0.8.3 gepind.
- Het shapes-bestand krijgt per run een andere volgorde van de property shapes: de blank nodes krijgen
  willekeurige id's en rdflib sorteert daarop (ruim 28.000 verplaatste regels per run). Deterministische
  blank-node-labels (afgeleid van de IRI van het pad) nemen dat weg. Het raakt alleen het bestand in
  git, niet de views of de ontologie.
