# Changes from v2.5.0 to v2.5.1

Entiteiten worden vergeleken op naam (gekwalificeerd met pakketpad), zodat een nieuwe `ea_guid` voor hetzelfde logische element niet als _Removed + Added_ verschijnt. Verwijzingen naar andere entiteiten (FK-velden zoals `enumeration_id`) worden vergeleken op de naam van het doel — niet op de interne sleutel.

**Structurele wijzigingen** raken het model zelf: toegevoegde of verwijderde elementen, naamswijzigingen, type/verplicht/multipliciteit/lengte/patroon en links tussen elementen. **Beschrijvende wijzigingen** updaten alleen metadata of documentatie (definitie, toelichting, gemma-tags, versie, auteur, herkomst, …) zonder de structuur van het model te veranderen.

## Samenvatting

| Element | + (struct.) | − (struct.) | ~ (struct.) | ~ (beschr.) |
| --- | ---: | ---: | ---: | ---: |
| Classes | 0 | 0 | 0 | 0 |
| Datatypes | 0 | 0 | 0 | 0 |
| Enumeraties | 0 | 0 | 1 | 0 |
| Attributen | 0 | 0 | 6 | 0 |
| Associaties | 0 | 0 | 0 | 0 |
| Generalisaties | 0 | 0 | 0 | 0 |
| Enum-literals | 1 | 0 | — | — |
| Pakketten (metadata) | 0 | 0 | 0 | 0 |

## Geraakte packages

- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/BAG/Model BAG** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernbagmodel-bag)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Model Kern RSGB** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelmodel-kern-rsgb)

## Structurele wijzigingen

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernbagmodel-bag"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/BAG/Model BAG

#### Classes

##### `Standplaats` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `beginGeldigheid` — Gewijzigd
    - **naam**: `Datum Begin Geldigheid` → `beginGeldigheid`
- 🟡 `datumEinde` — Gewijzigd
    - **naam**: `Datum Einde` → `datumEinde`
- 🟡 `datumIngang` — Gewijzigd
    - **naam**: `Datum Ingang` → `datumIngang`
- 🟡 `eindGeldigheid` — Gewijzigd
    - **naam**: `Datum Einde Geldigheid` → `eindGeldigheid`

#### Enumeraties

##### `statusVerblijfsobject` — 🟡 Gewijzigd

**Literals:**

- 🟢 `verblijfsobject verbouwing` — Toegevoegd

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelmodel-kern-rsgb"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Model Kern RSGB

#### Classes

##### `BegroeidTerreindeel` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `opTalud` — Gewijzigd
    - **primitieve type**: `boolean` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Enumeratiesoort::Boolean`

##### `OnbegroeidTerreindeel` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `onbegroeidTerreindeelOpTalud` — Gewijzigd
    - **primitieve type**: `boolean` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Enumeratiesoort::Boolean`

## Beschrijvende wijzigingen

_Geen beschrijvende wijzigingen._
