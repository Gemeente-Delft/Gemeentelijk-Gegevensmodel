# Datatypes GGM v3.0.0 naar MIM: mapping

*Status: doorgevoerd in het EA-model op 4 november 2026 met tools/fix_datatypes_mim.py (3.267 attributen). De vervolgstappen onder "Open punten" staan nog open.*

## Context

Het GGM v3.0.0 typeert attributen nog grotendeels in de RSGB/StUF-notatie (AN80, N2, int, datum, Text, string, Bedrag, GUID …). De classifier van die attributen wijst in Enterprise Architect meestal al naar het pakket *MIM11 Primitieve datatypen* (AN80 → CharacterString, int → Integer, datum → Date), maar de zichtbare typetekst niet, en de lengte zit in de typetekst en in het EA-veld *Length* in plaats van in de MIM-tag *Lengte*. Alle generatoren werken op de typetekst: de codegeneratietemplates (DDL) en crunch_uml (markdown, LOD, Excel, vertalingen).

De omzetting maakt de typetekst gelijk aan het MIM-datatype en zet lengte, eenheid en patroon in de MIM-tags. De informatie die nu in de typetekst zit, gaat dus niet verloren maar verhuist naar de plek waar MIM hem verwacht.

## Uitgangspunten

- Alleen de elf MIM-standaardtypen (CharacterString, Integer, Real, Decimal, Boolean, Date, DateTime, Year, Day, Month, URI), aangevuld met drie eigen primitieve datatypen (Blob, OnvolledigeDatum, Tijd), één gestructureerd datatype (NEN3610ID) en de GML3-geometrieën (GM_Point enz.).
- De typetekst van een attribuut is altijd gelijk aan de naam van de classifier.
- **Lengte**: tag *Lengte* met een kaal getal, gelezen als maximumlengte ("80"). Bij Decimal "cijfers,decimalen" ("10,2"). De EA-velden *Length*, *Precision* en *Scale* worden ook gevuld, voor de DDL-templates.
- **Eenheid**: tag *Eenheid* ("EUR" bij bedragen).
- **Patroon**: tag *Formeel patroon* (reguliere expressie) bij GUID, e-mail, IBAN en telefoonnummer.
- **Ja/nee-velden**: MIM Boolean. Alleen INDIC en StdIndJN blijven een eigen enumeratie (keuze beheerder).
- Real wordt niet gebruikt; double en decimal worden Decimal.

## Mappingtabel

| Nu in het model | Aantal | Wordt | Tags en velden |
| :--- | ---: | :--- | :--- |
| AN80, AN200, AN40, AN20, AN50, AN255, AN100, AN250, … en A1 | 1.287 | CharacterString | Lengte = n; EA Length = n |
| Text, Tekst, string, varchar, char, AN zonder getal, CharacterString | 404 | CharacterString | geen lengte, tenzij EA Length of tag al gevuld is |
| Date, datum | 761 | Date | |
| DateTime, DatumTijd | 110 | DateTime | |
| int, Integer, Number | 481 | Integer | |
| N2, N3, N4, N5, N6, N8, N9, N11, N12 | 106 | Integer | Lengte = n |
| N10.2 | 1 | Decimal | Lengte 10,2; Precision 10, Scale 2 |
| double, decimal | 10 | Decimal | |
| Boolean, Bool | 315 | Boolean | |
| Boolean als enumeratie Ja/Nee/Onbekend/Leeg (Enumeratiesoort, Model BAG) | 22 | Boolean | Mogelijk geen waarde = Ja; de twee enumeraties *Boolean* vervallen |
| StdIndJN (enumeratie Ja/Nee) | 43 | StdIndJN, blijft eigen enumeratie | 8 attributen krijgen alsnog de classifier |
| INDIC | 4 | INDIC, nieuwe eigen enumeratie (Ja/Nee) in Enumeratiesoort | |
| Bedrag, bedrag, Geldbedrag | 167 | Decimal | Lengte 10,2; Eenheid EUR; Precision 10, Scale 2 |
| GUID | 50 | CharacterString | Lengte 36; Formeel patroon UUID |
| Email, IBAN, telefoonnummer | 4 | CharacterString | Formeel patroon per soort; IBAN Lengte 34, telefoonnummer Lengte 10 |
| URL, URI | 2 | URI | |
| JAAR, Jaar, Dag, Maand | 2 | Year, Day, Month | GGM-varianten vervallen (Dag en Maand zijn ongebruikt) |
| Time | 3 | Tijd, nieuw eigen «Primitief datatype» in GGM Datatypes | crunch_uml mapt "tijd" al naar xsd:time |
| BLOB, Image | 5 | Blob, blijft eigen «Primitief datatype» | |
| OnvolledigeDatum | 16 | OnvolledigeDatum, blijft eigen «Primitief datatype» | Formeel patroon op het datatype: jjjjmmdd, 00 voor onbekend |
| NEN3610ID, CompositeID | 29 | NEN3610ID als «Gestructureerd datatype» (namespace, lokaalID, versie) | CompositeID gaat erin op; de foute classifier Integer wordt hersteld |
| Point, punt, Spatial, Surface, Vlak, MultiSurface, Curve, Lijn, MultiCurve, MultiPoint, Object | 115 | GM_Point, GM_Surface, GM_MultiSurface, GM_Curve, GM_MultiCurve, GM_MultiPoint, GM_Object (GML3, ongewijzigd) | alleen typetekst gelijk aan classifier |
| "1" (hoek), "2" (som), "ntatie" (oriëntatie), Enum | 12 | Decimal, Decimal, Decimal, handmatig | |
| Type, TypePlus, Materiaal, Leverancier, … zonder classifier (vooral Model IMBOR) | 292 | buiten deze omzetting | later koppelen aan enumeraties (IMBOR-werk) |
| Enumeraties, objecttypen, gestructureerde datatypen als type | 379 | ongewijzigd | |

Aantallen: attributen in v3.0.0 op 4 november 2026 vóór de omzetting (4.585, exclusief 4.236 enumeratiewaarden). Bij de doorvoering waren het er 4.618 door 33 nieuwe attributen uit de Financiën-proposals van diezelfde middag; het rapport tools/mim-datatypes-omzetting.md heeft de definitieve aantallen.

## Formele patronen

| Soort | Formeel patroon |
| :--- | :--- |
| GUID (UUID zonder accolades) | `^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$` |
| E-mail | `^[^@\s]+@[^@\s]+\.[^@\s]+$` |
| IBAN | `^[A-Z]{2}[0-9]{2}[A-Z0-9]{1,30}$` |
| Telefoonnummer (10 cijfers, conform de huidige GGM-definitie) | `^[0-9]{10}$` |
| OnvolledigeDatum (jjjjmmdd, 00 voor onbekend) | `^[0-9]{4}([0-9]{2}\|00)([0-9]{2}\|00)$` |

## Wat verandert er voor de generatoren

- **crunch_uml, import**: `primitive` krijgt de MIM-naam in plaats van AN80; de tag *Lengte* komt als `lengte` mee. Geen aanpassing nodig.
- **crunch_uml, LOD**: `map_datatype` kent characterstring, integer, decimal, boolean, date, datetime, uri, year en tijd al. De maximumlengte komt na de omzetting uit `mim:lengte` (sh:maxLength) in plaats van uit "AN80". Controlegetal: de shapes-ttl van v3.0.0 heeft nu 1.317 sh:maxLength; dat mag niet dalen. Eigen primitieve datatypen (Blob, OnvolledigeDatum, Tijd) worden mim:PrimitiefDatatype met sh:datatype.
- **crunch_uml, markdown (tools/ggm_markdown.j2)**: toont alleen `getDatatype()`; de lengte erbij tonen, bijvoorbeeld "CharacterString (80)".
- **crunch_uml, JSON-schema en SQLAlchemy** (niet in de GGM-pijplijn): kennen geen decimal en gebruiken `lengte` niet; de $def *bedrag* vervalt. Apart op te pakken.
- **Codegeneratietemplates (EA, Tables_Transform_Template › Attribute__RSGB)**: vertakt op de typetekst. Nieuwe takken nodig voor characterstring (varchar met de attribuutlengte, zonder lengte text), decimal (precision en scale uit de EA-velden), year/day/month, uri en nen3610id. Bug: na TO_LOWER matchen de vergelijkingen op "CharacterString", "Geldbedrag" en "StdIndJN" nooit. De takken an<n>, bedrag en guid kunnen als terugval blijven.
- **Excel-export**: de kolom *primitive* verandert van inhoud (AN80 → CharacterString, lengte in de kolom *lengte*).
- **Vertalingen**: volgen vanzelf na `task translate`.
- **Documentatie**: de datatypelijst in docs/generatie.md en het cookbook herschrijven naar de MIM-namen.

## Open punten

- NEN3610ID als gestructureerd datatype volgens NEN 3610 (voorkeur) of als CharacterString met formeel patroon; het gestructureerde datatype raakt de DDL-templates.
- De stereotypen «Primitief datatype» en «Gestructureerd datatype» (MIM-profiel) op de eigen datatypen, in plaats van «Interface».
- De 292 losse typenamen zonder classifier (vooral Model IMBOR en Beheer Openbare Ruimte).
- Het verwijderen van de nu onverwezen datatypen (Bedrag, Dag, Jaar, Maand, Email, GUID, IBAN, Telefoonnummer, Geldbedrag, CompositeID, de twee enumeraties Boolean) gebeurt pas na controle in EA; de enumeratie Boolean staat nog op 10 diagrammen, CompositeID op 6.
- Zes attributen met typetekst "Enum" (Leerroute, Rijbewijs/Certificaat) zijn handmatig te typeren.
