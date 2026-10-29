# Vergelijking crunch_uml-import: xmi (EA-XMI) versus qea (.qea)

Database: /private/tmp/claude-501/-Users-arjen-kDrive-Development-GemeentelijkGegevensmodel-v3-0-0/f0d6e72d-b27d-4384-933e-5bb6d6d79f95/scratchpad/vergelijk.db 

## 1. Aantallen per tabel

| Tabel | xmi | qea | alleen xmi | alleen qea | beide |
|---|---|---|---|---|---|
| packages | 296 | 296 | 0 | 0 | 296 |
| classes | 987 | 969 | 24 | 6 | 963 |
| enumerations | 601 | 598 | 213 | 210 | 388 |
| attributes | 5189 | 4542 | 656 | 9 | 4533 |
| enumerationliterals | 6157 | 6138 | 1925 | 1906 | 4232 |
| associations | 1073 | 1083 | 2 | 12 | 1071 |
| generalizations | 304 | 304 | 0 | 0 | 304 |
| diagrams | 243 | 243 | 0 | 0 | 243 |
| diagram_class | 1866 | 1838 | 34 | 6 | 1832 |
| diagram_enumeration | 259 | 259 | 0 | 0 | 259 |
| diagram_association | 1740 | 1746 | 8 | 14 | 1732 |
| diagram_generalization | 447 | 447 | 0 | 0 | 447 |

## 2. Elementen die maar in één bron zitten

**classes, alleen xmi: 24**
  - Proxyconnector (Diagram); DetailleringSubjecten (Semantische relaties); RSGB (View (Zaak)objecten); DetailleringWOZObjecttypen (Semantische relaties); RSGB (View Betrokkene); EAID_47EA6A95_24DD_4ff9_BC2C_1B9BBC08C694 (Tekenwijze); ProxyConnector (Diagram); Vroegsignalering (Diagram) ...

**classes, alleen qea: 6**
  - Gebruikerrol (Model ICT); Belangtype (Model Musea); Historische Rol (Model Erfgoed Generiek); Sport (Model Sport); Rol (Model Musea); Aantal (Model Sport)

**enumerations, alleen xmi: 213**
  - CdRedenAanvraagEindeUitkering (Reden aanvraag); fysiekVoorkomenOnbegroeidTerrein (Model Kern RSGB); Verwerkingsstatus (Model Terug- en invordering); CdRedenAanvraagEindeWerk (Reden aanvraag); CdSzWet (Model Inkomsten); Boolean (Model Kern RGBZ); ontsluitingswijzeVerdieping (Model Kern RSGB); redenWijzigingAdres (Groepattribuutsoort) ...

**enumerations, alleen qea: 210**
  - soortRechtsvorm (Model Kern RSGB); Oppervlakte Woning (Model Wonen); typeringOverbruggingsdeel (Model Kern RSGB); statusWOZ-Beschikking (Model Kern RSGB); StdIndJN (Reden aanvraag); typeringInrichtingselement (Model Kern RSGB); Brontype (Model Diensten); Boolean (Model Dienstverlening) ...

**attributes, alleen xmi: 656**
  - EAID_dst004512_4FFD_40af_B10A_D73656A9E4FE (Vestiging); organisatorische eenheid (Medewerker); EAID_dst00F9CB_3617_4d92_B5F4_5B5C9AF87002 (Dienst); EAID_dst0100B0_3544_4f97_90AF_1CA621FCD924 (Juridische Regel); EAID_dst028461_42B8_4cd3_A3FA_B244697452FA (Schuldhulporganisatie); EAID_dst03A698_1CF8_4bef_8262_FD5C31CD2912 (AdresseerbaarObject); EAID_dst03AA60_7038_4d6e_B5BA_2741116E7008 (Veld); EAID_dst04376C_1AD6_4103_A360_B0C6C7B11452 (Object) ...

**attributes, alleen qea: 9**
  - naam (Rol); aantalMateriaal (Aantal); omschrijving (Belangtype); naam (Sport); naam (Historische Rol); naam (Belangtype); omschrijving (Historische Rol); rol (Gebruikerrol) ...

**enumerationliterals, alleen xmi: 1925**
  - 11 Loon of salaris ambtenaren in de zin van de Ambtenarenwet (CdSrtInkomstenverhouding); kosten in verband met geboorte (CdSrtKostenBijzBijstand); bruto inkomen PTO klant (OnderdeelDienstTypeRubriek); Ja (Boolean); Kwartaal (CdPeriode); gescheiden (burgelijkeStaat); telefonisch (Soorten Klantcontact); Verwijtbare vordering Ioaw (SubCategorieVordering) ...

**enumerationliterals, alleen qea: 1906**
  - recreatie:camping (typeringFunctioneelGebied); taxikosten (CdSrtKostenBijzBijstand); verzorgingstehuis en bejaardentehuis (bouwkundigeBestemming); cassatie ingesteld (statusWOZ-Beschikking); 52 weken (CdPeriode); Remigratiewet (CdSzWet); verbindingsweg (functieWegPlus); terrein (typeringOpenbareRuimte) ...

**associations, alleen xmi: 2**
  - EAID_0CECB460_6E7D_4fbd_A2F6_8163465F555E (ProxyConnector); EAID_8006C819_68B3_41e8_984F_ED0D0C2CBC19 (Proxyconnector)

**associations, alleen qea: 12**
  - gegenereerd door (VLogInfo); betreft (Melding); oefent uit (Sportvereniging); heeft verbinding (Museumobject); rollen (Applicatie); speelt rol in (Historisch Persoon); gegenereerd door (Sensor); heeft (Beheerobject) ...


## 3. Verschillen op gedeelde elementen

Per tabel het aantal gedeelde elementen waarvan een veld verschilt (witruimte genegeerd).

**packages** (296 gedeeld): geen verschillen

**classes** (963 gedeeld):
  - `indicatie_formele_historie`: 40 verschillend; bv. NaamNatuurlijkPersoon: xmi='Ja#NOTES#Description: Indicatie of de formele historie van d…' qea='Ja'
  - `definitie`: 9 verschillend; bv. Linkbaar CMDB-item: xmi='Niet opnemen' qea='CMDB-item dat via een koppeling met andere CMDB-items verbon…'
  - `herkomst`: 7 verschillend; bv. TypeLandinrichtingsrente: xmi='BRK#NOTES#Description: De basisregistratie of het informatie…' qea='BRK'
  - `herkomst_definitie`: 7 verschillend; bv. TypeLandinrichtingsrente: xmi='BRK#NOTES#Description: De basisregistratie of het informatie…' qea='BRK'
  - `datum_opname`: 7 verschillend; bv. TypeLandinrichtingsrente: xmi='1 mei 2016#NOTES#Description: De datum waarop de complex dat…' qea='1 mei 2016'
  - `name`: 2 verschillend; bv. Flexibliteit: xmi='Flexibliteit' qea='Flexibiliteit'

**enumerations** (388 gedeeld):
  - `name`: 7 verschillend; bv. enum_Leefgebied: xmi='enum_Leefgebied' qea='EnumLeefgebied'

**attributes** (4533 gedeeld):
  - `primitive`: 4049 verschillend; bv. datumReservering: xmi='Date' qea='∅'
  - `type_class_id`: 3627 verschillend; bv. datumReservering: xmi='∅' qea='EAID_3E6F5023_BF71_4da0_8747_0B8D334A8D04'
  - `stereotype`: 3149 verschillend; bv. materiaal: xmi='enum' qea='Attribuutsoort'
  - `enumeration_id`: 211 verschillend; bv. soortWoonobject: xmi='EAID_af745015_391d_4cec_8680_3d28e71e4d8f' qea='EAID_be02efcb_fc4e_4198_aa41_0c3525a00f93'
  - `mult_end`: 9 verschillend; bv. gebruiksdoel: xmi='-1' qea='*'
  - `herkomst`: 7 verschillend; bv. datumAanvangVerblijfsrecht: xmi='∅' qea='BRP'
  - `toelichting`: 4 verschillend; bv. datumEindeGeldigheidAutoriteitVanAfgifte: xmi='∅' qea='<memo>'

**enumerationliterals** (4232 gedeeld):
  - `alias`: 779 verschillend; bv. Dagopleiding: xmi='1' qea='∅'
  - `name`: 3 verschillend; bv. Instituuttioneel Huishouden: xmi='Instituuttioneel Huishouden' qea='Institutioneel Huishouden'

**associations** (1071 gedeeld):
  - `stereotype`: 1071 verschillend; bv. is origine van: xmi='∅' qea='Relatiesoort'
  - `src_mult_end`: 576 verschillend; bv. is origine van: xmi='-1' qea='*'
  - `dst_mult_end`: 502 verschillend; bv. bevat: xmi='-1' qea='*'
  - `dst_role`: 32 verschillend; bv. is gehuisvest in: xmi='vestiging' qea='∅'
  - `src_role`: 11 verschillend; bv. heeft: xmi='partner' qea='∅'
  - `src_mult_start`: 6 verschillend; bv. ('EAID_391EB107_6E86_4933_957B_D28543000F46',): xmi='None' qea='∅'
  - `dst_mult_start`: 1 verschillend; bv. ('EAID_391EB107_6E86_4933_957B_D28543000F46',): xmi='None' qea='∅'
  - `dst_class_id`: 1 verschillend; bv. ligt aan: xmi='EAID_FB13857C_C695_4b53_8060_BACFA0E16950' qea='EAID_BFE30E32_8CB9_4272_A559_9FB3FD74DACC'

**generalizations** (304 gedeeld): geen verschillen

**diagrams** (243 gedeeld): geen verschillen


## 4. Vulling van de MIM-metagegevens

Aantal elementen met een waarde per kolom (gedeelde én eigen elementen).

**classes**

| kolom | xmi | qea |
|---|---|---|
| definitie | 948 | 954 |
| toelichting | 219 | 219 |
| herkomst | 324 | 324 |
| herkomst_definitie | 350 | 350 |
| begrip | 211 | 211 |
| datum_opname | 324 | 324 |
| populatie | 84 | 84 |
| kwaliteit | 208 | 208 |
| synoniemen | 26 | 27 |
| indicatie_formele_historie | 40 | 40 |
| stereotype | 965 | 964 |
| alias | 1 | 1 |

**attributes**

| kolom | xmi | qea |
|---|---|---|
| definitie | 1770 | 1770 |
| toelichting | 665 | 669 |
| herkomst | 586 | 593 |
| herkomst_definitie | 571 | 571 |
| datum_opname | 537 | 537 |
| authentiek | 9 | 9 |
| lengte | 34 | 34 |
| patroon | 690 | 690 |
| indicatie_classificerend | 163 | 163 |
| mogelijk_geen_waarde | 5189 | 4542 |
| heeft_tijdlijn_geldigheid | 5189 | 4542 |
| heeft_tijdlijn_registratie | 5189 | 4542 |
| indicatie_formele_historie | 5189 | 4542 |
| indicatie_materiele_historie | 5189 | 4542 |
| indicatie_in_onderzoek | 5189 | 4542 |
| stereotype | 1917 | 4533 |
| mult_start | 5189 | 4542 |
| mult_end | 5178 | 4542 |
| verplicht | 5189 | 4542 |

**associations**

| kolom | xmi | qea |
|---|---|---|
| definitie | 77 | 77 |
| toelichting | 492 | 501 |
| herkomst | 45 | 45 |
| herkomst_definitie | 45 | 45 |
| datum_opname | 45 | 45 |
| authentiek | 114 | 114 |
| mogelijk_geen_waarde | 1073 | 1083 |
| heeft_tijdlijn_geldigheid | 1073 | 1083 |
| heeft_tijdlijn_registratie | 1073 | 1083 |
| indicatie_formele_historie | 1073 | 1083 |
| indicatie_materiele_historie | 1073 | 1083 |
| stereotype | 0 | 1071 |
| src_mult_start | 1073 | 1080 |
| src_mult_end | 1073 | 1075 |
| dst_mult_start | 1073 | 1082 |
| dst_mult_end | 1073 | 1069 |
| src_role | 11 | 0 |
| dst_role | 32 | 0 |

**enumerations**

| kolom | xmi | qea |
|---|---|---|
| definitie | 38 | 38 |
| toelichting | 86 | 86 |
| herkomst | 90 | 89 |
| herkomst_definitie | 90 | 89 |
| datum_opname | 90 | 89 |
| stereotype | 601 | 598 |


## 5. Diagrammen

- xmi: 243 diagrammen, 1866 klasse-plaatsingen (1866 met geometrie), 138 verborgen associaties
- qea: 243 diagrammen, 1838 klasse-plaatsingen (1838 met geometrie), 138 verborgen associaties
