# Public Space

## Base object types

### Standards

A number of national and international data standards come together in the elaboration of public space; they do not line up seamlessly:

1. [GML 3.2.1 (Geography Markup Language)](https://www.geonovum.nl/geo-standaarden/geography-markup-language-gml/gml-encoding-standard-321) — describes how geographic locations, lines, areas and combinations must be recorded and exchanged. Standardised by OGC and as ISO 19136:2007. The ISO variant is on the Dutch *comply-or-explain* list of the Standardisation Forum.
2. [NEN 3610: 2011 (Base model for geo-information)](https://www.geonovum.nl/geo-standaarden/nen-3610-basismodel-voor-informatiemodellen) — terms, definitions, relationships and general rules for exchanging information about spatial objects. Also on the *comply-or-explain* list.
3. [IMBGT/IMGeo version 2.1.1](https://www.geonovum.nl/geo-standaarden/bgt-imgeo/gegevenscatalogus-imgeo-versie-211) — the BGT defines information available via the BGT base registration, serving as a base layer for the other models.
4. [IMBAG version 0.99](https://www.geonovum.nl/geo-standaarden/informatiemodellen-nen3610-familie/gegevenscatalogus-basisregistratie-adressen-en) — addresses and buildings in the Netherlands. Based on NEN 3610 principles.
5. [RSGB 3.0](https://www.gemmaonline.nl/index.php/RSGB_3.0_in_ontwikkeling) — the semantic standard for municipal basic data.
6. [IMBOR version 2018-1](https://www.crow.nl/thema-s/management-openbare-ruimte/imbor/project-imbor) — national agreements on object data for managing public space.

Where applicable to Delft, these standards are used as much as possible. Some object types are not (yet) in these models, such as [IMKL](https://www.geonovum.nl/geo-standaarden/informatiemodellen-nen3610-familie/informatiemodel-kabels-en-leidingen-imkl) (cables and pipelines), [IMWV](https://www.crow.nl/thema-s/wegontwerp/imwv-informatiemodel-wegen-en-verkeer) (roads and traffic) and [IMWA](http://www.aquo.nl/over-aquo/aquo-onderdelen/aquo-modellen/imwa/) (water). The next figure shows how the coherence of these standards is elaborated in the GGM.

![Coherence of Spatial Standards][samenhangRuimtelijkeStandaarden]

<em>Diagram (in Dutch): coherence between GML, NEN 3610, IMBGT/IMGeo, IMBAG, RSGB and IMBOR in the GGM.</em>

### Geo-objects

Geo-objects are object types containing information about objects in space and how they can be rendered. IMGeo and the RSGB include geo-object types. RSGB 3.0 contains little to no information about managing public-space objects — that is in IMBOR.
The GGM builds on the RSGB and supplements it with other standards when not covered by the RSGB. Where no standard is available, the GGM is extended with new object types. To stay aligned with the other spatial standards, GML and NEN 3610 are applied.

RSGB version 3.0 (still in concept) was chosen because it incorporates IMGeo and IMBAG. A generic new object type, *Geo-Object*, has been added that is not in RSGB 3.0. The required RSGB 3.0 parts were added to the *Core* model.

![Geo-objects from RSGB][geoObjectenUitRSGB]

<em>Diagram (in Dutch): how geo-objects from RSGB derive from Geo-Object, and link to Management Object from IMBOR.</em>

The figure shows how all geo-objects from the RSGB derive from the object type *Geo-Object*, and how it links to the object type *Management Object* from IMBOR. The shown object types are all adopted from IMGeo, establishing the connection with the BGT.

In RSGB 3.0, the following object types are not adopted from IMGeo: Bak, Bord, Bouwwerk, Installatie, Kast, Mast, OverigeConstructie, Paal, Put, RegistratiefGebied, Sensor, Straatmeubilair, Waterinrichtingselement, Weginrichtingselement. The designers and reviewers of RSGB 3.0 chose this because these did not merit a full representation. Instead, the generic object type *Inrichtingselement* (furnishing element) was added to the RSGB. All of the above object types are to be seen as *Inrichtingselement*.

### Management objects

Management objects are object types from public space with their management aspects — in contrast to geo-objects, which describe how objects are rendered on a map. Management objects derive from IMBOR, and the object types that Delft manages or that otherwise play a role are adopted.

![Management Objects][beheerobjecten]

<em>Diagram (in Dutch): management objects from IMBOR adopted into the GGM, and their relation to geo-objects.</em>

The figure above shows which management objects from IMBOR are adopted in the GGM and how they relate to the geo-objects. Only the main objects are adopted, all derived from *Management Object*. There is also a set of management objects derived from these main objects:

```
Aansluitput, Abri, AED, Afvalbak, Afwateringsgebied, Bank, Bemalingsgebied, Bergingsbassin, Beschoeiing, Boom, Brug, Container, Debietmeter, Dek, Depot, Detectielus, Drainageput, Drinkkraan, Drukknoppaal, Ecoduct, Fietsparkeervoorziening, Filterput, Flyover, Geluidsscherm, Gemaal, Halteplaats, Hondenpoeppaal, Hoogtebegrenzer, Hotspot, Huisnummerbord, Infiltratieput, InklapbarePaal, Inzamelpunt, Kademuur, Keermuur, Kering, Klimplant, Klok, Kolk, Landhoofd, Lichtmast, Ligplaatsstrook, Mottobord, OndergrondseContainer, Onttrekkingsput, OV-kast, Overstortconstructie, Park, Parkeerautomaat, Parkeerbeugel, Parkeerdek, Parkeerverwijssysteem, Picknicktafel, Pijlbak, Plaatsnaambord, Pomp, Putdeksel, Recreatie, Regenmeter, Rioleringsgebied, Rioolkast, Rioolput, Risicogebied, Rooster, Sloof, SolitairePlant, Speelterrein, Speeltoestel, Sportcomplex, Sportterrein, Steiger, Straatnaambord, Stuwgebied, Toilet, Trap, Tunnelbak, Tunnelbuis, Tunnelgang, Tunnelwand, Uitlaatconstructie, Urinoir, Vacuümopslagtank, Veldverlichting, Verkeersbord, Verkeersbordpaal, Verkeersdrempel, Verkeerskast, Verkeerslichtmast, Verkeerslichtportaal, Viaduct, Vlonder, VRI-locatie, VRI-paal, Walstroomkast, Zandkist, Zoutbak en Zuiveringsgebied
```

These are included in the model, but listing them all here goes beyond scope.

### Management objects vs geo-objects

The next figure shows the relationship between geo-objects and management objects.

![IMGeo vs IMBOR][imgeovsimbor]

<em>Diagram (in Dutch): two perspectives on a tree — IMGeo (rendering attributes) vs IMBOR (management attributes).</em>

Two perspectives on a tree are shown. In the BGT/IMGeo (RSGB 3.0) domain, attributes are shown for correctly rendering the tree. In the management part, attributes needed for managing the tree are held. The next figure shows the different kinds of information held about the same object type.

![IMGeo vs IMBOR object types][imborvsimgeoobjecttypen]

<em>Diagram (in Dutch): IMGeo vs IMBOR object types for the same real-world object.</em>

## Object types and Municipal Information

### Inspections and reports

Maintenance of management objects is carried out via inspection rounds. The GGM has a number of object types in addition to management objects. These are elaborated in the next figure.

An *Inspection Round* may have multiple reports. Each report relates to a *Management Object*, and management objects have a *Logbook* in which reports are recorded. A *Report* has a reporter and a supplier who will resolve it.
There are several kinds of report:

1. CROW report, per the CROW methodology.
2. Accident report — only for play equipment, where accidents per item are tracked.
3. Malfunction — reports on traffic lights and street lighting, where malfunctions in the system become visible and are resolved by a supplier.
4. Inspection — done by an inspector and reported as such.
5. Action — planned maintenance actions.

![Inspection rounds management objects][schouwrondesbeheerobjecten]

<em>Diagram (in Dutch): data model for inspection rounds covering management objects.</em>

Inspection rounds are carried out within *Areas*, which fall within one or more *Districts* or *Neighbourhoods*.

![Inspection rounds within areas][schouwrondesInArealen]

<em>Diagram (in Dutch): inspection rounds and how they relate to areas, districts and neighbourhoods.</em>

### Road excavations

For planned road excavations a *MOOR report* (*Melding Opbreking Openbare Ruimte*) is submitted by the *Contractor* performing the digging work. A *Contractor* may be a *Supplier* or a *Landowner*, both *Legal Entity*.
An applied-for *Environmental Permit* may require multiple MOOR reports. After the digging, an inspection is performed by a municipal *Staff Member*, who produces an *Official Report* recorded in a *Document*.

![Report of excavation work][meldingGraafwerkzaamheden]

<em>Diagram (in Dutch): data model for MOOR-reports of excavation work.</em>

### Housing-construction projects

Housing-construction projects executed in the context of area management are administered separately. Housing-construction projects may fall within a *Programme*. Each project delivers a number of homes of one of three kinds: owner-occupied, rented or student housing. A *Housing-construction Project* has one or more project developers and may have a *Project Leader*.

![Housing-construction projects][woningbouwprojecten]

<em>Diagram (in Dutch): data model for housing-construction projects.</em>

Energy labels and home sizes use predefined lists/enumerations.

## Base registrations

### BAG (Base Registration of Addresses and Buildings)

The IMBAG (Information Model for the Base Registration of Addresses and Buildings) is adopted in RSGB 3.0. For this reason, the object types are taken from RSGB 3.0.

These are all object types addressable from the BAG and therefore have a BAG identification. All objects have a real address with postcode and house number. With the most generic object type *Addressable Object Designation* giving all underlying object types a real address, there are two generic object types below it: *Number Designation* and *Other Addressable Object Designation*, both giving all object types a BAG id. See the figure below.

![Addressable objects][adresseerbareObjecten]

<em>Diagram (in Dutch): the generic addressable-object types from the BAG, via RSGB 3.0.</em>

The next figure shows all BAG object types in coherence: the three generic ones and the five concrete ones.

![Addresses, buildings and terrains][ruimteAdressenEnGebouwenEnTerreinen]

<em>Diagram (in Dutch): all BAG object types in coherence — Ligplaats, Standplaats, Verblijfsobject, Overig Gebouwd Object, Overig benoemd terrein.</em>

All five concrete object types are actual addressable objects found in the BAG — all *"formally designated as such by the competent municipal body"*.

**Ligplaats (mooring place)**: place in the water, possibly supplemented with land or part thereof, intended for permanently mooring a vessel suitable for residential, business or recreational purposes.

**Standplaats (pitch)**: terrain or part thereof intended for permanently placing a space not directly and durably connected to the earth, suitable for residential, business or recreational purposes.

**Verblijfsobject (residence object)**: the smallest unit of use within one or more buildings, suitable for residential, business or recreational purposes, accessed via its own lockable entrance from the public road, a courtyard or shared traffic space; can be the subject of property-rights transactions; and is functionally self-contained.

**Overig Gebouwd object (other built object)**: the smallest unit of use, not being a residence object, within a functionally and constructively self-contained unit directly and durably connected to the earth.

**Overig benoemd terrein (other named terrain)**: unbuilt terrain (or part thereof), not a *standplaats* or part of a *ligplaats*, intended for performing a social activity over a longer period.

### Cadastral objects and restrictions

Cadastral objects are used for applying a property right to an object. In RSGB 3.0 this may be a parcel or an apartment right. A property right may be: ownership, co-ownership, apartment right, right of usufruct, right of use and occupation, easements, ground lease and the right of superficies. The holder of a property right may be a natural or non-natural person.

The next figure shows how a *Property Right* rests on a *Cadastral Real Estate*. Such a *Cadastral Real Estate* may be a *Cadastral Parcel* or an *Apartment Right*, or may remain generic. A public-law restriction under the WKPB is established via a *Cadastral real-estate note*.
The connection with addressable objects from the BAG is made via the relationship with the most generic type *Named Object*. A *Legal Entity* (natural person or business) holds a *property right* and can thus, for example, own a parcel.

![Cadastral objects and restrictions][kadastraleObjectenEnBeperkingen]

<em>Diagram (in Dutch): data model for cadastral objects and property-right restrictions.</em>

A *Cadastral Mutation* may lead to establishing or changing a property right (e.g. transfer of ownership). A mutation always concerns one or more *Cadastral real-estate objects*; in the case of a sale one, but in the case of a split two or more.

[imgeovsimbor]: image/IMGeoVSIMBOR.png "IMGeo vs IMBOR"
[samenhangRuimtelijkeStandaarden]: image/SamenhangRuimtelijkeStandaarden.png "Coherence of Spatial Standards"
[geoObjectenUitRSGB]: image/EAID_4896574A_C4DD_4b27_A3B9_4481F4B29CCB.jpg "Geo-objects from RSGB"
[beheerobjecten]: image/EAID_E3EBD7A0_35C4_4bf4_BD01_6D97AD0B8BF3.jpg "Management objects"
[imborvsimgeoobjecttypen]: image/EAID_B832F543_BBE3_421e_B76D_561E53237684.jpg "IMGeo vs IMBOR object types"
[schouwrondesbeheerobjecten]: image/EAID_F9907E9B_BD04_439e_A0A9_C6E7BA7F6623.jpg "Inspection rounds management objects"
[schouwrondesInArealen]: image/EAID_8BE01DD9_B915_4291_B190_AB69D0252391.jpg "Inspection rounds within areas"
[meldingGraafwerkzaamheden]: image/EAID_1D1CC6D9_472B_4f91_8096_0260E27F641C.jpg "Excavation report"
[woningbouwprojecten]: image/EAID_5B2022A2_1DAB_476d_BBCD_CD27F56F169F.jpg "Housing-construction projects"
[adresseerbareObjecten]: image/EAID_1279615F_663B_4c7f_BDF3_CD1DA37A87BC.jpg "Addressable objects"
[ruimteAdressenEnGebouwenEnTerreinen]: image/EAID_7561B00D_273B_425a_B2FE_1C3AE499ED2E.jpg "Addresses, buildings and terrains"
[kadastraleObjectenEnBeperkingen]: image/EAID_F9683FD0_4AA1_40c0_A132_4EA8F639B371.jpg "Cadastral objects and restrictions"
