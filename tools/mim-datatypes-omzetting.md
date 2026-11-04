# Omzetting datatypes naar MIM: doorgevoerd

*2026-11-04 16:26:10, script tools/fix_datatypes_mim.py, mapping in tools/mim-datatypes-mapping.md.*

Attributen (zonder enumeratiewaarden): 4618. Met een geplande wijziging: 3267. Handmatig te beoordelen: 6. Buiten scope: 283. Attributen zonder enige MIM-tag: 274.

## Samenvatting per doel

| Doel | Attributen | Gewijzigd | Typetekst | Classifier | Tag Lengte | Lengte-rij nieuw | Andere tags | EA Length/Prec/Scale |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| CharacterString + Lengte | 1357 | 1321 | 1287 | 9 | 1316 | 5 | 0 | 43 |
| Date | 766 | 404 | 352 | 52 | 0 | 0 | 0 | 0 |
| Integer | 481 | 474 | 466 | 9 | 0 | 0 | 0 | 0 |
| ongewijzigd (enumeratie, objecttype of datatype als type) | 376 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| CharacterString (zonder lengte) | 352 | 312 | 259 | 56 | 0 | 0 | 0 | 0 |
| Boolean | 294 | 200 | 200 | 0 | 0 | 0 | 0 | 0 |
| buiten scope: losse typenaam zonder classifier | 283 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Decimal 10,2 EUR (was Bedrag/Geldbedrag) | 171 | 171 | 171 | 171 | 129 | 42 | 171 | 342 |
| GM_* (GML3, ongewijzigd) | 115 | 115 | 115 | 4 | 0 | 0 | 0 | 0 |
| DateTime | 110 | 22 | 22 | 0 | 0 | 0 | 0 | 0 |
| Integer + Lengte | 106 | 106 | 106 | 0 | 106 | 0 | 0 | 0 |
| CharacterString 36 + patroon (was GUID) | 50 | 50 | 50 | 50 | 50 | 0 | 50 | 50 |
| StdIndJN (eigen enumeratie) | 43 | 8 | 0 | 8 | 0 | 0 | 0 | 0 |
| NEN3610ID (gestructureerd datatype, herstructurering apart) | 29 | 29 | 4 | 29 | 0 | 0 | 0 | 0 |
| Boolean (was enumeratie Ja/Nee/Onbekend/Leeg) | 22 | 22 | 0 | 22 | 0 | 0 | 3 | 0 |
| Decimal | 16 | 11 | 11 | 3 | 0 | 0 | 0 | 0 |
| OnvolledigeDatum (eigen primitief datatype) | 16 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| handmatig | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Blob (eigen primitief datatype) | 5 | 3 | 3 | 1 | 0 | 0 | 0 | 0 |
| INDIC (eigen enumeratie) | 4 | 4 | 0 | 4 | 0 | 0 | 0 | 0 |
| CharacterString + patroon (was Email/IBAN/Telefoonnummer) | 4 | 4 | 4 | 4 | 2 | 0 | 4 | 2 |
| typetekst gelijk aan classifier | 3 | 3 | 3 | 0 | 0 | 0 | 0 | 0 |
| Tijd (eigen primitief datatype) | 3 | 3 | 3 | 3 | 0 | 0 | 0 | 0 |
| URI | 3 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| Year (was Jaar) | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 0 |
| Decimal + Lengte | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 2 |

## Brontypen per doel

- **CharacterString + Lengte**: AN80 ×303, AN200 ×195, AN40 ×163, AN20 ×124, AN50 ×83, CharacterString ×70, AN255 ×50, AN100 ×48, AN250 ×41, AN2 ×26, AN300 ×25, AN10 ×19 … (+40 andere)
- **Date**: Date ×414, DATUM ×130, Datum ×115, date ×85, datum ×19, DATE ×3
- **Integer**: integer ×243, int ×221, Integer ×15, Number ×1, Int ×1
- **ongewijzigd (enumeratie, objecttype of datatype als type)**: statusGeoObject ×17, Wet ×12, ClassificatieArmTotUitstekend ×10, BAGObjectnummering ×10, Document ×8, LandOfgebied ×6, Land ×6, Adresaanduiding ×6, Opdrachtcategorie ×6, CdPeriode ×5, Eenheid ×5, TypeAdresseerbaarObject ×4 … (+223 andere)
- **CharacterString (zonder lengte)**: text ×106, CharacterString ×93, Text ×74, string ×39, String ×14, Varchar ×11, char ×6, AN ×4, Tekst ×3, varchar ×2
- **Boolean**: boolean ×168, Boolean ×94, bool ×20, Bool ×12
- **buiten scope: losse typenaam zonder classifier**: Type ×30, Leverancier ×17, TypePlus ×15, Materiaal ×15, KwaliteitsniveauGewenst ×10, Vorm ×8, Taalvaardigheid ×8, TypeFundering ×7, CategorieAnderInkomen ×6, BelastingklasseNieuw ×5, BelastingklasseOud ×5, Kleuren ×5 … (+108 andere)
- **Decimal 10,2 EUR (was Bedrag/Geldbedrag)**: Bedrag ×109, bedrag ×38, Geldbedrag ×23, 2 ×1
- **GM_* (GML3, ongewijzigd)**: Surface ×38, Point ×24, MultiSurface ×15, Object ×15, Curve ×9, Vlak ×3, punt ×3, Punt ×2, MultiCurve ×2, point ×1, Lijn ×1, Spatial ×1 … (+1 andere)
- **DateTime**: DateTime ×88, Datetime ×12, datetime ×5, DatumTijd ×3, dateTime ×2
- **Integer + Lengte**: N2 ×28, N3 ×20, N4 ×15, N5 ×13, N6 ×10, N1 ×7, N8 ×5, N9 ×3, N12 ×2, N11 ×2, n4 ×1
- **CharacterString 36 + patroon (was GUID)**: GUID ×42, guid ×8
- **StdIndJN (eigen enumeratie)**: StdIndJN ×43
- **NEN3610ID (gestructureerd datatype, herstructurering apart)**: NEN3610ID ×25, CompositeID ×4
- **Boolean (was enumeratie Ja/Nee/Onbekend/Leeg)**: Boolean ×22
- **Decimal**: double ×7, Decimal ×5, ntatie ×2, 1 ×1, decimal ×1
- **OnvolledigeDatum (eigen primitief datatype)**: OnvolledigeDatum ×15, Onvolledigedatum ×1
- **handmatig**: Enum ×5, enum ×1
- **Blob (eigen primitief datatype)**: BLOB ×2, Blob ×2, Image ×1
- **INDIC (eigen enumeratie)**: INDIC ×4
- **CharacterString + patroon (was Email/IBAN/Telefoonnummer)**: email ×2, IBAN ×1, telefoonnummer ×1
- **typetekst gelijk aan classifier**: <Orphan Class> ×2, NATIONALITEIT ×1
- **Tijd (eigen primitief datatype)**: Time ×3
- **URI**: URI ×2, URL ×1
- **Year (was Jaar)**: JAAR ×2
- **Decimal + Lengte**: N10.2 ×1

## Nieuwe en vervallende modelelementen

- Aan te maken: enumeratie **INDIC** (Ja/Nee) in pakket Enumeratiesoort; eigen primitief datatype **Tijd** in GGM Datatypes.
- Na de omzetting onverwezen (verwijderen gebeurt apart, na controle in EA):

| Element | Pakket | Attributen nu | Attributen na omzetting | Op diagrammen | Connectors |
| :--- | :--- | ---: | ---: | ---: | ---: |
| DataType Bedrag | GGM Datatypes | 128 | 0 | 0 | 0 |
| Enumeration Boolean | Model BAG | 3 | 0 | 1 | 0 |
| Enumeration Boolean | Enumeratiesoort | 19 | 0 | 10 | 0 |
| DataType CompositeID | Complex datatype | 4 | 0 | 6 | 0 |
| DataType Dag | GGM Datatypes | 0 | 0 | 0 | 0 |
| DataType Email | GGM Datatypes | 0 | 0 | 0 | 0 |
| DataType GUID | GGM Datatypes | 50 | 0 | 0 | 0 |
| DataType Geldbedrag | Datatypes | 0 | 0 | 0 | 0 |
| DataType IBAN | GGM Datatypes | 1 | 0 | 0 | 0 |
| DataType Jaar | GGM Datatypes | 0 | 0 | 0 | 0 |
| DataType Maand | GGM Datatypes | 0 | 0 | 0 | 0 |
| DataType Telefoonnummer | GGM Datatypes | 0 | 0 | 0 | 0 |
- Apart te doen: NEN3610ID herstructureren tot «Gestructureerd datatype» (namespace, lokaalID, versie) met CompositeID erin; stereotype «Primitief datatype» op Blob, OnvolledigeDatum en Tijd.

## Handmatig te beoordelen (6)

- Model Inburgering › Leerroute.LeerrouteType : `Enum` — typetekst 'Enum' zonder enumeratie
- Model Inburgering › Leerroute.Niveau : `Enum` — typetekst 'Enum' zonder enumeratie
- Model Inburgering › Leerroute.GeschatteIntensiteitB1Route : `Enum` — typetekst 'Enum' zonder enumeratie
- Model Inburgering › Leerroute.IndicatorToestemmingExamenA2 : `Enum` — typetekst 'Enum' zonder enumeratie
- Model Werk › Rijbewijs /Certificaat.NaamCertificaat : `enum` — typetekst 'Enum' zonder enumeratie
- Model Werk › Rijbewijs /Certificaat.VerstrekkendePartij : `Enum` — typetekst 'Enum' zonder enumeratie

## Lengteconflicten (0)

Gevallen waar de bestaande tag Lengte of het EA-veld Length afwijkt van de lengte uit de typetekst; de typetekst wint.


## Buiten scope: losse typenamen zonder classifier (283 attributen)

Niet omgezet; apart te koppelen aan enumeraties (IMBOR-werk). Per pakket, met de typenamen:

- **Model IMBOR** (234): Type ×30, Leverancier ×17, TypePlus ×15, Materiaal ×15, KwaliteitsniveauGewenst ×10, Vorm ×8, TypeFundering ×7, BelastingklasseNieuw ×5, BelastingklasseOud ×5, Kleuren ×5, Fabrikant ×4, Bereikbaarheid ×4, Frequentie ×4, Installateur ×4, VrijeDoorrijhoogte ×3, BereikbaarheidPlus ×3, Soortnaam ×3, BoomhoogteklasseActueel ×2, KroondiameterklasseActueel ×2, TypeOmgevingsrisicoklasse ×2, Boomveiligheidsklasse ×2, Bedienaar ×2, CultuurhistorischWaardevol ×2, TypeBewerking ×2, TypeCommunicatie ×2, Onderhoudsregime ×2, IMKLThema ×2, Modaliteit ×2, Wegfunctie ×2, WegcategorieDV ×2, Beheergebied ×1, Gebruiksfunctie ×1, Gebiedstype ×1, Grondsoort ×1, GrondsoortPlus ×1, Onderhoudsplichtige ×1, Status ×1, TypeBeheerder ×1, TypeBeheerderPlus ×1, TypeEigenaar ×1, TypeEigenaarPlus ×1, TypeLigging ×1, Zettingsgevoeligheid ×1, ZettingsgevoeligheidPlus ×1, Beleidsstatus ×1, BeoogdeOmlooptijd ×1, Boombeeld ×1, Boomgroep ×1, TypeBeschermingsstatusPlus ×1, Boomvoorziening ×1, Controlefrequentie ×1, Groeifase ×1, Snoeifase ×1, StamdiameterKlasse ×1, TakvrijeStam ×1, TypeBeschermingsstatus ×1, TypeVermeerderingsvorm ×1, VrijeTakval ×1, BreedteklasseHaag ×1, Sluitingspercentage ×1, HoogteklasseHaag ×1, Ondergroei ×1, Taludsteilte ×1, TypeBovenkantKademuur ×1, TypeSlot ×1, Ondersteuningsvorm ×1, BereikbaarheidKolk ×1, Constructietype ×1, TypeMonument ×1, TypeOnderdeelMetPomp ×1, TypeWaaier ×1, TypeAfdekking ×1, Constructieonderdeel ×1, LeeftijdDoelgroep ×1, Certificeringsinstantie ×1, Toestelonderdeel ×1, Toestelgroep ×1, TypeSport ×1, Kweker ×1, TypeStandplaats ×1, TypeStandplaatsPlus ×1, AanOfVrijliggend ×1, Afmeting ×1, Belasting ×1, Formaat ×1, LengteKunstgras ×1, SoortVoeg ×1, TypeConstructie ×1, TypeVoeg ×1, TypeVoegvulling ×1, Vegen ×1, VulmateriaalKunstgras ×1, Waterdoorlatendheid ×1, WegtypeBestaand ×1, TypeVaarwater ×1, TypeWaterplant ×1
- **Model Werk** (16): Taalvaardigheid ×8, arbeidsvermogen ×1, ontheffing ×1, document ×1, CodeNiveauOpleiding ×1, Opleidingsrichting ×1, CodeLeerwegMBO ×1, CodeSoortOpleidingsnaam ×1, score ×1
- **Reden aanvraag** (7): CdRedenAanvraagWwafgewezen ×5, CdRedenAanvraagEindeBijstand ×2
- **Model Terug- en invordering** (6): CategorieAnderInkomen ×6
- **Model Kern RSGB** (4): LAND ×2, typeringOndersteunendWaterPlus ×1, functieOndersteunendWegdeelPlus ×1
- **Model Diensten** (3): Brontype ×2, CdTypeVerstrekkingsvorm ×1
- **Model Vermogen** (3): Brontype ×2, Rekeningtype ×1
- **Model BAG** (2): statusOpenbareRuimte ×2
- **Model Normafwijking** (2): CodeRedenMaatregel ×2
- **Model Sport** (2): Adresaanduiding ×2
- **Groepattribuutsoort** (1): LAND ×1
- **Model Inkomsten** (1): CategorieVorderingCBS ×1
- **Model Onderwijs** (1): Adres ×1
- **Model Sociaal Domein Generiek** (1): EnumHuishoudenssoort ×1

Typenamen waarvoor een gelijknamig element bestaat (niet automatisch gekoppeld; controleer of het past):

- `Leverancier` ×17: gelijknamig: Class Leverancier in Model Sociaal Domein Generiek; Class Leverancier in Model Inkoop
- `Taalvaardigheid` ×8: gelijknamig: Class Taalvaardigheid in Model Inburgering; Enumeration Taalvaardigheid in Model Werk
- `CategorieAnderInkomen` ×6: gelijknamig: Enumeration CategorieAnderInkomen in Datatypes
- `CdRedenAanvraagWwafgewezen` ×5: gelijknamig: Enumeration CdRedenAanvraagWwafgewezen in Datatypes
- `Brontype` ×4: gelijknamig: Enumeration Brontype in Datatypes
- `Frequentie` ×4: gelijknamig: Enumeration Frequentie in Model Jeugd en Wmo Generiek
- `LAND` ×3: gelijknamig: Class Land in Referentielijsten
- `statusOpenbareRuimte` ×2: gelijknamig: Enumeration statusOpenbareRuimte in Model BAG; Enumeration statusOpenbareRuimte in Enumeratiesoort
- `CodeRedenMaatregel` ×2: gelijknamig: Enumeration CodeRedenMaatregel in Datatypes
- `Adresaanduiding` ×2: gelijknamig: Class Adresaanduiding in Model Vastgoed; Class Adresaanduiding in Groepattribuutsoort
- `CdRedenAanvraagEindeBijstand` ×2: gelijknamig: Enumeration CdRedenAanvraagEindeBijstand in Datatypes
- `CdTypeVerstrekkingsvorm` ×1: gelijknamig: Enumeration CdTypeVerstrekkingsvorm in Datatypes
- `Status` ×1: gelijknamig: Class Status in Model Kern RGBZ
- `TypeMonument` ×1: gelijknamig: Enumeration TypeMonument in Model Monumenten
- `CategorieVorderingCBS` ×1: gelijknamig: Enumeration CategorieVorderingCBS in Datatypes
- `EnumHuishoudenssoort` ×1: gelijknamig: Enumeration EnumHuishoudenssoort in Model Schuldhulpverlening
- `Rekeningtype` ×1: gelijknamig: Enumeration Rekeningtype in Datatypes
- `arbeidsvermogen` ×1: gelijknamig: Class Arbeidsvermogen in Model Werk
- `ontheffing` ×1: gelijknamig: Class Ontheffing in Model Inburgering; Class Ontheffing in Model Werk
- `document` ×1: gelijknamig: Class Document in Model Kern RGBZ
- `CodeNiveauOpleiding` ×1: gelijknamig: Enumeration CodeNiveauOpleiding in Model Werk
- `Opleidingsrichting` ×1: gelijknamig: Enumeration Opleidingsrichting in Model Werk
- `CodeLeerwegMBO` ×1: gelijknamig: Enumeration CodeLeerwegMBO in Model Werk
- `CodeSoortOpleidingsnaam` ×1: gelijknamig: Enumeration CodeSoortOpleidingsnaam in Model Werk
- `score` ×1: gelijknamig: Class Score in Model Jeugd en Wmo Generiek
