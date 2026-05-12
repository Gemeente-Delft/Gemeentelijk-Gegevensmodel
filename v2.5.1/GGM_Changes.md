# Changes from v2.5.0 to v2.5.1

## Summary

- **Classes**: +0 / -0 / ~0
- **Datatypes**: +0 / -0 / ~0
- **Enumerations**: +133 / -131 / ~223
- **Attributes**: +0 / -0 / ~137
- **Literals**: +939 / -930

## Overview

**Packages touched:** `Complex datatype`, `Groepattribuutsoort`, `Model BAG`, `Model Dienstverlening`, `Model Inburgering`, `Model Inkomen`, `Model Inkomsten`, `Model Kern RGBZ`, `Model Kern RSGB`, `Model Kern RSGB`, `Model Leerplicht en Leerlingenvervoer`, `Model Onderwijs`, `Model Parkeren`, `Model Sociaal Domein Generiek`, `Model Terug- en invordering`, `Model VTH`, `Model Vastgoed`, `Model Vermogen`, `Model Wonen`


## Top-down changes

## Package: Complex datatype

_No class changes in this package._

_No datatype changes in this package._

### Enumerations

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

## Package: Groepattribuutsoort

### Classes

#### MigratieIngeschrevenNatuurlijkPersoon — **Unchanged**

##### Attributes

- aangeverMigratie — **Changed**
  - **enumeration_id**: `Enumeratie: aangever` → `Enumeratie: aangever`
- redenWijzigingMigratie — **Changed**
  - **enumeration_id**: `Enumeratie: redenWijzigingAdres` → `Enumeratie: redenWijzigingAdres`
- soortMigratie — **Changed**
  - **enumeration_id**: `Enumeratie: soortMigratie` → `Enumeratie: soortMigratie`

#### NaamgebruikNatuurlijkPersoon — **Unchanged**

##### Attributes

- adellijkeTitelNaamgebruik — **Changed**
  - **enumeration_id**: `Enumeratie: adelijkeTitel` → `Enumeratie: adelijkeTitel`

#### OntbindingHuwelijk/geregistreerdPartnerschap — **Unchanged**

##### Attributes

- redenEinde — **Changed**
  - **enumeration_id**: `Enumeratie: redenEindeRelatie` → `Enumeratie: redenEindeRelatie`

#### SamengesteldeNaamNatuurlijkPersoon — **Unchanged**

##### Attributes

- adellijkeTitel — **Changed**
  - **enumeration_id**: `Enumeratie: adelijkeTitel` → `Enumeratie: adelijkeTitel`
- predicaat — **Changed**
  - **enumeration_id**: `Enumeratie: predicaat` → `Enumeratie: predicaat`

#### SoortFunctioneelGebied — **Unchanged**

##### Attributes

- typeFunctioneelGebied — **Changed**
  - **enumeration_id**: `Enumeratie: typeringFunctioneelGebied` → `Enumeratie: typeringFunctioneelGebied`

#### SoortKunstwerk — **Unchanged**

##### Attributes

- typeKunstwerk — **Changed**
  - **enumeration_id**: `Enumeratie: typeringKunstwerk` → `Enumeratie: typeringKunstwerk`

#### SoortOverigBouwwerk — **Unchanged**

##### Attributes

- typeOverigBouwwerk — **Changed**
  - **enumeration_id**: `Enumeratie: typeringOverigBouwwerk` → `Enumeratie: typeringOverigBouwwerk`

#### SoortScheiding — **Unchanged**

##### Attributes

- typeScheiding — **Changed**
  - **enumeration_id**: `Enumeratie: typeringScheiding` → `Enumeratie: typeringScheiding`

#### SoortSpoor — **Unchanged**

##### Attributes

- functieSpoor — **Changed**
  - **enumeration_id**: `Enumeratie: functieSpoor` → `Enumeratie: functieSpoor`

_No datatype changes in this package._

### Enumerations

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

#### functieSpoor — **Removed**

##### Literals

- `(haven)kraan` — **Removed**
- `sneltram` — **Removed**
- `tram` — **Removed**
- `trein` — **Removed**

#### functieSpoor — **Added**

##### Literals

- `(haven)kraan` — **Added**
- `sneltram` — **Added**
- `tram` — **Added**
- `trein` — **Added**

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

#### soortMigratie — **Removed**

##### Literals

- `Emigratie` — **Removed**
- `Immigratie` — **Removed**

#### soortMigratie — **Added**

##### Literals

- `Emigratie` — **Added**
- `Immigratie` — **Added**

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

## Package: Model BAG

### Classes

#### Standplaats — **Unchanged**

##### Attributes

- beginGeldigheid — **Changed**
  - **name**: `Datum Begin Geldigheid` → `beginGeldigheid`
- datumEinde — **Changed**
  - **name**: `Datum Einde` → `datumEinde`
- datumIngang — **Changed**
  - **name**: `Datum Ingang` → `datumIngang`
- eindGeldigheid — **Changed**
  - **name**: `Datum Einde Geldigheid` → `eindGeldigheid`

_No datatype changes in this package._

### Enumerations

#### statusVerblijfsobject — **Changed**

##### Literals

- `verblijfsobject verbouwing` — **Added**

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

## Package: Model Inburgering

### Classes

#### Asielstatushouder — **Unchanged**

##### Attributes

- DigiD aangevraagd — **Changed**
  - **enumeration_id**: `Enumeratie: Boolean` → `Enumeratie: Boolean`
- Rijbewijs — **Changed**
  - **enumeration_id**: `Enumeratie: Boolean` → `Enumeratie: Boolean`

#### Educatie — **Unchanged**

##### Attributes

- Opleiding — **Changed**
  - **enumeration_id**: `Enumeratie: CodeNiveauOpleiding` → `Enumeratie: CodeNiveauOpleiding`

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

#### CodeNiveauOpleiding — **Added**

##### Literals

- `Basisonderwijs` — **Added**
- `HAVO / VWO` — **Added**
- `HBO / Bachelor` — **Added**
- `MBO` — **Added**
- `VMBO / MBO-1` — **Added**
- `WO / Master` — **Added**

#### CodeNiveauOpleiding — **Removed**

##### Literals

- `Basisonderwijs` — **Removed**
- `HAVO / VWO` — **Removed**
- `HBO / Bachelor` — **Removed**
- `MBO` — **Removed**
- `VMBO / MBO-1` — **Removed**
- `WO / Master` — **Removed**

## Package: Model Inkomen

### Classes

#### Inkomensvoorzieningsoort — **Unchanged**

##### Attributes

- wet — **Changed**
  - **enumeration_id**: `Enumeratie: Wet` → `Enumeratie: Wet`

_No datatype changes in this package._

### Enumerations

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

## Package: Model Inkomsten

### Classes

#### Alimentatie — **Unchanged**

##### Attributes

- Inkomstensoort alimentatie — **Changed**
  - **enumeration_id**: `Enumeratie: InkomstensoortAlimentatie` → `Enumeratie: InkomstensoortAlimentatie`

#### Betaald werk — **Unchanged**

##### Attributes

- Inkomstensoort betaald werk — **Changed**
  - **enumeration_id**: `Enumeratie: InkomstensoortBetaaldWerk` → `Enumeratie: InkomstensoortBetaaldWerk`
- Periodiciteit uitbetaling loon — **Changed**
  - **enumeration_id**: `Enumeratie: CdUitkeringsperiode` → `Enumeratie: CdUitkeringsperiode`
- Soort contract — **Changed**
  - **enumeration_id**: `Enumeratie: SoortContract` → `Enumeratie: SoortContract`

#### Inkomstencomponent — **Unchanged**

##### Attributes

- Bruto-Netto — **Changed**
  - **enumeration_id**: `Enumeratie: BrutoNettoInkomsten` → `Enumeratie: BrutoNettoInkomsten`
- Inkomstencomponenttype — **Changed**
  - **enumeration_id**: `Enumeratie: Inkomstencomponenttype` → `Enumeratie: Inkomstencomponenttype`

#### Inkomstenverhouding — **Unchanged**

##### Attributes

- Categorie Inkomsten — **Changed**
  - **enumeration_id**: `Enumeratie: CdSrtInkomstenverhouding` → `Enumeratie: CdSrtInkomstenverhouding`

#### Onderhoudsplicht — **Unchanged**

##### Attributes

- Onderhoudsplichttype — **Changed**
  - **enumeration_id**: `Enumeratie: Onderhoudsplichttype` → `Enumeratie: Onderhoudsplichttype`

#### Pensioen — **Unchanged**

##### Attributes

- Inkomstensoort pensioen — **Changed**
  - **enumeration_id**: `Enumeratie: InkomstensoortPensioen` → `Enumeratie: InkomstensoortPensioen`
- Periodiciteit uitbetaling pensioen — **Changed**
  - **enumeration_id**: `Enumeratie: CdUitkeringsperiode` → `Enumeratie: CdUitkeringsperiode`

#### Stage — **Unchanged**

##### Attributes

- Periodiciteit uitbetaling loon — **Changed**
  - **enumeration_id**: `Enumeratie: CdUitkeringsperiode` → `Enumeratie: CdUitkeringsperiode`

#### Studiefinanciering — **Unchanged**

##### Attributes

- Inkomstensoort studiefinanciering — **Changed**
  - **enumeration_id**: `Enumeratie: InkomstensoortStudiefinanciering` → `Enumeratie: InkomstensoortStudiefinanciering`

#### Uitkering — **Unchanged**

##### Attributes

- Inkomstensoort uitkering — **Changed**
  - **enumeration_id**: `Enumeratie: CdSzWet` → `Enumeratie: CdSzWet`
- Periodiciteit uitbetaling uitkering — **Changed**
  - **enumeration_id**: `Enumeratie: CdUitkeringsperiode` → `Enumeratie: CdUitkeringsperiode`

#### Vrijlating inkomsten — **Unchanged**

##### Attributes

- Doelgroep — **Changed**
  - **enumeration_id**: `Enumeratie: JsonRuledGroupType` → `Enumeratie: JsonRuledGroupType`
- Soort vrijlating — **Changed**
  - **enumeration_id**: `Enumeratie: CodeSoortVrijlating` → `Enumeratie: CodeSoortVrijlating`

_No datatype changes in this package._

### Enumerations

#### BrutoNettoInkomsten — **Added**

#### BrutoNettoInkomsten — **Removed**

#### CdSrtInkomstenverhouding — **Added**

#### CdSrtInkomstenverhouding — **Removed**

#### CdSzWet — **Removed**

#### CdSzWet — **Added**

#### CdUitkeringsperiode — **Removed**

#### CdUitkeringsperiode — **Removed**

#### CdUitkeringsperiode — **Added**

#### CdUitkeringsperiode — **Added**

#### CdUitkeringsperiode — **Removed**

#### CdUitkeringsperiode — **Added**

#### CdUitkeringsperiode — **Added**

#### CdUitkeringsperiode — **Removed**

#### CodeSoortVrijlating — **Added**

#### CodeSoortVrijlating — **Removed**

#### Inkomstencomponenttype — **Removed**

#### Inkomstencomponenttype — **Added**

#### InkomstensoortAlimentatie — **Added**

#### InkomstensoortAlimentatie — **Removed**

#### InkomstensoortBetaaldWerk — **Added**

#### InkomstensoortBetaaldWerk — **Removed**

#### InkomstensoortPensioen — **Removed**

#### InkomstensoortPensioen — **Added**

#### InkomstensoortStudiefinanciering — **Removed**

#### InkomstensoortStudiefinanciering — **Added**

#### JsonRuledGroupType — **Removed**

#### JsonRuledGroupType — **Added**

#### Onderhoudsplichttype — **Added**

#### Onderhoudsplichttype — **Removed**

#### SoortContract — **Removed**

#### SoortContract — **Added**

## Package: Model Kern RGBZ

### Classes

#### Bedrijfsproces — **Unchanged**

##### Attributes

- Afgerond — **Changed**
  - **enumeration_id**: `Enumeratie: Boolean` → `Enumeratie: Boolean`

#### Heffing — **Unchanged**

##### Attributes


#### Klantcontact — **Unchanged**

##### Attributes


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

#### Heffingsoort — **Added**

##### Literals

- `leges` — **Added**
- `precario` — **Added**

#### Heffingsoort — **Removed**

##### Literals

- `leges` — **Removed**
- `precario` — **Removed**

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

#### Appartementsrechtsplitsing — **Unchanged**

##### Attributes

- typeSplitsing — **Changed**
  - **enumeration_id**: `Enumeratie: typeringAppartementsrechtsplitsing` → `Enumeratie: typeringAppartementsrechtsplitsing`

#### BegroeidTerreindeel — **Unchanged**

##### Attributes

- fysiekVoorkomen — **Changed**
  - **enumeration_id**: `Enumeratie: fysiekVoorkomenBegroeidTerrein` → `Enumeratie: fysiekVoorkomenBegroeidTerrein`
- opTalud — **Changed**
  - **primitive**: `boolean` → `Boolean`
  - **enumeration_id**: `` → `Enumeratie: Boolean`
- plusFysiekVoorkomen — **Changed**
  - **enumeration_id**: `Enumeratie: fysiekVoorkomenBegroeidTerreinPlus` → `Enumeratie: fysiekVoorkomenBegroeidTerreinPlus`
- status — **Changed**
  - **enumeration_id**: `Enumeratie: statusGeoObject` → `Enumeratie: statusGeoObject`

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

- plusTypeInrichtingselement — **Changed**
  - **enumeration_id**: `Enumeratie: typeringInrichtingselementPlus` → `Enumeratie: typeringInrichtingselementPlus`
- statusInrichtingselement — **Changed**
  - **enumeration_id**: `Enumeratie: statusGeoObject` → `Enumeratie: statusGeoObject`
- typeInrichtingselement — **Changed**
  - **enumeration_id**: `Enumeratie: typeringInrichtingselement` → `Enumeratie: typeringInrichtingselement`

#### Kunstwerkdeel — **Unchanged**

##### Attributes

- statusKunstwerkdeel — **Changed**
  - **enumeration_id**: `Enumeratie: statusGeoObject` → `Enumeratie: statusGeoObject`

#### NatuurlijkPersoon — **Unchanged**

##### Attributes

- adellijkeTitelOfPredikaat — **Changed**
  - **enumeration_id**: `Enumeratie: adelijkeTitel` → `Enumeratie: adelijkeTitel`

#### NietNatuurlijkPersoon — **Unchanged**

##### Attributes

- rechtsvorm — **Changed**
  - **enumeration_id**: `Enumeratie: soortRechtsvorm` → `Enumeratie: soortRechtsvorm`

#### OnbegroeidTerreindeel — **Unchanged**

##### Attributes

- fysiekVoorkomen — **Changed**
  - **enumeration_id**: `Enumeratie: fysiekVoorkomenOnbegroeidTerrein` → `Enumeratie: fysiekVoorkomenOnbegroeidTerrein`
- onbegroeidTerreindeelOpTalud — **Changed**
  - **primitive**: `boolean` → `Boolean`
  - **enumeration_id**: `` → `Enumeratie: Boolean`
- plusFysiekVoorkomen — **Changed**
  - **enumeration_id**: `Enumeratie: fysiekVoorkomenOnbegroeidTerreinPlus` → `Enumeratie: fysiekVoorkomenOnbegroeidTerreinPlus`
- status — **Changed**
  - **enumeration_id**: `Enumeratie: statusGeoObject` → `Enumeratie: statusGeoObject`

#### OndersteunendWaterdeel — **Unchanged**

##### Attributes

- status — **Changed**
  - **enumeration_id**: `Enumeratie: statusGeoObject` → `Enumeratie: statusGeoObject`
- type — **Changed**
  - **enumeration_id**: `Enumeratie: typeringOndersteunendWater` → `Enumeratie: typeringOndersteunendWater`

#### OndersteunendWegdeel — **Unchanged**

##### Attributes

- functie — **Changed**
  - **enumeration_id**: `Enumeratie: functieOndersteunendWegdeel` → `Enumeratie: functieOndersteunendWegdeel`
- fysiekVoorkomen — **Changed**
  - **enumeration_id**: `Enumeratie: fysiekVoorkomenOndersteunendWegdeel` → `Enumeratie: fysiekVoorkomenOndersteunendWegdeel`
- plusFysiekVoorkomen — **Changed**
  - **enumeration_id**: `Enumeratie: fysiekVoorkomenOndersteunendWegdeelPlus` → `Enumeratie: fysiekVoorkomenOndersteunendWegdeelPlus`
- status — **Changed**
  - **enumeration_id**: `Enumeratie: statusGeoObject` → `Enumeratie: statusGeoObject`

#### Overbruggingsdeel — **Unchanged**

##### Attributes

- hoortBijTypeOverbrugging — **Changed**
  - **enumeration_id**: `Enumeratie: typeOverbrugging` → `Enumeratie: typeOverbrugging`
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

- statusOverigBouwwerk — **Changed**
  - **enumeration_id**: `Enumeratie: statusGeoObject` → `Enumeratie: statusGeoObject`

#### OverigeScheiding — **Unchanged**

##### Attributes

- statusOverigeScheiding — **Changed**
  - **enumeration_id**: `Enumeratie: statusGeoObject` → `Enumeratie: statusGeoObject`
- typeOverigeScheiding — **Changed**
  - **enumeration_id**: `Enumeratie: typeringOverigeScheiding` → `Enumeratie: typeringOverigeScheiding`

#### Reisdocument — **Unchanged**

##### Attributes

- aanduidingInhoudingVermissing — **Changed**
  - **enumeration_id**: `Enumeratie: aanduidingInhoudingVermissingReisdocument` → `Enumeratie: aanduidingInhoudingVermissingReisdocument`

#### Scheiding — **Unchanged**

##### Attributes

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

#### Zekerheidsrecht — **Unchanged**

##### Attributes

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

#### aanduidingInhoudingVermissingReisdocument — **Removed**

##### Literals

- `Ingehouden, ingeleverd` — **Removed**
- `Onbekend` — **Removed**
- `Rechtswege` — **Removed**
- `Vermist` — **Removed**

#### aanduidingInhoudingVermissingReisdocument — **Added**

##### Literals

- `Ingehouden, ingeleverd` — **Added**
- `Onbekend` — **Added**
- `Rechtswege` — **Added**
- `Vermist` — **Added**

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

#### functieOndersteunendWegdeel — **Removed**

##### Literals

- `berm` — **Removed**
- `verkeerseiland` — **Removed**

#### functieOndersteunendWegdeel — **Added**

##### Literals

- `berm` — **Added**
- `verkeerseiland` — **Added**

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

#### fysiekVoorkomenOnbegroeidTerrein — **Removed**

##### Literals

- `Gesloten verharding` — **Removed**
- `erf` — **Removed**
- `half verhard` — **Removed**
- `onverhard` — **Removed**
- `open verharding` — **Removed**
- `zand` — **Removed**

#### fysiekVoorkomenOnbegroeidTerrein — **Added**

##### Literals

- `Gesloten verharding` — **Added**
- `erf` — **Added**
- `half verhard` — **Added**
- `onverhard` — **Added**
- `open verharding` — **Added**
- `zand` — **Added**

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

#### fysiekVoorkomenWeg — **Added**

##### Literals

- `gesloten verharding` — **Added**
- `half verhard` — **Added**
- `onverhard` — **Added**
- `open verharding` — **Added**

#### fysiekVoorkomenWeg — **Removed**

##### Literals

- `gesloten verharding` — **Removed**
- `half verhard` — **Removed**
- `onverhard` — **Removed**
- `open verharding` — **Removed**

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

#### statusWOZ(Deel)Object — **Added**

##### Literals

- `actief` — **Added**
- `beëindigd` — **Added**
- `gevormd, niet actief` — **Added**
- `ten onrechte opgevoerd` — **Added**

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

#### typeOverbrugging — **Added**

##### Literals

- `aquaduct` — **Added**
- `brug` — **Added**
- `ecoduct` — **Added**
- `fly-over` — **Added**
- `viaduct` — **Added**

#### typeOverbrugging — **Removed**

##### Literals

- `aquaduct` — **Removed**
- `brug` — **Removed**
- `ecoduct` — **Removed**
- `fly-over` — **Removed**
- `viaduct` — **Removed**

#### typeringAppartementsrechtsplitsing — **Added**

##### Literals

- `Leeg` — **Added**
- `Onbekend` — **Added**
- `hoofdsplitsing` — **Added**
- `ondersplitsing` — **Added**
- `splitsingafkooperfpacht` — **Added**

#### typeringAppartementsrechtsplitsing — **Removed**

##### Literals

- `Leeg` — **Removed**
- `Onbekend` — **Removed**
- `hoofdsplitsing` — **Removed**
- `ondersplitsing` — **Removed**
- `splitsingafkooperfpacht` — **Removed**

#### typeringGebouwinstallatie — **Added**

##### Literals

- `bordes` — **Added**
- `luifel` — **Added**
- `toegangstrap` — **Added**

#### typeringGebouwinstallatie — **Removed**

##### Literals

- `bordes` — **Removed**
- `luifel` — **Removed**
- `toegangstrap` — **Removed**

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

#### typeringOndersteunendWater — **Added**

##### Literals

- `oever, slootkant` — **Added**
- `slik` — **Added**

#### typeringOndersteunendWater — **Removed**

##### Literals

- `oever, slootkant` — **Removed**
- `slik` — **Removed**

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

#### typeringOverigeScheiding — **Added**

##### Literals

- `draadraster` — **Added**
- `faunaraster` — **Added**

#### typeringOverigeScheiding — **Removed**

##### Literals

- `draadraster` — **Removed**
- `faunaraster` — **Removed**

#### typeringVegetatieobject — **Added**

##### Literals

- `boom` — **Added**
- `haag` — **Added**

#### typeringVegetatieobject — **Removed**

##### Literals

- `boom` — **Removed**
- `haag` — **Removed**

#### typeringWater — **Added**

##### Literals

- `greppel, droge sloot` — **Added**
- `waterloop` — **Added**
- `watervlakte` — **Added**
- `zee` — **Added**

#### typeringWater — **Removed**

##### Literals

- `greppel, droge sloot` — **Removed**
- `waterloop` — **Removed**
- `watervlakte` — **Removed**
- `zee` — **Removed**

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

#### typeringZekerheidsrecht — **Removed**

##### Literals

- `beslag` — **Removed**
- `recht van hypotheek` — **Removed**

#### typeringZekerheidsrecht — **Added**

##### Literals

- `beslag` — **Added**
- `recht van hypotheek` — **Added**

## Package: Model Kern RSGB

### Classes

#### GebouwdObject — **Unchanged**

##### Attributes

- bouwkundigeBestemmingActueel — **Changed**
  - **enumeration_id**: `Enumeratie: bouwkundigeBestemming` → `Enumeratie: bouwkundigeBestemming`
- inwinningOppervlakte — **Changed**
  - **enumeration_id**: `Enumeratie: inwinningsmethodeOppervlakte` → `Enumeratie: inwinningsmethodeOppervlakte`
- statusVoortgangBouw — **Changed**
  - **enumeration_id**: `Enumeratie: statusVoortgangBouw` → `Enumeratie: statusVoortgangBouw`

#### Ligplaats — **Unchanged**

##### Attributes

- ligplaatsstatus — **Changed**
  - **enumeration_id**: `Enumeratie: StatLigplaatsStandplaats` → `Enumeratie: StatLigplaatsStandplaats`

#### Nummeraanduiding — **Unchanged**

##### Attributes

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

- inwinningGeometrieBovenaanzicht — **Changed**
  - **enumeration_id**: `Enumeratie: inwinningsmethodeGeometrie` → `Enumeratie: inwinningsmethodeGeometrie`
- inwinningGeometrieMaaiveld — **Changed**
  - **enumeration_id**: `Enumeratie: inwinningsmethodeGeometrie` → `Enumeratie: inwinningsmethodeGeometrie`
- pandstatus — **Changed**
  - **enumeration_id**: `Enumeratie: statusPand` → `Enumeratie: statusPand`
- statusVoortgangBouw — **Changed**
  - **enumeration_id**: `Enumeratie: statusVoortgangBouw` → `Enumeratie: statusVoortgangBouw`

#### Standplaats — **Unchanged**

##### Attributes

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

#### ontsluitingswijzeVerdieping — **Removed**

##### Literals

- `Leeg` — **Removed**
- `Onbekend` — **Removed**
- `lift` — **Removed**
- `roltrap` — **Removed**
- `trap` — **Removed**

#### ontsluitingswijzeVerdieping — **Added**

##### Literals

- `Leeg` — **Added**
- `Onbekend` — **Added**
- `lift` — **Added**
- `roltrap` — **Added**
- `trap` — **Added**

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

#### statusNummeraanduiding — **Removed**

##### Literals

- `Leeg` — **Removed**
- `Onbekend` — **Removed**
- `naamgeving ingetrokken` — **Removed**
- `naamgeving uitgegeven` — **Removed**

#### statusNummeraanduiding — **Added**

##### Literals

- `Leeg` — **Added**
- `Onbekend` — **Added**
- `naamgeving ingetrokken` — **Added**
- `naamgeving uitgegeven` — **Added**

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

## Package: Model Parkeren

### Classes

#### Parkeerzone — **Unchanged**

##### Attributes

- isParkeergarage — **Changed**
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

## Package: Model Sociaal Domein Generiek

### Classes

#### Incident — **Unchanged**

##### Attributes

- soort — **Changed**
  - **enumeration_id**: `Enumeratie: enum_Incidenttype` → `Enumeratie: enum_Incidenttype`

_No datatype changes in this package._

### Enumerations

#### enum_Incidenttype — **Removed**

#### enum_Incidenttype — **Added**

## Package: Model Terug- en invordering

### Classes

#### Vorderingscomponent — **Unchanged**

##### Attributes

- Priotype — **Changed**
  - **enumeration_id**: `Enumeratie: Verwerkingsstatus` → `Enumeratie: Verwerkingsstatus`

_No datatype changes in this package._

### Enumerations

#### Verwerkingsstatus — **Removed**

#### Verwerkingsstatus — **Added**

## Package: Model VTH

### Classes

#### MORAanvraagOfMelding — **Unchanged**

##### Attributes

- CROW — **Changed**
  - **enumeration_id**: `Enumeratie: Boolean` → `Enumeratie: Boolean`

#### VTHzaak — **Unchanged**

##### Attributes

- verkamering — **Changed**
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

## Package: Model Vastgoed

### Classes

#### Gebruiksdoel — **Unchanged**

##### Attributes

- gebruiksdoelGebouwdObject — **Changed**
  - **enumeration_id**: `Enumeratie: gebruiksdoel` → `Enumeratie: gebruiksdoel`

#### LocatieaanduidingWozObject — **Unchanged**

##### Attributes

- primair — **Changed**
  - **enumeration_id**: `Enumeratie: Boolean` → `Enumeratie: Boolean`

#### Vastgoedobject — **Unchanged**

##### Attributes

- afgekochteErfpacht — **Changed**
  - **enumeration_id**: `Enumeratie: Boolean` → `Enumeratie: Boolean`
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

#### Boolean — **Added**

##### Literals

- `Ja` — **Added**
- `Leeg` — **Added**
- `Nee` — **Added**
- `Onbekend` — **Added**

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

## Package: Model Vermogen

### Classes

#### Motorvoertuig — **Unchanged**

##### Attributes

- Soort motorvoertuig — **Changed**
  - **enumeration_id**: `Enumeratie: CdSrtVoertuig` → `Enumeratie: CdSrtVoertuig`

#### Vermogenscomponent — **Unchanged**

##### Attributes

- Code soort vermogenscomponent — **Changed**
  - **enumeration_id**: `Enumeratie: CdSrtVermogenscomponent` → `Enumeratie: CdSrtVermogenscomponent`

#### Waardepeiling — **Unchanged**

##### Attributes

- WaardeSoort vermogenscomponent — **Changed**
  - **enumeration_id**: `Enumeratie: CdSrtWaardeVermogenscomponent` → `Enumeratie: CdSrtWaardeVermogenscomponent`

_No datatype changes in this package._

### Enumerations

#### CdSrtVermogenscomponent — **Added**

#### CdSrtVermogenscomponent — **Removed**

#### CdSrtVoertuig — **Added**

#### CdSrtVoertuig — **Removed**

#### CdSrtWaardeVermogenscomponent — **Added**

#### CdSrtWaardeVermogenscomponent — **Removed**

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

#### Oppervlakte Woning — **Removed**

##### Literals

- `100 - 124 m2` — **Removed**
- `125 - 149 m2` — **Removed**
- `15 - 49 m2` — **Removed**
- `150 en groter` — **Removed**
- `50 - 74 m2` — **Removed**
- `75 - 99 m2` — **Removed**
- `kleiner dan 15 m2` — **Removed**

#### Oppervlakte Woning — **Added**

##### Literals

- `100 - 124 m2` — **Added**
- `125 - 149 m2` — **Added**
- `15 - 49 m2` — **Added**
- `150 en groter` — **Added**
- `50 - 74 m2` — **Added**
- `75 - 99 m2` — **Added**
- `kleiner dan 15 m2` — **Added**
