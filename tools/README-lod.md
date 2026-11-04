# Linked Data: genereren en publiceren

Beheerdersnotitie bij de taken `generate:lod` en `publish:lod` in de TaskFile. De opties van de
export zelf staan in de handleiding van crunch_uml (`docs/handleiding/export.md`, onderdeel
*Linked Data*).

## Eén pad

```
model (.qea)  --import:model-->  crunch_uml.db
              --generate:lod-->  <release>/ttl/Gemeentelijk Gegevensmodel Linked Data.ttl         het geheel: ontologie (RDFS/OWL + MIM 1.2)
                                 <release>/ttl/Gemeentelijk Gegevensmodel Linked Data-shapes.ttl  SHACL-shapes (owl:imports ontologie)
                                 <release>/ttl/<pad>.ttl                                          deelmodel per EA-diagram
              --publish:lod-->   named graphs <LINKED_DATA_NS>/<versie>/<pad> op de LOD-server
```

Alle Linked Data staat in `<release>/ttl` (var `LOD_DIR`). De namen van het geheel en de shapes
volgen `LOD_FILE` uit `.env`; de shapes krijgen dezelfde naam met `-shapes`.

Er is één bestand met het hele model: de ontologie. Die bevat alle pakketten, ook klassen en
enumeraties die op geen diagram staan; de deelmodellen zijn er deelgrafen van. Een apart
samengevoegd bestand van de deelmodellen (tot 4 november 2026 `ggm-geheel-<versie>.ttl`) is
daarom vervallen: dat was een onvolledige kopie van de ontologie.

Er is bewust één manier om te publiceren: de deelmodellen als named graphs. De ontologie en de
shapes gaan niet naar de server; `stage_lod_views.py` slaat ze over (`--skip`). Wie het geheel
wil, downloadt de ontologie.

## Deelmodellen (views)

Een deelmodel is een deelgraaf van de ontologie, met dezelfde IRI's en zonder SHACL: de klassen en
enumeraties op het diagram met al hun attributen en waarden, de enumeraties die een attribuut
typeren, en de associaties en generalisaties tussen de diagramelementen. Het pad volgt de
pakketboom van EA zonder volgnummers, zonder het package *Diagram* en zonder het losse woord
*Model*: `99 Kern › BAG › Model BAG › Diagram › Onderzoek` wordt `kern/bag/onderzoek`. De
term-IRI's gebruiken dezelfde segmenten (`kern/bag/pand`). Elk bestand begint met
`# graph: <LINKED_DATA_NS/versie/pad>` en beschrijft zichzelf als `owl:Ontology` met de
EA-diagramnaam als label en de EA-GUID als `dcterms:identifier`.

Welke diagrammen meedoen bepaalt `LOD_EXCLUDE_DIAGRAMS` (patronen op diagram- en pakketnamen).

## De loader op de server

De stack (github.com/AshkanA/lod-browser: Virtuoso, loader, Flask-app, Caddy) bewaakt de dropmap
`LOD_DROP`. Elke `*.ttl` daarin wordt een named graph met als IRI `GRAPH_BASE` plus het relatieve
pad zonder `.ttl`. De loader leest de kopregel `# graph:` dus niet; de dropmap moet de
graph-IRI's volgen. Daarom zet `tools/stage_lod_views.py` de bestanden eerst in een staging-boom
`<pad>.ttl`, die `publish:lod` naar `<LOD_DROP>/<versie>/` rsynct.

De loader herlaadt een graph (`CLEAR GRAPH` + laden) zodra de md5 van het bestand wijzigt, elke
30 seconden. Hij wist nooit een graph: een verwijderd bestand laat de graph in Virtuoso staan.
`publish:lod` lost dat op zonder isql-rechten: het vraagt de lijst live graphs op (SPARQL via
SSH), en voor elke graph onder `<versie>/` die geen deelmodel meer is gaat een leeg bestand mee.
De loader maakt die graph dan leeg, waarna hij uit de lijst en uit de browser verdwijnt. Bij de
volgende publicatie staat de graph niet meer in de lijst, gaat er geen leeg bestand mee en haalt
`--delete` het bestand weer uit de dropmap.

## rsync-keuzes

- `-c`: vergelijken op inhoud. De staging krijgt elke run nieuwe bestandsdatums; zonder `-c`
  gaan alle bestanden opnieuw over.
- `--delete` alleen binnen `<LOD_DROP>/<versie>/`; de rest van de dropmap blijft staan.
- Rechten 644 voor bestanden en 755 voor mappen: de loader-container leest als een andere
  gebruiker. macOS openrsync past `--chmod` niet toe op mappen en `-a` neemt de rechten van de
  bron over, daarom zet het stagingscript ze zelf (en maakt `mktemp -d` een map met 700).
- `DRY_RUN=true` toont wat er zou gaan (`<f` = inhoud gewijzigd, `.f..t` = alleen datum).

## Controleren

```bash
task publish:lod-list          # alle graphs in Virtuoso met hun aantal triples (SSH, read-only)
python tools/validate_mim_lod.py ontologie.ttl ontologie-shapes.ttl   # in de crunch_uml-checkout
```

`generate:lod` controleert na de export elk deelmodel (kopregel, uniek graph-pad, geldige Turtle)
met `stage_lod_views.py` zonder `--stage`; `publish:lod` doet dezelfde controle vóór de staging.

De browser (lod.gemeentelijkgegevensmodel.nl) toont elke graph onder `LINKED_DATA_NS` waarin
klassen staan; het domein in de keuzelijst is het eerste padsegment na de versie. De lijst wordt
elke vijf minuten ververst.

## Bekende aandachtspunten

- Task draait elke `cmds`-regel in zijn eigen Go-shell (mvdan/sh); `while read`-lussen en
  `< <(...)` blijven daar hangen. Luslogica hoort daarom in een script.
- Hernoem je een diagram of pakket, dan verandert het pad en dus de graph-IRI; de oude graph
  wordt bij de volgende `publish:lod` leeggemaakt. Term-IRI's veranderen alleen als een pakket of
  klasse van naam of plaats verandert.
