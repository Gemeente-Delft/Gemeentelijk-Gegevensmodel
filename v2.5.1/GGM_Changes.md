# Changes from v2.5.0 to v2.5.1

Entiteiten worden vergeleken op naam (gekwalificeerd met pakketpad), zodat een nieuwe `ea_guid` voor hetzelfde logische element niet als _Removed + Added_ verschijnt. Verwijzingen naar andere entiteiten (FK-velden zoals `enumeration_id`) worden vergeleken op de naam van het doel — niet op de interne sleutel.

**Structurele wijzigingen** raken het model zelf: toegevoegde of verwijderde elementen, naamswijzigingen, type/verplicht/multipliciteit/lengte/patroon en links tussen elementen. **Beschrijvende wijzigingen** updaten alleen metadata of documentatie (definitie, toelichting, gemma-tags, versie, auteur, herkomst, …) zonder de structuur van het model te veranderen.

## Samenvatting

| Element | + (struct.) | − (struct.) | ~ (struct.) | ~ (beschr.) |
| --- | ---: | ---: | ---: | ---: |
| Classes | 0 | 0 | 0 | 0 |
| Datatypes | 0 | 0 | 0 | 0 |
| Enumeraties | 35 | 37 | 14 | 0 |
| Attributen | 0 | 0 | 6 | 0 |
| Associaties | 0 | 0 | 0 | 0 |
| Generalisaties | 0 | 0 | 0 | 0 |
| Enum-literals | 0 | 93 | — | — |
| Pakketten (metadata) | 0 | 0 | 0 | 0 |

## Geraakte packages

- **Delfts Gemeentelijk Gegevensmodel/1 Veiligheid en Vergunningen/Model VTH** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel1-veiligheid-en-vergunningenmodel-vth)
- **Delfts Gemeentelijk Gegevensmodel/4 Onderwijs/Leerplicht en Leerlingenvervoer/Model Leerplicht en Leerlingenvervoer** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel4-onderwijsleerplicht-en-leerlingenvervoermodel-leerplicht-en-leerlingenvervoer)
- **Delfts Gemeentelijk Gegevensmodel/4 Onderwijs/Onderwijs/Model Onderwijs** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel4-onderwijsonderwijsmodel-onderwijs)
- **Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inburgering/Model Inburgering** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeininburgeringmodel-inburgering)
- **Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Inkomsten/Model Inkomsten** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiekmodel-sociaal-domein-generiekinkomstenmodel-inkomsten)
- **Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/Vastgoed/Model Vastgoed** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel9-interne-organisatievastgoedmodel-vastgoed)
- **Delfts Gemeentelijk Gegevensmodel/99 Kern/BAG/Model BAG** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel99-kernbagmodel-bag)
- **Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Groepattribuutsoort** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelgroepattribuutsoort)
- **Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Model Kern RSGB** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelmodel-kern-rsgb)
- **Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/archief/Model Kern RSGB** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelarchiefmodel-kern-rsgb)

## Structurele wijzigingen

<a id="structureel-delfts-gemeentelijk-gegevensmodel1-veiligheid-en-vergunningenmodel-vth"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/1 Veiligheid en Vergunningen/Model VTH

#### Enumeraties

##### `Boolean` — 🟢 Toegevoegd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `Boolean` — 🔴 Verwijderd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `Boolean` — 🟡 Gewijzigd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodel4-onderwijsleerplicht-en-leerlingenvervoermodel-leerplicht-en-leerlingenvervoer"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/4 Onderwijs/Leerplicht en Leerlingenvervoer/Model Leerplicht en Leerlingenvervoer

#### Enumeraties

##### `Boolean` — 🟢 Toegevoegd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `Boolean` — 🔴 Verwijderd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `Boolean` — 🟡 Gewijzigd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodel4-onderwijsonderwijsmodel-onderwijs"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/4 Onderwijs/Onderwijs/Model Onderwijs

#### Enumeraties

##### `Boolean` — 🟢 Toegevoegd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `Boolean` — 🔴 Verwijderd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `Boolean` — 🟡 Gewijzigd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeininburgeringmodel-inburgering"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inburgering/Model Inburgering

#### Enumeraties

##### `Boolean` — 🟢 Toegevoegd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `Boolean` — 🔴 Verwijderd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `Boolean` — 🟡 Gewijzigd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiekmodel-sociaal-domein-generiekinkomstenmodel-inkomsten"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Inkomsten/Model Inkomsten

#### Enumeraties

##### `CdUitkeringsperiode` — 🟢 Toegevoegd

##### `CdUitkeringsperiode` — 🟢 Toegevoegd

##### `CdUitkeringsperiode` — 🟢 Toegevoegd

##### `CdUitkeringsperiode` — 🔴 Verwijderd

##### `CdUitkeringsperiode` — 🔴 Verwijderd

##### `CdUitkeringsperiode` — 🔴 Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodel9-interne-organisatievastgoedmodel-vastgoed"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/Vastgoed/Model Vastgoed

#### Enumeraties

##### `Boolean` — 🟢 Toegevoegd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `Boolean` — 🟢 Toegevoegd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `Boolean` — 🟢 Toegevoegd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `Boolean` — 🔴 Verwijderd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `Boolean` — 🔴 Verwijderd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `Boolean` — 🔴 Verwijderd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `Boolean` — 🟡 Gewijzigd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodel99-kernbagmodel-bag"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/99 Kern/BAG/Model BAG

#### Classes

##### `Standplaats` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `Datum Begin Geldigheid` — Gewijzigd
    - **naam**: `beginGeldigheid` → `Datum Begin Geldigheid`
- 🟡 `Datum Einde` — Gewijzigd
    - **naam**: `datumEinde` → `Datum Einde`
- 🟡 `Datum Einde Geldigheid` — Gewijzigd
    - **naam**: `eindGeldigheid` → `Datum Einde Geldigheid`
- 🟡 `Datum Ingang` — Gewijzigd
    - **naam**: `datumIngang` → `Datum Ingang`

#### Enumeraties

##### `statusVerblijfsobject` — 🟡 Gewijzigd

**Literals:**

- 🔴 `verblijfsobject verbouwing` — Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelgroepattribuutsoort"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Groepattribuutsoort

#### Enumeraties

##### `adelijkeTitel` — 🟢 Toegevoegd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `baron` — Verwijderd
- 🔴 `barones` — Verwijderd
- 🔴 `graaf` — Verwijderd
- 🔴 `gravin` — Verwijderd
- 🔴 `hertog` — Verwijderd
- 🔴 `hertogin` — Verwijderd
- 🔴 `markies` — Verwijderd
- 🔴 `markiezin` — Verwijderd
- 🔴 `prins` — Verwijderd
- 🔴 `prinses` — Verwijderd
- 🔴 `ridder` — Verwijderd

##### `adelijkeTitel` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `baron` — Verwijderd
- 🔴 `barones` — Verwijderd
- 🔴 `graaf` — Verwijderd
- 🔴 `gravin` — Verwijderd
- 🔴 `hertog` — Verwijderd
- 🔴 `hertogin` — Verwijderd
- 🔴 `markies` — Verwijderd
- 🔴 `markiezin` — Verwijderd
- 🔴 `prins` — Verwijderd
- 🔴 `prinses` — Verwijderd
- 🔴 `ridder` — Verwijderd

##### `adelijkeTitel` — 🟡 Gewijzigd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `baron` — Verwijderd
- 🔴 `barones` — Verwijderd
- 🔴 `graaf` — Verwijderd
- 🔴 `gravin` — Verwijderd
- 🔴 `hertog` — Verwijderd
- 🔴 `hertogin` — Verwijderd
- 🔴 `markies` — Verwijderd
- 🔴 `markiezin` — Verwijderd
- 🔴 `prins` — Verwijderd
- 🔴 `prinses` — Verwijderd
- 🔴 `ridder` — Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelmodel-kern-rsgb"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Model Kern RSGB

#### Classes

##### `BegroeidTerreindeel` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `opTalud` — Gewijzigd
    - **primitieve type**: `Boolean` → `boolean`
    - **enumeratie**: `Enumeratie: Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Model Kern RSGB::Boolean` → _(leeg)_

##### `OnbegroeidTerreindeel` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `onbegroeidTerreindeelOpTalud` — Gewijzigd
    - **primitieve type**: `Boolean` → `boolean`
    - **enumeratie**: `Enumeratie: Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Model Kern RSGB::Boolean` → _(leeg)_

#### Enumeraties

##### `Boolean` — 🟢 Toegevoegd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `Boolean` — 🟢 Toegevoegd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `Boolean` — 🟢 Toegevoegd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `soortRechtsvorm` — 🟢 Toegevoegd

**Literals:**

- 🔴 `Besloten vennootschap` — Verwijderd
- 🔴 `Europese Cooperatieve Vennootschap` — Verwijderd
- 🔴 `Europese Naamloze Vennootschap` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `commanditaire vennootschap` — Verwijderd
- 🔴 `cooperatie, Europees Economische Samenwerking` — Verwijderd
- 🔴 `kapitaalvennootschap binnen EER` — Verwijderd
- 🔴 `kapitaalvennootschap buiten EER` — Verwijderd
- 🔴 `kerkelijke Organisatie` — Verwijderd
- 🔴 `maatschap` — Verwijderd
- 🔴 `naamloze Vennootschap` — Verwijderd
- 🔴 `onderlinge Waarborg Maatschappij` — Verwijderd
- 🔴 `overig privaatrechtelijke rechtspersoon` — Verwijderd
- 🔴 `overige buitenlandse rechtspersoon vennootschap` — Verwijderd
- 🔴 `publiekrechtelijke Rechtspersoon` — Verwijderd
- 🔴 `rederij` — Verwijderd
- 🔴 `stichting` — Verwijderd
- 🔴 `vennootschap onder Firma` — Verwijderd
- 🔴 `vereniging` — Verwijderd
- 🔴 `vereniging van Eigenaars` — Verwijderd

##### `statusGeoObject` — 🟢 Toegevoegd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🟢 Toegevoegd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🟢 Toegevoegd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🟢 Toegevoegd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🟢 Toegevoegd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🟢 Toegevoegd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🟢 Toegevoegd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🟢 Toegevoegd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🟢 Toegevoegd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🟢 Toegevoegd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🟢 Toegevoegd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🟢 Toegevoegd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🟢 Toegevoegd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🟢 Toegevoegd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🟢 Toegevoegd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🟢 Toegevoegd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusWOZ(Deel)Object` — 🟢 Toegevoegd

**Literals:**

- 🔴 `actief` — Verwijderd
- 🔴 `beëindigd` — Verwijderd
- 🔴 `gevormd, niet actief` — Verwijderd
- 🔴 `ten onrechte opgevoerd` — Verwijderd

##### `Boolean` — 🔴 Verwijderd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `Boolean` — 🔴 Verwijderd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `Boolean` — 🔴 Verwijderd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `Boolean` — 🔴 Verwijderd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `Boolean` — 🔴 Verwijderd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `soortRechtsvorm` — 🔴 Verwijderd

**Literals:**

- 🔴 `Besloten vennootschap` — Verwijderd
- 🔴 `Europese Cooperatieve Vennootschap` — Verwijderd
- 🔴 `Europese Naamloze Vennootschap` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `commanditaire vennootschap` — Verwijderd
- 🔴 `cooperatie, Europees Economische Samenwerking` — Verwijderd
- 🔴 `kapitaalvennootschap binnen EER` — Verwijderd
- 🔴 `kapitaalvennootschap buiten EER` — Verwijderd
- 🔴 `kerkelijke Organisatie` — Verwijderd
- 🔴 `maatschap` — Verwijderd
- 🔴 `naamloze Vennootschap` — Verwijderd
- 🔴 `onderlinge Waarborg Maatschappij` — Verwijderd
- 🔴 `overig privaatrechtelijke rechtspersoon` — Verwijderd
- 🔴 `overige buitenlandse rechtspersoon vennootschap` — Verwijderd
- 🔴 `publiekrechtelijke Rechtspersoon` — Verwijderd
- 🔴 `rederij` — Verwijderd
- 🔴 `stichting` — Verwijderd
- 🔴 `vennootschap onder Firma` — Verwijderd
- 🔴 `vereniging` — Verwijderd
- 🔴 `vereniging van Eigenaars` — Verwijderd

##### `statusGeoObject` — 🔴 Verwijderd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🔴 Verwijderd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🔴 Verwijderd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🔴 Verwijderd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🔴 Verwijderd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🔴 Verwijderd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🔴 Verwijderd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🔴 Verwijderd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🔴 Verwijderd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🔴 Verwijderd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🔴 Verwijderd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🔴 Verwijderd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🔴 Verwijderd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🔴 Verwijderd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🔴 Verwijderd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusGeoObject` — 🔴 Verwijderd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusWOZ(Deel)Object` — 🔴 Verwijderd

**Literals:**

- 🔴 `actief` — Verwijderd
- 🔴 `beëindigd` — Verwijderd
- 🔴 `gevormd, niet actief` — Verwijderd
- 🔴 `ten onrechte opgevoerd` — Verwijderd

##### `Boolean` — 🟡 Gewijzigd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `soortRechtsvorm` — 🟡 Gewijzigd

**Literals:**

- 🔴 `Besloten vennootschap` — Verwijderd
- 🔴 `Europese Cooperatieve Vennootschap` — Verwijderd
- 🔴 `Europese Naamloze Vennootschap` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `commanditaire vennootschap` — Verwijderd
- 🔴 `cooperatie, Europees Economische Samenwerking` — Verwijderd
- 🔴 `kapitaalvennootschap binnen EER` — Verwijderd
- 🔴 `kapitaalvennootschap buiten EER` — Verwijderd
- 🔴 `kerkelijke Organisatie` — Verwijderd
- 🔴 `maatschap` — Verwijderd
- 🔴 `naamloze Vennootschap` — Verwijderd
- 🔴 `onderlinge Waarborg Maatschappij` — Verwijderd
- 🔴 `overig privaatrechtelijke rechtspersoon` — Verwijderd
- 🔴 `overige buitenlandse rechtspersoon vennootschap` — Verwijderd
- 🔴 `publiekrechtelijke Rechtspersoon` — Verwijderd
- 🔴 `rederij` — Verwijderd
- 🔴 `stichting` — Verwijderd
- 🔴 `vennootschap onder Firma` — Verwijderd
- 🔴 `vereniging` — Verwijderd
- 🔴 `vereniging van Eigenaars` — Verwijderd

##### `statusGeoObject` — 🟡 Gewijzigd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusWOZ(Deel)Object` — 🟡 Gewijzigd

**Literals:**

- 🔴 `actief` — Verwijderd
- 🔴 `beëindigd` — Verwijderd
- 🔴 `gevormd, niet actief` — Verwijderd
- 🔴 `ten onrechte opgevoerd` — Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelarchiefmodel-kern-rsgb"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/archief/Model Kern RSGB

#### Enumeraties

##### `inwinningsmethodeGeometrie` — 🟢 Toegevoegd

**Literals:**

- 🔴 `bouwtekening` — Verwijderd
- 🔴 `digitaliseren` — Verwijderd
- 🔴 `fotogrammetrisch` — Verwijderd
- 🔴 `geconstrueerd` — Verwijderd
- 🔴 `laser` — Verwijderd
- 🔴 `niet bekend` — Verwijderd
- 🔴 `panoramabeelden` — Verwijderd
- 🔴 `scannen` — Verwijderd
- 🔴 `terrestrisch` — Verwijderd

##### `StatLigplaatsStandplaats` — 🟢 Toegevoegd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `plaats aangewezen` — Verwijderd
- 🔴 `plaats ingetrokken` — Verwijderd

##### `statusVoortgangBouw` — 🟢 Toegevoegd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `nieuwbouw gereed` — Verwijderd
- 🔴 `nieuwbouw gestart` — Verwijderd
- 🔴 `nieuwbouwvergunning ingetrokken` — Verwijderd
- 🔴 `nieuwbouwvergunning verleend` — Verwijderd
- 🔴 `sloop gereed` — Verwijderd
- 🔴 `sloop gestart` — Verwijderd
- 🔴 `sloopvergunning ingetrokken` — Verwijderd
- 🔴 `sloopvergunning verleend` — Verwijderd
- 🔴 `verbouw gereed` — Verwijderd
- 🔴 `verbouw gestart` — Verwijderd
- 🔴 `verbouwvergunning ingetrokken` — Verwijderd
- 🔴 `verbouwvergunning verleend` — Verwijderd

##### `inwinningsmethodeGeometrie` — 🔴 Verwijderd

**Literals:**

- 🔴 `bouwtekening` — Verwijderd
- 🔴 `digitaliseren` — Verwijderd
- 🔴 `fotogrammetrisch` — Verwijderd
- 🔴 `geconstrueerd` — Verwijderd
- 🔴 `laser` — Verwijderd
- 🔴 `niet bekend` — Verwijderd
- 🔴 `panoramabeelden` — Verwijderd
- 🔴 `scannen` — Verwijderd
- 🔴 `terrestrisch` — Verwijderd

##### `StatLigplaatsStandplaats` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `plaats aangewezen` — Verwijderd
- 🔴 `plaats ingetrokken` — Verwijderd

##### `statusVoortgangBouw` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `nieuwbouw gereed` — Verwijderd
- 🔴 `nieuwbouw gestart` — Verwijderd
- 🔴 `nieuwbouwvergunning ingetrokken` — Verwijderd
- 🔴 `nieuwbouwvergunning verleend` — Verwijderd
- 🔴 `sloop gereed` — Verwijderd
- 🔴 `sloop gestart` — Verwijderd
- 🔴 `sloopvergunning ingetrokken` — Verwijderd
- 🔴 `sloopvergunning verleend` — Verwijderd
- 🔴 `verbouw gereed` — Verwijderd
- 🔴 `verbouw gestart` — Verwijderd
- 🔴 `verbouwvergunning ingetrokken` — Verwijderd
- 🔴 `verbouwvergunning verleend` — Verwijderd

##### `inwinningsmethodeGeometrie` — 🟡 Gewijzigd

**Literals:**

- 🔴 `bouwtekening` — Verwijderd
- 🔴 `digitaliseren` — Verwijderd
- 🔴 `fotogrammetrisch` — Verwijderd
- 🔴 `geconstrueerd` — Verwijderd
- 🔴 `laser` — Verwijderd
- 🔴 `niet bekend` — Verwijderd
- 🔴 `panoramabeelden` — Verwijderd
- 🔴 `scannen` — Verwijderd
- 🔴 `terrestrisch` — Verwijderd

##### `StatLigplaatsStandplaats` — 🟡 Gewijzigd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `plaats aangewezen` — Verwijderd
- 🔴 `plaats ingetrokken` — Verwijderd

##### `statusVoortgangBouw` — 🟡 Gewijzigd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `nieuwbouw gereed` — Verwijderd
- 🔴 `nieuwbouw gestart` — Verwijderd
- 🔴 `nieuwbouwvergunning ingetrokken` — Verwijderd
- 🔴 `nieuwbouwvergunning verleend` — Verwijderd
- 🔴 `sloop gereed` — Verwijderd
- 🔴 `sloop gestart` — Verwijderd
- 🔴 `sloopvergunning ingetrokken` — Verwijderd
- 🔴 `sloopvergunning verleend` — Verwijderd
- 🔴 `verbouw gereed` — Verwijderd
- 🔴 `verbouw gestart` — Verwijderd
- 🔴 `verbouwvergunning ingetrokken` — Verwijderd
- 🔴 `verbouwvergunning verleend` — Verwijderd

## Beschrijvende wijzigingen

_Geen beschrijvende wijzigingen._
