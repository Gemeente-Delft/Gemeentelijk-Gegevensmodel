# Changes from v2.4.0 to v2.5.0

## Summary

- **Classes**: +2 / -6 / ~1
- **Datatypes**: +0 / -0 / ~0
- **Enumerations**: +165 / -114 / ~223
- **Attributes**: +46 / -228 / ~419
- **Literals**: +957 / -938

## Overview

**Packages touched:** `Complex datatype`, `Datatypes`, `Datatypes`, `Datatypes`, `Enumeratiesoort`, `Groepattribuutsoort`, `Groepattribuutsoort`, `Metagegevens`, `Model`, `Model Afval`, `Model Archeologie`, `Model BAG`, `Model Beheer Openbare Ruimte`, `Model Diensten`, `Model Dienstverlening`, `Model Generiek`, `Model HR`, `Model ICT`, `Model IMBOR`, `Model Inburgering`, `Model Inkomen`, `Model Inkomsten`, `Model Inkoop`, `Model Jeugd en Wmo Generiek`, `Model Jeugdbescherming`, `Model Kern RGBZ`, `Model Kern RSGB`, `Model Kern RSGB`, `Model Leerplicht en Leerlingenvervoer`, `Model Onderwijs`, `Model Parkeren`, `Model Schuldhulpverlening`, `Model Sociaal Domein Generiek`, `Model Sport`, `Model Terug- en invordering`, `Model VTH`, `Model Vastgoed`, `Model Vermogen`, `Model Vroegsignalering`, `Model Werk`, `Model Wonen`, `Referentielijsten`


## Top-down changes

## Package: Complex datatype

_No class changes in this package._

_No datatype changes in this package._

### Enumerations

#### typeObjectcode — **Added**

##### Literals

- `ligplaats` — **Added**
- `nummeraanduiding` — **Added**
- `openbare ruimte` — **Added**
- `overig adreseerbaar object aanduiding` — **Added**
- `overig benoemd terrein` — **Added**
- `overig gebouwd object` — **Added**
- `pand` — **Added**
- `standplaats` — **Added**
- `verblijfsobject` — **Added**

#### typeObjectcode — **Removed**

##### Literals

- `ligplaats` — **Removed**
- `nummeraanduiding` — **Removed**
- `openbare ruimte` — **Removed**
- `overig adreseerbaar object aanduiding` — **Removed**
- `overig benoemd terrein` — **Removed**
- `overig gebouwd object` — **Removed**
- `pand` — **Removed**
- `standplaats` — **Removed**
- `verblijfsobject` — **Removed**

## Package: Datatypes

_No class changes in this package._

_No datatype changes in this package._

### Enumerations

#### BrutoNettoInkomsten — **Added**

#### CdSrtInkomstenverhouding — **Added**

#### CdSzWet — **Added**

#### CdUitkeringsperiode — **Added**

#### CodeSoortVrijlating — **Added**

#### Inkomstencomponenttype — **Added**

#### InkomstensoortAlimentatie — **Added**

#### InkomstensoortBetaaldWerk — **Added**

#### InkomstensoortPensioen — **Added**

#### InkomstensoortStudiefinanciering — **Added**

#### JsonRuledGroupType — **Added**

#### Onderhoudsplichttype — **Added**

#### SoortContract — **Added**

## Package: Datatypes

_No class changes in this package._

_No datatype changes in this package._

### Enumerations

#### AdresType — **Added**

#### CdSrtVermogenscomponent — **Added**

#### CdSrtVoertuig — **Added**

#### CdSrtWaardeVermogenscomponent — **Added**

## Package: Datatypes

_No class changes in this package._

_No datatype changes in this package._

### Enumerations

#### CdRedenAanvraagANWaangevraagd — **Added**

#### CdRedenAanvraagANWafgewezenReden — **Added**

#### CdRedenAanvraagContractperiode — **Added**

#### CdRedenAanvraagEindeBijstand — **Added**

#### CdRedenAanvraagEindeEigenBedrijf — **Added**

#### CdRedenAanvraagEindeUitkering — **Added**

#### CdRedenAanvraagEindeUitkeringReden — **Added**

#### CdRedenAanvraagEindeWerk — **Added**

#### CdRedenAanvraagOnvoldoendeInkomen — **Added**

#### CdRedenAanvraagVerblijfstatus — **Added**

#### CdRedenAanvraagWWgevraagd — **Added**

#### CdRedenAanvraagWijzigingGezin — **Added**

#### CdRedenAanvraagWwafgewezen — **Added**

#### CdRedenAanvraagZelfstandige — **Added**

#### CodeRedenAfwijkendeStartdatum — **Added**

#### RedenKwijtscheldingVordering — **Added**

## Package: Enumeratiesoort

_No class changes in this package._

_No datatype changes in this package._

### Enumerations

#### functieOndersteunendWegdeelPlus — **Removed**

#### typeringOndersteunendWaterPlus — **Removed**

## Package: Groepattribuutsoort

### Classes

#### GeboorteIngeschrevenNatuurlijkPersoon — **Unchanged**

##### Attributes

- datumGeboorte — **Changed**
  - **primitive**: `` → `Datum`

#### GeboorteIngeschrevenPersoon — **Unchanged**

##### Attributes

- datumGeboorte — **Changed**
  - **primitive**: `` → `Datum`
- geboorteplaats — **Changed**
  - **primitive**: `` → `AN200`

#### KoopsomKadastraleOnroerendeZaak — **Unchanged**

##### Attributes

- datumTransactie — **Changed**
  - **primitive**: `` → `Datum`

#### MigratieIngeschrevenNatuurlijkPersoon — **Unchanged**

##### Attributes

- aangeverMigratie — **Changed**
  - **enumeration_id**: `Enumeratie: aangever` → `Enumeratie: aangever`
- redenWijzigingMigratie — **Changed**
  - **enumeration_id**: `Enumeratie: redenWijzigingAdres` → `Enumeratie: redenWijzigingAdres`
- soortMigratie — **Changed**
  - **enumeration_id**: `Enumeratie: soortMigratie` → `Enumeratie: soortMigratie`

#### NaamNatuurlijkPersoon — **Unchanged**

##### Attributes

- geslachtsnaam — **Changed**
  - **primitive**: `` → `AN255`
- voornamen — **Changed**
  - **primitive**: `` → `AN200`
- voorvoegselGeslachtsnaam — **Changed**
  - **primitive**: `` → `AN255`

#### NaamgebruikNatuurlijkPersoon — **Unchanged**

##### Attributes

- adellijkeTitelNaamgebruik — **Changed**
  - **enumeration_id**: `Enumeratie: adelijkeTitel` → `Enumeratie: adelijkeTitel`

#### NederlandseNationaliteitIngeschrevenPersoon — **Unchanged**

##### Attributes

- aanduidingBijzonderNederlanderschap — **Changed**
  - **primitive**: `` → `boolean`
- redenVerkrijgingNederlandseNationaliteit — **Changed**
  - **primitive**: `` → `AN200`
- redenVerliesNederlandseNationaliteit — **Changed**
  - **primitive**: `` → `AN200`

#### OntbindingHuwelijk/geregistreerdPartnerschap — **Unchanged**

##### Attributes

- datumEinde — **Changed**
  - **primitive**: `` → `Datum`
- redenEinde — **Changed**
  - **enumeration_id**: `Enumeratie: redenEindeRelatie` → `Enumeratie: redenEindeRelatie`

#### OverlijdenIngeschrevenNatuurlijkPersoon — **Unchanged**

##### Attributes

- datumOverlijden — **Changed**
  - **primitive**: `` → `Datum`

#### OverlijdenIngeschrevenPersoon — **Unchanged**

##### Attributes

- datumOverlijden — **Changed**
  - **primitive**: `` → `Datum`
- overlijdensplaats — **Changed**
  - **primitive**: `` → `AN200`

#### Postadres — **Unchanged**

##### Attributes

- postadresType — **Changed**
  - **primitive**: `postadresType` → `AN255`
- postcodePostadres — **Changed**
  - **primitive**: `POSTCODE` → `AN6`

#### SamengesteldeNaamNatuurlijkPersoon — **Unchanged**

##### Attributes

- adellijkeTitel — **Changed**
  - **enumeration_id**: `Enumeratie: adelijkeTitel` → `Enumeratie: adelijkeTitel`
- namenreeks — **Changed**
  - **primitive**: `INDIC` → `boolean`
- predicaat — **Changed**
  - **enumeration_id**: `Enumeratie: predicaat` → `Enumeratie: predicaat`
- scheidingsteken — **Changed**
  - **primitive**: `VOORVOEGSEL` → `AN255`
- voorvoegsel — **Changed**
  - **primitive**: `VOORVOEGSEL` → `AN255`

#### SluitingOfAangaanHuwelijkOfGeregistreerdPartnerschap — **Unchanged**

##### Attributes

- datumAanvang — **Changed**
  - **primitive**: `` → `Datum`

#### SoortFunctioneelGebied — **Unchanged**

##### Attributes

- indicatiePlusBRPopulatie — **Changed**
  - **primitive**: `INDIC` → ``
- typeFunctioneelGebied — **Changed**
  - **enumeration_id**: `Enumeratie: typeringFunctioneelGebied` → `Enumeratie: typeringFunctioneelGebied`

#### SoortKunstwerk — **Unchanged**

##### Attributes

- indicatiePlusBRPopulatie — **Changed**
  - **primitive**: `INDIC` → ``
- typeKunstwerk — **Changed**
  - **enumeration_id**: `Enumeratie: typeringKunstwerk` → `Enumeratie: typeringKunstwerk`

#### SoortOverigBouwwerk — **Unchanged**

##### Attributes

- indicatiePlusBRPopulatie — **Changed**
  - **primitive**: `INDIC` → ``
- typeOverigBouwwerk — **Changed**
  - **enumeration_id**: `Enumeratie: typeringOverigBouwwerk` → `Enumeratie: typeringOverigBouwwerk`

#### SoortScheiding — **Unchanged**

##### Attributes

- indicatiePlusBRPopulatie — **Changed**
  - **primitive**: `INDIC` → ``
- typeScheiding — **Changed**
  - **enumeration_id**: `Enumeratie: typeringScheiding` → `Enumeratie: typeringScheiding`

#### SoortSpoor — **Unchanged**

##### Attributes

- functieSpoor — **Changed**
  - **enumeration_id**: `Enumeratie: functieSpoor` → `Enumeratie: functieSpoor`
- indicatiePlusBRPopulatie — **Changed**
  - **primitive**: `INDIC` → ``

#### VerblijfBuitenlandSubject — **Unchanged**

##### Attributes

- adresBuitenland1 — **Changed**
  - **primitive**: `` → `AN200`
- adresBuitenland2 — **Changed**
  - **primitive**: `` → `AN200`
- adresBuitenland3 — **Changed**
  - **primitive**: `` → `AN200`

#### VerblijfadresIngeschrevenPersoon — **Unchanged**

##### Attributes

- beschrijvingLocatie — **Changed**
  - **primitive**: `` → `AN255`

#### VerblijfsrechtIngeschrevenNatuurlijkPersoon — **Unchanged**

##### Attributes

- datumAanvangVerblijfsrecht — **Changed**
  - **primitive**: `` → `Datum`
- datumMededelingVerblijfsrecht — **Changed**
  - **primitive**: `` → `Datum`
- datumVoorzienEindeVerblijfsrecht — **Changed**
  - **primitive**: `` → `Datum`

_No datatype changes in this package._

### Enumerations

#### aangever — **Added**

##### Literals

- `Echtgenoot/geregistreerd partner` — **Added**
- `Gezaghouder` — **Added**
- `Hoofd instelling` — **Added**
- `Ingeschrevene` — **Added**
- `Inwonend ouder voor meerderjarig kind` — **Added**
- `Meerderjarig gemachtigde` — **Added**
- `Meerderjarig inwonend kind voor ouder` — **Added**
- `Verzorger` — **Added**

#### aangever — **Removed**

##### Literals

- `Echtgenoot/geregistreerd partner` — **Removed**
- `Gezaghouder` — **Removed**
- `Hoofd instelling` — **Removed**
- `Ingeschrevene` — **Removed**
- `Inwonend ouder voor meerderjarig kind` — **Removed**
- `Meerderjarig gemachtigde` — **Removed**
- `Meerderjarig inwonend kind voor ouder` — **Removed**
- `Verzorger` — **Removed**

#### adelijkeTitel — **Added**

##### Literals

- `Leeg` — **Added**
- `Onbekend` — **Added**
- `baron` — **Added**
- `barones` — **Added**
- `graaf` — **Added**
- `gravin` — **Added**
- `hertog` — **Added**
- `hertogin` — **Added**
- `markies` — **Added**
- `markiezin` — **Added**
- `prins` — **Added**
- `prinses` — **Added**
- `ridder` — **Added**

#### adelijkeTitel — **Removed**

##### Literals

- `Leeg` — **Removed**
- `Onbekend` — **Removed**
- `baron` — **Removed**
- `barones` — **Removed**
- `graaf` — **Removed**
- `gravin` — **Removed**
- `hertog` — **Removed**
- `hertogin` — **Removed**
- `markies` — **Removed**
- `markiezin` — **Removed**
- `prins` — **Removed**
- `prinses` — **Removed**
- `ridder` — **Removed**

#### adelijkeTitel — **Removed**

##### Literals

- `Leeg` — **Removed**
- `Onbekend` — **Removed**
- `baron` — **Removed**
- `barones` — **Removed**
- `graaf` — **Removed**
- `gravin` — **Removed**
- `hertog` — **Removed**
- `hertogin` — **Removed**
- `markies` — **Removed**
- `markiezin` — **Removed**
- `prins` — **Removed**
- `prinses` — **Removed**
- `ridder` — **Removed**

#### adelijkeTitel — **Added**

##### Literals

- `Leeg` — **Added**
- `Onbekend` — **Added**
- `baron` — **Added**
- `barones` — **Added**
- `graaf` — **Added**
- `gravin` — **Added**
- `hertog` — **Added**
- `hertogin` — **Added**
- `markies` — **Added**
- `markiezin` — **Added**
- `prins` — **Added**
- `prinses` — **Added**
- `ridder` — **Added**

#### functieSpoor — **Added**

##### Literals

- `(haven)kraan` — **Added**
- `sneltram` — **Added**
- `tram` — **Added**
- `trein` — **Added**

#### functieSpoor — **Removed**

##### Literals

- `(haven)kraan` — **Removed**
- `sneltram` — **Removed**
- `tram` — **Removed**
- `trein` — **Removed**

#### predicaat — **Added**

##### Literals

- `Hare Hoogheid` — **Added**
- `Hare Koninklijke Hoogheid` — **Added**
- `Zijne Hoogheid` — **Added**
- `Zijne Koninklijke Hoogheid` — **Added**
- `jonkheer` — **Added**
- `jonkvrouw` — **Added**

#### predicaat — **Removed**

##### Literals

- `Hare Hoogheid` — **Removed**
- `Hare Koninklijke Hoogheid` — **Removed**
- `Zijne Hoogheid` — **Removed**
- `Zijne Koninklijke Hoogheid` — **Removed**
- `jonkheer` — **Removed**
- `jonkvrouw` — **Removed**

#### redenEindeRelatie — **Removed**

##### Literals

- `Echtscheiding, ontbinding of eindigen conform Nederlands recht` — **Removed**
- `Naar vreemd recht anders beëindigd` — **Removed**
- `Nietigverklaring` — **Removed**
- `Omzetting van soort verbintenis` — **Removed**
- `Onbekend` — **Removed**
- `Overlijden partner` — **Removed**
- `Rechtsvermoeden van overlijden partner` — **Removed**
- `Vermissing van een persoon gevolgd door andere verbintenis` — **Removed**

#### redenEindeRelatie — **Added**

##### Literals

- `Echtscheiding, ontbinding of eindigen conform Nederlands recht` — **Added**
- `Naar vreemd recht anders beëindigd` — **Added**
- `Nietigverklaring` — **Added**
- `Omzetting van soort verbintenis` — **Added**
- `Onbekend` — **Added**
- `Overlijden partner` — **Added**
- `Rechtsvermoeden van overlijden partner` — **Added**
- `Vermissing van een persoon gevolgd door andere verbintenis` — **Added**

#### redenWijzigingAdres — **Added**

##### Literals

- `Aangifte door persoon` — **Added**
- `Ambtshalve` — **Added**
- `Infrastructurele wijziging` — **Added**
- `Ministerieel besluit` — **Added**
- `Onbekend` — **Added**
- `Technische wijzigingen i.v.m. BAG` — **Added**

#### redenWijzigingAdres — **Removed**

##### Literals

- `Aangifte door persoon` — **Removed**
- `Ambtshalve` — **Removed**
- `Infrastructurele wijziging` — **Removed**
- `Ministerieel besluit` — **Removed**
- `Onbekend` — **Removed**
- `Technische wijzigingen i.v.m. BAG` — **Removed**

#### soortMigratie — **Added**

##### Literals

- `Emigratie` — **Added**
- `Immigratie` — **Added**

#### soortMigratie — **Removed**

##### Literals

- `Emigratie` — **Removed**
- `Immigratie` — **Removed**

#### typeringFunctioneelGebied — **Removed**

##### Literals

- `bedrijvigheid` — **Removed**
- `begraafplaats` — **Removed**
- `benzinestation` — **Removed**
- `bewoning` — **Removed**
- `bushalte` — **Removed**
- `carpoolplaats` — **Removed**
- `functioneel beheer` — **Removed**
- `functioneel beheer:hondenuitlaatplaats` — **Removed**
- `infrastructuur verkeer en vervoer` — **Removed**
- `infrastructuur waterstaatswerken` — **Removed**
- `kering` — **Removed**
- `landbouw` — **Removed**
- `maatschappelijke en / of publieksvoorziening` — **Removed**
- `natuur & landschap` — **Removed**
- `recreatie` — **Removed**
- `recreatie:bungalowpark` — **Removed**
- `recreatie:camping` — **Removed**
- `recreatie:park` — **Removed**
- `recreatie:speeltuin` — **Removed**
- `recreatie:sportterrein` — **Removed**
- `recreatie:volkstuin` — **Removed**
- `verzorgingsplaats` — **Removed**
- `waterbergingsgebied` — **Removed**

#### typeringFunctioneelGebied — **Added**

##### Literals

- `bedrijvigheid` — **Added**
- `begraafplaats` — **Added**
- `benzinestation` — **Added**
- `bewoning` — **Added**
- `bushalte` — **Added**
- `carpoolplaats` — **Added**
- `functioneel beheer` — **Added**
- `functioneel beheer:hondenuitlaatplaats` — **Added**
- `infrastructuur verkeer en vervoer` — **Added**
- `infrastructuur waterstaatswerken` — **Added**
- `kering` — **Added**
- `landbouw` — **Added**
- `maatschappelijke en / of publieksvoorziening` — **Added**
- `natuur & landschap` — **Added**
- `recreatie` — **Added**
- `recreatie:bungalowpark` — **Added**
- `recreatie:camping` — **Added**
- `recreatie:park` — **Added**
- `recreatie:speeltuin` — **Added**
- `recreatie:sportterrein` — **Added**
- `recreatie:volkstuin` — **Added**
- `verzorgingsplaats` — **Added**
- `waterbergingsgebied` — **Added**

#### typeringKunstwerk — **Removed**

##### Literals

- `bodemval` — **Removed**
- `coupure` — **Removed**
- `duiker` — **Removed**
- `faunavoorziening` — **Removed**
- `gemaal` — **Removed**
- `hoogspanningsmast` — **Removed**
- `keermuur` — **Removed**
- `overkluizing` — **Removed**
- `perron` — **Removed**
- `ponton` — **Removed**
- `sluis` — **Removed**
- `steiger` — **Removed**
- `strekdam` — **Removed**
- `stuw` — **Removed**
- `vispassage` — **Removed**
- `voorde` — **Removed**

#### typeringKunstwerk — **Added**

##### Literals

- `bodemval` — **Added**
- `coupure` — **Added**
- `duiker` — **Added**
- `faunavoorziening` — **Added**
- `gemaal` — **Added**
- `hoogspanningsmast` — **Added**
- `keermuur` — **Added**
- `overkluizing` — **Added**
- `perron` — **Added**
- `ponton` — **Added**
- `sluis` — **Added**
- `steiger` — **Added**
- `strekdam` — **Added**
- `stuw` — **Added**
- `vispassage` — **Added**
- `voorde` — **Added**

#### typeringOverigBouwwerk — **Removed**

##### Literals

- `bassin` — **Removed**
- `bezinkbak` — **Removed**
- `bunker` — **Removed**
- `lage trafo` — **Removed**
- `open loods` — **Removed**
- `opslagtank` — **Removed**
- `overkapping` — **Removed**
- `schuur` — **Removed**
- `voedersilo` — **Removed**
- `windturbine` — **Removed**

#### typeringOverigBouwwerk — **Added**

##### Literals

- `bassin` — **Added**
- `bezinkbak` — **Added**
- `bunker` — **Added**
- `lage trafo` — **Added**
- `open loods` — **Added**
- `opslagtank` — **Added**
- `overkapping` — **Added**
- `schuur` — **Added**
- `voedersilo` — **Added**
- `windturbine` — **Added**

#### typeringScheiding — **Removed**

##### Literals

- `damwand` — **Removed**
- `geluidsscherm` — **Removed**
- `hek` — **Removed**
- `kademuur` — **Removed**
- `muur` — **Removed**
- `walbescherming` — **Removed**

#### typeringScheiding — **Added**

##### Literals

- `damwand` — **Added**
- `geluidsscherm` — **Added**
- `hek` — **Added**
- `kademuur` — **Added**
- `muur` — **Added**
- `walbescherming` — **Added**

## Package: Groepattribuutsoort

### Classes

#### AfwijkendBuitenlandsCorrespondentieadresRol — **Unchanged**

##### Attributes

- adresBuitenland1 — **Changed**
  - **primitive**: `` → `AN200`
- adresBuitenland2 — **Changed**
  - **primitive**: `` → `AN200`
- adresBuitenland3 — **Changed**
  - **primitive**: `` → `AN200`

#### AnderZaakobjectZaak — **Unchanged**

##### Attributes

- anderZaakobjectLocatie — **Changed**
  - **primitive**: `GML` → `Point`

_No datatype changes in this package._

_No enumeration changes in this package._

## Package: Metagegevens

### Classes

#### Brondocumenten — **Unchanged**

##### Attributes

- datumDocument — **Changed**
  - **primitive**: `` → `Datum`

#### FormeleHistorie — **Unchanged**

##### Attributes

- tijdstipRegistratieGegevens — **Changed**
  - **primitive**: `` → `DateTime`

#### MaterieleHistorie — **Unchanged**

##### Attributes

- datumBeginGeldigheidGegevens — **Changed**
  - **primitive**: `` → `Datum`
- datumEindeGeldigheidGegevens — **Changed**
  - **primitive**: `` → `Datum`

_No datatype changes in this package._

_No enumeration changes in this package._

## Package: Model

### Classes

#### Periode — **Unchanged**

##### Attributes

- omschrijving — **Changed**
  - **primitive**: `` → `AN255`

_No datatype changes in this package._

_No enumeration changes in this package._

## Package: Model Afval

### Classes

#### Locatie — **Unchanged**

##### Attributes

- locatiePunt — **Changed**
  - **name**: `locatie` → `locatiePunt`
  - **primitive**: `GML` → `Point`

#### Route — **Unchanged**

##### Attributes

- geometrie — **Changed**
  - **primitive**: `GML` → `Point`

_No datatype changes in this package._

_No enumeration changes in this package._

## Package: Model Archeologie

### Classes

#### Kaart — **Unchanged**

##### Attributes

- content — **Changed**
  - **name**: `kaart` → `content`

#### Project — **Unchanged**

##### Attributes

- coordinaten — **Changed**
  - **primitive**: `GML` → `Point`

#### Vindplaats — **Unchanged**

##### Attributes

- locatie — **Changed**
  - **primitive**: `GML` → `Point`
- vindplaatsOmschrijving — **Changed**
  - **name**: `vindplaats` → `vindplaatsOmschrijving`

#### locatie — **Unchanged**

##### Attributes

- locatiePunt — **Changed**
  - **name**: `locatie` → `locatiePunt`
  - **primitive**: `GML` → `Point`

_No datatype changes in this package._

_No enumeration changes in this package._

## Package: Model BAG

### Classes

#### BinnenlandsAdres — **Added**

##### Attributes

- BAGID — **Added**
- gemeentenaam — **Added**
- huisletter — **Added**
- huisnummer — **Added**
- huisnummertoevoeging — **Added**
- postcode — **Added**
- straatnaam — **Added**

#### Nummeraanduiding — **Unchanged**

##### Attributes

- postcode — **Changed**
  - **primitive**: `char` → `AN6`

#### Pand — **Unchanged**

##### Attributes

- oorspronkelijkBouwjaar — **Changed**
  - **primitive**: `JAAR` → `N4`

_No datatype changes in this package._

_No enumeration changes in this package._

## Package: Model Beheer Openbare Ruimte

### Classes

#### Melding — **Unchanged**

##### Attributes

- locatie — **Changed**
  - **primitive**: `Locatie` → `Point`

_No datatype changes in this package._

_No enumeration changes in this package._

## Package: Model Diensten

### Classes

#### Periodiek dienst Bijz. bijstand — **Changed**

- **name**: `Periodiek dienst (Bijz. bijstand)` → `Periodiek dienst Bijz. bijstand`

_No datatype changes in this package._

_No enumeration changes in this package._

## Package: Model Dienstverlening

### Classes

#### AanvraagOfMelding — **Unchanged**

##### Attributes

- afgehandeld — **Changed**
  - **enumeration_id**: `Enumeratie: Boolean` → `Enumeratie: Boolean`

_No datatype changes in this package._

### Enumerations

#### Boolean — **Added**

##### Literals

- `Ja` — **Added**
- `Leeg` — **Added**
- `Nee` — **Added**
- `Onbekend` — **Added**

#### Boolean — **Removed**

##### Literals

- `Ja` — **Removed**
- `Leeg` — **Removed**
- `Nee` — **Removed**
- `Onbekend` — **Removed**

## Package: Model Generiek

### Classes

#### Foto — **Unchanged**

##### Attributes

- locatie — **Changed**
  - **primitive**: `GML` → `Point`

#### Gebied — **Unchanged**

##### Attributes

- gebiedsAanduiding — **Changed**
  - **name**: `gebied` → `gebiedsAanduiding`
  - **primitive**: `Polygoon` → `MultiSurface`

#### Lijn — **Unchanged**

##### Attributes

- lijnLocatie — **Changed**
  - **name**: `lijn` → `lijnLocatie`

#### Punt — **Unchanged**

##### Attributes

- puntLocatie — **Changed**
  - **name**: `punt` → `puntLocatie`

_No datatype changes in this package._

_No enumeration changes in this package._

## Package: Model HR

### Classes

#### Rol — **Unchanged**

##### Attributes

- omschrijving — **Changed**
  - **name**: `rol` → `omschrijving`

_No datatype changes in this package._

_No enumeration changes in this package._

## Package: Model ICT

### Classes

#### Classificatie — **Unchanged**

##### Attributes

- bevatPersoonsgegevens — **Changed**
  - **primitive**: `Persoonsgegevens` → `boolean`
- gerelateerdPersoonsgegevens — **Changed**
  - **primitive**: `Persoonsgegevens` → `AN200`
- id — **Removed**

#### Database — **Unchanged**

##### Attributes

- OTAP — **Changed**
  - **primitive**: `` → `Boolean`
- databaseInstantie — **Changed**
  - **name**: `database` → `databaseInstantie`

_No datatype changes in this package._

_No enumeration changes in this package._

## Package: Model IMBOR

### Classes

#### Beheerobject — **Unchanged**

##### Attributes

- beheerobjectMemo — **Changed**
  - **primitive**: `Memo` → `Tekst`

#### Groenobject — **Unchanged**

##### Attributes

- opTalud — **Changed**
  - **primitive**: `nee` → `Boolean`

#### Installatie — **Unchanged**

##### Attributes

- installateur — **Changed**
  - **primitive**: `Installateur` → ``

#### Leiding — **Unchanged**

##### Attributes

- verhoogdRisico — **Changed**
  - **primitive**: `nee` → `Boolean`

#### Put — **Unchanged**

##### Attributes

- bovengrondsZichtbaar — **Changed**
  - **primitive**: `nee` → `Boolean`

#### Terreindeel — **Unchanged**

##### Attributes

- opTalud — **Changed**
  - **primitive**: `nee` → `Boolean`

#### Verhardingsobject — **Unchanged**

##### Attributes

- opTalud — **Changed**
  - **primitive**: `nee` → `Boolean`

_No datatype changes in this package._

_No enumeration changes in this package._

## Package: Model Inburgering

### Classes

#### Aandachtspunt — **Unchanged**

##### Attributes

- aandachtspuntOmschrijving — **Changed**
  - **name**: `Aandachtspunt` → `aandachtspuntOmschrijving`

#### Asielstatushouder — **Unchanged**

##### Attributes

- DigiD aangevraagd — **Changed**
  - **enumeration_id**: `Enumeratie: Boolean` → `Enumeratie: Boolean`
- Rijbewijs — **Changed**
  - **enumeration_id**: `Enumeratie: Boolean` → `Enumeratie: Boolean`

#### Brede Intake — **Unchanged**

##### Attributes

- AantalUrenAlfabetiseringsOnderwijs — **Added**
- DatumTot(Peildatum) — **Added**
- GevolgdeUrenKNMenTaalles — **Added**
- UrenGeoorloofdVerzuim — **Added**
- UrenOngeoorloofdVerzuim — **Added**
- einddatum — **Added**
- startdatum — **Added**

#### Educatie — **Unchanged**

##### Attributes

- EducatieLand — **Changed**
  - **primitive**: `Enum` → `Land`
  - **type_class_id**: `` → `Objecttype: Land`
- Opleiding — **Changed**
  - **enumeration_id**: `Enumeratie: CodeNiveauOpleiding` → `Enumeratie: CodeNiveauOpleiding`

#### Examen — **Unchanged**

##### Attributes

- ExamenResultaat — **Added**

#### Examenonderdeel — **Unchanged**

##### Attributes

- BehaaldeScore — **Added**
- DatumRegistratieUitslag — **Added**
- ExamenOnderdeelSpecificatie — **Added**
- Ontheffing — **Added**
- RedenVrijstelling — **Added**
- Resultaat — **Added**

#### Inburgeraar — **Unchanged**

##### Attributes

- Gedetailleerde Doelgroep — **Changed**
  - **enumeration_id**: `Enumeratie: Doelgroep` → `Enumeratie: Doelgroep`

#### InburgeringsAanbod — **Unchanged**

##### Attributes

- CursusInstelling — **Changed**
  - **primitive**: `Onderwijsroute` → `AN200`
  - **type_class_id**: `Objecttype: Onderwijsroute` → ``

#### Inburgeringstraject — **Unchanged**

##### Attributes

- UItkomstLeerbaarheidstoets — **Added**

#### KNM — **Removed**

##### Attributes


#### Leerroute — **Unchanged**

##### Attributes

- geenLeerbaarheidstoetsZB — **Changed**
  - **name**: `IndicatorLeerbaarheidstoetsOvergeslagenVanwegeZintuigelijkeBeperking` → `geenLeerbaarheidstoetsZB`

#### MAP — **Unchanged**

##### Attributes

- DatumEindgesprekMAP — **Added**
- IndicatorVerwijtbaar — **Added**
- RedenNietSuccesvolVoltooid — **Added**
- Resultaat — **Added**

#### Onderwijsroute — **Removed**

#### Ontwikkelwens — **Unchanged**

##### Attributes

- ontwikkelwensOmschrijving — **Changed**
  - **name**: `Ontwikkelwens` → `ontwikkelwensOmschrijving`

#### PIP — **Unchanged**

##### Attributes

- DagtekeningInitielePIP — **Added**
- DagtekeningPIP — **Added**
- EmailContactPersoon — **Added**
- IndicatorMagOpleidingAfmaken — **Added**
- NaamContactPersoon — **Added**

#### PVT — **Unchanged**

##### Attributes

- DatumOndertekening PVT — **Added**
- RedenNietVoldaan — **Added**
- Resultaat — **Added**
- VerwijtbaarNietVoldaan — **Added**

#### ParticipatieComponent — **Removed**

##### Attributes


#### Taalonderwijs deelname — **Removed**

#### Taalvaardigheid — **Unchanged**

##### Attributes

- TaalvaardigheidOverall — **Changed**
  - **name**: `Taalvaardigheid` → `TaalvaardigheidOverall`

#### Training — **Unchanged**

##### Attributes

- TrainingGevolgd — **Changed**
  - **name**: `Training` → `TrainingGevolgd`

#### Verblijfplaats — **Removed**

#### Verblijfplaats AZC — **Unchanged**

##### Attributes

- Huisnummer — **Added**
- Plaats — **Added**
- Straatnummer — **Added**

#### Verlengingsgrond — **Unchanged**

##### Attributes

- Verlengingsgrondslag — **Changed**
  - **name**: `Verlengingsgrond` → `Verlengingsgrondslag`

#### Z-route — **Removed**

#### Z-route — **Added**

##### Attributes

- AantalGratisExamenpogingenTegoed — **Added**
- ExamenDatum — **Added**
- GevolgdeUrenParticipatieActiviteiten — **Added**
- Niveau — **Added**
- Onderdeel — **Added**
- RedenGeenResultaat — **Added**
- Resultaat — **Added**

_No datatype changes in this package._

### Enumerations

#### Boolean — **Removed**

##### Literals

- `Ja` — **Removed**
- `Leeg` — **Removed**
- `Nee` — **Removed**
- `Onbekend` — **Removed**

#### Boolean — **Removed**

##### Literals

- `Ja` — **Removed**
- `Leeg` — **Removed**
- `Nee` — **Removed**
- `Onbekend` — **Removed**

#### Boolean — **Added**

##### Literals

- `Ja` — **Added**
- `Leeg` — **Added**
- `Nee` — **Added**
- `Onbekend` — **Added**

#### Boolean — **Added**

##### Literals

- `Ja` — **Added**
- `Leeg` — **Added**
- `Nee` — **Added**
- `Onbekend` — **Added**

#### CodeNiveauOpleiding — **Removed**

##### Literals

- `Basisonderwijs` — **Removed**
- `HAVO / VWO` — **Removed**
- `HBO / Bachelor` — **Removed**
- `MBO` — **Removed**
- `VMBO / MBO-1` — **Removed**
- `WO / Master` — **Removed**

#### CodeNiveauOpleiding — **Added**

##### Literals

- `Basisonderwijs` — **Added**
- `HAVO / VWO` — **Added**
- `HBO / Bachelor` — **Added**
- `MBO` — **Added**
- `VMBO / MBO-1` — **Added**
- `WO / Master` — **Added**

#### Doelgroep — **Removed**

##### Literals

- `Asielstatushouder` — **Removed**
- `Geestelijk bedienaar` — **Removed**
- `Gezinshereniger` — **Removed**
- `Gezinshereniger met Asielstatushouder` — **Removed**
- `Gezinsvormer` — **Removed**
- `Gezinsvormer met Asielstatushouder` — **Removed**
- `Overig` — **Removed**

#### Doelgroep — **Added**

##### Literals

- `Arbeidsmigranten met vestigingsintentie` — **Added**
- `EU-burgers` — **Added**
- `Expats en kennismigranten` — **Added**
- `Gezinsmigranten` — **Added**
- `Internationale studenten (blijvers)` — **Added**
- `Kwetsbare nieuwkomers` — **Added**
- `Nieuwkomers` — **Added**
- `Oudkomers` — **Added**

## Package: Model Inkomen

### Classes

#### Inkomensvoorzieningsoort — **Unchanged**

##### Attributes

- wet — **Changed**
  - **enumeration_id**: `Enumeratie: Wet` → `Enumeratie: Wet`

_No datatype changes in this package._

### Enumerations

#### Wet — **Removed**

##### Literals

- `Andere wet` — **Removed**
- `Bijzondere Bijstand` — **Removed**
- `I.O.A.W./I.O.A.Z.` — **Removed**
- `Jeugdwet` — **Removed**
- `Leeg` — **Removed**
- `Niet van toepassing` — **Removed**
- `Onbekend` — **Removed**
- `Participatiewet PW-I` — **Removed**
- `Wmo` — **Removed**

#### Wet — **Added**

##### Literals

- `Andere wet` — **Added**
- `Bijzondere Bijstand` — **Added**
- `I.O.A.W./I.O.A.Z.` — **Added**
- `Jeugdwet` — **Added**
- `Leeg` — **Added**
- `Niet van toepassing` — **Added**
- `Onbekend` — **Added**
- `Participatiewet PW-I` — **Added**
- `Wmo` — **Added**

## Package: Model Inkomsten

### Classes

#### Alimentatie — **Unchanged**

##### Attributes

- Alimentatie.Id — **Removed**
- Bedrag aan andere rekeningen — **Changed**
  - **primitive**: `Geldbedrag` → `Bedrag`
- Bedrag in convenant — **Changed**
  - **primitive**: `StdIndJN` → `Boolean`
- BijdrageExPartnerAndereRekeningen — **Changed**
  - **name**: `Bijdrage ex partner voor andere rekeningen` → `BijdrageExPartnerAndereRekeningen`
  - **primitive**: `StdIndJN` → `Boolean`
- Inkomstensoort alimentatie — **Changed**
  - **enumeration_id**: `` → `Enumeratie: InkomstensoortAlimentatie`
  - **type_class_id**: `Objecttype: EAID_07E4E120_7D9E_3C43_1D1F_26EBD1635427` → ``
- Juiste bedrag betaald door ex partner — **Changed**
  - **primitive**: `StdIndJN` → `Boolean`
- LBIO ingeschakeld — **Changed**
  - **primitive**: `StdIndJN` → `Boolean`

#### Ander inkomen — **Unchanged**

##### Attributes

- AnderInkomen.Id — **Removed**

#### Betaald werk — **Unchanged**

##### Attributes

- Arbeidscontract — **Changed**
  - **primitive**: `StdIndJN` → `Boolean`
- BetaaldWerk.Id — **Removed**
- Inkomsten uit IKB-regeling — **Changed**
  - **primitive**: `StdIndJN` → `Boolean`
- Inkomstensoort betaald werk — **Changed**
  - **enumeration_id**: `` → `Enumeratie: InkomstensoortBetaaldWerk`
  - **type_class_id**: `Objecttype: EAID_24104FB5_2F1C_EFBF_8AC3_26EBD163D2F4` → ``
- Loondienst — **Changed**
  - **primitive**: `StdIndJN` → `Boolean`
- Periodiciteit uitbetaling loon — **Changed**
  - **enumeration_id**: `` → `Enumeratie: CdUitkeringsperiode`
  - **type_class_id**: `Objecttype: EAID_1FA03C02_F7CE_31C4_506D_273ED24EBECD` → ``
- Soort contract — **Changed**
  - **enumeration_id**: `` → `Enumeratie: SoortContract`
  - **type_class_id**: `Objecttype: EAID_0C0AD449_ECBB_8C03_B698_26EBD163CD95` → ``

#### Dertiende maand - eindejaarsuitkering — **Unchanged**

##### Attributes

- DertiendeMaandEindejaarsuitkering.Id — **Removed**

#### Draagkracht — **Unchanged**

##### Attributes

- Draagkracht.Id — **Removed**

#### Draagkrachtregime — **Unchanged**

##### Attributes

- Draagkrachtregime.Id — **Removed**
- Initiele draagkracht — **Changed**
  - **primitive**: `Geldbedrag` → `Bedrag`
- Resterende draagkracht — **Changed**
  - **primitive**: `Geldbedrag` → `Bedrag`

#### Eigen bedrijf — **Unchanged**

##### Attributes

- EigenBedrijf.Id — **Removed**
- Ingeschreven bij KvK — **Changed**
  - **primitive**: `StdIndJN` → `Boolean`
- Recht op zelfstandigenaftrek — **Changed**
  - **primitive**: `StdIndJN` → `Boolean`
- Toestemming gemeente parttime ondernemen — **Changed**
  - **primitive**: `StdIndJN` → `Boolean`

#### Heffingskorting — **Unchanged**

##### Attributes

- Algemene heffingskorting — **Changed**
  - **primitive**: `StdIndJN` → `Boolean`
- Heffingskorting.Id — **Removed**
- Inkomensafhankelijke combinatiekorting — **Changed**
  - **primitive**: `StdIndJN` → `Boolean`

#### Hobby — **Unchanged**

##### Attributes

- Hobby.Id — **Removed**

#### Inkomstencomponent — **Unchanged**

##### Attributes

- Bijgevoegd bewijs — **Changed**
  - **primitive**: `StdIndJN` → `Boolean`
- Bruto-Netto — **Changed**
  - **enumeration_id**: `` → `Enumeratie: BrutoNettoInkomsten`
  - **type_class_id**: `Objecttype: EAID_189703AD_5462_E8C7_C523_293A5A46936C` → ``
- Inkomsten — **Changed**
  - **primitive**: `Geldbedrag` → `Bedrag`
- Inkomstencomponent.Id — **Removed**
- Inkomstencomponenttype — **Changed**
  - **enumeration_id**: `` → `Enumeratie: Inkomstencomponenttype`
  - **type_class_id**: `Objecttype: EAID_e92e0ca6_9e22_40f9_a1af_d8a44889963b` → ``

#### Inkomstenverhouding — **Unchanged**

##### Attributes

- Categorie Inkomsten — **Changed**
  - **enumeration_id**: `` → `Enumeratie: CdSrtInkomstenverhouding`
  - **type_class_id**: `Objecttype: EAID_1CFCC259_4648_55CC_95EC_273ED24D398A` → ``
- Inkomstenverhouding.Id — **Removed**

#### Inkomstenvermindering — **Unchanged**

##### Attributes

- Inkomstenvermindering.Id — **Removed**

#### Kostencomponent — **Unchanged**

##### Attributes

- Bedrag — **Changed**
  - **primitive**: `Geldbedrag` → `Bedrag`
- Kostencomponent.Id — **Removed**

#### Loonbeslag — **Unchanged**

##### Attributes

- Loonbeslag.Id — **Removed**

#### Maaltijdvergoeding — **Unchanged**

##### Attributes

- Maaltijdvergoeding.Id — **Removed**

#### Onderhoudsplicht — **Unchanged**

##### Attributes

- Bijdrage — **Changed**
  - **primitive**: `Geldbedrag` → `Bedrag`
- Onderhoudsplicht.Id — **Removed**
- Onderhoudsplichttype — **Changed**
  - **enumeration_id**: `` → `Enumeratie: Onderhoudsplichttype`
  - **type_class_id**: `Objecttype: EAID_b4380c62_69ef_4b52_8585_5cccdc9c5d72` → ``

#### Onderhoudsverhouding — **Unchanged**

##### Attributes

- Onderhoudsverhouding.Id — **Removed**

#### Onkostenvergoeding — **Unchanged**

##### Attributes

- Onkostenvergoeding.Id — **Removed**

#### Pensioen — **Unchanged**

##### Attributes

- Beslag op pensioen — **Changed**
  - **primitive**: `StdIndJN` → `Boolean`
- Inkomstensoort pensioen — **Changed**
  - **enumeration_id**: `` → `Enumeratie: InkomstensoortPensioen`
  - **type_class_id**: `Objecttype: EAID_10635E76_7AF2_1575_DDF8_26EBD163EC4C` → ``
- Loonheffingskorting — **Changed**
  - **primitive**: `StdIndJN` → `Boolean`
- Pensioen.Id — **Removed**
- Periodiciteit uitbetaling pensioen — **Changed**
  - **enumeration_id**: `` → `Enumeratie: CdUitkeringsperiode`
  - **type_class_id**: `Objecttype: EAID_1FA03C02_F7CE_31C4_506D_273ED24EBECD` → ``

#### Primair inkomstencomponent — **Unchanged**

##### Attributes

- PrimairInkomstencomponent.Id — **Removed**

#### Reiskostenvergoeding — **Unchanged**

##### Attributes

- Reiskostenvergoeding.Id — **Removed**

#### Secundair inkomstencomponent — **Unchanged**

##### Attributes

- SecundairInkomstencomponent.Id — **Removed**

#### Stage — **Unchanged**

##### Attributes

- Maaltijdvergoeding — **Changed**
  - **primitive**: `StdIndJN` → `Boolean`
- Onkostenvergoeding — **Changed**
  - **primitive**: `StdIndJN` → `Boolean`
- Periodiciteit uitbetaling loon — **Changed**
  - **enumeration_id**: `` → `Enumeratie: CdUitkeringsperiode`
  - **type_class_id**: `Objecttype: EAID_1FA03C02_F7CE_31C4_506D_273ED24EBECD` → ``
- Reiskostenvergoeding — **Changed**
  - **primitive**: `StdIndJN` → `Boolean`
- Stage.Id — **Removed**
- Vergoeding in natura — **Changed**
  - **primitive**: `StdIndJN` → `Boolean`

#### Studiefinanciering — **Unchanged**

##### Attributes

- Daadwerkelijk Genoten — **Changed**
  - **primitive**: `StdIndJN` → `Boolean`
- Inkomstensoort studiefinanciering — **Changed**
  - **enumeration_id**: `` → `Enumeratie: InkomstensoortStudiefinanciering`
  - **type_class_id**: `Objecttype: EAID_1A0F77A2_EC7C_BFAE_32D3_26EBD1630331` → ``
- Studiefinanciering.Id — **Removed**

#### Uitkering — **Unchanged**

##### Attributes

- Beslag op uitkering — **Changed**
  - **primitive**: `StdIndJN` → `Boolean`
- Inkomstensoort uitkering — **Changed**
  - **enumeration_id**: `` → `Enumeratie: CdSzWet`
  - **type_class_id**: `Objecttype: EAID_0AFBC0B5_2217_3FED_8EE6_273ED24E9888` → ``
- Loonheffingskorting — **Changed**
  - **primitive**: `StdIndJN` → `Boolean`
- Periodiciteit uitbetaling uitkering — **Changed**
  - **enumeration_id**: `` → `Enumeratie: CdUitkeringsperiode`
  - **type_class_id**: `Objecttype: EAID_1FA03C02_F7CE_31C4_506D_273ED24EBECD` → ``
- Toeslag op uitkering — **Changed**
  - **primitive**: `StdIndJN` → `Boolean`
- Uitkering verlaagd door boete — **Changed**
  - **primitive**: `StdIndJN` → `Boolean`
- Uitkering verlaagd door maatregel — **Changed**
  - **primitive**: `StdIndJN` → `Boolean`
- Uitkering.Id — **Removed**
- Vakantiegeld jaarlijks ontvangen — **Changed**
  - **primitive**: `StdIndJN` → `Boolean`

#### Vakantiegeld — **Unchanged**

##### Attributes

- Vakantiegeld.Id — **Removed**

#### Vergoeding — **Unchanged**

##### Attributes

- Vergoeding.Id — **Removed**

#### Vergoeding in natura — **Unchanged**

##### Attributes

- VergoedingInNatura.Id — **Removed**

#### Verlaging door boete — **Unchanged**

##### Attributes

- VerlagingDoorBoete.Id — **Removed**

#### Verlaging door maatregel — **Unchanged**

##### Attributes

- VerlagingDoorMaatregel.Id — **Removed**

#### Vrijlating inkomsten — **Unchanged**

##### Attributes

- Doelgroep — **Changed**
  - **enumeration_id**: `` → `Enumeratie: JsonRuledGroupType`
  - **type_class_id**: `Objecttype: EAID_05A0B109_A778_273A_32B0_28DF727D601A` → ``
- Medisch — **Changed**
  - **primitive**: `StdIndJN` → `Boolean`
- Soort vrijlating — **Changed**
  - **enumeration_id**: `` → `Enumeratie: CodeSoortVrijlating`
  - **type_class_id**: `Objecttype: EAID_0B35B810_5B49_6EF7_F1E9_2871B3C11F1D` → ``
- Vrijgelaten bedrag — **Changed**
  - **primitive**: `Geldbedrag` → `Bedrag`
- VrijlatingInkomsten.Id — **Removed**

_No datatype changes in this package._

### Enumerations

#### BrutoNettoInkomsten — **Added**

#### CdSrtInkomstenverhouding — **Added**

#### CdSzWet — **Added**

#### CdUitkeringsperiode — **Added**

#### CdUitkeringsperiode — **Added**

#### CdUitkeringsperiode — **Added**

#### CdUitkeringsperiode — **Added**

#### CodeSoortVrijlating — **Added**

#### Inkomstencomponenttype — **Added**

#### InkomstensoortAlimentatie — **Added**

#### InkomstensoortBetaaldWerk — **Added**

#### InkomstensoortPensioen — **Added**

#### InkomstensoortStudiefinanciering — **Added**

#### JsonRuledGroupType — **Added**

#### Onderhoudsplichttype — **Added**

#### SoortContract — **Added**

## Package: Model Inkoop

### Classes

#### Aanbesteding Inhuur — **Unchanged**

##### Attributes

- datumSluiting — **Removed**

_No datatype changes in this package._

_No enumeration changes in this package._

## Package: Model Jeugd en Wmo Generiek

### Classes

#### Beschikking — **Unchanged**

##### Attributes

- wet — **Changed**
  - **primitive**: `` → `Wet`
  - **enumeration_id**: `` → `Enumeratie: Wet`

_No datatype changes in this package._

_No enumeration changes in this package._

## Package: Model Jeugdbescherming

### Classes

#### Leefgebied — **Unchanged**

##### Attributes

- leefgebiedOmschrijving — **Changed**
  - **name**: `leefgebied` → `leefgebiedOmschrijving`

_No datatype changes in this package._

_No enumeration changes in this package._

## Package: Model Kern RGBZ

### Classes

#### Bedrijfsproces — **Unchanged**

##### Attributes

- Afgerond — **Changed**
  - **enumeration_id**: `Enumeratie: Boolean` → `Enumeratie: Boolean`

#### Bedrijfsprocestype — **Unchanged**

##### Attributes

- Omschrijving — **Changed**
  - **primitive**: `AM200` → `AN200`

#### Besluit — **Unchanged**

##### Attributes

- datumBesluit — **Changed**
  - **primitive**: `` → `Datum`
- datumPublicatie — **Changed**
  - **primitive**: `` → `Datum`
- datumStart — **Changed**
  - **primitive**: `` → `Datum`
- datumUiterlijkeReactie — **Changed**
  - **primitive**: `` → `Datum`
- datumVerval — **Changed**
  - **primitive**: `` → `Datum`
- datumVerzending — **Changed**
  - **primitive**: `` → `Datum`
- omschrijving — **Changed**
  - **name**: `besluit` → `omschrijving`
- redenVerval — **Changed**
  - **primitive**: `X40` → `AN40`

#### Betrokkene — **Unchanged**

##### Attributes

- adresBinnenland — **Changed**
  - **primitive**: `` → `BinnenlandsAdres`
  - **type_class_id**: `` → `Objecttype: BinnenlandsAdres`
- adresBuitenland — **Changed**
  - **primitive**: `` → `AN200`

#### Document — **Unchanged**

##### Attributes

- datumCreatieDocument — **Changed**
  - **primitive**: `` → `Datum`
- datumOntvangstdocument — **Changed**
  - **primitive**: `` → `Datum`
- datumVerzendingDocument — **Changed**
  - **primitive**: `` → `Datum`

#### EnkelvoudigDocument — **Unchanged**

##### Attributes

- documentInhoud — **Changed**
  - **primitive**: `Documentformaat` → `AN255`

#### Heffing — **Unchanged**

##### Attributes


#### Klantcontact — **Unchanged**

##### Attributes


#### Medewerker — **Unchanged**

##### Attributes

- datumUitDienst — **Changed**
  - **primitive**: `` → `Datum`

#### Object — **Unchanged**

##### Attributes

- adresBinnenland — **Changed**
  - **primitive**: `` → `BinnenlandsAdres`
  - **type_class_id**: `` → `Objecttype: BinnenlandsAdres`
- adresBuitenland — **Changed**
  - **primitive**: `` → `AN200`
- geometrie — **Changed**
  - **primitive**: `GML` → `Point`
- toelichting — **Changed**
  - **primitive**: `` → `Tekst`

#### OrganisatorischeEenheid — **Unchanged**

##### Attributes

- Formatie — **Changed**
  - **stereotype**: `` → `Attribuutsoort`
  - **primitive**: `` → `AN255`
- datumOntstaan — **Changed**
  - **primitive**: `` → `Datum`
- datumOpheffing — **Changed**
  - **primitive**: `` → `Datum`

#### Status — **Unchanged**

##### Attributes

- datumStatusGezet — **Changed**
  - **primitive**: `` → `Datum`

#### ZAAK - Origineel — **Unchanged**

##### Attributes

- datumEinde — **Changed**
  - **primitive**: `` → `Datum`
- datumEindeGepland — **Changed**
  - **primitive**: `` → `Datum`
- datumEindeUiterlijkeAfdoening — **Changed**
  - **primitive**: `` → `Datum`
- datumLaatsteBetaling — **Changed**
  - **primitive**: `` → `Datum`
- datumRegistratie — **Changed**
  - **primitive**: `` → `Datum`
- datumStart — **Changed**
  - **primitive**: `` → `Datum`
- datumVernietigingDossier — **Changed**
  - **primitive**: `` → `Datum`
- indicatieDeelzaken — **Changed**
  - **primitive**: `A1` → ``

#### Zaak — **Unchanged**

##### Attributes

- datumEinde — **Changed**
  - **primitive**: `` → `Datum`
- datumEindeGepland — **Changed**
  - **primitive**: `` → `Datum`
- datumEindeUiterlijkeAfdoening — **Changed**
  - **primitive**: `` → `Datum`
- datumLaatsteBetaling — **Changed**
  - **primitive**: `` → `Datum`
- datumRegistratie — **Changed**
  - **primitive**: `` → `Datum`
- datumStart — **Changed**
  - **primitive**: `` → `Datum`
- datumVernietigingDossier — **Changed**
  - **primitive**: `` → `Datum`
- indicatieDeelzaken — **Changed**
  - **primitive**: `A1` → ``

_No datatype changes in this package._

### Enumerations

#### Boolean — **Removed**

##### Literals

- `Ja` — **Removed**
- `Leeg` — **Removed**
- `Nee` — **Removed**
- `Onbekend` — **Removed**

#### Boolean — **Added**

##### Literals

- `Ja` — **Added**
- `Leeg` — **Added**
- `Nee` — **Added**
- `Onbekend` — **Added**

#### Heffingsoort — **Removed**

##### Literals

- `leges` — **Removed**
- `precario` — **Removed**

#### Heffingsoort — **Added**

##### Literals

- `leges` — **Added**
- `precario` — **Added**

#### Soorten Klantcontact — **Added**

##### Literals

- `balie` — **Added**
- `brief` — **Added**
- `internet` — **Added**
- `selfserviceloket` — **Added**
- `telefonisch` — **Added**

#### Soorten Klantcontact — **Removed**

##### Literals

- `balie` — **Removed**
- `brief` — **Removed**
- `internet` — **Removed**
- `selfserviceloket` — **Removed**
- `telefonisch` — **Removed**

## Package: Model Kern RSGB

### Classes

#### GebouwdObject — **Unchanged**

##### Attributes

- bouwkundigeBestemmingActueel — **Changed**
  - **enumeration_id**: `Enumeratie: bouwkundigeBestemming` → `Enumeratie: bouwkundigeBestemming`
- inwinningOppervlakte — **Changed**
  - **enumeration_id**: `Enumeratie: inwinningsmethodeOppervlakte` → `Enumeratie: inwinningsmethodeOppervlakte`
- statusVoortgangBouw — **Changed**
  - **primitive**: `` → `statusVoortgangBouw`
  - **enumeration_id**: `` → `Enumeratie: statusVoortgangBouw`

#### Ligplaats — **Unchanged**

##### Attributes

- indicatieGeconstateerdeLigplaats — **Changed**
  - **primitive**: `INDIC` → `boolean`
- ligplaatsstatus — **Changed**
  - **enumeration_id**: `Enumeratie: StatLigplaatsStandplaats` → `Enumeratie: StatLigplaatsStandplaats`

#### Nummeraanduiding — **Unchanged**

##### Attributes

- geconstateerd — **Changed**
  - **primitive**: `INDIC` → `boolean`
- postcode — **Changed**
  - **primitive**: `POSTCODE` → `AN6`
- status — **Changed**
  - **enumeration_id**: `Enumeratie: statusNummeraanduiding` → `Enumeratie: statusNummeraanduiding`
- typeAdresseerbaarObject — **Changed**
  - **enumeration_id**: `Enumeratie: TypeAdresseerbaarObject` → `Enumeratie: TypeAdresseerbaarObject`

#### OpenbareRuimte — **Unchanged**

##### Attributes

- statusOpenbareRuimte — **Changed**
  - **enumeration_id**: `Enumeratie: statusOpenbareRuimte` → `Enumeratie: statusOpenbareRuimte`
- typeOpenbareRuimte — **Changed**
  - **enumeration_id**: `Enumeratie: typeringOpenbareRuimte` → `Enumeratie: typeringOpenbareRuimte`

#### Pand — **Unchanged**

##### Attributes

- indicatieGeconstateerdPand — **Changed**
  - **primitive**: `INDIC` → `boolean`
- indicatiePlanobject — **Changed**
  - **primitive**: `INDIC` → `boolean`
- inwinningGeometrieBovenaanzicht — **Changed**
  - **enumeration_id**: `Enumeratie: inwinningsmethodeGeometrie` → `Enumeratie: inwinningsmethodeGeometrie`
- inwinningGeometrieMaaiveld — **Changed**
  - **enumeration_id**: `Enumeratie: inwinningsmethodeGeometrie` → `Enumeratie: inwinningsmethodeGeometrie`
- oorspronkelijkBouwjaarPand — **Changed**
  - **primitive**: `JAAR` → `N4`
- pandstatus — **Changed**
  - **enumeration_id**: `Enumeratie: statusPand` → `Enumeratie: statusPand`
- statusVoortgangBouw — **Changed**
  - **enumeration_id**: `Enumeratie: statusVoortgangBouw` → `Enumeratie: statusVoortgangBouw`

#### Standplaats — **Unchanged**

##### Attributes

- indicatieGeconstateerdeStandplaats — **Changed**
  - **primitive**: `INDIC` → `boolean`
- standplaatsstatus — **Changed**
  - **enumeration_id**: `Enumeratie: StatLigplaatsStandplaats` → `Enumeratie: StatLigplaatsStandplaats`

#### Verblijfsobject — **Unchanged**

##### Attributes

- ontsluitingVerdieping — **Changed**
  - **enumeration_id**: `Enumeratie: ontsluitingswijzeVerdieping` → `Enumeratie: ontsluitingswijzeVerdieping`
- soortWoonobject — **Changed**
  - **enumeration_id**: `Enumeratie: soortWoonobject` → `Enumeratie: soortWoonobject`
- verblijfsobjectstatus — **Changed**
  - **enumeration_id**: `Enumeratie: statusVerblijfsobject` → `Enumeratie: statusVerblijfsobject`

#### Woonplaats — **Unchanged**

##### Attributes

- woonplaatsStatus — **Changed**
  - **enumeration_id**: `Enumeratie: statusWoonplaats` → `Enumeratie: statusWoonplaats`

_No datatype changes in this package._

### Enumerations

#### StatLigplaatsStandplaats — **Removed**

##### Literals

- `Leeg` — **Removed**
- `Onbekend` — **Removed**
- `plaats aangewezen` — **Removed**
- `plaats ingetrokken` — **Removed**

#### StatLigplaatsStandplaats — **Added**

##### Literals

- `Leeg` — **Added**
- `Onbekend` — **Added**
- `plaats aangewezen` — **Added**
- `plaats ingetrokken` — **Added**

#### StatLigplaatsStandplaats — **Added**

##### Literals

- `Leeg` — **Added**
- `Onbekend` — **Added**
- `plaats aangewezen` — **Added**
- `plaats ingetrokken` — **Added**

#### StatLigplaatsStandplaats — **Removed**

##### Literals

- `Leeg` — **Removed**
- `Onbekend` — **Removed**
- `plaats aangewezen` — **Removed**
- `plaats ingetrokken` — **Removed**

#### TypeAdresseerbaarObject — **Removed**

##### Literals

- `KADbinnenlandsadres` — **Removed**
- `Leeg` — **Removed**
- `Ligplaats` — **Removed**
- `Onbekend` — **Removed**
- `Standplaats` — **Removed**
- `Verblijfsobject` — **Removed**

#### TypeAdresseerbaarObject — **Added**

##### Literals

- `KADbinnenlandsadres` — **Added**
- `Leeg` — **Added**
- `Ligplaats` — **Added**
- `Onbekend` — **Added**
- `Standplaats` — **Added**
- `Verblijfsobject` — **Added**

#### bouwkundigeBestemming — **Removed**

##### Literals

- `CAI` — **Removed**
- `aanleunwoonverblijf` — **Removed**
- `academisch onderwijs` — **Removed**
- `akkerbouw` — **Removed**
- `algemeen voortgezet onderwijs` — **Removed**
- `andere doeleinden van openbaar nut` — **Removed**
- `basisschool` — **Removed**
- `begraafplaats/crematorium` — **Removed**
- `bejaardenwoning` — **Removed**
- `bejaardenwoonverblijf (in bejaardenoord, centrale keuken)` — **Removed**
- `bibliotheek` — **Removed**
- `bijzonder onderwijs` — **Removed**
- `bioscoop` — **Removed**
- `brandweer` — **Removed**
- `cafe/bar/restaurant` — **Removed**
- `congres` — **Removed**
- `dagverblijf` — **Removed**
- `defensie` — **Removed**
- `detailhandel` — **Removed**
- `dienstwoning` — **Removed**
- `dierenverzorging` — **Removed**
- `doeleinden voor agrarisch bedrijf` — **Removed**
- `doeleinden voor cultuur` — **Removed**
- `doeleinden voor gezondheidszorg` — **Removed**
- `doeleinden voor handel, horeca en bedrijf` — **Removed**
- `doeleinden voor niet-wonen` — **Removed**
- `doeleinden voor nutsvoorzieningen` — **Removed**
- `doeleinden voor onderwijs` — **Removed**
- `doeleinden voor recreatie` — **Removed**
- `doeleinden voor verkeer` — **Removed**
- `doeleinden voor wonen` — **Removed**
- `eengezinswoning` — **Removed**
- `elektriciteit` — **Removed**
- `expositie` — **Removed**
- `fabricage en productie` — **Removed**
- `gas` — **Removed**
- `gehandicaptenwooneenheid` — **Removed**
- `gemeentehuis` — **Removed**
- `gemengd bedrijf` — **Removed**
- `gevangenis/gesticht` — **Removed**
- `godsdienst (kerk, klooster e.d.)` — **Removed**
- `hoger beroepsonderwijs` — **Removed**
- `hotel/logies` — **Removed**
- `jongerenwooneenheid` — **Removed**
- `kantoor` — **Removed**
- `kinderopvang` — **Removed**
- `laboratoria` — **Removed**
- `luchtvaart` — **Removed**
- `meergezinswoning` — **Removed**
- `musea` — **Removed**
- `natuur en landschap` — **Removed**
- `onderhoud en reparatie` — **Removed**
- `opslag en distributie` — **Removed**
- `overige andere doeleinden van openbaar nut` — **Removed**
- `overige doeleinden voor agrarisch bedrijf` — **Removed**
- `overige doeleinden voor cultuur` — **Removed**
- `overige doeleinden voor gezondheidszorg` — **Removed**
- `overige doeleinden voor niet-wonen` — **Removed**
- `overige doeleinden voor nutsvoorzieningen` — **Removed**
- `overige doeleinden voor onderwijs` — **Removed**
- `overige doeleinden voor recreatie` — **Removed**
- `overige doeleinden voor verkeer` — **Removed**
- `polikliniek` — **Removed**
- `politie` — **Removed**
- `praktijkruimte` — **Removed**
- `psychiatrische inrichting` — **Removed**
- `recreatie` — **Removed**
- `recreatiewoning` — **Removed**
- `scheepvaart` — **Removed**
- `spoorwegverkeer` — **Removed**
- `sport binnen` — **Removed**
- `sport buiten` — **Removed**
- `stalling (fietsen/auto's)` — **Removed**
- `telecommunicatie` — **Removed**
- `theater en concert` — **Removed**
- `tuinbouw` — **Removed**
- `veeteelt` — **Removed**
- `verpleegtehuis` — **Removed**
- `verzorgingstehuis en bejaardentehuis` — **Removed**
- `vrijetijds onderwijs` — **Removed**
- `waternuts doeleinden` — **Removed**
- `waterschaps en waterverdediging` — **Removed**
- `wegverkeer` — **Removed**
- `wijk-/buurt-/verenigingsactiviteiten` — **Removed**
- `wijkverzorging` — **Removed**
- `ziekenhuis` — **Removed**
- `zorgwoonverblijf` — **Removed**
- `zwembad` — **Removed**

#### bouwkundigeBestemming — **Added**

##### Literals

- `CAI` — **Added**
- `aanleunwoonverblijf` — **Added**
- `academisch onderwijs` — **Added**
- `akkerbouw` — **Added**
- `algemeen voortgezet onderwijs` — **Added**
- `andere doeleinden van openbaar nut` — **Added**
- `basisschool` — **Added**
- `begraafplaats/crematorium` — **Added**
- `bejaardenwoning` — **Added**
- `bejaardenwoonverblijf (in bejaardenoord, centrale keuken)` — **Added**
- `bibliotheek` — **Added**
- `bijzonder onderwijs` — **Added**
- `bioscoop` — **Added**
- `brandweer` — **Added**
- `cafe/bar/restaurant` — **Added**
- `congres` — **Added**
- `dagverblijf` — **Added**
- `defensie` — **Added**
- `detailhandel` — **Added**
- `dienstwoning` — **Added**
- `dierenverzorging` — **Added**
- `doeleinden voor agrarisch bedrijf` — **Added**
- `doeleinden voor cultuur` — **Added**
- `doeleinden voor gezondheidszorg` — **Added**
- `doeleinden voor handel, horeca en bedrijf` — **Added**
- `doeleinden voor niet-wonen` — **Added**
- `doeleinden voor nutsvoorzieningen` — **Added**
- `doeleinden voor onderwijs` — **Added**
- `doeleinden voor recreatie` — **Added**
- `doeleinden voor verkeer` — **Added**
- `doeleinden voor wonen` — **Added**
- `eengezinswoning` — **Added**
- `elektriciteit` — **Added**
- `expositie` — **Added**
- `fabricage en productie` — **Added**
- `gas` — **Added**
- `gehandicaptenwooneenheid` — **Added**
- `gemeentehuis` — **Added**
- `gemengd bedrijf` — **Added**
- `gevangenis/gesticht` — **Added**
- `godsdienst (kerk, klooster e.d.)` — **Added**
- `hoger beroepsonderwijs` — **Added**
- `hotel/logies` — **Added**
- `jongerenwooneenheid` — **Added**
- `kantoor` — **Added**
- `kinderopvang` — **Added**
- `laboratoria` — **Added**
- `luchtvaart` — **Added**
- `meergezinswoning` — **Added**
- `musea` — **Added**
- `natuur en landschap` — **Added**
- `onderhoud en reparatie` — **Added**
- `opslag en distributie` — **Added**
- `overige andere doeleinden van openbaar nut` — **Added**
- `overige doeleinden voor agrarisch bedrijf` — **Added**
- `overige doeleinden voor cultuur` — **Added**
- `overige doeleinden voor gezondheidszorg` — **Added**
- `overige doeleinden voor niet-wonen` — **Added**
- `overige doeleinden voor nutsvoorzieningen` — **Added**
- `overige doeleinden voor onderwijs` — **Added**
- `overige doeleinden voor recreatie` — **Added**
- `overige doeleinden voor verkeer` — **Added**
- `polikliniek` — **Added**
- `politie` — **Added**
- `praktijkruimte` — **Added**
- `psychiatrische inrichting` — **Added**
- `recreatie` — **Added**
- `recreatiewoning` — **Added**
- `scheepvaart` — **Added**
- `spoorwegverkeer` — **Added**
- `sport binnen` — **Added**
- `sport buiten` — **Added**
- `stalling (fietsen/auto's)` — **Added**
- `telecommunicatie` — **Added**
- `theater en concert` — **Added**
- `tuinbouw` — **Added**
- `veeteelt` — **Added**
- `verpleegtehuis` — **Added**
- `verzorgingstehuis en bejaardentehuis` — **Added**
- `vrijetijds onderwijs` — **Added**
- `waternuts doeleinden` — **Added**
- `waterschaps en waterverdediging` — **Added**
- `wegverkeer` — **Added**
- `wijk-/buurt-/verenigingsactiviteiten` — **Added**
- `wijkverzorging` — **Added**
- `ziekenhuis` — **Added**
- `zorgwoonverblijf` — **Added**
- `zwembad` — **Added**

#### gebruiksdoel — **Added**

##### Literals

- `Leeg` — **Added**
- `Onbekend` — **Added**
- `bijeenkomstfunctie` — **Added**
- `celfunctie` — **Added**
- `gezondheidszorgfunctie` — **Added**
- `industriefunctie` — **Added**
- `kantoorfunctie` — **Added**
- `logiesfunctie` — **Added**
- `onderwijsfunctie` — **Added**
- `overige gebruiksfunctie` — **Added**
- `sportfunctie` — **Added**
- `winkelfunctie` — **Added**
- `woonfunctie` — **Added**

#### gebruiksdoel — **Removed**

##### Literals

- `Leeg` — **Removed**
- `Onbekend` — **Removed**
- `bijeenkomstfunctie` — **Removed**
- `celfunctie` — **Removed**
- `gezondheidszorgfunctie` — **Removed**
- `industriefunctie` — **Removed**
- `kantoorfunctie` — **Removed**
- `logiesfunctie` — **Removed**
- `onderwijsfunctie` — **Removed**
- `overige gebruiksfunctie` — **Removed**
- `sportfunctie` — **Removed**
- `winkelfunctie` — **Removed**
- `woonfunctie` — **Removed**

#### inwinningsmethodeGeometrie — **Added**

##### Literals

- `bouwtekening` — **Added**
- `digitaliseren` — **Added**
- `fotogrammetrisch` — **Added**
- `geconstrueerd` — **Added**
- `laser` — **Added**
- `niet bekend` — **Added**
- `panoramabeelden` — **Added**
- `scannen` — **Added**
- `terrestrisch` — **Added**

#### inwinningsmethodeGeometrie — **Removed**

##### Literals

- `bouwtekening` — **Removed**
- `digitaliseren` — **Removed**
- `fotogrammetrisch` — **Removed**
- `geconstrueerd` — **Removed**
- `laser` — **Removed**
- `niet bekend` — **Removed**
- `panoramabeelden` — **Removed**
- `scannen` — **Removed**
- `terrestrisch` — **Removed**

#### inwinningsmethodeGeometrie — **Added**

##### Literals

- `bouwtekening` — **Added**
- `digitaliseren` — **Added**
- `fotogrammetrisch` — **Added**
- `geconstrueerd` — **Added**
- `laser` — **Added**
- `niet bekend` — **Added**
- `panoramabeelden` — **Added**
- `scannen` — **Added**
- `terrestrisch` — **Added**

#### inwinningsmethodeGeometrie — **Removed**

##### Literals

- `bouwtekening` — **Removed**
- `digitaliseren` — **Removed**
- `fotogrammetrisch` — **Removed**
- `geconstrueerd` — **Removed**
- `laser` — **Removed**
- `niet bekend` — **Removed**
- `panoramabeelden` — **Removed**
- `scannen` — **Removed**
- `terrestrisch` — **Removed**

#### inwinningsmethodeOppervlakte — **Removed**

##### Literals

- `gemeten op basis van de bouwtekening` — **Removed**
- `initiële vulling d.m.v. conversietabel inhoud-oppervlak` — **Removed**
- `initiële vulling d.m.v. gegevens bouw- en woningtoezicht` — **Removed**
- `initiële vulling d.m.v. gegevens woningbouwvereniging` — **Removed**
- `initiële vulling d.m.v. oppervlaktegegevens WOZ-administratie` — **Removed**
- `initiële vulling d.m.v. overige brongegevens` — **Removed**
- `overgenomen uit bouwaanvraag` — **Removed**
- `ter plaatse ingemeten` — **Removed**

#### inwinningsmethodeOppervlakte — **Added**

##### Literals

- `gemeten op basis van de bouwtekening` — **Added**
- `initiële vulling d.m.v. conversietabel inhoud-oppervlak` — **Added**
- `initiële vulling d.m.v. gegevens bouw- en woningtoezicht` — **Added**
- `initiële vulling d.m.v. gegevens woningbouwvereniging` — **Added**
- `initiële vulling d.m.v. oppervlaktegegevens WOZ-administratie` — **Added**
- `initiële vulling d.m.v. overige brongegevens` — **Added**
- `overgenomen uit bouwaanvraag` — **Added**
- `ter plaatse ingemeten` — **Added**

#### ontsluitingswijzeVerdieping — **Added**

##### Literals

- `Leeg` — **Added**
- `Onbekend` — **Added**
- `lift` — **Added**
- `roltrap` — **Added**
- `trap` — **Added**

#### ontsluitingswijzeVerdieping — **Removed**

##### Literals

- `Leeg` — **Removed**
- `Onbekend` — **Removed**
- `lift` — **Removed**
- `roltrap` — **Removed**
- `trap` — **Removed**

#### soortWoonobject — **Added**

##### Literals

- `Leeg` — **Added**
- `Onbekend` — **Added**
- `bijzonder woongebouw` — **Added**
- `overig woonverblijf` — **Added**
- `recreatiewoning` — **Added**
- `woning` — **Added**
- `wooneenheid` — **Added**

#### soortWoonobject — **Removed**

##### Literals

- `Leeg` — **Removed**
- `Onbekend` — **Removed**
- `bijzonder woongebouw` — **Removed**
- `overig woonverblijf` — **Removed**
- `recreatiewoning` — **Removed**
- `woning` — **Removed**
- `wooneenheid` — **Removed**

#### statusNummeraanduiding — **Added**

##### Literals

- `Leeg` — **Added**
- `Onbekend` — **Added**
- `naamgeving ingetrokken` — **Added**
- `naamgeving uitgegeven` — **Added**

#### statusNummeraanduiding — **Removed**

##### Literals

- `Leeg` — **Removed**
- `Onbekend` — **Removed**
- `naamgeving ingetrokken` — **Removed**
- `naamgeving uitgegeven` — **Removed**

#### statusOpenbareRuimte — **Removed**

##### Literals

- `Leeg` — **Removed**
- `Onbekend` — **Removed**
- `naamgeving ingetrokken` — **Removed**
- `naamgeving uitgegeven` — **Removed**

#### statusOpenbareRuimte — **Added**

##### Literals

- `Leeg` — **Added**
- `Onbekend` — **Added**
- `naamgeving ingetrokken` — **Added**
- `naamgeving uitgegeven` — **Added**

#### statusPand — **Removed**

##### Literals

- `Leeg` — **Removed**
- `Onbekend` — **Removed**
- `bouw gestart` — **Removed**
- `bouwaanvraag ontvangen` — **Removed**
- `bouwvergunning verleend` — **Removed**
- `niet gerealiseerd pand` — **Removed**
- `pand buiten gebruik` — **Removed**
- `pand gesloopt` — **Removed**
- `pand in gebruik` — **Removed**
- `pand in gebruik (niet ingemeten)` — **Removed**
- `pand ten onrechte opgevoerd` — **Removed**
- `sloopvergunning verleend` — **Removed**
- `verbouwing pand` — **Removed**

#### statusPand — **Added**

##### Literals

- `Leeg` — **Added**
- `Onbekend` — **Added**
- `bouw gestart` — **Added**
- `bouwaanvraag ontvangen` — **Added**
- `bouwvergunning verleend` — **Added**
- `niet gerealiseerd pand` — **Added**
- `pand buiten gebruik` — **Added**
- `pand gesloopt` — **Added**
- `pand in gebruik` — **Added**
- `pand in gebruik (niet ingemeten)` — **Added**
- `pand ten onrechte opgevoerd` — **Added**
- `sloopvergunning verleend` — **Added**
- `verbouwing pand` — **Added**

#### statusVerblijfsobject — **Removed**

##### Literals

- `Leeg` — **Removed**
- `Onbekend` — **Removed**
- `niet gerealiseerd verblijfsobject` — **Removed**
- `verblijfsobject buiten gebruik` — **Removed**
- `verblijfsobject gevormd` — **Removed**
- `verblijfsobject in gebruik` — **Removed**
- `verblijfsobject in gebruik (niet ingemeten)` — **Removed**
- `verblijfsobject ingetrokken` — **Removed**

#### statusVerblijfsobject — **Added**

##### Literals

- `Leeg` — **Added**
- `Onbekend` — **Added**
- `niet gerealiseerd verblijfsobject` — **Added**
- `verblijfsobject buiten gebruik` — **Added**
- `verblijfsobject gevormd` — **Added**
- `verblijfsobject in gebruik` — **Added**
- `verblijfsobject in gebruik (niet ingemeten)` — **Added**
- `verblijfsobject ingetrokken` — **Added**

#### statusVoortgangBouw — **Added**

##### Literals

- `Leeg` — **Added**
- `Onbekend` — **Added**
- `nieuwbouw gereed` — **Added**
- `nieuwbouw gestart` — **Added**
- `nieuwbouwvergunning ingetrokken` — **Added**
- `nieuwbouwvergunning verleend` — **Added**
- `sloop gereed` — **Added**
- `sloop gestart` — **Added**
- `sloopvergunning ingetrokken` — **Added**
- `sloopvergunning verleend` — **Added**
- `verbouw gereed` — **Added**
- `verbouw gestart` — **Added**
- `verbouwvergunning ingetrokken` — **Added**
- `verbouwvergunning verleend` — **Added**

#### statusVoortgangBouw — **Added**

##### Literals

- `Leeg` — **Added**
- `Onbekend` — **Added**
- `nieuwbouw gereed` — **Added**
- `nieuwbouw gestart` — **Added**
- `nieuwbouwvergunning ingetrokken` — **Added**
- `nieuwbouwvergunning verleend` — **Added**
- `sloop gereed` — **Added**
- `sloop gestart` — **Added**
- `sloopvergunning ingetrokken` — **Added**
- `sloopvergunning verleend` — **Added**
- `verbouw gereed` — **Added**
- `verbouw gestart` — **Added**
- `verbouwvergunning ingetrokken` — **Added**
- `verbouwvergunning verleend` — **Added**

#### statusVoortgangBouw — **Removed**

##### Literals

- `Leeg` — **Removed**
- `Onbekend` — **Removed**
- `nieuwbouw gereed` — **Removed**
- `nieuwbouw gestart` — **Removed**
- `nieuwbouwvergunning ingetrokken` — **Removed**
- `nieuwbouwvergunning verleend` — **Removed**
- `sloop gereed` — **Removed**
- `sloop gestart` — **Removed**
- `sloopvergunning ingetrokken` — **Removed**
- `sloopvergunning verleend` — **Removed**
- `verbouw gereed` — **Removed**
- `verbouw gestart` — **Removed**
- `verbouwvergunning ingetrokken` — **Removed**
- `verbouwvergunning verleend` — **Removed**

#### statusWoonplaats — **Added**

##### Literals

- `Leeg` — **Added**
- `Onbekend` — **Added**
- `woonplaats aangewezen` — **Added**
- `woonplaats ingetrokken` — **Added**

#### statusWoonplaats — **Removed**

##### Literals

- `Leeg` — **Removed**
- `Onbekend` — **Removed**
- `woonplaats aangewezen` — **Removed**
- `woonplaats ingetrokken` — **Removed**

#### typeringOpenbareRuimte — **Removed**

##### Literals

- `Leeg` — **Removed**
- `Onbekend` — **Removed**
- `administratief gebied` — **Removed**
- `functioneel gebied` — **Removed**
- `kunstwerk` — **Removed**
- `landschappelijk gebied` — **Removed**
- `spoorbaan` — **Removed**
- `terrein` — **Removed**
- `water` — **Removed**
- `weg` — **Removed**

#### typeringOpenbareRuimte — **Added**

##### Literals

- `Leeg` — **Added**
- `Onbekend` — **Added**
- `administratief gebied` — **Added**
- `functioneel gebied` — **Added**
- `kunstwerk` — **Added**
- `landschappelijk gebied` — **Added**
- `spoorbaan` — **Added**
- `terrein` — **Added**
- `water` — **Added**
- `weg` — **Added**

## Package: Model Kern RSGB

### Classes

#### Appartementsrechtsplitsing — **Unchanged**

##### Attributes

- typeSplitsing — **Changed**
  - **primitive**: `` → `typeringAppartementsrechtsplitsing`
  - **enumeration_id**: `` → `Enumeratie: typeringAppartementsrechtsplitsing`

#### BegroeidTerreindeel — **Unchanged**

##### Attributes

- LOD0Geometrie — **Changed**
  - **name**: `LOD0GeometrieBegroeidTerreindeel` → `LOD0Geometrie`
- datumBeginGeldigheid — **Changed**
  - **name**: `datumBeginGeldigheidBegroeidTerreindeel` → `datumBeginGeldigheid`
- datumEindeGeldigheid — **Changed**
  - **name**: `datumEindeGeldigheidBegroeidTerreindeel` → `datumEindeGeldigheid`
- fysiekVoorkomen — **Changed**
  - **name**: `fysiekVoorkomenBegroeidTerreindeel` → `fysiekVoorkomen`
  - **enumeration_id**: `Enumeratie: fysiekVoorkomenBegroeidTerrein` → `Enumeratie: fysiekVoorkomenBegroeidTerrein`
- geometrie — **Changed**
  - **name**: `geometrieBegroeidTerreindeel` → `geometrie`
- identificatie — **Changed**
  - **name**: `identificatieBegroeidTerreindeel` → `identificatie`
- kruinlijngeometrie — **Changed**
  - **name**: `kruinlijngeometrieBegroeidTerreindeel` → `kruinlijngeometrie`
- opTalud — **Changed**
  - **name**: `begroeidTerreindeelOpTalud` → `opTalud`
  - **primitive**: `INDIC` → `boolean`
- plusFysiekVoorkomen — **Changed**
  - **name**: `plusFysiekVoorkomenBegroeidTerreindeel` → `plusFysiekVoorkomen`
  - **enumeration_id**: `Enumeratie: fysiekVoorkomenBegroeidTerreinPlus` → `Enumeratie: fysiekVoorkomenBegroeidTerreinPlus`
- relatieveHoogteligging — **Changed**
  - **name**: `relatieveHoogteliggingBegroeidTerreindeel` → `relatieveHoogteligging`
- status — **Changed**
  - **name**: `statusBegroeidTerreindeel` → `status`
  - **enumeration_id**: `Enumeratie: statusGeoObject` → `Enumeratie: statusGeoObject`

#### Briefadres — **Unchanged**

##### Attributes

- adresFunctie — **Changed**
  - **primitive**: `` → `An200`
- omschrijvingAangifte — **Changed**
  - **primitive**: `Text` → `AN255`

#### FunctioneelGebied — **Unchanged**

##### Attributes

- statusFunctioneelGebied — **Changed**
  - **enumeration_id**: `Enumeratie: statusGeoObject` → `Enumeratie: statusGeoObject`

#### Gebouwinstallatie — **Unchanged**

##### Attributes

- statusGebouwinstallatie — **Changed**
  - **enumeration_id**: `Enumeratie: statusGeoObject` → `Enumeratie: statusGeoObject`
- typeGebouwinstallatie — **Changed**
  - **enumeration_id**: `Enumeratie: typeringGebouwinstallatie` → `Enumeratie: typeringGebouwinstallatie`

#### IngeschrevenPersoon — **Unchanged**

##### Attributes

- gezinsrelatie — **Changed**
  - **enumeration_id**: `Enumeratie: Gezinsrelatie` → `Enumeratie: Gezinsrelatie`
- indicatieGeheim — **Changed**
  - **enumeration_id**: `Enumeratie: Boolean` → `Enumeratie: Boolean`
- ingezetene — **Changed**
  - **enumeration_id**: `Enumeratie: Boolean` → `Enumeratie: Boolean`
- signaleringReisdocument — **Changed**
  - **enumeration_id**: `Enumeratie: Boolean` → `Enumeratie: Boolean`

#### Inrichtingselement — **Unchanged**

##### Attributes

- LOD0GeometrieInrichtingselement — **Changed**
  - **primitive**: `PuntLijnVlak` → `Surface`
- geometrieInrichtingselement — **Changed**
  - **primitive**: `PuntLijnVlak` → `Surface`
- plusTypeInrichtingselement — **Changed**
  - **enumeration_id**: `Enumeratie: typeringInrichtingselementPlus` → `Enumeratie: typeringInrichtingselementPlus`
- statusInrichtingselement — **Changed**
  - **enumeration_id**: `Enumeratie: statusGeoObject` → `Enumeratie: statusGeoObject`
- typeInrichtingselement — **Changed**
  - **enumeration_id**: `Enumeratie: typeringInrichtingselement` → `Enumeratie: typeringInrichtingselement`

#### KadastraalPerceel — **Unchanged**

##### Attributes

- indicatieDeelperceel — **Changed**
  - **primitive**: `INDIC` → `boolean`

#### KadastraleOnroerendeZaak — **Unchanged**

##### Attributes

- appartementsrechtvolgnummer — **Changed**
  - **stereotype**: `Data element` → `Attribuutsoort`
- datumBeginGeldigheid — **Changed**
  - **name**: `datumBeginGeldigheidKadastraleOnroerendeZaak` → `datumBeginGeldigheid`
- datumEindeGeldigheid — **Changed**
  - **name**: `datumEindeGeldigheidKadastraleOnroerendeZaak` → `datumEindeGeldigheid`
- perceelnummer — **Changed**
  - **stereotype**: `Data element` → `Attribuutsoort`

#### Kunstwerkdeel — **Unchanged**

##### Attributes

- LOD0GeometrieKunstwerkdeel — **Changed**
  - **primitive**: `PuntLijnVlak` → `Surface`
- statusKunstwerkdeel — **Changed**
  - **enumeration_id**: `Enumeratie: statusGeoObject` → `Enumeratie: statusGeoObject`

#### MaatschappelijkeActiviteit — **Unchanged**

##### Attributes

- adresBinnenland — **Changed**
  - **primitive**: `AN257` → `BinnenlandsAdres`
  - **type_class_id**: `` → `Objecttype: BinnenlandsAdres`
- indicatieEconomischActief — **Changed**
  - **primitive**: `INDIC` → `boolean`

#### Nationaliteit — **Unchanged**

##### Attributes

- omschrijving — **Changed**
  - **name**: `Nationaliteit` → `omschrijving`
- redenVerkrijgingNLNationaliteit — **Changed**
  - **name**: `Reden verkrijging Nederlandse nationaliteit` → `redenVerkrijgingNLNationaliteit`
- redenVerliesNLNationaliteit — **Changed**
  - **name**: `Reden verlies Nederlandse nationaliteit` → `redenVerliesNLNationaliteit`

#### NatuurlijkPersoon — **Unchanged**

##### Attributes

- adellijkeTitelOfPredikaat — **Changed**
  - **enumeration_id**: `Enumeratie: adelijkeTitel` → `Enumeratie: adelijkeTitel`
- bijzonderNederlanderschap — **Changed**
  - **name**: `aanduidingBijzonderNederlanderschapPersoon` → `bijzonderNederlanderschap`
- geslachtsaanduiding — **Changed**
  - **primitive**: `geslacht` → `A1`
  - **enumeration_id**: `Enumeratie: geslacht` → ``

#### NietNatuurlijkPersoon — **Unchanged**

##### Attributes

- rechtsvorm — **Changed**
  - **enumeration_id**: `Enumeratie: soortRechtsvorm` → `Enumeratie: soortRechtsvorm`

#### OnbegroeidTerreindeel — **Unchanged**

##### Attributes

- datumBeginGeldigheid — **Changed**
  - **name**: `datumBeginGeldigheidOnbegroeidTerreindeel` → `datumBeginGeldigheid`
- datumEindeGeldigheid — **Changed**
  - **name**: `datumEindeGeldigheidOnbegroeidTerreindeel` → `datumEindeGeldigheid`
- fysiekVoorkomen — **Changed**
  - **name**: `fysiekVoorkomenOnbegroeidTerreindeel` → `fysiekVoorkomen`
  - **enumeration_id**: `Enumeratie: fysiekVoorkomenOnbegroeidTerrein` → `Enumeratie: fysiekVoorkomenOnbegroeidTerrein`
- geometrie — **Changed**
  - **name**: `geometrieOnbegroeidTerreindeel` → `geometrie`
- identificatie — **Changed**
  - **name**: `identificatieOnbegroeidTerreindeel` → `identificatie`
- kruinlijngeometrie — **Changed**
  - **name**: `kruinlijngeometrieOnbegroeidTerreindeel` → `kruinlijngeometrie`
- onbegroeidTerreindeelOpTalud — **Changed**
  - **primitive**: `INDIC` → `boolean`
- plusFysiekVoorkomen — **Changed**
  - **name**: `plusFysiekVoorkomenOnbegroeidTerreindeel` → `plusFysiekVoorkomen`
  - **enumeration_id**: `Enumeratie: fysiekVoorkomenOnbegroeidTerreinPlus` → `Enumeratie: fysiekVoorkomenOnbegroeidTerreinPlus`
- relatieveHoogteligging — **Changed**
  - **name**: `relatieveHoogteliggingOnbegroeidTerreindeel` → `relatieveHoogteligging`
- status — **Changed**
  - **name**: `statusOnbegroeidTerreindeel` → `status`
  - **enumeration_id**: `Enumeratie: statusGeoObject` → `Enumeratie: statusGeoObject`

#### Onbestemd Adres — **Unchanged**

##### Attributes

- postcode — **Changed**
  - **primitive**: `postcode` → `AN6`

#### OndersteunendWaterdeel — **Unchanged**

##### Attributes

- datumBeginGeldigheid — **Changed**
  - **name**: `datumBeginGeldigheidOndersteunendWaterdeel` → `datumBeginGeldigheid`
- datumEindeGeldigheid — **Changed**
  - **name**: `datumEindeGeldigheidOndersteunendWaterdeel` → `datumEindeGeldigheid`
- geometrie — **Changed**
  - **name**: `geometrieOndersteunendWaterdeel` → `geometrie`
- identificatie — **Changed**
  - **name**: `identificatieOndersteunendWaterdeel` → `identificatie`
- plusType — **Changed**
  - **name**: `plusTypeOndersteunendWaterdeel` → `plusType`
  - **enumeration_id**: `Enumeratie: typeringOndersteunendWaterPlus` → ``
- relatieveHoogteligging — **Changed**
  - **name**: `relatieveHoogteliggingOndersteunendWaterdeel` → `relatieveHoogteligging`
- status — **Changed**
  - **name**: `statusOndersteunendWaterdeel` → `status`
  - **enumeration_id**: `Enumeratie: statusGeoObject` → `Enumeratie: statusGeoObject`
- type — **Changed**
  - **name**: `typeOndersteunendWaterdeel` → `type`
  - **enumeration_id**: `Enumeratie: typeringOndersteunendWater` → `Enumeratie: typeringOndersteunendWater`

#### OndersteunendWegdeel — **Unchanged**

##### Attributes

- LOD0Geometrie — **Changed**
  - **name**: `LOD0GeometrieOndersteunendWegdeel` → `LOD0Geometrie`
- datumBeginGeldigheid — **Changed**
  - **name**: `datumBeginGeldigheidOndersteunendWegdeel` → `datumBeginGeldigheid`
- datumEindeGeldigheid — **Changed**
  - **name**: `datumEindeGeldigheidOndersteunendWegdeel` → `datumEindeGeldigheid`
- functie — **Changed**
  - **name**: `functieOndersteunendWegdeel` → `functie`
  - **enumeration_id**: `Enumeratie: functieOndersteunendWegdeel` → `Enumeratie: functieOndersteunendWegdeel`
- fysiekVoorkomen — **Changed**
  - **name**: `fysiekVoorkomenOndersteunendWegdeel ` → `fysiekVoorkomen`
  - **enumeration_id**: `Enumeratie: fysiekVoorkomenOndersteunendWegdeel` → `Enumeratie: fysiekVoorkomenOndersteunendWegdeel`
- geometrie — **Changed**
  - **name**: `geometrieOndersteunendWegdeel` → `geometrie`
- identificatie — **Changed**
  - **name**: `identificatieOndersteunendWegdeel` → `identificatie`
- kruinlijngeometrie — **Changed**
  - **name**: `kruinlijngeometrieOndersteunendWegdeel` → `kruinlijngeometrie`
- opTalud — **Changed**
  - **name**: `ondersteunendWegdeelOpTalud` → `opTalud`
  - **primitive**: `INDIC` → `boolean`
- plusFunctie — **Changed**
  - **name**: `plusFunctieOndersteunendWegdeel` → `plusFunctie`
  - **enumeration_id**: `Enumeratie: functieOndersteunendWegdeelPlus` → ``
- plusFysiekVoorkomen — **Changed**
  - **name**: `plusFysiekVoorkomenOndersteunendWegdeel` → `plusFysiekVoorkomen`
  - **enumeration_id**: `Enumeratie: fysiekVoorkomenOndersteunendWegdeelPlus` → `Enumeratie: fysiekVoorkomenOndersteunendWegdeelPlus`
- relatieveHoogteligging — **Changed**
  - **name**: `relatieveHoogteliggingOndersteunendWegdeel` → `relatieveHoogteligging`
- status — **Changed**
  - **name**: `statusOndersteunendWegdeel` → `status`
  - **enumeration_id**: `Enumeratie: statusGeoObject` → `Enumeratie: statusGeoObject`

#### Overbruggingsdeel — **Unchanged**

##### Attributes

- hoortBijTypeOverbrugging — **Changed**
  - **enumeration_id**: `Enumeratie: typeOverbrugging` → `Enumeratie: typeOverbrugging`
- overbruggingIsBeweegbaar — **Changed**
  - **primitive**: `INDIC` → ``
- statusOverbruggingsdeel — **Changed**
  - **enumeration_id**: `Enumeratie: statusGeoObject` → `Enumeratie: statusGeoObject`
- typeOverbruggingsdeel — **Changed**
  - **enumeration_id**: `Enumeratie: typeringOverbruggingsdeel` → `Enumeratie: typeringOverbruggingsdeel`

#### OverigBenoemdTerrein — **Unchanged**

##### Attributes

- gebruiksdoelOverigBenoemdTerrein — **Changed**
  - **enumeration_id**: `Enumeratie: gebruiksdoel` → `Enumeratie: gebruiksdoel`

#### OverigBouwwerk — **Unchanged**

##### Attributes

- LOD0GeometrieOverigBouwwerk — **Changed**
  - **primitive**: `PuntLijnVlak` → `Surface`
- statusOverigBouwwerk — **Changed**
  - **enumeration_id**: `Enumeratie: statusGeoObject` → `Enumeratie: statusGeoObject`

#### OverigGebouwdObject — **Unchanged**

##### Attributes

- bouwjaar — **Changed**
  - **primitive**: `JAAR` → `N4`
- indicatiePlanobject — **Changed**
  - **primitive**: `INDIC` → `boolean`

#### OverigeAdresseerbaarObjectAanduiding — **Unchanged**

##### Attributes

- Identificatiecode — **Changed**
  - **name**: `IdentificatiecodeOverigAdresseerbaarObjectAanduiding` → `Identificatiecode`

#### OverigeScheiding — **Unchanged**

##### Attributes

- LOD0GeometrieOverigeScheiding — **Changed**
  - **primitive**: `PuntLijnVlak` → `Surface`
- statusOverigeScheiding — **Changed**
  - **enumeration_id**: `Enumeratie: statusGeoObject` → `Enumeratie: statusGeoObject`
- typeOverigeScheiding — **Changed**
  - **enumeration_id**: `Enumeratie: typeringOverigeScheiding` → `Enumeratie: typeringOverigeScheiding`

#### Rechtspersoon — **Unchanged**

##### Attributes

- adresBinnenland — **Changed**
  - **primitive**: `AN257` → `BinnenlandsAdres`
  - **type_class_id**: `` → `Objecttype: BinnenlandsAdres`

#### Reisdocument — **Unchanged**

##### Attributes

- aanduidingInhoudingVermissing — **Changed**
  - **enumeration_id**: `Enumeratie: aanduidingInhoudingVermissingReisdocument` → `Enumeratie: aanduidingInhoudingVermissingReisdocument`
- datumEindeGeldigheidDocument — **Changed**
  - **primitive**: `` → `Datum`
- datumIngangDocument — **Changed**
  - **primitive**: `` → `Datum`
- datumInhoudingOfVermissing — **Changed**
  - **primitive**: `` → `Datum`
- datumUitgifte — **Changed**
  - **primitive**: `` → `Datum`

#### Scheiding — **Unchanged**

##### Attributes

- LOD0GeometrieScheiding — **Changed**
  - **primitive**: `PuntLijnVlak` → `Surface`
- statusScheiding — **Changed**
  - **enumeration_id**: `Enumeratie: statusGeoObject` → `Enumeratie: statusGeoObject`

#### Spoor — **Unchanged**

##### Attributes

- statusSpoor — **Changed**
  - **enumeration_id**: `Enumeratie: statusGeoObject` → `Enumeratie: statusGeoObject`

#### Tenaamstelling — **Unchanged**

##### Attributes

- burgerlijkeStaatTenTijdeVanVerkrijging — **Changed**
  - **enumeration_id**: `Enumeratie: burgelijkeStaat` → `Enumeratie: burgelijkeStaat`
- exploitantcode — **Changed**
  - **enumeration_id**: `Enumeratie: codeExploitant` → `Enumeratie: codeExploitant`
- verkregenNamensSamenwerkingsverband — **Changed**
  - **enumeration_id**: `Enumeratie: soortRechtsvorm` → `Enumeratie: soortRechtsvorm`

#### Tunneldeel — **Unchanged**

##### Attributes

- statusTunneldeel — **Changed**
  - **enumeration_id**: `Enumeratie: statusGeoObject` → `Enumeratie: statusGeoObject`

#### Vegetatieobject — **Unchanged**

##### Attributes

- LOD0GeometrieVegetatieobject — **Changed**
  - **primitive**: `PuntLijnVlak` → `Surface`
- geometrieVegetatieobject — **Changed**
  - **primitive**: `PuntLijnVlak` → `Surface`
- statusVegetatieobject — **Changed**
  - **enumeration_id**: `Enumeratie: statusGeoObject` → `Enumeratie: statusGeoObject`
- typeVegetatieobject — **Changed**
  - **enumeration_id**: `Enumeratie: typeringVegetatieobject` → `Enumeratie: typeringVegetatieobject`

#### Vestiging — **Unchanged**

##### Attributes

- commercieleVestiging — **Changed**
  - **enumeration_id**: `Enumeratie: Boolean` → `Enumeratie: Boolean`

#### WOZ-Waarde — **Unchanged**

##### Attributes

- statusBeschikking — **Changed**
  - **enumeration_id**: `Enumeratie: statusWOZ-Beschikking` → `Enumeratie: statusWOZ-Beschikking`

#### WOZ-deelobject — **Unchanged**

##### Attributes

- statusWOZDeelobject — **Changed**
  - **enumeration_id**: `Enumeratie: statusWOZ(Deel)Object` → `Enumeratie: statusWOZ(Deel)Object`

#### WOZ-object — **Unchanged**

##### Attributes

- gebruikscode — **Changed**
  - **enumeration_id**: `Enumeratie: soortGebruik` → `Enumeratie: soortGebruik`
- statusWOZObject — **Changed**
  - **enumeration_id**: `Enumeratie: statusWOZ(Deel)Object` → `Enumeratie: statusWOZ(Deel)Object`

#### Waterdeel — **Unchanged**

##### Attributes

- plusTypeWaterdeel — **Changed**
  - **enumeration_id**: `Enumeratie: typeringWaterPlus` → `Enumeratie: typeringWaterPlus`
- statusWaterdeel — **Changed**
  - **enumeration_id**: `Enumeratie: statusGeoObject` → `Enumeratie: statusGeoObject`
- typeWaterdeel — **Changed**
  - **enumeration_id**: `Enumeratie: typeringWater` → `Enumeratie: typeringWater`

#### Wegdeel — **Unchanged**

##### Attributes

- functieWegdeel — **Changed**
  - **enumeration_id**: `Enumeratie: functieWeg` → `Enumeratie: functieWeg`
- fysiekVoorkomenWegdeel — **Changed**
  - **enumeration_id**: `Enumeratie: fysiekVoorkomenWeg` → `Enumeratie: fysiekVoorkomenWeg`
- plusFunctieWegdeel — **Changed**
  - **enumeration_id**: `Enumeratie: functieWegPlus` → `Enumeratie: functieWegPlus`
- plusFysiekVoorkomenWegdeel — **Changed**
  - **enumeration_id**: `Enumeratie: fysiekVoorkomenWegPlus` → `Enumeratie: fysiekVoorkomenWegPlus`
- statusWegdeel — **Changed**
  - **enumeration_id**: `Enumeratie: statusGeoObject` → `Enumeratie: statusGeoObject`
- wegdeelOpTalud — **Changed**
  - **primitive**: `INDIC` → `boolean`

#### Zekerheidsrecht — **Unchanged**

##### Attributes

- omschrijvingBetrokkenRecht — **Changed**
  - **primitive**: `AN` → `AN255`
- typeZekerheidsrecht — **Changed**
  - **enumeration_id**: `Enumeratie: typeringZekerheidsrecht` → `Enumeratie: typeringZekerheidsrecht`

_No datatype changes in this package._

### Enumerations

#### Boolean — **Added**

##### Literals

- `Ja` — **Added**
- `Leeg` — **Added**
- `Nee` — **Added**
- `Onbekend` — **Added**

#### Boolean — **Removed**

##### Literals

- `Ja` — **Removed**
- `Leeg` — **Removed**
- `Nee` — **Removed**
- `Onbekend` — **Removed**

#### Boolean — **Added**

##### Literals

- `Ja` — **Added**
- `Leeg` — **Added**
- `Nee` — **Added**
- `Onbekend` — **Added**

#### Boolean — **Removed**

##### Literals

- `Ja` — **Removed**
- `Leeg` — **Removed**
- `Nee` — **Removed**
- `Onbekend` — **Removed**

#### Boolean — **Removed**

##### Literals

- `Ja` — **Removed**
- `Leeg` — **Removed**
- `Nee` — **Removed**
- `Onbekend` — **Removed**

#### Boolean — **Removed**

##### Literals

- `Ja` — **Removed**
- `Leeg` — **Removed**
- `Nee` — **Removed**
- `Onbekend` — **Removed**

#### Boolean — **Added**

##### Literals

- `Ja` — **Added**
- `Leeg` — **Added**
- `Nee` — **Added**
- `Onbekend` — **Added**

#### Boolean — **Added**

##### Literals

- `Ja` — **Added**
- `Leeg` — **Added**
- `Nee` — **Added**
- `Onbekend` — **Added**

#### Gezinsrelatie — **Removed**

##### Literals

- `Alleenstaand/Samenwonend` — **Removed**
- `Echtgenote binnen gezin` — **Removed**
- `Hoofd gezin met kind(eren)` — **Removed**
- `Hoofd gezin zonder kind(eren)` — **Removed**
- `Hoofd huwelijk gelijk geslacht` — **Removed**
- `Hoofd partnerrelatie` — **Removed**
- `Kind` — **Removed**
- `Leeg` — **Removed**
- `Onbekend` — **Removed**
- `Ouder met kind(eren)` — **Removed**

#### Gezinsrelatie — **Added**

##### Literals

- `Alleenstaand/Samenwonend` — **Added**
- `Echtgenote binnen gezin` — **Added**
- `Hoofd gezin met kind(eren)` — **Added**
- `Hoofd gezin zonder kind(eren)` — **Added**
- `Hoofd huwelijk gelijk geslacht` — **Added**
- `Hoofd partnerrelatie` — **Added**
- `Kind` — **Added**
- `Leeg` — **Added**
- `Onbekend` — **Added**
- `Ouder met kind(eren)` — **Added**

#### aanduidingInhoudingVermissingReisdocument — **Added**

##### Literals

- `Ingehouden, ingeleverd` — **Added**
- `Onbekend` — **Added**
- `Rechtswege` — **Added**
- `Vermist` — **Added**

#### aanduidingInhoudingVermissingReisdocument — **Removed**

##### Literals

- `Ingehouden, ingeleverd` — **Removed**
- `Onbekend` — **Removed**
- `Rechtswege` — **Removed**
- `Vermist` — **Removed**

#### adelijkeTitel — **Added**

##### Literals

- `Leeg` — **Added**
- `Onbekend` — **Added**
- `baron` — **Added**
- `barones` — **Added**
- `graaf` — **Added**
- `gravin` — **Added**
- `hertog` — **Added**
- `hertogin` — **Added**
- `markies` — **Added**
- `markiezin` — **Added**
- `prins` — **Added**
- `prinses` — **Added**
- `ridder` — **Added**

#### adelijkeTitel — **Removed**

##### Literals

- `Leeg` — **Removed**
- `Onbekend` — **Removed**
- `baron` — **Removed**
- `barones` — **Removed**
- `graaf` — **Removed**
- `gravin` — **Removed**
- `hertog` — **Removed**
- `hertogin` — **Removed**
- `markies` — **Removed**
- `markiezin` — **Removed**
- `prins` — **Removed**
- `prinses` — **Removed**
- `ridder` — **Removed**

#### burgelijkeStaat — **Added**

##### Literals

- `achtergebeleven partner` — **Added**
- `gehuwd` — **Added**
- `gescheiden` — **Added**
- `onbekend` — **Added**
- `ongehuwd en nooit gehuwd geweest` — **Added**
- `parnetschap beeeindigd` — **Added**
- `partnerschap` — **Added**
- `weduwe / weduwnaar` — **Added**

#### burgelijkeStaat — **Removed**

##### Literals

- `achtergebeleven partner` — **Removed**
- `gehuwd` — **Removed**
- `gescheiden` — **Removed**
- `onbekend` — **Removed**
- `ongehuwd en nooit gehuwd geweest` — **Removed**
- `parnetschap beeeindigd` — **Removed**
- `partnerschap` — **Removed**
- `weduwe / weduwnaar` — **Removed**

#### codeExploitant — **Removed**

##### Literals

- `erfpacht uitgegeven` — **Removed**
- `overige zakelijk rechten verkregen` — **Removed**
- `recht van opstal verleend` — **Removed**
- `derden (niet zijnde gemeente` — **Removed**
- `erfpacht verkregen` — **Removed**
- `gedeeltelijk eigendom` — **Removed**
- `onbekend/handmatig oplossen` — **Removed**
- `overige zakelijk rechten verleend` — **Removed**
- `recht van opstal verkregen` — **Removed**
- `vol eigendom` — **Removed**

#### codeExploitant — **Added**

##### Literals

- `erfpacht uitgegeven` — **Added**
- `overige zakelijk rechten verkregen` — **Added**
- `recht van opstal verleend` — **Added**
- `derden (niet zijnde gemeente` — **Added**
- `erfpacht verkregen` — **Added**
- `gedeeltelijk eigendom` — **Added**
- `onbekend/handmatig oplossen` — **Added**
- `overige zakelijk rechten verleend` — **Added**
- `recht van opstal verkregen` — **Added**
- `vol eigendom` — **Added**

#### functieOndersteunendWegdeel — **Removed**

##### Literals

- `berm` — **Removed**
- `verkeerseiland` — **Removed**

#### functieOndersteunendWegdeel — **Added**

##### Literals

- `berm` — **Added**
- `verkeerseiland` — **Added**

#### functieOndersteunendWegdeelPlus — **Removed**

#### functieWeg — **Added**

##### Literals

- `OV-baan` — **Added**
- `baan voor vliegverkeer` — **Added**
- `fietspad` — **Added**
- `inrit` — **Added**
- `overweg` — **Added**
- `parkeervlak` — **Added**
- `rijbaan autosnelweg` — **Added**
- `rijbaan autoweg` — **Added**
- `rijbaan lokale weg` — **Added**
- `rijbaan regionale weg` — **Added**
- `ruiterpad` — **Added**
- `spoorbaan` — **Added**
- `voetgangersgebied` — **Added**
- `voetpad` — **Added**
- `voetpad op trap` — **Added**
- `woonerf` — **Added**

#### functieWeg — **Removed**

##### Literals

- `OV-baan` — **Removed**
- `baan voor vliegverkeer` — **Removed**
- `fietspad` — **Removed**
- `inrit` — **Removed**
- `overweg` — **Removed**
- `parkeervlak` — **Removed**
- `rijbaan autosnelweg` — **Removed**
- `rijbaan autoweg` — **Removed**
- `rijbaan lokale weg` — **Removed**
- `rijbaan regionale weg` — **Removed**
- `ruiterpad` — **Removed**
- `spoorbaan` — **Removed**
- `voetgangersgebied` — **Removed**
- `voetpad` — **Removed**
- `voetpad op trap` — **Removed**
- `woonerf` — **Removed**

#### functieWegPlus — **Removed**

##### Literals

- `calamiteitendoorstee` — **Removed**
- `verbindingsweg` — **Removed**
- `verkeersdrempel` — **Removed**

#### functieWegPlus — **Added**

##### Literals

- `calamiteitendoorstee` — **Added**
- `verbindingsweg` — **Added**
- `verkeersdrempel` — **Added**

#### fysiekVoorkomenBegroeidTerrein — **Removed**

##### Literals

- `boomteelt` — **Removed**
- `bouwland` — **Removed**
- `duin` — **Removed**
- `fruitteelt` — **Removed**
- `gemengd bos` — **Removed**
- `grasland agrarisch` — **Removed**
- `grasland overig` — **Removed**
- `groenvoorziening` — **Removed**
- `heide` — **Removed**
- `houtwal` — **Removed**
- `kwelder` — **Removed**
- `loofbos` — **Removed**
- `moeras` — **Removed**
- `naaldbos` — **Removed**
- `rietland` — **Removed**
- `struiken` — **Removed**

#### fysiekVoorkomenBegroeidTerrein — **Added**

##### Literals

- `boomteelt` — **Added**
- `bouwland` — **Added**
- `duin` — **Added**
- `fruitteelt` — **Added**
- `gemengd bos` — **Added**
- `grasland agrarisch` — **Added**
- `grasland overig` — **Added**
- `groenvoorziening` — **Added**
- `heide` — **Added**
- `houtwal` — **Added**
- `kwelder` — **Added**
- `loofbos` — **Added**
- `moeras` — **Added**
- `naaldbos` — **Added**
- `rietland` — **Added**
- `struiken` — **Added**

#### fysiekVoorkomenBegroeidTerreinPlus — **Added**

##### Literals

- `akkerbouw` — **Added**
- `bodembedekkers` — **Added**
- `bollenteelt` — **Added**
- `bosplantsoen` — **Added**
- `braakliggend` — **Added**
- `gesloten duinvegetatie` — **Added**
- `gras en kruidachtigen` — **Added**
- `grien en hakhout` — **Added**
- `heesters` — **Added**
- `hoogstam boomgaarden` — **Added**
- `klein fruit` — **Added**
- `laagstam boomgaarden` — **Added**
- `open duinvegetatie` — **Added**
- `planten` — **Added**
- `struikrozen` — **Added**
- `vollegrondsteelt` — **Added**
- `wijngaarden` — **Added**

#### fysiekVoorkomenBegroeidTerreinPlus — **Removed**

##### Literals

- `akkerbouw` — **Removed**
- `bodembedekkers` — **Removed**
- `bollenteelt` — **Removed**
- `bosplantsoen` — **Removed**
- `braakliggend` — **Removed**
- `gesloten duinvegetatie` — **Removed**
- `gras en kruidachtigen` — **Removed**
- `grien en hakhout` — **Removed**
- `heesters` — **Removed**
- `hoogstam boomgaarden` — **Removed**
- `klein fruit` — **Removed**
- `laagstam boomgaarden` — **Removed**
- `open duinvegetatie` — **Removed**
- `planten` — **Removed**
- `struikrozen` — **Removed**
- `vollegrondsteelt` — **Removed**
- `wijngaarden` — **Removed**

#### fysiekVoorkomenOnbegroeidTerrein — **Added**

##### Literals

- `Gesloten verharding` — **Added**
- `erf` — **Added**
- `half verhard` — **Added**
- `onverhard` — **Added**
- `open verharding` — **Added**
- `zand` — **Added**

#### fysiekVoorkomenOnbegroeidTerrein — **Removed**

##### Literals

- `Gesloten verharding` — **Removed**
- `erf` — **Removed**
- `half verhard` — **Removed**
- `onverhard` — **Removed**
- `open verharding` — **Removed**
- `zand` — **Removed**

#### fysiekVoorkomenOnbegroeidTerreinPlus — **Removed**

##### Literals

- `asfalt` — **Removed**
- `betonelement` — **Removed**
- `betonstraatstenen` — **Removed**
- `boomschors` — **Removed**
- `cementbeton` — **Removed**
- `gebakken klinkers` — **Removed**
- `grasklinkers` — **Removed**
- `gravel` — **Removed**
- `grind` — **Removed**
- `kunststof` — **Removed**
- `puin` — **Removed**
- `schelpen` — **Removed**
- `sierbestrating` — **Removed**
- `strand en strandwal` — **Removed**
- `tegels` — **Removed**
- `zand` — **Removed**
- `zandverstuiving` — **Removed**

#### fysiekVoorkomenOnbegroeidTerreinPlus — **Added**

##### Literals

- `asfalt` — **Added**
- `betonelement` — **Added**
- `betonstraatstenen` — **Added**
- `boomschors` — **Added**
- `cementbeton` — **Added**
- `gebakken klinkers` — **Added**
- `grasklinkers` — **Added**
- `gravel` — **Added**
- `grind` — **Added**
- `kunststof` — **Added**
- `puin` — **Added**
- `schelpen` — **Added**
- `sierbestrating` — **Added**
- `strand en strandwal` — **Added**
- `tegels` — **Added**
- `zand` — **Added**
- `zandverstuiving` — **Added**

#### fysiekVoorkomenOndersteunendWegdeel — **Removed**

##### Literals

- `gesloten verharding` — **Removed**
- `groenvoorziening` — **Removed**
- `half verhard` — **Removed**
- `onverhard` — **Removed**

#### fysiekVoorkomenOndersteunendWegdeel — **Added**

##### Literals

- `gesloten verharding` — **Added**
- `groenvoorziening` — **Added**
- `half verhard` — **Added**
- `onverhard` — **Added**

#### fysiekVoorkomenOndersteunendWegdeelPlus — **Removed**

##### Literals

- `puin` — **Removed**
- `asfalt` — **Removed**
- `beton element` — **Removed**
- `betonstraatstenen` — **Removed**
- `bodembedekkers` — **Removed**
- `boomschors` — **Removed**
- `bosplantsoen` — **Removed**
- `cementbeton` — **Removed**
- `gebakken klinkers` — **Removed**
- `gras- en kruidachtigen` — **Removed**
- `grasklinkers` — **Removed**
- `gravel` — **Removed**
- `grind` — **Removed**
- `heesters` — **Removed**
- `planten` — **Removed**
- `schelpen` — **Removed**
- `sierbestrating` — **Removed**
- `struikrozen` — **Removed**
- `tegels` — **Removed**
- `zand` — **Removed**

#### fysiekVoorkomenOndersteunendWegdeelPlus — **Added**

##### Literals

- `puin` — **Added**
- `asfalt` — **Added**
- `beton element` — **Added**
- `betonstraatstenen` — **Added**
- `bodembedekkers` — **Added**
- `boomschors` — **Added**
- `bosplantsoen` — **Added**
- `cementbeton` — **Added**
- `gebakken klinkers` — **Added**
- `gras- en kruidachtigen` — **Added**
- `grasklinkers` — **Added**
- `gravel` — **Added**
- `grind` — **Added**
- `heesters` — **Added**
- `planten` — **Added**
- `schelpen` — **Added**
- `sierbestrating` — **Added**
- `struikrozen` — **Added**
- `tegels` — **Added**
- `zand` — **Added**

#### fysiekVoorkomenWeg — **Removed**

##### Literals

- `gesloten verharding` — **Removed**
- `half verhard` — **Removed**
- `onverhard` — **Removed**
- `open verharding` — **Removed**

#### fysiekVoorkomenWeg — **Added**

##### Literals

- `gesloten verharding` — **Added**
- `half verhard` — **Added**
- `onverhard` — **Added**
- `open verharding` — **Added**

#### fysiekVoorkomenWegPlus — **Removed**

##### Literals

- `asfalt` — **Removed**
- `beton element` — **Removed**
- `betonstraatstenen` — **Removed**
- `boomschors` — **Removed**
- `cementbeton` — **Removed**
- `gebakken klinkers` — **Removed**
- `grasklinkers` — **Removed**
- `gravel` — **Removed**
- `grind` — **Removed**
- `puin` — **Removed**
- `schelpen` — **Removed**
- `sierbestrating` — **Removed**
- `tegels` — **Removed**
- `zand` — **Removed**

#### fysiekVoorkomenWegPlus — **Added**

##### Literals

- `asfalt` — **Added**
- `beton element` — **Added**
- `betonstraatstenen` — **Added**
- `boomschors` — **Added**
- `cementbeton` — **Added**
- `gebakken klinkers` — **Added**
- `grasklinkers` — **Added**
- `gravel` — **Added**
- `grind` — **Added**
- `puin` — **Added**
- `schelpen` — **Added**
- `sierbestrating` — **Added**
- `tegels` — **Added**
- `zand` — **Added**

#### gebruiksdoel — **Removed**

##### Literals

- `Leeg` — **Removed**
- `Onbekend` — **Removed**
- `bijeenkomstfunctie` — **Removed**
- `celfunctie` — **Removed**
- `gezondheidszorgfunctie` — **Removed**
- `industriefunctie` — **Removed**
- `kantoorfunctie` — **Removed**
- `logiesfunctie` — **Removed**
- `onderwijsfunctie` — **Removed**
- `overige gebruiksfunctie` — **Removed**
- `sportfunctie` — **Removed**
- `winkelfunctie` — **Removed**
- `woonfunctie` — **Removed**

#### gebruiksdoel — **Added**

##### Literals

- `Leeg` — **Added**
- `Onbekend` — **Added**
- `bijeenkomstfunctie` — **Added**
- `celfunctie` — **Added**
- `gezondheidszorgfunctie` — **Added**
- `industriefunctie` — **Added**
- `kantoorfunctie` — **Added**
- `logiesfunctie` — **Added**
- `onderwijsfunctie` — **Added**
- `overige gebruiksfunctie` — **Added**
- `sportfunctie` — **Added**
- `winkelfunctie` — **Added**
- `woonfunctie` — **Added**

#### geslacht — **Removed**

##### Literals

- `Leeg` — **Removed**
- `Man` — **Removed**
- `Onbekend` — **Removed**
- `Vrouw` — **Removed**

#### soortGebruik — **Removed**

##### Literals

- `terrein` — **Removed**
- `boerderij` — **Removed**
- `niet-woning` — **Removed**
- `niet-woning deels in gebruik als woning` — **Removed**
- `recreatiewoning en overige woningen` — **Removed**
- `sluimerend WOZ-object` — **Removed**
- `uitgezonderd gebouwd object` — **Removed**
- `uitgezonderd ongebouwd object` — **Removed**
- `woning dienend tot hoofdverblijf` — **Removed**
- `woning met praktijkruimte` — **Removed**

#### soortGebruik — **Added**

##### Literals

- `terrein` — **Added**
- `boerderij` — **Added**
- `niet-woning` — **Added**
- `niet-woning deels in gebruik als woning` — **Added**
- `recreatiewoning en overige woningen` — **Added**
- `sluimerend WOZ-object` — **Added**
- `uitgezonderd gebouwd object` — **Added**
- `uitgezonderd ongebouwd object` — **Added**
- `woning dienend tot hoofdverblijf` — **Added**
- `woning met praktijkruimte` — **Added**

#### soortRechtsvorm — **Removed**

##### Literals

- `Besloten vennootschap` — **Removed**
- `Europese Cooperatieve Vennootschap` — **Removed**
- `Europese Naamloze Vennootschap` — **Removed**
- `Leeg` — **Removed**
- `Onbekend` — **Removed**
- `commanditaire vennootschap` — **Removed**
- `cooperatie, Europees Economische Samenwerking` — **Removed**
- `kapitaalvennootschap binnen EER` — **Removed**
- `kapitaalvennootschap buiten EER` — **Removed**
- `kerkelijke Organisatie` — **Removed**
- `maatschap` — **Removed**
- `naamloze Vennootschap` — **Removed**
- `onderlinge Waarborg Maatschappij` — **Removed**
- `overig privaatrechtelijke rechtspersoon` — **Removed**
- `overige buitenlandse rechtspersoon vennootschap` — **Removed**
- `publiekrechtelijke Rechtspersoon` — **Removed**
- `rederij` — **Removed**
- `stichting` — **Removed**
- `vennootschap onder Firma` — **Removed**
- `vereniging` — **Removed**
- `vereniging van Eigenaars` — **Removed**

#### soortRechtsvorm — **Added**

##### Literals

- `Besloten vennootschap` — **Added**
- `Europese Cooperatieve Vennootschap` — **Added**
- `Europese Naamloze Vennootschap` — **Added**
- `Leeg` — **Added**
- `Onbekend` — **Added**
- `commanditaire vennootschap` — **Added**
- `cooperatie, Europees Economische Samenwerking` — **Added**
- `kapitaalvennootschap binnen EER` — **Added**
- `kapitaalvennootschap buiten EER` — **Added**
- `kerkelijke Organisatie` — **Added**
- `maatschap` — **Added**
- `naamloze Vennootschap` — **Added**
- `onderlinge Waarborg Maatschappij` — **Added**
- `overig privaatrechtelijke rechtspersoon` — **Added**
- `overige buitenlandse rechtspersoon vennootschap` — **Added**
- `publiekrechtelijke Rechtspersoon` — **Added**
- `rederij` — **Added**
- `stichting` — **Added**
- `vennootschap onder Firma` — **Added**
- `vereniging` — **Added**
- `vereniging van Eigenaars` — **Added**

#### soortRechtsvorm — **Removed**

##### Literals

- `Besloten vennootschap` — **Removed**
- `Europese Cooperatieve Vennootschap` — **Removed**
- `Europese Naamloze Vennootschap` — **Removed**
- `Leeg` — **Removed**
- `Onbekend` — **Removed**
- `commanditaire vennootschap` — **Removed**
- `cooperatie, Europees Economische Samenwerking` — **Removed**
- `kapitaalvennootschap binnen EER` — **Removed**
- `kapitaalvennootschap buiten EER` — **Removed**
- `kerkelijke Organisatie` — **Removed**
- `maatschap` — **Removed**
- `naamloze Vennootschap` — **Removed**
- `onderlinge Waarborg Maatschappij` — **Removed**
- `overig privaatrechtelijke rechtspersoon` — **Removed**
- `overige buitenlandse rechtspersoon vennootschap` — **Removed**
- `publiekrechtelijke Rechtspersoon` — **Removed**
- `rederij` — **Removed**
- `stichting` — **Removed**
- `vennootschap onder Firma` — **Removed**
- `vereniging` — **Removed**
- `vereniging van Eigenaars` — **Removed**

#### soortRechtsvorm — **Added**

##### Literals

- `Besloten vennootschap` — **Added**
- `Europese Cooperatieve Vennootschap` — **Added**
- `Europese Naamloze Vennootschap` — **Added**
- `Leeg` — **Added**
- `Onbekend` — **Added**
- `commanditaire vennootschap` — **Added**
- `cooperatie, Europees Economische Samenwerking` — **Added**
- `kapitaalvennootschap binnen EER` — **Added**
- `kapitaalvennootschap buiten EER` — **Added**
- `kerkelijke Organisatie` — **Added**
- `maatschap` — **Added**
- `naamloze Vennootschap` — **Added**
- `onderlinge Waarborg Maatschappij` — **Added**
- `overig privaatrechtelijke rechtspersoon` — **Added**
- `overige buitenlandse rechtspersoon vennootschap` — **Added**
- `publiekrechtelijke Rechtspersoon` — **Added**
- `rederij` — **Added**
- `stichting` — **Added**
- `vennootschap onder Firma` — **Added**
- `vereniging` — **Added**
- `vereniging van Eigenaars` — **Added**

#### statusGeoObject — **Removed**

##### Literals

- `bestaand` — **Removed**
- `historie` — **Removed**
- `plan` — **Removed**

#### statusGeoObject — **Removed**

##### Literals

- `bestaand` — **Removed**
- `historie` — **Removed**
- `plan` — **Removed**

#### statusGeoObject — **Removed**

##### Literals

- `bestaand` — **Removed**
- `historie` — **Removed**
- `plan` — **Removed**

#### statusGeoObject — **Added**

##### Literals

- `bestaand` — **Added**
- `historie` — **Added**
- `plan` — **Added**

#### statusGeoObject — **Added**

##### Literals

- `bestaand` — **Added**
- `historie` — **Added**
- `plan` — **Added**

#### statusGeoObject — **Removed**

##### Literals

- `bestaand` — **Removed**
- `historie` — **Removed**
- `plan` — **Removed**

#### statusGeoObject — **Added**

##### Literals

- `bestaand` — **Added**
- `historie` — **Added**
- `plan` — **Added**

#### statusGeoObject — **Removed**

##### Literals

- `bestaand` — **Removed**
- `historie` — **Removed**
- `plan` — **Removed**

#### statusGeoObject — **Removed**

##### Literals

- `bestaand` — **Removed**
- `historie` — **Removed**
- `plan` — **Removed**

#### statusGeoObject — **Added**

##### Literals

- `bestaand` — **Added**
- `historie` — **Added**
- `plan` — **Added**

#### statusGeoObject — **Removed**

##### Literals

- `bestaand` — **Removed**
- `historie` — **Removed**
- `plan` — **Removed**

#### statusGeoObject — **Removed**

##### Literals

- `bestaand` — **Removed**
- `historie` — **Removed**
- `plan` — **Removed**

#### statusGeoObject — **Removed**

##### Literals

- `bestaand` — **Removed**
- `historie` — **Removed**
- `plan` — **Removed**

#### statusGeoObject — **Added**

##### Literals

- `bestaand` — **Added**
- `historie` — **Added**
- `plan` — **Added**

#### statusGeoObject — **Removed**

##### Literals

- `bestaand` — **Removed**
- `historie` — **Removed**
- `plan` — **Removed**

#### statusGeoObject — **Added**

##### Literals

- `bestaand` — **Added**
- `historie` — **Added**
- `plan` — **Added**

#### statusGeoObject — **Removed**

##### Literals

- `bestaand` — **Removed**
- `historie` — **Removed**
- `plan` — **Removed**

#### statusGeoObject — **Removed**

##### Literals

- `bestaand` — **Removed**
- `historie` — **Removed**
- `plan` — **Removed**

#### statusGeoObject — **Added**

##### Literals

- `bestaand` — **Added**
- `historie` — **Added**
- `plan` — **Added**

#### statusGeoObject — **Removed**

##### Literals

- `bestaand` — **Removed**
- `historie` — **Removed**
- `plan` — **Removed**

#### statusGeoObject — **Added**

##### Literals

- `bestaand` — **Added**
- `historie` — **Added**
- `plan` — **Added**

#### statusGeoObject — **Removed**

##### Literals

- `bestaand` — **Removed**
- `historie` — **Removed**
- `plan` — **Removed**

#### statusGeoObject — **Added**

##### Literals

- `bestaand` — **Added**
- `historie` — **Added**
- `plan` — **Added**

#### statusGeoObject — **Removed**

##### Literals

- `bestaand` — **Removed**
- `historie` — **Removed**
- `plan` — **Removed**

#### statusGeoObject — **Added**

##### Literals

- `bestaand` — **Added**
- `historie` — **Added**
- `plan` — **Added**

#### statusGeoObject — **Added**

##### Literals

- `bestaand` — **Added**
- `historie` — **Added**
- `plan` — **Added**

#### statusGeoObject — **Added**

##### Literals

- `bestaand` — **Added**
- `historie` — **Added**
- `plan` — **Added**

#### statusGeoObject — **Added**

##### Literals

- `bestaand` — **Added**
- `historie` — **Added**
- `plan` — **Added**

#### statusGeoObject — **Removed**

##### Literals

- `bestaand` — **Removed**
- `historie` — **Removed**
- `plan` — **Removed**

#### statusGeoObject — **Removed**

##### Literals

- `bestaand` — **Removed**
- `historie` — **Removed**
- `plan` — **Removed**

#### statusGeoObject — **Added**

##### Literals

- `bestaand` — **Added**
- `historie` — **Added**
- `plan` — **Added**

#### statusGeoObject — **Added**

##### Literals

- `bestaand` — **Added**
- `historie` — **Added**
- `plan` — **Added**

#### statusGeoObject — **Added**

##### Literals

- `bestaand` — **Added**
- `historie` — **Added**
- `plan` — **Added**

#### statusGeoObject — **Added**

##### Literals

- `bestaand` — **Added**
- `historie` — **Added**
- `plan` — **Added**

#### statusWOZ(Deel)Object — **Added**

##### Literals

- `actief` — **Added**
- `beëindigd` — **Added**
- `gevormd, niet actief` — **Added**
- `ten onrechte opgevoerd` — **Added**

#### statusWOZ(Deel)Object — **Removed**

##### Literals

- `actief` — **Removed**
- `beëindigd` — **Removed**
- `gevormd, niet actief` — **Removed**
- `ten onrechte opgevoerd` — **Removed**

#### statusWOZ(Deel)Object — **Added**

##### Literals

- `actief` — **Added**
- `beëindigd` — **Added**
- `gevormd, niet actief` — **Added**
- `ten onrechte opgevoerd` — **Added**

#### statusWOZ(Deel)Object — **Removed**

##### Literals

- `actief` — **Removed**
- `beëindigd` — **Removed**
- `gevormd, niet actief` — **Removed**
- `ten onrechte opgevoerd` — **Removed**

#### statusWOZ-Beschikking — **Added**

##### Literals

- `uitspraak hoger beroep, vastgestelde waarde veranderd` — **Added**
- `vernietiging beschikking` — **Added**
- `arrest Hoge Raad, beschikking gehandhaafd` — **Added**
- `arrest Hoge Raad, geding verwezen` — **Added**
- `arrest Hoge Raad, vastgestelde waarde veranderd` — **Added**
- `beroep aangetekend` — **Added**
- `beschikking genomen` — **Added**
- `bezwaar afgehandeld, beschikking gehandhaafd` — **Added**
- `bezwaar afgehandeld, vastgestelde waarde veranderd` — **Added**
- `bezwaar ingediend` — **Added**
- `cassatie ingesteld` — **Added**
- `herzieningsbeschikking` — **Added**
- `hoger beroep aangetekend` — **Added**
- `uitspraak beroep, beschikking gehandhaafd` — **Added**
- `uitspraak beroep, vastgestelde waarde veranderd` — **Added**
- `uitspraak hoger beroep, beschikking gehandhaafd` — **Added**
- `waarde ambtshalve verminderd` — **Added**
- `waarde te gebruiken voor voorlopige aanslag` — **Added**

#### statusWOZ-Beschikking — **Removed**

##### Literals

- `uitspraak hoger beroep, vastgestelde waarde veranderd` — **Removed**
- `vernietiging beschikking` — **Removed**
- `arrest Hoge Raad, beschikking gehandhaafd` — **Removed**
- `arrest Hoge Raad, geding verwezen` — **Removed**
- `arrest Hoge Raad, vastgestelde waarde veranderd` — **Removed**
- `beroep aangetekend` — **Removed**
- `beschikking genomen` — **Removed**
- `bezwaar afgehandeld, beschikking gehandhaafd` — **Removed**
- `bezwaar afgehandeld, vastgestelde waarde veranderd` — **Removed**
- `bezwaar ingediend` — **Removed**
- `cassatie ingesteld` — **Removed**
- `herzieningsbeschikking` — **Removed**
- `hoger beroep aangetekend` — **Removed**
- `uitspraak beroep, beschikking gehandhaafd` — **Removed**
- `uitspraak beroep, vastgestelde waarde veranderd` — **Removed**
- `uitspraak hoger beroep, beschikking gehandhaafd` — **Removed**
- `waarde ambtshalve verminderd` — **Removed**
- `waarde te gebruiken voor voorlopige aanslag` — **Removed**

#### typeOverbrugging — **Removed**

##### Literals

- `aquaduct` — **Removed**
- `brug` — **Removed**
- `ecoduct` — **Removed**
- `fly-over` — **Removed**
- `viaduct` — **Removed**

#### typeOverbrugging — **Added**

##### Literals

- `aquaduct` — **Added**
- `brug` — **Added**
- `ecoduct` — **Added**
- `fly-over` — **Added**
- `viaduct` — **Added**

#### typeringAppartementsrechtsplitsing — **Added**

##### Literals

- `Leeg` — **Added**
- `Onbekend` — **Added**
- `hoofdsplitsing` — **Added**
- `ondersplitsing` — **Added**
- `splitsingafkooperfpacht` — **Added**

#### typeringGebouwinstallatie — **Removed**

##### Literals

- `bordes` — **Removed**
- `luifel` — **Removed**
- `toegangstrap` — **Removed**

#### typeringGebouwinstallatie — **Added**

##### Literals

- `bordes` — **Added**
- `luifel` — **Added**
- `toegangstrap` — **Added**

#### typeringInrichtingselement — **Removed**

##### Literals

- `bak` — **Removed**
- `bord` — **Removed**
- `installatie` — **Removed**
- `kast` — **Removed**
- `mast` — **Removed**
- `paal` — **Removed**
- `put` — **Removed**
- `sensor` — **Removed**
- `straatmeubilair` — **Removed**
- `waterinrichtingselement` — **Removed**
- `weginrichtingselement` — **Removed**

#### typeringInrichtingselement — **Added**

##### Literals

- `bak` — **Added**
- `bord` — **Added**
- `installatie` — **Added**
- `kast` — **Added**
- `mast` — **Added**
- `paal` — **Added**
- `put` — **Added**
- `sensor` — **Added**
- `straatmeubilair` — **Added**
- `waterinrichtingselement` — **Added**
- `weginrichtingselement` — **Added**

#### typeringInrichtingselementPlus — **Added**

##### Literals

- `CAI-kast` — **Added**
- `GMS kast` — **Added**
- `GMS sensor` — **Added**
- `abri` — **Added**
- `afsluitpaal` — **Added**
- `afval aparte plaats` — **Added**
- `afvalbak` — **Added**
- `balustrade` — **Added**
- `bank` — **Added**
- `benzine- / olieput` — **Added**
- `betaalautomaat` — **Added**
- `betonning` — **Added**
- `bloembak` — **Added**
- `bolder` — **Added**
- `boomspiegel` — **Added**
- `bovenleidingmast` — **Added**
- `brandkraan / -put` — **Added**
- `brievenbus` — **Added**
- `camera` — **Added**
- `container` — **Added**
- `debietmeter` — **Added**
- `detectielus` — **Added**
- `dijkpaal` — **Added**
- `drainageput` — **Added**
- `drinkbak` — **Added**
- `drukknoppaal` — **Added**
- `dynamische snelheidsindicator` — **Added**
- `elektrakast` — **Added**
- `fietsenkluis` — **Added**
- `fietsenrek` — **Added**
- `flitser` — **Added**
- `fontein` — **Added**
- `gaskast` — **Added**
- `gasput` — **Added**
- `geleideconstructie` — **Added**
- `geleidewerk` — **Added**
- `grensmarkering` — **Added**
- `haltepaal` — **Added**
- `hectometerpaal` — **Added**
- `herdenkingsmonument` — **Added**
- `hoogtedetectieapparaat` — **Added**
- `hoogtemerk` — **Added**
- `informatiebord` — **Added**
- `inspectie- / rioolput` — **Added**
- `kolk` — **Added**
- `kunstobject` — **Added**
- `laagspanningsmast` — **Added**
- `lichtcel` — **Added**
- `lichtmast` — **Added**
- `lichtpunt` — **Added**
- `lijnafwatering` — **Added**
- `meerpaal` — **Added**
- `molgoot` — **Added**
- `openbaar toilet` — **Added**
- `openbare verlichtingskast` — **Added**
- `parkeerbeugel` — **Added**
- `picknicktafel` — **Added**
- `plaatsnaambord` — **Added**
- `poller` — **Added**
- `pomp` — **Added**
- `portaal` — **Added**
- `praatpaal` — **Added**
- `radar detector` — **Added**
- `radarmast` — **Added**
- `reclamebord` — **Added**
- `reclamezuil` — **Added**
- `remmingswerk` — **Added**
- `rioolkast` — **Added**
- `scheepvaartbord` — **Added**
- `sirene` — **Added**
- `slagboom` — **Added**
- `speelvoorziening` — **Added**
- `straalzender` — **Added**
- `straatnaambord` — **Added**
- `telecom kast` — **Added**
- `telefooncel` — **Added**
- `telkast` — **Added**
- `telpaal` — **Added**
- `verblindingswering` — **Added**
- `verkeersbord` — **Added**
- `verkeersbordpaal` — **Added**
- `verkeersregelinstallatiekast` — **Added**
- `verkeersregelinstallatiepaal` — **Added**
- `verklikker transportleiding` — **Added**
- `vlaggenmast` — **Added**
- `vuilvang` — **Added**
- `waarschuwingshek` — **Added**
- `waterleidingput` — **Added**
- `waterstandmeter` — **Added**
- `weerstation` — **Added**
- `wegmarkering` — **Added**
- `wegwijzer` — **Added**
- `wildrooster` — **Added**
- `windmeter` — **Added**
- `zand- / zoutbak` — **Added**
- `zendmast` — **Added**
- `zonnepaneel` — **Added**

#### typeringInrichtingselementPlus — **Removed**

##### Literals

- `CAI-kast` — **Removed**
- `GMS kast` — **Removed**
- `GMS sensor` — **Removed**
- `abri` — **Removed**
- `afsluitpaal` — **Removed**
- `afval aparte plaats` — **Removed**
- `afvalbak` — **Removed**
- `balustrade` — **Removed**
- `bank` — **Removed**
- `benzine- / olieput` — **Removed**
- `betaalautomaat` — **Removed**
- `betonning` — **Removed**
- `bloembak` — **Removed**
- `bolder` — **Removed**
- `boomspiegel` — **Removed**
- `bovenleidingmast` — **Removed**
- `brandkraan / -put` — **Removed**
- `brievenbus` — **Removed**
- `camera` — **Removed**
- `container` — **Removed**
- `debietmeter` — **Removed**
- `detectielus` — **Removed**
- `dijkpaal` — **Removed**
- `drainageput` — **Removed**
- `drinkbak` — **Removed**
- `drukknoppaal` — **Removed**
- `dynamische snelheidsindicator` — **Removed**
- `elektrakast` — **Removed**
- `fietsenkluis` — **Removed**
- `fietsenrek` — **Removed**
- `flitser` — **Removed**
- `fontein` — **Removed**
- `gaskast` — **Removed**
- `gasput` — **Removed**
- `geleideconstructie` — **Removed**
- `geleidewerk` — **Removed**
- `grensmarkering` — **Removed**
- `haltepaal` — **Removed**
- `hectometerpaal` — **Removed**
- `herdenkingsmonument` — **Removed**
- `hoogtedetectieapparaat` — **Removed**
- `hoogtemerk` — **Removed**
- `informatiebord` — **Removed**
- `inspectie- / rioolput` — **Removed**
- `kolk` — **Removed**
- `kunstobject` — **Removed**
- `laagspanningsmast` — **Removed**
- `lichtcel` — **Removed**
- `lichtmast` — **Removed**
- `lichtpunt` — **Removed**
- `lijnafwatering` — **Removed**
- `meerpaal` — **Removed**
- `molgoot` — **Removed**
- `openbaar toilet` — **Removed**
- `openbare verlichtingskast` — **Removed**
- `parkeerbeugel` — **Removed**
- `picknicktafel` — **Removed**
- `plaatsnaambord` — **Removed**
- `poller` — **Removed**
- `pomp` — **Removed**
- `portaal` — **Removed**
- `praatpaal` — **Removed**
- `radar detector` — **Removed**
- `radarmast` — **Removed**
- `reclamebord` — **Removed**
- `reclamezuil` — **Removed**
- `remmingswerk` — **Removed**
- `rioolkast` — **Removed**
- `scheepvaartbord` — **Removed**
- `sirene` — **Removed**
- `slagboom` — **Removed**
- `speelvoorziening` — **Removed**
- `straalzender` — **Removed**
- `straatnaambord` — **Removed**
- `telecom kast` — **Removed**
- `telefooncel` — **Removed**
- `telkast` — **Removed**
- `telpaal` — **Removed**
- `verblindingswering` — **Removed**
- `verkeersbord` — **Removed**
- `verkeersbordpaal` — **Removed**
- `verkeersregelinstallatiekast` — **Removed**
- `verkeersregelinstallatiepaal` — **Removed**
- `verklikker transportleiding` — **Removed**
- `vlaggenmast` — **Removed**
- `vuilvang` — **Removed**
- `waarschuwingshek` — **Removed**
- `waterleidingput` — **Removed**
- `waterstandmeter` — **Removed**
- `weerstation` — **Removed**
- `wegmarkering` — **Removed**
- `wegwijzer` — **Removed**
- `wildrooster` — **Removed**
- `windmeter` — **Removed**
- `zand- / zoutbak` — **Removed**
- `zendmast` — **Removed**
- `zonnepaneel` — **Removed**

#### typeringOndersteunendWater — **Removed**

##### Literals

- `oever, slootkant` — **Removed**
- `slik` — **Removed**

#### typeringOndersteunendWater — **Added**

##### Literals

- `oever, slootkant` — **Added**
- `slik` — **Added**

#### typeringOndersteunendWaterPlus — **Removed**

#### typeringOverbruggingsdeel — **Removed**

##### Literals

- `dek` — **Removed**
- `landhoofd` — **Removed**
- `pijler` — **Removed**
- `pyloon` — **Removed**
- `sloof` — **Removed**

#### typeringOverbruggingsdeel — **Added**

##### Literals

- `dek` — **Added**
- `landhoofd` — **Added**
- `pijler` — **Added**
- `pyloon` — **Added**
- `sloof` — **Added**

#### typeringOverigeScheiding — **Removed**

##### Literals

- `draadraster` — **Removed**
- `faunaraster` — **Removed**

#### typeringOverigeScheiding — **Added**

##### Literals

- `draadraster` — **Added**
- `faunaraster` — **Added**

#### typeringVegetatieobject — **Added**

##### Literals

- `boom` — **Added**
- `haag` — **Added**

#### typeringVegetatieobject — **Removed**

##### Literals

- `boom` — **Removed**
- `haag` — **Removed**

#### typeringWater — **Removed**

##### Literals

- `greppel, droge sloot` — **Removed**
- `waterloop` — **Removed**
- `watervlakte` — **Removed**
- `zee` — **Removed**

#### typeringWater — **Added**

##### Literals

- `greppel, droge sloot` — **Added**
- `waterloop` — **Added**
- `watervlakte` — **Added**
- `zee` — **Added**

#### typeringWaterPlus — **Removed**

##### Literals

- `beek` — **Removed**
- `bron` — **Removed**
- `gracht` — **Removed**
- `haven` — **Removed**
- `kanaal` — **Removed**
- `meer, plas, ven, vijver` — **Removed**
- `rivier` — **Removed**
- `sloot` — **Removed**

#### typeringWaterPlus — **Added**

##### Literals

- `beek` — **Added**
- `bron` — **Added**
- `gracht` — **Added**
- `haven` — **Added**
- `kanaal` — **Added**
- `meer, plas, ven, vijver` — **Added**
- `rivier` — **Added**
- `sloot` — **Added**

#### typeringZekerheidsrecht — **Added**

##### Literals

- `beslag` — **Added**
- `recht van hypotheek` — **Added**

#### typeringZekerheidsrecht — **Removed**

##### Literals

- `beslag` — **Removed**
- `recht van hypotheek` — **Removed**

## Package: Model Leerplicht en Leerlingenvervoer

### Classes

#### Procesverbaal Onderwijs — **Unchanged**

##### Attributes

- geldboeteVoorwaardelijk — **Changed**
  - **enumeration_id**: `Enumeratie: Boolean` → `Enumeratie: Boolean`

#### Vrijstelling — **Unchanged**

##### Attributes

- aanvraagToegekend — **Changed**
  - **enumeration_id**: `Enumeratie: Boolean` → `Enumeratie: Boolean`

_No datatype changes in this package._

### Enumerations

#### Boolean — **Removed**

##### Literals

- `Ja` — **Removed**
- `Leeg` — **Removed**
- `Nee` — **Removed**
- `Onbekend` — **Removed**

#### Boolean — **Added**

##### Literals

- `Ja` — **Added**
- `Leeg` — **Added**
- `Nee` — **Added**
- `Onbekend` — **Added**

#### Boolean — **Added**

##### Literals

- `Ja` — **Added**
- `Leeg` — **Added**
- `Nee` — **Added**
- `Onbekend` — **Added**

#### Boolean — **Removed**

##### Literals

- `Ja` — **Removed**
- `Leeg` — **Removed**
- `Nee` — **Removed**
- `Onbekend` — **Removed**

## Package: Model Onderwijs

### Classes

#### Leerling — **Unchanged**

##### Attributes

- kwetsbareJongere — **Changed**
  - **enumeration_id**: `Enumeratie: Boolean` → `Enumeratie: Boolean`

#### Uitschrijving — **Unchanged**

##### Attributes

- diplomaBehaald — **Changed**
  - **enumeration_id**: `Enumeratie: Boolean` → `Enumeratie: Boolean`

_No datatype changes in this package._

### Enumerations

#### Boolean — **Added**

##### Literals

- `Ja` — **Added**
- `Leeg` — **Added**
- `Nee` — **Added**
- `Onbekend` — **Added**

#### Boolean — **Removed**

##### Literals

- `Ja` — **Removed**
- `Leeg` — **Removed**
- `Nee` — **Removed**
- `Onbekend` — **Removed**

#### Boolean — **Removed**

##### Literals

- `Ja` — **Removed**
- `Leeg` — **Removed**
- `Nee` — **Removed**
- `Onbekend` — **Removed**

#### Boolean — **Added**

##### Literals

- `Ja` — **Added**
- `Leeg` — **Added**
- `Nee` — **Added**
- `Onbekend` — **Added**

## Package: Model Parkeren

### Classes

#### Parkeerscan — **Unchanged**

##### Attributes

- coordinaten — **Changed**
  - **primitive**: `GML` → `Point`

#### Parkeervlak — **Unchanged**

##### Attributes

- coordinaten — **Changed**
  - **primitive**: `GML` → `Point`

#### Parkeerzone — **Unchanged**

##### Attributes

- geometrie — **Changed**
  - **primitive**: `Multivlak` → `MultiSurface`
- isParkeergarage — **Changed**
  - **enumeration_id**: `Enumeratie: Boolean` → `Enumeratie: Boolean`

_No datatype changes in this package._

### Enumerations

#### Boolean — **Added**

##### Literals

- `Ja` — **Added**
- `Leeg` — **Added**
- `Nee` — **Added**
- `Onbekend` — **Added**

#### Boolean — **Removed**

##### Literals

- `Ja` — **Removed**
- `Leeg` — **Removed**
- `Nee` — **Removed**
- `Onbekend` — **Removed**

## Package: Model Schuldhulpverlening

### Classes

#### Begeleiding — **Unchanged**

##### Attributes

- soort — **Changed**
  - **stereotype**: `` → `enum`

#### Begeleidingssoort — **Unchanged**

##### Attributes

- soort — **Changed**
  - **stereotype**: `` → `enum`
  - **primitive**: `BegeleidingsoortEnum` → `EnumBegeleidingssoort`
  - **enumeration_id**: `` → `Enumeratie: EnumBegeleidingssoort`

#### Oplossing — **Unchanged**

##### Attributes

- soort — **Changed**
  - **stereotype**: `` → `enum`

#### Oplossingssoort — **Unchanged**

##### Attributes

- soort — **Changed**
  - **stereotype**: `` → `enum`
  - **primitive**: `SchuldregelingsoortEnum` → `EnumSchuldensoort`
  - **enumeration_id**: `` → `Enumeratie: EnumSchuldensoort`

_No datatype changes in this package._

_No enumeration changes in this package._

## Package: Model Sociaal Domein Generiek

### Classes

#### Incident — **Unchanged**

##### Attributes

- locatie — **Changed**
  - **primitive**: `Locatie` → `Point`
- soort — **Changed**
  - **primitive**: `Incidenttype` → `enum_Incidenttype`
  - **enumeration_id**: `` → `Enumeratie: enum_Incidenttype`

#### Relatiesoort — **Unchanged**

##### Attributes

- Omschrijving — **Added**

#### Sociale Groep — **Unchanged**

##### Attributes

- typering — **Changed**
  - **primitive**: `Groep` → `Text`

#### Sociale Relatie — **Unchanged**

##### Attributes

- typering — **Changed**
  - **primitive**: `Relatie` → `text`

_No datatype changes in this package._

### Enumerations

#### enum_Incidenttype — **Added**

## Package: Model Sport

### Classes

#### Binnenlocatie — **Unchanged**

##### Attributes

- locatie — **Changed**
  - **primitive**: `GML` → `Point`

_No datatype changes in this package._

_No enumeration changes in this package._

## Package: Model Terug- en invordering

### Classes

#### Vorderingscomponent — **Unchanged**

##### Attributes

- Priotype — **Changed**
  - **name**: `Vorderingscomponent.Id` → `Priotype`
  - **primitive**: `RedenKwijtscheldingVordering` → `Verwerkingsstatus`
  - **enumeration_id**: `Enumeratie: Verwerkingsstatus` → `Enumeratie: Verwerkingsstatus`
  - **type_class_id**: `Objecttype: EAID_63ede881_e81f_4445_9e93_7180d30a2390` → ``

_No datatype changes in this package._

### Enumerations

#### Verwerkingsstatus — **Removed**

#### Verwerkingsstatus — **Added**

## Package: Model VTH

### Classes

#### Inspectie — **Unchanged**

##### Attributes


#### Kosten — **Unchanged**

##### Attributes


#### Leges_Grondslag — **Unchanged**

##### Attributes


#### MORAanvraagOfMelding — **Unchanged**

##### Attributes

- CROW — **Changed**
  - **enumeration_id**: `Enumeratie: Boolean` → `Enumeratie: Boolean`

#### VOMAanvraagOfMelding — **Unchanged**

##### Attributes

- locatie — **Changed**
  - **primitive**: `GML` → `Point`

#### VTH-Melding — **Unchanged**

##### Attributes

- locatie — **Changed**
  - **primitive**: `GML` → `Point`

#### VTHzaak — **Unchanged**

##### Attributes

- verkamering — **Changed**
  - **enumeration_id**: `Enumeratie: Boolean` → `Enumeratie: Boolean`

#### Vordering — **Unchanged**

##### Attributes


_No datatype changes in this package._

### Enumerations

#### Boolean — **Added**

##### Literals

- `Ja` — **Added**
- `Leeg` — **Added**
- `Nee` — **Added**
- `Onbekend` — **Added**

#### Boolean — **Added**

##### Literals

- `Ja` — **Added**
- `Leeg` — **Added**
- `Nee` — **Added**
- `Onbekend` — **Added**

#### Boolean — **Removed**

##### Literals

- `Ja` — **Removed**
- `Leeg` — **Removed**
- `Nee` — **Removed**
- `Onbekend` — **Removed**

#### Boolean — **Removed**

##### Literals

- `Ja` — **Removed**
- `Leeg` — **Removed**
- `Nee` — **Removed**
- `Onbekend` — **Removed**

## Package: Model Vastgoed

### Classes

#### Adresaanduiding — **Unchanged**

##### Attributes

- adres — **Changed**
  - **name**: `adresaanduiding` → `adres`

#### Gebruiksdoel — **Unchanged**

##### Attributes

- gebruiksdoelGebouwdObject — **Changed**
  - **enumeration_id**: `Enumeratie: gebruiksdoel` → `Enumeratie: gebruiksdoel`

#### LocatieaanduidingWozObject — **Unchanged**

##### Attributes

- primair — **Changed**
  - **enumeration_id**: `Enumeratie: Boolean` → `Enumeratie: Boolean`

#### Locatieonroerendezaak — **Unchanged**

##### Attributes

- geometrie — **Changed**
  - **primitive**: `Vlak` → `Surface`

#### Vastgoedobject — **Unchanged**

##### Attributes

- afgekochteErfpacht — **Changed**
  - **primitive**: `` → `Boolean`
  - **enumeration_id**: `` → `Enumeratie: Boolean`
- asbestrapportageAanwezig — **Changed**
  - **enumeration_id**: `Enumeratie: Boolean` → `Enumeratie: Boolean`
- gearchiveerd — **Changed**
  - **enumeration_id**: `Enumeratie: Boolean` → `Enumeratie: Boolean`

#### WOZ-Belang — **Unchanged**

##### Attributes

- eigenaarGebruiker — **Changed**
  - **enumeration_id**: `Enumeratie: aanduidingEigenaarGebruiker` → `Enumeratie: aanduidingEigenaarGebruiker`

_No datatype changes in this package._

### Enumerations

#### Boolean — **Added**

##### Literals

- `Ja` — **Added**
- `Leeg` — **Added**
- `Nee` — **Added**
- `Onbekend` — **Added**

#### Boolean — **Removed**

##### Literals

- `Ja` — **Removed**
- `Leeg` — **Removed**
- `Nee` — **Removed**
- `Onbekend` — **Removed**

#### Boolean — **Removed**

##### Literals

- `Ja` — **Removed**
- `Leeg` — **Removed**
- `Nee` — **Removed**
- `Onbekend` — **Removed**

#### Boolean — **Added**

##### Literals

- `Ja` — **Added**
- `Leeg` — **Added**
- `Nee` — **Added**
- `Onbekend` — **Added**

#### Boolean — **Added**

##### Literals

- `Ja` — **Added**
- `Leeg` — **Added**
- `Nee` — **Added**
- `Onbekend` — **Added**

#### Boolean — **Added**

##### Literals

- `Ja` — **Added**
- `Leeg` — **Added**
- `Nee` — **Added**
- `Onbekend` — **Added**

#### Boolean — **Removed**

##### Literals

- `Ja` — **Removed**
- `Leeg` — **Removed**
- `Nee` — **Removed**
- `Onbekend` — **Removed**

#### aanduidingEigenaarGebruiker — **Added**

##### Literals

- `Leeg` — **Added**
- `Onbekend` — **Added**
- `eigenaar` — **Added**
- `eigenaar-gebruiker` — **Added**
- `gebruiker` — **Added**
- `medebelanghebbende` — **Added**

#### aanduidingEigenaarGebruiker — **Removed**

##### Literals

- `Leeg` — **Removed**
- `Onbekend` — **Removed**
- `eigenaar` — **Removed**
- `eigenaar-gebruiker` — **Removed**
- `gebruiker` — **Removed**
- `medebelanghebbende` — **Removed**

#### gebruiksdoel — **Removed**

##### Literals

- `Leeg` — **Removed**
- `Onbekend` — **Removed**
- `bijeenkomstfunctie` — **Removed**
- `celfunctie` — **Removed**
- `gezondheidszorgfunctie` — **Removed**
- `industriefunctie` — **Removed**
- `kantoorfunctie` — **Removed**
- `logiesfunctie` — **Removed**
- `onderwijsfunctie` — **Removed**
- `overige gebruiksfunctie` — **Removed**
- `sportfunctie` — **Removed**
- `winkelfunctie` — **Removed**
- `woonfunctie` — **Removed**

#### gebruiksdoel — **Added**

##### Literals

- `Leeg` — **Added**
- `Onbekend` — **Added**
- `bijeenkomstfunctie` — **Added**
- `celfunctie` — **Added**
- `gezondheidszorgfunctie` — **Added**
- `industriefunctie` — **Added**
- `kantoorfunctie` — **Added**
- `logiesfunctie` — **Added**
- `onderwijsfunctie` — **Added**
- `overige gebruiksfunctie` — **Added**
- `sportfunctie` — **Added**
- `winkelfunctie` — **Added**
- `woonfunctie` — **Added**

## Package: Model Vermogen

### Classes

#### Bankrekening — **Unchanged**

##### Attributes

- Bankrekening ID — **Removed**
- Voorkeur bankrekening — **Changed**
  - **primitive**: `StdIndJN` → `Boolean`

#### Hypotheek — **Unchanged**

##### Attributes

- Overwaarde — **Changed**
  - **primitive**: `Geldbedrag` → `Bedrag`

#### Motorvoertuig — **Unchanged**

##### Attributes

- Soort motorvoertuig — **Changed**
  - **enumeration_id**: `` → `Enumeratie: CdSrtVoertuig`
  - **type_class_id**: `Objecttype: EAID_04EB2E57_05B5_0E41_7859_273ED24D9EDF` → ``

#### Onroerend goed — **Unchanged**

##### Attributes

- Overwaarde — **Changed**
  - **primitive**: `Geldbedrag` → `Bedrag`

#### Vermogenscomponent — **Unchanged**

##### Attributes

- Code soort vermogenscomponent — **Changed**
  - **enumeration_id**: `` → `Enumeratie: CdSrtVermogenscomponent`
  - **type_class_id**: `Objecttype: EAID_051FB82B_E809_143E_3F7B_273ED24D1E2E` → ``
- Nog aan te spreken vermogen — **Changed**
  - **primitive**: `Geldbedrag` → `Bedrag`
- Vrij te laten vermogen — **Changed**
  - **primitive**: `Geldbedrag` → `Bedrag`
- identificatie — **Changed**
  - **name**: `Vermogenscomponent ID` → `identificatie`

#### Waardepeiling — **Unchanged**

##### Attributes

- Bijgevoegd bewijs — **Changed**
  - **primitive**: `StdIndJN` → `Boolean`
- Waarde vermogenscomponent — **Changed**
  - **primitive**: `Geldbedrag` → `Bedrag`
- WaardeSoort vermogenscomponent — **Changed**
  - **enumeration_id**: `` → `Enumeratie: CdSrtWaardeVermogenscomponent`
  - **type_class_id**: `Objecttype: EAID_1721EBD6_A6E2_CEC4_6AB8_27DB661BCC09` → ``

_No datatype changes in this package._

### Enumerations

#### CdSrtVermogenscomponent — **Added**

#### CdSrtVoertuig — **Added**

#### CdSrtWaardeVermogenscomponent — **Added**

## Package: Model Vroegsignalering

_No class changes in this package._

_No datatype changes in this package._

### Enumerations

#### EnumContactsoort — **Changed**

##### Literals

- `Administratief` — **Added**
- `Afspraak op locatie` — **Added**
- `Overige` — **Removed**

#### EnumEindresultaat — **Changed**

##### Literals

- `Definitief geen contact kunnen krijgen` — **Added**
- `Geen reactie na eerder contact` — **Added**
- `Inwoner heeft zelf al betaald/betalingsregeling getroffen` — **Added**
- `Inwoner hoeft geen hulp vanuit vroegsignalering` — **Added**
- `Inwoner is overleden` — **Added**
- `Niet opgepakt: andere reden` — **Added**
- `Niet opgepakt: herhaalde melding` — **Added**
- `Niet opgepakt: onterecht signaal` — **Added**
- `Persoon is geen inwoner (meer) in de gemeente` — **Added**
- `Vervolghulp en/of verwijzing financieel` — **Added**
- `Vervolghulp en/of verwijzing niet financieel` — **Added**
- `Verwijzing zonder contact` — **Added**
- `Geen contact (meer) kunnen krijgen` — **Removed**
- `Inwoner heeft betaald/betalingsregeling getroffen voor oppakken melding` — **Removed**
- `Inwoner heeft zelf betaald/betalingsregeling getroffen na oppakken melding` — **Removed**
- `Inwoner probeert het zelf op te lossen` — **Removed**
- `Inwoner wil geen hulp` — **Removed**
- `Niet opgepakt` — **Removed**
- `Niet opgepakt: BRP-uitsluiting` — **Removed**
- `Niet opgepakt: geen capaciteit` — **Removed**
- `Niet opgepakt: inwoner wil geen contact` — **Removed**
- `Verwijzing financieel` — **Removed**
- `Verwijzing niet-financieel` — **Removed**
- `Voorzien van informatie` — **Removed**

#### EnumSignaalstatus — **Changed**

##### Literals

- `Inwoner is overleden` — **Added**
- `Niet opgepakt: andere reden` — **Added**
- `Niet opgepakt: herhaalde melding` — **Added**
- `Niet opgepakt: onterecht signaal` — **Added**
- `Persoon is geen inwoner (meer) in de gemeente` — **Added**
- `Herhaalde melding` — **Removed**
- `Niet opgepakt` — **Removed**
- `Onterecht signaal` — **Removed**
- `Opgepakt` — **Removed**
- `Overleden` — **Removed**
- `Woont niet in gemeente` — **Removed**
- `Woont op een ander adres binnen gemeente` — **Removed**

## Package: Model Werk

### Classes

#### BeschikbaarVoorArbeid — **Unchanged**

##### Attributes

- DagBeschikbaarheid — **Changed**
  - **primitive**: `beschikbaarheid` → `Dag beschikbaarheid`
  - **enumeration_id**: `` → `Enumeratie: Dag beschikbaarheid`

#### Flexibliteit — **Unchanged**

##### Attributes

- IndicatieBereidBuitenBeroepswens — **Changed**
  - **name**: `IndicatieBereidheidZoekenBuitenBeroepswens` → `IndicatieBereidBuitenBeroepswens`

#### Mobiliteit — **Unchanged**

##### Attributes

- CodeVervoermiddel — **Changed**
  - **primitive**: `Vervoersmogelijkheden` → `Vervoermiddel`
  - **enumeration_id**: `` → `Enumeratie: Vervoermiddel`

#### Ontheffing — **Unchanged**

##### Attributes

- MotivatieOntheffingsbesluit — **Changed**
  - **primitive**: `document` → `Document`
  - **type_class_id**: `` → `Objecttype: Document`
- OntheffenVerplichtingen — **Changed**
  - **primitive**: `Ontheffingsverplichting` → `Ontheffingsverplichting
`
  - **enumeration_id**: `` → `Enumeratie: Ontheffingsverplichting
`
- Ontheffingsbesluit — **Changed**
  - **primitive**: `document` → `Document`
  - **type_class_id**: `` → `Objecttype: Document`

#### Opleiding — **Unchanged**

##### Attributes

- CodeStatusOpleiding — **Changed**
  - **primitive**: `StatusOpleiding` → `CodeStatusOpleiding`
  - **enumeration_id**: `` → `Enumeratie: CodeStatusOpleiding`
- CodeTijdsBeslagOpleiding — **Changed**
  - **primitive**: `opleiding` → `Code tijdsbeslag opleiding
`
  - **enumeration_id**: `` → `Enumeratie: Code tijdsbeslag opleiding
`
- Instituutnaam — **Changed**
  - **primitive**: `short` → `Text`
- Opleidingstype — **Changed**
  - **stereotype**: `` → `enum`
  - **primitive**: `Opleidingstype` → `Opleidingsrichting`
  - **enumeration_id**: `` → `Enumeratie: Opleidingsrichting`

#### Opleidingsnaam — **Unchanged**

##### Attributes

- naamOpleiding — **Changed**
  - **name**: `Opleidingsnaam` → `naamOpleiding`

#### OpleidingsnaamOngecodeerd — **Unchanged**

##### Attributes

- naamOpleidingOngecodeerd — **Changed**
  - **name**: `OpleidingsnaamOngecodeerd` → `naamOpleidingOngecodeerd`

#### Opleidingsniveau — **Unchanged**

##### Attributes

- CodeOpleidingsniveauClient — **Changed**
  - **primitive**: `cliënt` → `Code opleidingsniveau cliënt
`
  - **enumeration_id**: `` → `Enumeratie: Code opleidingsniveau cliënt
`

#### Rijbewijs /Certificaat — **Unchanged**

##### Attributes

- CodeSoortRijbewijs — **Changed**
  - **primitive**: `` → `AN12`
- NummerCertificaat — **Changed**
  - **primitive**: `RegEx` → `varchar`

#### Taalbeheersing — **Unchanged**

##### Attributes

- Taalcode — **Changed**
  - **primitive**: `ìnt` → `varchar`

#### Vaardigheidsvaststelling — **Unchanged**

##### Attributes

- Indicatie mate van vaardigheid — **Changed**
  - **primitive**: `vaardigheid` → `Taalvaardigheid
`
  - **enumeration_id**: `` → `Enumeratie: Taalvaardigheid
`
- datumLaatsteVaststelling — **Changed**
  - **name**: `Datum laatste vaststelling van vaardigheid` → `datumLaatsteVaststelling`

#### Voorkeur — **Unchanged**

##### Attributes

- SoortWerk — **Changed**
  - **primitive**: `enum` → `SoortWerk`
  - **enumeration_id**: `` → `Enumeratie: SoortWerk`

#### Werkzaamheden anders dan in arbeidsverhouding — **Unchanged**

##### Attributes

- PersoonOrganisatieWaarbij — **Changed**
  - **name**: `Naam persoon of organisatie bij wie of waar` → `PersoonOrganisatieWaarbij`
- aantalUrenGemiddeldWeek — **Changed**
  - **name**: `Aantal uren werkzaamheden gemiddeld per week` → `aantalUrenGemiddeldWeek`

#### ZelfredzaamheidScore — **Unchanged**

##### Attributes

- Domein van Zelfredzaamheid — **Changed**
  - **primitive**: `zelfredzaamheid` → `Domein van zelfredzaamheid
`
  - **enumeration_id**: `` → `Enumeratie: Domein van zelfredzaamheid
`
- KenmerkBeoordelaar — **Changed**
  - **primitive**: `Name` → `AN200`

_No datatype changes in this package._

_No enumeration changes in this package._

## Package: Model Wonen

### Classes

#### Gebouw — **Unchanged**

##### Attributes

- energielabel — **Changed**
  - **enumeration_id**: `Enumeratie: Energielabel` → `Enumeratie: Energielabel`
- oppervlakte — **Changed**
  - **enumeration_id**: `Enumeratie: Oppervlakte Woning` → `Enumeratie: Oppervlakte Woning`

_No datatype changes in this package._

### Enumerations

#### Energielabel — **Removed**

##### Literals

- `A` — **Removed**
- `B` — **Removed**
- `C` — **Removed**
- `D` — **Removed**
- `E` — **Removed**
- `F` — **Removed**

#### Energielabel — **Added**

##### Literals

- `A` — **Added**
- `B` — **Added**
- `C` — **Added**
- `D` — **Added**
- `E` — **Added**
- `F` — **Added**

#### Oppervlakte Woning — **Added**

##### Literals

- `100 - 124 m2` — **Added**
- `125 - 149 m2` — **Added**
- `15 - 49 m2` — **Added**
- `150 en groter` — **Added**
- `50 - 74 m2` — **Added**
- `75 - 99 m2` — **Added**
- `kleiner dan 15 m2` — **Added**

#### Oppervlakte Woning — **Removed**

##### Literals

- `100 - 124 m2` — **Removed**
- `125 - 149 m2` — **Removed**
- `15 - 49 m2` — **Removed**
- `150 en groter` — **Removed**
- `50 - 74 m2` — **Removed**
- `75 - 99 m2` — **Removed**
- `kleiner dan 15 m2` — **Removed**

## Package: Referentielijsten

### Classes

#### AardAantekening — **Unchanged**

##### Attributes

- naamAardAantekening — **Changed**
  - **primitive**: `AN` → `AN255`

#### AardFiliatie — **Unchanged**

##### Attributes

- naamAardFiliatie — **Changed**
  - **primitive**: `AN` → `AN255`

#### AardZakelijkRecht — **Unchanged**

##### Attributes

- naamAardZakelijkRecht — **Changed**
  - **primitive**: `AN` → `AN255`

#### AkrKadastraleGemeentecode — **Unchanged**

##### Attributes

- AKRCode — **Changed**
  - **primitive**: `AN` → `AN255`

#### AutoriteitAfgifteNederlandsReisdocument — **Unchanged**

##### Attributes

- omschrijving — **Changed**
  - **primitive**: `AN` → `AN255`

#### CultuurcodeBebouwd — **Unchanged**

##### Attributes

- code — **Changed**
  - **name**: `cultuurcodeBebouwd` → `code`
- naamCultuurcodeBebouwd — **Changed**
  - **primitive**: `AN` → `AN255`

#### CultuurcodeOnbebouwd — **Unchanged**

##### Attributes

- code — **Changed**
  - **name**: `cultuurcodeOnbebouwd` → `code`
- naamCultuurcodeOnbebouwd — **Changed**
  - **primitive**: `AN` → `AN255`

#### Partij — **Unchanged**

##### Attributes

- verstrekkingsbeperkingMogelijk — **Changed**
  - **primitive**: `INDIC` → ``

#### SoortGrootte — **Unchanged**

##### Attributes

- naamSoortGrootte — **Changed**
  - **primitive**: `AN` → `AN255`

#### SoortWOZObject — **Unchanged**

##### Attributes

- naamSoortObjectcode — **Changed**
  - **primitive**: `AN` → `AN255`
- opmerkingenSoortObjectcode — **Changed**
  - **primitive**: `AN` → `AN255`

#### Valutasoort — **Unchanged**

##### Attributes

- naamValuta — **Changed**
  - **primitive**: `AN` → `AN255`

#### WOZ-Deelobjectcode — **Unchanged**

##### Attributes

- naamDeelobjectcode — **Changed**
  - **primitive**: `AN` → `AN255`

_No datatype changes in this package._

_No enumeration changes in this package._
