# Changes from v2.5.0 to v2.5.1

Entiteiten worden vergeleken op naam (gekwalificeerd met pakketpad), zodat een nieuwe `ea_guid` voor hetzelfde logische element niet als _Removed + Added_ verschijnt. Verwijzingen naar andere entiteiten (FK-velden zoals `enumeration_id`) worden vergeleken op de naam van het doel — niet op de interne sleutel.

**Structurele wijzigingen** raken het model zelf: toegevoegde of verwijderde elementen, naamswijzigingen, type/verplicht/multipliciteit/lengte/patroon en links tussen elementen. **Beschrijvende wijzigingen** updaten alleen metadata of documentatie (definitie, toelichting, gemma-tags, versie, auteur, herkomst, …) zonder de structuur van het model te veranderen.

## Samenvatting

| Element | + (struct.) | − (struct.) | ~ (struct.) | ~ (beschr.) |
| --- | ---: | ---: | ---: | ---: |
| Classes | 0 | 976 | 0 | 0 |
| Datatypes | 0 | 0 | 0 | 0 |
| Enumeraties | 0 | 521 | 0 | 0 |
| Attributen | 0 | 4925 | 0 | 0 |
| Associaties | 0 | 1073 | 0 | 0 |
| Generalisaties | 0 | 304 | 0 | 0 |
| Enum-literals | 0 | 4273 | — | — |
| Pakketten (metadata) | 0 | 0 | 0 | 0 |

## Geraakte packages

- **Delfts Gemeentelijk Gegevensmodel/0 Bestuur, Politiek en Ondersteuning/Griffie/Model Griffie** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel0-bestuur-politiek-en-ondersteuninggriffiemodel-griffie)
- **Delfts Gemeentelijk Gegevensmodel/1 Veiligheid en Vergunningen/Model VTH** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel1-veiligheid-en-vergunningenmodel-vth)
- **Delfts Gemeentelijk Gegevensmodel/10 Dienstverlening/Model Dienstverlening** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel10-dienstverleningmodel-dienstverlening)
- **Delfts Gemeentelijk Gegevensmodel/2 Verkeer, Vervoer en Waterstaat/Mobiliteit/Model Mobiliteit** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel2-verkeer-vervoer-en-waterstaatmobiliteitmodel-mobiliteit)
- **Delfts Gemeentelijk Gegevensmodel/2 Verkeer, Vervoer en Waterstaat/Parkeren/Model Parkeren** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel2-verkeer-vervoer-en-waterstaatparkerenmodel-parkeren)
- **Delfts Gemeentelijk Gegevensmodel/3 Economie/Diagram** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel3-economiediagram)
- **Delfts Gemeentelijk Gegevensmodel/3 Economie/Model Economie** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel3-economiemodel-economie)
- **Delfts Gemeentelijk Gegevensmodel/4 Onderwijs/Leerplicht en Leerlingenvervoer/Model Leerplicht en Leerlingenvervoer** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel4-onderwijsleerplicht-en-leerlingenvervoermodel-leerplicht-en-leerlingenvervoer)
- **Delfts Gemeentelijk Gegevensmodel/4 Onderwijs/Onderwijs/Model Onderwijs** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel4-onderwijsonderwijsmodel-onderwijs)
- **Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Erfgoed/Archeologie/Model Archeologie** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatieerfgoedarcheologiemodel-archeologie)
- **Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Erfgoed/Archief/Model Archief** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatieerfgoedarchiefmodel-archief)
- **Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Erfgoed/Generieke Entiteiten Erfgoed/Model Erfgoed Generiek** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatieerfgoedgenerieke-entiteiten-erfgoedmodel-erfgoed-generiek)
- **Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Erfgoed/Monumenten/Model Monumenten** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatieerfgoedmonumentenmodel-monumenten)
- **Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Musea/Diagram** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatiemuseadiagram)
- **Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Musea/Model Musea** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatiemuseamodel-musea)
- **Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Sport/Diagram** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatiesportdiagram)
- **Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Sport/Model Sport** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatiesportmodel-sport)
- **Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Dak- en thuislozen/Model Dak- en thuislozen** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeindak--en-thuislozenmodel-dak--en-thuislozen)
- **Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Gemeentebegrafenissen/Model Gemeentebegrafenissen** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeingemeentebegrafenissenmodel-gemeentebegrafenissen)
- **Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Generiek Jeugd en Wmo/Model Jeugd en Wmo Generiek** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeingeneriek-jeugd-en-wmomodel-jeugd-en-wmo-generiek)
- **Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inburgering/Model Inburgering** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeininburgeringmodel-inburgering)
- **Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Diensten/Datatypes** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomendienstendatatypes)
- **Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Diensten/Model Diensten** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomendienstenmodel-diensten)
- **Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Model Inkomen** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomenmodel-inkomen)
- **Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Normafwijking/Datatypes** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomennormafwijkingdatatypes)
- **Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Normafwijking/Model Normafwijking** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomennormafwijkingmodel-normafwijking)
- **Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Reden aanvraag/Datatypes** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomenreden-aanvraagdatatypes)
- **Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Reden aanvraag/Reden aanvraag** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomenreden-aanvraagreden-aanvraag)
- **Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Terug- en invordering/Datatypes** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomenterug--en-invorderingdatatypes)
- **Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Terug- en invordering/Model Terug- en invordering** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomenterug--en-invorderingmodel-terug--en-invordering)
- **Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Jeugdbescherming en reclassering/Model Jeugdbescherming** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeinjeugdbescherming-en-reclasseringmodel-jeugdbescherming)
- **Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Schulden/Schuldhulpverlening/Diagram** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeinschuldenschuldhulpverleningdiagram)
- **Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Schulden/Schuldhulpverlening/Model Schuldhulpverlening** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeinschuldenschuldhulpverleningmodel-schuldhulpverlening)
- **Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Schulden/Vroegsignalering/Diagram** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeinschuldenvroegsignaleringdiagram)
- **Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Schulden/Vroegsignalering/Model Vroegsignalering** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeinschuldenvroegsignaleringmodel-vroegsignalering)
- **Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Diagram** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiekdiagram)
- **Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiekmodel-sociaal-domein-generiek)
- **Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Inkomsten/Datatypes** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiekmodel-sociaal-domein-generiekinkomstendatatypes)
- **Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Inkomsten/Model Inkomsten** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiekmodel-sociaal-domein-generiekinkomstenmodel-inkomsten)
- **Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Vermogen/Datatypes** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiekmodel-sociaal-domein-generiekvermogendatatypes)
- **Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Vermogen/Model Vermogen** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiekmodel-sociaal-domein-generiekvermogenmodel-vermogen)
- **Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociale Teams/Model Sociale Teams** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociale-teamsmodel-sociale-teams)
- **Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Werk/Model Werk** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeinwerkmodel-werk)
- **Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel7-volksgezondheid-en-milieuafvalmodel-afval)
- **Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Beheer Openbare Ruimte/Model Basis IMBOR/Enumeratiesoort** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingbeheer-openbare-ruimtemodel-basis-imborenumeratiesoort)
- **Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Beheer Openbare Ruimte/Model Basis IMBOR/Model IMBOR** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingbeheer-openbare-ruimtemodel-basis-imbormodel-imbor)
- **Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Beheer Openbare Ruimte/Model Beheer Openbare Ruimte** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingbeheer-openbare-ruimtemodel-beheer-openbare-ruimte)
- **Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Bouwen en Wonen/Model Wonen** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingbouwen-en-wonenmodel-wonen)
- **Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Omgevingswet/Model Omgevingswet/Model Aanvragen en Meldingen** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingomgevingswetmodel-omgevingswetmodel-aanvragen-en-meldingen)
- **Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Omgevingswet/Model Omgevingswet/Model Officiele Publicaties** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingomgevingswetmodel-omgevingswetmodel-officiele-publicaties)
- **Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Omgevingswet/Model Omgevingswet/Model Omgevingswet** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingomgevingswetmodel-omgevingswetmodel-omgevingswet)
- **Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Omgevingswet/Model Omgevingswet/Model Toepasbare Regels** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingomgevingswetmodel-omgevingswetmodel-toepasbare-regels)
- **Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/Financien/Model Financien** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel9-interne-organisatiefinancienmodel-financien)
- **Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/HR/Model HR** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel9-interne-organisatiehrmodel-hr)
- **Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/ICT/Diagram** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel9-interne-organisatieictdiagram)
- **Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/ICT/Model ICT** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel9-interne-organisatieictmodel-ict)
- **Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/Inkoop/Model Inkoop** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel9-interne-organisatieinkoopmodel-inkoop)
- **Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/Organisatie-indeling/Model Organisatie** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel9-interne-organisatieorganisatie-indelingmodel-organisatie)
- **Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/Subsidies/Model Subsidies** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel9-interne-organisatiesubsidiesmodel-subsidies)
- **Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/Vastgoed/Model Vastgoed** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel9-interne-organisatievastgoedmodel-vastgoed)
- **Delfts Gemeentelijk Gegevensmodel/99 Kern/BAG/Model BAG** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel99-kernbagmodel-bag)
- **Delfts Gemeentelijk Gegevensmodel/99 Kern/Dimensies/Model** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel99-kerndimensiesmodel)
- **Delfts Gemeentelijk Gegevensmodel/99 Kern/Generiek/Model Generiek** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel99-kerngeneriekmodel-generiek)
- **Delfts Gemeentelijk Gegevensmodel/99 Kern/RGBZPlus/Diagram/View (Zaak)objecten** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel99-kernrgbzplusdiagramview-zaakobjecten)
- **Delfts Gemeentelijk Gegevensmodel/99 Kern/RGBZPlus/Diagram/View Betrokkene** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel99-kernrgbzplusdiagramview-betrokkene)
- **Delfts Gemeentelijk Gegevensmodel/99 Kern/RGBZPlus/Model RGBZ/Enumeratiesoort** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel99-kernrgbzplusmodel-rgbzenumeratiesoort)
- **Delfts Gemeentelijk Gegevensmodel/99 Kern/RGBZPlus/Model RGBZ/Groepattribuutsoort** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel99-kernrgbzplusmodel-rgbzgroepattribuutsoort)
- **Delfts Gemeentelijk Gegevensmodel/99 Kern/RGBZPlus/Model RGBZ/Metagegevens** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel99-kernrgbzplusmodel-rgbzmetagegevens)
- **Delfts Gemeentelijk Gegevensmodel/99 Kern/RGBZPlus/Model RGBZ/Model Kern RGBZ** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel99-kernrgbzplusmodel-rgbzmodel-kern-rgbz)
- **Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/Diagram** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel99-kernrsgbplusdiagram)
- **Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/Diagram RSGB/Catalogus RSGB/Tekenwijze** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel99-kernrsgbplusdiagram-rsgbcatalogus-rsgbtekenwijze)
- **Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/Diagram RSGB/Diagrammen intern gebruik/Semantische relaties** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel99-kernrsgbplusdiagram-rsgbdiagrammen-intern-gebruiksemantische-relaties)
- **Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Complex datatype** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelcomplex-datatype)
- **Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Enumeratiesoort** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelenumeratiesoort)
- **Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Groepattribuutsoort** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelgroepattribuutsoort)
- **Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Model Kern RSGB** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelmodel-kern-rsgb)
- **Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Referentielijsten** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelreferentielijsten)
- **Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Relatieklasse** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelrelatieklasse)
- **Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Union** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelunion)
- **Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/archief/Model Kern RSGB** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelarchiefmodel-kern-rsgb)

## Structurele wijzigingen

<a id="structureel-delfts-gemeentelijk-gegevensmodel0-bestuur-politiek-en-ondersteuninggriffiemodel-griffie"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/0 Bestuur, Politiek en Ondersteuning/Griffie/Model Griffie

#### Classes

##### `Aanwezige Deelnemer` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aanvangAanwezigheid` — Verwijderd
- 🔴 `eindeAanwezigheid` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `rol` — Verwijderd
- 🔴 `vertegenwoordigtOrganisatie` — Verwijderd

##### `Agendapunt` — 🔴 Verwijderd

**Attributen:**

- 🔴 `nummer` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `titel` — Verwijderd

##### `Categorie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd

##### `Collegelid` — 🔴 Verwijderd

**Attributen:**

- 🔴 `achternaam` — Verwijderd
- 🔴 `datumAanstelling` — Verwijderd
- 🔴 `datumUittreding` — Verwijderd
- 🔴 `fractie` — Verwijderd
- 🔴 `portefeuille` — Verwijderd
- 🔴 `titel` — Verwijderd
- 🔴 `voornaam` — Verwijderd

##### `Dossier` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd

##### `Indiener` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Programma` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd

##### `Raadscommissie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd

##### `Raadslid` — 🔴 Verwijderd

**Attributen:**

- 🔴 `achternaam` — Verwijderd
- 🔴 `datumAanstelling` — Verwijderd
- 🔴 `datumUittreding` — Verwijderd
- 🔴 `fractie` — Verwijderd
- 🔴 `titel` — Verwijderd
- 🔴 `voornaam` — Verwijderd

##### `Raadsstuk` — 🔴 Verwijderd

**Attributen:**

- 🔴 `besloten` — Verwijderd
- 🔴 `datumExpiratie` — Verwijderd
- 🔴 `datumPublicatie` — Verwijderd
- 🔴 `datumRegistratie` — Verwijderd
- 🔴 `typeRaadsstuk` — Verwijderd

##### `Stemming` — 🔴 Verwijderd

**Attributen:**

- 🔴 `resultaat` — Verwijderd
- 🔴 `stemmingstype` — Verwijderd

##### `Taakveld` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd

##### `Vergadering` — 🔴 Verwijderd

**Attributen:**

- 🔴 `eindtijd` — Verwijderd
- 🔴 `locatie` — Verwijderd
- 🔴 `starttijd` — Verwijderd
- 🔴 `titel` — Verwijderd

#### Enumeraties

##### `Deelnemersrol` — 🔴 Verwijderd

**Literals:**

- 🔴 `Inspreker` — Verwijderd
- 🔴 `Overig` — Verwijderd
- 🔴 `Portefeuillehouder` — Verwijderd
- 🔴 `Raadslid` — Verwijderd
- 🔴 `Statenlid` — Verwijderd
- 🔴 `Vice-voorzitter` — Verwijderd
- 🔴 `Voorzitter` — Verwijderd

##### `Stemmingsresultaattype` — 🔴 Verwijderd

**Literals:**

- 🔴 `Gelijk` — Verwijderd
- 🔴 `Tegen` — Verwijderd
- 🔴 `Voor` — Verwijderd

##### `Stemmingstype` — 🔴 Verwijderd

**Literals:**

- 🔴 `Hoofdelijk` — Verwijderd
- 🔴 `Regulier` — Verwijderd
- 🔴 `Schriftelijk` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `Aanwezige Deelnemer` «is» → `Collegelid`
- 🔴 Verwijderd: `Aanwezige Deelnemer` «is» → `NatuurlijkPersoon`
- 🔴 Verwijderd: `Categorie` «heeft» → `Raadsstuk`
- 🔴 Verwijderd: `Dossier` «hoort bij» → `Raadsstuk`
- 🔴 Verwijderd: `Indiener` «heeft» → `Raadsstuk`
- 🔴 Verwijderd: `Indiener` «is» → `Collegelid`
- 🔴 Verwijderd: `Indiener` «is» → `Raadslid`
- 🔴 Verwijderd: `Indiener` «is» → `Rechtspersoon`
- 🔴 Verwijderd: `Raadscommissie` «heeft» → `Vergadering`
- 🔴 Verwijderd: `Raadslid` «is lid van» → `Raadscommissie`
- 🔴 Verwijderd: `Raadslid` «is» → `Aanwezige Deelnemer`
- 🔴 Verwijderd: `Raadsstuk` «behandelt» → `Agendapunt`
- 🔴 Verwijderd: `Raadsstuk` «heeft» → `Taakveld`
- 🔴 Verwijderd: `Raadsstuk` «hoort bij» → `Programma`
- 🔴 Verwijderd: `Raadsstuk` «wordt behandeld in» → `Vergadering`
- 🔴 Verwijderd: `Stemming` «betreft» → `Raadsstuk`
- 🔴 Verwijderd: `Stemming` «hoort bij» → `Agendapunt`
- 🔴 Verwijderd: `Vergadering` «betreft» → `Video-opname`
- 🔴 Verwijderd: `Vergadering` «heeft verslag» → `Raadsstuk`
- 🔴 Verwijderd: `Vergadering` «heeft» → `Agendapunt`
- 🔴 Verwijderd: `Vergadering` → `Aanwezige Deelnemer`

#### Generalisaties

- 🔴 Verwijderd: `Collegelid` ⟶ `Ingezetene`
- 🔴 Verwijderd: `Raadslid` ⟶ `Ingezetene`

<a id="structureel-delfts-gemeentelijk-gegevensmodel1-veiligheid-en-vergunningenmodel-vth"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/1 Veiligheid en Vergunningen/Model VTH

#### Classes

##### `Activiteit Omgevingswet` — 🔴 Verwijderd

**Attributen:**

- 🔴 `omschrijving` — Verwijderd

##### `AOMStatus` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginStatus` — Verwijderd
- 🔴 `datumEindeStatus` — Verwijderd
- 🔴 `status` — Verwijderd
- 🔴 `statuscode` — Verwijderd
- 🔴 `statusVolgorde` — Verwijderd

##### `Bevinding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aangemaaktDoor` — Verwijderd
- 🔴 `activiteit` — Verwijderd
- 🔴 `controleElement` — Verwijderd
- 🔴 `controleniveau` — Verwijderd
- 🔴 `datumAanmaak` — Verwijderd
- 🔴 `datumMutatie` — Verwijderd
- 🔴 `diepte` — Verwijderd
- 🔴 `fase` — Verwijderd
- 🔴 `gemuteerdDoor` — Verwijderd
- 🔴 `resultaat` — Verwijderd
- 🔴 `risico` — Verwijderd

##### `BOA` — 🔴 Verwijderd

##### `Combibon` — 🔴 Verwijderd

**Attributen:**

- 🔴 `sanctie` — Verwijderd

##### `Fietsregistratie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `gelabeld` — Verwijderd
- 🔴 `verwijderd` — Verwijderd

##### `Grondslag` — 🔴 Verwijderd

**Attributen:**

- 🔴 `code` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Heffinggrondslag` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bedrag` — Verwijderd
- 🔴 `domein` — Verwijderd
- 🔴 `hoofdstuk` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `paragraaf` — Verwijderd

##### `Heffingsverordening` — 🔴 Verwijderd

##### `Indiener` — 🔴 Verwijderd

##### `Inspectie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aangemaaktDoor` — Verwijderd
- 🔴 `datumAanmaak` — Verwijderd
- 🔴 `datumGepland` — Verwijderd
- 🔴 `datumInspectie` — Verwijderd
- 🔴 `datumMutatie` — Verwijderd
- 🔴 `gemuteerdDoor` — Verwijderd
- 🔴 `inspectietype` — Verwijderd
- 🔴 `kenmerk` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `opmerkingen` — Verwijderd
- 🔴 `status` — Verwijderd

##### `Kosten` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aangemaaktDoor` — Verwijderd
- 🔴 `aantal` — Verwijderd
- 🔴 `bedrag` — Verwijderd
- 🔴 `bedragTotaal` — Verwijderd
- 🔴 `datumAanmaak` — Verwijderd
- 🔴 `datumMutatie` — Verwijderd
- 🔴 `eenheid` — Verwijderd
- 🔴 `geaccordeerd` — Verwijderd
- 🔴 `gefactureerdOp` — Verwijderd
- 🔴 `gemuteerdDoor` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `opBasisVanGrondslag` — Verwijderd
- 🔴 `tarief` — Verwijderd
- 🔴 `type` — Verwijderd
- 🔴 `vastgesteldBedrag` — Verwijderd

##### `Leges_Grondslag` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aangemaaktDoor` — Verwijderd
- 🔴 `aantalOpgegeven` — Verwijderd
- 🔴 `aantalVastgesteld` — Verwijderd
- 🔴 `automatisch` — Verwijderd
- 🔴 `datumAanmaak` — Verwijderd
- 🔴 `datumMutatie` — Verwijderd
- 🔴 `eenheid` — Verwijderd
- 🔴 `gemuteerdDoor` — Verwijderd
- 🔴 `legesGrondslag` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Ligplaatsontheffing` — 🔴 Verwijderd

**Attributen:**

- 🔴 `stickernummer` — Verwijderd

##### `MORAanvraagOfMelding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `CROW` — Verwijderd
- 🔴 `locatie` — Verwijderd
- 🔴 `locatieOmschrijving` — Verwijderd
- 🔴 `meldingOmschrijving` — Verwijderd
- 🔴 `meldingTekst` — Verwijderd

##### `OpenbareActiviteit` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `evenmentnaam` — Verwijderd
- 🔴 `locatieOmschrijving` — Verwijderd
- 🔴 `status` — Verwijderd

##### `Precario` — 🔴 Verwijderd

##### `Producttype` — 🔴 Verwijderd

**Attributen:**

- 🔴 `omschrijving` — Verwijderd

##### `SubProducttype` — 🔴 Verwijderd

**Attributen:**

- 🔴 `omschrijving` — Verwijderd
- 🔴 `prioriteit` — Verwijderd

##### `Vaartuig` — 🔴 Verwijderd

**Attributen:**

- 🔴 `breedte` — Verwijderd
- 🔴 `hoogte` — Verwijderd
- 🔴 `kleur` — Verwijderd
- 🔴 `lengte` — Verwijderd
- 🔴 `naamVaartuig` — Verwijderd
- 🔴 `registratienummer` — Verwijderd

##### `VOMAanvraagOfMelding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `activiteiten` — Verwijderd
- 🔴 `adres` — Verwijderd
- 🔴 `BAGID` — Verwijderd
- 🔴 `dossiernummer` — Verwijderd
- 🔴 `intaketype` — Verwijderd
- 🔴 `internNummer` — Verwijderd
- 🔴 `kadastraleAanduiding` — Verwijderd
- 🔴 `kenmerk` — Verwijderd
- 🔴 `locatie` — Verwijderd
- 🔴 `locatieOmschrijving` — Verwijderd
- 🔴 `toelichting` — Verwijderd

##### `Vordering` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aangemaaktDoor` — Verwijderd
- 🔴 `bedragBTW` — Verwijderd
- 🔴 `datumAanmaak` — Verwijderd
- 🔴 `datumMutatie` — Verwijderd
- 🔴 `geaccordeerd` — Verwijderd
- 🔴 `geaccordeerdDoor` — Verwijderd
- 🔴 `geaccordeerdOp` — Verwijderd
- 🔴 `geexporteerd` — Verwijderd
- 🔴 `gemuteerdDoor` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `totaalbedrag` — Verwijderd
- 🔴 `totaalbedragInclusief` — Verwijderd
- 🔴 `vorderingnummer` — Verwijderd

##### `Vorderingregel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Aangemaakt_door` — Verwijderd
- 🔴 `Aanmaakdatum` — Verwijderd
- 🔴 `Bedrag_excl_btw` — Verwijderd
- 🔴 `Bedrag_incl_btw` — Verwijderd
- 🔴 `Btwcategorie` — Verwijderd
- 🔴 `Gemuteerd_door` — Verwijderd
- 🔴 `Mutatiedatum` — Verwijderd
- 🔴 `Omschrijving` — Verwijderd
- 🔴 `Periodiek` — Verwijderd
- 🔴 `Type` — Verwijderd

##### `VTH-Melding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `activiteit` — Verwijderd
- 🔴 `beoordeling` — Verwijderd
- 🔴 `datumSeponering` — Verwijderd
- 🔴 `datumtijdTot` — Verwijderd
- 🔴 `geseponeerd` — Verwijderd
- 🔴 `locatie` — Verwijderd
- 🔴 `organisatieonderdeel` — Verwijderd
- 🔴 `overtredingscode` — Verwijderd
- 🔴 `overtredingsgroep` — Verwijderd
- 🔴 `referentienummer` — Verwijderd
- 🔴 `resultaat` — Verwijderd
- 🔴 `soortVTHMelding` — Verwijderd
- 🔴 `status` — Verwijderd
- 🔴 `straatnaam` — Verwijderd
- 🔴 `taaktype` — Verwijderd
- 🔴 `zaaknummer` — Verwijderd

##### `VTHAanvraagOfMelding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `omschrijving` — Verwijderd

##### `VTHzaak` — 🔴 Verwijderd

**Attributen:**

- 🔴 `behandelaar` — Verwijderd
- 🔴 `bevoegdGezag` — Verwijderd
- 🔴 `prioritering` — Verwijderd
- 🔴 `teamBehandelaar` — Verwijderd
- 🔴 `uitvoerendeInstantie` — Verwijderd
- 🔴 `verkamering` — Verwijderd

##### `Waarneming` — 🔴 Verwijderd

##### `WABOAanvraagOfMelding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bouwkosten` — Verwijderd
- 🔴 `OLONummer` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `projectkosten` — Verwijderd
- 🔴 `registratienummer` — Verwijderd

##### `WoonfraudeAanvraagOfMelding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `adres` — Verwijderd
- 🔴 `categorie` — Verwijderd
- 🔴 `locatieOmschrijving` — Verwijderd
- 🔴 `meldingOmschrijving` — Verwijderd
- 🔴 `meldingTekst` — Verwijderd

##### `WoonoverlastAanvraagOfMelding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `locatie` — Verwijderd
- 🔴 `locatieOmschrijving` — Verwijderd
- 🔴 `meldingOmschrijving` — Verwijderd
- 🔴 `meldingTekst` — Verwijderd

#### Enumeraties

##### `Beoordelingsoort` — 🔴 Verwijderd

**Literals:**

- 🔴 `Niet Oke` — Verwijderd
- 🔴 `Niet Relevant` — Verwijderd
- 🔴 `Oke` — Verwijderd

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

##### `Heffingsoort` — 🔴 Verwijderd

**Literals:**

- 🔴 `leges` — Verwijderd
- 🔴 `precario` — Verwijderd

##### `StatusOpenbareActiviteit` — 🔴 Verwijderd

**Literals:**

- 🔴 `Aangemeld` — Verwijderd
- 🔴 `Aangevraagd` — Verwijderd
- 🔴 `Verleend` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `Activiteit Omgevingswet` «heeft» → `Leges_Grondslag`
- 🔴 Verwijderd: `Activiteit Omgevingswet` «Heeft» → `VTHzaak`
- 🔴 Verwijderd: `Bevinding` «heeft» → `Inspectie`
- 🔴 Verwijderd: `Bevinding` → `Bevinding`
- 🔴 Verwijderd: `BOA` «verbalisant» → `VTH-Melding`
- 🔴 Verwijderd: `Grondslag` «heeft» → `Leges_Grondslag`
- 🔴 Verwijderd: `Grondslag` «Heeft» → `Zaak`
- 🔴 Verwijderd: `Heffinggrondslag` «heeft» → `Activiteit Omgevingswet`
- 🔴 Verwijderd: `Heffingsverordening` «vermeld in» → `Heffinggrondslag`
- 🔴 Verwijderd: `Inspectie` «heeft» → `VTHzaak`
- 🔴 Verwijderd: `Kosten` «heeft» → `VTHzaak`
- 🔴 Verwijderd: `Leges_Grondslag` «is van» → `VTHzaak`
- 🔴 Verwijderd: `Producttype` «Heeft» → `VTHzaak`
- 🔴 Verwijderd: `SubProducttype` «heeft» → `Producttype`
- 🔴 Verwijderd: `SubProducttype` «Heeft» → `VTHzaak`
- 🔴 Verwijderd: `Vordering` «heeft» → `Vorderingregel`
- 🔴 Verwijderd: `Vordering` «heeft» → `VTHzaak`
- 🔴 Verwijderd: `Vorderingregel` «betreft» → `Kosten`
- 🔴 Verwijderd: `VTH-Melding` «betreft» → `Object`
- 🔴 Verwijderd: `VTH-Melding` «heeft» → `Foto`

#### Generalisaties

- 🔴 Verwijderd: `Combibon` ⟶ `VTH-Melding`
- 🔴 Verwijderd: `Fietsregistratie` ⟶ `VTH-Melding`
- 🔴 Verwijderd: `Heffingsverordening` ⟶ `Document`
- 🔴 Verwijderd: `Indiener` ⟶ `Rechtspersoon`
- 🔴 Verwijderd: `MORAanvraagOfMelding` ⟶ `AanvraagOfMelding`
- 🔴 Verwijderd: `VOMAanvraagOfMelding` ⟶ `AanvraagOfMelding`
- 🔴 Verwijderd: `VTH-Melding` ⟶ `AanvraagOfMelding`
- 🔴 Verwijderd: `VTHAanvraagOfMelding` ⟶ `VOMAanvraagOfMelding`
- 🔴 Verwijderd: `VTHzaak` ⟶ `Zaak`
- 🔴 Verwijderd: `Waarneming` ⟶ `VTH-Melding`
- 🔴 Verwijderd: `WABOAanvraagOfMelding` ⟶ `VOMAanvraagOfMelding`
- 🔴 Verwijderd: `WoonfraudeAanvraagOfMelding` ⟶ `AanvraagOfMelding`
- 🔴 Verwijderd: `WoonoverlastAanvraagOfMelding` ⟶ `AanvraagOfMelding`

<a id="structureel-delfts-gemeentelijk-gegevensmodel10-dienstverleningmodel-dienstverlening"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/10 Dienstverlening/Model Dienstverlening

#### Classes

##### `Aanvraagdata` — 🔴 Verwijderd

**Attributen:**

- 🔴 `data` — Verwijderd
- 🔴 `veld` — Verwijderd

##### `AanvraagOfMelding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `afgehandeld` — Verwijderd
- 🔴 `categorie` — Verwijderd
- 🔴 `categoriecode` — Verwijderd
- 🔴 `datumAanmaak` — Verwijderd
- 🔴 `datumAfhandeling` — Verwijderd
- 🔴 `datumBeginStatus` — Verwijderd
- 🔴 `datumEindeStatus` — Verwijderd
- 🔴 `hoofdcategorie` — Verwijderd
- 🔴 `hoofdcategoriecode` — Verwijderd
- 🔴 `identificatie` — Verwijderd
- 🔴 `kanaal` — Verwijderd
- 🔴 `onderwerp` — Verwijderd
- 🔴 `onderwerpcode` — Verwijderd
- 🔴 `soort` — Verwijderd
- 🔴 `status` — Verwijderd
- 🔴 `statuscode` — Verwijderd
- 🔴 `statusVolgorde` — Verwijderd
- 🔴 `subcategorie` — Verwijderd
- 🔴 `subcategoriecode` — Verwijderd

##### `Afspraakstatus` — 🔴 Verwijderd

**Attributen:**

- 🔴 `status` — Verwijderd

##### `Artikel` — 🔴 Verwijderd

##### `Balieafspraak` — 🔴 Verwijderd

**Attributen:**

- 🔴 `eindtijdGepland` — Verwijderd
- 🔴 `notitie` — Verwijderd
- 🔴 `starttijdGepland` — Verwijderd
- 🔴 `tijdAangemaakt` — Verwijderd
- 🔴 `tijdsduurGepland` — Verwijderd
- 🔴 `toelichting` — Verwijderd
- 🔴 `wachttijdNaStartAfspraak` — Verwijderd
- 🔴 `wachttijdTotaal` — Verwijderd
- 🔴 `wachttijdVoorStartAfspraak` — Verwijderd
- 🔴 `werkelijkeTijdsduur` — Verwijderd

##### `ExterneBron` — 🔴 Verwijderd

##### `Formuliersoort` — 🔴 Verwijderd

**Attributen:**

- 🔴 `ingebruik` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `onderwerp` — Verwijderd

##### `Formuliersoortveld` — 🔴 Verwijderd

**Attributen:**

- 🔴 `helptekst` — Verwijderd
- 🔴 `isVerplicht` — Verwijderd
- 🔴 `label` — Verwijderd
- 🔴 `maxLengte` — Verwijderd
- 🔴 `veldnaam` — Verwijderd
- 🔴 `veldtype` — Verwijderd

##### `Klantbeoordeling` — 🔴 Verwijderd

**Attributen:**

- 🔴 `beoordeling` — Verwijderd
- 🔴 `categorie` — Verwijderd
- 🔴 `contactOpnemen` — Verwijderd
- 🔴 `ddBeoordeling` — Verwijderd
- 🔴 `kanaal` — Verwijderd
- 🔴 `onderwerp` — Verwijderd
- 🔴 `subCategorie` — Verwijderd

##### `Klantbeoordelingreden` — 🔴 Verwijderd

**Attributen:**

- 🔴 `reden` — Verwijderd

##### `MOR-AanvraagOfMelding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `locatie` — Verwijderd
- 🔴 `locatieOmschrijving` — Verwijderd
- 🔴 `meldingOmschrijving` — Verwijderd
- 🔴 `meldingTekst` — Verwijderd

##### `Onderwerp` — 🔴 Verwijderd

**Attributen:**

- 🔴 `isActief` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `toelichting` — Verwijderd

##### `ProductOfDienst` — 🔴 Verwijderd

**Attributen:**

- 🔴 `afhandeltijd` — Verwijderd
- 🔴 `ingebruik` — Verwijderd
- 🔴 `naam` — Verwijderd

##### `Telefoononderwerp` — 🔴 Verwijderd

**Attributen:**

- 🔴 `onderwerp` — Verwijderd

##### `Telefoonstatus` — 🔴 Verwijderd

**Attributen:**

- 🔴 `contactConnectionState` — Verwijderd
- 🔴 `status` — Verwijderd

##### `Telefoontje` — 🔴 Verwijderd

**Attributen:**

- 🔴 `afhandeltijdNaGesprek` — Verwijderd
- 🔴 `deltaISDNConnectie` — Verwijderd
- 🔴 `eindtijd` — Verwijderd
- 🔴 `starttijd` — Verwijderd
- 🔴 `totaleOnHoldTijd` — Verwijderd
- 🔴 `totaleSpreektijd` — Verwijderd
- 🔴 `totaleTijdsduur` — Verwijderd
- 🔴 `totaleWachttijd` — Verwijderd
- 🔴 `trackID` — Verwijderd

#### Enumeraties

##### `Boolean` — 🔴 Verwijderd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `Aanvraagdata` «is conform» → `Formuliersoortveld`
- 🔴 Verwijderd: `AanvraagOfMelding` «aanvraag met» → `Formuliersoort`
- 🔴 Verwijderd: `AanvraagOfMelding` «betreft» → `Onderwerp`
- 🔴 Verwijderd: `AanvraagOfMelding` «heeft data» → `Aanvraagdata`
- 🔴 Verwijderd: `AanvraagOfMelding` «heeft documenten» → `Document`
- 🔴 Verwijderd: `AanvraagOfMelding` «heeft» → `AOMStatus`
- 🔴 Verwijderd: `AanvraagOfMelding` «ingediend door» → `Indiener`
- 🔴 Verwijderd: `AanvraagOfMelding` «kan leiden tot» → `Zaak`
- 🔴 Verwijderd: `AanvraagOfMelding` «melder» → `Rechtspersoon`
- 🔴 Verwijderd: `Balieafspraak` «betreft» → `ProductOfDienst`
- 🔴 Verwijderd: `Balieafspraak` «heeft betrekking op» → `Zaak`
- 🔴 Verwijderd: `Balieafspraak` «heeft» → `Afspraakstatus`
- 🔴 Verwijderd: `Balieafspraak` «locatie» → `VestigingVanZaakbehandelendeOrganisatie`
- 🔴 Verwijderd: `Balieafspraak` «met» → `Medewerker`
- 🔴 Verwijderd: `Balieafspraak` «mondt uit in» → `Klantcontact`
- 🔴 Verwijderd: `Formuliersoort` «heeft velden» → `Formuliersoortveld`
- 🔴 Verwijderd: `Formuliersoort` «is aanleiding voor» → `Zaaktype`
- 🔴 Verwijderd: `Klantbeoordeling` «heeft» → `Klantbeoordelingreden`
- 🔴 Verwijderd: `Onderwerp` «hoofdonderwerp» → `Onderwerp`
- 🔴 Verwijderd: `ProductOfDienst` «heeft» → `Klantbeoordeling`
- 🔴 Verwijderd: `Telefoononderwerp` «heeft» → `Klantcontact`
- 🔴 Verwijderd: `Telefoononderwerp` «heeft» → `Telefoontje`
- 🔴 Verwijderd: `Telefoontje` «heeft» → `Telefoonstatus`
- 🔴 Verwijderd: `Telefoontje` «mondt uit in» → `Klantcontact`

#### Generalisaties

- 🔴 Verwijderd: `MOR-AanvraagOfMelding` ⟶ `AanvraagOfMelding`

<a id="structureel-delfts-gemeentelijk-gegevensmodel2-verkeer-vervoer-en-waterstaatmobiliteitmodel-mobiliteit"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/2 Verkeer, Vervoer en Waterstaat/Mobiliteit/Model Mobiliteit

#### Classes

##### `Stremming` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aantalGehinderden` — Verwijderd
- 🔴 `datumAanmelding` — Verwijderd
- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `datumWijziging` — Verwijderd
- 🔴 `delenToegestaan` — Verwijderd
- 🔴 `geschiktVoorPublicatie` — Verwijderd
- 🔴 `hinderklasse` — Verwijderd
- 🔴 `locatie` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `status` — Verwijderd

##### `Strooidag` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datum` — Verwijderd
- 🔴 `maximumtemperatuur` — Verwijderd
- 🔴 `minimumtemperatuur` — Verwijderd
- 🔴 `tijdMaximumtemperatuur` — Verwijderd
- 🔴 `tijdMinimumtemperatuur` — Verwijderd

##### `Strooiroute` — 🔴 Verwijderd

**Attributen:**

- 🔴 `route` — Verwijderd

##### `StrooirouteUitvoering` — 🔴 Verwijderd

**Attributen:**

- 🔴 `geplandEinde` — Verwijderd
- 🔴 `geplandStart` — Verwijderd
- 🔴 `route` — Verwijderd
- 🔴 `werkelijkEinde` — Verwijderd
- 🔴 `werkelijkeStart` — Verwijderd

##### `Verkeersbesluit` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBesluit` — Verwijderd
- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `huisnummer` — Verwijderd
- 🔴 `postcode` — Verwijderd
- 🔴 `referentienummer` — Verwijderd
- 🔴 `straat` — Verwijderd
- 🔴 `titel` — Verwijderd

##### `Verkeerstelling` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aantal` — Verwijderd
- 🔴 `tijdTot` — Verwijderd
- 🔴 `tijdVanaf` — Verwijderd

##### `VLogInfo` — 🔴 Verwijderd

**Attributen:**

- 🔴 `detectieVerkeer` — Verwijderd
- 🔴 `eindegroen` — Verwijderd
- 🔴 `snelheid` — Verwijderd
- 🔴 `startgroen` — Verwijderd
- 🔴 `tijdstip` — Verwijderd
- 🔴 `verkeerWilGroen` — Verwijderd
- 🔴 `wachttijd` — Verwijderd

#### Enumeraties

##### `Aantal Gehinderden` — 🔴 Verwijderd

**Literals:**

- 🔴 `1.000 tot 10.000` — Verwijderd
- 🔴 `10.000 tot 100.000` — Verwijderd
- 🔴 `100.000 tot 1.000.000` — Verwijderd
- 🔴 `meer dan 1.000.000` — Verwijderd
- 🔴 `minder dan 1000` — Verwijderd

##### `Hindercategorie` — 🔴 Verwijderd

**Literals:**

- 🔴 `A` — Verwijderd
- 🔴 `B` — Verwijderd
- 🔴 `C` — Verwijderd
- 🔴 `D` — Verwijderd
- 🔴 `E` — Verwijderd

##### `Hinderklasse` — 🔴 Verwijderd

**Literals:**

- 🔴 `Klasse 0: Geen hinder` — Verwijderd
- 🔴 `Klasse 1: Kleine hinder` — Verwijderd
- 🔴 `Klasse 2: Matige hinder` — Verwijderd
- 🔴 `Klasse 3: Grote hinder` — Verwijderd
- 🔴 `Klasse 4: Zeer grote hinder` — Verwijderd

##### `Stremmingstatus` — 🔴 Verwijderd

**Literals:**

- 🔴 `Aangemeld` — Verwijderd
- 🔴 `Afgerond` — Verwijderd
- 🔴 `Gepulbliceerd` — Verwijderd
- 🔴 `In Uitvoering` — Verwijderd
- 🔴 `Plan Afhandelen` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `Stremming` «betreft» → `Wegdeel`
- 🔴 Verwijderd: `StrooirouteUitvoering` «uitvoering op» → `Strooidag`
- 🔴 Verwijderd: `StrooirouteUitvoering` «volgens» → `Strooiroute`
- 🔴 Verwijderd: `Verkeersbesluit` «is vastgelegd in» → `Document`

<a id="structureel-delfts-gemeentelijk-gegevensmodel2-verkeer-vervoer-en-waterstaatparkerenmodel-parkeren"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/2 Verkeer, Vervoer en Waterstaat/Parkeren/Model Parkeren

#### Classes

##### `Belprovider` — 🔴 Verwijderd

**Attributen:**

- 🔴 `code` — Verwijderd

##### `MulderFeit` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bedrag` — Verwijderd
- 🔴 `bezwaarAfgehandeld` — Verwijderd
- 🔴 `bezwaarIngetrokken` — Verwijderd
- 🔴 `bezwaarToegewezen` — Verwijderd
- 🔴 `bonnummer` — Verwijderd
- 🔴 `datumBetaling` — Verwijderd
- 🔴 `datumBezwaar` — Verwijderd
- 🔴 `datumGeseponeerd` — Verwijderd
- 🔴 `datumIndiening` — Verwijderd
- 🔴 `dienstCD` — Verwijderd
- 🔴 `organisatie` — Verwijderd
- 🔴 `overtreding` — Verwijderd
- 🔴 `parkeertarief` — Verwijderd
- 🔴 `redenSeponeren` — Verwijderd
- 🔴 `vorderingnummer` — Verwijderd

##### `Naheffing` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bedrag` — Verwijderd
- 🔴 `bezwaarAfgehandeld` — Verwijderd
- 🔴 `bezwaarIngetrokken` — Verwijderd
- 🔴 `bezwaarToegewezen` — Verwijderd
- 🔴 `bonnummer` — Verwijderd
- 🔴 `datumBetaling` — Verwijderd
- 🔴 `datumBezwaar` — Verwijderd
- 🔴 `datumGeseponeerd` — Verwijderd
- 🔴 `datumIndiening` — Verwijderd
- 🔴 `dienstCD` — Verwijderd
- 🔴 `fiscaal` — Verwijderd
- 🔴 `organisatie` — Verwijderd
- 🔴 `overtreding` — Verwijderd
- 🔴 `parkeertarief` — Verwijderd
- 🔴 `redenSeponeren` — Verwijderd
- 🔴 `vorderingnummer` — Verwijderd

##### `Parkeergarage` — 🔴 Verwijderd

##### `Parkeerrecht` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aanmaaktijd` — Verwijderd
- 🔴 `bedragAankoop` — Verwijderd
- 🔴 `bedragBTW` — Verwijderd
- 🔴 `datumtijdEinde` — Verwijderd
- 🔴 `datumtijdStart` — Verwijderd
- 🔴 `productnaam` — Verwijderd
- 🔴 `productomschrijving` — Verwijderd

##### `Parkeerscan` — 🔴 Verwijderd

**Attributen:**

- 🔴 `codeGebruiker` — Verwijderd
- 🔴 `codeScanvoertuig` — Verwijderd
- 🔴 `coordinaten` — Verwijderd
- 🔴 `foto` — Verwijderd
- 🔴 `kenteken` — Verwijderd
- 🔴 `parkeerrecht` — Verwijderd
- 🔴 `tijdstip` — Verwijderd
- 🔴 `transactieID` — Verwijderd

##### `Parkeervergunning` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumEindeGeldigheid` — Verwijderd
- 🔴 `datumReservering` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `kenteken` — Verwijderd
- 🔴 `minutenAfgeschreven` — Verwijderd
- 🔴 `minutenGeldig` — Verwijderd
- 🔴 `minutenResterend` — Verwijderd
- 🔴 `nummer` — Verwijderd
- 🔴 `type` — Verwijderd

##### `Parkeervlak` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aantal` — Verwijderd
- 🔴 `coordinaten` — Verwijderd
- 🔴 `doelgroep` — Verwijderd
- 🔴 `fiscaal` — Verwijderd
- 🔴 `plaats` — Verwijderd
- 🔴 `vlakID` — Verwijderd

##### `Parkeerzone` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aantalParkeervlakken` — Verwijderd
- 🔴 `alleenDagtarief` — Verwijderd
- 🔴 `dagtarief` — Verwijderd
- 🔴 `eindedag` — Verwijderd
- 🔴 `eindtijd` — Verwijderd
- 🔴 `gebruik` — Verwijderd
- 🔴 `geometrie` — Verwijderd
- 🔴 `IPMCode` — Verwijderd
- 🔴 `IPMNaam` — Verwijderd
- 🔴 `isParkeergarage` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `sectorcode` — Verwijderd
- 🔴 `soortCode` — Verwijderd
- 🔴 `startdag` — Verwijderd
- 🔴 `starttarief` — Verwijderd
- 🔴 `starttijd` — Verwijderd
- 🔴 `typeCode` — Verwijderd
- 🔴 `typeNaam` — Verwijderd
- 🔴 `uurtarief` — Verwijderd

##### `Productgroep` — 🔴 Verwijderd

**Attributen:**

- 🔴 `beslisboom` — Verwijderd
- 🔴 `code` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Productsoort` — 🔴 Verwijderd

**Attributen:**

- 🔴 `code` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `tarief` — Verwijderd
- 🔴 `tariefperiode` — Verwijderd

##### `Straatsectie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `code` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `zoneCode` — Verwijderd

##### `Voertuig` — 🔴 Verwijderd

**Attributen:**

- 🔴 `kenteken` — Verwijderd
- 🔴 `kleur` — Verwijderd
- 🔴 `land` — Verwijderd
- 🔴 `merk` — Verwijderd
- 🔴 `type` — Verwijderd

#### Enumeraties

##### `Boolean` — 🔴 Verwijderd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `Doelgroepenplaatsen` — 🔴 Verwijderd

**Literals:**

- 🔴 `DP01` — Verwijderd
- 🔴 `DP02` — Verwijderd
- 🔴 `DP03` — Verwijderd
- 🔴 `DP04` — Verwijderd
- 🔴 `DP05` — Verwijderd
- 🔴 `Leeg` — Verwijderd

##### `Zonesoort` — 🔴 Verwijderd

**Literals:**

- 🔴 `GSM-Zone` — Verwijderd
- 🔴 `Vergunninghouderzone` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `MulderFeit` «betreft voertuig» → `Voertuig`
- 🔴 Verwijderd: `Parkeerrecht` «betreft» → `Parkeerzone`
- 🔴 Verwijderd: `Parkeerrecht` «betreft» → `Voertuig`
- 🔴 Verwijderd: `Parkeerrecht` «leverancier» → `Belprovider`
- 🔴 Verwijderd: `Parkeerscan` «betreft» → `Parkeervlak`
- 🔴 Verwijderd: `Parkeerscan` «betreft» → `Voertuig`
- 🔴 Verwijderd: `Parkeerscan` «komt voort uit» → `Naheffing`
- 🔴 Verwijderd: `Parkeerscan` «uitgevoerd door» → `Medewerker`
- 🔴 Verwijderd: `Parkeerscan` «verificatie» → `Parkeerrecht`
- 🔴 Verwijderd: `Parkeervergunning` «geldig voor» → `Parkeerzone`
- 🔴 Verwijderd: `Parkeervergunning` «houder» → `Rechtspersoon`
- 🔴 Verwijderd: `Parkeervergunning` «resulteert» → `Parkeerrecht`
- 🔴 Verwijderd: `Parkeervergunning` → `Ingezetene`
- 🔴 Verwijderd: `Parkeerzone` «bevat» → `Parkeervlak`
- 🔴 Verwijderd: `Parkeerzone` «bevat» → `Straatsectie`
- 🔴 Verwijderd: `Productgroep` «soort» → `Parkeervergunning`
- 🔴 Verwijderd: `Productsoort` «soort» → `Parkeervergunning`
- 🔴 Verwijderd: `Productsoort` «valt binnen» → `Productgroep`
- 🔴 Verwijderd: `Straatsectie` «bevat» → `Parkeervlak`

#### Generalisaties

- 🔴 Verwijderd: `Belprovider` ⟶ `Leverancier`
- 🔴 Verwijderd: `Parkeergarage` ⟶ `Parkeerzone`

<a id="structureel-delfts-gemeentelijk-gegevensmodel3-economiediagram"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/3 Economie/Diagram

#### Classes

##### `ProxyConnector` — 🔴 Verwijderd

##### `ProxyConnector` — 🔴 Verwijderd

#### Associaties

- 🔴 Verwijderd: `ProxyConnector` → `ProxyConnector`

<a id="structureel-delfts-gemeentelijk-gegevensmodel3-economiemodel-economie"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/3 Economie/Model Economie

#### Classes

##### `Contact` — 🔴 Verwijderd

**Attributen:**

- 🔴 `contactsoort` — Verwijderd
- 🔴 `datum` — Verwijderd
- 🔴 `tekst` — Verwijderd

##### `Hotel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aantalKamers` — Verwijderd

##### `Hotelbezoek` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumStart` — Verwijderd

##### `Verkooppunt` — 🔴 Verwijderd

**Attributen:**

- 🔴 `winkelformule` — Verwijderd

##### `Werkgelegenheid` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aantalFulltimeMannen` — Verwijderd
- 🔴 `aantalFulltimeVrouwen` — Verwijderd
- 🔴 `aantalParttimeMannen` — Verwijderd
- 🔴 `aantalParttimeVrouwen` — Verwijderd
- 🔴 `grootteklasse` — Verwijderd

##### `Winkelvloeroppervlak` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aantalKassa` — Verwijderd
- 🔴 `bronWVO` — Verwijderd
- 🔴 `leegstand` — Verwijderd
- 🔴 `winkelvloeroppervlakte` — Verwijderd
- 🔴 `WVOKlasse` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `Contact` «bij» → `Vestiging`
- 🔴 Verwijderd: `Contact` «met» → `NatuurlijkPersoon`
- 🔴 Verwijderd: `Hotel` «heeft» → `Hotelbezoek`

#### Generalisaties

- 🔴 Verwijderd: `Hotel` ⟶ `Vestiging`
- 🔴 Verwijderd: `Verkooppunt` ⟶ `Vestiging`

<a id="structureel-delfts-gemeentelijk-gegevensmodel4-onderwijsleerplicht-en-leerlingenvervoermodel-leerplicht-en-leerlingenvervoer"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/4 Onderwijs/Leerplicht en Leerlingenvervoer/Model Leerplicht en Leerlingenvervoer

#### Classes

##### `Aanvraag Leerlingenvervoer` — 🔴 Verwijderd

##### `AanvraagOfMelding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datum` — Verwijderd
- 🔴 `opmerkingen` — Verwijderd
- 🔴 `reden` — Verwijderd
- 🔴 `soortVerzuimOfAanvraag` — Verwijderd

##### `AanvraagVrijstelling` — 🔴 Verwijderd

**Attributen:**

- 🔴 `buitenlandseSchoollocatie` — Verwijderd
- 🔴 `datumAanvraag` — Verwijderd

##### `Beschikking Leerlingenvervoer` — 🔴 Verwijderd

##### `Beslissing` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datum` — Verwijderd
- 🔴 `opmerkingen` — Verwijderd
- 🔴 `reden` — Verwijderd

##### `Doorgeleiding OM` — 🔴 Verwijderd

**Attributen:**

- 🔴 `afdoening` — Verwijderd

##### `HALT-verwijzing` — 🔴 Verwijderd

**Attributen:**

- 🔴 `afdoening` — Verwijderd
- 🔴 `datumMutatie` — Verwijderd
- 🔴 `datumRetour` — Verwijderd
- 🔴 `memo` — Verwijderd

##### `Klacht Leerlingenvervoer` — 🔴 Verwijderd

##### `Leerplichtambtenaar` — 🔴 Verwijderd

##### `Procesverbaal Onderwijs` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumAfgehandeld` — Verwijderd
- 🔴 `datumEindeProeftijd` — Verwijderd
- 🔴 `datumIngelicht` — Verwijderd
- 🔴 `datumUitspraak` — Verwijderd
- 🔴 `datumZitting` — Verwijderd
- 🔴 `geldboete` — Verwijderd
- 🔴 `geldboeteVoorwaardelijk` — Verwijderd
- 🔴 `opmerkingen` — Verwijderd
- 🔴 `proeftijd` — Verwijderd
- 🔴 `reden` — Verwijderd
- 🔴 `sanctiesoort` — Verwijderd
- 🔴 `uitspraak` — Verwijderd
- 🔴 `verzuimsoort` — Verwijderd

##### `Verlofaanvraag` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumStart` — Verwijderd
- 🔴 `datumTot` — Verwijderd
- 🔴 `soortVerlof` — Verwijderd

##### `Vervoerder` — 🔴 Verwijderd

##### `Verzuimmelding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `voorstelSchool` — Verwijderd

##### `Vrijstelling` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aanvraagToegekend` — Verwijderd
- 🔴 `buitenlandseSchoollocatie` — Verwijderd
- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `verzuimsoort` — Verwijderd

##### `Ziekmelding Leerlingenvervoer` — 🔴 Verwijderd

#### Enumeraties

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

##### `Sanctiesoort` — 🔴 Verwijderd

##### `Verzuimsoort` — 🔴 Verwijderd

**Literals:**

- 🔴 `absoluut` — Verwijderd
- 🔴 `relatief` — Verwijderd

##### `Vrijstellingsoort` — 🔴 Verwijderd

#### Associaties

- 🔴 Verwijderd: `AanvraagOfMelding` «betreft» → `Leerling`
- 🔴 Verwijderd: `AanvraagOfMelding` «betreft» → `School`
- 🔴 Verwijderd: `AanvraagOfMelding` «leidt tot» → `Beslissing`
- 🔴 Verwijderd: `Beschikking Leerlingenvervoer` «vervoerder» → `Vervoerder`
- 🔴 Verwijderd: `Beslissing` «behandelaar» → `Leerplichtambtenaar`
- 🔴 Verwijderd: `Beslissing` «betreft» → `Leerling`
- 🔴 Verwijderd: `Beslissing` «betreft» → `School`
- 🔴 Verwijderd: `Doorgeleiding OM` «verantwoordelijk ouder» → `Ouder Of Verzorger`
- 🔴 Verwijderd: `Klacht Leerlingenvervoer` «betreft» → `Leerling`
- 🔴 Verwijderd: `Klacht Leerlingenvervoer` «betreft» → `Vervoerder`
- 🔴 Verwijderd: `Leerplichtambtenaar` «opgelegd door» → `Procesverbaal Onderwijs`
- 🔴 Verwijderd: `Procesverbaal Onderwijs` «verantwoordelijke ouder» → `Ouder Of Verzorger`
- 🔴 Verwijderd: `Verzuimmelding` «heeft» → `School`
- 🔴 Verwijderd: `Vrijstelling` «heeft» → `School`

#### Generalisaties

- 🔴 Verwijderd: `AanvraagOfMelding` ⟶ `AanvraagOfMelding`
- 🔴 Verwijderd: `AanvraagVrijstelling` ⟶ `AanvraagOfMelding`
- 🔴 Verwijderd: `Beschikking Leerlingenvervoer` ⟶ `Beslissing`
- 🔴 Verwijderd: `Doorgeleiding OM` ⟶ `Beslissing`
- 🔴 Verwijderd: `HALT-verwijzing` ⟶ `Beslissing`
- 🔴 Verwijderd: `Leerplichtambtenaar` ⟶ `Medewerker`
- 🔴 Verwijderd: `Procesverbaal Onderwijs` ⟶ `Beslissing`
- 🔴 Verwijderd: `Verlofaanvraag` ⟶ `AanvraagOfMelding`
- 🔴 Verwijderd: `Vervoerder` ⟶ `Leverancier`
- 🔴 Verwijderd: `Verzuimmelding` ⟶ `AanvraagOfMelding`
- 🔴 Verwijderd: `Vrijstelling` ⟶ `Beslissing`

<a id="structureel-delfts-gemeentelijk-gegevensmodel4-onderwijsonderwijsmodel-onderwijs"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/4 Onderwijs/Onderwijs/Model Onderwijs

#### Classes

##### `Inschrijving` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datum` — Verwijderd

##### `Leerjaar` — 🔴 Verwijderd

**Attributen:**

- 🔴 `jaarEinde` — Verwijderd
- 🔴 `jaarStart` — Verwijderd

##### `Leerling` — 🔴 Verwijderd

**Attributen:**

- 🔴 `kwetsbareJongere` — Verwijderd

##### `Locatie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `adres` — Verwijderd

##### `Loopbaanstap` — 🔴 Verwijderd

**Attributen:**

- 🔴 `klas` — Verwijderd
- 🔴 `onderwijstype` — Verwijderd
- 🔴 `schooljaar` — Verwijderd

##### `Onderwijsloopbaan` — 🔴 Verwijderd

##### `Onderwijsniveau` — 🔴 Verwijderd

##### `Onderwijssoort` — 🔴 Verwijderd

**Attributen:**

- 🔴 `omschrijving` — Verwijderd
- 🔴 `onderwijstype` — Verwijderd

##### `Ouder Of Verzorger` — 🔴 Verwijderd

##### `School` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd

##### `Startkwalificatie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBehaald` — Verwijderd

##### `Uitschrijving` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datum` — Verwijderd
- 🔴 `diplomaBehaald` — Verwijderd

#### Enumeraties

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

##### `Onderwijstype` — 🔴 Verwijderd

**Literals:**

- 🔴 `HAVO` — Verwijderd
- 🔴 `VMBO-B` — Verwijderd
- 🔴 `VMBO-K` — Verwijderd
- 🔴 `VMBO-T` — Verwijderd
- 🔴 `VWO` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `Inschrijving` «heeft» → `School`
- 🔴 Verwijderd: `Leerling` «betreft leerling» → `Procesverbaal Onderwijs`
- 🔴 Verwijderd: `Leerling` «betreft» → `Ziekmelding Leerlingenvervoer`
- 🔴 Verwijderd: `Leerling` «heeft» → `Inschrijving`
- 🔴 Verwijderd: `Leerling` «heeft» → `Onderwijsloopbaan`
- 🔴 Verwijderd: `Leerling` «heeft» → `Startkwalificatie`
- 🔴 Verwijderd: `Leerling` «heeft» → `Uitschrijving`
- 🔴 Verwijderd: `Leerling` «heeft» → `Verzuimmelding`
- 🔴 Verwijderd: `Leerling` «heeft» → `Vrijstelling`
- 🔴 Verwijderd: `Onderwijsloopbaan` → `Loopbaanstap`
- 🔴 Verwijderd: `School` «gebruikt» → `Sportlocatie`
- 🔴 Verwijderd: `School` «heeft» → `Onderwijssoort`
- 🔴 Verwijderd: `School` «heeft» → `Uitschrijving`
- 🔴 Verwijderd: `School` «kent» → `Onderwijsloopbaan`
- 🔴 Verwijderd: `School` «school heeft» → `Locatie`

#### Generalisaties

- 🔴 Verwijderd: `Leerling` ⟶ `IngeschrevenPersoon`
- 🔴 Verwijderd: `Locatie` ⟶ `Vastgoedobject`
- 🔴 Verwijderd: `Ouder Of Verzorger` ⟶ `IngeschrevenPersoon`
- 🔴 Verwijderd: `School` ⟶ `NietNatuurlijkPersoon`
- 🔴 Verwijderd: `School` ⟶ `NietNatuurlijkPersoon`

<a id="structureel-delfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatieerfgoedarcheologiemodel-archeologie"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Erfgoed/Archeologie/Model Archeologie

#### Classes

##### `Archeologiebesluit` — 🔴 Verwijderd

##### `Artefact` — 🔴 Verwijderd

**Attributen:**

- 🔴 `artefectnummer` — Verwijderd
- 🔴 `beschrijving` — Verwijderd
- 🔴 `conserveren` — Verwijderd
- 🔴 `datering` — Verwijderd
- 🔴 `dateringComplex` — Verwijderd
- 🔴 `determinatieniveau` — Verwijderd
- 🔴 `dianummer` — Verwijderd
- 🔴 `doosnummer` — Verwijderd
- 🔴 `exposabel` — Verwijderd
- 🔴 `fotonummer` — Verwijderd
- 🔴 `functie` — Verwijderd
- 🔴 `herkomst` — Verwijderd
- 🔴 `key` — Verwijderd
- 🔴 `keyDoos` — Verwijderd
- 🔴 `keyMagazijnplaatsing` — Verwijderd
- 🔴 `keyPut` — Verwijderd
- 🔴 `keyVondst` — Verwijderd
- 🔴 `literatuur` — Verwijderd
- 🔴 `maten` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `opmerkingen` — Verwijderd
- 🔴 `origine` — Verwijderd
- 🔴 `projectCD` — Verwijderd
- 🔴 `putnummer` — Verwijderd
- 🔴 `restauratieWenselijk` — Verwijderd
- 🔴 `tekeningnummer` — Verwijderd
- 🔴 `type` — Verwijderd
- 🔴 `vondstnummer` — Verwijderd

##### `Artefactsoort` — 🔴 Verwijderd

**Attributen:**

- 🔴 `code` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `boring` — 🔴 Verwijderd

##### `Doos` — 🔴 Verwijderd

**Attributen:**

- 🔴 `doosnummer` — Verwijderd
- 🔴 `herkomst` — Verwijderd
- 🔴 `inhoud` — Verwijderd
- 🔴 `key` — Verwijderd
- 🔴 `keyMagazijnlocatie` — Verwijderd
- 🔴 `projectCD` — Verwijderd

##### `Kaart` — 🔴 Verwijderd

**Attributen:**

- 🔴 `content` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `locatie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `locatiePunt` — Verwijderd

##### `Magazijnlocatie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `key` — Verwijderd
- 🔴 `stelling` — Verwijderd
- 🔴 `vaknummer` — Verwijderd
- 🔴 `volgletter` — Verwijderd

##### `Magazijnplaatsing` — 🔴 Verwijderd

**Attributen:**

- 🔴 `beschrijving` — Verwijderd
- 🔴 `datumGeplaatst` — Verwijderd
- 🔴 `herkomst` — Verwijderd
- 🔴 `key` — Verwijderd
- 🔴 `keyDoos` — Verwijderd
- 🔴 `keyMagazijnlocatie` — Verwijderd
- 🔴 `projectCD` — Verwijderd
- 🔴 `uitgeleend` — Verwijderd

##### `Project` — 🔴 Verwijderd

**Attributen:**

- 🔴 `coordinaten` — Verwijderd
- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `jaarTot` — Verwijderd
- 🔴 `jaarVan` — Verwijderd
- 🔴 `locatie` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `naamcode` — Verwijderd
- 🔴 `projectCD` — Verwijderd
- 🔴 `toponiem` — Verwijderd
- 🔴 `trefwoorden` — Verwijderd

##### `Put` — 🔴 Verwijderd

**Attributen:**

- 🔴 `key` — Verwijderd
- 🔴 `projectCD` — Verwijderd
- 🔴 `putnummer` — Verwijderd

##### `Spoor` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aard` — Verwijderd
- 🔴 `beschrijving` — Verwijderd
- 🔴 `datering` — Verwijderd
- 🔴 `datum` — Verwijderd
- 🔴 `hoogteBoven` — Verwijderd
- 🔴 `hoogteOnder` — Verwijderd
- 🔴 `key` — Verwijderd
- 🔴 `keyVlak` — Verwijderd
- 🔴 `projectCD` — Verwijderd
- 🔴 `putnummer` — Verwijderd
- 🔴 `spoornummer` — Verwijderd
- 🔴 `vlaknummer` — Verwijderd
- 🔴 `vorm` — Verwijderd

##### `Stelling` — 🔴 Verwijderd

**Attributen:**

- 🔴 `inhoud` — Verwijderd
- 🔴 `stellingcode` — Verwijderd

##### `Vindplaats` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aard` — Verwijderd
- 🔴 `begindatering` — Verwijderd
- 🔴 `beschrijving` — Verwijderd
- 🔴 `bibliografie` — Verwijderd
- 🔴 `datering` — Verwijderd
- 🔴 `depot` — Verwijderd
- 🔴 `documentatie` — Verwijderd
- 🔴 `einddatering` — Verwijderd
- 🔴 `gemeente` — Verwijderd
- 🔴 `locatie` — Verwijderd
- 🔴 `mobilia` — Verwijderd
- 🔴 `onderzoek` — Verwijderd
- 🔴 `projectcode` — Verwijderd
- 🔴 `vindplaatsOmschrijving` — Verwijderd

##### `Vlak` — 🔴 Verwijderd

**Attributen:**

- 🔴 `diepteTot` — Verwijderd
- 🔴 `diepteVan` — Verwijderd
- 🔴 `key` — Verwijderd
- 🔴 `keyPut` — Verwijderd
- 🔴 `projectCD` — Verwijderd
- 🔴 `putnummer` — Verwijderd
- 🔴 `vlaknummer` — Verwijderd

##### `Vondst` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datum` — Verwijderd
- 🔴 `key` — Verwijderd
- 🔴 `keyVulling` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `omstandigheden` — Verwijderd
- 🔴 `projectCD` — Verwijderd
- 🔴 `putnummer` — Verwijderd
- 🔴 `spoornummer` — Verwijderd
- 🔴 `vlaknummer` — Verwijderd
- 🔴 `vondstnummer` — Verwijderd
- 🔴 `vullingnummer` — Verwijderd
- 🔴 `XCoordinaat` — Verwijderd
- 🔴 `YCoordinaat` — Verwijderd

##### `Vulling` — 🔴 Verwijderd

**Attributen:**

- 🔴 `grondsoort` — Verwijderd
- 🔴 `key` — Verwijderd
- 🔴 `keySpoor` — Verwijderd
- 🔴 `kleur` — Verwijderd
- 🔴 `projectCD` — Verwijderd
- 🔴 `putnummer` — Verwijderd
- 🔴 `spoornummer` — Verwijderd
- 🔴 `structuur` — Verwijderd
- 🔴 `vlaknummer` — Verwijderd
- 🔴 `vullingnummer` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `Artefact` «is van soort» → `Artefactsoort`
- 🔴 Verwijderd: `Artefact` «vindbaar op» → `Magazijnplaatsing`
- 🔴 Verwijderd: `Artefact` «zit in» → `Doos`
- 🔴 Verwijderd: `Doos` «staat op» → `Magazijnlocatie`
- 🔴 Verwijderd: `Magazijnplaatsing` «hoort bij» → `Project`
- 🔴 Verwijderd: `Magazijnplaatsing` «staat op» → `Magazijnlocatie`
- 🔴 Verwijderd: `Magazijnplaatsing` «zit in» → `Doos`
- 🔴 Verwijderd: `Project` «heeft» → `Archeologiebesluit`
- 🔴 Verwijderd: `Project` «heeft» → `boring`
- 🔴 Verwijderd: `Project` «heeft» → `Put`
- 🔴 Verwijderd: `Project` «wordt begrensd door» → `locatie`
- 🔴 Verwijderd: `Put` «heeft locatie» → `locatie`
- 🔴 Verwijderd: `Put` «heeft» → `Vlak`
- 🔴 Verwijderd: `Spoor` «heeft» → `Vulling`
- 🔴 Verwijderd: `Stelling` «heeft» → `Magazijnlocatie`
- 🔴 Verwijderd: `Vindplaats` «hoort bij» → `Project`
- 🔴 Verwijderd: `Vlak` «heeft» → `Spoor`
- 🔴 Verwijderd: `Vondst` «bevat» → `Artefact`
- 🔴 Verwijderd: `Vulling` «heeft» → `Vondst`

<a id="structureel-delfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatieerfgoedarchiefmodel-archief"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Erfgoed/Archief/Model Archief

#### Classes

##### `Aanvraag` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumtijd` — Verwijderd

##### `Archief` — 🔴 Verwijderd

**Attributen:**

- 🔴 `archiefnummer` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `openbaarheidsbeperking` — Verwijderd

##### `Archiefcategorie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `nummer` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Archiefstuk` — 🔴 Verwijderd

**Attributen:**

- 🔴 `beschrijving` — Verwijderd
- 🔴 `inventarisnummer` — Verwijderd
- 🔴 `omvang` — Verwijderd
- 🔴 `openbaarheidsbeperking` — Verwijderd
- 🔴 `trefwoorden` — Verwijderd
- 🔴 `uiterlijkeVorm` — Verwijderd

##### `Auteur` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumGeboorte` — Verwijderd
- 🔴 `datumOverlijden` — Verwijderd

##### `Bezoeker` — 🔴 Verwijderd

##### `Depot` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `DigitaalBestand` — 🔴 Verwijderd

**Attributen:**

- 🔴 `blob` — Verwijderd
- 🔴 `mimetype` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Indeling` — 🔴 Verwijderd

**Attributen:**

- 🔴 `indelingsoort` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `nummer` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Index` — 🔴 Verwijderd

**Attributen:**

- 🔴 `indexnaam` — Verwijderd
- 🔴 `indexwaarde` — Verwijderd

##### `Kast` — 🔴 Verwijderd

**Attributen:**

- 🔴 `kastnummer` — Verwijderd

##### `Nadere Toegang` — 🔴 Verwijderd

##### `Ordeningsschema` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `text` — Verwijderd

##### `Plank` — 🔴 Verwijderd

**Attributen:**

- 🔴 `planknummer` — Verwijderd

##### `Rechthebbende` — 🔴 Verwijderd

##### `Stelling` — 🔴 Verwijderd

**Attributen:**

- 🔴 `stellingnummer` — Verwijderd

##### `Uitgever` — 🔴 Verwijderd

##### `Vindplaats` — 🔴 Verwijderd

#### Associaties

- 🔴 Verwijderd: `Aanvraag` «voor» → `Archiefstuk`
- 🔴 Verwijderd: `Archief` «heeft» → `Rechthebbende`
- 🔴 Verwijderd: `Archief` «stamt uit» → `Periode`
- 🔴 Verwijderd: `Archief` «valt binnen» → `Archiefcategorie`
- 🔴 Verwijderd: `Archiefstuk` «heeft» → `DigitaalBestand`
- 🔴 Verwijderd: `Archiefstuk` «heeft» → `Nadere Toegang`
- 🔴 Verwijderd: `Archiefstuk` «heeft» → `Ordeningsschema`
- 🔴 Verwijderd: `Archiefstuk` «heeft» → `Uitgever`
- 🔴 Verwijderd: `Archiefstuk` «heeft» → `Vindplaats`
- 🔴 Verwijderd: `Archiefstuk` «is onderdeel van» → `Archief`
- 🔴 Verwijderd: `Archiefstuk` «stamt uit» → `Periode`
- 🔴 Verwijderd: `Bezoeker` «doet» → `Aanvraag`
- 🔴 Verwijderd: `Depot` «heeft» → `Stelling`
- 🔴 Verwijderd: `Indeling` «hoort bij» → `Archief`
- 🔴 Verwijderd: `Indeling` «valt binnen» → `Archiefstuk`
- 🔴 Verwijderd: `Indeling` «valt binnen» → `Indeling`
- 🔴 Verwijderd: `Kast` «heeft» → `Plank`
- 🔴 Verwijderd: `Nadere Toegang` «wordt beschreven» → `Index`
- 🔴 Verwijderd: `Stelling` «heeft» → `Kast`
- 🔴 Verwijderd: `Vindplaats` «is te vinden in» → `Depot`
- 🔴 Verwijderd: `Vindplaats` «is te vinden in» → `Kast`
- 🔴 Verwijderd: `Vindplaats` «is te vinden in» → `Plank`
- 🔴 Verwijderd: `Vindplaats` «is te vinden in» → `Stelling`

#### Generalisaties

- 🔴 Verwijderd: `Archiefstuk` ⟶ `Document`
- 🔴 Verwijderd: `Archiefstuk` ⟶ `Erfgoed Object`
- 🔴 Verwijderd: `Auteur` ⟶ `Historisch Persoon `
- 🔴 Verwijderd: `Bezoeker` ⟶ `NatuurlijkPersoon`
- 🔴 Verwijderd: `Rechthebbende` ⟶ `Rechtspersoon`
- 🔴 Verwijderd: `Uitgever` ⟶ `Rechtspersoon`

<a id="structureel-delfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatieerfgoedgenerieke-entiteiten-erfgoedmodel-erfgoed-generiek"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Erfgoed/Generieke Entiteiten Erfgoed/Model Erfgoed Generiek

#### Classes

##### `Erfgoed Object` — 🔴 Verwijderd

**Attributen:**

- 🔴 `dateringTot` — Verwijderd
- 🔴 `dateringVanaf` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `titel` — Verwijderd

##### `Historisch Persoon` — 🔴 Verwijderd

**Attributen:**

- 🔴 `beroep` — Verwijderd
- 🔴 `datumGeboorte` — Verwijderd
- 🔴 `datumOverlijden` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `publiekToegankelijk` — Verwijderd
- 🔴 `woondeOp` — Verwijderd

##### `Objectclassificatie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `Erfgoed Object` «valt binnen» → `Objectclassificatie`

#### Generalisaties

- 🔴 Verwijderd: `Historisch Persoon ` ⟶ `NatuurlijkPersoon`

<a id="structureel-delfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatieerfgoedmonumentenmodel-monumenten"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Erfgoed/Monumenten/Model Monumenten

#### Classes

##### `Ambacht` — 🔴 Verwijderd

**Attributen:**

- 🔴 `ambachtsoort` — Verwijderd
- 🔴 `jaarAmbachtTot` — Verwijderd
- 🔴 `jaarAmbachtVanaf` — Verwijderd

##### `Beschermde Status` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bronnen` — Verwijderd
- 🔴 `complex` — Verwijderd
- 🔴 `datumInschrijvingRegister` — Verwijderd
- 🔴 `gemeentelijkMonumentCode` — Verwijderd
- 🔴 `gezichtscode` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `opmerkingen` — Verwijderd
- 🔴 `rijksmonumentcode` — Verwijderd
- 🔴 `type` — Verwijderd

##### `Bouwactiviteit` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bouwjaarklasse` — Verwijderd
- 🔴 `bouwjaarTot` — Verwijderd
- 🔴 `bouwjaarVan` — Verwijderd
- 🔴 `indicatie` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Bouwstijl` — 🔴 Verwijderd

**Attributen:**

- 🔴 `hoofdstijl` — Verwijderd
- 🔴 `substijl` — Verwijderd
- 🔴 `toelichting` — Verwijderd
- 🔴 `zuiverheid` — Verwijderd

##### `Bouwtype` — 🔴 Verwijderd

**Attributen:**

- 🔴 `hoofdcategorie` — Verwijderd
- 🔴 `subcategorie` — Verwijderd
- 🔴 `toelichting` — Verwijderd

##### `OorspronkelijkeFunctie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `functie` — Verwijderd
- 🔴 `functiesoort` — Verwijderd
- 🔴 `hoofdcategorie` — Verwijderd
- 🔴 `hoofdfunctie` — Verwijderd
- 🔴 `subcategorie` — Verwijderd
- 🔴 `toelichting` — Verwijderd
- 🔴 `verbijzondering` — Verwijderd

#### Enumeraties

##### `TypeMonument` — 🔴 Verwijderd

**Literals:**

- 🔴 `gemeentelijkmonument` — Verwijderd
- 🔴 `rijksmonument` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `Beschermde Status` «betreft» → `KadastraleOnroerendeZaak`
- 🔴 Verwijderd: `Beschermde Status` «betreft» → `OpenbareRuimte`
- 🔴 Verwijderd: `Beschermde Status` «betreft» → `OpenbareRuimte`
- 🔴 Verwijderd: `Beschermde Status` «betreft» → `Pand`
- 🔴 Verwijderd: `Beschermde Status` «monument ambacht» → `Ambacht`
- 🔴 Verwijderd: `Beschermde Status` «monument bouwactiviteit» → `Bouwactiviteit`
- 🔴 Verwijderd: `Beschermde Status` «monument bouwstijl» → `Bouwstijl`
- 🔴 Verwijderd: `Beschermde Status` «monument bouwtype» → `Bouwtype`
- 🔴 Verwijderd: `Beschermde Status` «monument fotos» → `Foto`
- 🔴 Verwijderd: `Beschermde Status` «monument functie» → `OorspronkelijkeFunctie`

<a id="structureel-delfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatiemuseadiagram"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Musea/Diagram

#### Classes

##### `Proxyconnector` — 🔴 Verwijderd

##### `Proxyconnector` — 🔴 Verwijderd

#### Associaties

- 🔴 Verwijderd: `Proxyconnector` → `Proxyconnector`

<a id="structureel-delfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatiemuseamodel-musea"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Musea/Model Musea

#### Classes

##### `Activiteit` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aantalPersonen` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Activiteitsoort` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Balieverkoop` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aantal` — Verwijderd
- 🔴 `kanaal` — Verwijderd
- 🔴 `verkooptijd` — Verwijderd

##### `Balieverkoop Entreekaart` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumEindeGeldigheid` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `gebruiktOp` — Verwijderd
- 🔴 `rondleiding` — Verwijderd

##### `Belanghebbende` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumStart` — Verwijderd
- 🔴 `datumTot` — Verwijderd

##### `Bruikleen` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aanvraagDoor` — Verwijderd
- 🔴 `datumAanvraag` — Verwijderd
- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `toestemmingDoor` — Verwijderd

##### `Collectie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Doelgroep` — 🔴 Verwijderd

**Attributen:**

- 🔴 `branch` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `segment` — Verwijderd

##### `Entreekaart` — 🔴 Verwijderd

**Attributen:**

- 🔴 `rondleiding` — Verwijderd

##### `Incident` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datum` — Verwijderd
- 🔴 `locatie` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Lener` — 🔴 Verwijderd

**Attributen:**

- 🔴 `opmerkingen` — Verwijderd

##### `Mailing` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datum` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Museumobject` — 🔴 Verwijderd

**Attributen:**

- 🔴 `afmeting` — Verwijderd
- 🔴 `bezitTot` — Verwijderd
- 🔴 `bezitVanaf` — Verwijderd
- 🔴 `medium` — Verwijderd
- 🔴 `verkrijging` — Verwijderd

##### `Museumrelatie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `relatiesoort` — Verwijderd

##### `Omzetgroep` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Prijs` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bedrag` — Verwijderd
- 🔴 `datumEindeGeldigheid` — Verwijderd
- 🔴 `datumStart` — Verwijderd

##### `Product` — 🔴 Verwijderd

**Attributen:**

- 🔴 `codeMuseumjaarkaart` — Verwijderd
- 🔴 `datumEindeGeldigheid` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `entreekaart` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `prijs` — Verwijderd

##### `Productgroep` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Productie-eenheid` — 🔴 Verwijderd

##### `Programma` — 🔴 Verwijderd

**Attributen:**

- 🔴 `BTW` — Verwijderd
- 🔴 `eindtijd` — Verwijderd
- 🔴 `locatie` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `prijsExclusiefBTW` — Verwijderd
- 🔴 `publiekstaak` — Verwijderd
- 🔴 `schoolniveau` — Verwijderd
- 🔴 `starttijd` — Verwijderd

##### `Programmasoort` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Reservering` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aantal` — Verwijderd
- 🔴 `BTW` — Verwijderd
- 🔴 `tijdTot` — Verwijderd
- 🔴 `tijdVanaf` — Verwijderd
- 🔴 `totaalprijs` — Verwijderd

##### `Rondleiding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `eindtijd` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `starttijd` — Verwijderd

##### `Samensteller` — 🔴 Verwijderd

**Attributen:**

- 🔴 `rol` — Verwijderd

##### `Standplaats` — 🔴 Verwijderd

**Attributen:**

- 🔴 `adres` — Verwijderd
- 🔴 `beschrijving` — Verwijderd
- 🔴 `naamInstelling` — Verwijderd

##### `Tentoonstelling` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `subtitel` — Verwijderd
- 🔴 `titel` — Verwijderd

##### `Voorziening` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aantalBeschikbaar` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Winkelverkoopgroep` — 🔴 Verwijderd

##### `Winkelvoorraaditem` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aantal` — Verwijderd
- 🔴 `aantalInBestelling` — Verwijderd
- 🔴 `datumLeveringBestelling` — Verwijderd
- 🔴 `locatie` — Verwijderd

##### `Zaal` — 🔴 Verwijderd

**Attributen:**

- 🔴 `capaciteit` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `nummer` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `Activiteit` «bestaat uit» → `Activiteit`
- 🔴 Verwijderd: `Activiteit` «heeft» → `Reservering`
- 🔴 Verwijderd: `Activiteit` «heeft» → `Rondleiding`
- 🔴 Verwijderd: `Activiteit` «van soort» → `Activiteitsoort`
- 🔴 Verwijderd: `Balieverkoop` «betreft» → `Product`
- 🔴 Verwijderd: `Balieverkoop` «tegen prijs» → `Prijs`
- 🔴 Verwijderd: `Bruikleen` «is bedoeld voor» → `Tentoonstelling`
- 🔴 Verwijderd: `Collectie` «bevat» → `Museumobject`
- 🔴 Verwijderd: `Doelgroep` «bestaat uit» → `Doelgroep`
- 🔴 Verwijderd: `Incident` «betreft» → `Museumobject`
- 🔴 Verwijderd: `Lener` «is» → `Bruikleen`
- 🔴 Verwijderd: `Mailing` «versturen aan» → `Museumrelatie`
- 🔴 Verwijderd: `Museumobject` «betreft» → `Bruikleen`
- 🔴 Verwijderd: `Museumobject` «locatie» → `Standplaats`
- 🔴 Verwijderd: `Museumobject` «onderdeel» → `Tentoonstelling`
- 🔴 Verwijderd: `Museumrelatie` «valt binnen» → `Doelgroep`
- 🔴 Verwijderd: `Museumrelatie` «voor» → `Programma`
- 🔴 Verwijderd: `Product` «heeft prijs» → `Prijs`
- 🔴 Verwijderd: `Product` «leverancier» → `Leverancier`
- 🔴 Verwijderd: `Product` «valt binnen» → `Omzetgroep`
- 🔴 Verwijderd: `Product` «valt binnen» → `Productgroep`
- 🔴 Verwijderd: `Productie-eenheid` «betreft» → `Leverancier`
- 🔴 Verwijderd: `Programma` «bestaat uit» → `Activiteit`
- 🔴 Verwijderd: `Programma` «heeft» → `Kostenplaats`
- 🔴 Verwijderd: `Programma` «voor» → `Programmasoort`
- 🔴 Verwijderd: `Reservering` «betreft» → `Productie-eenheid`
- 🔴 Verwijderd: `Reservering` «betreft» → `Voorziening`
- 🔴 Verwijderd: `Reservering` «betreft» → `Zaal`
- 🔴 Verwijderd: `Rondleiding` «voor» → `Tentoonstelling`
- 🔴 Verwijderd: `Samensteller` «stelt samen» → `Tentoonstelling`
- 🔴 Verwijderd: `Tentoonstelling` «is gewijd aan» → `Historisch Persoon `
- 🔴 Verwijderd: `Tentoonstelling` → `Zaal`
- 🔴 Verwijderd: `Winkelvoorraaditem` «betreft» → `Product`

#### Generalisaties

- 🔴 Verwijderd: `Balieverkoop Entreekaart` ⟶ `Balieverkoop`
- 🔴 Verwijderd: `Belanghebbende` ⟶ `Rechtspersoon`
- 🔴 Verwijderd: `Entreekaart` ⟶ `Product`
- 🔴 Verwijderd: `Lener` ⟶ `Rechtspersoon`
- 🔴 Verwijderd: `Museumobject` ⟶ `Erfgoed Object`
- 🔴 Verwijderd: `Museumrelatie` ⟶ `Rechtspersoon`
- 🔴 Verwijderd: `Samensteller` ⟶ `Medewerker`

<a id="structureel-delfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatiesportdiagram"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Sport/Diagram

#### Classes

##### `Proxyconnector` — 🔴 Verwijderd

##### `Proxyconnector` — 🔴 Verwijderd

##### `Proxyconnector` — 🔴 Verwijderd

##### `Proxyconnector` — 🔴 Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatiesportmodel-sport"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Sport/Model Sport

#### Classes

##### `Belijning` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd

##### `Bezetting` — 🔴 Verwijderd

##### `Binnenlocatie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `adres` — Verwijderd
- 🔴 `bouwjaar` — Verwijderd
- 🔴 `gemeentelijk` — Verwijderd
- 🔴 `geschatteKostenPerJaar` — Verwijderd
- 🔴 `gymzaal` — Verwijderd
- 🔴 `klokurenOnderwijs` — Verwijderd
- 🔴 `klokurenVerenigingen` — Verwijderd
- 🔴 `locatie` — Verwijderd
- 🔴 `onderhoudsniveau` — Verwijderd
- 🔴 `onderhoudsstatus` — Verwijderd
- 🔴 `sporthal` — Verwijderd
- 🔴 `vloeroppervlakte` — Verwijderd

##### `Onderhoudskosten` — 🔴 Verwijderd

##### `Sportlocatie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd

##### `Sportmateriaal` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd

##### `Sportpark` — 🔴 Verwijderd

##### `Sportvereniging` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aantalNormTeams` — Verwijderd
- 🔴 `adres` — Verwijderd
- 🔴 `binnensport` — Verwijderd
- 🔴 `buitensport` — Verwijderd
- 🔴 `email` — Verwijderd
- 🔴 `ledenaantal` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `typeSport` — Verwijderd

##### `Veld` — 🔴 Verwijderd

#### Associaties

- 🔴 Verwijderd: `Binnenlocatie` «bedient» → `Wijk`
- 🔴 Verwijderd: `Binnenlocatie` «bedient» → `Wijk`
- 🔴 Verwijderd: `Binnenlocatie` «heeft» → `Belijning`
- 🔴 Verwijderd: `Binnenlocatie` «heeft» → `Sportmateriaal`
- 🔴 Verwijderd: `Binnenlocatie` «is gevestigd in» → `Verblijfsobject`
- 🔴 Verwijderd: `Binnenlocatie` «is gevestigd in» → `Verblijfsobject`
- 🔴 Verwijderd: `Sportpark` «heeft» → `Veld`
- 🔴 Verwijderd: `Sportpark` «ligt op» → `OverigBenoemdTerrein`
- 🔴 Verwijderd: `Sportvereniging` «gebruikt» → `Sportlocatie`
- 🔴 Verwijderd: `Veld` «heeft» → `Belijning`
- 🔴 Verwijderd: `Veld` «ligt op» → `OverigBenoemdTerrein`

#### Generalisaties

- 🔴 Verwijderd: `Binnenlocatie` ⟶ `Sportlocatie`
- 🔴 Verwijderd: `Sportpark` ⟶ `Sportlocatie`
- 🔴 Verwijderd: `Sportvereniging` ⟶ `NietNatuurlijkPersoon`

<a id="structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeindak--en-thuislozenmodel-dak--en-thuislozen"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Dak- en thuislozen/Model Dak- en thuislozen

#### Classes

##### `Dakloosheid` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumEind` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `gemeenteOorsprong` — Verwijderd
- 🔴 `toestemmingGemeentelijkBriefadres` — Verwijderd
- 🔴 `toestemmingNachtopvang` — Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeingemeentebegrafenissenmodel-gemeentebegrafenissen"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Gemeentebegrafenissen/Model Gemeentebegrafenissen

#### Classes

##### `Gemeentebegrafenis` — 🔴 Verwijderd

**Attributen:**

- 🔴 `achtergrondMelding` — Verwijderd
- 🔴 `begrafeniskosten` — Verwijderd
- 🔴 `datumAfgedaan` — Verwijderd
- 🔴 `datumBegrafenis` — Verwijderd
- 🔴 `datumGemeld` — Verwijderd
- 🔴 `datumRuimingGraf` — Verwijderd
- 🔴 `doodsoorzaak` — Verwijderd
- 🔴 `gemeentelijkeKosten` — Verwijderd
- 🔴 `inkoopordernummer` — Verwijderd
- 🔴 `melder` — Verwijderd
- 🔴 `urenGemeente` — Verwijderd
- 🔴 `verhaaldBedrag` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `Gemeentebegrafenis` «heeft» → `NatuurlijkPersoon`

<a id="structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeingeneriek-jeugd-en-wmomodel-jeugd-en-wmo-generiek"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Generiek Jeugd en Wmo/Model Jeugd en Wmo Generiek

#### Classes

##### `AOM_AanvraagWmoJeugd` — 🔴 Verwijderd

**Attributen:**

- 🔴 `clientReactie` — Verwijderd
- 🔴 `datumBeschikking` — Verwijderd
- 🔴 `datumEersteAfspraak` — Verwijderd
- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumPlanVastgesteld` — Verwijderd
- 🔴 `datumStartAanvraag` — Verwijderd
- 🔴 `deskundigheid` — Verwijderd
- 🔴 `doorloopmethodiek` — Verwijderd
- 🔴 `maximaleDoorlooptijd` — Verwijderd
- 🔴 `redenAfsluiting` — Verwijderd

##### `AOMMeldingWmoJeugd` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aanmelder` — Verwijderd
- 🔴 `aanmeldingDoor` — Verwijderd
- 🔴 `aanmeldingDoorLandelijk` — Verwijderd
- 🔴 `aanmeldwijze` — Verwijderd
- 🔴 `deskundigheid` — Verwijderd
- 🔴 `isClientOpDeHoogte` — Verwijderd
- 🔴 `onderzoekswijze` — Verwijderd
- 🔴 `redenAfsluiting` — Verwijderd
- 🔴 `vervolg` — Verwijderd
- 🔴 `verwezen` — Verwijderd

##### `Beperking` — 🔴 Verwijderd

**Attributen:**

- 🔴 `categorie` — Verwijderd
- 🔴 `commentaar` — Verwijderd
- 🔴 `duur` — Verwijderd
- 🔴 `wet` — Verwijderd

##### `Beperkingscategorie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `code` — Verwijderd
- 🔴 `wet` — Verwijderd

##### `Beperkingscore` — 🔴 Verwijderd

**Attributen:**

- 🔴 `commentaar` — Verwijderd
- 🔴 `score` — Verwijderd
- 🔴 `wet` — Verwijderd

##### `Beperkingscoresoort` — 🔴 Verwijderd

**Attributen:**

- 🔴 `vraag` — Verwijderd
- 🔴 `wet` — Verwijderd

##### `Beschikking` — 🔴 Verwijderd

**Attributen:**

- 🔴 `code` — Verwijderd
- 🔴 `commentaar` — Verwijderd
- 🔴 `datumAfgifte` — Verwijderd
- 🔴 `grondslagen` — Verwijderd
- 🔴 `wet` — Verwijderd

##### `Beschikkingsoort` — 🔴 Verwijderd

##### `Beschikte Voorziening` — 🔴 Verwijderd

**Attributen:**

- 🔴 `code` — Verwijderd
- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumEindeOorspronkelijk` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `eenheid` — Verwijderd
- 🔴 `frequentie` — Verwijderd
- 🔴 `leveringsvorm` — Verwijderd
- 🔴 `omvang` — Verwijderd
- 🔴 `redenEinde` — Verwijderd
- 🔴 `status` — Verwijderd
- 🔴 `wet` — Verwijderd

##### `Budgetuitputting` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datum` — Verwijderd
- 🔴 `uitgenutBedrag` — Verwijderd

##### `Declaratie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumDeclaratie` — Verwijderd
- 🔴 `declaratieBedrag` — Verwijderd
- 🔴 `declaratieStatus` — Verwijderd

##### `Declaratieregel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bedrag` — Verwijderd
- 🔴 `code` — Verwijderd
- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumStart` — Verwijderd

##### `Leefgebied` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd

##### `Levering` — 🔴 Verwijderd

**Attributen:**

- 🔴 `code` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `datumStop` — Verwijderd
- 🔴 `eenheid` — Verwijderd
- 🔴 `frequentie` — Verwijderd
- 🔴 `omvang` — Verwijderd
- 🔴 `stopreden` — Verwijderd

##### `Leveringsvorm` — 🔴 Verwijderd

**Attributen:**

- 🔴 `leveringsvormCode` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `wet` — Verwijderd

##### `Melding Eigen bijdrage` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumStart` — Verwijderd
- 🔴 `datumStop` — Verwijderd

##### `PGB-Toekenning` — 🔴 Verwijderd

**Attributen:**

- 🔴 `budget` — Verwijderd
- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumToekenning` — Verwijderd

##### `Score` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datum` — Verwijderd

##### `Scoresoort` — 🔴 Verwijderd

**Attributen:**

- 🔴 `niveau` — Verwijderd

##### `Tarief` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bedrag` — Verwijderd
- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `eenheid` — Verwijderd
- 🔴 `wet` — Verwijderd

##### `Team` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Toewijzing` — 🔴 Verwijderd

**Attributen:**

- 🔴 `code` — Verwijderd
- 🔴 `commentaar` — Verwijderd
- 🔴 `datumAanschaf` — Verwijderd
- 🔴 `datumEindeToewijzing` — Verwijderd
- 🔴 `datumStartToewijzing` — Verwijderd
- 🔴 `datumToewijzing` — Verwijderd
- 🔴 `eenheid` — Verwijderd
- 🔴 `frequentie` — Verwijderd
- 🔴 `omvang` — Verwijderd
- 🔴 `redenWijziging` — Verwijderd
- 🔴 `toewijzingnummer` — Verwijderd
- 🔴 `wet` — Verwijderd

##### `Verplichting Wmo Jeugd` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Budgetsoort` — Verwijderd
- 🔴 `budgetsoortgroep` — Verwijderd
- 🔴 `Einddatumgepland` — Verwijderd
- 🔴 `Feitelijke Einddatum` — Verwijderd
- 🔴 `Jaar` — Verwijderd
- 🔴 `Periodiciteit` — Verwijderd
- 🔴 `verplichtingsoort` — Verwijderd

##### `Verzoek om Toewijzing` — 🔴 Verwijderd

**Attributen:**

- 🔴 `beschikkingsnummer` — Verwijderd
- 🔴 `commentaar` — Verwijderd
- 🔴 `datumEindeToewijzing` — Verwijderd
- 🔴 `datumIngangBeschikking` — Verwijderd
- 🔴 `datumIngangToewijzing` — Verwijderd
- 🔴 `datumOntvangst` — Verwijderd
- 🔴 `eenheid` — Verwijderd
- 🔴 `frequentie` — Verwijderd
- 🔴 `raamcontract` — Verwijderd
- 🔴 `referentieAanbieder` — Verwijderd
- 🔴 `soortVerwijzer` — Verwijderd
- 🔴 `verwijzer` — Verwijderd
- 🔴 `volume` — Verwijderd

##### `Voorziening` — 🔴 Verwijderd

**Attributen:**

- 🔴 `afhandelwijze` — Verwijderd
- 🔴 `code` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `productcode` — Verwijderd
- 🔴 `wet` — Verwijderd

##### `Voorzieningsoort` — 🔴 Verwijderd

**Attributen:**

- 🔴 `code` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `productcategorie` — Verwijderd
- 🔴 `productcategoriecode` — Verwijderd
- 🔴 `productcode` — Verwijderd
- 🔴 `wet` — Verwijderd

##### `Zelfredzaamheidmatrix` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumEindeGeldigheid` — Verwijderd
- 🔴 `datumStartGeldigheid` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

#### Enumeraties

##### `Doelgroep` — 🔴 Verwijderd

**Literals:**

- 🔴 `Asielstatushouder` — Verwijderd
- 🔴 `Geestelijk bedienaar` — Verwijderd
- 🔴 `Gezinshereniger` — Verwijderd
- 🔴 `Gezinshereniger met Asielstatushouder` — Verwijderd
- 🔴 `Gezinsvormer` — Verwijderd
- 🔴 `Gezinsvormer met Asielstatushouder` — Verwijderd
- 🔴 `Overig` — Verwijderd

##### `Eenheid` — 🔴 Verwijderd

**Literals:**

- 🔴 `Dagdeel (4 uur)` — Verwijderd
- 🔴 `Etmaal` — Verwijderd
- 🔴 `Euros` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Minuut` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Stuks` — Verwijderd
- 🔴 `Uur` — Verwijderd

##### `Frequentie` — 🔴 Verwijderd

**Literals:**

- 🔴 `Binnen geldigheid Beschikking` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Per 4 weken` — Verwijderd
- 🔴 `Per dag` — Verwijderd
- 🔴 `Per jaar` — Verwijderd
- 🔴 `Per maand` — Verwijderd
- 🔴 `Per week` — Verwijderd

##### `Leveringsvorm` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `PGB` — Verwijderd
- 🔴 `ZIN` — Verwijderd

##### `Soort Verwijzer` — 🔴 Verwijderd

**Literals:**

- 🔴 `Gecertificeerde instelling` — Verwijderd
- 🔴 `Gemeente` — Verwijderd
- 🔴 `Huisarts` — Verwijderd
- 🔴 `Jeugdarts` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Medisch specialist` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Rechter, Officier van Justitie, functionaris Justitiële jeugdinrichting` — Verwijderd
- 🔴 `Zelfverwijzer / geen verwijzer` — Verwijderd

##### `Wet` — 🔴 Verwijderd

**Literals:**

- 🔴 `Andere wet` — Verwijderd
- 🔴 `Bijzondere Bijstand` — Verwijderd
- 🔴 `I.O.A.W./I.O.A.Z.` — Verwijderd
- 🔴 `Jeugdwet` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Niet van toepassing` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Participatiewet PW-I` — Verwijderd
- 🔴 `Wmo` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `AOM_AanvraagWmoJeugd` «heeft» → `Client`
- 🔴 Verwijderd: `AOM_AanvraagWmoJeugd` «leidt_tot» → `Beschikking`
- 🔴 Verwijderd: `AOMMeldingWmoJeugd` «heeft» → `Client`
- 🔴 Verwijderd: `Beperking` «is een» → `Beperkingscategorie`
- 🔴 Verwijderd: `Beperking` «is gebaseerd op» → `Beschikking`
- 🔴 Verwijderd: `Beperking` → `Beperkingscore`
- 🔴 Verwijderd: `Beperkingscore` «is een» → `Beperkingscoresoort`
- 🔴 Verwijderd: `Beschikking` «betreft» → `AOMMeldingWmoJeugd`
- 🔴 Verwijderd: `Beschikking` «heeft voorzieningen» → `Beschikte Voorziening`
- 🔴 Verwijderd: `Beschikking` «toewijzing» → `Toewijzing`
- 🔴 Verwijderd: `Beschikking` → `Client`
- 🔴 Verwijderd: `Beschikte Voorziening` «heeft» → `Leveringsvorm`
- 🔴 Verwijderd: `Beschikte Voorziening` «is voorziening» → `Voorziening`
- 🔴 Verwijderd: `Beschikte Voorziening` «Toegewezen Product» → `Toewijzing`
- 🔴 Verwijderd: `Declaratie` «Ingediend door» → `Leverancier`
- 🔴 Verwijderd: `Declaratieregel` «betreft» → `Client`
- 🔴 Verwijderd: `Declaratieregel` «is voor» → `Beschikking`
- 🔴 Verwijderd: `Declaratieregel` «valt binnen» → `Declaratie`
- 🔴 Verwijderd: `Levering` «geleverde prestatie» → `Beschikking`
- 🔴 Verwijderd: `Levering` «geleverde zorg» → `Toewijzing`
- 🔴 Verwijderd: `Levering` «prestatie voor» → `Client`
- 🔴 Verwijderd: `Levering` «voorziening» → `Voorziening`
- 🔴 Verwijderd: `Melding Eigen bijdrage` «betreft» → `Beschikking`
- 🔴 Verwijderd: `PGB-Toekenning` «betreft» → `Beschikte Voorziening`
- 🔴 Verwijderd: `PGB-Toekenning` «betreft» → `Budgetuitputting`
- 🔴 Verwijderd: `Score` «hoogte score» → `Scoresoort`
- 🔴 Verwijderd: `Score` «score bij leeggebied» → `Leefgebied`
- 🔴 Verwijderd: `Tarief` «heeft» → `Leverancier`
- 🔴 Verwijderd: `Toewijzing` «is op basis van» → `Declaratieregel`
- 🔴 Verwijderd: `Toewijzing` «levert voorziening» → `Leverancier`
- 🔴 Verwijderd: `Verplichting Wmo Jeugd` «heeft» → `Client`
- 🔴 Verwijderd: `Verplichting Wmo Jeugd` «Verplichting aan» → `Leverancier`
- 🔴 Verwijderd: `Verplichting Wmo Jeugd` → `AOM_AanvraagWmoJeugd`
- 🔴 Verwijderd: `Verplichting Wmo Jeugd` → `Beschikte Voorziening`
- 🔴 Verwijderd: `Verzoek om Toewijzing` «betreft» → `Client`
- 🔴 Verwijderd: `Verzoek om Toewijzing` «betreft» → `Voorziening`
- 🔴 Verwijderd: `Verzoek om Toewijzing` «leidt tot» → `Beschikking`
- 🔴 Verwijderd: `Verzoek om Toewijzing` «leverancier» → `Leverancier`
- 🔴 Verwijderd: `Voorziening` «heeft» → `Tarief`
- 🔴 Verwijderd: `Voorziening` «valt binnen» → `Voorzieningsoort`
- 🔴 Verwijderd: `Zelfredzaamheidmatrix` «onderkent leefgebiieden» → `Leefgebied`
- 🔴 Verwijderd: `Zelfredzaamheidmatrix` «onderkent scores» → `Scoresoort`

#### Generalisaties

- 🔴 Verwijderd: `AOM_AanvraagWmoJeugd` ⟶ `AanvraagOfMelding`
- 🔴 Verwijderd: `AOMMeldingWmoJeugd` ⟶ `AanvraagOfMelding`
- 🔴 Verwijderd: `Verplichting Wmo Jeugd` ⟶ `Inkooporder`

<a id="structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeininburgeringmodel-inburgering"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inburgering/Model Inburgering

#### Classes

##### `Aandachtspunt` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aandachtspuntOmschrijving` — Verwijderd
- 🔴 `EindDatum` — Verwijderd
- 🔴 `StartDatum` — Verwijderd

##### `Aanvraag verlenging Inburgeringstermijn` — 🔴 Verwijderd

**Attributen:**

- 🔴 `BeoordelingAanvraagVerlenging` — Verwijderd
- 🔴 `VerlengingsGrond` — Verwijderd

##### `Asielstatushouder` — 🔴 Verwijderd

**Attributen:**

- 🔴 `DigiD aangevraagd` — Verwijderd
- 🔴 `Emailadres verblijf AZC` — Verwijderd
- 🔴 `Is gekoppeld aan` — Verwijderd
- 🔴 `Land Rijbewijs` — Verwijderd
- 🔴 `Rijbewijs` — Verwijderd
- 🔴 `Telefoonnummer verblijf AZC` — Verwijderd

##### `B1-route` — 🔴 Verwijderd

**Attributen:**

- 🔴 `AantalGratisExamenpogingenTegoed` — Verwijderd
- 🔴 `ExamenDatum` — Verwijderd
- 🔴 `GevolgdeUrenParticipatieTaalles` — Verwijderd
- 🔴 `RedenGeenResultaat` — Verwijderd
- 🔴 `Resultaat` — Verwijderd

##### `Brede Intake` — 🔴 Verwijderd

**Attributen:**

- 🔴 `AantalUrenAlfabetiseringsOnderwijs` — Verwijderd
- 🔴 `DatumTot(Peildatum)` — Verwijderd
- 🔴 `einddatum` — Verwijderd
- 🔴 `GevolgdeUrenKNMenTaalles` — Verwijderd
- 🔴 `startdatum` — Verwijderd
- 🔴 `UrenGeoorloofdVerzuim` — Verwijderd
- 🔴 `UrenOngeoorloofdVerzuim` — Verwijderd

##### `Diplomawaardering` — 🔴 Verwijderd

**Attributen:**

- 🔴 `DiplomaWaarderingNederlandsNiveau` — Verwijderd
- 🔴 `DiplomaWaarderingRichting` — Verwijderd
- 🔴 `DiplomaWaarderingVoor` — Verwijderd
- 🔴 `NiveauCompetentie` — Verwijderd
- 🔴 `WaarderingAangevraagd` — Verwijderd

##### `Educatie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `EducatieDiploma` — Verwijderd
- 🔴 `EducatieInBezit` — Verwijderd
- 🔴 `EducatieLand` — Verwijderd
- 🔴 `EducatieTot` — Verwijderd
- 🔴 `EducatieVan` — Verwijderd
- 🔴 `Opleiding` — Verwijderd

##### `Examen` — 🔴 Verwijderd

**Attributen:**

- 🔴 `ExamenResultaat` — Verwijderd

##### `Examenonderdeel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `BehaaldeScore` — Verwijderd
- 🔴 `DatumRegistratieUitslag` — Verwijderd
- 🔴 `ExamenOnderdeelSpecificatie` — Verwijderd
- 🔴 `Ontheffing` — Verwijderd
- 🔴 `RedenVrijstelling` — Verwijderd
- 🔴 `Resultaat` — Verwijderd

##### `Gezinsmigrant en Overige migrant` — 🔴 Verwijderd

##### `Hoofddoel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Doel` — Verwijderd
- 🔴 `EindDatum` — Verwijderd
- 🔴 `StartDatum` — Verwijderd

##### `ICT-Vaardigheid` — 🔴 Verwijderd

**Attributen:**

- 🔴 `ICTVaardigheid` — Verwijderd
- 🔴 `NiveauICTVaardigheid` — Verwijderd

##### `Inburgeraar` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Doelgroep` — Verwijderd
- 🔴 `Gedetailleerde Doelgroep` — Verwijderd

##### `InburgeringsAanbod` — 🔴 Verwijderd

**Attributen:**

- 🔴 `ContractId` — Verwijderd
- 🔴 `CursusInstelling` — Verwijderd
- 🔴 `DatumAanvangTaalschakelTraject` — Verwijderd
- 🔴 `DatumEindeCursus` — Verwijderd
- 🔴 `DatumInburgeringsAanbod` — Verwijderd
- 🔴 `DatumTaalschakelDiploma` — Verwijderd
- 🔴 `IndicatorAlfabetisering` — Verwijderd
- 🔴 `ParticipatieDeelname` — Verwijderd
- 🔴 `TaalschakelTraject` — Verwijderd

##### `Inburgeringsplicht` — 🔴 Verwijderd

**Attributen:**

- 🔴 `BeschikkingVoldaanInburgeringsplicht` — Verwijderd
- 🔴 `DatumEind` — Verwijderd
- 🔴 `DatumGewijzigdInburgeringsplicht` — Verwijderd
- 🔴 `DatumGewijzigdWordtBehandeldAls` — Verwijderd
- 🔴 `DatumStart` — Verwijderd
- 🔴 `InburgeraarSpecialisatie` — Verwijderd
- 🔴 `IndicatorInburgeringsplicht` — Verwijderd
- 🔴 `RedenGeenInburgeringsplicht` — Verwijderd
- 🔴 `UitkomstLeerbaarheidstoets` — Verwijderd
- 🔴 `V-nummer` — Verwijderd
- 🔴 `WordtBehandelsAls` — Verwijderd

##### `Inburgeringstermijn` — 🔴 Verwijderd

**Attributen:**

- 🔴 `BoeteBedrag` — Verwijderd
- 🔴 `DatumAanvangInburgeringstermijn` — Verwijderd
- 🔴 `DatumBoete` — Verwijderd
- 🔴 `DatumEindeInburgeringstermijn` — Verwijderd
- 🔴 `VooraankondigingBoete` — Verwijderd

##### `Inburgeringstraject` — 🔴 Verwijderd

**Attributen:**

- 🔴 `UItkomstLeerbaarheidstoets` — Verwijderd

##### `Introductiemodule` — 🔴 Verwijderd

**Attributen:**

- 🔴 `DeelnameIntroductieModule` — Verwijderd
- 🔴 `ModuleNaam` — Verwijderd

##### `Leerroute` — 🔴 Verwijderd

**Attributen:**

- 🔴 `ExamenA2` — Verwijderd
- 🔴 `geenLeerbaarheidstoetsZB` — Verwijderd
- 🔴 `GeschatteIntensiteitB1Route` — Verwijderd
- 🔴 `IndicatorAlfabetisering` — Verwijderd
- 🔴 `IndicatorMagOpleidingAfmaken` — Verwijderd
- 🔴 `IndicatorToestemmingExamenA2` — Verwijderd
- 🔴 `LeerrouteType` — Verwijderd
- 🔴 `Niveau` — Verwijderd

##### `MAP` — 🔴 Verwijderd

**Attributen:**

- 🔴 `DatumEindgesprekMAP` — Verwijderd
- 🔴 `IndicatorVerwijtbaar` — Verwijderd
- 🔴 `RedenNietSuccesvolVoltooid` — Verwijderd
- 🔴 `Resultaat` — Verwijderd

##### `Ontheffing` — 🔴 Verwijderd

**Attributen:**

- 🔴 `BeslissingOntheffing` — Verwijderd
- 🔴 `DatumOntheffing` — Verwijderd

##### `Ontwikkelwens` — 🔴 Verwijderd

**Attributen:**

- 🔴 `EindDatum` — Verwijderd
- 🔴 `ontwikkelwensOmschrijving` — Verwijderd
- 🔴 `StartDatum` — Verwijderd

##### `PIP` — 🔴 Verwijderd

**Attributen:**

- 🔴 `DagtekeningInitielePIP` — Verwijderd
- 🔴 `DagtekeningPIP` — Verwijderd
- 🔴 `EmailContactPersoon` — Verwijderd
- 🔴 `IndicatorMagOpleidingAfmaken` — Verwijderd
- 🔴 `NaamContactPersoon` — Verwijderd

##### `PVT` — 🔴 Verwijderd

**Attributen:**

- 🔴 `DatumOndertekening PVT` — Verwijderd
- 🔴 `RedenNietVoldaan` — Verwijderd
- 🔴 `Resultaat` — Verwijderd
- 🔴 `VerwijtbaarNietVoldaan` — Verwijderd

##### `Subdoel Aandachtspunt` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Einddatum` — Verwijderd
- 🔴 `Startdatum` — Verwijderd
- 🔴 `Subdoel` — Verwijderd

##### `Subdoel Ontwikkelwens` — 🔴 Verwijderd

**Attributen:**

- 🔴 `EindDatum` — Verwijderd
- 🔴 `StartDatum` — Verwijderd
- 🔴 `Subdoel` — Verwijderd

##### `Taalvaardigheid` — 🔴 Verwijderd

**Attributen:**

- 🔴 `EindeVanTaallesActviteit` — Verwijderd
- 🔴 `OpleidingsniveauGeschat` — Verwijderd
- 🔴 `PresentieTaalles` — Verwijderd
- 🔴 `ResultaatTaalles` — Verwijderd
- 🔴 `ResultaatToetsSpreekvaardigheid` — Verwijderd
- 🔴 `ResultaatToetsTaalleerbaarheid` — Verwijderd
- 🔴 `Score` — Verwijderd
- 🔴 `StartVanTaallesActviteit` — Verwijderd
- 🔴 `TaallesActiviteit` — Verwijderd
- 🔴 `TaalvaardigheidMondeling` — Verwijderd
- 🔴 `TaalvaardigheidOverall` — Verwijderd
- 🔴 `TaalvaardigheidSchriftelijk` — Verwijderd
- 🔴 `ToetsSpreekvaardigheid` — Verwijderd
- 🔴 `ToetsTaalleerbaarheid` — Verwijderd

##### `Training` — 🔴 Verwijderd

**Attributen:**

- 🔴 `PeriodeTraining` — Verwijderd
- 🔴 `ResultaatTraining` — Verwijderd
- 🔴 `TrainingGevolgd` — Verwijderd

##### `Verblijfplaats AZC` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Huisnummer` — Verwijderd
- 🔴 `Plaats` — Verwijderd
- 🔴 `Straatnummer` — Verwijderd

##### `Verlengingsgrond` — 🔴 Verwijderd

**Attributen:**

- 🔴 `AanwezigheidAanvraagVerlening` — Verwijderd
- 🔴 `DatumAanvangVerlengingsgrond` — Verwijderd
- 🔴 `DatumBeoordelingVerlengingsgrond` — Verwijderd
- 🔴 `DatumEindeVerlengingsgrond` — Verwijderd
- 🔴 `VerlengingInWeken` — Verwijderd
- 🔴 `Verlengingsgrondslag` — Verwijderd

##### `Voorbereiding op Inburgering` — 🔴 Verwijderd

**Attributen:**

- 🔴 `DatumInstemming` — Verwijderd
- 🔴 `InstemmingDeelnameVoorinburgering` — Verwijderd
- 🔴 `Reden` — Verwijderd

##### `Vreemdeling` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Sociaal Referent` — Verwijderd
- 🔴 `v-nummer` — Verwijderd

##### `Vrijstelling` — 🔴 Verwijderd

**Attributen:**

- 🔴 `DatumVrijstelling` — Verwijderd
- 🔴 `EindoordeelVrijstelling` — Verwijderd

##### `Werk` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Ambitie` — Verwijderd
- 🔴 `Beroep` — Verwijderd
- 🔴 `BeroepTot` — Verwijderd
- 🔴 `BeroepVan` — Verwijderd
- 🔴 `ContactUAF` — Verwijderd
- 🔴 `CVGemaakt` — Verwijderd
- 🔴 `SoortAanstelling` — Verwijderd
- 🔴 `Taak` — Verwijderd
- 🔴 `TaakTot` — Verwijderd
- 🔴 `TaakVan` — Verwijderd
- 🔴 `VrijeTekstBesteding` — Verwijderd

##### `Z-route` — 🔴 Verwijderd

**Attributen:**

- 🔴 `AantalGratisExamenpogingenTegoed` — Verwijderd
- 🔴 `ExamenDatum` — Verwijderd
- 🔴 `GevolgdeUrenParticipatieActiviteiten` — Verwijderd
- 🔴 `Niveau` — Verwijderd
- 🔴 `Onderdeel` — Verwijderd
- 🔴 `RedenGeenResultaat` — Verwijderd
- 🔴 `Resultaat` — Verwijderd

#### Enumeraties

##### `Aandachtspunt` — 🔴 Verwijderd

**Literals:**

- 🔴 `Digitale vaardigheden` — Verwijderd
- 🔴 `Financien` — Verwijderd
- 🔴 `Justitie` — Verwijderd
- 🔴 `Lichaamelijke gezondheid` — Verwijderd
- 🔴 `Psychische gezondheid` — Verwijderd
- 🔴 `Taal` — Verwijderd
- 🔴 `Verslaving` — Verwijderd
- 🔴 `Woonsituatie` — Verwijderd
- 🔴 `Zorgtaken` — Verwijderd

##### `BeoordelingAanvraagVerlenging` — 🔴 Verwijderd

**Literals:**

- 🔴 `NietToegestaan` — Verwijderd
- 🔴 `Toegestaan` — Verwijderd

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

##### `ClassificatieArmTotUitstekend` — 🔴 Verwijderd

**Literals:**

- 🔴 `Arm` — Verwijderd
- 🔴 `Goed` — Verwijderd
- 🔴 `Middelmatig` — Verwijderd
- 🔴 `Uitstekend` — Verwijderd
- 🔴 `Voldoende` — Verwijderd

##### `ClassificatieVoldoendeOnvoldoende` — 🔴 Verwijderd

**Literals:**

- 🔴 `Onvoldoende` — Verwijderd
- 🔴 `Voldoende` — Verwijderd

##### `CodeNiveauOpleiding` — 🔴 Verwijderd

**Literals:**

- 🔴 `Basisonderwijs` — Verwijderd
- 🔴 `HAVO / VWO` — Verwijderd
- 🔴 `HBO / Bachelor` — Verwijderd
- 🔴 `MBO` — Verwijderd
- 🔴 `VMBO / MBO-1` — Verwijderd
- 🔴 `WO / Master` — Verwijderd

##### `Doel` — 🔴 Verwijderd

**Literals:**

- 🔴 `Betaal werken naar vermogen` — Verwijderd
- 🔴 `Betaald Werken` — Verwijderd
- 🔴 `Maatschappelijk fit worden` — Verwijderd
- 🔴 `Ondernemen` — Verwijderd
- 🔴 `Opleiding met studiefinanciering` — Verwijderd
- 🔴 `Werkfit worden` — Verwijderd

##### `Doelgroep` — 🔴 Verwijderd

**Literals:**

- 🔴 `Arbeidsmigranten met vestigingsintentie` — Verwijderd
- 🔴 `EU-burgers` — Verwijderd
- 🔴 `Expats en kennismigranten` — Verwijderd
- 🔴 `Gezinsmigranten` — Verwijderd
- 🔴 `Internationale studenten (blijvers)` — Verwijderd
- 🔴 `Kwetsbare nieuwkomers` — Verwijderd
- 🔴 `Nieuwkomers` — Verwijderd
- 🔴 `Oudkomers` — Verwijderd

##### `EindoordeelVrijstelling` — 🔴 Verwijderd

**Literals:**

- 🔴 `Fysieke reden` — Verwijderd
- 🔴 `Heeft competentie` — Verwijderd
- 🔴 `Overig` — Verwijderd
- 🔴 `Zwangerschap` — Verwijderd

##### `Ontwikkelwens` — 🔴 Verwijderd

**Literals:**

- 🔴 `Betaald werken` — Verwijderd
- 🔴 `Betaald werken met een opleiding` — Verwijderd
- 🔴 `Betaald werken naar vermogen` — Verwijderd
- 🔴 `Ondernemen` — Verwijderd
- 🔴 `Opleiding volgen` — Verwijderd
- 🔴 `Passende dagbesteding hebben` — Verwijderd
- 🔴 `Taalvaardigheden opdoen` — Verwijderd
- 🔴 `Vrijwilligerswerk` — Verwijderd
- 🔴 `Werkervaring opdoen` — Verwijderd
- 🔴 `Werknemersvaardigheden ontwikkelen` — Verwijderd

##### `Opleidingsniveau` — 🔴 Verwijderd

**Literals:**

- 🔴 `Basisniveau` — Verwijderd
- 🔴 `Geen basisopleiding` — Verwijderd
- 🔴 `HBO-niveau` — Verwijderd
- 🔴 `LBO/MAVO-niveau` — Verwijderd
- 🔴 `MBO/HAVO/VWO-niveau` — Verwijderd
- 🔴 `Niet van toepassing` — Verwijderd
- 🔴 `Wetenschappelijk onderwijs` — Verwijderd

##### `ParticipatieDeelname` — 🔴 Verwijderd

**Literals:**

- 🔴 `Onvoldoende` — Verwijderd
- 🔴 `Voldoende` — Verwijderd

##### `PresentieTaalles` — 🔴 Verwijderd

**Literals:**

- 🔴 `Altijd aanwezig` — Verwijderd
- 🔴 `Nooit aanwezig` — Verwijderd
- 🔴 `Wel/niet aanwezig` — Verwijderd

##### `SETU job category` — 🔴 Verwijderd

**Literals:**

- 🔴 `Administratieve / Secretariat` — Verwijderd
- 🔴 `Agricultural / Cattle breeding / Animal care / Nature conservation` — Verwijderd
- 🔴 `Building industry` — Verwijderd
- 🔴 `Business services / Retail trade` — Verwijderd
- 🔴 `Catering / Tourism` — Verwijderd
- 🔴 `Cleaning / Housekeeing / Clean up` — Verwijderd
- 🔴 `Consulting / Staff / Policy` — Verwijderd
- 🔴 `Culture / Arts / Creative` — Verwijderd
- 🔴 `Customer service / Call centre / Reception` — Verwijderd
- 🔴 `Design / Architecture / Graphical` — Verwijderd
- 🔴 `Editior / Journalism` — Verwijderd
- 🔴 `Education / Training` — Verwijderd
- 🔴 `Financial administratieve / Accounting` — Verwijderd
- 🔴 `Government service / Government` — Verwijderd
- 🔴 `Health care / Medical / Nursing / Paramedical` — Verwijderd
- 🔴 `IT / ICT / Software development/ Internet` — Verwijderd
- 🔴 `Legal` — Verwijderd
- 🔴 `Marketing / Advertisement / Public relations / Communication` — Verwijderd
- 🔴 `Personal health car` — Verwijderd
- 🔴 `Personnel matters / Human resources / Employment-finding` — Verwijderd
- 🔴 `Production / Crafts` — Verwijderd
- 🔴 `Research / Science / Laboratory` — Verwijderd
- 🔴 `Sales / Commercial` — Verwijderd
- 🔴 `Security / Defence / Auxiliary service` — Verwijderd
- 🔴 `Sport / Relaxation` — Verwijderd
- 🔴 `Technology / Engineering` — Verwijderd

##### `SoortWerk` — 🔴 Verwijderd

**Literals:**

- 🔴 `Aanpakken` — Verwijderd
- 🔴 `Helpen` — Verwijderd
- 🔴 `Maken` — Verwijderd
- 🔴 `Verkopen` — Verwijderd
- 🔴 `Vervoeren` — Verwijderd

##### `Subdoel betaald werken` — 🔴 Verwijderd

##### `Subdoel betaald werken met een opleiding` — 🔴 Verwijderd

**Literals:**

- 🔴 `ik ben gestart met een BBL opleiding (werken en leren)` — Verwijderd
- 🔴 `ik volg een opleiding naast mijn parttime betaalde baan` — Verwijderd
- 🔴 `ik weet welke opleiding past bij mijn mogelijkheden` — Verwijderd

##### `Subdoel betaald werken naar vermogen` — 🔴 Verwijderd

**Literals:**

- 🔴 `ik ben gestart met werken en behoud mijn werk succesvol` — Verwijderd
- 🔴 `ik heb urenuitbreiding gekregen` — Verwijderd
- 🔴 `ik heb werk gevonden waarmee ik uit de bijstand ga` — Verwijderd
- 🔴 `ik weet hoeveel uur ik kan werken` — Verwijderd
- 🔴 `ik weet wat mijn kwaliteiten zijn` — Verwijderd
- 🔴 `ik weet welk werk bij mijn past` — Verwijderd

##### `Subdoel digitale vaardigheden` — 🔴 Verwijderd

**Literals:**

- 🔴 `ik heb voldoende digitale vaardigheden om een stap te zetten richting de arbeidsmarkt` — Verwijderd
- 🔴 `ik kan omgaan met computer, smartphone en tablet en kan zelfstandig mailen en zoeken op internet` — Verwijderd

##### `Subdoel eenzaamheid` — 🔴 Verwijderd

**Literals:**

- 🔴 `ik heb een netwerk waarmee ik sociale contacten heb` — Verwijderd
- 🔴 `ik heb vertrouwen in mijzelf` — Verwijderd

##### `Subdoel Financien` — 🔴 Verwijderd

**Literals:**

- 🔴 `ik ben gestart met de hulp voor mijn schulden` — Verwijderd
- 🔴 `ik heb geen financiele belemmeringen om aan het werk te gaan` — Verwijderd
- 🔴 `ik heb hulp bij het regelen van mijn financien` — Verwijderd
- 🔴 `ik heb overzicht over mijn financiele situatie en het lukt mij om rond te komen` — Verwijderd

##### `Subdoel Justitie` — 🔴 Verwijderd

**Literals:**

- 🔴 `ik heb mijn penitentair programma succesvol afgerond` — Verwijderd
- 🔴 `ik weet wat mijn mogelijkheden zijn met mijn justitiele verleden` — Verwijderd

##### `Subdoel lichamelijke gezondheid` — 🔴 Verwijderd

**Literals:**

- 🔴 `ik ben onder behandeling voor mijn lichamelijke klachten` — Verwijderd
- 🔴 `ik heb een beoordeling arbeidsvermogen aangevraagd bij het UWV` — Verwijderd
- 🔴 `ik heb hulp gevraagd voor mijn lichamelijke klachten` — Verwijderd
- 🔴 `ik heb vertrouwen in mijzelf` — Verwijderd
- 🔴 `ik weet wat mijn mogelijkheden zijn ondanks mijn lichamelijke klachten` — Verwijderd

##### `Subdoel ondernemen` — 🔴 Verwijderd

**Literals:**

- 🔴 `Mijn BBZ aanvraag is toegekend` — Verwijderd
- 🔴 `ik heb een ondernemingsplan geschreven` — Verwijderd
- 🔴 `ik heb mijn BBZ aanvraag ingediend` — Verwijderd
- 🔴 `ik weet of ik in aanmerking kom om te ondernemen vanuit bijstand` — Verwijderd

##### `Subdoel opleiding volgen` — 🔴 Verwijderd

**Literals:**

- 🔴 `ik ben gestart met een opleiding` — Verwijderd
- 🔴 `ik weet welke opleiding past bij mijn mogelijkheden` — Verwijderd

##### `Subdoel passende dagbesteding hebben (maatschappelijk fit worden)` — 🔴 Verwijderd

**Literals:**

- 🔴 `ik ben gestart met een passende dagbesteding` — Verwijderd

##### `Subdoel psychische gezondheid` — 🔴 Verwijderd

**Literals:**

- 🔴 `ik ben onder behandeling voor mijn psychische klachten` — Verwijderd
- 🔴 `ik heb een beoordeling arbeidsvermogen aangevraagd bij het UWV` — Verwijderd
- 🔴 `ik heb hulp gevraagd voor mijn psychische klachten` — Verwijderd
- 🔴 `ik heb vertrouwen in mijzelf` — Verwijderd
- 🔴 `ik weet wat mijn mogelijkkheden zijn ondanks de psychische klachten` — Verwijderd

##### `Subdoel Taal` — 🔴 Verwijderd

**Literals:**

- 🔴 `ik beheers de Nederlandse taal op het voor mij hoogst haalbare niveau` — Verwijderd
- 🔴 `ik beheers de Nederlandse taal voldoende om een volgende stap te kunnen zetten` — Verwijderd
- 🔴 `ik weet wat mijn Nederlands taalniveau is` — Verwijderd

##### `Subdoel taalvaardigheden opdoen` — 🔴 Verwijderd

**Literals:**

- 🔴 `ik beheers de nederlandse taal voldoende om aan het werk te gaan of te ondernemen` — Verwijderd

##### `Subdoel verslaving` — 🔴 Verwijderd

**Literals:**

- 🔴 `Ik heb vertrouwen in mijzelf` — Verwijderd
- 🔴 `ik ben onder behandeling voor mijn verslavingsproblematiek` — Verwijderd
- 🔴 `ik heb hulp gevraagd voor mijn verslavingsproblematiek` — Verwijderd
- 🔴 `ik weet wat mijn mogelijkheden zijn ondanks de verslavingsproblematiek` — Verwijderd

##### `Subdoel vrijwilligerswerk doen (maatschappelijk fit worden)` — 🔴 Verwijderd

**Literals:**

- 🔴 `ik ben gestart met vrijwilligerswerk` — Verwijderd

##### `Subdoel Werkervaring opdoen (werkfit worden)` — 🔴 Verwijderd

**Literals:**

- 🔴 `ik heb opgebouwd in het aantal uren wat ik kan werken` — Verwijderd
- 🔴 `ik heb werkervaring opgedaan in een functie` — Verwijderd
- 🔴 `ik weet hoeveel uren ik kan werken` — Verwijderd
- 🔴 `ik weet wat mijn kwaltiteiten zijn` — Verwijderd

##### `Subdoel Werknemersvaardigheden ontwikkelen (werkfit worden)` — 🔴 Verwijderd

**Literals:**

- 🔴 `ik heb een werkritme` — Verwijderd
- 🔴 `ik heb opgebouwd in het aantal uren wat ik kan werken` — Verwijderd
- 🔴 `ik weet hoeveel uren ik kan werken` — Verwijderd
- 🔴 `ik weet wat er van mijn verwacht wordt als werknemer` — Verwijderd
- 🔴 `ik weet wat mijn kwaliteiten zijn` — Verwijderd

##### `Subdoel woonsituatie` — 🔴 Verwijderd

**Literals:**

- 🔴 `ik heb ervoor gezorgd dat mijn woonsituatie verbeterd` — Verwijderd
- 🔴 `ik heb hulp gevraagd om mijn woonsituatie te verbeteren` — Verwijderd

##### `Subdoel zorgtaken` — 🔴 Verwijderd

**Literals:**

- 🔴 `ik heb kinderopvang voor mijn kinderen` — Verwijderd
- 🔴 `ik kan mijn zorgtaken (mantelzorg) overdragen aan anderen` — Verwijderd
- 🔴 `ik krijg betaald voor mijn werkzaamheden als mantelzorger (vanuit PGB)` — Verwijderd
- 🔴 `ik weet hoe ik mijn zorgtaken kan combineren met een baan, opleiding of andere activiteit` — Verwijderd
- 🔴 `ik weet of ik (vanuit PGB) betaald kan krijgen voor mijn werkzaamheden als mantelzorger` — Verwijderd

##### `UitkomstLeerbaarheidstoets` — 🔴 Verwijderd

**Literals:**

- 🔴 `B1-route` — Verwijderd
- 🔴 `Onderwijsroute` — Verwijderd
- 🔴 `Z-route` — Verwijderd

##### `WordtBehandeldAls` — 🔴 Verwijderd

**Literals:**

- 🔴 `AsielStatushouder` — Verwijderd
- 🔴 `GezinsMigrant` — Verwijderd
- 🔴 `OverigeMigrant` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `Aandachtspunt ` → `Subdoel Aandachtspunt`
- 🔴 Verwijderd: `Aanvraag verlenging Inburgeringstermijn` «beoordeling Aanvraag» → `Inburgeringstermijn`
- 🔴 Verwijderd: `Aanvraag verlenging Inburgeringstermijn` → `Verlengingsgrond`
- 🔴 Verwijderd: `Asielstatushouder` «bezit» → `ICT-Vaardigheid`
- 🔴 Verwijderd: `Asielstatushouder` «heeft aangevraagd» → `Diplomawaardering`
- 🔴 Verwijderd: `Asielstatushouder` «heeft gevolgd» → `Educatie`
- 🔴 Verwijderd: `Asielstatushouder` «heeft gevolgd» → `Training`
- 🔴 Verwijderd: `Asielstatushouder` «heeft» → `Taalvaardigheid`
- 🔴 Verwijderd: `Asielstatushouder` «is gekoppeld aan» → `Gemeente`
- 🔴 Verwijderd: `Asielstatushouder` «is gekoppeld aan» → `Gemeente`
- 🔴 Verwijderd: `Asielstatushouder` «neemt deel» → `Voorbereiding op Inburgering`
- 🔴 Verwijderd: `Asielstatushouder` «verblijft» → `Verblijfplaats AZC`
- 🔴 Verwijderd: `Asielstatushouder` → `Werk`
- 🔴 Verwijderd: `B1-route` «onderdeel van» → `Leerroute`
- 🔴 Verwijderd: `Brede Intake` «heeft» → `Leerroute`
- 🔴 Verwijderd: `Brede Intake` «onderdeel van» → `Inburgeringstraject`
- 🔴 Verwijderd: `Examen` «Afgerond met» → `Inburgeringstraject`
- 🔴 Verwijderd: `Examenonderdeel` → `Examen`
- 🔴 Verwijderd: `Inburgeraar` «heeft een» → `Inburgeringsplicht`
- 🔴 Verwijderd: `Inburgeraar` «heeft» → `Aandachtspunt `
- 🔴 Verwijderd: `Inburgeraar` «heeft» → `Aanvraag verlenging Inburgeringstermijn`
- 🔴 Verwijderd: `Inburgeraar` «heeft» → `Hoofddoel`
- 🔴 Verwijderd: `Inburgeraar` «heeft» → `Ontwikkelwens `
- 🔴 Verwijderd: `InburgeringsAanbod` «voor» → `Inburgeraar`
- 🔴 Verwijderd: `Inburgeringsplicht` «heeft» → `Inburgeringstermijn`
- 🔴 Verwijderd: `Inburgeringsplicht` «Ontheffing» → `Ontheffing`
- 🔴 Verwijderd: `Inburgeringsplicht` «Vrijstelling» → `Vrijstelling`
- 🔴 Verwijderd: `Inburgeringstraject` «Heeft» → `Inburgeringsplicht`
- 🔴 Verwijderd: `Leerroute` «afgesproken in» → `PIP`
- 🔴 Verwijderd: `MAP` «Onderdeel van» → `Leerroute`
- 🔴 Verwijderd: `Ontheffing` «ontheffing voor» → `Examenonderdeel`
- 🔴 Verwijderd: `Ontwikkelwens ` → `Subdoel Ontwikkelwens`
- 🔴 Verwijderd: `PIP` «bevat» → `InburgeringsAanbod`
- 🔴 Verwijderd: `PVT` «Onderdeel van» → `Leerroute`
- 🔴 Verwijderd: `Voorbereiding op Inburgering` «bestaat uit» → `Introductiemodule`
- 🔴 Verwijderd: `Vrijstelling` «vrijstelling voor» → `Examenonderdeel`
- 🔴 Verwijderd: `Z-route` «heeft (onderdeel van)» → `Leerroute`

#### Generalisaties

- 🔴 Verwijderd: `Asielstatushouder` ⟶ `Inburgeraar`
- 🔴 Verwijderd: `Gezinsmigrant en Overige migrant
` ⟶ `Inburgeraar`
- 🔴 Verwijderd: `Inburgeraar` ⟶ `Vreemdeling`
- 🔴 Verwijderd: `Vreemdeling` ⟶ `NatuurlijkPersoon`

<a id="structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomendienstendatatypes"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Diensten/Datatypes

#### Enumeraties

##### `CdSrtKostenBijzBijstand` — 🔴 Verwijderd

##### `CdTypeVerstrekkingsvorm` — 🔴 Verwijderd

##### `CodeSTORKbetrouwbaarheid` — 🔴 Verwijderd

##### `OnderdeelDienstTypeRubriek` — 🔴 Verwijderd

##### `Referteperiodebepalingtype` — 🔴 Verwijderd

##### `SoortAanvraag` — 🔴 Verwijderd

##### `SoortBetaling` — 🔴 Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomendienstenmodel-diensten"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Diensten/Model Diensten

#### Classes

##### `Aanvraag` — 🔴 Verwijderd

##### `Aanvraagtype` — 🔴 Verwijderd

##### `Beschikking` — 🔴 Verwijderd

##### `Besluit` — 🔴 Verwijderd

##### `Betalingsblokkade` — 🔴 Verwijderd

##### `Dienst` — 🔴 Verwijderd

##### `Diensttype` — 🔴 Verwijderd

##### `Individuele plicht` — 🔴 Verwijderd

##### `Leveringscomponent` — 🔴 Verwijderd

##### `Leveringscomponenttype` — 🔴 Verwijderd

##### `Leveringsopdracht` — 🔴 Verwijderd

##### `Leveringsspecificatie` — 🔴 Verwijderd

##### `Onderdeel beschikking` — 🔴 Verwijderd

##### `Periodiek dienst Bijz. bijstand` — 🔴 Verwijderd

##### `Recht` — 🔴 Verwijderd

##### `Referteperiode` — 🔴 Verwijderd

##### `Regeling` — 🔴 Verwijderd

##### `Uitsluitingsgrond` — 🔴 Verwijderd

##### `Verstrekkingsvorm` — 🔴 Verwijderd

##### `Voorliggende voorziening` — 🔴 Verwijderd

##### `Voorwaarde` — 🔴 Verwijderd

##### `Voorwaardetype` — 🔴 Verwijderd

#### Associaties

- 🔴 Verwijderd: `Aanvraag` «leidt tot» → `Besluit`
- 🔴 Verwijderd: `Aanvraagtype` «beschrijft» → `Aanvraag`
- 🔴 Verwijderd: `Aanvraagtype` «betreft» → `Diensttype`
- 🔴 Verwijderd: `Beschikking` «bevat» → `Onderdeel beschikking`
- 🔴 Verwijderd: `Besluit` «initieert» → `Dienst`
- 🔴 Verwijderd: `Besluit` «leidt tot» → `Beschikking`
- 🔴 Verwijderd: `Dienst` «heeft» → `Referteperiode`
- 🔴 Verwijderd: `Dienst` «ondergaat» → `Betalingsblokkade`
- 🔴 Verwijderd: `Dienst` «vereist» → `Individuele plicht`
- 🔴 Verwijderd: `Diensttype` «beschrijft» → `Dienst`
- 🔴 Verwijderd: `Diensttype` «bevat» → `Onderdeel beschikking`
- 🔴 Verwijderd: `Diensttype` «heeft» → `Leveringscomponenttype`
- 🔴 Verwijderd: `Diensttype` «heeft» → `Verstrekkingsvorm`
- 🔴 Verwijderd: `Diensttype` «vereist» → `Voorwaardetype`
- 🔴 Verwijderd: `Leveringscomponent` «heeft» → `Kostenplaats`
- 🔴 Verwijderd: `Leveringscomponent` «Leveringscomponent levert Vordering» → `Vordering`
- 🔴 Verwijderd: `Leveringscomponenttype` «beschrijft» → `Leveringscomponent`
- 🔴 Verwijderd: `Leveringsopdracht` «bestaat uit» → `Leveringsspecificatie`
- 🔴 Verwijderd: `Leveringsopdracht` «heeft» → `Verstrekkingsvorm`
- 🔴 Verwijderd: `Leveringsopdracht` «in kader van» → `Dienst`
- 🔴 Verwijderd: `Leveringsspecificatie` «bestaat uit» → `Leveringscomponent`
- 🔴 Verwijderd: `Recht` «is gebaseerd op» → `Voorwaarde`
- 🔴 Verwijderd: `Recht` «is grondslag voor» → `Besluit`
- 🔴 Verwijderd: `Regeling` «bevat» → `Diensttype`
- 🔴 Verwijderd: `Voorwaarde` «is opgebouwd uit» → `Voorwaarde`
- 🔴 Verwijderd: `Voorwaardetype` «beschrijft» → `Voorwaarde`

#### Generalisaties

- 🔴 Verwijderd: `Uitsluitingsgrond` ⟶ `Voorwaarde`
- 🔴 Verwijderd: `Voorliggende voorziening` ⟶ `Voorwaarde`

<a id="structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomenmodel-inkomen"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Model Inkomen

#### Classes

##### `Component` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bedrag` — Verwijderd
- 🔴 `begindatumBetrekkingop` — Verwijderd
- 🔴 `debetCredit` — Verwijderd
- 🔴 `eindatumBetrekkingop` — Verwijderd
- 🔴 `groep` — Verwijderd
- 🔴 `groepcode` — Verwijderd
- 🔴 `grootboekcode` — Verwijderd
- 🔴 `grootboekomschrijving` — Verwijderd
- 🔴 `kostenplaats` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `rekeningNummer` — Verwijderd
- 🔴 `toelichting` — Verwijderd

##### `ComponentSoort` — 🔴 Verwijderd

**Attributen:**

- 🔴 `componentcode` — Verwijderd
- 🔴 `kolom` — Verwijderd
- 🔴 `kolomcode` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `regeling` — Verwijderd
- 🔴 `regelingcode` — Verwijderd

##### `Huisvestingsoort` — 🔴 Verwijderd

**Attributen:**

- 🔴 `begindatumGeldigheid` — Verwijderd
- 🔴 `einddatumGeldigheid` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `soorthuisvestingCode` — Verwijderd

##### `Inkomensvoorziening` — 🔴 Verwijderd

**Attributen:**

- 🔴 `administratieveEinddatum` — Verwijderd
- 🔴 `administratieveStartdatum` — Verwijderd
- 🔴 `bedrag` — Verwijderd
- 🔴 `betalingsmomentcode` — Verwijderd
- 🔴 `code` — Verwijderd
- 🔴 `datumToekenning` — Verwijderd
- 🔴 `eenmalig` — Verwijderd
- 🔴 `einddatum` — Verwijderd
- 🔴 `groep` — Verwijderd
- 🔴 `indicatieBlokkering` — Verwijderd
- 🔴 `indicatieStudietoeslag` — Verwijderd
- 🔴 `indicatieUitkeringSplitsen` — Verwijderd
- 🔴 `indicatieUitkeringsspecificatie` — Verwijderd
- 🔴 `ingangsdatum` — Verwijderd
- 🔴 `toekenningsdatum` — Verwijderd
- 🔴 `versterkkingsvorm` — Verwijderd
- 🔴 `verwerktTotEnMetDatum` — Verwijderd

##### `Inkomensvoorzieningsoort` — 🔴 Verwijderd

**Attributen:**

- 🔴 `code` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `regeling` — Verwijderd
- 🔴 `regelingscode` — Verwijderd
- 🔴 `vergoeding` — Verwijderd
- 🔴 `vergoedingscode` — Verwijderd
- 🔴 `wet` — Verwijderd

##### `RedenBlokkering` — 🔴 Verwijderd

**Attributen:**

- 🔴 `begindatumGeldigheid` — Verwijderd
- 🔴 `einddatumGeldigheid` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `redenBlokkeringCode` — Verwijderd

##### `RedenInstroom` — 🔴 Verwijderd

**Attributen:**

- 🔴 `begindatumGeldigheid` — Verwijderd
- 🔴 `CBS-code` — Verwijderd
- 🔴 `CBS-omschrijving` — Verwijderd
- 🔴 `einddatumGeldigheid` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `redenInstroomCode` — Verwijderd

##### `RedenUitstroom` — 🔴 Verwijderd

**Attributen:**

- 🔴 `begindatumGeldigheid` — Verwijderd
- 🔴 `CBS-code` — Verwijderd
- 🔴 `CBS-omschrijving` — Verwijderd
- 🔴 `einddatumGeldigheid` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `redenUitstroomCode` — Verwijderd

##### `Regeling` — 🔴 Verwijderd

**Attributen:**

- 🔴 `einddatum` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `startdatum` — Verwijderd
- 🔴 `toekenningsdatum` — Verwijderd

##### `Regelingsoort` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `UitkeringsRun` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumRun` — Verwijderd
- 🔴 `frequentie` — Verwijderd
- 🔴 `periodeRun` — Verwijderd
- 🔴 `soortRun` — Verwijderd

#### Enumeraties

##### `Wet` — 🔴 Verwijderd

**Literals:**

- 🔴 `Andere wet` — Verwijderd
- 🔴 `Bijzondere Bijstand` — Verwijderd
- 🔴 `I.O.A.W./I.O.A.Z.` — Verwijderd
- 🔴 `Jeugdwet` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Niet van toepassing` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Participatiewet PW-I` — Verwijderd
- 🔴 `Wmo` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `Component` «heeft» → `UitkeringsRun`
- 🔴 Verwijderd: `Component` «is van soort» → `ComponentSoort`
- 🔴 Verwijderd: `Inkomensvoorziening` «is opgebouwd uit» → `Component`
- 🔴 Verwijderd: `Inkomensvoorziening` «redenBlokkering» → `RedenBlokkering`
- 🔴 Verwijderd: `Inkomensvoorziening` «redenInstroom» → `RedenInstroom`
- 🔴 Verwijderd: `Inkomensvoorziening` «redenUitstroom» → `RedenUitstroom`
- 🔴 Verwijderd: `Inkomensvoorziening` «soortHuisvesting» → `Huisvestingsoort`
- 🔴 Verwijderd: `Inkomensvoorzieningsoort` «is soort voorziening» → `Inkomensvoorziening`
- 🔴 Verwijderd: `Regeling` «is regelingsoort» → `Regelingsoort`

<a id="structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomennormafwijkingdatatypes"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Normafwijking/Datatypes

#### Enumeraties

##### `CodeRedenMaatregel` — 🔴 Verwijderd

##### `Predicaat` — 🔴 Verwijderd

##### `StdIndJN` — 🔴 Verwijderd

##### `TypeMaatregel` — 🔴 Verwijderd

##### `TypeNormafwijking` — 🔴 Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomennormafwijkingmodel-normafwijking"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Normafwijking/Model Normafwijking

#### Classes

##### `Afwijkende maatregel` — 🔴 Verwijderd

##### `Boete` — 🔴 Verwijderd

##### `Maatregel` — 🔴 Verwijderd

##### `Maatregel op uitkering` — 🔴 Verwijderd

##### `Normafwijking` — 🔴 Verwijderd

#### Associaties

- 🔴 Verwijderd: `Afwijkende maatregel` «refereert» → `Maatregel op uitkering`
- 🔴 Verwijderd: `Normafwijking` «Normafwijking leidt tot Maatregel» → `Maatregel`

#### Generalisaties

- 🔴 Verwijderd: `Afwijkende maatregel` ⟶ `Maatregel`
- 🔴 Verwijderd: `Boete` ⟶ `Maatregel`
- 🔴 Verwijderd: `Maatregel op uitkering` ⟶ `Maatregel`

<a id="structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomenreden-aanvraagdatatypes"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Reden aanvraag/Datatypes

#### Enumeraties

##### `CdRedenAanvraagANWaangevraagd` — 🔴 Verwijderd

##### `CdRedenAanvraagANWafgewezenReden` — 🔴 Verwijderd

##### `CdRedenAanvraagContractperiode` — 🔴 Verwijderd

##### `CdRedenAanvraagEindeBijstand` — 🔴 Verwijderd

##### `CdRedenAanvraagEindeEigenBedrijf` — 🔴 Verwijderd

##### `CdRedenAanvraagEindeUitkering` — 🔴 Verwijderd

##### `CdRedenAanvraagEindeUitkeringReden` — 🔴 Verwijderd

##### `CdRedenAanvraagEindeWerk` — 🔴 Verwijderd

##### `CdRedenAanvraagOnvoldoendeInkomen` — 🔴 Verwijderd

##### `CdRedenAanvraagVerblijfstatus` — 🔴 Verwijderd

##### `CdRedenAanvraagWijzigingGezin` — 🔴 Verwijderd

##### `CdRedenAanvraagWwafgewezen` — 🔴 Verwijderd

##### `CdRedenAanvraagWWgevraagd` — 🔴 Verwijderd

##### `CdRedenAanvraagZelfstandige` — 🔴 Verwijderd

##### `CodeRedenAfwijkendeStartdatum` — 🔴 Verwijderd

##### `RedenKwijtscheldingVordering` — 🔴 Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomenreden-aanvraagreden-aanvraag"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Reden aanvraag/Reden aanvraag

#### Classes

##### `Andere reden afwijkende startdatum` — 🔴 Verwijderd

##### `Andere reden verzoek` — 🔴 Verwijderd

##### `Diensten::Aanvraag` — 🔴 Verwijderd

##### `Diensten::Aanvraag levensonderhoud` — 🔴 Verwijderd

##### `Gestopt betaald werk` — 🔴 Verwijderd

##### `Gestopt of verkocht eigen bedrijf` — 🔴 Verwijderd

##### `Gestopte bijstanduitkering` — 🔴 Verwijderd

##### `Gestopte detentie` — 🔴 Verwijderd

##### `Gestopte of verlaagde alimentatie` — 🔴 Verwijderd

##### `Gestopte studiefinanciering` — 🔴 Verwijderd

##### `Gestopte uitkering` — 🔴 Verwijderd

##### `Ingang bijstandsuitkering` — 🔴 Verwijderd

##### `Levenssituatie::Levenssituatie` — 🔴 Verwijderd

##### `Opname instelling` — 🔴 Verwijderd

##### `Overleden partner` — 🔴 Verwijderd

##### `Reden aanvraag` — 🔴 Verwijderd

##### `Reden aanvraag Levensonderhoud` — 🔴 Verwijderd

##### `Reden afwijkende startdatum` — 🔴 Verwijderd

##### `Verbroken relatie` — 🔴 Verwijderd

##### `Vertrek uit asielzoekerscentrum` — 🔴 Verwijderd

##### `Wachten beslissing instantie` — 🔴 Verwijderd

##### `Wachten DigiD` — 🔴 Verwijderd

#### Associaties

- 🔴 Verwijderd: `Diensten::Aanvraag` «Is aanleiding tot» → `Reden aanvraag`
- 🔴 Verwijderd: `Ingang bijstandsuitkering` «Bevat» → `Diensten::Aanvraag levensonderhoud`
- 🔴 Verwijderd: `Ingang bijstandsuitkering` «bevat» → `Reden afwijkende startdatum`
- 🔴 Verwijderd: `Levenssituatie::Levenssituatie` «Is reden tot» → `Reden aanvraag`

#### Generalisaties

- 🔴 Verwijderd: `Andere reden afwijkende startdatum` ⟶ `Reden afwijkende startdatum`
- 🔴 Verwijderd: `Andere reden verzoek` ⟶ `Reden aanvraag Levensonderhoud`
- 🔴 Verwijderd: `Diensten::Aanvraag levensonderhoud` ⟶ `Diensten::Aanvraag`
- 🔴 Verwijderd: `Gestopt betaald werk` ⟶ `Reden aanvraag Levensonderhoud`
- 🔴 Verwijderd: `Gestopt of verkocht eigen bedrijf` ⟶ `Reden aanvraag Levensonderhoud`
- 🔴 Verwijderd: `Gestopte bijstanduitkering` ⟶ `Reden aanvraag Levensonderhoud`
- 🔴 Verwijderd: `Gestopte detentie` ⟶ `Reden aanvraag Levensonderhoud`
- 🔴 Verwijderd: `Gestopte of verlaagde alimentatie` ⟶ `Reden aanvraag Levensonderhoud`
- 🔴 Verwijderd: `Gestopte studiefinanciering` ⟶ `Reden aanvraag Levensonderhoud`
- 🔴 Verwijderd: `Gestopte uitkering` ⟶ `Reden aanvraag Levensonderhoud`
- 🔴 Verwijderd: `Opname instelling` ⟶ `Reden afwijkende startdatum`
- 🔴 Verwijderd: `Overleden partner` ⟶ `Reden aanvraag Levensonderhoud`
- 🔴 Verwijderd: `Reden aanvraag Levensonderhoud` ⟶ `Reden aanvraag`
- 🔴 Verwijderd: `Verbroken relatie` ⟶ `Reden aanvraag Levensonderhoud`
- 🔴 Verwijderd: `Vertrek uit asielzoekerscentrum` ⟶ `Reden aanvraag Levensonderhoud`
- 🔴 Verwijderd: `Wachten beslissing instantie` ⟶ `Reden afwijkende startdatum`
- 🔴 Verwijderd: `Wachten DigiD` ⟶ `Reden afwijkende startdatum`

<a id="structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomenterug--en-invorderingdatatypes"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Terug- en invordering/Datatypes

#### Enumeraties

##### `Brontype` — 🔴 Verwijderd

##### `CategorieAnderInkomen` — 🔴 Verwijderd

##### `CategorieVorderingCBS` — 🔴 Verwijderd

##### `CdPeriode` — 🔴 Verwijderd

##### `CdPeriodiciteitStatusformulier` — 🔴 Verwijderd

##### `CdRedenAanvraagReden` — 🔴 Verwijderd

##### `CodeSoortDebiteur` — 🔴 Verwijderd

##### `CodeSoortInterventie` — 🔴 Verwijderd

##### `CodeTypeInvorderingsmogelijkheid` — 🔴 Verwijderd

##### `DefaultEnumeratie` — 🔴 Verwijderd

##### `OnderdeelDienstGevalsrubriek` — 🔴 Verwijderd

##### `OrganisatieSoort` — 🔴 Verwijderd

##### `Regeling` — 🔴 Verwijderd

##### `Rekeningtype` — 🔴 Verwijderd

##### `SubCategorieVordering` — 🔴 Verwijderd

##### `Verwerkingsstatus` — 🔴 Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomenterug--en-invorderingmodel-terug--en-invordering"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Terug- en invordering/Model Terug- en invordering

#### Classes

##### `Aflossing` — 🔴 Verwijderd

##### `Aflossingsafspraak` — 🔴 Verwijderd

##### `Aflossingsplan` — 🔴 Verwijderd

##### `Afschrijving` — 🔴 Verwijderd

##### `Betaalcomponent` — 🔴 Verwijderd

##### `Boetevordering` — 🔴 Verwijderd

##### `Conservatoir beslag` — 🔴 Verwijderd

##### `Correctie` — 🔴 Verwijderd

##### `Debiteur` — 🔴 Verwijderd

##### `Incassokostenvordering` — 🔴 Verwijderd

##### `Interventie` — 🔴 Verwijderd

##### `Interventieverzoek` — 🔴 Verwijderd

##### `Invorderingsbasis` — 🔴 Verwijderd

##### `Krediethypotheek` — 🔴 Verwijderd

##### `Krediethypotheekvordering` — 🔴 Verwijderd

##### `Kwijtschelding` — 🔴 Verwijderd

##### `Leenbijstand` — 🔴 Verwijderd

##### `Leenbijstandvordering` — 🔴 Verwijderd

##### `Loonbeslagafspraak` — 🔴 Verwijderd

##### `Rechtmaand` — 🔴 Verwijderd

##### `Rentevordering` — 🔴 Verwijderd

##### `Restitutie` — 🔴 Verwijderd

##### `Terugvorderingsverzoek` — 🔴 Verwijderd

##### `Uitstel aflossing` — 🔴 Verwijderd

##### `Vermindering terugvordering` — 🔴 Verwijderd

##### `Verrekening` — 🔴 Verwijderd

##### `Verwijtbare vordering` — 🔴 Verwijderd

##### `Vordering` — 🔴 Verwijderd

##### `Vorderingscomponent` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Priotype` — Verwijderd

#### Enumeraties

##### `Verwerkingsstatus` — 🔴 Verwijderd

#### Associaties

- 🔴 Verwijderd: `Aflossing` «Aflossing is gedaan vanuit Bankrekening» → `Bankrekening`
- 🔴 Verwijderd: `Aflossingsafspraak` «Aflossingsafspraak betreft Vordering» → `Vordering`
- 🔴 Verwijderd: `Aflossingsafspraak` «Aflossingsafspraak bevat Aflossing» → `Aflossing`
- 🔴 Verwijderd: `Aflossingsplan` «Aflossingsplan ondergaat Uitstel aflossing» → `Uitstel aflossing`
- 🔴 Verwijderd: `Aflossingsplan` «bevat» → `Aflossingsafspraak`
- 🔴 Verwijderd: `Aflossingsplan` «is gebaseerd op» → `Invorderingsbasis`
- 🔴 Verwijderd: `Boetevordering` «is gerelateerd aan» → `Verwijtbare vordering`
- 🔴 Verwijderd: `Debiteur` «Debiteur heeft aangegaan Leenbijstand» → `Leenbijstand`
- 🔴 Verwijderd: `Debiteur` «Debiteur heeft afgesloten Krediethypotheek» → `Krediethypotheek`
- 🔴 Verwijderd: `Debiteur` «Debiteur heeft Invorderingsbasis» → `Invorderingsbasis`
- 🔴 Verwijderd: `Debiteur` «Debiteur heeft Vordering» → `Vordering`
- 🔴 Verwijderd: `Debiteur` «heeft» → `Aflossingsplan`
- 🔴 Verwijderd: `Debiteur` «verwijst» → `Client`
- 🔴 Verwijderd: `Incassokostenvordering` «Incassokostenvordering is gerelateerd aan Vordering» → `Vordering`
- 🔴 Verwijderd: `Interventieverzoek` «heeft betrekking op» → `Aflossingsafspraak`
- 🔴 Verwijderd: `Interventieverzoek` «initieert» → `Interventie`
- 🔴 Verwijderd: `Krediethypotheek` «is origine van» → `Krediethypotheekvordering`
- 🔴 Verwijderd: `Leenbijstand` «is origine van» → `Leenbijstandvordering`
- 🔴 Verwijderd: `Rechtmaand` «Rechtmaand bevat Betaalcomponent» → `Betaalcomponent`
- 🔴 Verwijderd: `Rentevordering` «Rentevordering is gerelateerd aan Vordering» → `Vordering`
- 🔴 Verwijderd: `Terugvorderingsverzoek` «betreft» → `Client`
- 🔴 Verwijderd: `Terugvorderingsverzoek` «leidt tot» → `Vordering`
- 🔴 Verwijderd: `Terugvorderingsverzoek` «Terugvorderingsverzoek betreft Dienst» → `Dienst`
- 🔴 Verwijderd: `Terugvorderingsverzoek` «Terugvorderingsverzoek bevat Rechtmaand» → `Rechtmaand`
- 🔴 Verwijderd: `Vordering` «Vordering bevat Aflossing» → `Aflossing`
- 🔴 Verwijderd: `Vordering` «Vordering bevat Afschrijving» → `Afschrijving`
- 🔴 Verwijderd: `Vordering` «Vordering bevat Correctie» → `Correctie`
- 🔴 Verwijderd: `Vordering` «Vordering bevat Kwijtschelding» → `Kwijtschelding`
- 🔴 Verwijderd: `Vordering` «Vordering bevat Restitutie» → `Restitutie`
- 🔴 Verwijderd: `Vordering` «Vordering bevat Vermindering terugvordering» → `Vermindering terugvordering`
- 🔴 Verwijderd: `Vordering` «Vordering bevat Vorderingscomponent» → `Vorderingscomponent`
- 🔴 Verwijderd: `Vordering` «Vordering is gerelateerd aan Conservatoir beslag» → `Conservatoir beslag`
- 🔴 Verwijderd: `Vorderingscomponent` «Vorderingscomponent bevat Rechtmaand» → `Rechtmaand`

#### Generalisaties

- 🔴 Verwijderd: `Boetevordering` ⟶ `Vordering`
- 🔴 Verwijderd: `Incassokostenvordering` ⟶ `Vordering`
- 🔴 Verwijderd: `Krediethypotheek` ⟶ `Hypotheek`
- 🔴 Verwijderd: `Krediethypotheekvordering` ⟶ `Vordering`
- 🔴 Verwijderd: `Leenbijstandvordering` ⟶ `Vordering`
- 🔴 Verwijderd: `Loonbeslagafspraak` ⟶ `Aflossingsafspraak`
- 🔴 Verwijderd: `Rentevordering` ⟶ `Vordering`
- 🔴 Verwijderd: `Verrekening` ⟶ `Vordering`
- 🔴 Verwijderd: `Verwijtbare vordering` ⟶ `Vordering`

<a id="structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeinjeugdbescherming-en-reclasseringmodel-jeugdbescherming"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Jeugdbescherming en reclassering/Model Jeugdbescherming

#### Classes

##### `Informering` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datum` — Verwijderd
- 🔴 `indicatieGeinformeerd` — Verwijderd
- 🔴 `reactie` — Verwijderd
- 🔴 `redenNietGeinformeerd` — Verwijderd

##### `Leefgebied` — 🔴 Verwijderd

**Attributen:**

- 🔴 `leefgebiedOmschrijving` — Verwijderd
- 🔴 `toelichting` — Verwijderd

##### `Zorgelijke Situatie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `nadereOmschrijving` — Verwijderd
- 🔴 `sitiuatieschets` — Verwijderd

##### `Zorgmelding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `nadereOmschrijving` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `terugkoppelingGewenst` — Verwijderd
- 🔴 `verzoek` — Verwijderd
- 🔴 `zorgmeldingsoort` — Verwijderd

#### Enumeraties

##### `Enum Sociale Groep` — 🔴 Verwijderd

##### `Enum Sociale Relatie` — 🔴 Verwijderd

##### `enum_Incidenttype` — 🔴 Verwijderd

##### `enum_Leefgebied` — 🔴 Verwijderd

##### `enum_Verzoeksoort` — 🔴 Verwijderd

#### Associaties

- 🔴 Verwijderd: `Informering` «informering» → `NatuurlijkPersoon`
- 🔴 Verwijderd: `Zorgelijke Situatie` «berust op» → `Incident`
- 🔴 Verwijderd: `Zorgelijke Situatie` «toelichting» → `Leefgebied`
- 🔴 Verwijderd: `Zorgmelding` «betreft» → `NatuurlijkPersoon`
- 🔴 Verwijderd: `Zorgmelding` «betrokken professional» → `Medewerker`
- 🔴 Verwijderd: `Zorgmelding` «betrokkenen» → `NatuurlijkPersoon`
- 🔴 Verwijderd: `Zorgmelding` «naar aanleiding van» → `Zorgelijke Situatie`

#### Generalisaties

- 🔴 Verwijderd: `Zorgmelding` ⟶ `AanvraagOfMelding`

<a id="structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeinschuldenschuldhulpverleningdiagram"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Schulden/Schuldhulpverlening/Diagram

#### Classes

##### `Model Vroegsignalering` — 🔴 Verwijderd

##### `Vroegsignalering` — 🔴 Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeinschuldenschuldhulpverleningmodel-schuldhulpverlening"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Schulden/Schuldhulpverlening/Model Schuldhulpverlening

#### Classes

##### `Aanmelding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `crisisinterventie` — Verwijderd
- 🔴 `einddatum` — Verwijderd
- 🔴 `startdatum` — Verwijderd

##### `Begeleiding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `einddatum` — Verwijderd
- 🔴 `soort` — Verwijderd
- 🔴 `startdatum` — Verwijderd

##### `Begeleidingssoort` — 🔴 Verwijderd

**Attributen:**

- 🔴 `soort` — Verwijderd

##### `Contactpersoon` — 🔴 Verwijderd

**Attributen:**

- 🔴 `email` — Verwijderd
- 🔴 `functietitel` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `telefoonnummer` — Verwijderd

##### `Crisisinterventie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `einddatum` — Verwijderd
- 🔴 `startdatum` — Verwijderd

##### `InformatieEnAdvies` — 🔴 Verwijderd

**Attributen:**

- 🔴 `einddatum` — Verwijderd
- 🔴 `startdatum` — Verwijderd

##### `Inkomen` — 🔴 Verwijderd

**Attributen:**

- 🔴 `brutoBedrag` — Verwijderd
- 🔴 `einddatum` — Verwijderd
- 🔴 `inkomenscategorie` — Verwijderd
- 🔴 `inkomstenbron` — Verwijderd
- 🔴 `nettoBedrag` — Verwijderd
- 🔴 `startdatum` — Verwijderd

##### `Intake` — 🔴 Verwijderd

**Attributen:**

- 🔴 `beschikkingsdatum` — Verwijderd
- 🔴 `beschikkingssoort` — Verwijderd
- 🔴 `einddatum` — Verwijderd
- 🔴 `startdatum` — Verwijderd

##### `Leefsituatie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumGeldigTot` — Verwijderd
- 🔴 `datumGeldigVanaf` — Verwijderd

##### `Moratorium` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumAanvraag` — Verwijderd
- 🔴 `datumGoedkeuring` — Verwijderd
- 🔴 `einddatum` — Verwijderd
- 🔴 `startdatum` — Verwijderd

##### `Nazorg` — 🔴 Verwijderd

**Attributen:**

- 🔴 `einddatum` — Verwijderd
- 🔴 `startdatum` — Verwijderd

##### `Ondernemer` — 🔴 Verwijderd

**Attributen:**

- 🔴 `einddatum` — Verwijderd
- 🔴 `startdatum` — Verwijderd

##### `Oplossing` — 🔴 Verwijderd

**Attributen:**

- 🔴 `einddatum` — Verwijderd
- 🔴 `soort` — Verwijderd
- 🔴 `startdatum` — Verwijderd
- 🔴 `vtlb` — Verwijderd

##### `Oplossingssoort` — 🔴 Verwijderd

**Attributen:**

- 🔴 `soort` — Verwijderd

##### `Partner` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumTot` — Verwijderd
- 🔴 `datumVanaf` — Verwijderd
- 🔴 `getrouwdOfGeregistreerdPartner` — Verwijderd
- 🔴 `samenwonend` — Verwijderd

##### `PlanVanAanpak` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumAfronding` — Verwijderd

##### `Schuld` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bedrag` — Verwijderd
- 🔴 `peildatum` — Verwijderd
- 🔴 `schuldsoort` — Verwijderd
- 🔴 `zakelijkeSchuld` — Verwijderd

##### `Schuldeiser` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `peildatum` — Verwijderd

##### `Schuldhulporganisatie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd

##### `Schuldhulptraject` — 🔴 Verwijderd

**Attributen:**

- 🔴 `einddatum` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `startdatum` — Verwijderd
- 🔴 `toekenningsdatum` — Verwijderd
- 🔴 `totaalSchuldbedragBijAanvangSchuld` — Verwijderd

##### `Schuldregeling` — 🔴 Verwijderd

**Attributen:**

- 🔴 `afgewezen` — Verwijderd
- 🔴 `datum` — Verwijderd
- 🔴 `datumVerzoekDwangakkoord` — Verwijderd
- 🔴 `dwangakkoord` — Verwijderd
- 🔴 `ingetrokken` — Verwijderd
- 🔴 `toegekend` — Verwijderd

##### `Stabilisatie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `einddatum` — Verwijderd
- 🔴 `startdatum` — Verwijderd

##### `Uitstroom` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datum` — Verwijderd
- 🔴 `datumBeeindigingsbeschikking` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `reden` — Verwijderd

##### `VoorlopigeVoorziening` — 🔴 Verwijderd

**Attributen:**

- 🔴 `einddatum` — Verwijderd
- 🔴 `startdatum` — Verwijderd

##### `Woningbezit` — 🔴 Verwijderd

**Attributen:**

- 🔴 `einddatum` — Verwijderd
- 🔴 `soort` — Verwijderd
- 🔴 `startdatum` — Verwijderd

##### `WSNP-traject` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumGoedkeuring` — Verwijderd
- 🔴 `datumVerzoek` — Verwijderd
- 🔴 `einddatum` — Verwijderd
- 🔴 `startdatum` — Verwijderd

##### `WSNP-verklaring` — 🔴 Verwijderd

#### Enumeraties

##### `EnumBegeleidingssoort` — 🔴 Verwijderd

**Literals:**

- 🔴 `Beschermingsbewind` — Verwijderd
- 🔴 `Budgetbegeleiding` — Verwijderd
- 🔴 `Budgetbeheer` — Verwijderd
- 🔴 `Budgetcoaching` — Verwijderd
- 🔴 `Lange Termijn Begeleiding (DFD)` — Verwijderd

##### `EnumBeschikkingssoort` — 🔴 Verwijderd

**Literals:**

- 🔴 `Afwijzingsbeschikking` — Verwijderd
- 🔴 `Toelatingsbeschikking` — Verwijderd

##### `EnumHuishoudenssoort` — 🔴 Verwijderd

**Literals:**

- 🔴 `Instituuttioneel Huishouden` — Verwijderd
- 🔴 `Particulier Huishouden` — Verwijderd

##### `EnumOplossingssoort` — 🔴 Verwijderd

**Literals:**

- 🔴 `0%-aanbod` — Verwijderd
- 🔴 `Betalingsregeling` — Verwijderd
- 🔴 `Herfinanciering` — Verwijderd
- 🔴 `Saneringskrediet` — Verwijderd
- 🔴 `Schuldbemiddeling` — Verwijderd

##### `EnumSchuldensoort` — 🔴 Verwijderd

**Literals:**

- 🔴 `Nuts` — Verwijderd
- 🔴 `Overig` — Verwijderd
- 🔴 `Publiek` — Verwijderd
- 🔴 `Zorg` — Verwijderd

##### `EnumUitstroomreden` — 🔴 Verwijderd

**Literals:**

- 🔴 `Afgerond` — Verwijderd
- 🔴 `Ingetrokken` — Verwijderd
- 🔴 `Niet passend` — Verwijderd
- 🔴 `Nietverschenen` — Verwijderd
- 🔴 `Overig` — Verwijderd
- 🔴 `Overleden` — Verwijderd
- 🔴 `Verhuisd` — Verwijderd
- 🔴 `Voldoet niet` — Verwijderd
- 🔴 `Zelf` — Verwijderd

##### `EnumWoningbezit` — 🔴 Verwijderd

**Literals:**

- 🔴 `Eigen Woning` — Verwijderd
- 🔴 `Huurwoning` — Verwijderd
- 🔴 `Huurwoning geen huurtoeslag` — Verwijderd
- 🔴 `Huurwoning wel huurtoeslag` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `Aanmelding` «resulteert in» → `Intake`
- 🔴 Verwijderd: `Begeleiding` «resulteert in» → `Nazorg`
- 🔴 Verwijderd: `Begeleiding` «soort» → `Begeleidingssoort`
- 🔴 Verwijderd: `Intake` «resulteert in» → `Begeleiding`
- 🔴 Verwijderd: `Intake` «resulteert in» → `InformatieEnAdvies`
- 🔴 Verwijderd: `Intake` «resulteert in» → `Stabilisatie`
- 🔴 Verwijderd: `Leefsituatie` «heeft» → `Inkomen`
- 🔴 Verwijderd: `Leefsituatie` «heeft» → `Partner`
- 🔴 Verwijderd: `Leefsituatie` «heeft» → `Woningbezit`
- 🔴 Verwijderd: `Leefsituatie` «is» → `Ondernemer`
- 🔴 Verwijderd: `Oplossing` «resulteert in» → `Nazorg`
- 🔴 Verwijderd: `Oplossing` «soort» → `Oplossingssoort`
- 🔴 Verwijderd: `Schuld` «schuld bij» → `Schuldeiser`
- 🔴 Verwijderd: `Schuldhulporganisatie` «dienstverlening» → `Begeleidingssoort`
- 🔴 Verwijderd: `Schuldhulporganisatie` «dienstverlening» → `Oplossingssoort`
- 🔴 Verwijderd: `Schuldhulporganisatie` «heeft» → `Contactpersoon`
- 🔴 Verwijderd: `Schuldhulporganisatie` «voert traject uit» → `Schuldhulptraject`
- 🔴 Verwijderd: `Schuldhulptraject` «bevat» → `Aanmelding`
- 🔴 Verwijderd: `Schuldhulptraject` «bevat» → `Begeleiding`
- 🔴 Verwijderd: `Schuldhulptraject` «bevat» → `InformatieEnAdvies`
- 🔴 Verwijderd: `Schuldhulptraject` «bevat» → `Intake`
- 🔴 Verwijderd: `Schuldhulptraject` «bevat» → `Nazorg`
- 🔴 Verwijderd: `Schuldhulptraject` «bevat» → `Oplossing`
- 🔴 Verwijderd: `Schuldhulptraject` «bevat» → `Schuldregeling`
- 🔴 Verwijderd: `Schuldhulptraject` «bevat» → `Stabilisatie`
- 🔴 Verwijderd: `Schuldhulptraject` «heeft traject» → `Client`
- 🔴 Verwijderd: `Schuldhulptraject` «heeft» → `PlanVanAanpak`
- 🔴 Verwijderd: `Schuldhulptraject` «heeft» → `Schuld`
- 🔴 Verwijderd: `Schuldhulptraject` «heeft» → `VoorlopigeVoorziening `
- 🔴 Verwijderd: `Schuldhulptraject` «kan hebben» → `Crisisinterventie`
- 🔴 Verwijderd: `Schuldhulptraject` «kan hebben» → `Moratorium`
- 🔴 Verwijderd: `Schuldhulptraject` «onder verantwoordelijkheid van» → `Gemeente`
- 🔴 Verwijderd: `Schuldhulptraject` «onder verantwoordelijkheid van» → `Gemeente`
- 🔴 Verwijderd: `Schuldhulptraject` «uitstroom» → `Uitstroom`
- 🔴 Verwijderd: `Schuldregeling` «resulteert in» → `Begeleiding`
- 🔴 Verwijderd: `Schuldregeling` «resulteert in» → `Oplossing`
- 🔴 Verwijderd: `Stabilisatie` «resulteert in» → `Begeleiding`
- 🔴 Verwijderd: `Stabilisatie` «resulteert in» → `Schuldregeling`
- 🔴 Verwijderd: `WSNP-traject` «heeft» → `Leefsituatie`

#### Generalisaties

- 🔴 Verwijderd: `Partner` ⟶ `NatuurlijkPersoon`
- 🔴 Verwijderd: `Schuldeiser` ⟶ `Rechtspersoon`
- 🔴 Verwijderd: `Schuldhulporganisatie` ⟶ `NietNatuurlijkPersoon`

<a id="structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeinschuldenvroegsignaleringdiagram"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Schulden/Vroegsignalering/Diagram

#### Classes

##### `Model Vroegsignalering` — 🔴 Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeinschuldenvroegsignaleringmodel-vroegsignalering"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Schulden/Vroegsignalering/Model Vroegsignalering

#### Classes

##### `AanleverendeOrganisatie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `kvk-nummer` — Verwijderd
- 🔴 `naam` — Verwijderd

##### `Contactpersoon` — 🔴 Verwijderd

**Attributen:**

- 🔴 `email` — Verwijderd
- 🔴 `functietitel` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `telefoonnummer` — Verwijderd

##### `Contactpoging` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bereikt` — Verwijderd
- 🔴 `dagdeel` — Verwijderd
- 🔴 `datum` — Verwijderd
- 🔴 `soort` — Verwijderd

##### `Signaalpartner` — 🔴 Verwijderd

**Attributen:**

- 🔴 `type` — Verwijderd

##### `Vroegsignaal` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bedrag` — Verwijderd
- 🔴 `crisissignaal` — Verwijderd
- 🔴 `ontstaansdatum` — Verwijderd
- 🔴 `signaaldatum` — Verwijderd
- 🔴 `status` — Verwijderd
- 🔴 `warmeOverdracht` — Verwijderd

##### `Vroegsignaalzaak` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datum_opgepakt` — Verwijderd
- 🔴 `einddatum_matchingperiode` — Verwijderd
- 🔴 `matchingsdatum` — Verwijderd
- 🔴 `resultaat` — Verwijderd
- 🔴 `startdatum_matchtingperiode` — Verwijderd

#### Enumeraties

##### `EnumContactsoort` — 🔴 Verwijderd

**Literals:**

- 🔴 `Administratief` — Verwijderd
- 🔴 `Afspraak op locatie` — Verwijderd
- 🔴 `Brief` — Verwijderd
- 🔴 `Huisbezoek` — Verwijderd
- 🔴 `Kaartje` — Verwijderd
- 🔴 `Mail` — Verwijderd
- 🔴 `SMS/Whatsapp` — Verwijderd
- 🔴 `Telefoon` — Verwijderd

##### `EnumDagdeel` — 🔴 Verwijderd

**Literals:**

- 🔴 `Avond` — Verwijderd
- 🔴 `Middag` — Verwijderd
- 🔴 `Ochtend` — Verwijderd

##### `EnumEindresultaat` — 🔴 Verwijderd

**Literals:**

- 🔴 `(Budget)advies en/of quick fix` — Verwijderd
- 🔴 `Definitief geen contact kunnen krijgen` — Verwijderd
- 🔴 `Geen reactie na eerder contact` — Verwijderd
- 🔴 `Inwoner al bekend bij schuldhulpverlening` — Verwijderd
- 🔴 `Inwoner heeft al een ander lopend traject` — Verwijderd
- 🔴 `Inwoner heeft zelf al betaald/betalingsregeling getroffen` — Verwijderd
- 🔴 `Inwoner hoeft geen hulp vanuit vroegsignalering` — Verwijderd
- 🔴 `Inwoner is overleden` — Verwijderd
- 🔴 `Niet opgepakt: andere reden` — Verwijderd
- 🔴 `Niet opgepakt: herhaalde melding` — Verwijderd
- 🔴 `Niet opgepakt: onterecht signaal` — Verwijderd
- 🔴 `Persoon is geen inwoner (meer) in de gemeente` — Verwijderd
- 🔴 `Vervolghulp en/of verwijzing financieel` — Verwijderd
- 🔴 `Vervolghulp en/of verwijzing niet financieel` — Verwijderd
- 🔴 `Verwijzing zonder contact` — Verwijderd

##### `EnumSignaalpartner` — 🔴 Verwijderd

**Literals:**

- 🔴 `Belastingdienst` — Verwijderd
- 🔴 `CAK Eigen bijdrage` — Verwijderd
- 🔴 `CAK Zorgverzekeringen` — Verwijderd
- 🔴 `DUO` — Verwijderd
- 🔴 `Dienst Toeslagen` — Verwijderd
- 🔴 `Energie` — Verwijderd
- 🔴 `Huur` — Verwijderd
- 🔴 `Hypotheek` — Verwijderd
- 🔴 `Overige` — Verwijderd
- 🔴 `Water` — Verwijderd
- 🔴 `Zorg` — Verwijderd

##### `EnumSignaalstatus` — 🔴 Verwijderd

**Literals:**

- 🔴 `Inwoner is overleden` — Verwijderd
- 🔴 `Niet opgepakt: andere reden` — Verwijderd
- 🔴 `Niet opgepakt: herhaalde melding` — Verwijderd
- 🔴 `Niet opgepakt: onterecht signaal` — Verwijderd
- 🔴 `Nog niet opgepakt` — Verwijderd
- 🔴 `Persoon is geen inwoner (meer) in de gemeente` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `AanleverendeOrganisatie` «contactpersonen» → `Contactpersoon`
- 🔴 Verwijderd: `Vroegsignaal` «betreft» → `Client`
- 🔴 Verwijderd: `Vroegsignaal` «opgepaktIn» → `Vroegsignaalzaak`
- 🔴 Verwijderd: `Vroegsignaal` «verzondenDoor» → `Signaalpartner`
- 🔴 Verwijderd: `Vroegsignaalzaak` «heeft» → `Contactpoging`
- 🔴 Verwijderd: `Vroegsignaalzaak` «opgepaktDoor» → `NietNatuurlijkPersoon`
- 🔴 Verwijderd: `Vroegsignaalzaak` «opgepaktNamens» → `Gemeente`

#### Generalisaties

- 🔴 Verwijderd: `Signaalpartner` ⟶ `Rechtspersoon`
- 🔴 Verwijderd: `Vroegsignaalzaak` ⟶ `Zaak`

<a id="structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiekdiagram"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Diagram

#### Classes

##### `Uitbreiding Zorgmelding` — 🔴 Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiekmodel-sociaal-domein-generiek"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek

#### Classes

##### `AanvraagStadspas` — 🔴 Verwijderd

##### `Client` — 🔴 Verwijderd

**Attributen:**

- 🔴 `client` — Verwijderd
- 🔴 `code` — Verwijderd
- 🔴 `gezagsdragerGekend` — Verwijderd
- 🔴 `juridischeStatus` — Verwijderd
- 🔴 `wettelijkeVertegenwoordiging` — Verwijderd

##### `Clientbegeleider` — 🔴 Verwijderd

**Attributen:**

- 🔴 `begeleiderscode` — Verwijderd

##### `Gerechtelijke uitspraak` — 🔴 Verwijderd

##### `Gezagsverhouding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `einddatum` — Verwijderd
- 🔴 `indicatie curateleregister` — Verwijderd
- 🔴 `indicatie gezag minderjarige` — Verwijderd
- 🔴 `ingangsdatum` — Verwijderd

##### `Huishouden` — 🔴 Verwijderd

**Attributen:**

- 🔴 `soort` — Verwijderd

##### `Incident` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumTijdTot` — Verwijderd
- 🔴 `datumtijdVanaf` — Verwijderd
- 🔴 `locatie` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `soort` — Verwijderd
- 🔴 `toelichting` — Verwijderd

##### `Leverancier` — 🔴 Verwijderd

**Attributen:**

- 🔴 `AGBCode` — Verwijderd
- 🔴 `leverancierscode` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `soortLeverancier` — Verwijderd
- 🔴 `soortLeverancierCode` — Verwijderd

##### `Profiel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumAanvangProfiel` — Verwijderd
- 🔴 `datumEindeProfiel` — Verwijderd
- 🔴 `profielID` — Verwijderd
- 🔴 `profieltype` — Verwijderd

##### `Relatie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `relatiesoort` — Verwijderd

##### `Relatiesoort` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Omschrijving` — Verwijderd

##### `Sociale Groep` — 🔴 Verwijderd

**Attributen:**

- 🔴 `einddatum` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `startdatum` — Verwijderd
- 🔴 `typering` — Verwijderd

##### `Sociale Relatie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `einddatum` — Verwijderd
- 🔴 `startdatum` — Verwijderd
- 🔴 `typering` — Verwijderd

##### `Stadspas` — 🔴 Verwijderd

**Attributen:**

- 🔴 `einddatum` — Verwijderd
- 🔴 `ingangsdatum` — Verwijderd

#### Enumeraties

##### `enum_Incidenttype` — 🔴 Verwijderd

#### Associaties

- 🔴 Verwijderd: `Client` «bezit» → `Bankrekening`
- 🔴 Verwijderd: `Client` «doet aanvraag» → `Aanvraag`
- 🔴 Verwijderd: `Client` «heeft financiele situatie» → `Leefsituatie`
- 🔴 Verwijderd: `Client` «heeft regeling» → `Regeling`
- 🔴 Verwijderd: `Client` «heeft relatie» → `Relatie`
- 🔴 Verwijderd: `Client` «heeft voorziening» → `Inkomensvoorziening`
- 🔴 Verwijderd: `Client` «heeft» → `Dakloosheid`
- 🔴 Verwijderd: `Client` «heeft» → `Profiel`
- 🔴 Verwijderd: `Client` «heeft» → `Score`
- 🔴 Verwijderd: `Client` «heeft» → `SociaalTeamDossier`
- 🔴 Verwijderd: `Client` «is partner van» → `Inkomensvoorziening`
- 🔴 Verwijderd: `Client` «maakt onderdeel uit van» → `Huishouden`
- 🔴 Verwijderd: `Client` «neemt dienst af» → `Dienst`
- 🔴 Verwijderd: `Client` «valt binnen» → `Doelgroep`
- 🔴 Verwijderd: `Client` «veroorzaakt» → `Normafwijking`
- 🔴 Verwijderd: `Client` «Voorziening Bijstandspartij» → `Inkomensvoorziening`
- 🔴 Verwijderd: `Clientbegeleider` «geeft af» → `Beschikking`
- 🔴 Verwijderd: `Clientbegeleider` «heeft» → `SociaalTeamDossier`
- 🔴 Verwijderd: `Clientbegeleider` «maakt onderdeel uit van» → `Team`
- 🔴 Verwijderd: `Clientbegeleider` «ondersteunt client» → `Client`
- 🔴 Verwijderd: `Clientbegeleider` → `Inkomensvoorziening`
- 🔴 Verwijderd: `Gerechtelijke uitspraak` «basis van» → `Gezagsverhouding`
- 🔴 Verwijderd: `Gezagsverhouding` «betreft» → `IngeschrevenPersoon`
- 🔴 Verwijderd: `Huishouden` «heeft als adres» → `Nummeraanduiding`
- 🔴 Verwijderd: `Huishouden` «heeft als adres» → `Nummeraanduiding`
- 🔴 Verwijderd: `Incident` «informering» → `Informering`
- 🔴 Verwijderd: `Leverancier` «heeft» → `Contract`
- 🔴 Verwijderd: `Leverancier` «leverde prestatie» → `Levering`
- 🔴 Verwijderd: `Profiel` «bevat» → `Inkomstenverhouding`
- 🔴 Verwijderd: `Profiel` «bevat» → `Reden aanvraag`
- 🔴 Verwijderd: `Profiel` «bevat» → `Vermogenscomponent`
- 🔴 Verwijderd: `Relatie` «is soort» → `Relatiesoort`
- 🔴 Verwijderd: `Relatie` «maakt onderdeel van» → `Huishouden`
- 🔴 Verwijderd: `Sociale Relatie` «heeft» → `NatuurlijkPersoon`

#### Generalisaties

- 🔴 Verwijderd: `Client` ⟶ `IngeschrevenPersoon`
- 🔴 Verwijderd: `Clientbegeleider` ⟶ `Medewerker`
- 🔴 Verwijderd: `Leverancier` ⟶ `Rechtspersoon`
- 🔴 Verwijderd: `Relatie` ⟶ `NatuurlijkPersoon`

<a id="structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiekmodel-sociaal-domein-generiekinkomstendatatypes"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Inkomsten/Datatypes

#### Enumeraties

##### `BrutoNettoInkomsten` — 🔴 Verwijderd

##### `CdSrtInkomstenverhouding` — 🔴 Verwijderd

##### `CdSzWet` — 🔴 Verwijderd

##### `CdUitkeringsperiode` — 🔴 Verwijderd

##### `CodeSoortVrijlating` — 🔴 Verwijderd

##### `Inkomstencomponenttype` — 🔴 Verwijderd

##### `InkomstensoortAlimentatie` — 🔴 Verwijderd

##### `InkomstensoortBetaaldWerk` — 🔴 Verwijderd

##### `InkomstensoortPensioen` — 🔴 Verwijderd

##### `InkomstensoortStudiefinanciering` — 🔴 Verwijderd

##### `JsonRuledGroupType` — 🔴 Verwijderd

##### `Onderhoudsplichttype` — 🔴 Verwijderd

##### `SoortContract` — 🔴 Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiekmodel-sociaal-domein-generiekinkomstenmodel-inkomsten"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Inkomsten/Model Inkomsten

#### Classes

##### `Alimentatie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Bedrag aan andere rekeningen` — Verwijderd
- 🔴 `Bedrag in convenant` — Verwijderd
- 🔴 `BijdrageExPartnerAndereRekeningen` — Verwijderd
- 🔴 `Inkomstensoort alimentatie` — Verwijderd
- 🔴 `Juiste bedrag betaald door ex partner` — Verwijderd
- 🔴 `LBIO ingeschakeld` — Verwijderd

##### `Ander inkomen` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Beschrijving ander inkomen` — Verwijderd
- 🔴 `Categorie` — Verwijderd

##### `Beslag op inkomen` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Soort` — Verwijderd

##### `Betaald werk` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Arbeidscontract` — Verwijderd
- 🔴 `Begindatum contract` — Verwijderd
- 🔴 `Einddatum contract` — Verwijderd
- 🔴 `Inkomsten uit IKB-regeling` — Verwijderd
- 🔴 `Inkomstensoort betaald werk` — Verwijderd
- 🔴 `Loondienst` — Verwijderd
- 🔴 `Loonheffingsnummer` — Verwijderd
- 🔴 `Periodiciteit uitbetaling loon` — Verwijderd
- 🔴 `Soort contract` — Verwijderd
- 🔴 `Urenvermindering` — Verwijderd

##### `Dertiende maand - eindejaarsuitkering` — 🔴 Verwijderd

##### `Draagkracht` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Einddatum` — Verwijderd
- 🔴 `Startdatum` — Verwijderd

##### `Draagkrachtregime` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Initiele draagkracht` — Verwijderd
- 🔴 `Naam` — Verwijderd
- 🔴 `Peildatum` — Verwijderd
- 🔴 `Resterende draagkracht` — Verwijderd

##### `Eigen bedrijf` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Aantal uren per week besteed aan werk` — Verwijderd
- 🔴 `Ingeschreven bij KvK` — Verwijderd
- 🔴 `Recht op zelfstandigenaftrek` — Verwijderd
- 🔴 `Soort bedrijf` — Verwijderd
- 🔴 `Toestemming gemeente parttime ondernemen` — Verwijderd

##### `Eigen bijdrage` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Soort` — Verwijderd

##### `Heffingskorting` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Algemene heffingskorting` — Verwijderd
- 🔴 `Inkomensafhankelijke combinatiekorting` — Verwijderd

##### `Hobby` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Aantal uren per week besteed aan hobby` — Verwijderd
- 🔴 `Beschrijving hobby` — Verwijderd

##### `Inkomstencomponent` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Bijgevoegd bewijs` — Verwijderd
- 🔴 `Boekingsdatum` — Verwijderd
- 🔴 `Bruto-Netto` — Verwijderd
- 🔴 `Inkomsten` — Verwijderd
- 🔴 `Inkomstencomponenttype` — Verwijderd
- 🔴 `Link naar bewijs` — Verwijderd
- 🔴 `Peilmoment` — Verwijderd
- 🔴 `Periode einddatum` — Verwijderd
- 🔴 `Periode startdatum` — Verwijderd

##### `Inkomstenverhouding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Categorie Inkomsten` — Verwijderd
- 🔴 `Periode einddatum` — Verwijderd
- 🔴 `Periode startdatum` — Verwijderd

##### `Inkomstenvermindering` — 🔴 Verwijderd

##### `Kostencomponent` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Bedrag` — Verwijderd

##### `Loonbeslag` — 🔴 Verwijderd

##### `Maaltijdvergoeding` — 🔴 Verwijderd

##### `Onderhoudsplicht` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Bijdrage` — Verwijderd
- 🔴 `Boekingsdatum` — Verwijderd
- 🔴 `Onderhoudsplichttype` — Verwijderd
- 🔴 `Peilmoment` — Verwijderd
- 🔴 `Periode einddatum` — Verwijderd
- 🔴 `Periode startdatum` — Verwijderd

##### `Onderhoudsverhouding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Onderhoudsverhoudingtype` — Verwijderd
- 🔴 `Periode einddatum` — Verwijderd
- 🔴 `Periode startdatum` — Verwijderd

##### `Onkostenvergoeding` — 🔴 Verwijderd

##### `Pensioen` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Beslag op pensioen` — Verwijderd
- 🔴 `Inkomstensoort pensioen` — Verwijderd
- 🔴 `Loonheffingskorting` — Verwijderd
- 🔴 `Periodiciteit uitbetaling pensioen` — Verwijderd
- 🔴 `Uitbetaling vakantiegeld pensioen` — Verwijderd

##### `Primair inkomstencomponent` — 🔴 Verwijderd

##### `Reiskosten naar het werk` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Soort` — Verwijderd

##### `Reiskostenvergoeding` — 🔴 Verwijderd

##### `Secundair inkomstencomponent` — 🔴 Verwijderd

##### `Stage` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Maaltijdvergoeding` — Verwijderd
- 🔴 `Onkostenvergoeding` — Verwijderd
- 🔴 `Periodiciteit uitbetaling loon` — Verwijderd
- 🔴 `Reiskostenvergoeding` — Verwijderd
- 🔴 `Vergoeding in natura` — Verwijderd

##### `Studiefinanciering` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Daadwerkelijk Genoten` — Verwijderd
- 🔴 `Inkomstensoort studiefinanciering` — Verwijderd

##### `Te betalen alimentatie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Soort` — Verwijderd

##### `Uitkering` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Beslag op uitkering` — Verwijderd
- 🔴 `Inkomstensoort uitkering` — Verwijderd
- 🔴 `Loonheffingskorting` — Verwijderd
- 🔴 `Periodiciteit uitbetaling uitkering` — Verwijderd
- 🔴 `Toeslag op uitkering` — Verwijderd
- 🔴 `Uitkering verlaagd door boete` — Verwijderd
- 🔴 `Uitkering verlaagd door maatregel` — Verwijderd
- 🔴 `Vakantiegeld jaarlijks ontvangen` — Verwijderd

##### `Vakantiegeld` — 🔴 Verwijderd

##### `Vergoeding` — 🔴 Verwijderd

##### `Vergoeding in natura` — 🔴 Verwijderd

##### `Verlaging door boete` — 🔴 Verwijderd

##### `Verlaging door maatregel` — 🔴 Verwijderd

##### `Vrijlating inkomsten` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Doelgroep` — Verwijderd
- 🔴 `Medisch` — Verwijderd
- 🔴 `Periode einddatum` — Verwijderd
- 🔴 `Periode startdatum` — Verwijderd
- 🔴 `Soort vrijlating` — Verwijderd
- 🔴 `Vrijgelaten bedrag` — Verwijderd

#### Enumeraties

##### `BrutoNettoInkomsten` — 🔴 Verwijderd

##### `CdSrtInkomstenverhouding` — 🔴 Verwijderd

##### `CdSzWet` — 🔴 Verwijderd

##### `CdUitkeringsperiode` — 🔴 Verwijderd

##### `CdUitkeringsperiode` — 🔴 Verwijderd

##### `CdUitkeringsperiode` — 🔴 Verwijderd

##### `CdUitkeringsperiode` — 🔴 Verwijderd

##### `CodeSoortVrijlating` — 🔴 Verwijderd

##### `Inkomstencomponenttype` — 🔴 Verwijderd

##### `InkomstensoortAlimentatie` — 🔴 Verwijderd

##### `InkomstensoortBetaaldWerk` — 🔴 Verwijderd

##### `InkomstensoortPensioen` — 🔴 Verwijderd

##### `InkomstensoortStudiefinanciering` — 🔴 Verwijderd

##### `JsonRuledGroupType` — 🔴 Verwijderd

##### `Onderhoudsplichttype` — 🔴 Verwijderd

##### `SoortContract` — 🔴 Verwijderd

#### Associaties

- 🔴 Verwijderd: `Betaald werk` «Betaald werk heeft Dertiende maand - eindejaarsuitkering» → `Dertiende maand - eindejaarsuitkering`
- 🔴 Verwijderd: `Betaald werk` «Betaald werk heeft Heffingskorting» → `Heffingskorting`
- 🔴 Verwijderd: `Betaald werk` «Betaald werk heeft Loonbeslag» → `Loonbeslag`
- 🔴 Verwijderd: `Betaald werk` «Betaald werk heeft Maaltijdvergoeding» → `Maaltijdvergoeding`
- 🔴 Verwijderd: `Betaald werk` «Betaald werk heeft Onkostenvergoeding» → `Onkostenvergoeding`
- 🔴 Verwijderd: `Betaald werk` «Betaald werk heeft Reiskostenvergoeding» → `Reiskostenvergoeding`
- 🔴 Verwijderd: `Betaald werk` «Betaald werk heeft Vakantiegeld» → `Vakantiegeld`
- 🔴 Verwijderd: `Draagkracht` «Draagkracht heeft Draagkrachtregime» → `Draagkrachtregime`
- 🔴 Verwijderd: `Inkomstenverhouding` «Inkomstenverhouding bevat Primair inkomstencomponent» → `Primair inkomstencomponent`
- 🔴 Verwijderd: `Onderhoudsverhouding` «Onderhoudsverhouding bevat Onderhoudsplicht» → `Onderhoudsplicht`
- 🔴 Verwijderd: `Pensioen` «Pensioen heeft Loonbeslag» → `Loonbeslag`
- 🔴 Verwijderd: `Pensioen` «Pensioen heeft Vakantiegeld» → `Vakantiegeld`
- 🔴 Verwijderd: `Stage` «Stage heeft Maaltijdvergoeding» → `Maaltijdvergoeding`
- 🔴 Verwijderd: `Stage` «Stage heeft Onkostenvergoeding» → `Onkostenvergoeding`
- 🔴 Verwijderd: `Stage` «Stage heeft Reiskostenvergoeding» → `Reiskostenvergoeding`
- 🔴 Verwijderd: `Stage` «Stage heeft Vergoeding in natura» → `Vergoeding in natura`
- 🔴 Verwijderd: `Uitkering` «Uitkering heeft Loonbeslag» → `Loonbeslag`
- 🔴 Verwijderd: `Uitkering` «Uitkering heeft Vakantiegeld» → `Vakantiegeld`
- 🔴 Verwijderd: `Uitkering` «Uitkering heeft Verlaging door boete» → `Verlaging door boete`
- 🔴 Verwijderd: `Uitkering` «Uitkering heeft Verlaging door maatregel» → `Verlaging door maatregel`

#### Generalisaties

- 🔴 Verwijderd: `Alimentatie` ⟶ `Primair inkomstencomponent`
- 🔴 Verwijderd: `Ander inkomen` ⟶ `Primair inkomstencomponent`
- 🔴 Verwijderd: `Beslag op inkomen` ⟶ `Kostencomponent`
- 🔴 Verwijderd: `Betaald werk` ⟶ `Primair inkomstencomponent`
- 🔴 Verwijderd: `Dertiende maand - eindejaarsuitkering` ⟶ `Secundair inkomstencomponent`
- 🔴 Verwijderd: `Eigen bedrijf` ⟶ `Primair inkomstencomponent`
- 🔴 Verwijderd: `Eigen bijdrage` ⟶ `Kostencomponent`
- 🔴 Verwijderd: `Heffingskorting` ⟶ `Secundair inkomstencomponent`
- 🔴 Verwijderd: `Hobby` ⟶ `Primair inkomstencomponent`
- 🔴 Verwijderd: `Inkomstenvermindering` ⟶ `Secundair inkomstencomponent`
- 🔴 Verwijderd: `Loonbeslag` ⟶ `Inkomstenvermindering`
- 🔴 Verwijderd: `Maaltijdvergoeding` ⟶ `Vergoeding`
- 🔴 Verwijderd: `Onkostenvergoeding` ⟶ `Vergoeding`
- 🔴 Verwijderd: `Pensioen` ⟶ `Primair inkomstencomponent`
- 🔴 Verwijderd: `Primair inkomstencomponent` ⟶ `Inkomstencomponent`
- 🔴 Verwijderd: `Reiskosten naar het werk ` ⟶ `Kostencomponent`
- 🔴 Verwijderd: `Reiskostenvergoeding` ⟶ `Vergoeding`
- 🔴 Verwijderd: `Secundair inkomstencomponent` ⟶ `Inkomstencomponent`
- 🔴 Verwijderd: `Stage` ⟶ `Primair inkomstencomponent`
- 🔴 Verwijderd: `Studiefinanciering` ⟶ `Primair inkomstencomponent`
- 🔴 Verwijderd: `Te betalen alimentatie` ⟶ `Kostencomponent`
- 🔴 Verwijderd: `Uitkering` ⟶ `Primair inkomstencomponent`
- 🔴 Verwijderd: `Vakantiegeld` ⟶ `Secundair inkomstencomponent`
- 🔴 Verwijderd: `Vergoeding in natura` ⟶ `Vergoeding`
- 🔴 Verwijderd: `Vergoeding` ⟶ `Secundair inkomstencomponent`
- 🔴 Verwijderd: `Verlaging door boete` ⟶ `Inkomstenvermindering`
- 🔴 Verwijderd: `Verlaging door maatregel` ⟶ `Inkomstenvermindering`

<a id="structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiekmodel-sociaal-domein-generiekvermogendatatypes"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Vermogen/Datatypes

#### Enumeraties

##### `AdresType` — 🔴 Verwijderd

##### `CdSrtVermogenscomponent` — 🔴 Verwijderd

##### `CdSrtVoertuig` — 🔴 Verwijderd

##### `CdSrtWaardeVermogenscomponent` — 🔴 Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiekmodel-sociaal-domein-generiekvermogenmodel-vermogen"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Vermogen/Model Vermogen

#### Classes

##### `Bankrekening` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Bankrekeningnummer` — Verwijderd
- 🔴 `Brontype` — Verwijderd
- 🔴 `Datum aanvang bankrekening` — Verwijderd
- 🔴 `Datum einde bankrekening` — Verwijderd
- 🔴 `IBAN` — Verwijderd
- 🔴 `Rekeningtype` — Verwijderd
- 🔴 `Tenaamstelling` — Verwijderd
- 🔴 `Voorkeur bankrekening` — Verwijderd

##### `Hypotheek` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Overwaarde` — Verwijderd

##### `Motorvoertuig` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Kenteken` — Verwijderd
- 🔴 `Soort motorvoertuig` — Verwijderd

##### `Onroerend goed` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Overwaarde` — Verwijderd

##### `Vermogenscomponent` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Code soort vermogenscomponent` — Verwijderd
- 🔴 `Datum vaststelling vermogencomponent` — Verwijderd
- 🔴 `identificatie` — Verwijderd
- 🔴 `Nog aan te spreken vermogen` — Verwijderd
- 🔴 `Vrij te laten vermogen` — Verwijderd

##### `Waardepeiling` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Bijgevoegd bewijs` — Verwijderd
- 🔴 `Brontype` — Verwijderd
- 🔴 `Datum aanspraak vermogenscomponent` — Verwijderd
- 🔴 `Link naar bewijs` — Verwijderd
- 🔴 `Peilmoment` — Verwijderd
- 🔴 `Waarde vermogenscomponent` — Verwijderd
- 🔴 `WaardepeilingId` — Verwijderd
- 🔴 `WaardeSoort vermogenscomponent` — Verwijderd

#### Enumeraties

##### `CdSrtVermogenscomponent` — 🔴 Verwijderd

##### `CdSrtVoertuig` — 🔴 Verwijderd

##### `CdSrtWaardeVermogenscomponent` — 🔴 Verwijderd

#### Associaties

- 🔴 Verwijderd: `Hypotheek` «Hypotheek rust op Onroerend goed» → `Onroerend goed`
- 🔴 Verwijderd: `Vermogenscomponent` «Vermogenscomponent is gewaardeerd met Waardepeiling» → `Waardepeiling`

#### Generalisaties

- 🔴 Verwijderd: `Bankrekening` ⟶ `Vermogenscomponent`
- 🔴 Verwijderd: `Hypotheek` ⟶ `Vermogenscomponent`
- 🔴 Verwijderd: `Motorvoertuig` ⟶ `Vermogenscomponent`
- 🔴 Verwijderd: `Onroerend goed` ⟶ `Vermogenscomponent`

<a id="structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociale-teamsmodel-sociale-teams"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociale Teams/Model Sociale Teams

#### Classes

##### `Behandeling` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `toelichting` — Verwijderd

##### `Behandelsoort` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Bijzonderheid` — 🔴 Verwijderd

**Attributen:**

- 🔴 `omschrijving` — Verwijderd

##### `Bijzonderheidsoort` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Caseaanmelding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datum` — Verwijderd

##### `Doelstelling` — 🔴 Verwijderd

**Attributen:**

- 🔴 `omschrijving` — Verwijderd

##### `Doelstellingsoort` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `SociaalTeamDossier` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `datumVaststelling` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `status` — Verwijderd

##### `SociaalteamDossiersoort` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `Behandeling` «is van soort» → `Behandelsoort`
- 🔴 Verwijderd: `Bijzonderheid` «is van soort» → `Bijzonderheidsoort`
- 🔴 Verwijderd: `Doelstelling` «is van soort» → `Doelstellingsoort`
- 🔴 Verwijderd: `SociaalTeamDossier` «heeft aanmelding» → `Caseaanmelding`
- 🔴 Verwijderd: `SociaalTeamDossier` «heeft behandeling» → `Behandeling`
- 🔴 Verwijderd: `SociaalTeamDossier` «heeft betrokkenen» → `Relatie`
- 🔴 Verwijderd: `SociaalTeamDossier` «heeft bijzonderheid» → `Bijzonderheid`
- 🔴 Verwijderd: `SociaalTeamDossier` «heeft doelstelling» → `Doelstelling`
- 🔴 Verwijderd: `SociaalTeamDossier` «heeft soort» → `SociaalteamDossiersoort`

<a id="structureel-delfts-gemeentelijk-gegevensmodel6-sociaal-domeinwerkmodel-werk"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Werk/Model Werk

#### Classes

##### `Arbeidsmarktkwalificaties` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Code taalbeheersing mondeling` — Verwijderd
- 🔴 `Code taalbeheersing schriftelijk` — Verwijderd
- 🔴 `Code werk en denkniveau` — Verwijderd
- 🔴 `KlantTypering` — Verwijderd
- 🔴 `ToelichtingArbeidsmarktKwalificaties` — Verwijderd

##### `Arbeidsperiode` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Contact email` — Verwijderd
- 🔴 `Contact persoon` — Verwijderd
- 🔴 `Contact telefoon` — Verwijderd
- 🔴 `Datum aanvang arbeidsperiode` — Verwijderd
- 🔴 `Datum einde arbeidsperiode` — Verwijderd
- 🔴 `Functienaam` — Verwijderd
- 🔴 `Functieomschrijving` — Verwijderd
- 🔴 `Gemiddeld aantal uur per week` — Verwijderd

##### `Arbeidsverhouding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Datum aanvraag arbeidsverhouding` — Verwijderd
- 🔴 `Datum einde arbeidsverhouding` — Verwijderd

##### `Arbeidsvermogen` — 🔴 Verwijderd

**Attributen:**

- 🔴 `CodeArbeidsvermogen` — Verwijderd

##### `Bemiddelingsactiviteit` — 🔴 Verwijderd

**Attributen:**

- 🔴 `DatumBemiddeling` — Verwijderd
- 🔴 `DatumVerwijzingVacature` — Verwijderd
- 🔴 `IndicatiePlaatsing` — Verwijderd
- 🔴 `OmschrijvingResultaatBemiddeling` — Verwijderd
- 🔴 `OmschrijvingSatutsBemiddeling` — Verwijderd
- 🔴 `OmschrijvingSoortContactbemiddeling` — Verwijderd

##### `Bemiddelingsberoep` — 🔴 Verwijderd

**Attributen:**

- 🔴 `ToelichtingBeroep` — Verwijderd

##### `Bemiddelingstraject` — 🔴 Verwijderd

**Attributen:**

- 🔴 `DatumBemiddeling` — Verwijderd
- 🔴 `DatumVacature` — Verwijderd
- 🔴 `IndicatiePlaatsing` — Verwijderd
- 🔴 `OmschrijvingContactbemiddeling` — Verwijderd
- 🔴 `OmschrijvingResultaatbemiddeling` — Verwijderd
- 🔴 `OmschrijvingStatusbemiddeling` — Verwijderd

##### `BeschikbaarVoorArbeid` — 🔴 Verwijderd

**Attributen:**

- 🔴 `AantalUrenpwBeschikbaar` — Verwijderd
- 🔴 `DagBeschikbaarheid` — Verwijderd
- 🔴 `EinddatumBeschikbaarheid` — Verwijderd
- 🔴 `EindtijdDagBeschikbaarheid` — Verwijderd
- 🔴 `Indicatie nog werkzaam` — Verwijderd
- 🔴 `Interval opzegtermijn` — Verwijderd
- 🔴 `StartdagBeschikbaarheid` — Verwijderd
- 🔴 `StartdatumBeschikbaarheid` — Verwijderd
- 🔴 `ToelichtingBeschikbaarheid` — Verwijderd
- 🔴 `WaardeOpzegtermijn` — Verwijderd

##### `BeschikbaarVoorBemiddeling` — 🔴 Verwijderd

**Attributen:**

- 🔴 `DatumEinde` — Verwijderd
- 🔴 `IndicatieDirectBemiddelbaar` — Verwijderd

##### `Doelgroep` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Doelgroepenregister` — 🔴 Verwijderd

**Attributen:**

- 🔴 `AdviesUWV` — Verwijderd
- 🔴 `Baanafspraak` — Verwijderd
- 🔴 `IndicatieDoelgroepenRegister` — Verwijderd

##### `DoelReintegratievoorziening` — 🔴 Verwijderd

**Attributen:**

- 🔴 `CodeDoelReintegratievoorziening` — Verwijderd

##### `Flexibliteit` — 🔴 Verwijderd

**Attributen:**

- 🔴 `IndicatieBereidBuitenBeroepswens` — Verwijderd
- 🔴 `IndicatieBereidheidOnregelmatigWerk` — Verwijderd
- 🔴 `IndicatieBereidheidZoekenOnderNiveau` — Verwijderd
- 🔴 `IndicatieBereidheidZwaarWerk` — Verwijderd
- 🔴 `IngeschrevenbijUitzendbureau` — Verwijderd

##### `Loonkostensubsidie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `PercentageLoonwaardeWML` — Verwijderd

##### `Mobiliteit` — 🔴 Verwijderd

**Attributen:**

- 🔴 `CodeVervoermiddel` — Verwijderd
- 🔴 `IndicatieBereidheidVerhuizen` — Verwijderd
- 🔴 `MaximaleReistijd` — Verwijderd
- 🔴 `ToelichtingMaximaleReistijd` — Verwijderd
- 🔴 `ToelichtingVervoermiddel` — Verwijderd

##### `Ontheffing` — 🔴 Verwijderd

**Attributen:**

- 🔴 `AanvraagdatumOntheffing` — Verwijderd
- 🔴 `BijlagenBijAanvraag` — Verwijderd
- 🔴 `BijlagenBijHerzieningsbesluit` — Verwijderd
- 🔴 `BijlagenBijOntheffingsbesluit` — Verwijderd
- 🔴 `EinddatumOntheffing` — Verwijderd
- 🔴 `HerzieningsdatumOntheffing` — Verwijderd
- 🔴 `IngangsdatumOntheffing` — Verwijderd
- 🔴 `MotivatieHerzieningsbesluit` — Verwijderd
- 🔴 `MotivatieOntheffingsbesluit` — Verwijderd
- 🔴 `OntheffenVerplichtingen` — Verwijderd
- 🔴 `Ontheffingsbesluit` — Verwijderd
- 🔴 `RedenAanvraag` — Verwijderd
- 🔴 `ResultaatInstrumentbeoordeling` — Verwijderd
- 🔴 `SoortOntheffing` — Verwijderd
- 🔴 `VersieNummerAanvraag` — Verwijderd

##### `Opleiding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `AantalJarenOpleiding` — Verwijderd
- 🔴 `CodeLeerwegMBO` — Verwijderd
- 🔴 `CodeNiveauOpleiding` — Verwijderd
- 🔴 `CodeStatusOpleiding` — Verwijderd
- 🔴 `CodeTijdsBeslagOpleiding` — Verwijderd
- 🔴 `DatumAanvang` — Verwijderd
- 🔴 `DatumDiploma` — Verwijderd
- 🔴 `DatumEinde` — Verwijderd
- 🔴 `Indicatiebuitenlandseopleiding` — Verwijderd
- 🔴 `IndicatieDeeltijdopleiding` — Verwijderd
- 🔴 `IndicatieDiploma` — Verwijderd
- 🔴 `Instituutnaam` — Verwijderd
- 🔴 `Opleidingsrichting` — Verwijderd
- 🔴 `Opleidingstype` — Verwijderd
- 🔴 `ToelichtingBeeindigenOpleiding` — Verwijderd
- 🔴 `ToelichtingOpleiding` — Verwijderd

##### `Opleidingsnaam` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naamOpleiding` — Verwijderd

##### `OpleidingsnaamGecodeerd` — 🔴 Verwijderd

**Attributen:**

- 🔴 `CodeOpleidingsnaam` — Verwijderd
- 🔴 `CodeSoortOpleidingsnaam` — Verwijderd
- 🔴 `IndicatieOpleidingsnaamActief` — Verwijderd
- 🔴 `OmschrijvingOpleidingsnaam` — Verwijderd

##### `OpleidingsnaamOngecodeerd` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naamOpleidingOngecodeerd` — Verwijderd

##### `Opleidingsniveau` — 🔴 Verwijderd

**Attributen:**

- 🔴 `CodeOpleidingsniveauClient` — Verwijderd

##### `Reintegratievoorziening` — 🔴 Verwijderd

**Attributen:**

- 🔴 `CodeType` — Verwijderd
- 🔴 `DatumEinde` — Verwijderd
- 🔴 `DatumEindeVerlengdeBeslistermijn` — Verwijderd
- 🔴 `DatumIngebruikname` — Verwijderd
- 🔴 `DatumInname` — Verwijderd
- 🔴 `DatumStart` — Verwijderd
- 🔴 `DatumStartVoorlopigeToekenning` — Verwijderd
- 🔴 `DatumVerwachtEinde` — Verwijderd
- 🔴 `Omschrijving` — Verwijderd
- 🔴 `OmschrijvingType` — Verwijderd
- 🔴 `RegistratienummerReintegratievoorziening` — Verwijderd
- 🔴 `ToelichtingOmschrijving` — Verwijderd

##### `Rijbewijs /Certificaat` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Beschrijving` — Verwijderd
- 🔴 `CodeSoortRijbewijs` — Verwijderd
- 🔴 `GeldigTot` — Verwijderd
- 🔴 `GeldigVanaf` — Verwijderd
- 🔴 `IndicatieGeldigheidRijbewijs` — Verwijderd
- 🔴 `NaamCertificaat` — Verwijderd
- 🔴 `NummerCertificaat` — Verwijderd
- 🔴 `VerstrekkendePartij` — Verwijderd

##### `Taalbeheersing` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Leesvaardigheid` — Verwijderd
- 🔴 `Moedertaal` — Verwijderd
- 🔴 `Schrijfvaardigheid` — Verwijderd
- 🔴 `Spreekvaardigheid` — Verwijderd
- 🔴 `Taalcode` — Verwijderd
- 🔴 `Taalnaam` — Verwijderd

##### `TaalbeheersingNederlands` — 🔴 Verwijderd

**Attributen:**

- 🔴 `GespreksvaardigheidNederlands` — Verwijderd
- 🔴 `LeesvaardigheidNederlands` — Verwijderd
- 🔴 `LuistervaardigheidNederlands` — Verwijderd
- 🔴 `OntheffingTaaleis` — Verwijderd
- 🔴 `SchrijfvaardigheidNederlands` — Verwijderd
- 🔴 `SpreeksvaardigheidNederlands` — Verwijderd

##### `Vaardigheidsvaststelling` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumLaatsteVaststelling` — Verwijderd
- 🔴 `Indicatie mate van vaardigheid` — Verwijderd

##### `Voorkeur` — 🔴 Verwijderd

**Attributen:**

- 🔴 `BezitPersoonlijkeOVkaart` — Verwijderd
- 🔴 `BrancheCode` — Verwijderd
- 🔴 `BrancheNaam` — Verwijderd
- 🔴 `GegevensWerklocatie` — Verwijderd
- 🔴 `NummerOVK` — Verwijderd
- 🔴 `SoortBaan` — Verwijderd
- 🔴 `SoortWerk` — Verwijderd
- 🔴 `ToelichtingVervoersmiddel` — Verwijderd
- 🔴 `VerloopdatumOVK` — Verwijderd
- 🔴 `Vervoermiddel` — Verwijderd

##### `VrijstellingArbeidsplicht` — 🔴 Verwijderd

**Attributen:**

- 🔴 `CodeRedenVrijheidstelling` — Verwijderd
- 🔴 `CodeVrijstelling` — Verwijderd
- 🔴 `DatumEinde` — Verwijderd
- 🔴 `DatumStart` — Verwijderd
- 🔴 `IndicatieVrijstelling` — Verwijderd

##### `Werkervaring` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Aantal jaren werkzaam in beroep` — Verwijderd
- 🔴 `Toelichting beroep` — Verwijderd

##### `Werkzaamheden als mantelzorger` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Andere mantelzorgtaken` — Verwijderd
- 🔴 `Hulp bij medicatie` — Verwijderd
- 🔴 `Mantelzorgovereenkomst afgesloten` — Verwijderd
- 🔴 `Mantelzorgverkalring verstrekt` — Verwijderd
- 🔴 `Omschrijving andere mantelzorgtaken` — Verwijderd
- 🔴 `Te bespreken mantelzorgtaken` — Verwijderd
- 🔴 `Toezicht houden` — Verwijderd
- 🔴 `Vervoer en begeleiding` — Verwijderd
- 🔴 `Verzorgde actviteiten` — Verwijderd

##### `Werkzaamheden anders dan in arbeidsverhouding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aantalUrenGemiddeldWeek` — Verwijderd
- 🔴 `Bedrag netto inkomsten uit Wadia` — Verwijderd
- 🔴 `Code maatschappelijke context` — Verwijderd
- 🔴 `Datum aanvang werkzaamheden` — Verwijderd
- 🔴 `Datum einde werkzaamheden` — Verwijderd
- 🔴 `Functienaam` — Verwijderd
- 🔴 `Omschrijving reden einde werkzaamheden` — Verwijderd
- 🔴 `Omschrijving werkzaamheden` — Verwijderd
- 🔴 `PersoonOrganisatieWaarbij` — Verwijderd

##### `Werkzoekende` — 🔴 Verwijderd

**Attributen:**

- 🔴 `DatumAanvangWerkzoekende` — Verwijderd
- 🔴 `DatumEindeWerkzoekende` — Verwijderd

##### `ZelfredzaamheidScore` — 🔴 Verwijderd

**Attributen:**

- 🔴 `DatumBeoordeling` — Verwijderd
- 🔴 `Domein van Zelfredzaamheid` — Verwijderd
- 🔴 `IndicatieHulpAanwezig` — Verwijderd
- 🔴 `KenmerkBeoordelaar` — Verwijderd
- 🔴 `Woongemeente` — Verwijderd
- 🔴 `ZRM score` — Verwijderd

#### Enumeraties

##### `Code arbeidsvermogen` — 🔴 Verwijderd

**Literals:**

- 🔴 `met hulp WML of hoger` — Verwijderd
- 🔴 `nog niet bekend` — Verwijderd
- 🔴 `onder WML` — Verwijderd
- 🔴 `tijdelijk geen arbeidsvermogen` — Verwijderd
- 🔴 `zelfstandig WML of hoger` — Verwijderd

##### `Code maatschappelijke context werkzaamheden anders dan in arbeidsverhouding` — 🔴 Verwijderd

**Literals:**

- 🔴 `Werkzaamheden als freelancer` — Verwijderd
- 🔴 `Werkzaamheden als mantelzorger` — Verwijderd
- 🔴 `Werkzaamheden als vrijwilliger` — Verwijderd
- 🔴 `Werkzaamheden als zelfstandige` — Verwijderd
- 🔴 `Werkzaamheden in een niet nader gespecificeerde context, niet zijnde een arbeidsverhouding` — Verwijderd
- 🔴 `Werkzaamheden in een politieke functie` — Verwijderd

##### `Code opleidingsniveau cliënt` — 🔴 Verwijderd

**Literals:**

- 🔴 `(Nog) niet bekend` — Verwijderd
- 🔴 `Basisniveau` — Verwijderd
- 🔴 `Geen basisopleiding` — Verwijderd
- 🔴 `Hbo-niveau` — Verwijderd
- 🔴 `Lbo/mavo-niveau` — Verwijderd
- 🔴 `Mbo/havo/vwo-niveau` — Verwijderd
- 🔴 `Niet van toepassing` — Verwijderd
- 🔴 `Wetenschappelijk onderwijs` — Verwijderd

##### `Code tijdsbeslag opleiding` — 🔴 Verwijderd

**Literals:**

- 🔴 `Anders` — Verwijderd
- 🔴 `Avondopleiding` — Verwijderd
- 🔴 `Dag- + avondopleiding` — Verwijderd
- 🔴 `Dagopleiding` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Schriftelijk` — Verwijderd

##### `CodeLeerwegMBO` — 🔴 Verwijderd

**Literals:**

- 🔴 `BBL  Beroepsbegeleidende leerweg` — Verwijderd
- 🔴 `BOL  Beroepsopleidende leerweg` — Verwijderd
- 🔴 `CBL  Combinatie beroepsbegeleidende leerweg` — Verwijderd
- 🔴 `COL  Combinatie beroepsopleidende leerweg` — Verwijderd
- 🔴 `OVO  Overig onderwijs (niet bekostigd)` — Verwijderd

##### `CodeNiveauOpleiding` — 🔴 Verwijderd

**Literals:**

- 🔴 `Basisonderwijs` — Verwijderd
- 🔴 `HAVO / VWO` — Verwijderd
- 🔴 `HBO / Bachelor` — Verwijderd
- 🔴 `MBO` — Verwijderd
- 🔴 `VMBO / MBO-1` — Verwijderd
- 🔴 `WO / Master` — Verwijderd

##### `CodeOpleidingsnaam` — 🔴 Verwijderd

**Literals:**

- 🔴 `Referentieopleiding` — Verwijderd
- 🔴 `Synoniem` — Verwijderd

##### `CodeSoortOpleidingsnaam` — 🔴 Verwijderd

##### `CodeStatusOpleiding` — 🔴 Verwijderd

**Literals:**

- 🔴 `Afgebroken` — Verwijderd
- 🔴 `Lopend` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Succesvol afgerond` — Verwijderd

##### `Dag beschikbaarheid` — 🔴 Verwijderd

**Literals:**

- 🔴 `Dinsdag` — Verwijderd
- 🔴 `Donderdag` — Verwijderd
- 🔴 `Maandag` — Verwijderd
- 🔴 `Vrijdag` — Verwijderd
- 🔴 `Woensdag` — Verwijderd
- 🔴 `Zaterdag` — Verwijderd
- 🔴 `Zondag` — Verwijderd

##### `Domein van zelfredzaamheid` — 🔴 Verwijderd

**Literals:**

- 🔴 `Basale ADL (Activiteiten Dagelijks Leven)` — Verwijderd
- 🔴 `Financiën` — Verwijderd
- 🔴 `Geestelijke gezondheid` — Verwijderd
- 🔴 `Huiselijke relaties` — Verwijderd
- 🔴 `Huisvesting` — Verwijderd
- 🔴 `Instrumentele ADL` — Verwijderd
- 🔴 `Justitie` — Verwijderd
- 🔴 `Lichamelijke gezondheid` — Verwijderd
- 🔴 `Maatschappelijke participatie` — Verwijderd
- 🔴 `Middelengebruik` — Verwijderd
- 🔴 `Sociaal netwerk` — Verwijderd
- 🔴 `Tijdsbesteding` — Verwijderd
- 🔴 `Werk & Opleiding` — Verwijderd

##### `Hulp aanwezig` — 🔴 Verwijderd

**Literals:**

- 🔴 `Ja, formeel` — Verwijderd
- 🔴 `Ja, informeel` — Verwijderd
- 🔴 `Nee` — Verwijderd

##### `Indicatie doelgroepenregister` — 🔴 Verwijderd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Vermoedelijk` — Verwijderd

##### `Indicatie mate van vaardigheid` — 🔴 Verwijderd

**Literals:**

- 🔴 `Goed` — Verwijderd
- 🔴 `Niet` — Verwijderd
- 🔴 `Niet van toepassing` — Verwijderd
- 🔴 `Onderzoek noodzakelijk` — Verwijderd
- 🔴 `Onvoldoende` — Verwijderd
- 🔴 `Voldoende` — Verwijderd

##### `Interval opzegtermijn` — 🔴 Verwijderd

**Literals:**

- 🔴 `Dag` — Verwijderd
- 🔴 `Maand` — Verwijderd
- 🔴 `Uur` — Verwijderd
- 🔴 `Week` — Verwijderd

##### `Kanaal contactmoment` — 🔴 Verwijderd

**Literals:**

- 🔴 `Berichten via THOMAS` — Verwijderd
- 🔴 `Fysiek gesprek` — Verwijderd
- 🔴 `Mail` — Verwijderd
- 🔴 `Ontvangen correspondentie` — Verwijderd
- 🔴 `Telefonisch gesprek` — Verwijderd

##### `Ontheffingsverplichting` — 🔴 Verwijderd

**Literals:**

- 🔴 `A,` — Verwijderd
- 🔴 `A,B,C` — Verwijderd
- 🔴 `A,C,` — Verwijderd

##### `Opleidingsrichting` — 🔴 Verwijderd

**Literals:**

- 🔴 `Hoger onderwijs, derde fase` — Verwijderd
- 🔴 `Hoger onderwijs, eerste fase` — Verwijderd
- 🔴 `Hoger onderwijs, tweede fase` — Verwijderd
- 🔴 `Onderwijs aan kleuters` — Verwijderd
- 🔴 `Primair onderwijs` — Verwijderd
- 🔴 `Secundair onderwijs, eerste fase` — Verwijderd
- 🔴 `Secundair onderwijs, tweede fase` — Verwijderd

##### `SETU job category` — 🔴 Verwijderd

**Literals:**

- 🔴 `Administratieve / Secretariat` — Verwijderd
- 🔴 `Agricultural / Cattle breeding / Animal care / Nature conservation` — Verwijderd
- 🔴 `Building industry` — Verwijderd
- 🔴 `Business services / Retail trade` — Verwijderd
- 🔴 `Catering / Tourism` — Verwijderd
- 🔴 `Cleaning / Housekeeing / Clean up` — Verwijderd
- 🔴 `Consulting / Staff / Policy` — Verwijderd
- 🔴 `Culture / Arts / Creative` — Verwijderd
- 🔴 `Customer service / Call centre / Reception` — Verwijderd
- 🔴 `Design / Architecture / Graphical` — Verwijderd
- 🔴 `Editior / Journalism` — Verwijderd
- 🔴 `Education / Training` — Verwijderd
- 🔴 `Financial administratieve / Accounting` — Verwijderd
- 🔴 `Government service / Government` — Verwijderd
- 🔴 `Health care / Medical / Nursing / Paramedical` — Verwijderd
- 🔴 `IT / ICT / Software development/ Internet` — Verwijderd
- 🔴 `Legal` — Verwijderd
- 🔴 `Marketing / Advertisement / Public relations / Communication` — Verwijderd
- 🔴 `Personal health car` — Verwijderd
- 🔴 `Personnel matters / Human resources / Employment-finding` — Verwijderd
- 🔴 `Production / Crafts` — Verwijderd
- 🔴 `Research / Science / Laboratory` — Verwijderd
- 🔴 `Sales / Commercial` — Verwijderd
- 🔴 `Security / Defence / Auxiliary service` — Verwijderd
- 🔴 `Sport / Relaxation` — Verwijderd
- 🔴 `Technology / Engineering` — Verwijderd

##### `Soort ontheffing` — 🔴 Verwijderd

**Literals:**

- 🔴 `Ouder met kind<5` — Verwijderd
- 🔴 `Sociaal/medisch permanent,` — Verwijderd
- 🔴 `Sociaal/medisch tijdelijk,` — Verwijderd

##### `SoortWerk` — 🔴 Verwijderd

**Literals:**

- 🔴 `Aanpakken` — Verwijderd
- 🔴 `Helpen` — Verwijderd
- 🔴 `Maken` — Verwijderd
- 🔴 `Verkopen` — Verwijderd
- 🔴 `Vervoeren` — Verwijderd

##### `Taalvaardigheid` — 🔴 Verwijderd

**Literals:**

- 🔴 `arm` — Verwijderd
- 🔴 `goed` — Verwijderd
- 🔴 `middelmatig` — Verwijderd
- 🔴 `uitstekend` — Verwijderd
- 🔴 `voldoende` — Verwijderd

##### `Vervoermiddel` — 🔴 Verwijderd

**Literals:**

- 🔴 `Anders` — Verwijderd
- 🔴 `Auto` — Verwijderd
- 🔴 `Bromfiets/scooter` — Verwijderd
- 🔴 `Fiets` — Verwijderd
- 🔴 `Geen` — Verwijderd
- 🔴 `Lopen` — Verwijderd
- 🔴 `Motorfiets` — Verwijderd
- 🔴 `Openbaar vervoer` — Verwijderd
- 🔴 `Openbaar vervoer (week-ov)` — Verwijderd
- 🔴 `Openbaar vervoer (weekend-ov)` — Verwijderd

##### `Vervoersmogelijkheden` — 🔴 Verwijderd

**Literals:**

- 🔴 `Anders` — Verwijderd
- 🔴 `Auto` — Verwijderd
- 🔴 `Bromfiets/scooter` — Verwijderd
- 🔴 `Fiets` — Verwijderd
- 🔴 `Geen` — Verwijderd
- 🔴 `Lopen` — Verwijderd
- 🔴 `Motorfiets` — Verwijderd
- 🔴 `Openbaar vervoer` — Verwijderd
- 🔴 `Openbaar vervoer (week-ov)` — Verwijderd
- 🔴 `Openbaar vervoer (weekend-ov)` — Verwijderd

##### `ZRM-score` — 🔴 Verwijderd

**Literals:**

- 🔴 `Acute problematiek` — Verwijderd
- 🔴 `Beperkt zelfredzaam` — Verwijderd
- 🔴 `Niet zelfredzaam` — Verwijderd
- 🔴 `Voldoende zelfredzaam` — Verwijderd
- 🔴 `Volledig zelfredzaam` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `Arbeidsverhouding` → `Arbeidsperiode`
- 🔴 Verwijderd: `Arbeidsverhouding` → `Werkzoekende`
- 🔴 Verwijderd: `Bemiddelingsberoep` → `Werkzoekende`
- 🔴 Verwijderd: `Opleiding` → `Opleidingsnaam`
- 🔴 Verwijderd: `OpleidingsnaamGecodeerd` «heeft synoniem» → `OpleidingsnaamGecodeerd`
- 🔴 Verwijderd: `Opleidingsniveau` → `Opleiding`
- 🔴 Verwijderd: `Reintegratievoorziening` → `Loonkostensubsidie`
- 🔴 Verwijderd: `Werkzoekende` → `Arbeidsmarktkwalificaties`
- 🔴 Verwijderd: `Werkzoekende` → `Arbeidsvermogen`
- 🔴 Verwijderd: `Werkzoekende` → `Bemiddelingstraject`
- 🔴 Verwijderd: `Werkzoekende` → `BeschikbaarVoorArbeid`
- 🔴 Verwijderd: `Werkzoekende` → `BeschikbaarVoorBemiddeling`
- 🔴 Verwijderd: `Werkzoekende` → `Doelgroepenregister`
- 🔴 Verwijderd: `Werkzoekende` → `DoelReintegratievoorziening`
- 🔴 Verwijderd: `Werkzoekende` → `Flexibliteit`
- 🔴 Verwijderd: `Werkzoekende` → `Mobiliteit`
- 🔴 Verwijderd: `Werkzoekende` → `Ontheffing`
- 🔴 Verwijderd: `Werkzoekende` → `Opleidingsniveau`
- 🔴 Verwijderd: `Werkzoekende` → `Reintegratievoorziening`
- 🔴 Verwijderd: `Werkzoekende` → `Rijbewijs /Certificaat`
- 🔴 Verwijderd: `Werkzoekende` → `Taalbeheersing`
- 🔴 Verwijderd: `Werkzoekende` → `TaalbeheersingNederlands`
- 🔴 Verwijderd: `Werkzoekende` → `Voorkeur`
- 🔴 Verwijderd: `Werkzoekende` → `VrijstellingArbeidsplicht`
- 🔴 Verwijderd: `Werkzoekende` → `Werkervaring`
- 🔴 Verwijderd: `Werkzoekende` → `Werkzaamheden anders dan in arbeidsverhouding`
- 🔴 Verwijderd: `Werkzoekende` → `ZelfredzaamheidScore`

#### Generalisaties

- 🔴 Verwijderd: `OpleidingsnaamGecodeerd` ⟶ `Opleidingsnaam`
- 🔴 Verwijderd: `OpleidingsnaamOngecodeerd` ⟶ `Opleidingsnaam`
- 🔴 Verwijderd: `Werkzaamheden als mantelzorger` ⟶ `Werkzaamheden anders dan in arbeidsverhouding`
- 🔴 Verwijderd: `Werkzoekende` ⟶ `Client`

<a id="structureel-delfts-gemeentelijk-gegevensmodel7-volksgezondheid-en-milieuafvalmodel-afval"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval

#### Classes

##### `Categorie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `code` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Container` — 🔴 Verwijderd

**Attributen:**

- 🔴 `containercode` — Verwijderd
- 🔴 `sensorID` — Verwijderd

##### `Containertype` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Fractie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Locatie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `adresaanduiding` — Verwijderd
- 🔴 `locatiecode` — Verwijderd
- 🔴 `locatiePunt` — Verwijderd

##### `Melding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `24uurs` — Verwijderd
- 🔴 `datumtijd` — Verwijderd
- 🔴 `illegaal` — Verwijderd
- 🔴 `meldingnummer` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Milieustraat` — 🔴 Verwijderd

**Attributen:**

- 🔴 `adresaanduiding` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Ophaalmoment` — 🔴 Verwijderd

**Attributen:**

- 🔴 `gewichtstoename` — Verwijderd
- 🔴 `tijdstip` — Verwijderd

##### `Pas` — 🔴 Verwijderd

**Attributen:**

- 🔴 `adresaanduiding` — Verwijderd
- 🔴 `pasnummer` — Verwijderd

##### `Prijsafspraak` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `titel` — Verwijderd

##### `Prijsregel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bedrag` — Verwijderd
- 🔴 `credit` — Verwijderd

##### `Rit` — 🔴 Verwijderd

**Attributen:**

- 🔴 `eindtijd` — Verwijderd
- 🔴 `ritcode` — Verwijderd
- 🔴 `starttijd` — Verwijderd

##### `Route` — 🔴 Verwijderd

**Attributen:**

- 🔴 `geometrie` — Verwijderd
- 🔴 `routecode` — Verwijderd
- 🔴 `routesoort` — Verwijderd

##### `Storting` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumtijd` — Verwijderd
- 🔴 `gewicht` — Verwijderd

##### `Vuilniswagen` — 🔴 Verwijderd

**Attributen:**

- 🔴 `code` — Verwijderd
- 🔴 `kenteken` — Verwijderd
- 🔴 `type` — Verwijderd

##### `Vulgraadmeting` — 🔴 Verwijderd

**Attributen:**

- 🔴 `tijdstip` — Verwijderd
- 🔴 `vulgraad` — Verwijderd
- 🔴 `vullingGewicht` — Verwijderd

#### Enumeraties

##### `Routesoort` — 🔴 Verwijderd

**Literals:**

- 🔴 `grofvuil` — Verwijderd
- 🔴 `hot-spot-locaties` — Verwijderd
- 🔴 `huis-aan-huis` — Verwijderd
- 🔴 `illegale dumping` — Verwijderd
- 🔴 `vangnetregeling` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `Container` «geschikt voor» → `Fractie`
- 🔴 Verwijderd: `Container` «heeft» → `Locatie`
- 🔴 Verwijderd: `Container` «heeft» → `Vulgraadmeting`
- 🔴 Verwijderd: `Container` «soort» → `Containertype`
- 🔴 Verwijderd: `Melding` «betreft» → `Containertype`
- 🔴 Verwijderd: `Melding` «betreft» → `Fractie`
- 🔴 Verwijderd: `Melding` «betreft» → `Locatie`
- 🔴 Verwijderd: `Melding` «hoofdcategorie» → `Categorie`
- 🔴 Verwijderd: `Melding` «subcategorie» → `Categorie`
- 🔴 Verwijderd: `Milieustraat` «inzamelpunt van» → `Fractie`
- 🔴 Verwijderd: `Ophaalmoment` «gelost» → `Container`
- 🔴 Verwijderd: `Ophaalmoment` «gestopt op» → `Locatie`
- 🔴 Verwijderd: `Pas` «geldig voor» → `Milieustraat`
- 🔴 Verwijderd: `Pas` «uitgevoerde storting» → `Storting`
- 🔴 Verwijderd: `Prijsafspraak` «heeft» → `Prijsregel`
- 🔴 Verwijderd: `Prijsregel` «betreft» → `Fractie`
- 🔴 Verwijderd: `Rit` «heeft» → `Ophaalmoment`
- 🔴 Verwijderd: `Rit` «uitgevoerd met» → `Vuilniswagen`
- 🔴 Verwijderd: `Rit` «volgens» → `Route`
- 🔴 Verwijderd: `Route` «gaat langs» → `Locatie`
- 🔴 Verwijderd: `Route` «ophalen» → `Fractie`
- 🔴 Verwijderd: `Storting` «bij» → `Milieustraat`
- 🔴 Verwijderd: `Storting` «fractie» → `Fractie`
- 🔴 Verwijderd: `Vuilniswagen` «geschikt voor» → `Containertype`

#### Generalisaties

- 🔴 Verwijderd: `Melding` ⟶ `AanvraagOfMelding`

<a id="structureel-delfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingbeheer-openbare-ruimtemodel-basis-imborenumeratiesoort"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Beheer Openbare Ruimte/Model Basis IMBOR/Enumeratiesoort

#### Enumeraties

##### `enum_AanOfVrijliggend` — 🔴 Verwijderd

**Literals:**

- 🔴 `Aanliggend` — Verwijderd
- 🔴 `Vrijliggend` — Verwijderd

##### `enum_Afmeting` — 🔴 Verwijderd

**Literals:**

- 🔴 `100x100x8` — Verwijderd
- 🔴 `20x20x7` — Verwijderd
- 🔴 `20x60x5` — Verwijderd
- 🔴 `21x21x8` — Verwijderd
- 🔴 `240x69x80` — Verwijderd
- 🔴 `30x30x10` — Verwijderd
- 🔴 `30x30x4` — Verwijderd
- 🔴 `30x30x5` — Verwijderd
- 🔴 `30x30x6` — Verwijderd
- 🔴 `30x30x8` — Verwijderd
- 🔴 `35x15x8` — Verwijderd
- 🔴 `40x40x7` — Verwijderd
- 🔴 `40x60x7` — Verwijderd
- 🔴 `50x100x5` — Verwijderd
- 🔴 `50x50x7` — Verwijderd
- 🔴 `60x60x7` — Verwijderd

##### `enum_Bedienaar` — 🔴 Verwijderd

**Literals:**

- 🔴 `Organisatiespecifieke domeinwaarden` — Verwijderd

##### `enum_Beheergebied` — 🔴 Verwijderd

**Literals:**

- 🔴 `Organisatiespecifieke domeinwaarden` — Verwijderd

##### `enum_BeheerobjectGebruiksfunctie` — 🔴 Verwijderd

**Literals:**

- 🔴 `Afscherming` — Verwijderd
- 🔴 `Afvoeren hemelwater naar de ondergrondÂ` — Verwijderd
- 🔴 `Anti-parkeer` — Verwijderd
- 🔴 `Anti-verblinding` — Verwijderd
- 🔴 `Bebakeningsstrook` — Verwijderd
- 🔴 `Begrazingsgebied` — Verwijderd
- 🔴 `Beluchten of ventileren` — Verwijderd
- 🔴 `Berm` — Verwijderd
- 🔴 `Bezinken stoffen` — Verwijderd
- 🔴 `Boezemkering` — Verwijderd
- 🔴 `Buitenberm` — Verwijderd
- 🔴 `Calamiteitendoorsteek` — Verwijderd
- 🔴 `Cultuurlijk groen` — Verwijderd
- 🔴 `Dierenweide` — Verwijderd
- 🔴 `Dijklichaam` — Verwijderd
- 🔴 `Doorsteek` — Verwijderd
- 🔴 `Doorsteek op rotonde` — Verwijderd
- 🔴 `Educatie` — Verwijderd
- 🔴 `Erf` — Verwijderd
- 🔴 `Erosiebeperking` — Verwijderd
- 🔴 `Evenemententerrein` — Verwijderd
- 🔴 `Fauna weren` — Verwijderd
- 🔴 `Faunageleiding` — Verwijderd
- 🔴 `Gebied met aanlijnplicht honden` — Verwijderd
- 🔴 `Geluidswal` — Verwijderd
- 🔴 `Helofytenfilter` — Verwijderd
- 🔴 `Hondenlosloopgebied` — Verwijderd
- 🔴 `Hondenuitlaatplaats` — Verwijderd
- 🔴 `Hoogwaterbemaling` — Verwijderd
- 🔴 `Hoogwaterkering` — Verwijderd
- 🔴 `Infiltratieveld` — Verwijderd
- 🔴 `Inlaatplaats veegboot` — Verwijderd
- 🔴 `Inloopkom` — Verwijderd
- 🔴 `Inzameling van grondwater` — Verwijderd
- 🔴 `Keermogelijkheid` — Verwijderd
- 🔴 `Kinderboerderij` — Verwijderd
- 🔴 `Klimboom` — Verwijderd
- 🔴 `Kunstuiting aangebracht op object` — Verwijderd
- 🔴 `Leidingen aansluiten` — Verwijderd
- 🔴 `Middenberm` — Verwijderd
- 🔴 `Middeneiland` — Verwijderd
- 🔴 `Middengeleider` — Verwijderd
- 🔴 `Natuurlijk speelgroen` — Verwijderd
- 🔴 `Natuurvriendelijke oever` — Verwijderd
- 🔴 `Niet bereden dek` — Verwijderd
- 🔴 `Obstakelbeveiliging (aanrijbescherming)` — Verwijderd
- 🔴 `Oever` — Verwijderd
- 🔴 `Onbegroeid terreindeel` — Verwijderd
- 🔴 `Onderdeel ecologische structuur` — Verwijderd
- 🔴 `Onderdeel landschappelijke groenstructuur` — Verwijderd
- 🔴 `Onderdeel stedelijke groenstructuur` — Verwijderd
- 🔴 `Open berging` — Verwijderd
- 🔴 `Opslag` — Verwijderd
- 🔴 `Opvang van afstromend hemelwater` — Verwijderd
- 🔴 `Overbruggen groot niveauverschilÂ` — Verwijderd
- 🔴 `Perceelscheiding` — Verwijderd
- 🔴 `Plasdras` — Verwijderd
- 🔴 `Recreatie` — Verwijderd
- 🔴 `Rijstrookscheiding` — Verwijderd
- 🔴 `Speelaanleiding` — Verwijderd
- 🔴 `Speelondergrond` — Verwijderd
- 🔴 `Sportondergrond` — Verwijderd
- 🔴 `Terreinafscheiding` — Verwijderd
- 🔴 `Tijdelijke opslag afvalwaterÂ Â` — Verwijderd
- 🔴 `Toegang verschaffen` — Verwijderd
- 🔴 `Transport van oppervlaktewater` — Verwijderd
- 🔴 `Trapveld` — Verwijderd
- 🔴 `Tussenberm` — Verwijderd
- 🔴 `Vee weren` — Verwijderd
- 🔴 `Veldafscheiding` — Verwijderd
- 🔴 `Verbetering koeling` — Verwijderd
- 🔴 `Verbetering luchtkwaliteit` — Verwijderd
- 🔴 `Verbetering vochthuishouding` — Verwijderd
- 🔴 `Verfraaiing` — Verwijderd
- 🔴 `Verkeerseiland` — Verwijderd
- 🔴 `Verkeersfunctie` — Verwijderd
- 🔴 `Verkeersgeleiding` — Verwijderd
- 🔴 `Verversing` — Verwijderd
- 🔴 `Verwijderen vervuiling` — Verwijderd
- 🔴 `Waterafvoer door infiltratie (Wadi)` — Verwijderd
- 🔴 `Waterafvoer of â€“berging algemeen` — Verwijderd
- 🔴 `Wild weren` — Verwijderd
- 🔴 `Windsingel` — Verwijderd
- 🔴 `Winterverblijf` — Verwijderd
- 🔴 `Zichthoek` — Verwijderd

##### `enum_Belasting` — 🔴 Verwijderd

**Literals:**

- 🔴 `Licht` — Verwijderd
- 🔴 `Normaal` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Zwaar` — Verwijderd

##### `enum_BelastingklasseNieuw` — 🔴 Verwijderd

**Literals:**

- 🔴 `Nog geen domeinwaaren bekend` — Verwijderd

##### `enum_BelastingklasseOud` — 🔴 Verwijderd

**Literals:**

- 🔴 `BK-100-1963 (.. Kg/m2)` — Verwijderd
- 🔴 `BK-30-1963 (200 kg/m2)` — Verwijderd
- 🔴 `BK-300` — Verwijderd
- 🔴 `BK-45-1963 (300 kg/m2)` — Verwijderd
- 🔴 `BK-450` — Verwijderd
- 🔴 `BK-60-1963 (400 kg/m2)` — Verwijderd
- 🔴 `BK-600` — Verwijderd
- 🔴 `BK-A-1938` — Verwijderd
- 🔴 `BK-B-1938` — Verwijderd
- 🔴 `BK-C-1938` — Verwijderd
- 🔴 `BK-D-1938` — Verwijderd
- 🔴 `NEN6723 VBB 1955` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `enum_Beleidsstatus` — 🔴 Verwijderd

**Literals:**

- 🔴 `Beschermwaardig/monumentaal` — Verwijderd
- 🔴 `Geen specifieke status-functionele laan- en parkbomen` — Verwijderd
- 🔴 `Geen specifieke status-verkorte omloop (tot ca. 20 jaar) en bomen 3e grootte` — Verwijderd
- 🔴 `Structuurbepalend/hoofd(groen/bomen)structuur` — Verwijderd

##### `enum_BeoogdeOmlooptijd` — 🔴 Verwijderd

**Literals:**

- 🔴 `10-20 jaar` — Verwijderd
- 🔴 `100-150 jaar` — Verwijderd
- 🔴 `150-200 jaar` — Verwijderd
- 🔴 `20-30 jaar` — Verwijderd
- 🔴 `30-50 jaar` — Verwijderd
- 🔴 `50-75 jaar` — Verwijderd
- 🔴 `75-100 jaar` — Verwijderd
- 🔴 `< 10 jaar` — Verwijderd
- 🔴 `>200 jaar` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `enum_Bereikbaarheid` — 🔴 Verwijderd

**Literals:**

- 🔴 `Bereikbaarheid met beperkingen` — Verwijderd
- 🔴 `Bereikbaarheid zonder beperkingen` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Onbereikbaar` — Verwijderd

##### `enum_BereikbaarheidKolk` — 🔴 Verwijderd

**Literals:**

- 🔴 `Grote zuiger` — Verwijderd
- 🔴 `Handmatig` — Verwijderd
- 🔴 `Kleine zuiger` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `enum_Boombeeld` — 🔴 Verwijderd

**Literals:**

- 🔴 `Aanvaard boombeeld` — Verwijderd
- 🔴 `Achterstallig boombeeld` — Verwijderd
- 🔴 `Boombeeld regulier (HB)` — Verwijderd
- 🔴 `Niet te beoordelen` — Verwijderd
- 🔴 `Niet van toepassing` — Verwijderd
- 🔴 `Verwaarloosd boombeeld` — Verwijderd

##### `enum_Boomgroep` — 🔴 Verwijderd

**Literals:**

- 🔴 `Boomweide` — Verwijderd
- 🔴 `Laanboom` — Verwijderd
- 🔴 `Solitaire boom` — Verwijderd

##### `enum_BoomhoogteklasseActueel` — 🔴 Verwijderd

**Literals:**

- 🔴 `12 tot 15 m.` — Verwijderd
- 🔴 `15 tot 18 m.` — Verwijderd
- 🔴 `18 tot 24 m.` — Verwijderd
- 🔴 `24 m. en hoger` — Verwijderd
- 🔴 `6 tot 9 m.` — Verwijderd
- 🔴 `9 tot 12 m.` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `tot 6 m.` — Verwijderd

##### `enum_BoomTypeBeschermingsstatusPlus` — 🔴 Verwijderd

**Literals:**

- 🔴 `Beeldbepalende boom` — Verwijderd
- 🔴 `Bijzondere groeivorm` — Verwijderd
- 🔴 `Bijzondere snoeivorm` — Verwijderd
- 🔴 `Bomenlijst boom` — Verwijderd
- 🔴 `Bomenstructuur boom` — Verwijderd
- 🔴 `Cultuurhistorisch waardevol` — Verwijderd
- 🔴 `Dendrologisch waardevol` — Verwijderd
- 🔴 `Ecologisch waardevol` — Verwijderd
- 🔴 `Herdenkingsboom` — Verwijderd
- 🔴 `Jaarrond beschermd nest` — Verwijderd
- 🔴 `Natuurwetenschappelijk waardevol` — Verwijderd
- 🔴 `Onderdeel van monumentale boomstructuur` — Verwijderd
- 🔴 `Toekomstboom` — Verwijderd
- 🔴 `Vaste rust- en of verblijfplaats` — Verwijderd
- 🔴 `Verblijfplaats Vleermuizen` — Verwijderd
- 🔴 `Veteranenboom` — Verwijderd
- 🔴 `Vliegroute vleermuizen` — Verwijderd
- 🔴 `Zeldzaamheidswaarde` — Verwijderd

##### `enum_Boomveiligheidsklasse` — 🔴 Verwijderd

**Literals:**

- 🔴 `Attentieboom` — Verwijderd
- 🔴 `Boom zonder gebreken` — Verwijderd
- 🔴 `Niet te beoordelen` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Risicoboom` — Verwijderd

##### `enum_Boomvoorziening` — 🔴 Verwijderd

**Literals:**

- 🔴 `Beluchtingsdrain` — Verwijderd
- 🔴 `Beluchtingssysteem aanlegfase` — Verwijderd
- 🔴 `Beluchtingssysteem permanent` — Verwijderd
- 🔴 `Boompaal` — Verwijderd
- 🔴 `Boomverankering` — Verwijderd
- 🔴 `Drainage` — Verwijderd
- 🔴 `Gietrand` — Verwijderd
- 🔴 `Infiltratiesysteem` — Verwijderd
- 🔴 `Kroonverankering` — Verwijderd
- 🔴 `Wortelgeleiding` — Verwijderd
- 🔴 `Wortelwering` — Verwijderd

##### `enum_BreedteklasseHaag` — 🔴 Verwijderd

**Literals:**

- 🔴 `0,5 tot 1 m.` — Verwijderd
- 🔴 `1 tot 1,5 m.` — Verwijderd
- 🔴 `1,5 tot 2 m.` — Verwijderd
- 🔴 `2 m. en groter` — Verwijderd
- 🔴 `Niet te beoordelen` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `tot 0,5 m.` — Verwijderd

##### `enum_Certificeringsinstantie` — 🔴 Verwijderd

**Literals:**

- 🔴 `Organisatiespecifieke domeinwaarden` — Verwijderd

##### `enum_Constructielaagsoort` — 🔴 Verwijderd

**Literals:**

- 🔴 `Asfaltverharding (deklaag)` — Verwijderd
- 🔴 `Asfaltverharding (onderlaag)` — Verwijderd
- 🔴 `Asfaltverharding (tussenlaag)` — Verwijderd
- 🔴 `Betonverharding` — Verwijderd
- 🔴 `Doek` — Verwijderd
- 🔴 `Elementenverharding` — Verwijderd
- 🔴 `Fundering` — Verwijderd
- 🔴 `Gras- en kruidachtigen` — Verwijderd
- 🔴 `Grondverbetering` — Verwijderd
- 🔴 `Halfverharding` — Verwijderd
- 🔴 `Kunststofverharding` — Verwijderd
- 🔴 `Natuurlijke ondergrond` — Verwijderd
- 🔴 `Ophoging` — Verwijderd
- 🔴 `Slijtlaag` — Verwijderd
- 🔴 `Straatlaag (elementenverharding)` — Verwijderd
- 🔴 `Wapening` — Verwijderd
- 🔴 `Zandbed` — Verwijderd

##### `enum_Constructietype` — 🔴 Verwijderd

**Literals:**

- 🔴 `Doosconstructie` — Verwijderd
- 🔴 `Tandoplegging` — Verwijderd

##### `enum_Controlefrequentie` — 🔴 Verwijderd

**Literals:**

- 🔴 `1 x per 10 jaar` — Verwijderd
- 🔴 `1 x per 2 jaar` — Verwijderd
- 🔴 `1 x per 3 jaar` — Verwijderd
- 🔴 `1 x per 4 jaar` — Verwijderd
- 🔴 `1 x per 5 jaar` — Verwijderd
- 🔴 `1 x per 6 jaar` — Verwijderd
- 🔴 `1 x per 7 jaar` — Verwijderd
- 🔴 `1 x per 8 jaar` — Verwijderd
- 🔴 `1 x per 9 jaar` — Verwijderd
- 🔴 `1 x per halfjaar` — Verwijderd
- 🔴 `1 x per jaar` — Verwijderd
- 🔴 `1 x per kwartaal` — Verwijderd
- 🔴 `1 x per maand` — Verwijderd
- 🔴 `3 x per jaar` — Verwijderd
- 🔴 `Niet van toepassing` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `enum_CultuurhistorischWaardevol` — 🔴 Verwijderd

**Literals:**

- 🔴 `Grafheuvel` — Verwijderd
- 🔴 `Graft` — Verwijderd
- 🔴 `Stinsenbeplanting` — Verwijderd
- 🔴 `Tuunwal` — Verwijderd

##### `enum_Doelsoort` — 🔴 Verwijderd

**Literals:**

- 🔴 `Algemene amfibieÃ«n` — Verwijderd
- 🔴 `Geen` — Verwijderd
- 🔴 `Kamsalamander` — Verwijderd
- 🔴 `Rugstreeppad` — Verwijderd

##### `enum_Fabrikant` — 🔴 Verwijderd

**Literals:**

- 🔴 `Organisatiespecifieke domeinwaarden` — Verwijderd

##### `enum_Formaat` — 🔴 Verwijderd

**Literals:**

- 🔴 `Dikformaat` — Verwijderd
- 🔴 `Dikformaat kant` — Verwijderd
- 🔴 `Dikformaat plat` — Verwijderd
- 🔴 `Gitruit` — Verwijderd
- 🔴 `Grootformaat` — Verwijderd
- 🔴 `Keiformaat` — Verwijderd
- 🔴 `Keiformaat kant` — Verwijderd
- 🔴 `Keiformaat plat` — Verwijderd
- 🔴 `Lingeformaat` — Verwijderd
- 🔴 `Noppen` — Verwijderd
- 🔴 `Ribbels` — Verwijderd
- 🔴 `Visbek` — Verwijderd
- 🔴 `Waalformaat` — Verwijderd
- 🔴 `Zeskant` — Verwijderd

##### `enum_FunderingLeiding` — 🔴 Verwijderd

**Literals:**

- 🔴 `Grondverbetering` — Verwijderd
- 🔴 `Kespen` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Onderheid` — Verwijderd
- 🔴 `Op staal` — Verwijderd
- 🔴 `Rietmatten` — Verwijderd
- 🔴 `Sloofconstructie` — Verwijderd

##### `enum_Gebiedstype` — 🔴 Verwijderd

**Literals:**

- 🔴 `Agrarisch gebied` — Verwijderd
- 🔴 `Begraafplaats` — Verwijderd
- 🔴 `Hoofdwegen` — Verwijderd
- 🔴 `Natuurgebied` — Verwijderd
- 🔴 `Recreatiegebied` — Verwijderd
- 🔴 `Sportterrein` — Verwijderd
- 🔴 `Waterwegen` — Verwijderd
- 🔴 `Werkgebied` — Verwijderd
- 🔴 `Winkelgebied` — Verwijderd
- 🔴 `Woongebied` — Verwijderd

##### `enum_GewenstSluitingspercentage` — 🔴 Verwijderd

**Literals:**

- 🔴 `N.v.t.` — Verwijderd
- 🔴 `Sluiting < 70%` — Verwijderd
- 🔴 `Sluiting >= 70% en < 90%` — Verwijderd
- 🔴 `Sluiting >= 90%` — Verwijderd

##### `enum_Groeifase` — 🔴 Verwijderd

**Literals:**

- 🔴 `Aanlegfase` — Verwijderd
- 🔴 `Eindfase` — Verwijderd
- 🔴 `Jeugdfase` — Verwijderd
- 🔴 `Niet te beoordelen` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Volwassen fase` — Verwijderd

##### `enum_GroenobjectBereikbaarheidPlus` — 🔴 Verwijderd

**Literals:**

- 🔴 `'s nachts werken` — Verwijderd
- 🔴 `Beperking aan de maximaal toegestane aslast` — Verwijderd
- 🔴 `Beperking aan de maximale doorrijhoogte` — Verwijderd
- 🔴 `Beperking aan de maximale voertuigbreedte` — Verwijderd
- 🔴 `Beperking door verhoogde ligging object` — Verwijderd
- 🔴 `Bereikbaarheidsvoorziening toepassen` — Verwijderd
- 🔴 `Duiken` — Verwijderd
- 🔴 `Hoogwerker gebruiken` — Verwijderd
- 🔴 `IndustriÃ«le omgeving` — Verwijderd
- 🔴 `Klimmen` — Verwijderd
- 🔴 `Laagwerker gebruiken` — Verwijderd
- 🔴 `Ladder gebruiken` — Verwijderd
- 🔴 `Niet bereikbaar voor hoogwerker` — Verwijderd
- 🔴 `Verkeersmaatregelen noodzakelijk` — Verwijderd
- 🔴 `Waadpak gebruiken` — Verwijderd
- 🔴 `Werk vanaf aanliggend perceel` — Verwijderd
- 🔴 `Werk vanaf water` — Verwijderd

##### `enum_Grondsoort` — 🔴 Verwijderd

**Literals:**

- 🔴 `Klei` — Verwijderd
- 🔴 `Klei/veen` — Verwijderd
- 🔴 `Leem` — Verwijderd
- 🔴 `LÃ¶ss` — Verwijderd
- 🔴 `Mergel` — Verwijderd
- 🔴 `Veen` — Verwijderd
- 🔴 `Zand` — Verwijderd

##### `enum_GrondsoortPlus` — 🔴 Verwijderd

**Literals:**

- 🔴 `Slap veen` — Verwijderd
- 🔴 `Zeer slap veen` — Verwijderd

##### `enum_HoogteklasseHaag` — 🔴 Verwijderd

**Literals:**

- 🔴 `0,5 tot 1 m.` — Verwijderd
- 🔴 `1 tot 2,5 m.` — Verwijderd
- 🔴 `2,5 meter en hoger` — Verwijderd
- 🔴 `Niet te beoordelen` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `tot 0,5 m.` — Verwijderd

##### `enum_IMKLThema` — 🔴 Verwijderd

**Literals:**

- 🔴 `(petro)chemie` — Verwijderd
- 🔴 `Buisleiding gevaarlijke inhoud` — Verwijderd
- 🔴 `Datatransport` — Verwijderd
- 🔴 `Gas hoge druk` — Verwijderd
- 🔴 `Gas lage druk` — Verwijderd
- 🔴 `Hoogspanning` — Verwijderd
- 🔴 `Laagspanning` — Verwijderd
- 🔴 `Landelijk hoogspanningsnet` — Verwijderd
- 🔴 `Middenspanning` — Verwijderd
- 🔴 `Overig` — Verwijderd
- 🔴 `Riool onder druk` — Verwijderd
- 🔴 `Riool vrijverval` — Verwijderd
- 🔴 `Warmte` — Verwijderd
- 🔴 `Water` — Verwijderd

##### `enum_Installateur` — 🔴 Verwijderd

**Literals:**

- 🔴 `Organisatiespecifieke domeinwaarden` — Verwijderd

##### `enum_Kleur` — 🔴 Verwijderd

**Literals:**

- 🔴 `Aardebruin` — Verwijderd
- 🔴 `Blauw` — Verwijderd
- 🔴 `Brons` — Verwijderd
- 🔴 `Bruin` — Verwijderd
- 🔴 `Geel` — Verwijderd
- 🔴 `Goud` — Verwijderd
- 🔴 `Grijs` — Verwijderd
- 🔴 `Groen` — Verwijderd
- 🔴 `Heidekleur` — Verwijderd
- 🔴 `Lichtbruin` — Verwijderd
- 🔴 `Metallic` — Verwijderd
- 🔴 `Oranje` — Verwijderd
- 🔴 `Paars` — Verwijderd
- 🔴 `Rood` — Verwijderd
- 🔴 `Roze` — Verwijderd
- 🔴 `Transparant` — Verwijderd
- 🔴 `Wit` — Verwijderd
- 🔴 `Zilver` — Verwijderd
- 🔴 `Zwart` — Verwijderd

##### `enum_KroondiameterklasseActueel` — 🔴 Verwijderd

**Literals:**

- 🔴 `10 tot 15 m.` — Verwijderd
- 🔴 `15 tot 20 m.` — Verwijderd
- 🔴 `20 m. en groter` — Verwijderd
- 🔴 `3 tot 5 m.` — Verwijderd
- 🔴 `5 tot 7 m.` — Verwijderd
- 🔴 `7 tot 10 m.` — Verwijderd
- 🔴 `Niet te beoordelen` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `tot 3 m.` — Verwijderd

##### `enum_KwaliteitsniveauGewenst` — 🔴 Verwijderd

**Literals:**

- 🔴 `A` — Verwijderd
- 🔴 `A+` — Verwijderd
- 🔴 `B` — Verwijderd
- 🔴 `C` — Verwijderd
- 🔴 `D` — Verwijderd

##### `enum_Kweker` — 🔴 Verwijderd

**Literals:**

- 🔴 `Organisatiespecifieke domeinwaarden` — Verwijderd

##### `enum_LengteKunstgras` — 🔴 Verwijderd

**Literals:**

- 🔴 `40 mm.` — Verwijderd
- 🔴 `60 mm.` — Verwijderd

##### `enum_Leverancier` — 🔴 Verwijderd

**Literals:**

- 🔴 `Organisatiespecifieke domeinwaarden` — Verwijderd

##### `enum_LiningType` — 🔴 Verwijderd

**Literals:**

- 🔴 `Anders` — Verwijderd
- 🔴 `Close fit lining` — Verwijderd
- 🔴 `Gesegmenteerde lining` — Verwijderd
- 🔴 `Lining aangebracht tijdens fabricage` — Verwijderd
- 🔴 `Lining met afzonderlijke buizen` — Verwijderd
- 🔴 `Lining met een doorlopende buis` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Opgespoten lining` — Verwijderd
- 🔴 `Ter plaatse uitgeharde lining` — Verwijderd
- 🔴 `Wikkelbuis relining` — Verwijderd

##### `enum_Markeringsbreedte` — 🔴 Verwijderd

**Literals:**

- 🔴 `0,10 m.` — Verwijderd
- 🔴 `0,15 m.` — Verwijderd
- 🔴 `0,20 m.` — Verwijderd
- 🔴 `0,30 m.` — Verwijderd
- 🔴 `0,45 m.` — Verwijderd
- 🔴 `3x 0,10 m.` — Verwijderd
- 🔴 `3x 0,15 m.` — Verwijderd

##### `enum_Markeringsoort` — 🔴 Verwijderd

**Literals:**

- 🔴 `Dwarsmarkering` — Verwijderd
- 🔴 `Lengtemarkering` — Verwijderd
- 🔴 `Overig` — Verwijderd

##### `enum_Markeringspatroon` — 🔴 Verwijderd

**Literals:**

- 🔴 `0,30-2,70` — Verwijderd
- 🔴 `1-1` — Verwijderd
- 🔴 `1-3` — Verwijderd
- 🔴 `2,70-0,30` — Verwijderd
- 🔴 `3-1` — Verwijderd
- 🔴 `3-3` — Verwijderd
- 🔴 `3-9` — Verwijderd
- 🔴 `9-3` — Verwijderd

##### `enum_Materiaal` — 🔴 Verwijderd

**Literals:**

- 🔴 `AC * base` — Verwijderd
- 🔴 `AC * bind` — Verwijderd
- 🔴 `AC * surf` — Verwijderd
- 🔴 `AC 11 bind` — Verwijderd
- 🔴 `AC 11 surf` — Verwijderd
- 🔴 `AC 16 base` — Verwijderd
- 🔴 `AC 16 bind` — Verwijderd
- 🔴 `AC 16 surf` — Verwijderd
- 🔴 `AC 22 base` — Verwijderd
- 🔴 `AC 22 bind` — Verwijderd
- 🔴 `AC 32 base` — Verwijderd
- 🔴 `AC 8 surf` — Verwijderd
- 🔴 `AVI- en AEC-bodemas` — Verwijderd
- 🔴 `Aluminium` — Verwijderd
- 🔴 `Asbestcement` — Verwijderd
- 🔴 `Asfalt` — Verwijderd
- 🔴 `Asfaltgranulaatstabilisatie` — Verwijderd
- 🔴 `Asfaltpuin` — Verwijderd
- 🔴 `Basalt` — Verwijderd
- 🔴 `Beton` — Verwijderd
- 🔴 `Betongranulaat` — Verwijderd
- 🔴 `Betonzand` — Verwijderd
- 🔴 `Bims` — Verwijderd
- 🔴 `Bitumen` — Verwijderd
- 🔴 `Bitumen-houtvezel composiet` — Verwijderd
- 🔴 `Boomschors` — Verwijderd
- 🔴 `Brekerzand` — Verwijderd
- 🔴 `Brekerzand-steenslagmengsel` — Verwijderd
- 🔴 `Brons` — Verwijderd
- 🔴 `Cementbeton` — Verwijderd
- 🔴 `Cementmortel` — Verwijderd
- 🔴 `Composiet` — Verwijderd
- 🔴 `Cortenstaal` — Verwijderd
- 🔴 `Deense tegels` — Verwijderd
- 🔴 `Drainagezand` — Verwijderd
- 🔴 `Driecomponenten koudplast` — Verwijderd
- 🔴 `E-bodemas` — Verwijderd
- 🔴 `Elementenbestrating` — Verwijderd
- 🔴 `Epoxy` — Verwijderd
- 🔴 `Fosforslakmengsel` — Verwijderd
- 🔴 `Franse kalksteen` — Verwijderd
- 🔴 `Franse schors` — Verwijderd
- 🔴 `Gaas` — Verwijderd
- 🔴 `Gaas met dood plantenmateriaal` — Verwijderd
- 🔴 `Gaas met kokosmat` — Verwijderd
- 🔴 `Gas met kunstmatig substraat` — Verwijderd
- 🔴 `Geanodiseerd aluminium` — Verwijderd
- 🔴 `Gehard spiegelglas` — Verwijderd
- 🔴 `Gekleurd en verduurzaamd geschredderd hout` — Verwijderd
- 🔴 `Geprofileerd markeringsmateriaal` — Verwijderd
- 🔴 `Gespoten beton` — Verwijderd
- 🔴 `Gewapend aluminium` — Verwijderd
- 🔴 `Gewapend beton` — Verwijderd
- 🔴 `GeÃ«mailleerd staal` — Verwijderd
- 🔴 `Gietijzer` — Verwijderd
- 🔴 `Glas` — Verwijderd
- 🔴 `Glasvezel` — Verwijderd
- 🔴 `Glasvezel versterkte kunststof` — Verwijderd
- 🔴 `Graniet` — Verwijderd
- 🔴 `Graniet Bleu Orient-China` — Verwijderd
- 🔴 `Graniet Bleu de Lanhelin-Frankrijk` — Verwijderd
- 🔴 `Graniet Braga-Portugal` — Verwijderd
- 🔴 `Graniet Roriz-Portugal` — Verwijderd
- 🔴 `Granulaat` — Verwijderd
- 🔴 `Gravel` — Verwijderd
- 🔴 `Gres` — Verwijderd
- 🔴 `Grijs gietijzer` — Verwijderd
- 🔴 `Grind` — Verwijderd
- 🔴 `Gritlaag` — Verwijderd
- 🔴 `Grond` — Verwijderd
- 🔴 `Grout` — Verwijderd
- 🔴 `HDPE` — Verwijderd
- 🔴 `Hardhout` — Verwijderd
- 🔴 `Hardsteen` — Verwijderd
- 🔴 `Hoogovenslakkenmengsel` — Verwijderd
- 🔴 `Hoogovenslakkenzand` — Verwijderd
- 🔴 `Hout` — Verwijderd
- 🔴 `Hydraulisch betongranulaat` — Verwijderd
- 🔴 `Hydraulisch menggranulaat` — Verwijderd
- 🔴 `Immobilisaat` — Verwijderd
- 🔴 `Kalksteen` — Verwijderd
- 🔴 `Karton` — Verwijderd
- 🔴 `Keien` — Verwijderd
- 🔴 `Kiezelbeton` — Verwijderd
- 🔴 `Kit` — Verwijderd
- 🔴 `Klei` — Verwijderd
- 🔴 `Kleischelpen` — Verwijderd
- 🔴 `Koper` — Verwijderd
- 🔴 `Koperslak` — Verwijderd
- 🔴 `Kunststof` — Verwijderd
- 🔴 `Kwartsiet` — Verwijderd
- 🔴 `LD-staalslakmengsel` — Verwijderd
- 🔴 `Lavasteen` — Verwijderd
- 🔴 `Leem` — Verwijderd
- 🔴 `Leislag` — Verwijderd
- 🔴 `Leisteen` — Verwijderd
- 🔴 `M3C zand` — Verwijderd
- 🔴 `Marmer` — Verwijderd
- 🔴 `Menggranulaat` — Verwijderd
- 🔴 `Messing` — Verwijderd
- 🔴 `Metaal, overig` — Verwijderd
- 🔴 `Metselwerk (baksteen)` — Verwijderd
- 🔴 `Metselwerk (bepleisterd)` — Verwijderd
- 🔴 `Metselwerk (onbepleisterd)` — Verwijderd
- 🔴 `Metselwerkgranulaat` — Verwijderd
- 🔴 `Metselzand` — Verwijderd
- 🔴 `Mijnsteen` — Verwijderd
- 🔴 `MozaÃ¯ek` — Verwijderd
- 🔴 `Natuursteen` — Verwijderd
- 🔴 `Natuursteen gevlamd` — Verwijderd
- 🔴 `Nodulair gietijzer` — Verwijderd
- 🔴 `Ophoogzand` — Verwijderd
- 🔴 `Polyester` — Verwijderd
- 🔴 `Polyesterbeton` — Verwijderd
- 🔴 `Polyetheen` — Verwijderd
- 🔴 `Polypropyleen` — Verwijderd
- 🔴 `Polyurethaan` — Verwijderd
- 🔴 `Polyvinylchloride` — Verwijderd
- 🔴 `Porfier` — Verwijderd
- 🔴 `Porfier Albiano-ItaliÃ«` — Verwijderd
- 🔴 `Puingranulaat` — Verwijderd
- 🔴 `RVS` — Verwijderd
- 🔴 `Rubber` — Verwijderd
- 🔴 `SMA*` — Verwijderd
- 🔴 `SMA-NL 11A` — Verwijderd
- 🔴 `SMA-NL 11B` — Verwijderd
- 🔴 `SMA-NL 5` — Verwijderd
- 🔴 `SMA-NL 8A` — Verwijderd
- 🔴 `Schraal beton` — Verwijderd
- 🔴 `Schuimbeton` — Verwijderd
- 🔴 `Schuimbitumenstabilisatie` — Verwijderd
- 🔴 `Silex` — Verwijderd
- 🔴 `Smashcourt` — Verwijderd
- 🔴 `Speelzand` — Verwijderd
- 🔴 `Staal` — Verwijderd
- 🔴 `Staal gegalvaniseerd` — Verwijderd
- 🔴 `Staal gepoedercoat` — Verwijderd
- 🔴 `Steen` — Verwijderd
- 🔴 `Steenpuin` — Verwijderd
- 🔴 `Steenslag` — Verwijderd
- 🔴 `Stol` — Verwijderd
- 🔴 `Straatzand` — Verwijderd
- 🔴 `Tegel keramiek` — Verwijderd
- 🔴 `Thermoplastisch materiaal` — Verwijderd
- 🔴 `Tufsteen` — Verwijderd
- 🔴 `Tweecomponenten koudplast` — Verwijderd
- 🔴 `Valzand` — Verwijderd
- 🔴 `Vezelcement` — Verwijderd
- 🔴 `Voegzand` — Verwijderd
- 🔴 `Voorgevormd plakmateriaal` — Verwijderd
- 🔴 `Wegenverf` — Verwijderd
- 🔴 `Wilgentenen` — Verwijderd
- 🔴 `ZOAB 11` — Verwijderd
- 🔴 `ZOAB 16` — Verwijderd
- 🔴 `ZOAB 22` — Verwijderd
- 🔴 `ZOAB PA*` — Verwijderd
- 🔴 `Zand voor kunstgras` — Verwijderd
- 🔴 `Zandasfalt` — Verwijderd
- 🔴 `Zandcement` — Verwijderd
- 🔴 `Zandgrindasfalt` — Verwijderd
- 🔴 `Zandsteen` — Verwijderd
- 🔴 `Zandsteen Gres-BelgiÃ«` — Verwijderd
- 🔴 `Zilverzand` — Verwijderd

##### `enum_Ondergroei` — 🔴 Verwijderd

**Literals:**

- 🔴 `Bodembedekkers` — Verwijderd
- 🔴 `Kruidachtig` — Verwijderd
- 🔴 `Natuurlijk` — Verwijderd
- 🔴 `Vaste planten` — Verwijderd

##### `enum_Onderhoudsplichtige` — 🔴 Verwijderd

**Literals:**

- 🔴 `Organisatiespecifieke domeinwaarden` — Verwijderd

##### `enum_Onderhoudsregime` — 🔴 Verwijderd

**Literals:**

- 🔴 `Nog geen domeinwaaren bekend` — Verwijderd

##### `enum_Ondersteuningsvorm` — 🔴 Verwijderd

**Literals:**

- 🔴 `Geluidsscherm` — Verwijderd
- 🔴 `Hekwerk` — Verwijderd
- 🔴 `Muur` — Verwijderd

##### `enum_OriÃ«ntatie` — 🔴 Verwijderd

**Literals:**

- 🔴 `Boven` — Verwijderd
- 🔴 `In` — Verwijderd
- 🔴 `Links` — Verwijderd
- 🔴 `Onder` — Verwijderd
- 🔴 `Op` — Verwijderd
- 🔴 `Rechts` — Verwijderd

##### `enum_OverbruggingsobjectModaliteit` — 🔴 Verwijderd

**Literals:**

- 🔴 `Autobus` — Verwijderd
- 🔴 `Bromfiets` — Verwijderd
- 🔴 `Bus` — Verwijderd
- 🔴 `Exceptioneel transport` — Verwijderd
- 🔴 `Fiets` — Verwijderd
- 🔴 `Gehandicaptenvoertuig` — Verwijderd
- 🔴 `Hulpverleningsvoertuig` — Verwijderd
- 🔴 `Landbouw- of bosbouwtrekker` — Verwijderd
- 🔴 `Langere en Zwaardere Vrachtautocombinatie (LZV)` — Verwijderd
- 🔴 `Lightrail` — Verwijderd
- 🔴 `Metro` — Verwijderd
- 🔴 `Motorfiets` — Verwijderd
- 🔴 `Personenauto` — Verwijderd
- 🔴 `Tram` — Verwijderd
- 🔴 `Trein` — Verwijderd
- 🔴 `Voetganger` — Verwijderd
- 🔴 `Vrachtauto (ontwerpvoertuig)` — Verwijderd

##### `enum_PlaatsoriÃ«ntatie` — 🔴 Verwijderd

**Literals:**

- 🔴 `L` — Verwijderd
- 🔴 `LL` — Verwijderd
- 🔴 `LM` — Verwijderd
- 🔴 `LR` — Verwijderd
- 🔴 `M` — Verwijderd
- 🔴 `O` — Verwijderd
- 🔴 `R` — Verwijderd
- 🔴 `RL` — Verwijderd
- 🔴 `RM` — Verwijderd
- 🔴 `RR` — Verwijderd

##### `enum_RioolputConstructieonderdeel` — 🔴 Verwijderd

**Literals:**

- 🔴 `Klep` — Verwijderd
- 🔴 `Lamellenafscheider` — Verwijderd
- 🔴 `Ontspanningsventiel` — Verwijderd
- 🔴 `OntstoppingsstukÂ Â` — Verwijderd
- 🔴 `Overstortdrempel` — Verwijderd
- 🔴 `Regelstuw` — Verwijderd
- 🔴 `Schildmuur` — Verwijderd
- 🔴 `Slibafscheider` — Verwijderd
- 🔴 `SlibvangputÂ Â` — Verwijderd
- 🔴 `Spoelklep` — Verwijderd
- 🔴 `Spoelvoorziening` — Verwijderd
- 🔴 `Standmeter` — Verwijderd
- 🔴 `Stroomprofiel` — Verwijderd
- 🔴 `Stuwconstructie` — Verwijderd
- 🔴 `Stuwmuur` — Verwijderd
- 🔴 `Terugslagklep` — Verwijderd
- 🔴 `UitklimvoorzieningÂ Â` — Verwijderd
- 🔴 `VeiligheidsroosterÂ Â` — Verwijderd
- 🔴 `VetafscheiderÂ Â` — Verwijderd
- 🔴 `VuilvangroosterÂ Â` — Verwijderd
- 🔴 `Wand` — Verwijderd
- 🔴 `Zonk` — Verwijderd

##### `enum_Snoeifase` — 🔴 Verwijderd

**Literals:**

- 🔴 `Begeleidingssnoeifase` — Verwijderd
- 🔴 `Niet van toepassing` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Onderhoudssnoeifase` — Verwijderd

##### `enum_Soortnaam` — 🔴 Verwijderd

**Literals:**

- 🔴 `http://www.internationalplantnames.com/` — Verwijderd

##### `enum_SoortPlantenbak` — 🔴 Verwijderd

**Literals:**

- 🔴 `Bak` — Verwijderd
- 🔴 `Hangende bloembak` — Verwijderd
- 🔴 `Piramide` — Verwijderd
- 🔴 `Schaal` — Verwijderd
- 🔴 `Zuil` — Verwijderd

##### `enum_SoortVoeg` — 🔴 Verwijderd

**Literals:**

- 🔴 `Dwarsvoeg` — Verwijderd
- 🔴 `Langsvoeg` — Verwijderd

##### `enum_SpeelterreinLeeftijdDoelgroep` — 🔴 Verwijderd

**Literals:**

- 🔴 `13 tot 15 jaar` — Verwijderd
- 🔴 `16 tot 19 jaar` — Verwijderd
- 🔴 `6 tot 12 jaar` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `tot 5 jaar` — Verwijderd

##### `enum_SpeeltoestelToestelonderdeel` — 🔴 Verwijderd

**Literals:**

- 🔴 `Balustrade` — Verwijderd
- 🔴 `Brandweerpaal` — Verwijderd
- 🔴 `Cluster` — Verwijderd
- 🔴 `Glijbaan` — Verwijderd
- 🔴 `Hellingbaan` — Verwijderd
- 🔴 `Ketting` — Verwijderd
- 🔴 `Klimtoestel` — Verwijderd
- 🔴 `Ladder` — Verwijderd
- 🔴 `Leuning` — Verwijderd
- 🔴 `Platform` — Verwijderd
- 🔴 `Reling` — Verwijderd
- 🔴 `Ruimtenet` — Verwijderd
- 🔴 `Schommel` — Verwijderd
- 🔴 `Speelhuisje` — Verwijderd
- 🔴 `Steil speelelement` — Verwijderd
- 🔴 `Touw` — Verwijderd
- 🔴 `Touwbrug` — Verwijderd
- 🔴 `Trap` — Verwijderd
- 🔴 `Trapsgewijs platform` — Verwijderd
- 🔴 `Tunnel` — Verwijderd
- 🔴 `Zware hangende balk` — Verwijderd

##### `enum_SportterreinTypeSport` — 🔴 Verwijderd

**Literals:**

- 🔴 `Atletiek` — Verwijderd
- 🔴 `Beach volleybal` — Verwijderd
- 🔴 `Cricket` — Verwijderd
- 🔴 `Handboogschieten` — Verwijderd
- 🔴 `Honkbal` — Verwijderd
- 🔴 `Jeu de boules` — Verwijderd
- 🔴 `Kaatsen` — Verwijderd
- 🔴 `Kogelslingeren` — Verwijderd
- 🔴 `Korfbal` — Verwijderd
- 🔴 `Paardrijden` — Verwijderd
- 🔴 `Rugby` — Verwijderd
- 🔴 `Schieten` — Verwijderd
- 🔴 `Softbal` — Verwijderd
- 🔴 `Tennis` — Verwijderd
- 🔴 `Voetbal` — Verwijderd
- 🔴 `Volleybal` — Verwijderd
- 🔴 `Wielrennen` — Verwijderd
- 🔴 `Zweefvliegen` — Verwijderd

##### `enum_Stamdiameterklasse` — 🔴 Verwijderd

**Literals:**

- 🔴 `0,2 tot 0,3 m.` — Verwijderd
- 🔴 `0,3 tot 0,5 m.` — Verwijderd
- 🔴 `0,5 tot 1 m.` — Verwijderd
- 🔴 `1 m. en groter` — Verwijderd
- 🔴 `Niet te beoordelen` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `tot 0,2 m.` — Verwijderd

##### `enum_Status` — 🔴 Verwijderd

**Literals:**

- 🔴 `Bestaand` — Verwijderd
- 🔴 `Nieuw` — Verwijderd
- 🔴 `Ontwerp` — Verwijderd
- 🔴 `Vervallen` — Verwijderd

##### `enum_TakvrijeStam` — 🔴 Verwijderd

**Literals:**

- 🔴 `0 m.` — Verwijderd
- 🔴 `2 m.` — Verwijderd
- 🔴 `4 m.` — Verwijderd
- 🔴 `6 m.` — Verwijderd
- 🔴 `8 m.` — Verwijderd
- 🔴 `Anders, namelijk` — Verwijderd
- 🔴 `Niet te beoordelen` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `enum_Taludsteilte` — 🔴 Verwijderd

**Literals:**

- 🔴 `1:3 tot 1:2` — Verwijderd
- 🔴 `1:4 tot 1:3` — Verwijderd
- 🔴 `< 1 : 4` — Verwijderd
- 🔴 `> 1:2` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `enum_Toestelgroep` — 🔴 Verwijderd

**Literals:**

- 🔴 `Groot` — Verwijderd
- 🔴 `Klein` — Verwijderd
- 🔴 `Middelgroot` — Verwijderd
- 🔴 `Zeer groot` — Verwijderd

##### `enum_Type` — 🔴 Verwijderd

**Literals:**

- 🔴 `Aansluitleiding` — Verwijderd
- 🔴 `Adoptiebak` — Verwijderd
- 🔴 `Afgezonken tunnel` — Verwijderd
- 🔴 `Afsluiter beregeningsleiding` — Verwijderd
- 🔴 `Afsluiter gasleiding` — Verwijderd
- 🔴 `Afsluiter rioolleiding` — Verwijderd
- 🔴 `Afsluiter waterleiding` — Verwijderd
- 🔴 `Asbaktegel` — Verwijderd
- 🔴 `Asfaltverharding` — Verwijderd
- 🔴 `Atletiekbaan` — Verwijderd
- 🔴 `Atletiekvoorziening` — Verwijderd
- 🔴 `Avontuurlijke speelplek` — Verwijderd
- 🔴 `Backstop` — Verwijderd
- 🔴 `Bak` — Verwijderd
- 🔴 `Balspelterrein` — Verwijderd
- 🔴 `Basaltblokken` — Verwijderd
- 🔴 `Basket` — Verwijderd
- 🔴 `Basketbalbord` — Verwijderd
- 🔴 `Basketbalpaal` — Verwijderd
- 🔴 `Bebakeningselement` — Verwijderd
- 🔴 `Bebouwde kombord` — Verwijderd
- 🔴 `Bedekt` — Verwijderd
- 🔴 `Begroeid` — Verwijderd
- 🔴 `Beheervak - brug` — Verwijderd
- 🔴 `Beheervak - gemaal` — Verwijderd
- 🔴 `Beheervak - sluis` — Verwijderd
- 🔴 `Beheervak - tunnel` — Verwijderd
- 🔴 `Beheervak - verkeersregelinstallatie` — Verwijderd
- 🔴 `Behendigheidstoestel` — Verwijderd
- 🔴 `Beluchtingsrooster` — Verwijderd
- 🔴 `Beregeningspomp` — Verwijderd
- 🔴 `Berging` — Verwijderd
- 🔴 `Betonverharding` — Verwijderd
- 🔴 `Beweegbare brug` — Verwijderd
- 🔴 `Bijzondere putconstructie` — Verwijderd
- 🔴 `Binnenterrein` — Verwijderd
- 🔴 `Biofilter` — Verwijderd
- 🔴 `Blauwe spiegel` — Verwijderd
- 🔴 `Bodembedekkers` — Verwijderd
- 🔴 `Bomengranulaat` — Verwijderd
- 🔴 `Bomengrond` — Verwijderd
- 🔴 `Bomenzand` — Verwijderd
- 🔴 `Boom` — Verwijderd
- 🔴 `Boom niet vrij uitgroeiend` — Verwijderd
- 🔴 `Boom vrij uitgroeiend` — Verwijderd
- 🔴 `Boombank` — Verwijderd
- 🔴 `Boombumper` — Verwijderd
- 🔴 `Boombunker` — Verwijderd
- 🔴 `Boomjuk` — Verwijderd
- 🔴 `Boomkorf` — Verwijderd
- 🔴 `Boomkrans` — Verwijderd
- 🔴 `Boomkratten` — Verwijderd
- 🔴 `Boomrooster` — Verwijderd
- 🔴 `Boomteelt` — Verwijderd
- 🔴 `Boostergemaal` — Verwijderd
- 🔴 `Bord` — Verwijderd
- 🔴 `Bosplantsoen` — Verwijderd
- 🔴 `Bouwland` — Verwijderd
- 🔴 `Bouwspeelplaats` — Verwijderd
- 🔴 `Bouwwerk` — Verwijderd
- 🔴 `Bromfietsdrempel` — Verwijderd
- 🔴 `Brugwachterskantoor` — Verwijderd
- 🔴 `Buffer` — Verwijderd
- 🔴 `Buishek` — Verwijderd
- 🔴 `Buispaal` — Verwijderd
- 🔴 `Buitenfitness` — Verwijderd
- 🔴 `Bushalteband` — Verwijderd
- 🔴 `Busvriendelijke verkeersdrempel` — Verwijderd
- 🔴 `Centrifugaalpomp` — Verwijderd
- 🔴 `Combinatietoestel` — Verwijderd
- 🔴 `DRIP` — Verwijderd
- 🔴 `Damtafel` — Verwijderd
- 🔴 `Dienstgang` — Verwijderd
- 🔴 `DilatatievoegovergangÂ` — Verwijderd
- 🔴 `Doel` — Verwijderd
- 🔴 `Doelwand` — Verwijderd
- 🔴 `Doorspoelput` — Verwijderd
- 🔴 `Doorspuitput` — Verwijderd
- 🔴 `Draaiende reflector` — Verwijderd
- 🔴 `Draaitoestel` — Verwijderd
- 🔴 `Drijvende bak` — Verwijderd
- 🔴 `Drijvende mat` — Verwijderd
- 🔴 `Drinkwatermeter` — Verwijderd
- 🔴 `Drukrioleringspomp` — Verwijderd
- 🔴 `Dubbele bak` — Verwijderd
- 🔴 `Dubbelkerende afsluiter` — Verwijderd
- 🔴 `Duikelrek` — Verwijderd
- 🔴 `Duikelrek fitness` — Verwijderd
- 🔴 `Duin` — Verwijderd
- 🔴 `Duiventil` — Verwijderd
- 🔴 `Dwarsgang` — Verwijderd
- 🔴 `Dynamische snelheidsindicator` — Verwijderd
- 🔴 `Educatietoestel` — Verwijderd
- 🔴 `Eenvoudige picknicktafel` — Verwijderd
- 🔴 `Eenzijdig kerende afsluiter` — Verwijderd
- 🔴 `Eigen bouw` — Verwijderd
- 🔴 `Elektrische slagboom` — Verwijderd
- 🔴 `Elementenverharding` — Verwijderd
- 🔴 `Enkele bak` — Verwijderd
- 🔴 `Erfafscheidingsput` — Verwijderd
- 🔴 `Externe overstortconstructie` — Verwijderd
- 🔴 `Familiegraf` — Verwijderd
- 🔴 `Faunatunnel groot` — Verwijderd
- 🔴 `Faunatunnel klein` — Verwijderd
- 🔴 `Fietsabri` — Verwijderd
- 🔴 `Fietsbeugel` — Verwijderd
- 🔴 `Fietscrossbaan` — Verwijderd
- 🔴 `Fietsenkluis` — Verwijderd
- 🔴 `Fietsenrek` — Verwijderd
- 🔴 `Fietsklem` — Verwijderd
- 🔴 `Fietssleuf` — Verwijderd
- 🔴 `Fietssteun` — Verwijderd
- 🔴 `Fietstrommel` — Verwijderd
- 🔴 `Fitnesstoestel` — Verwijderd
- 🔴 `Flespaal` — Verwijderd
- 🔴 `Flexibele voegovergang` — Verwijderd
- 🔴 `Fruitboom` — Verwijderd
- 🔴 `Fruitteelt` — Verwijderd
- 🔴 `FunctioneelGebied` — Verwijderd
- 🔴 `GRIP` — Verwijderd
- 🔴 `GVC beschoeiing` — Verwijderd
- 🔴 `Gaashek` — Verwijderd
- 🔴 `Gazonband` — Verwijderd
- 🔴 `Geallieerdengraf` — Verwijderd
- 🔴 `Geboorde tunnel` — Verwijderd
- 🔴 `Gecombineerde straat-trottoirkolk` — Verwijderd
- 🔴 `Gegraven tunnel` — Verwijderd
- 🔴 `Gekandelaberde boom` — Verwijderd
- 🔴 `Geleideband` — Verwijderd
- 🔴 `Geleidebarrier` — Verwijderd
- 🔴 `Geleidehek` — Verwijderd
- 🔴 `Geleiderail` — Verwijderd
- 🔴 `Gemaal in droge opstelling` — Verwijderd
- 🔴 `Gemaal in natte opstelling` — Verwijderd
- 🔴 `Gemengd bos` — Verwijderd
- 🔴 `Gierzwaluwtil` — Verwijderd
- 🔴 `Glijbaan` — Verwijderd
- 🔴 `Graft` — Verwijderd
- 🔴 `Gras- en kruidachtigen` — Verwijderd
- 🔴 `Grasland agrarisch` — Verwijderd
- 🔴 `Grasland overig` — Verwijderd
- 🔴 `Greppel` — Verwijderd
- 🔴 `Groenobject` — Verwijderd
- 🔴 `Grondwatermeetpunt` — Verwijderd
- 🔴 `Grondwatermeter` — Verwijderd
- 🔴 `Groot wild` — Verwijderd
- 🔴 `Grote sproeier` — Verwijderd
- 🔴 `Haag` — Verwijderd
- 🔴 `Halfverharding` — Verwijderd
- 🔴 `Haltetegel` — Verwijderd
- 🔴 `Handbediende slagboom` — Verwijderd
- 🔴 `Heesters` — Verwijderd
- 🔴 `Hefdeur` — Verwijderd
- 🔴 `Heide` — Verwijderd
- 🔴 `Hek Verre Veld` — Verwijderd
- 🔴 `Hoekblok` — Verwijderd
- 🔴 `Hondenpoepbak` — Verwijderd
- 🔴 `Hondenrooster` — Verwijderd
- 🔴 `Hoog raster` — Verwijderd
- 🔴 `HoogspanningskabelÂ Â` — Verwijderd
- 🔴 `Houten beschoeiing` — Verwijderd
- 🔴 `Houtwal` — Verwijderd
- 🔴 `Huisvuilcontainerplaats` — Verwijderd
- 🔴 `IBA` — Verwijderd
- 🔴 `IJsvogelwand` — Verwijderd
- 🔴 `Ijsbaan` — Verwijderd
- 🔴 `Infiltratiebassin` — Verwijderd
- 🔴 `Infiltratiekolk` — Verwijderd
- 🔴 `Informatief verkeersbord` — Verwijderd
- 🔴 `Inspectieput` — Verwijderd
- 🔴 `Installatie` — Verwijderd
- 🔴 `Interne overstortconstructie` — Verwijderd
- 🔴 `Jeu de Boules` — Verwijderd
- 🔴 `JongerenOntmoetingsPlek` — Verwijderd
- 🔴 `Kabelbaan` — Verwijderd
- 🔴 `Kast` — Verwijderd
- 🔴 `Keermuur met bank` — Verwijderd
- 🔴 `Keermuur met plantenbak` — Verwijderd
- 🔴 `Keersluis` — Verwijderd
- 🔴 `Kleine sproeier` — Verwijderd
- 🔴 `Klimklauterparcours` — Verwijderd
- 🔴 `Klimplant` — Verwijderd
- 🔴 `Klimtoestel` — Verwijderd
- 🔴 `Knikkertegel` — Verwijderd
- 🔴 `Knotboom` — Verwijderd
- 🔴 `Korfbalpaal` — Verwijderd
- 🔴 `Kruisingsput` — Verwijderd
- 🔴 `Kunststofverharding` — Verwijderd
- 🔴 `Kunstwerk` — Verwijderd
- 🔴 `Kwelder` — Verwijderd
- 🔴 `Laadperron` — Verwijderd
- 🔴 `Laag raster` — Verwijderd
- 🔴 `Laagspanningskabel` — Verwijderd
- 🔴 `Lamellenvoegovergang` — Verwijderd
- 🔴 `Leiboom` — Verwijderd
- 🔴 `Leiding` — Verwijderd
- 🔴 `Leidingelement` — Verwijderd
- 🔴 `Leiplant` — Verwijderd
- 🔴 `Lijnmarkering` — Verwijderd
- 🔴 `Loofbos` — Verwijderd
- 🔴 `Lozingspunt` — Verwijderd
- 🔴 `Lozingsput` — Verwijderd
- 🔴 `Mast` — Verwijderd
- 🔴 `Matten` — Verwijderd
- 🔴 `Mattenvoegovergang` — Verwijderd
- 🔴 `Mechanische rioolleiding` — Verwijderd
- 🔴 `Mechanische transportleiding` — Verwijderd
- 🔴 `Meervoudige voegovergang` — Verwijderd
- 🔴 `Met instroomvoorziening` — Verwijderd
- 🔴 `Meubilair` — Verwijderd
- 🔴 `Microtunneling,` — Verwijderd
- 🔴 `MiddenspanningskabelÂ Â` — Verwijderd
- 🔴 `Midgetgolfbaan` — Verwijderd
- 🔴 `Moeras` — Verwijderd
- 🔴 `Monsternamepunt` — Verwijderd
- 🔴 `Motorfietsdrempel` — Verwijderd
- 🔴 `Muur met hek` — Verwijderd
- 🔴 `Naaldbos` — Verwijderd
- 🔴 `Natte pompkelderÂ` — Verwijderd
- 🔴 `Natuurlijke elementen` — Verwijderd
- 🔴 `Nestkast voor vogels` — Verwijderd
- 🔴 `Nestkast voor zoogdieren` — Verwijderd
- 🔴 `Net` — Verwijderd
- 🔴 `Nooduitlaat` — Verwijderd
- 🔴 `Oeverzwaluwenwand` — Verwijderd
- 🔴 `Omleidingsbord` — Verwijderd
- 🔴 `Onbedekt` — Verwijderd
- 🔴 `Onderbord` — Verwijderd
- 🔴 `Onderwaterbeschoeiing` — Verwijderd
- 🔴 `Ontstoppingsput` — Verwijderd
- 🔴 `Onverhard` — Verwijderd
- 🔴 `Oorlogsgraf` — Verwijderd
- 🔴 `Opbouwputtunnel` — Verwijderd
- 🔴 `Opruimplicht hondenpoep` — Verwijderd
- 🔴 `Opsluitband` — Verwijderd
- 🔴 `Overbruggingsobject` — Verwijderd
- 🔴 `Overdekte bank` — Verwijderd
- 🔴 `Overgangsconstructie voor integraal kunstwerk` — Verwijderd
- 🔴 `Overkapping` — Verwijderd
- 🔴 `Overnamepunt` — Verwijderd
- 🔴 `Overstortput` — Verwijderd
- 🔴 `Paal` — Verwijderd
- 🔴 `Paaltje (Amsterdammertje)` — Verwijderd
- 🔴 `Palen met draad` — Verwijderd
- 🔴 `Palen met planken` — Verwijderd
- 🔴 `Parcours` — Verwijderd
- 🔴 `Parkeerbord` — Verwijderd
- 🔴 `Perceelaansluitpunt` — Verwijderd
- 🔴 `Perkoen` — Verwijderd
- 🔴 `Persluchtpomp` — Verwijderd
- 🔴 `Picknicktafel zeshoekig` — Verwijderd
- 🔴 `Piramideblok` — Verwijderd
- 🔴 `Planken beschoeiing` — Verwijderd
- 🔴 `Planten` — Verwijderd
- 🔴 `Poef` — Verwijderd
- 🔴 `Pompput` — Verwijderd
- 🔴 `Puntdeur` — Verwijderd
- 🔴 `Puntmarkering` — Verwijderd
- 🔴 `Put` — Verwijderd
- 🔴 `Putschacht` — Verwijderd
- 🔴 `Reddingsboei` — Verwijderd
- 🔴 `Reddingshaak` — Verwijderd
- 🔴 `Reinigende put` — Verwijderd
- 🔴 `Rietland` — Verwijderd
- 🔴 `Rij-ijzer` — Verwijderd
- 🔴 `Rijbaan` — Verwijderd
- 🔴 `Rijrichtingbord` — Verwijderd
- 🔴 `Rijstrook` — Verwijderd
- 🔴 `Rimob` — Verwijderd
- 🔴 `Riooleindgemaal` — Verwijderd
- 🔴 `Rioolput met geleiding` — Verwijderd
- 🔴 `Roldeur` — Verwijderd
- 🔴 `Rood wit paaltje (toegangsbeperking)` — Verwijderd
- 🔴 `Roostergoot` — Verwijderd
- 🔴 `Sandwichconstructie` — Verwijderd
- 🔴 `Schaaktafel` — Verwijderd
- 🔴 `Schampblok` — Verwijderd
- 🔴 `Schampkant` — Verwijderd
- 🔴 `Scheiding` — Verwijderd
- 🔴 `Schijnvoeg` — Verwijderd
- 🔴 `Schommel` — Verwijderd
- 🔴 `Schoolspeelplaats` — Verwijderd
- 🔴 `Schotbalk` — Verwijderd
- 🔴 `SchroefcentrifugaalpompÂ` — Verwijderd
- 🔴 `Schroefpomp` — Verwijderd
- 🔴 `Schuine trottoirband` — Verwijderd
- 🔴 `Schutsluis` — Verwijderd
- 🔴 `Sensor` — Verwijderd
- 🔴 `Septictank` — Verwijderd
- 🔴 `Sierhek` — Verwijderd
- 🔴 `Signaleringsband` — Verwijderd
- 🔴 `Sinusvormige verkeersdrempel` — Verwijderd
- 🔴 `Skateboardbaan` — Verwijderd
- 🔴 `Skateterrein` — Verwijderd
- 🔴 `Skatevoorziening` — Verwijderd
- 🔴 `Slik` — Verwijderd
- 🔴 `Sluiswachterskantoor` — Verwijderd
- 🔴 `Snelheidsbord` — Verwijderd
- 🔴 `Sociaal spel` — Verwijderd
- 🔴 `Solitair gras` — Verwijderd
- 🔴 `Solitaire heester` — Verwijderd
- 🔴 `Speciale bank` — Verwijderd
- 🔴 `Speelkuil` — Verwijderd
- 🔴 `Speelplek` — Verwijderd
- 🔴 `Speeltuin` — Verwijderd
- 🔴 `Spijlenhek` — Verwijderd
- 🔴 `Spiraal gegolfd stalen duikerbuizen` — Verwijderd
- 🔴 `Spoor` — Verwijderd
- 🔴 `Sportcombinatietoestel` — Verwijderd
- 🔴 `Spuisluis` — Verwijderd
- 🔴 `Staafmathek` — Verwijderd
- 🔴 `Standaard` — Verwijderd
- 🔴 `Standaard reflector` — Verwijderd
- 🔴 `Stedenbandbord` — Verwijderd
- 🔴 `Steilwand` — Verwijderd
- 🔴 `Stobbe` — Verwijderd
- 🔴 `Stootband` — Verwijderd
- 🔴 `Straatbank` — Verwijderd
- 🔴 `Straatkolk` — Verwijderd
- 🔴 `Struiken` — Verwijderd
- 🔴 `Struikrozen` — Verwijderd
- 🔴 `Stuwput` — Verwijderd
- 🔴 `Tafeltennistafel` — Verwijderd
- 🔴 `Technische gang` — Verwijderd
- 🔴 `Tennisbaan` — Verwijderd
- 🔴 `Tennisbaanafrastering` — Verwijderd
- 🔴 `Terreindeel` — Verwijderd
- 🔴 `Thematische bank` — Verwijderd
- 🔴 `Thematische picknicktafel` — Verwijderd
- 🔴 `Toegangshekinstallatie` — Verwijderd
- 🔴 `Toegangspoort` — Verwijderd
- 🔴 `Toldeur` — Verwijderd
- 🔴 `Trapeziumvormige verkeersdrempel` — Verwijderd
- 🔴 `Trimbaan` — Verwijderd
- 🔴 `Trottoirband` — Verwijderd
- 🔴 `Trottoirkolk` — Verwijderd
- 🔴 `Tunnelobject` — Verwijderd
- 🔴 `Turntoestel` — Verwijderd
- 🔴 `Uitlaatpunt` — Verwijderd
- 🔴 `Uitneembare brug` — Verwijderd
- 🔴 `V-polder` — Verwijderd
- 🔴 `VacuÃ¼mpompstation` — Verwijderd
- 🔴 `Vaste brug` — Verwijderd
- 🔴 `Veerooster` — Verwijderd
- 🔴 `Vegetatieobject` — Verwijderd
- 🔴 `Veldafscheiding` — Verwijderd
- 🔴 `Velddrain` — Verwijderd
- 🔴 `Verbindingsstuk` — Verwijderd
- 🔴 `Verbodsbord` — Verwijderd
- 🔴 `Verborgen voegovergang` — Verwijderd
- 🔴 `Verdekte put` — Verwijderd
- 🔴 `Verholen goot` — Verwijderd
- 🔴 `Verkeersplateau` — Verwijderd
- 🔴 `Verkeerstegel` — Verwijderd
- 🔴 `Verlichtingsobject` — Verwijderd
- 🔴 `Verwijsbord` — Verwijderd
- 🔴 `Verzameldrain` — Verwijderd
- 🔴 `Verzamelput` — Verwijderd
- 🔴 `Vijzelgemaal` — Verwijderd
- 🔴 `Vijzelpomp` — Verwijderd
- 🔴 `Vingervoegovergang` — Verwijderd
- 🔴 `Visoverwinteringsplek` — Verwijderd
- 🔴 `Vlakmarkering` — Verwijderd
- 🔴 `Vluchtdeur` — Verwijderd
- 🔴 `Vluchtgang` — Verwijderd
- 🔴 `Voegovergang met of zonder balken en randprofielen met afdichtingrubbers` — Verwijderd
- 🔴 `Voetbalveld` — Verwijderd
- 🔴 `Volleybalset` — Verwijderd
- 🔴 `Voorrangsbord` — Verwijderd
- 🔴 `Voorwaarschuwingsbord` — Verwijderd
- 🔴 `Vormboom` — Verwijderd
- 🔴 `Vrijverval rioolleiding` — Verwijderd
- 🔴 `Vrijverval transportleiding` — Verwijderd
- 🔴 `Waaierdeur` — Verwijderd
- 🔴 `Waarschuwingsbord` — Verwijderd
- 🔴 `Wand` — Verwijderd
- 🔴 `Wanden dak methode tunnel` — Verwijderd
- 🔴 `Water over water` — Verwijderd
- 🔴 `Water over weg` — Verwijderd
- 🔴 `Waterinrichtingsobject` — Verwijderd
- 🔴 `Waterloop` — Verwijderd
- 🔴 `Waterobject` — Verwijderd
- 🔴 `Waterspeelplaats` — Verwijderd
- 🔴 `Waterspeeltoestel` — Verwijderd
- 🔴 `Watervlakte` — Verwijderd
- 🔴 `Watervogels` — Verwijderd
- 🔴 `Weg` — Verwijderd
- 🔴 `Weginrichtingsobject` — Verwijderd
- 🔴 `Wegobject` — Verwijderd
- 🔴 `Werk in uitvoering-bord` — Verwijderd
- 🔴 `Wervelput` — Verwijderd
- 🔴 `Wildrooster` — Verwijderd
- 🔴 `Wildspiegel op voet` — Verwijderd
- 🔴 `Winterverblijf algemene amfibieÃ«n en kamsalamder` — Verwijderd
- 🔴 `Winterverblijf amfibieÃ«n` — Verwijderd
- 🔴 `Winterverblijf rugstreeppad` — Verwijderd
- 🔴 `Winterverblijf slangen` — Verwijderd
- 🔴 `Wiptoestel` — Verwijderd
- 🔴 `Zandspeelplaats` — Verwijderd
- 🔴 `Zandspeeltoestel` — Verwijderd
- 🔴 `Zandvlakte` — Verwijderd
- 🔴 `Zeecontainer` — Verwijderd
- 🔴 `Zinkerput` — Verwijderd
- 🔴 `Zinkvoeg` — Verwijderd
- 🔴 `Zinloos geweld tegel` — Verwijderd
- 🔴 `Zitmuur` — Verwijderd
- 🔴 `Zuigerpomp` — Verwijderd

##### `enum_TypeAfdekking` — 🔴 Verwijderd

**Literals:**

- 🔴 `Gekneveld` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Ontluchtingsklep` — Verwijderd
- 🔴 `Roosterdeksel` — Verwijderd
- 🔴 `Roosterlopen` — Verwijderd
- 🔴 `Selflevel` — Verwijderd

##### `enum_TypeAsbesthoudend` — 🔴 Verwijderd

**Literals:**

- 🔴 `Asbesthoudend` — Verwijderd
- 🔴 `Asbestverdacht` — Verwijderd
- 🔴 `Asbestvrij` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `enum_TypeBediening` — 🔴 Verwijderd

**Literals:**

- 🔴 `Elektrisch` — Verwijderd
- 🔴 `Elektro-mechanisch` — Verwijderd
- 🔴 `Handmatig` — Verwijderd
- 🔴 `Hydraulisch` — Verwijderd
- 🔴 `Magnetisch` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `enum_TypeBeheerder` — 🔴 Verwijderd

**Literals:**

- 🔴 `Gemeente` — Verwijderd
- 🔴 `Ministerie van Defensie` — Verwijderd
- 🔴 `Ministerie van Economische Zaken` — Verwijderd
- 🔴 `Ministerie van Infrastructuur en Waterstaat` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Particulier` — Verwijderd
- 🔴 `Prorail` — Verwijderd
- 🔴 `Provincie` — Verwijderd
- 🔴 `Waterschap` — Verwijderd

##### `enum_TypeBeheerderPlus` — 🔴 Verwijderd

**Literals:**

- 🔴 `Havenschap` — Verwijderd
- 🔴 `Landgoed` — Verwijderd
- 🔴 `Natuurorganisaties` — Verwijderd
- 🔴 `Netbeheerder` — Verwijderd
- 🔴 `Recreatieschap` — Verwijderd
- 🔴 `Rijksvastgoedbedrijf` — Verwijderd
- 🔴 `Rijkswaterstaat` — Verwijderd
- 🔴 `Speeltuinvereniging` — Verwijderd
- 🔴 `Stichting` — Verwijderd
- 🔴 `Universiteit` — Verwijderd
- 🔴 `Woningbouwcorporatie` — Verwijderd

##### `enum_TypeBeschermingsstatus` — 🔴 Verwijderd

**Literals:**

- 🔴 `Geen beschermingsstatus` — Verwijderd
- 🔴 `Monumentale boom` — Verwijderd
- 🔴 `Rust - en of verblijfplaats fauna` — Verwijderd

##### `enum_TypeBewerking` — 🔴 Verwijderd

**Literals:**

- 🔴 `Handmatig` — Verwijderd
- 🔴 `Machinaal` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `enum_TypeBouwdeel` — 🔴 Verwijderd

**Literals:**

- 🔴 `Nog geen domeinwaaren bekend` — Verwijderd

##### `enum_TypeBovenkantKademuur` — 🔴 Verwijderd

**Literals:**

- 🔴 `Dekzerk` — Verwijderd
- 🔴 `Rollaag` — Verwijderd

##### `enum_TypeCommunicatie` — 🔴 Verwijderd

**Literals:**

- 🔴 `ADSL` — Verwijderd
- 🔴 `GPRS` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `PSTN` — Verwijderd

##### `enum_TypeConstructie` — 🔴 Verwijderd

**Literals:**

- 🔴 `Gemiddelde constructie` — Verwijderd
- 🔴 `Lichte constructie` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Zware constructie` — Verwijderd

##### `enum_TypeDeurbediening` — 🔴 Verwijderd

**Literals:**

- 🔴 `Boot` — Verwijderd
- 🔴 `Elektro-mechanisch` — Verwijderd
- 🔴 `Geen` — Verwijderd
- 🔴 `Handlieren` — Verwijderd
- 🔴 `Handracht` — Verwijderd
- 🔴 `Houten kaapstanders` — Verwijderd
- 🔴 `Hydraulisch` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Stalen kaapstanders` — Verwijderd
- 🔴 `Tandheugel handbediend` — Verwijderd

##### `enum_TypeEigenaar` — 🔴 Verwijderd

**Literals:**

- 🔴 `Gemeente` — Verwijderd
- 🔴 `Ministerie van Defensie` — Verwijderd
- 🔴 `Ministerie van Economische Zaken` — Verwijderd
- 🔴 `Ministerie van Infrastructuur en Waterstaat` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Particulier` — Verwijderd
- 🔴 `Prorail` — Verwijderd
- 🔴 `Provincie` — Verwijderd
- 🔴 `Waterschap` — Verwijderd

##### `enum_TypeEigenaarPlus` — 🔴 Verwijderd

**Literals:**

- 🔴 `Havenschap` — Verwijderd
- 🔴 `Landgoed` — Verwijderd
- 🔴 `Natuurorganisatie` — Verwijderd
- 🔴 `Netbeheerder` — Verwijderd
- 🔴 `Recreatieschap` — Verwijderd
- 🔴 `Rijksvastgoedbedrijf` — Verwijderd
- 🔴 `Rijkswaterstaat` — Verwijderd
- 🔴 `Stichting` — Verwijderd
- 🔴 `Woningbouwcorporatie` — Verwijderd

##### `enum_TypeElement` — 🔴 Verwijderd

**Literals:**

- 🔴 `Nog geen domeinwaaren bekend` — Verwijderd

##### `enum_TypeFundering` — 🔴 Verwijderd

**Literals:**

- 🔴 `Cementgebonden` — Verwijderd
- 🔴 `Funderingspalen van hout` — Verwijderd
- 🔴 `Funderingspalen van prefab beton` — Verwijderd
- 🔴 `Funderingspalen van staal` — Verwijderd
- 🔴 `Funderingsplaat` — Verwijderd
- 🔴 `Gestort` — Verwijderd
- 🔴 `Hydraulisch gebonden` — Verwijderd
- 🔴 `NOC-NSF Classificatie` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Ongebonden` — Verwijderd
- 🔴 `Op staal` — Verwijderd
- 🔴 `Overig` — Verwijderd
- 🔴 `Poerenfundering` — Verwijderd
- 🔴 `Prefab` — Verwijderd

##### `enum_TypeLigging` — 🔴 Verwijderd

**Literals:**

- 🔴 `Binnen de bebouwde kom` — Verwijderd
- 🔴 `Binnen de bebouwde kom: centrum` — Verwijderd
- 🔴 `Buiten de bebouwde kom` — Verwijderd

##### `enum_TypeMantel` — 🔴 Verwijderd

**Literals:**

- 🔴 `Drainagekous` — Verwijderd
- 🔴 `Geen` — Verwijderd
- 🔴 `Kokok-1000` — Verwijderd
- 🔴 `Kokos` — Verwijderd
- 🔴 `Kokos-700` — Verwijderd
- 🔴 `Kunstgras` — Verwijderd
- 🔴 `Kunststofvezel` — Verwijderd
- 🔴 `PP450` — Verwijderd
- 🔴 `PP700` — Verwijderd
- 🔴 `PS1000` — Verwijderd

##### `enum_TypeMonument` — 🔴 Verwijderd

**Literals:**

- 🔴 `Beschermd stadsgezicht` — Verwijderd
- 🔴 `Geen` — Verwijderd
- 🔴 `Gemeentelijk monument` — Verwijderd
- 🔴 `Rijksmonument` — Verwijderd
- 🔴 `Werelderfgoed` — Verwijderd

##### `enum_TypeNivelleerschijf` — 🔴 Verwijderd

**Literals:**

- 🔴 `Geen` — Verwijderd
- 🔴 `Omloopriool` — Verwijderd
- 🔴 `Rinket` — Verwijderd

##### `enum_TypeOmgevingsrisicoklasse` — 🔴 Verwijderd

**Literals:**

- 🔴 `Geen` — Verwijderd
- 🔴 `Gemiddeld` — Verwijderd
- 🔴 `Hoog` — Verwijderd
- 🔴 `Laag` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `enum_TypeOnderdeelMetPomp` — 🔴 Verwijderd

**Literals:**

- 🔴 `Bijzondere putconstructieÂ` — Verwijderd
- 🔴 `Compartiment` — Verwijderd
- 🔴 `Gemaal` — Verwijderd
- 🔴 `Ledigingsvoorziening` — Verwijderd
- 🔴 `Pompput` — Verwijderd
- 🔴 `Spoelvoorziening` — Verwijderd

##### `enum_TypePlus` — 🔴 Verwijderd

**Literals:**

- 🔴 `Afgekruist vlak` — Verwijderd
- 🔴 `Akkerbouw` — Verwijderd
- 🔴 `Angle Box` — Verwijderd
- 🔴 `Archimedesspiraal` — Verwijderd
- 🔴 `Balance beam` — Verwijderd
- 🔴 `Balanceernet` — Verwijderd
- 🔴 `Balansvorm` — Verwijderd
- 🔴 `Ballenpaal` — Verwijderd
- 🔴 `Ballentrechter` — Verwijderd
- 🔴 `Bandenloop` — Verwijderd
- 🔴 `Basculebrug` — Verwijderd
- 🔴 `Basket en doel` — Verwijderd
- 🔴 `Basketbalterrein` — Verwijderd
- 🔴 `Beachvolleybalveld` — Verwijderd
- 🔴 `Bedrijfsaansluitleiding` — Verwijderd
- 🔴 `Beek` — Verwijderd
- 🔴 `Behendigheidsparcours` — Verwijderd
- 🔴 `Bench` — Verwijderd
- 🔴 `Bergbezinkleiding` — Verwijderd
- 🔴 `Bergingsleiding` — Verwijderd
- 🔴 `Betonelement` — Verwijderd
- 🔴 `Betonstraatstenen` — Verwijderd
- 🔴 `Big Wedge` — Verwijderd
- 🔴 `Bloemrijk gras` — Verwijderd
- 🔴 `Blokboom` — Verwijderd
- 🔴 `Blokhaag` — Verwijderd
- 🔴 `BochtstukÂ Â` — Verwijderd
- 🔴 `Bodembedekkende heesters` — Verwijderd
- 🔴 `Bodembedekkende rozen` — Verwijderd
- 🔴 `Bodembedekkende vaste planten` — Verwijderd
- 🔴 `Bodembedekkers` — Verwijderd
- 🔴 `Body Flexer` — Verwijderd
- 🔴 `Body Flexer - Upperbody Trainer` — Verwijderd
- 🔴 `Bokspringpaal` — Verwijderd
- 🔴 `Bolboom` — Verwijderd
- 🔴 `Bollenteelt` — Verwijderd
- 🔴 `Bomen en struikvormers` — Verwijderd
- 🔴 `Boogbrug` — Verwijderd
- 🔴 `Boomstam` — Verwijderd
- 🔴 `Boomvormers` — Verwijderd
- 🔴 `Bootcamp & Circuit Training` — Verwijderd
- 🔴 `Bootcamp Base` — Verwijderd
- 🔴 `Bootcamp Box en Gear` — Verwijderd
- 🔴 `Botanische rozen` — Verwijderd
- 🔴 `Boter-kaas-eieren` — Verwijderd
- 🔴 `Box Ramp` — Verwijderd
- 🔴 `Braakliggend` — Verwijderd
- 🔴 `Bron` — Verwijderd
- 🔴 `Brug` — Verwijderd
- 🔴 `Buik- en rugsteun` — Verwijderd
- 🔴 `Chest Press en Horizontal Row` — Verwijderd
- 🔴 `Chill schijf` — Verwijderd
- 🔴 `Chin up` — Verwijderd
- 🔴 `Circuit Training` — Verwijderd
- 🔴 `Cladding` — Verwijderd
- 🔴 `Combi` — Verwijderd
- 🔴 `Combi Step` — Verwijderd
- 🔴 `Combinatie - Kind` — Verwijderd
- 🔴 `Combinatie - Kleuter` — Verwijderd
- 🔴 `Combinatie - Peuter` — Verwijderd
- 🔴 `Combinatie van een smalle doorgetrokken en een smalle onderbroken streep` — Verwijderd
- 🔴 `Container` — Verwijderd
- 🔴 `Coping` — Verwijderd
- 🔴 `Core twist` — Verwijderd
- 🔴 `Corner Ramp` — Verwijderd
- 🔴 `Crank` — Verwijderd
- 🔴 `Cross & Circuit Training` — Verwijderd
- 🔴 `Cross Trainer` — Verwijderd
- 🔴 `Cross Training, Circuit Training, Bootcamp, Street Workout 256m_` — Verwijderd
- 🔴 `Cross Training, Street Workout 130m_` — Verwijderd
- 🔴 `Crosstrainer` — Verwijderd
- 🔴 `Cultuurrozen` — Verwijderd
- 🔴 `Curved Grind Rail` — Verwijderd
- 🔴 `Dakboom` — Verwijderd
- 🔴 `Decline Bench` — Verwijderd
- 🔴 `Dichte deklagen` — Verwijderd
- 🔴 `Dip - bar` — Verwijderd
- 🔴 `Dip Bench` — Verwijderd
- 🔴 `Discuskooi` — Verwijderd
- 🔴 `Doel P-model` — Verwijderd
- 🔴 `Doorgetrokken brede streep` — Verwijderd
- 🔴 `Doorgetrokken en dubbele smalle strepen` — Verwijderd
- 🔴 `Doorgetrokken smalle streep` — Verwijderd
- 🔴 `Double Chest Press` — Verwijderd
- 🔴 `Double Overhead Ladder` — Verwijderd
- 🔴 `Double Turbo Challenge` — Verwijderd
- 🔴 `Draadcircus` — Verwijderd
- 🔴 `Draaibrug` — Verwijderd
- 🔴 `Draaiende evenwichtsbalk` — Verwijderd
- 🔴 `Draaiende stoeltjes (type A)` — Verwijderd
- 🔴 `Draaihek` — Verwijderd
- 🔴 `Draaimolen` — Verwijderd
- 🔴 `Draaischijf (type E)` — Verwijderd
- 🔴 `Driekhoeksmarkering` — Verwijderd
- 🔴 `Drievoudig duikelrek` — Verwijderd
- 🔴 `Drievoudig duikelrek gebogen` — Verwijderd
- 🔴 `Drievoudig duikelrek zigzag` — Verwijderd
- 🔴 `Drijvende brug` — Verwijderd
- 🔴 `Droge heide` — Verwijderd
- 🔴 `Drukleiding` — Verwijderd
- 🔴 `Dubbele basculebrug` — Verwijderd
- 🔴 `Dubbele draaibrug` — Verwijderd
- 🔴 `Dubbele kabelbaan` — Verwijderd
- 🔴 `Dubbele ophaalbrug` — Verwijderd
- 🔴 `Dubbele platformkabelbaan` — Verwijderd
- 🔴 `Dubbele taludkabelbaan` — Verwijderd
- 🔴 `Dubbelstaafmathek` — Verwijderd
- 🔴 `Duikerbrug` — Verwijderd
- 🔴 `Duo ab - bench en ladder` — Verwijderd
- 🔴 `Duo pull up bar en ladder` — Verwijderd
- 🔴 `Enkel duikelrek` — Verwijderd
- 🔴 `Enkelstaafmathek` — Verwijderd
- 🔴 `Enkelvoudige kabelbaan` — Verwijderd
- 🔴 `Enkelvoudige platformkabelbaan` — Verwijderd
- 🔴 `Enkelvoudige taludkabelbaan` — Verwijderd
- 🔴 `Enterladder` — Verwijderd
- 🔴 `Enterrek` — Verwijderd
- 🔴 `Evenwichtsbalk` — Verwijderd
- 🔴 `Evenwichtsparcours` — Verwijderd
- 🔴 `Evenwichtsplateau op veren` — Verwijderd
- 🔴 `Externe overstortput` — Verwijderd
- 🔴 `Fietsparkeervak` — Verwijderd
- 🔴 `Fietssymbool` — Verwijderd
- 🔴 `Fijne sierheester` — Verwijderd
- 🔴 `Fitness Bike` — Verwijderd
- 🔴 `Fitnesstoestel` — Verwijderd
- 🔴 `Flat Bank` — Verwijderd
- 🔴 `Flat Bank with Platform` — Verwijderd
- 🔴 `Flat Ramp` — Verwijderd
- 🔴 `FlensverbindingÂ Â` — Verwijderd
- 🔴 `Flex Wheel` — Verwijderd
- 🔴 `Flex Wheel - Body Flexer` — Verwijderd
- 🔴 `Fly box` — Verwijderd
- 🔴 `Frame` — Verwijderd
- 🔴 `Frame & net` — Verwijderd
- 🔴 `Frame klimtoestel` — Verwijderd
- 🔴 `Free Runner` — Verwijderd
- 🔴 `Free Runner - Cross Trainer` — Verwijderd
- 🔴 `Free Runner - Cross Trainer - Power bike` — Verwijderd
- 🔴 `Fun box` — Verwijderd
- 🔴 `Gaybrapad` — Verwijderd
- 🔴 `Gazon` — Verwijderd
- 🔴 `Gebogen evenwichtsbalk` — Verwijderd
- 🔴 `Gecombineerde glijbaan - type 1` — Verwijderd
- 🔴 `Gecombineerde glijbaan - type 2` — Verwijderd
- 🔴 `Geknipte boom` — Verwijderd
- 🔴 `Gemengd riool` — Verwijderd
- 🔴 `Geschoren boom` — Verwijderd
- 🔴 `Gesloten duinvegetatie` — Verwijderd
- 🔴 `Getalmarkering` — Verwijderd
- 🔴 `Gewapend beton` — Verwijderd
- 🔴 `Gewone normale vaste brug` — Verwijderd
- 🔴 `Glas` — Verwijderd
- 🔴 `GlijverbindingÂ Â` — Verwijderd
- 🔴 `Goot` — Verwijderd
- 🔴 `Gracht` — Verwijderd
- 🔴 `Gras- en kruidachtigen` — Verwijderd
- 🔴 `Grasveld` — Verwijderd
- 🔴 `Griend en hakhout` — Verwijderd
- 🔴 `Grind Bench` — Verwijderd
- 🔴 `Grind Box` — Verwijderd
- 🔴 `Grind Rail` — Verwijderd
- 🔴 `Grondwaterpomp` — Verwijderd
- 🔴 `Grove sierheester` — Verwijderd
- 🔴 `Half Pipe` — Verwijderd
- 🔴 `Hand Bike` — Verwijderd
- 🔴 `Handrail Box` — Verwijderd
- 🔴 `Hang- en zweefmolens (type C)` — Verwijderd
- 🔴 `Hangbrug` — Verwijderd
- 🔴 `Hangelduo` — Verwijderd
- 🔴 `Hangtouwen` — Verwijderd
- 🔴 `Haven` — Verwijderd
- 🔴 `Heesterrozen` — Verwijderd
- 🔴 `Heesters` — Verwijderd
- 🔴 `Hefbrug` — Verwijderd
- 🔴 `Hellende enterladder` — Verwijderd
- 🔴 `Hellingklimmer` — Verwijderd
- 🔴 `Helmgras` — Verwijderd
- 🔴 `Hemelwaterriool` — Verwijderd
- 🔴 `Hexagon Pull Up Station` — Verwijderd
- 🔴 `High rotator` — Verwijderd
- 🔴 `Hink-stapspringbak` — Verwijderd
- 🔴 `Hinkelbaan` — Verwijderd
- 🔴 `Hobbelbrug` — Verwijderd
- 🔴 `Hockeydoel` — Verwijderd
- 🔴 `Hoogspringbak` — Verwijderd
- 🔴 `Hoogstam` — Verwijderd
- 🔴 `Hoogstam boomgaarden` — Verwijderd
- 🔴 `Horden` — Verwijderd
- 🔴 `Hout` — Verwijderd
- 🔴 `Hurdles` — Verwijderd
- 🔴 `Incline Press` — Verwijderd
- 🔴 `Infiltratiegreppel` — Verwijderd
- 🔴 `Infiltratieriool` — Verwijderd
- 🔴 `Ingemetselde nestkast` — Verwijderd
- 🔴 `Instructiebord` — Verwijderd
- 🔴 `Interne overstortput` — Verwijderd
- 🔴 `JOP` — Verwijderd
- 🔴 `Jongerenbank` — Verwijderd
- 🔴 `Jump Box` — Verwijderd
- 🔴 `Jump Ramp` — Verwijderd
- 🔴 `Jump pod` — Verwijderd
- 🔴 `Jurytrap` — Verwijderd
- 🔴 `Kanaal` — Verwijderd
- 🔴 `Kindertafel` — Verwijderd
- 🔴 `Klapbrug` — Verwijderd
- 🔴 `Klaphek` — Verwijderd
- 🔴 `Klassieke draaimolen met meedraaiende vloer (type B)` — Verwijderd
- 🔴 `Klauterparcours` — Verwijderd
- 🔴 `Klein fruit` — Verwijderd
- 🔴 `Kliedertafel` — Verwijderd
- 🔴 `Klimgordijn` — Verwijderd
- 🔴 `Klimladder` — Verwijderd
- 🔴 `Klimmuur/ladder combi` — Verwijderd
- 🔴 `Klimnet met duikelrekken` — Verwijderd
- 🔴 `Klimpaal` — Verwijderd
- 🔴 `Klimrek` — Verwijderd
- 🔴 `Klimschans` — Verwijderd
- 🔴 `Klimwand` — Verwijderd
- 🔴 `Kogelslingerkooi` — Verwijderd
- 🔴 `Kogelstotenbak` — Verwijderd
- 🔴 `Kolkaansluitleiding` — Verwijderd
- 🔴 `Kooi` — Verwijderd
- 🔴 `Kruipbuis` — Verwijderd
- 🔴 `Kunstgras` — Verwijderd
- 🔴 `Kunstmatige oeverzwaluwwand` — Verwijderd
- 🔴 `Kunststof vloer` — Verwijderd
- 🔴 `Laagstam` — Verwijderd
- 🔴 `Laagstam boomgaarden` — Verwijderd
- 🔴 `Ladder` — Verwijderd
- 🔴 `LasverbindingÂ Â` — Verwijderd
- 🔴 `Leunhek` — Verwijderd
- 🔴 `Liggerbrug` — Verwijderd
- 🔴 `LijmverbindingÂ Â` — Verwijderd
- 🔴 `Lijnvormige haag` — Verwijderd
- 🔴 `Lo-Box` — Verwijderd
- 🔴 `Log hop` — Verwijderd
- 🔴 `Loopbrug` — Verwijderd
- 🔴 `Loopton` — Verwijderd
- 🔴 `Looptouw` — Verwijderd
- 🔴 `Loopvlonder` — Verwijderd
- 🔴 `Los` — Verwijderd
- 🔴 `Magnetic bells` — Verwijderd
- 🔴 `Magnetic bells, suspension trainer en multi net link` — Verwijderd
- 🔴 `Meer` — Verwijderd
- 🔴 `Meerdelig duikelrek` — Verwijderd
- 🔴 `Metaal` — Verwijderd
- 🔴 `Midi Ramp` — Verwijderd
- 🔴 `Mini Box` — Verwijderd
- 🔴 `Mini Ramp` — Verwijderd
- 🔴 `Minidoel` — Verwijderd
- 🔴 `Mobile bar` — Verwijderd
- 🔴 `Moerasvegetatie` — Verwijderd
- 🔴 `Molens op spoor met voet of hand aangedreven (type D)` — Verwijderd
- 🔴 `Monkey bar` — Verwijderd
- 🔴 `Monkey bar extended` — Verwijderd
- 🔴 `Multi net` — Verwijderd
- 🔴 `Natte heide` — Verwijderd
- 🔴 `Natuurlijke grasvegetatie` — Verwijderd
- 🔴 `Natuurlijke oeverzwaluwwand` — Verwijderd
- 🔴 `Natuursteen` — Verwijderd
- 🔴 `Nestkast Eekhoorn` — Verwijderd
- 🔴 `Nestkast Marter` — Verwijderd
- 🔴 `Nestkast bonte vliegenvanger` — Verwijderd
- 🔴 `Nestkast boomklever` — Verwijderd
- 🔴 `Nestkast boomkruiper` — Verwijderd
- 🔴 `Nestkast bosuil` — Verwijderd
- 🔴 `Nestkast gierzwaluw` — Verwijderd
- 🔴 `Nestkast grote bonte specht` — Verwijderd
- 🔴 `Nestkast huismus` — Verwijderd
- 🔴 `Nestkast koolmees` — Verwijderd
- 🔴 `Nestkast pimpelmees` — Verwijderd
- 🔴 `Nestkast roodborst` — Verwijderd
- 🔴 `Nestkast spreeuw` — Verwijderd
- 🔴 `Nestkast steenuil` — Verwijderd
- 🔴 `Nestkast torenvalk` — Verwijderd
- 🔴 `Nestkast winterkoning` — Verwijderd
- 🔴 `Nestkast zwarte roodstaart` — Verwijderd
- 🔴 `Neststeen voor gierzwaluw` — Verwijderd
- 🔴 `Net` — Verwijderd
- 🔴 `Netbrug oversteek` — Verwijderd
- 🔴 `Ollie Hurdle` — Verwijderd
- 🔴 `Ollie Jump` — Verwijderd
- 🔴 `Onderbroken brede streep` — Verwijderd
- 🔴 `Onderbroken smalle streep` — Verwijderd
- 🔴 `Ongewapend nietverdeuveld beton` — Verwijderd
- 🔴 `Ongewapend verdeuveld beton` — Verwijderd
- 🔴 `Opdrukken` — Verwijderd
- 🔴 `Open duinvegetatie` — Verwijderd
- 🔴 `Open grond` — Verwijderd
- 🔴 `Ophaalbrug` — Verwijderd
- 🔴 `Oppervlakbehandelingen` — Verwijderd
- 🔴 `Optrekken` — Verwijderd
- 🔴 `Over Under` — Verwijderd
- 🔴 `OvergangsstukÂ Â` — Verwijderd
- 🔴 `Overhead Ladder` — Verwijderd
- 🔴 `Overige markering` — Verwijderd
- 🔴 `Overstortleiding` — Verwijderd
- 🔴 `Palenwoud` — Verwijderd
- 🔴 `Panel` — Verwijderd
- 🔴 `Pannaveld` — Verwijderd
- 🔴 `Pants Driveway` — Verwijderd
- 🔴 `Parallel bar` — Verwijderd
- 🔴 `Parallel bars` — Verwijderd
- 🔴 `Parkeerplaats` — Verwijderd
- 🔴 `Parkeervak` — Verwijderd
- 🔴 `Pendelwaag` — Verwijderd
- 🔴 `Perceelaansluitleiding` — Verwijderd
- 🔴 `Persleiding` — Verwijderd
- 🔴 `Pijlmarkering` — Verwijderd
- 🔴 `Piramidevorm` — Verwijderd
- 🔴 `Pirouette` — Verwijderd
- 🔴 `Plaatbrug` — Verwijderd
- 🔴 `Planten` — Verwijderd
- 🔴 `Planter for Steps` — Verwijderd
- 🔴 `Plas` — Verwijderd
- 🔴 `Plasberm` — Verwijderd
- 🔴 `Platform` — Verwijderd
- 🔴 `Pleinplakker` — Verwijderd
- 🔴 `Poel` — Verwijderd
- 🔴 `Polsstokhoogspringbak` — Verwijderd
- 🔴 `Pompunit` — Verwijderd
- 🔴 `Pontje` — Verwijderd
- 🔴 `Power Bike` — Verwijderd
- 🔴 `Praatpaal` — Verwijderd
- 🔴 `Pull up Station` — Verwijderd
- 🔴 `Pull up bars` — Verwijderd
- 🔴 `Pull up bars, parallel bars & multi net link` — Verwijderd
- 🔴 `Puntstukken en witte vlakken` — Verwijderd
- 🔴 `Push up bars` — Verwijderd
- 🔴 `Push up bars met paal` — Verwijderd
- 🔴 `Puzzelbord` — Verwijderd
- 🔴 `Pyramid` — Verwijderd
- 🔴 `Quad Box` — Verwijderd
- 🔴 `Quarterpipe` — Verwijderd
- 🔴 `Ramp` — Verwijderd
- 🔴 `Rear Panel` — Verwijderd
- 🔴 `Rek- en strekbrug` — Verwijderd
- 🔴 `Rietvegetatie` — Verwijderd
- 🔴 `Ringenrek met balanceertouw` — Verwijderd
- 🔴 `Rioolstreng` — Verwijderd
- 🔴 `Rivier` — Verwijderd
- 🔴 `Rodeo stier` — Verwijderd
- 🔴 `Rolbrug` — Verwijderd
- 🔴 `Roll-In Ramp` — Verwijderd
- 🔴 `Roll-off Ramp` — Verwijderd
- 🔴 `RolverbindingÂ Â` — Verwijderd
- 🔴 `Rondobollen` — Verwijderd
- 🔴 `Ruig gras` — Verwijderd
- 🔴 `Ruigte` — Verwijderd
- 🔴 `Ruimtenet` — Verwijderd
- 🔴 `Ruw gras` — Verwijderd
- 🔴 `Samenhangend` — Verwijderd
- 🔴 `Schraalgrasland` — Verwijderd
- 🔴 `Schudzeef` — Verwijderd
- 🔴 `Schuifhek` — Verwijderd
- 🔴 `Shaped Grind Rail` — Verwijderd
- 🔴 `Side Panel` — Verwijderd
- 🔴 `Sierbestrating` — Verwijderd
- 🔴 `Sit up bench` — Verwijderd
- 🔴 `Sit up bench - Power Bike` — Verwijderd
- 🔴 `Slinger-klim-entercombi` — Verwijderd
- 🔴 `Sloot` — Verwijderd
- 🔴 `Small Wedge` — Verwijderd
- 🔴 `Speelauto` — Verwijderd
- 🔴 `Speelboot` — Verwijderd
- 🔴 `Speelhuis` — Verwijderd
- 🔴 `Speelpaneel` — Verwijderd
- 🔴 `Speelplatform` — Verwijderd
- 🔴 `Speelschip` — Verwijderd
- 🔴 `Speelspoor` — Verwijderd
- 🔴 `Speelstoel en tafel` — Verwijderd
- 🔴 `Speeltafel` — Verwijderd
- 🔴 `Speeltrein` — Verwijderd
- 🔴 `Spine` — Verwijderd
- 🔴 `Split Quarter Pipe` — Verwijderd
- 🔴 `Spoelleiding` — Verwijderd
- 🔴 `Springkussen` — Verwijderd
- 🔴 `Springplank` — Verwijderd
- 🔴 `Square Pull Up Station` — Verwijderd
- 🔴 `Squat en Shoulder Press en Lat Pull Down` — Verwijderd
- 🔴 `Stammenstapel` — Verwijderd
- 🔴 `Stammentrap` — Verwijderd
- 🔴 `Stappalen` — Verwijderd
- 🔴 `Stapstenen` — Verwijderd
- 🔴 `Start Box` — Verwijderd
- 🔴 `Steeple-chase waterbak` — Verwijderd
- 🔴 `Step` — Verwijderd
- 🔴 `Step block` — Verwijderd
- 🔴 `Step en Swing` — Verwijderd
- 🔴 `Steps` — Verwijderd
- 🔴 `Ster klim-duikelrek combinatie` — Verwijderd
- 🔴 `Steunbrug` — Verwijderd
- 🔴 `Steunsprong` — Verwijderd
- 🔴 `Straatbaksteen` — Verwijderd
- 🔴 `Strand en strandwal` — Verwijderd
- 🔴 `Street Spine` — Verwijderd
- 🔴 `Street Workout, Parkour` — Verwijderd
- 🔴 `Stretch Bar` — Verwijderd
- 🔴 `Strip` — Verwijderd
- 🔴 `Struikvormers` — Verwijderd
- 🔴 `Stuwrioolleiding` — Verwijderd
- 🔴 `Supernova` — Verwijderd
- 🔴 `Suspension Trainer, Parallel Bars & Magnetic Bells Link` — Verwijderd
- 🔴 `Suspension trainer` — Verwijderd
- 🔴 `T-stuk` — Verwijderd
- 🔴 `Tafeltennistafel rond` — Verwijderd
- 🔴 `Tafeltennistafel vierkant` — Verwijderd
- 🔴 `Tafelvoetbaltafel` — Verwijderd
- 🔴 `Take Off Ramp` — Verwijderd
- 🔴 `Talud verkeersdrempel` — Verwijderd
- 🔴 `Taludglijbaan - type 1` — Verwijderd
- 🔴 `Taludglijbaan - type 2` — Verwijderd
- 🔴 `Tegels` — Verwijderd
- 🔴 `Telefoonpaal` — Verwijderd
- 🔴 `Thematisch evenwichtsplateau op veren` — Verwijderd
- 🔴 `Thematische basketbalpaal` — Verwijderd
- 🔴 `Toroveld` — Verwijderd
- 🔴 `Touw tornado` — Verwijderd
- 🔴 `Touwbalans` — Verwijderd
- 🔴 `Touwbrug` — Verwijderd
- 🔴 `Touwduikelrek` — Verwijderd
- 🔴 `Tractorband` — Verwijderd
- 🔴 `Trainingsdoeltje` — Verwijderd
- 🔴 `Trampoline` — Verwijderd
- 🔴 `Transportrioolleiding` — Verwijderd
- 🔴 `Trapoefenwand` — Verwijderd
- 🔴 `Trapschot` — Verwijderd
- 🔴 `Trekvaste koppeling` — Verwijderd
- 🔴 `Triple Bars` — Verwijderd
- 🔴 `Triple Ramp Grinder` — Verwijderd
- 🔴 `Tuibrug` — Verwijderd
- 🔴 `Tuinachtige grond` — Verwijderd
- 🔴 `Tuinbouwgrond` — Verwijderd
- 🔴 `Turnbrug` — Verwijderd
- 🔴 `Turnparcours` — Verwijderd
- 🔴 `Twist en Step` — Verwijderd
- 🔴 `Twist en Swing` — Verwijderd
- 🔴 `Twist en Wobble` — Verwijderd
- 🔴 `Type 1 - Rotatie om 1 as` — Verwijderd
- 🔴 `Type 1 - Wip - 1 richting` — Verwijderd
- 🔴 `Type 2 - Rotatie op meerdere assen` — Verwijderd
- 🔴 `Type 2A - Enkelpunts - 1 richting` — Verwijderd
- 🔴 `Type 2B - Enkelpunts - Meerdere richtingen` — Verwijderd
- 🔴 `Type 3 - Rotatie om 1 punt` — Verwijderd
- 🔴 `Type 3A - Meerpunts - 1 richting` — Verwijderd
- 🔴 `Type 3B - Meerpunts - Meerdere richtingen` — Verwijderd
- 🔴 `Type 4 - Contactschommel` — Verwijderd
- 🔴 `Type 4 - Meer assen - 1 richting` — Verwijderd
- 🔴 `Type 5 - Zweefwip` — Verwijderd
- 🔴 `Type 6 - Schommelwip met enkelvoudige hoge as` — Verwijderd
- 🔴 `Upperbody Trainer` — Verwijderd
- 🔴 `Upperbody Trainer - Free Runner - Body Flexer` — Verwijderd
- 🔴 `Upright Row en Press Down` — Verwijderd
- 🔴 `VacuÃ¼mleiding` — Verwijderd
- 🔴 `VacuÃ¼mpompstation` — Verwijderd
- 🔴 `Vakwerkbrug` — Verwijderd
- 🔴 `Valdempend gras` — Verwijderd
- 🔴 `Vast` — Verwijderd
- 🔴 `Vaste planten` — Verwijderd
- 🔴 `Ven` — Verwijderd
- 🔴 `Verbeterde overstortput` — Verwijderd
- 🔴 `Verdrijfstrepen` — Verwijderd
- 🔴 `Verkeersbord` — Verwijderd
- 🔴 `Verkeersdruppel` — Verwijderd
- 🔴 `Verloopstuk` — Verwijderd
- 🔴 `Verplaatsbaar` — Verwijderd
- 🔴 `Verspring- en hinkstapspringbak` — Verwijderd
- 🔴 `Verspringbak` — Verwijderd
- 🔴 `Verstopschotten` — Verwijderd
- 🔴 `Vertikale ladder` — Verwijderd
- 🔴 `Vijver` — Verwijderd
- 🔴 `Vleermuiskast gewone dwergvleermuis` — Verwijderd
- 🔴 `Vleermuiskast rosse vleermuis` — Verwijderd
- 🔴 `Vlot` — Verwijderd
- 🔴 `Voetbaldoel` — Verwijderd
- 🔴 `Voetbaldoelnet` — Verwijderd
- 🔴 `Voethek` — Verwijderd
- 🔴 `Vogelvide` — Verwijderd
- 🔴 `Volcano` — Verwijderd
- 🔴 `Vollegrondsteelt` — Verwijderd
- 🔴 `Volleybalveld` — Verwijderd
- 🔴 `Voorwaarschuwingsdriehoek` — Verwijderd
- 🔴 `Vormhaag` — Verwijderd
- 🔴 `Vouwhek` — Verwijderd
- 🔴 `Vrijstaande glijbaan - type 1` — Verwijderd
- 🔴 `Vrijstaande glijbaan - type 2` — Verwijderd
- 🔴 `Vuilwaterriool` — Verwijderd
- 🔴 `Wall Ride` — Verwijderd
- 🔴 `Wall with Net` — Verwijderd
- 🔴 `Wateremmer` — Verwijderd
- 🔴 `Waterglijbaan` — Verwijderd
- 🔴 `Waterpomp` — Verwijderd
- 🔴 `Waterrad` — Verwijderd
- 🔴 `Watertappunt` — Verwijderd
- 🔴 `Waterwip` — Verwijderd
- 🔴 `Weide` — Verwijderd
- 🔴 `Wiebelbrug` — Verwijderd
- 🔴 `Wiebelloop` — Verwijderd
- 🔴 `Wiebelplaat` — Verwijderd
- 🔴 `Wijngaarden` — Verwijderd
- 🔴 `Wisselperken` — Verwijderd
- 🔴 `Wobble en Step` — Verwijderd
- 🔴 `Wobble en Swing` — Verwijderd
- 🔴 `Wobble en Swing en Step en Twist` — Verwijderd
- 🔴 `Woordmarkering` — Verwijderd
- 🔴 `Workout combination` — Verwijderd
- 🔴 `Y-stuk` — Verwijderd
- 🔴 `Zand` — Verwijderd
- 🔴 `Zandbak` — Verwijderd
- 🔴 `Zandgraver` — Verwijderd
- 🔴 `Zandkraan` — Verwijderd
- 🔴 `Zandspeelhuis` — Verwijderd
- 🔴 `Zandspeeltafel` — Verwijderd
- 🔴 `Zandstransportband` — Verwijderd
- 🔴 `Zandtransporttoestel` — Verwijderd
- 🔴 `Zandverstuiving` — Verwijderd
- 🔴 `Zee` — Verwijderd
- 🔴 `Zesvoudig duikelrek` — Verwijderd
- 🔴 `Zigzag-markering` — Verwijderd
- 🔴 `Zinker` — Verwijderd
- 🔴 `ZinloosGeweldMarkering` — Verwijderd
- 🔴 `Zitpaal` — Verwijderd
- 🔴 `Zoab en open deklagen` — Verwijderd
- 🔴 `Zonemarkering` — Verwijderd
- 🔴 `Zwarte grond` — Verwijderd
- 🔴 `Zwevende evenwichtsbalk` — Verwijderd

##### `enum_TypeSlot` — 🔴 Verwijderd

**Literals:**

- 🔴 `Nog geen domeinwaaren bekend` — Verwijderd

##### `enum_TypeStandplaats` — 🔴 Verwijderd

**Literals:**

- 🔴 `Asfaltverharding` — Verwijderd
- 🔴 `Betonverharding` — Verwijderd
- 🔴 `Bodembedekkers` — Verwijderd
- 🔴 `Bosplantsoen` — Verwijderd
- 🔴 `Drijvende constructie` — Verwijderd
- 🔴 `Elementenverharding` — Verwijderd
- 🔴 `Gras- en kruidachtigen` — Verwijderd
- 🔴 `Haag` — Verwijderd
- 🔴 `Halfverharding` — Verwijderd
- 🔴 `Heesters` — Verwijderd
- 🔴 `Kunststofverharding` — Verwijderd
- 🔴 `Niet te beoordelen` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Onverhard` — Verwijderd
- 🔴 `Planten` — Verwijderd
- 🔴 `Plantenbak` — Verwijderd
- 🔴 `Struikrozen` — Verwijderd
- 🔴 `Terreindeel` — Verwijderd
- 🔴 `Verhardingsobject` — Verwijderd

##### `enum_TypeStandplaatsPlus` — 🔴 Verwijderd

**Literals:**

- 🔴 `Betonelement` — Verwijderd
- 🔴 `Betonstraatstenen` — Verwijderd
- 🔴 `Bloemrijk gras` — Verwijderd
- 🔴 `Blokhaag` — Verwijderd
- 🔴 `Bodembedekkende heesters` — Verwijderd
- 🔴 `Bodembedekkende rozen` — Verwijderd
- 🔴 `Bodembedekkende vaste planten` — Verwijderd
- 🔴 `Bomen en struikvormers` — Verwijderd
- 🔴 `Boomteelt` — Verwijderd
- 🔴 `Boomvormers` — Verwijderd
- 🔴 `Botanische rozen` — Verwijderd
- 🔴 `Bouwland` — Verwijderd
- 🔴 `Cultuurrozen` — Verwijderd
- 🔴 `Dichte deklagen` — Verwijderd
- 🔴 `Duin` — Verwijderd
- 🔴 `Fijne sierheester` — Verwijderd
- 🔴 `Fruitteelt` — Verwijderd
- 🔴 `Gazon` — Verwijderd
- 🔴 `Gemengd bos` — Verwijderd
- 🔴 `Gewapend beton` — Verwijderd
- 🔴 `Glas` — Verwijderd
- 🔴 `Graft` — Verwijderd
- 🔴 `Grasland agrarisch` — Verwijderd
- 🔴 `Grasland overig` — Verwijderd
- 🔴 `Grove sierheester` — Verwijderd
- 🔴 `Heesterrozen` — Verwijderd
- 🔴 `Heide` — Verwijderd
- 🔴 `Hout` — Verwijderd
- 🔴 `Houtwal` — Verwijderd
- 🔴 `Kunstgras` — Verwijderd
- 🔴 `Kunststof vloer` — Verwijderd
- 🔴 `Lijnvormige haag` — Verwijderd
- 🔴 `Loofbos` — Verwijderd
- 🔴 `Los` — Verwijderd
- 🔴 `Metaal` — Verwijderd
- 🔴 `Naaldbos` — Verwijderd
- 🔴 `Natuursteen` — Verwijderd
- 🔴 `Ongewapend nietverdeuveld beton` — Verwijderd
- 🔴 `Ongewapend verdeuveld beton` — Verwijderd
- 🔴 `Open grond` — Verwijderd
- 🔴 `Oppervlakbehandelingen` — Verwijderd
- 🔴 `Recreatief grasveld` — Verwijderd
- 🔴 `Ruigte` — Verwijderd
- 🔴 `Ruw gras` — Verwijderd
- 🔴 `Samenhangend` — Verwijderd
- 🔴 `Sierbestrating` — Verwijderd
- 🔴 `Steilwand` — Verwijderd
- 🔴 `Straatbaksteen` — Verwijderd
- 🔴 `Struiken` — Verwijderd
- 🔴 `Struikvormers` — Verwijderd
- 🔴 `Tegels` — Verwijderd
- 🔴 `Vaste planten` — Verwijderd
- 🔴 `Vormhaag` — Verwijderd
- 🔴 `Wisselperken` — Verwijderd
- 🔴 `Zand` — Verwijderd
- 🔴 `Zoab en open deklagen` — Verwijderd
- 🔴 `Zwarte grond` — Verwijderd

##### `enum_TypeTeerhoudend` — 🔴 Verwijderd

**Literals:**

- 🔴 `Onbekend` — Verwijderd
- 🔴 `Teerhoudend` — Verwijderd
- 🔴 `Teerverdacht` — Verwijderd
- 🔴 `Teervrij` — Verwijderd

##### `enum_TypeVaarwater` — 🔴 Verwijderd

**Literals:**

- 🔴 `Onbekend` — Verwijderd
- 🔴 `Primair` — Verwijderd
- 🔴 `Secundair` — Verwijderd
- 🔴 `Tertiair` — Verwijderd

##### `enum_TypeVermeerderingsvorm` — 🔴 Verwijderd

**Literals:**

- 🔴 `Eigen wortel` — Verwijderd
- 🔴 `Gezaaid` — Verwijderd
- 🔴 `GeÃ«nt` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Veredeld` — Verwijderd

##### `enum_TypeVoeg` — 🔴 Verwijderd

**Literals:**

- 🔴 `Constructievoeg` — Verwijderd
- 🔴 `Krimpvoeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Overgangsvoeg` — Verwijderd
- 🔴 `Uitzetvoeg` — Verwijderd

##### `enum_TypeVoegvulling` — 🔴 Verwijderd

**Literals:**

- 🔴 `Flexibel gebonden` — Verwijderd
- 🔴 `Gebonden` — Verwijderd
- 🔴 `Lichtgebonden` — Verwijderd
- 🔴 `Ongebonden` — Verwijderd

##### `enum_TypeWaaier` — 🔴 Verwijderd

**Literals:**

- 🔴 `Organisatiespecifieke domeinwaarden` — Verwijderd

##### `enum_TypeWaterplant` — 🔴 Verwijderd

**Literals:**

- 🔴 `Waterplant drijvend` — Verwijderd
- 🔴 `Waterplant ondergedoken` — Verwijderd

##### `enum_Vegen` — 🔴 Verwijderd

**Literals:**

- 🔴 `Niet vegen` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Vegen` — Verwijderd

##### `enum_Verbindingstype` — 🔴 Verwijderd

**Literals:**

- 🔴 `Anders` — Verwijderd
- 🔴 `Dubbele steekmof` — Verwijderd
- 🔴 `Las` — Verwijderd
- 🔴 `Mof/Spie` — Verwijderd
- 🔴 `Vaar/moer` — Verwijderd

##### `enum_VerhardingsobjectWegfunctie` — 🔴 Verwijderd

**Literals:**

- 🔴 `Achterpad` — Verwijderd
- 🔴 `BaanVoorVliegverkeer` — Verwijderd
- 🔴 `Busbaan` — Verwijderd
- 🔴 `Busperron` — Verwijderd
- 🔴 `Bussluis` — Verwijderd
- 🔴 `Busstrook` — Verwijderd
- 🔴 `Dynamische busbaan` — Verwijderd
- 🔴 `Fietspad` — Verwijderd
- 🔴 `Gehandicaptenparkeerplaats` — Verwijderd
- 🔴 `Halte eiland` — Verwijderd
- 🔴 `Halte voetpad` — Verwijderd
- 🔴 `Haltekom` — Verwijderd
- 🔴 `Haltekom OV` — Verwijderd
- 🔴 `Haltekom informatiehalte` — Verwijderd
- 🔴 `Inrit` — Verwijderd
- 🔴 `Kraanbaan` — Verwijderd
- 🔴 `Loswal` — Verwijderd
- 🔴 `Metrobaan` — Verwijderd
- 🔴 `OV-baan` — Verwijderd
- 🔴 `Onverplicht fietspad` — Verwijderd
- 🔴 `Overweg` — Verwijderd
- 🔴 `Parallelweg` — Verwijderd
- 🔴 `Parkeerstrook` — Verwijderd
- 🔴 `Parkeerterrein` — Verwijderd
- 🔴 `Parkeervak` — Verwijderd
- 🔴 `Parkeervak fietsen` — Verwijderd
- 🔴 `Parkeervak scooters` — Verwijderd
- 🔴 `Parkeervoorziening` — Verwijderd
- 🔴 `Parkeren op rijbaan` — Verwijderd
- 🔴 `Parkeren op rijbaan: langsparkeren op rijbaan` — Verwijderd
- 🔴 `Recreatief voetpad` — Verwijderd
- 🔴 `Rijbaan` — Verwijderd
- 🔴 `Ruiterpad` — Verwijderd
- 🔴 `Schouwpad` — Verwijderd
- 🔴 `Spoorbaan` — Verwijderd
- 🔴 `Trambaan` — Verwijderd
- 🔴 `Tramheuvel` — Verwijderd
- 🔴 `Utilitair fietspad` — Verwijderd
- 🔴 `Utilitair voetpad` — Verwijderd
- 🔴 `Verbindingsweg` — Verwijderd
- 🔴 `Verbindingsweg - afrit` — Verwijderd
- 🔴 `Verbindingsweg - toerit` — Verwijderd
- 🔴 `Verkeersdrempel` — Verwijderd
- 🔴 `Verplicht fiets-/bromfietspad` — Verwijderd
- 🔴 `Verplicht fietspad` — Verwijderd
- 🔴 `Voetgangersgebied` — Verwijderd
- 🔴 `Voetpad` — Verwijderd
- 🔴 `Voetpad op trap` — Verwijderd
- 🔴 `Winkelerf` — Verwijderd
- 🔴 `Woonerf` — Verwijderd
- 🔴 `Woonerfparkeervak` — Verwijderd
- 🔴 `Woonstraat` — Verwijderd

##### `enum_Vorm` — 🔴 Verwijderd

**Literals:**

- 🔴 `Driehoek` — Verwijderd
- 🔴 `Eivormig` — Verwijderd
- 🔴 `Heul` — Verwijderd
- 🔴 `Muil` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Ovaal` — Verwijderd
- 🔴 `Rechthoekig` — Verwijderd
- 🔴 `Rond` — Verwijderd
- 🔴 `Trapezium` — Verwijderd
- 🔴 `U-vorm` — Verwijderd
- 🔴 `Vierkant` — Verwijderd

##### `enum_VrijeDoorrijhoogte` — 🔴 Verwijderd

**Literals:**

- 🔴 `0 m.` — Verwijderd
- 🔴 `2,5 m. en groter` — Verwijderd
- 🔴 `4,5 m. en groter` — Verwijderd
- 🔴 `6,5 m. en groter` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `enum_VrijeTakval` — 🔴 Verwijderd

**Literals:**

- 🔴 `Geen vrije takval mogelijk` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Vrije takval mogelijk` — Verwijderd

##### `enum_VulmateriaalKunstgras` — 🔴 Verwijderd

**Literals:**

- 🔴 `Gecoat rubber` — Verwijderd
- 🔴 `Geen vulmateriaal` — Verwijderd
- 🔴 `Kurk` — Verwijderd
- 🔴 `Overig` — Verwijderd
- 🔴 `Rood zand (Provision)` — Verwijderd
- 🔴 `Rood zand (Smashcourt)` — Verwijderd
- 🔴 `Rood zand (overig)` — Verwijderd
- 🔴 `Rubber` — Verwijderd
- 🔴 `TPE` — Verwijderd
- 🔴 `Zand` — Verwijderd

##### `enum_Waterdoorlatendheid` — 🔴 Verwijderd

**Literals:**

- 🔴 `Geen` — Verwijderd
- 🔴 `Waterdoorlatende verharding` — Verwijderd
- 🔴 `Waterpasserende verharding` — Verwijderd

##### `enum_WegasTypeRoute` — 🔴 Verwijderd

**Literals:**

- 🔴 `Bevoorradingsroute` — Verwijderd
- 🔴 `Distributieroute` — Verwijderd
- 🔴 `Doorgaande route` — Verwijderd
- 🔴 `Europese route (E-route)` — Verwijderd
- 🔴 `Fietsroute` — Verwijderd
- 🔴 `Fietsroute: hoofdfietsroute` — Verwijderd
- 🔴 `Fietsroute: subroute` — Verwijderd
- 🔴 `Huisvuilophaalroute` — Verwijderd
- 🔴 `OV-route` — Verwijderd
- 🔴 `OV-route: hoofdroute (regionaal)` — Verwijderd
- 🔴 `OV-route: subroute (stad)` — Verwijderd
- 🔴 `Omleidingsroute (incidenteel)` — Verwijderd
- 🔴 `Ontsluitingsroute` — Verwijderd
- 🔴 `Permanente omleidingsroute (U-route)` — Verwijderd
- 🔴 `Route LZV vrachtverkeer` — Verwijderd
- 🔴 `Route exceptioneel vrachtverkeer` — Verwijderd
- 🔴 `Route gevaarlijke stoffen` — Verwijderd
- 🔴 `Route hulpdienst ambulance` — Verwijderd
- 🔴 `Route hulpdienst ambulance: hoofdroute` — Verwijderd
- 🔴 `Route hulpdienst ambulance: subroute` — Verwijderd
- 🔴 `Route hulpdienst brandweer` — Verwijderd
- 🔴 `Route hulpdienst brandweer: hoofdroute` — Verwijderd
- 🔴 `Route hulpdienst brandweer: subroute` — Verwijderd
- 🔴 `Route hulpdienst incident management` — Verwijderd
- 🔴 `Route landbouwverkeer` — Verwijderd
- 🔴 `Route landbouwverkeer: hoofdroute` — Verwijderd
- 🔴 `Route landbouwverkeer: subroute` — Verwijderd
- 🔴 `Route vrachtverkeer` — Verwijderd
- 🔴 `Route vrachtverkeer: hoofdroute` — Verwijderd
- 🔴 `Route vrachtverkeer: subroute` — Verwijderd
- 🔴 `Schoolroute` — Verwijderd
- 🔴 `Stadsroute` — Verwijderd
- 🔴 `Strooiroute (gladheidsbestrijding)` — Verwijderd
- 🔴 `Strooiroute: geen gladheidsbestrijding` — Verwijderd
- 🔴 `Strooiroute: prioriteit 1` — Verwijderd
- 🔴 `Strooiroute: prioriteit 2` — Verwijderd
- 🔴 `Wandelroute` — Verwijderd

##### `enum_WegcategorieDV` — 🔴 Verwijderd

**Literals:**

- 🔴 `Erftoegangsweg` — Verwijderd
- 🔴 `Gebiedsontsluitingsweg` — Verwijderd
- 🔴 `Nationale stroomweg` — Verwijderd
- 🔴 `Regionale stroomweg` — Verwijderd

##### `enum_WegtypeBestaand` — 🔴 Verwijderd

**Literals:**

- 🔴 `1 - Hoofdwegennet` — Verwijderd
- 🔴 `2 - Zwaar belaste weg` — Verwijderd
- 🔴 `3 - Gemiddeld belaste weg` — Verwijderd
- 🔴 `4 - Licht belaste weg` — Verwijderd
- 🔴 `5 - Weg in woongebied` — Verwijderd
- 🔴 `6 - Weg in verblijfsgebied` — Verwijderd
- 🔴 `7 - Fietspaden` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `enum_Zettingsgevoeligheid` — 🔴 Verwijderd

**Literals:**

- 🔴 `Niet zettingsgevoelig` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Zettingsgevoelig` — Verwijderd

##### `enum_ZettingsgevoeligheidPlus` — 🔴 Verwijderd

**Literals:**

- 🔴 `Licht zettingsgevoelig` — Verwijderd
- 🔴 `Matig zettingsgevoelig` — Verwijderd
- 🔴 `Sterk zettingsgevoelig` — Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingbeheer-openbare-ruimtemodel-basis-imbormodel-imbor"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Beheer Openbare Ruimte/Model Basis IMBOR/Model IMBOR

#### Classes

##### `Aansluitput` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aansluitpunt` — Verwijderd
- 🔴 `risicogebied` — Verwijderd
- 🔴 `type` — Verwijderd

##### `Afvalbak` — 🔴 Verwijderd

**Attributen:**

- 🔴 `type` — Verwijderd
- 🔴 `typePlus` — Verwijderd

##### `Bak` — 🔴 Verwijderd

**Attributen:**

- 🔴 `breedte` — Verwijderd
- 🔴 `diameter` — Verwijderd
- 🔴 `gewichtLeeg` — Verwijderd
- 🔴 `gewichtVol` — Verwijderd
- 🔴 `hoogte` — Verwijderd
- 🔴 `inhoud` — Verwijderd
- 🔴 `jaarOnderhoudUitgevoerd` — Verwijderd
- 🔴 `kwaliteitsniveauActueel` — Verwijderd
- 🔴 `kwaliteitsniveauGewenst` — Verwijderd
- 🔴 `lengte` — Verwijderd
- 🔴 `materiaal` — Verwijderd
- 🔴 `verplaatsbaar` — Verwijderd
- 🔴 `vorm` — Verwijderd

##### `Bank` — 🔴 Verwijderd

**Attributen:**

- 🔴 `type` — Verwijderd
- 🔴 `typePlus` — Verwijderd

##### `Beheerobject` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aangemaaktDoor` — Verwijderd
- 🔴 `beginGarantieperiode` — Verwijderd
- 🔴 `beheergebied` — Verwijderd
- 🔴 `beheerobjectBeheervak` — Verwijderd
- 🔴 `beheerobjectGebruiksfunctie` — Verwijderd
- 🔴 `beheerobjectMemo` — Verwijderd
- 🔴 `beschermdeFloraEnFauna` — Verwijderd
- 🔴 `buurt` — Verwijderd
- 🔴 `conversieID` — Verwijderd
- 🔴 `datumMutatie` — Verwijderd
- 🔴 `datumOplevering` — Verwijderd
- 🔴 `datumPublicatieLV` — Verwijderd
- 🔴 `datumVerwijdering` — Verwijderd
- 🔴 `eindeGarantieperiode` — Verwijderd
- 🔴 `gebiedstype` — Verwijderd
- 🔴 `gemeente` — Verwijderd
- 🔴 `geometrie` — Verwijderd
- 🔴 `gewijzigdDoor` — Verwijderd
- 🔴 `grondsoort` — Verwijderd
- 🔴 `grondsoortPlus` — Verwijderd
- 🔴 `identificatieIMBOR` — Verwijderd
- 🔴 `identificatieIMGeo` — Verwijderd
- 🔴 `jaarVanAanleg` — Verwijderd
- 🔴 `objectBeginTijd` — Verwijderd
- 🔴 `objectEindtijd` — Verwijderd
- 🔴 `onderhoudsplichtige` — Verwijderd
- 🔴 `openbareRuimte` — Verwijderd
- 🔴 `postcode` — Verwijderd
- 🔴 `relatieveHoogteligging` — Verwijderd
- 🔴 `stadsdeel` — Verwijderd
- 🔴 `status` — Verwijderd
- 🔴 `theoretischEindejaar` — Verwijderd
- 🔴 `tijdstipRegistratie` — Verwijderd
- 🔴 `typeBeheerder` — Verwijderd
- 🔴 `typeBeheerderPlus` — Verwijderd
- 🔴 `typeEigenaar` — Verwijderd
- 🔴 `typeEigenaarPlus` — Verwijderd
- 🔴 `typeLigging` — Verwijderd
- 🔴 `waterschap` — Verwijderd
- 🔴 `wijk` — Verwijderd
- 🔴 `woonplaats` — Verwijderd
- 🔴 `zettingsgevoeligheid` — Verwijderd
- 🔴 `zettingsgevoeligheidPlus` — Verwijderd

##### `Bemalingsgebied` — 🔴 Verwijderd

**Attributen:**

- 🔴 `rioleringsgebied` — Verwijderd

##### `Bergingsbassin` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bergendVermogen` — Verwijderd
- 🔴 `pompLedigingsVoorziening` — Verwijderd
- 🔴 `pompSpoelVoorziening` — Verwijderd
- 🔴 `spoelleiding` — Verwijderd
- 🔴 `vorm` — Verwijderd

##### `Boom` — 🔴 Verwijderd

**Attributen:**

- 🔴 `beleidsstatus` — Verwijderd
- 🔴 `beoogdeOmlooptijd` — Verwijderd
- 🔴 `boombeeld` — Verwijderd
- 🔴 `boombeschermer` — Verwijderd
- 🔴 `boomgroep` — Verwijderd
- 🔴 `boomhoogteActueel` — Verwijderd
- 🔴 `boomhoogteklasseActueel` — Verwijderd
- 🔴 `boomhoogteklasseEindebeeld` — Verwijderd
- 🔴 `boomspiegel` — Verwijderd
- 🔴 `boomTypeBeschermingsstatusPlus` — Verwijderd
- 🔴 `boomvoorziening` — Verwijderd
- 🔴 `controlefrequentie` — Verwijderd
- 🔴 `feestverlichting` — Verwijderd
- 🔴 `groeifase` — Verwijderd
- 🔴 `groeiplaatsinrichting` — Verwijderd
- 🔴 `herplantplicht` — Verwijderd
- 🔴 `kiemjaar` — Verwijderd
- 🔴 `kroondiameterklasseActueel` — Verwijderd
- 🔴 `kroondiameterklasseEindebeeld` — Verwijderd
- 🔴 `kroonvolume` — Verwijderd
- 🔴 `leeftijd` — Verwijderd
- 🔴 `meerstammig` — Verwijderd
- 🔴 `monetaireBoomwaarde` — Verwijderd
- 🔴 `snoeifase` — Verwijderd
- 🔴 `stamdiameter` — Verwijderd
- 🔴 `stamdiameterklasse` — Verwijderd
- 🔴 `takvrijeRuimteTotGebouw` — Verwijderd
- 🔴 `takvrijeStam` — Verwijderd
- 🔴 `takvrijeZonePrimair` — Verwijderd
- 🔴 `takvrijeZoneSecundair` — Verwijderd
- 🔴 `transponder` — Verwijderd
- 🔴 `type` — Verwijderd
- 🔴 `typeBeschermingsstatus` — Verwijderd
- 🔴 `typeOmgevingsrisicoklasse` — Verwijderd
- 🔴 `typePlus` — Verwijderd
- 🔴 `typeVermeerderingsvorm` — Verwijderd
- 🔴 `veiligheidsklasseBoom` — Verwijderd
- 🔴 `verplant` — Verwijderd
- 🔴 `verplantbaar` — Verwijderd
- 🔴 `vrijeDoorrijhoogte` — Verwijderd
- 🔴 `vrijeDoorrijhoogtePrimair` — Verwijderd
- 🔴 `vrijeDoorrijhoogteSecundair` — Verwijderd
- 🔴 `vrijeTakval` — Verwijderd

##### `Bord` — 🔴 Verwijderd

**Attributen:**

- 🔴 `breedte` — Verwijderd
- 🔴 `diameter` — Verwijderd
- 🔴 `drager` — Verwijderd
- 🔴 `hoogte` — Verwijderd
- 🔴 `jaarOnderhoudUitgevoerd` — Verwijderd
- 🔴 `lengte` — Verwijderd
- 🔴 `leverancier` — Verwijderd
- 🔴 `materiaal` — Verwijderd
- 🔴 `vorm` — Verwijderd

##### `Bouwwerk` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aanleghoogte` — Verwijderd
- 🔴 `bouwwerkMateriaal` — Verwijderd
- 🔴 `breedte` — Verwijderd
- 🔴 `fabrikant` — Verwijderd
- 🔴 `hoogte` — Verwijderd
- 🔴 `jaarOnderhoudUitgevoerd` — Verwijderd
- 🔴 `lengte` — Verwijderd
- 🔴 `leverancier` — Verwijderd
- 🔴 `oppervlakte` — Verwijderd
- 🔴 `typeFundering` — Verwijderd

##### `Brug` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aantalOverspanningen` — Verwijderd
- 🔴 `bedienaar` — Verwijderd
- 🔴 `bedieningstijden` — Verwijderd
- 🔴 `belastingklasseNieuw` — Verwijderd
- 🔴 `belastingklasseOud` — Verwijderd
- 🔴 `beweegbaar` — Verwijderd
- 🔴 `doorrijbreedte` — Verwijderd
- 🔴 `draagvermogen` — Verwijderd
- 🔴 `hoofdroute` — Verwijderd
- 🔴 `hoofdvaarroute` — Verwijderd
- 🔴 `maximaalToelaatbaarVoertuiggewicht` — Verwijderd
- 🔴 `maximaleAsbelasting` — Verwijderd
- 🔴 `maximaleOverspanning` — Verwijderd
- 🔴 `statischMoment` — Verwijderd
- 🔴 `type` — Verwijderd
- 🔴 `typePlus` — Verwijderd
- 🔴 `zwaarsteVoertuig` — Verwijderd

##### `Drainageput` — 🔴 Verwijderd

**Attributen:**

- 🔴 `risicogebied` — Verwijderd
- 🔴 `type` — Verwijderd

##### `Ecoduct` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aantalOverspanningen` — Verwijderd
- 🔴 `draagvermogen` — Verwijderd
- 🔴 `maximaalToelaatbaarVoertuiggewicht` — Verwijderd
- 🔴 `maximaleAsbelasting` — Verwijderd
- 🔴 `maximaleOverspanning` — Verwijderd
- 🔴 `overbruggingsobjectDoorrijopening` — Verwijderd
- 🔴 `type` — Verwijderd
- 🔴 `zwaarsteVoertuig` — Verwijderd

##### `Fietsparkeervoorziening` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aantalParkeerplaatsen` — Verwijderd
- 🔴 `type` — Verwijderd
- 🔴 `typePlus` — Verwijderd

##### `Filterput` — 🔴 Verwijderd

**Attributen:**

- 🔴 `drain` — Verwijderd
- 🔴 `risicogebied` — Verwijderd

##### `Flyover` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aantalOverspanningen` — Verwijderd
- 🔴 `belastingklasseNieuw` — Verwijderd
- 🔴 `belastingklasseOud` — Verwijderd
- 🔴 `draagvermogen` — Verwijderd
- 🔴 `maximaalToelaatbaarVoertuiggewicht` — Verwijderd
- 🔴 `maximaleAsbelasting` — Verwijderd
- 🔴 `maximaleOverspanning` — Verwijderd
- 🔴 `overbruggingsobjectDoorrijopening` — Verwijderd
- 🔴 `type` — Verwijderd
- 🔴 `zwaarsteVoertuig` — Verwijderd

##### `FunctioneelGebied` — 🔴 Verwijderd

**Attributen:**

- 🔴 `functioneelGebiedCode` — Verwijderd
- 🔴 `functioneelGebiedNaam` — Verwijderd
- 🔴 `omtrek` — Verwijderd
- 🔴 `oppervlakte` — Verwijderd

##### `Geluidsscherm` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aantalDeuren` — Verwijderd
- 🔴 `aantalPanelen` — Verwijderd
- 🔴 `type` — Verwijderd

##### `Gemaal` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aantalBedrijfsaansluitingen` — Verwijderd
- 🔴 `aantalHuisaansluitingen` — Verwijderd
- 🔴 `aantalPompen` — Verwijderd
- 🔴 `bedienaar` — Verwijderd
- 🔴 `effectieveGemaalcapaciteit` — Verwijderd
- 🔴 `hijsinrichting` — Verwijderd
- 🔴 `lanceerinrichting` — Verwijderd
- 🔴 `pompenInSamenloop` — Verwijderd
- 🔴 `type` — Verwijderd
- 🔴 `veiligheidsrooster` — Verwijderd

##### `Groenobject` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aantalObstakels` — Verwijderd
- 🔴 `aantalZijden` — Verwijderd
- 🔴 `afvoeren` — Verwijderd
- 🔴 `bereikbaarheid` — Verwijderd
- 🔴 `bergendVermogen` — Verwijderd
- 🔴 `bewerkingspercentage` — Verwijderd
- 🔴 `BGTFysiekVoorkomen` — Verwijderd
- 🔴 `bollen` — Verwijderd
- 🔴 `breedte` — Verwijderd
- 🔴 `breedteklasseHaag` — Verwijderd
- 🔴 `BVC` — Verwijderd
- 🔴 `cultuurhistorischWaardevol` — Verwijderd
- 🔴 `draagkrachtig` — Verwijderd
- 🔴 `ecologischBeheer` — Verwijderd
- 🔴 `fysiekVoorkomenIMGeo` — Verwijderd
- 🔴 `gewenstSluitingspercentage` — Verwijderd
- 🔴 `groenobjectBereikbaarheidPlus` — Verwijderd
- 🔴 `groenobjectConstructielaag` — Verwijderd
- 🔴 `groenobjectRand` — Verwijderd
- 🔴 `groenobjectSoortnaam` — Verwijderd
- 🔴 `haagvoetLengte` — Verwijderd
- 🔴 `haagvoetOppervlakte` — Verwijderd
- 🔴 `herplantplicht` — Verwijderd
- 🔴 `hoogte` — Verwijderd
- 🔴 `hoogteklasseHaag` — Verwijderd
- 🔴 `knipfrequentie` — Verwijderd
- 🔴 `knipoppervlakte` — Verwijderd
- 🔴 `kwaliteitsniveauActueel` — Verwijderd
- 🔴 `kwaliteitsniveauGewenst` — Verwijderd
- 🔴 `lengte` — Verwijderd
- 🔴 `leverancier` — Verwijderd
- 🔴 `maaifrequentie` — Verwijderd
- 🔴 `maximaleValhoogte` — Verwijderd
- 🔴 `objectnummer` — Verwijderd
- 🔴 `obstakels` — Verwijderd
- 🔴 `omtrek` — Verwijderd
- 🔴 `ondergroei` — Verwijderd
- 🔴 `oppervlakte` — Verwijderd
- 🔴 `opTalud` — Verwijderd
- 🔴 `taludsteilte` — Verwijderd
- 🔴 `type` — Verwijderd
- 🔴 `typeBewerking` — Verwijderd
- 🔴 `typeOmgevingsrisicoklasse` — Verwijderd
- 🔴 `typePlus` — Verwijderd
- 🔴 `typePlus2` — Verwijderd
- 🔴 `veiligheidsklasseBoom` — Verwijderd

##### `Infiltratieput` — 🔴 Verwijderd

**Attributen:**

- 🔴 `porositeit` — Verwijderd
- 🔴 `risicogebied` — Verwijderd

##### `Installatie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `breedte` — Verwijderd
- 🔴 `EANCode` — Verwijderd
- 🔴 `fabrikant` — Verwijderd
- 🔴 `hoogte` — Verwijderd
- 🔴 `inbelgegevens` — Verwijderd
- 🔴 `installateur` — Verwijderd
- 🔴 `jaarOnderhoudUitgevoerd` — Verwijderd
- 🔴 `lengte` — Verwijderd
- 🔴 `leverancier` — Verwijderd
- 🔴 `typeCommunicatie` — Verwijderd

##### `Kademuur` — 🔴 Verwijderd

**Attributen:**

- 🔴 `belastingklasseNieuw` — Verwijderd
- 🔴 `belastingklasseOud` — Verwijderd
- 🔴 `grijpstenen` — Verwijderd
- 🔴 `hoogteBovenkantKademuur` — Verwijderd
- 🔴 `materiaalBovenkantKademuur` — Verwijderd
- 🔴 `oppervlakteBovenkantKademuur` — Verwijderd
- 🔴 `reddingslijn` — Verwijderd
- 🔴 `type` — Verwijderd
- 🔴 `typeBovenkantKademuur` — Verwijderd
- 🔴 `typeFundering` — Verwijderd
- 🔴 `typeVerankering` — Verwijderd

##### `Kast` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aantalDeuren` — Verwijderd
- 🔴 `adresTelecom` — Verwijderd
- 🔴 `BAGCode` — Verwijderd
- 🔴 `breedte` — Verwijderd
- 🔴 `EANCode` — Verwijderd
- 🔴 `fabrikant` — Verwijderd
- 🔴 `hoogte` — Verwijderd
- 🔴 `inbelgegevens` — Verwijderd
- 🔴 `installateur` — Verwijderd
- 🔴 `jaarOnderhoudUitgevoerd` — Verwijderd
- 🔴 `kleur` — Verwijderd
- 🔴 `lengte` — Verwijderd
- 🔴 `leverancier` — Verwijderd
- 🔴 `typeCommunicatie` — Verwijderd
- 🔴 `typeFundering` — Verwijderd
- 🔴 `typeSlot` — Verwijderd
- 🔴 `vermogen` — Verwijderd

##### `Keermuur` — 🔴 Verwijderd

**Attributen:**

- 🔴 `belastingklasseNieuw` — Verwijderd
- 🔴 `belastingklasseOud` — Verwijderd
- 🔴 `type` — Verwijderd

##### `Klimplant` — 🔴 Verwijderd

**Attributen:**

- 🔴 `hoogte` — Verwijderd
- 🔴 `knipfrequentie` — Verwijderd
- 🔴 `knipoppervlakte` — Verwijderd
- 🔴 `ondersteuningsvorm` — Verwijderd
- 🔴 `type` — Verwijderd

##### `Kolk` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bereikbaarheidKolk` — Verwijderd
- 🔴 `risicogebied` — Verwijderd
- 🔴 `type` — Verwijderd

##### `Kunstwerk` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aanleghoogte` — Verwijderd
- 🔴 `antiGraffitiVoorziening` — Verwijderd
- 🔴 `bereikbaarheid` — Verwijderd
- 🔴 `breedte` — Verwijderd
- 🔴 `constructietype` — Verwijderd
- 🔴 `gewicht` — Verwijderd
- 🔴 `hoogte` — Verwijderd
- 🔴 `installateur` — Verwijderd
- 🔴 `jaarConserveren` — Verwijderd
- 🔴 `jaarOnderhoudUitgevoerd` — Verwijderd
- 🔴 `jaarRenovatie` — Verwijderd
- 🔴 `jaarVervanging` — Verwijderd
- 🔴 `kilometreringBegin` — Verwijderd
- 🔴 `kilometreringEinde` — Verwijderd
- 🔴 `kleur` — Verwijderd
- 🔴 `kunstwerkBereikbaarheidPlus` — Verwijderd
- 🔴 `kunstwerkMateriaal` — Verwijderd
- 🔴 `kwaliteitsniveauActueel` — Verwijderd
- 🔴 `kwaliteitsniveauGewenst` — Verwijderd
- 🔴 `lengte` — Verwijderd
- 🔴 `leverancier` — Verwijderd
- 🔴 `looprichel` — Verwijderd
- 🔴 `minimumConditiescore` — Verwijderd
- 🔴 `monument` — Verwijderd
- 🔴 `monumentnummer` — Verwijderd
- 🔴 `objectnaam` — Verwijderd
- 🔴 `objectnummer` — Verwijderd
- 🔴 `onderhoudsregime` — Verwijderd
- 🔴 `oppervlakte` — Verwijderd
- 🔴 `orientatie` — Verwijderd
- 🔴 `technischeLevensduur` — Verwijderd
- 🔴 `typeFundering` — Verwijderd
- 🔴 `typeMonument` — Verwijderd
- 🔴 `vervangingswaarde` — Verwijderd
- 🔴 `wegnummer` — Verwijderd

##### `Leiding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `afwijkendeDieptelegging` — Verwijderd
- 🔴 `breedte` — Verwijderd
- 🔴 `diameter` — Verwijderd
- 🔴 `diepte` — Verwijderd
- 🔴 `eisVoorzorgsmaatregel` — Verwijderd
- 🔴 `geoNauwkeurigheidXY` — Verwijderd
- 🔴 `hoogte` — Verwijderd
- 🔴 `jaarOnderhoudUitgevoerd` — Verwijderd
- 🔴 `lengte` — Verwijderd
- 🔴 `leverancier` — Verwijderd
- 🔴 `materiaal` — Verwijderd
- 🔴 `themaIMKL` — Verwijderd
- 🔴 `verhoogdRisico` — Verwijderd

##### `Leidingelement` — 🔴 Verwijderd

**Attributen:**

- 🔴 `afwijkendeDieptelegging` — Verwijderd
- 🔴 `diepte` — Verwijderd
- 🔴 `geoNauwkeurigheidXY` — Verwijderd
- 🔴 `jaarOnderhoudUitgevoerd` — Verwijderd
- 🔴 `leverancier` — Verwijderd
- 🔴 `themaIMKL` — Verwijderd

##### `Mast` — 🔴 Verwijderd

##### `Meubilair` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aanleghoogte` — Verwijderd
- 🔴 `bouwjaar` — Verwijderd
- 🔴 `breedte` — Verwijderd
- 🔴 `datumAanschaf` — Verwijderd
- 🔴 `diameter` — Verwijderd
- 🔴 `fabrikant` — Verwijderd
- 🔴 `gewicht` — Verwijderd
- 🔴 `hoogte` — Verwijderd
- 🔴 `installateur` — Verwijderd
- 🔴 `jaarOnderhoudUitgevoerd` — Verwijderd
- 🔴 `jaarPraktischEinde` — Verwijderd
- 🔴 `kleur` — Verwijderd
- 🔴 `kwaliteitsniveauActueel` — Verwijderd
- 🔴 `kwaliteitsniveauGewenst` — Verwijderd
- 🔴 `lengte` — Verwijderd
- 🔴 `leverancier` — Verwijderd
- 🔴 `meubilairMateriaal` — Verwijderd
- 🔴 `model` — Verwijderd
- 🔴 `ondergrond` — Verwijderd
- 🔴 `oppervlakte` — Verwijderd
- 🔴 `prijsAanschaf` — Verwijderd
- 🔴 `serienummer` — Verwijderd
- 🔴 `transponder` — Verwijderd
- 🔴 `transponderlocatie` — Verwijderd
- 🔴 `typeFundering` — Verwijderd
- 🔴 `typePlaat` — Verwijderd

##### `Overbruggingsobject` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aanleghoogte` — Verwijderd
- 🔴 `antiGraffitiVoorziening` — Verwijderd
- 🔴 `bereikbaarheid` — Verwijderd
- 🔴 `breedte` — Verwijderd
- 🔴 `hoogte` — Verwijderd
- 🔴 `installateur` — Verwijderd
- 🔴 `jaarConserveren` — Verwijderd
- 🔴 `jaarOnderhoudUitgevoerd` — Verwijderd
- 🔴 `jaarRenovatie` — Verwijderd
- 🔴 `jaarVervanging` — Verwijderd
- 🔴 `kleur` — Verwijderd
- 🔴 `kwaliteitsniveauActueel` — Verwijderd
- 🔴 `kwaliteitsniveauGewenst` — Verwijderd
- 🔴 `lengte` — Verwijderd
- 🔴 `looprichel` — Verwijderd
- 🔴 `minimumConditiescore` — Verwijderd
- 🔴 `onderhoudsregime` — Verwijderd
- 🔴 `oppervlakte` — Verwijderd
- 🔴 `overbruggingsobjectMateriaal` — Verwijderd
- 🔴 `overbruggingsobjectModaliteit` — Verwijderd
- 🔴 `technischeLevensduur` — Verwijderd
- 🔴 `typeFundering` — Verwijderd
- 🔴 `vervangingswaarde` — Verwijderd

##### `Overstortconstructie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bassin` — Verwijderd
- 🔴 `drempelbreedte` — Verwijderd
- 🔴 `drempelniveau` — Verwijderd
- 🔴 `klep` — Verwijderd
- 🔴 `type` — Verwijderd
- 🔴 `vormDrempel` — Verwijderd
- 🔴 `waking` — Verwijderd

##### `Paal` — 🔴 Verwijderd

**Attributen:**

- 🔴 `breedte` — Verwijderd
- 🔴 `diameter` — Verwijderd
- 🔴 `hoogte` — Verwijderd
- 🔴 `jaarOnderhoudUitgevoerd` — Verwijderd
- 🔴 `kwaliteitsniveauActueel` — Verwijderd
- 🔴 `kwaliteitsniveauGewenst` — Verwijderd
- 🔴 `lengte` — Verwijderd
- 🔴 `leverancier` — Verwijderd
- 🔴 `materiaal` — Verwijderd
- 🔴 `vorm` — Verwijderd

##### `Pomp` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aanslagniveau` — Verwijderd
- 🔴 `beginstandDraaiurenteller` — Verwijderd
- 🔴 `besturingskast` — Verwijderd
- 🔴 `laatsteStandDraaiurenteller` — Verwijderd
- 🔴 `laatsteStandkWhTeller` — Verwijderd
- 🔴 `levensduur` — Verwijderd
- 🔴 `model` — Verwijderd
- 🔴 `motorvermogen` — Verwijderd
- 🔴 `onderdeelMetPomp` — Verwijderd
- 🔴 `ontwerpcapaciteit` — Verwijderd
- 🔴 `pompcapaciteit` — Verwijderd
- 🔴 `serienummer` — Verwijderd
- 🔴 `type` — Verwijderd
- 🔴 `typeOnderdeelMetPomp` — Verwijderd
- 🔴 `typePlus` — Verwijderd
- 🔴 `typeWaaier` — Verwijderd
- 🔴 `uitslagpeil` — Verwijderd

##### `Put` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bovengrondsZichtbaar` — Verwijderd
- 🔴 `breedte` — Verwijderd
- 🔴 `diameter` — Verwijderd
- 🔴 `hoogte` — Verwijderd
- 🔴 `jaarOnderhoudUitgevoerd` — Verwijderd
- 🔴 `lengte` — Verwijderd
- 🔴 `leverancier` — Verwijderd
- 🔴 `maaiveldhoogte` — Verwijderd
- 🔴 `materiaal` — Verwijderd
- 🔴 `toegankelijk` — Verwijderd
- 🔴 `typeAfdekking` — Verwijderd
- 🔴 `vorm` — Verwijderd
- 🔴 `wanddikte` — Verwijderd

##### `Putdeksel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `diameter` — Verwijderd
- 🔴 `put` — Verwijderd
- 🔴 `type` — Verwijderd
- 🔴 `vorm` — Verwijderd

##### `Rioleringsgebied` — 🔴 Verwijderd

**Attributen:**

- 🔴 `rioleringsgebied` — Verwijderd
- 🔴 `zuiveringsgebied` — Verwijderd

##### `Rioolput` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aantalBedrijven` — Verwijderd
- 🔴 `aantalRecreatie` — Verwijderd
- 🔴 `aantalWoningen` — Verwijderd
- 🔴 `afvoerendOppervlak` — Verwijderd
- 🔴 `bergendOppervlak` — Verwijderd
- 🔴 `rioolputConstructieonderdeel` — Verwijderd
- 🔴 `rioolputRioolleiding` — Verwijderd
- 🔴 `risicogebied` — Verwijderd
- 🔴 `toegangBreedte` — Verwijderd
- 🔴 `toegangLengte` — Verwijderd
- 🔴 `type` — Verwijderd
- 🔴 `typePlus` — Verwijderd

##### `Scheiding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aanleghoogte` — Verwijderd
- 🔴 `breedte` — Verwijderd
- 🔴 `hoogte` — Verwijderd
- 🔴 `jaarOnderhoudUitgevoerd` — Verwijderd
- 🔴 `lengte` — Verwijderd
- 🔴 `leverancier` — Verwijderd
- 🔴 `objectnaam` — Verwijderd
- 🔴 `objectnummer` — Verwijderd
- 🔴 `oppervlakte` — Verwijderd
- 🔴 `scheidingMateriaal` — Verwijderd
- 🔴 `verplaatsbaar` — Verwijderd

##### `Sensor` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aanleghoogte` — Verwijderd
- 🔴 `elektrakast` — Verwijderd
- 🔴 `frequentieOmvormer` — Verwijderd
- 🔴 `hoogte` — Verwijderd
- 🔴 `jaarOnderhoudUitgevoerd` — Verwijderd
- 🔴 `leverancier` — Verwijderd
- 🔴 `meetpunt` — Verwijderd
- 🔴 `PLC` — Verwijderd

##### `SolitairePlant` — 🔴 Verwijderd

**Attributen:**

- 🔴 `hoogte` — Verwijderd
- 🔴 `type` — Verwijderd

##### `Speelterrein` — 🔴 Verwijderd

**Attributen:**

- 🔴 `jaarHerinrichting` — Verwijderd
- 🔴 `speelterreinLeeftijdDoelgroep` — Verwijderd
- 🔴 `type` — Verwijderd
- 🔴 `typePlus` — Verwijderd

##### `Speeltoestel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `catalogusprijs` — Verwijderd
- 🔴 `certificaat` — Verwijderd
- 🔴 `certificaatnummer` — Verwijderd
- 🔴 `certificeringsinstantie` — Verwijderd
- 🔴 `controlefrequentie` — Verwijderd
- 🔴 `datumCertificaat` — Verwijderd
- 🔴 `gemakkelijkToegankelijk` — Verwijderd
- 🔴 `inspectievolgorde` — Verwijderd
- 🔴 `installatiekosten` — Verwijderd
- 🔴 `speelterrein` — Verwijderd
- 🔴 `speeltoestelToestelonderdeel` — Verwijderd
- 🔴 `technischeLevensduur` — Verwijderd
- 🔴 `toestelcode` — Verwijderd
- 🔴 `toestelgroep` — Verwijderd
- 🔴 `toestelnaam` — Verwijderd
- 🔴 `type` — Verwijderd
- 🔴 `typenummer` — Verwijderd
- 🔴 `typePlus` — Verwijderd
- 🔴 `typePlus2` — Verwijderd
- 🔴 `valruimteHoogte` — Verwijderd
- 🔴 `valruimteOmvang` — Verwijderd
- 🔴 `vrijeValhoogte` — Verwijderd

##### `Sportterrein` — 🔴 Verwijderd

**Attributen:**

- 🔴 `drainage` — Verwijderd
- 🔴 `gebruiksvorm` — Verwijderd
- 🔴 `sportcomplex` — Verwijderd
- 🔴 `sportterreinTypeSport` — Verwijderd
- 🔴 `type` — Verwijderd
- 🔴 `typePlus` — Verwijderd
- 🔴 `veldnummer` — Verwijderd
- 🔴 `verlicht` — Verwijderd

##### `Stuwgebied` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bemalingsgebied` — Verwijderd

##### `Terreindeel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `breedte` — Verwijderd
- 🔴 `cultuurhistorischWaardevol` — Verwijderd
- 🔴 `herplantplicht` — Verwijderd
- 🔴 `oppervlakte` — Verwijderd
- 🔴 `opTalud` — Verwijderd
- 🔴 `percentageLoofbos` — Verwijderd
- 🔴 `terreindeelSoortnaam` — Verwijderd
- 🔴 `type` — Verwijderd
- 🔴 `typeBewerking` — Verwijderd
- 🔴 `typePlus` — Verwijderd
- 🔴 `typePlus2` — Verwijderd

##### `Tunnelobject` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aanleghoogte` — Verwijderd
- 🔴 `aantalTunnelbuizen` — Verwijderd
- 🔴 `breedte` — Verwijderd
- 🔴 `doorrijbreedte` — Verwijderd
- 🔴 `doorrijhoogte` — Verwijderd
- 🔴 `hoogte` — Verwijderd
- 🔴 `jaarConserveren` — Verwijderd
- 🔴 `jaarOnderhoudUitgevoerd` — Verwijderd
- 🔴 `lengte` — Verwijderd
- 🔴 `leverancier` — Verwijderd
- 🔴 `objectnaam` — Verwijderd
- 🔴 `objectnummer` — Verwijderd
- 🔴 `oppervlakte` — Verwijderd
- 🔴 `tunnelobjectMateriaal` — Verwijderd

##### `Uitlaatconstructie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `type` — Verwijderd
- 🔴 `waterobject` — Verwijderd

##### `Vegetatieobject` — 🔴 Verwijderd

**Attributen:**

- 🔴 `afvoeren` — Verwijderd
- 🔴 `bereikbaarheid` — Verwijderd
- 🔴 `ecologischBeheer` — Verwijderd
- 🔴 `kwaliteitsniveauActueel` — Verwijderd
- 🔴 `kwaliteitsniveauGewenst` — Verwijderd
- 🔴 `kweker` — Verwijderd
- 🔴 `leverancier` — Verwijderd
- 🔴 `objectnummer` — Verwijderd
- 🔴 `soortnaam` — Verwijderd
- 🔴 `typeStandplaats` — Verwijderd
- 🔴 `typeStandplaatsPlus` — Verwijderd
- 🔴 `vegetatieobjectBereikbaarheidPlus` — Verwijderd

##### `Verhardingsobject` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aanleghoogte` — Verwijderd
- 🔴 `aanOfVrijliggend` — Verwijderd
- 🔴 `aantalDeklagen` — Verwijderd
- 🔴 `aantalOnderlagen` — Verwijderd
- 🔴 `aantalTussenlagen` — Verwijderd
- 🔴 `afmeting` — Verwijderd
- 🔴 `belasting` — Verwijderd
- 🔴 `bergendVermogen` — Verwijderd
- 🔴 `BGTFysiekVoorkomen` — Verwijderd
- 🔴 `breedte` — Verwijderd
- 🔴 `dikteConstructie` — Verwijderd
- 🔴 `draagkrachtig` — Verwijderd
- 🔴 `formaat` — Verwijderd
- 🔴 `fysiekVoorkomenIMGeo` — Verwijderd
- 🔴 `geluidsreducerend` — Verwijderd
- 🔴 `jaarConserveren` — Verwijderd
- 🔴 `jaarOnderhoudUitgevoerd` — Verwijderd
- 🔴 `jaarPraktischEinde` — Verwijderd
- 🔴 `kleur` — Verwijderd
- 🔴 `kwaliteitsniveauActueel` — Verwijderd
- 🔴 `kwaliteitsniveauGewenst` — Verwijderd
- 🔴 `lengte` — Verwijderd
- 🔴 `lengteKunstgras` — Verwijderd
- 🔴 `lengteVoegen` — Verwijderd
- 🔴 `levensduur` — Verwijderd
- 🔴 `materiaal` — Verwijderd
- 🔴 `maximaleValhoogte` — Verwijderd
- 🔴 `omtrek` — Verwijderd
- 🔴 `ondergrondcode` — Verwijderd
- 🔴 `oppervlakte` — Verwijderd
- 🔴 `opTalud` — Verwijderd
- 🔴 `plaatsorientatie` — Verwijderd
- 🔴 `prijsAanschaf` — Verwijderd
- 🔴 `rijstrook` — Verwijderd
- 🔴 `soortVoeg` — Verwijderd
- 🔴 `toelichtingGemengdeBestrating` — Verwijderd
- 🔴 `type` — Verwijderd
- 🔴 `typeConstructie` — Verwijderd
- 🔴 `typeFundering` — Verwijderd
- 🔴 `typePlus` — Verwijderd
- 🔴 `typePlus2` — Verwijderd
- 🔴 `typeRijstrook` — Verwijderd
- 🔴 `typeVoeg` — Verwijderd
- 🔴 `typeVoegvulling` — Verwijderd
- 🔴 `vegen` — Verwijderd
- 🔴 `verhardingsobjectConstructielaag` — Verwijderd
- 🔴 `verhardingsobjectModaliteit` — Verwijderd
- 🔴 `verhardingsobjectRand` — Verwijderd
- 🔴 `verhardingsobjectWegfunctie` — Verwijderd
- 🔴 `verhoogdeLigging` — Verwijderd
- 🔴 `vulmateriaalKunstgras` — Verwijderd
- 🔴 `waterdoorlatendheid` — Verwijderd
- 🔴 `wegas` — Verwijderd
- 🔴 `wegcategorieDV` — Verwijderd
- 🔴 `wegcategorieDVPlus` — Verwijderd
- 🔴 `wegnummer` — Verwijderd
- 🔴 `wegtypeBestaand` — Verwijderd
- 🔴 `wegvak` — Verwijderd
- 🔴 `wegvaknummer` — Verwijderd

##### `Verkeersdrempel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `ontwerpsnelheid` — Verwijderd
- 🔴 `type` — Verwijderd
- 🔴 `typePlus` — Verwijderd

##### `Verlichtingsobject` — 🔴 Verwijderd

##### `Viaduct` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aantalOverspanningen` — Verwijderd
- 🔴 `belastingklasseNieuw` — Verwijderd
- 🔴 `belastingklasseOud` — Verwijderd
- 🔴 `draagvermogen` — Verwijderd
- 🔴 `maximaalToelaatbaarVoertuiggewicht` — Verwijderd
- 🔴 `maximaleAsbelasting` — Verwijderd
- 🔴 `maximaleOverspanning` — Verwijderd
- 🔴 `overbruggingsobjectDoorrijopening` — Verwijderd
- 🔴 `type` — Verwijderd
- 🔴 `waterobject` — Verwijderd
- 🔴 `zwaarsteVoertuig` — Verwijderd

##### `Waterinrichtingsobject` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aanleghoogte` — Verwijderd
- 🔴 `breedte` — Verwijderd
- 🔴 `jaarConserveren` — Verwijderd
- 🔴 `jaarOnderhoudUitgevoerd` — Verwijderd
- 🔴 `kwaliteitsniveauActueel` — Verwijderd
- 🔴 `kwaliteitsniveauGewenst` — Verwijderd
- 🔴 `lengte` — Verwijderd
- 🔴 `leverancier` — Verwijderd
- 🔴 `materiaal` — Verwijderd
- 🔴 `oppervlakte` — Verwijderd

##### `Waterobject` — 🔴 Verwijderd

**Attributen:**

- 🔴 `breedte` — Verwijderd
- 🔴 `folie` — Verwijderd
- 🔴 `hoogte` — Verwijderd
- 🔴 `infiltrerendOppervlak` — Verwijderd
- 🔴 `infiltrerendVermogen` — Verwijderd
- 🔴 `lengte` — Verwijderd
- 🔴 `lozingspunt` — Verwijderd
- 🔴 `oppervlakte` — Verwijderd
- 🔴 `porositeit` — Verwijderd
- 🔴 `streefdiepte` — Verwijderd
- 🔴 `type` — Verwijderd
- 🔴 `typePlus` — Verwijderd
- 🔴 `typePlus2` — Verwijderd
- 🔴 `typeVaarwater` — Verwijderd
- 🔴 `typeWaterplant` — Verwijderd
- 🔴 `uitstroomniveau` — Verwijderd
- 🔴 `vaarwegtraject` — Verwijderd
- 🔴 `vorm` — Verwijderd
- 🔴 `waternaam` — Verwijderd
- 🔴 `waterpeil` — Verwijderd
- 🔴 `waterpeilWinter` — Verwijderd
- 🔴 `waterpeilZomer` — Verwijderd
- 🔴 `waterplanten` — Verwijderd

##### `Weginrichtingsobject` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aanleghoogte` — Verwijderd
- 🔴 `breedte` — Verwijderd
- 🔴 `hoogte` — Verwijderd
- 🔴 `jaarConserveren` — Verwijderd
- 🔴 `jaarOnderhoudUitgevoerd` — Verwijderd
- 🔴 `kwaliteitsniveauActueel` — Verwijderd
- 🔴 `kwaliteitsniveauGewenst` — Verwijderd
- 🔴 `lengte` — Verwijderd
- 🔴 `leverancier` — Verwijderd
- 🔴 `materiaal` — Verwijderd
- 🔴 `oppervlakte` — Verwijderd
- 🔴 `weginrichtingsobjectWegfunctie` — Verwijderd

#### Generalisaties

- 🔴 Verwijderd: `Aansluitput` ⟶ `Put`
- 🔴 Verwijderd: `Afvalbak` ⟶ `Bak`
- 🔴 Verwijderd: `Bak` ⟶ `Beheerobject`
- 🔴 Verwijderd: `Bank` ⟶ `Meubilair`
- 🔴 Verwijderd: `Bemalingsgebied` ⟶ `FunctioneelGebied`
- 🔴 Verwijderd: `Bergingsbassin` ⟶ `Bouwwerk`
- 🔴 Verwijderd: `Boom` ⟶ `Vegetatieobject`
- 🔴 Verwijderd: `Bord` ⟶ `Beheerobject`
- 🔴 Verwijderd: `Bouwwerk` ⟶ `Beheerobject`
- 🔴 Verwijderd: `Brug` ⟶ `Overbruggingsobject`
- 🔴 Verwijderd: `Drainageput` ⟶ `Put`
- 🔴 Verwijderd: `Ecoduct` ⟶ `Overbruggingsobject`
- 🔴 Verwijderd: `Fietsparkeervoorziening` ⟶ `Meubilair`
- 🔴 Verwijderd: `Filterput` ⟶ `Put`
- 🔴 Verwijderd: `Flyover` ⟶ `Overbruggingsobject`
- 🔴 Verwijderd: `FunctioneelGebied` ⟶ `Beheerobject`
- 🔴 Verwijderd: `Geluidsscherm` ⟶ `Scheiding`
- 🔴 Verwijderd: `Gemaal` ⟶ `Kunstwerk`
- 🔴 Verwijderd: `Groenobject` ⟶ `Beheerobject`
- 🔴 Verwijderd: `Infiltratieput` ⟶ `Put`
- 🔴 Verwijderd: `Installatie` ⟶ `Beheerobject`
- 🔴 Verwijderd: `Kademuur` ⟶ `Scheiding`
- 🔴 Verwijderd: `Kast` ⟶ `Beheerobject`
- 🔴 Verwijderd: `Keermuur` ⟶ `Scheiding`
- 🔴 Verwijderd: `Klimplant` ⟶ `Vegetatieobject`
- 🔴 Verwijderd: `Kolk` ⟶ `Put`
- 🔴 Verwijderd: `Kunstwerk` ⟶ `Beheerobject`
- 🔴 Verwijderd: `Leiding` ⟶ `Beheerobject`
- 🔴 Verwijderd: `Leidingelement` ⟶ `Beheerobject`
- 🔴 Verwijderd: `Mast` ⟶ `Beheerobject`
- 🔴 Verwijderd: `Meubilair` ⟶ `Beheerobject`
- 🔴 Verwijderd: `Overbruggingsobject` ⟶ `Beheerobject`
- 🔴 Verwijderd: `Overstortconstructie` ⟶ `Kunstwerk`
- 🔴 Verwijderd: `Paal` ⟶ `Beheerobject`
- 🔴 Verwijderd: `Pomp` ⟶ `Installatie`
- 🔴 Verwijderd: `Put` ⟶ `Beheerobject`
- 🔴 Verwijderd: `Putdeksel` ⟶ `Weginrichtingsobject`
- 🔴 Verwijderd: `Rioleringsgebied` ⟶ `FunctioneelGebied`
- 🔴 Verwijderd: `Rioolput` ⟶ `Put`
- 🔴 Verwijderd: `Scheiding` ⟶ `Beheerobject`
- 🔴 Verwijderd: `Sensor` ⟶ `Beheerobject`
- 🔴 Verwijderd: `SolitairePlant` ⟶ `Vegetatieobject`
- 🔴 Verwijderd: `Speelterrein` ⟶ `FunctioneelGebied`
- 🔴 Verwijderd: `Speeltoestel` ⟶ `Meubilair`
- 🔴 Verwijderd: `Sportterrein` ⟶ `FunctioneelGebied`
- 🔴 Verwijderd: `Stuwgebied` ⟶ `FunctioneelGebied`
- 🔴 Verwijderd: `Terreindeel` ⟶ `Beheerobject`
- 🔴 Verwijderd: `Tunnelobject` ⟶ `Beheerobject`
- 🔴 Verwijderd: `Uitlaatconstructie` ⟶ `Kunstwerk`
- 🔴 Verwijderd: `Vegetatieobject` ⟶ `Beheerobject`
- 🔴 Verwijderd: `Verhardingsobject` ⟶ `Beheerobject`
- 🔴 Verwijderd: `Verkeersdrempel` ⟶ `Weginrichtingsobject`
- 🔴 Verwijderd: `Verlichtingsobject` ⟶ `Beheerobject`
- 🔴 Verwijderd: `Viaduct` ⟶ `Overbruggingsobject`
- 🔴 Verwijderd: `Waterinrichtingsobject` ⟶ `Beheerobject`
- 🔴 Verwijderd: `Waterobject` ⟶ `Beheerobject`
- 🔴 Verwijderd: `Weginrichtingsobject` ⟶ `Beheerobject`

<a id="structureel-delfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingbeheer-openbare-ruimtemodel-beheer-openbare-ruimte"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Beheer Openbare Ruimte/Model Beheer Openbare Ruimte

#### Classes

##### `Actie` — 🔴 Verwijderd

##### `Areaal` — 🔴 Verwijderd

**Attributen:**

- 🔴 `geometrie` — Verwijderd

##### `CROW-Melding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `kwaliteitsniveau` — Verwijderd

##### `Deelplan/Veld` — 🔴 Verwijderd

##### `Fase/Oplevering` — 🔴 Verwijderd

##### `Geo-Object` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheid` — Verwijderd
- 🔴 `datumEindeGeldigheid` — Verwijderd
- 🔴 `geometrieSoort` — Verwijderd
- 🔴 `identificatie` — Verwijderd

##### `Grondbeheerder` — 🔴 Verwijderd

##### `Inspectie` — 🔴 Verwijderd

##### `KadastraleMutatie` — 🔴 Verwijderd

##### `Kwaliteitscatalogus Openbare Ruimte` — 🔴 Verwijderd

##### `Kwaliteitskenmerken` — 🔴 Verwijderd

##### `Logboek` — 🔴 Verwijderd

##### `Melding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `advies` — Verwijderd
- 🔴 `categorie` — Verwijderd
- 🔴 `constatering` — Verwijderd
- 🔴 `datumAdvies` — Verwijderd
- 🔴 `datumMelding` — Verwijderd
- 🔴 `datumUitvoering` — Verwijderd
- 🔴 `foto` — Verwijderd
- 🔴 `locatie` — Verwijderd
- 🔴 `opmerkingen` — Verwijderd
- 🔴 `status` — Verwijderd
- 🔴 `uitgevoerd` — Verwijderd

##### `MeldingOngeval` — 🔴 Verwijderd

##### `MOOR-melding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `adresaanduiding` — Verwijderd
- 🔴 `datumAanmelding` — Verwijderd
- 🔴 `datumGoedkeuring` — Verwijderd
- 🔴 `eindtijd` — Verwijderd
- 🔴 `goedgekeurd` — Verwijderd
- 🔴 `herstelwerkzaamhedenVereist` — Verwijderd
- 🔴 `omschrijvingHerstelwerkzaamheden` — Verwijderd
- 🔴 `publiceren` — Verwijderd
- 🔴 `starttijd` — Verwijderd
- 🔴 `wegbeheerder` — Verwijderd

##### `Omgevingsvergunning` — 🔴 Verwijderd

##### `Onderhoud` — 🔴 Verwijderd

##### `Opbreking` — 🔴 Verwijderd

##### `Proces-verbaal-MOOR-melding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datum` — Verwijderd
- 🔴 `goedkeuring` — Verwijderd
- 🔴 `opmerkingen` — Verwijderd

##### `Schouwronde` — 🔴 Verwijderd

##### `Storing` — 🔴 Verwijderd

##### `Taak` — 🔴 Verwijderd

##### `Uitvoerder Graafwerkzaamheden` — 🔴 Verwijderd

##### `Verkeerslicht` — 🔴 Verwijderd

#### Enumeraties

##### `CROW-Kwaliteitsniveaus` — 🔴 Verwijderd

**Literals:**

- 🔴 `Niveau A` — Verwijderd
- 🔴 `Niveau A+` — Verwijderd
- 🔴 `Niveau B` — Verwijderd
- 🔴 `Niveau C` — Verwijderd
- 🔴 `Niveau D` — Verwijderd

##### `Energielabel` — 🔴 Verwijderd

**Literals:**

- 🔴 `A` — Verwijderd
- 🔴 `B` — Verwijderd
- 🔴 `C` — Verwijderd
- 🔴 `D` — Verwijderd
- 🔴 `E` — Verwijderd
- 🔴 `F` — Verwijderd

##### `Oppervlakte Woning` — 🔴 Verwijderd

**Literals:**

- 🔴 `100 - 124 m2` — Verwijderd
- 🔴 `125 - 149 m2` — Verwijderd
- 🔴 `15 - 49 m2` — Verwijderd
- 🔴 `150 en groter` — Verwijderd
- 🔴 `50 - 74 m2` — Verwijderd
- 🔴 `75 - 99 m2` — Verwijderd
- 🔴 `kleiner dan 15 m2` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `Areaal` «binnen» → `Schouwronde`
- 🔴 Verwijderd: `Areaal` «ligt in» → `Buurt`
- 🔴 Verwijderd: `Areaal` «ligt in» → `Buurt`
- 🔴 Verwijderd: `Areaal` «valt binnen» → `Wijk`
- 🔴 Verwijderd: `Areaal` «valt binnen» → `Wijk`
- 🔴 Verwijderd: `CROW-Melding` «conform» → `Kwaliteitscatalogus Openbare Ruimte`
- 🔴 Verwijderd: `KadastraleMutatie` «betreft» → `KadastraleOnroerendeZaak`
- 🔴 Verwijderd: `KadastraleMutatie` «heeft betrekking op» → `ZakelijkRecht`
- 🔴 Verwijderd: `Logboek` «bevat» → `Melding`
- 🔴 Verwijderd: `Melding` «melder» → `Medewerker`
- 🔴 Verwijderd: `Melding` «melder» → `NatuurlijkPersoon`
- 🔴 Verwijderd: `Melding` «uitvoerder» → `Leverancier`
- 🔴 Verwijderd: `Melding` «uitvoerder» → `Medewerker`
- 🔴 Verwijderd: `MOOR-melding` «betreft» → `Opbreking`
- 🔴 Verwijderd: `MOOR-melding` «betreft» → `Proces-verbaal-MOOR-melding`
- 🔴 Verwijderd: `MOOR-melding` «verplicht tot» → `Omgevingsvergunning`
- 🔴 Verwijderd: `Omgevingsvergunning` «betrekking op» → `Plan`
- 🔴 Verwijderd: `Proces-verbaal-MOOR-melding` «heeft» → `Document`
- 🔴 Verwijderd: `Schouwronde` «heeft» → `Melding`
- 🔴 Verwijderd: `Uitvoerder Graafwerkzaamheden` «doet» → `MOOR-melding`
- 🔴 Verwijderd: `Uitvoerder Graafwerkzaamheden` «maakt» → `Opbreking`

#### Generalisaties

- 🔴 Verwijderd: `Actie` ⟶ `Melding`
- 🔴 Verwijderd: `CROW-Melding` ⟶ `Melding`
- 🔴 Verwijderd: `Grondbeheerder` ⟶ `Rechtspersoon`
- 🔴 Verwijderd: `Inspectie` ⟶ `Melding`
- 🔴 Verwijderd: `MeldingOngeval` ⟶ `Melding`
- 🔴 Verwijderd: `Storing` ⟶ `Melding`
- 🔴 Verwijderd: `Uitvoerder Graafwerkzaamheden` ⟶ `Grondbeheerder`
- 🔴 Verwijderd: `Uitvoerder Graafwerkzaamheden` ⟶ `Leverancier`

<a id="structureel-delfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingbouwen-en-wonenmodel-wonen"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Bouwen en Wonen/Model Wonen

#### Classes

##### `Gebouw` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aantal` — Verwijderd
- 🔴 `aantalAdressen` — Verwijderd
- 🔴 `aantalKamers` — Verwijderd
- 🔴 `aardgasloos` — Verwijderd
- 🔴 `duurzaam` — Verwijderd
- 🔴 `energielabel` — Verwijderd
- 🔴 `natuurinclusief` — Verwijderd
- 🔴 `oppervlakte` — Verwijderd
- 🔴 `regenwater` — Verwijderd

##### `Huurwoningen` — 🔴 Verwijderd

**Attributen:**

- 🔴 `huurprijs` — Verwijderd

##### `Koopwoningen` — 🔴 Verwijderd

**Attributen:**

- 🔴 `koopprijs` — Verwijderd

##### `Plan` — 🔴 Verwijderd

**Attributen:**

- 🔴 `70ProcentVerkocht` — Verwijderd
- 🔴 `aardgasloos` — Verwijderd
- 🔴 `bestemmingGoedgekeurd` — Verwijderd
- 🔴 `eersteOplevering` — Verwijderd
- 🔴 `eigendomGemeente` — Verwijderd
- 🔴 `gebiedstransformatie` — Verwijderd
- 🔴 `intentie` — Verwijderd
- 🔴 `laatsteOplevering` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `nummer` — Verwijderd
- 🔴 `onherroepelijk` — Verwijderd
- 🔴 `percelen` — Verwijderd
- 🔴 `startbouw` — Verwijderd
- 🔴 `startVerkoop` — Verwijderd

##### `Projectleider` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd

##### `Projectontwikkelaar` — 🔴 Verwijderd

**Attributen:**

- 🔴 `adres` — Verwijderd
- 🔴 `naam` — Verwijderd

##### `Studentenwoningen` — 🔴 Verwijderd

**Attributen:**

- 🔴 `huurprijs` — Verwijderd
- 🔴 `zelfstandig` — Verwijderd

#### Enumeraties

##### `Energielabel` — 🔴 Verwijderd

**Literals:**

- 🔴 `A` — Verwijderd
- 🔴 `B` — Verwijderd
- 🔴 `C` — Verwijderd
- 🔴 `D` — Verwijderd
- 🔴 `E` — Verwijderd
- 🔴 `F` — Verwijderd

##### `Oppervlakte Woning` — 🔴 Verwijderd

**Literals:**

- 🔴 `100 - 124 m2` — Verwijderd
- 🔴 `125 - 149 m2` — Verwijderd
- 🔴 `15 - 49 m2` — Verwijderd
- 🔴 `150 en groter` — Verwijderd
- 🔴 `50 - 74 m2` — Verwijderd
- 🔴 `75 - 99 m2` — Verwijderd
- 🔴 `kleiner dan 15 m2` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `Plan` «Bestaat uit» → `Gebouw`
- 🔴 Verwijderd: `Projectleider` «is projectleider van» → `Plan`
- 🔴 Verwijderd: `Projectontwikkelaar` «heeft» → `Plan`

#### Generalisaties

- 🔴 Verwijderd: `Huurwoningen` ⟶ `Gebouw`
- 🔴 Verwijderd: `Koopwoningen` ⟶ `Gebouw`
- 🔴 Verwijderd: `Projectleider` ⟶ `NatuurlijkPersoon`
- 🔴 Verwijderd: `Projectontwikkelaar` ⟶ `NietNatuurlijkPersoon`
- 🔴 Verwijderd: `Studentenwoningen` ⟶ `Gebouw`

<a id="structureel-delfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingomgevingswetmodel-omgevingswetmodel-aanvragen-en-meldingen"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Omgevingswet/Model Omgevingswet/Model Aanvragen en Meldingen

#### Classes

##### `Bevoegd Gezag` — 🔴 Verwijderd

##### `Gemachtigde` — 🔴 Verwijderd

##### `Initiatiefnemer` — 🔴 Verwijderd

##### `Project` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Projectactiviteit` — 🔴 Verwijderd

##### `Projectlocatie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `adres` — Verwijderd
- 🔴 `kadastraalPerceel` — Verwijderd
- 🔴 `kadastraleGemeente` — Verwijderd
- 🔴 `kadastraleSectie` — Verwijderd

##### `Specificatie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `antwoord` — Verwijderd
- 🔴 `groepering` — Verwijderd
- 🔴 `publiceerbaar` — Verwijderd
- 🔴 `vraagClassificatie` — Verwijderd
- 🔴 `vraagID` — Verwijderd
- 🔴 `vraagreferentie` — Verwijderd
- 🔴 `vraagtekst` — Verwijderd

##### `Uitvoerende instantie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd

##### `Verzoek` — 🔴 Verwijderd

**Attributen:**

- 🔴 `akkoordverklaring` — Verwijderd
- 🔴 `ambtshalve` — Verwijderd
- 🔴 `datumIndiening` — Verwijderd
- 🔴 `doel` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `referentieAanvrager` — Verwijderd
- 🔴 `toelichtingLaterAanTeLeverenInformatie` — Verwijderd
- 🔴 `toelichtingNietAanTeLeverenInformatie` — Verwijderd
- 🔴 `toelichtingVerzoek` — Verwijderd
- 🔴 `type` — Verwijderd
- 🔴 `verzoeknummer` — Verwijderd
- 🔴 `volgnummer` — Verwijderd

#### Enumeraties

##### `Doel verzoek` — 🔴 Verwijderd

**Literals:**

- 🔴 `aanvullen` — Verwijderd
- 🔴 `initieren` — Verwijderd
- 🔴 `intrekken` — Verwijderd
- 🔴 `vooroverleg` — Verwijderd

##### `Type Verzoek` — 🔴 Verwijderd

**Literals:**

- 🔴 `Aanvraag Maatwerkvoorschrift` — Verwijderd
- 🔴 `Aanvraag Toestemming Gelijkwaardige Maatregel` — Verwijderd
- 🔴 `Aanvraag vergunning` — Verwijderd
- 🔴 `Informatie` — Verwijderd
- 🔴 `Informatie ongewoon Voorval` — Verwijderd
- 🔴 `Melding` — Verwijderd
- 🔴 `Melding Gelijkwaardige Maatregel` — Verwijderd

##### `Vraag Classificatie` — 🔴 Verwijderd

**Literals:**

- 🔴 `Aanvrager` — Verwijderd
- 🔴 `Activiteit` — Verwijderd
- 🔴 `Gevraagde Bijlage` — Verwijderd
- 🔴 `Project` — Verwijderd
- 🔴 `Verzoek` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `Gemachtigde` «dient in» → `Verzoek`
- 🔴 Verwijderd: `Initiatiefnemer` «heeft als verantwoordelijke» → `Verzoek`
- 🔴 Verwijderd: `Project` «heeft» → `Projectactiviteit`
- 🔴 Verwijderd: `Project` «heeft» → `Projectlocatie`
- 🔴 Verwijderd: `Projectactiviteit` «uitgevoerd op» → `Projectlocatie`
- 🔴 Verwijderd: `Projectlocatie` «betreft» → `Locatie`
- 🔴 Verwijderd: `Specificatie` «gedefinieerd door» → `Projectactiviteit`
- 🔴 Verwijderd: `Verzoek` «behandelaar» → `Uitvoerende instantie`
- 🔴 Verwijderd: `Verzoek` «betreft eerder verzoek» → `Verzoek`
- 🔴 Verwijderd: `Verzoek` «betreft» → `Activiteit`
- 🔴 Verwijderd: `Verzoek` «betreft» → `Locatie`
- 🔴 Verwijderd: `Verzoek` «betreft» → `Project`
- 🔴 Verwijderd: `Verzoek` «betreft» → `Projectactiviteit`
- 🔴 Verwijderd: `Verzoek` «bevat» → `Specificatie`
- 🔴 Verwijderd: `Verzoek` «leidt tot» → `Zaak`
- 🔴 Verwijderd: `Verzoek` «verantwoordelijke» → `Bevoegd Gezag`

#### Generalisaties

- 🔴 Verwijderd: `Bevoegd Gezag` ⟶ `Rechtspersoon`
- 🔴 Verwijderd: `Gemachtigde` ⟶ `Rechtspersoon`
- 🔴 Verwijderd: `Initiatiefnemer` ⟶ `Rechtspersoon`

<a id="structureel-delfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingomgevingswetmodel-omgevingswetmodel-officiele-publicaties"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Omgevingswet/Model Omgevingswet/Model Officiele Publicaties

#### Classes

##### `Omgevingsdocument` — 🔴 Verwijderd

##### `Regeltekst` — 🔴 Verwijderd

**Attributen:**

- 🔴 `identificatie` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `tekst` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `Omgevingsdocument` «bevat» → `Regeltekst`
- 🔴 Verwijderd: `Regeltekst` «heeft idealisatie» → `Idealisatie`
- 🔴 Verwijderd: `Regeltekst` «heeft thema» → `Thema`
- 🔴 Verwijderd: `Regeltekst` «is gerelateerd» → `Regeltekst`
- 🔴 Verwijderd: `Regeltekst` «werkingsgebied» → `Locatie`
- 🔴 Verwijderd: `Regeltekst` «werkingsgebied» → `Regeltekst`

<a id="structureel-delfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingomgevingswetmodel-omgevingswetmodel-omgevingswet"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Omgevingswet/Model Omgevingswet/Model Omgevingswet

#### Classes

##### `Activiteit` — 🔴 Verwijderd

**Attributen:**

- 🔴 `groep` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `NEN3610ID` — Verwijderd

##### `Beperkingsgebied` — 🔴 Verwijderd

**Attributen:**

- 🔴 `groep` — Verwijderd
- 🔴 `naam` — Verwijderd

##### `Functie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `groep` — Verwijderd
- 🔴 `naam` — Verwijderd

##### `Gebiedsaanwijzing` — 🔴 Verwijderd

**Attributen:**

- 🔴 `groep` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `NEN3610ID` — Verwijderd

##### `Idealisatie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Instructieregel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `instructieregelInstrument` — Verwijderd
- 🔴 `instructieregelTaakuitoefening` — Verwijderd

##### `Juridische Regel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBekend` — Verwijderd
- 🔴 `datumEindeGeldigheid` — Verwijderd
- 🔴 `datumInWerking` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `regeltekst` — Verwijderd
- 🔴 `thema` — Verwijderd

##### `Norm` — 🔴 Verwijderd

**Attributen:**

- 🔴 `NEN3610ID` — Verwijderd

##### `Normwaarde` — 🔴 Verwijderd

**Attributen:**

- 🔴 `kwalitatieveWaarde` — Verwijderd
- 🔴 `kwantitatieveWaardeEenheid` — Verwijderd
- 🔴 `kwantitatieveWaardeOmvang` — Verwijderd

##### `Omgevingsnorm` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `omgevingsnormGroep` — Verwijderd

##### `Omgevingswaarde` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `omgevingswaardeGroep` — Verwijderd

##### `Omgevingswaarderegel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `groep` — Verwijderd
- 🔴 `naam` — Verwijderd

##### `Regel voor Iedereen` — 🔴 Verwijderd

**Attributen:**

- 🔴 `activiteitRegelKwalificatie` — Verwijderd

##### `Thema` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `Activiteit` «bovenliggende activiteit» → `Activiteit`
- 🔴 Verwijderd: `Activiteit` «gerelateerde activiteit» → `Activiteit`
- 🔴 Verwijderd: `Activiteit` «is verbonden met» → `Locatie`
- 🔴 Verwijderd: `Gebiedsaanwijzing` «verwijst naar» → `Locatie`
- 🔴 Verwijderd: `Instructieregel` «beschrijft gebiedsaanwijzing» → `Gebiedsaanwijzing`
- 🔴 Verwijderd: `Juridische Regel` «geldt voor» → `Activiteit`
- 🔴 Verwijderd: `Juridische Regel` «heeft idealisatie» → `Idealisatie`
- 🔴 Verwijderd: `Juridische Regel` «heeft thema» → `Thema`
- 🔴 Verwijderd: `Juridische Regel` «is opgenomen in» → `Regeltekst`
- 🔴 Verwijderd: `Juridische Regel` «werkingsgebied» → `Locatie`
- 🔴 Verwijderd: `Norm` «bevat» → `Normwaarde`
- 🔴 Verwijderd: `Normwaarde` «geldt voor» → `Locatie`
- 🔴 Verwijderd: `Omgevingswaarderegel` «beschrijft» → `Omgevingsnorm`
- 🔴 Verwijderd: `Omgevingswaarderegel` «beschrijft» → `Omgevingswaarde`
- 🔴 Verwijderd: `Regel voor Iedereen` «beschrijft activiteit» → `Activiteit`
- 🔴 Verwijderd: `Regel voor Iedereen` «beschrijft gebiedsaanwijzing» → `Gebiedsaanwijzing`
- 🔴 Verwijderd: `Regel voor Iedereen` «beschrijft norm» → `Omgevingsnorm`
- 🔴 Verwijderd: `Thema` «subthema» → `Thema`

#### Generalisaties

- 🔴 Verwijderd: `Beperkingsgebied` ⟶ `Gebiedsaanwijzing`
- 🔴 Verwijderd: `Functie` ⟶ `Gebiedsaanwijzing`
- 🔴 Verwijderd: `Instructieregel` ⟶ `Juridische Regel`
- 🔴 Verwijderd: `Omgevingsnorm` ⟶ `Norm`
- 🔴 Verwijderd: `Omgevingswaarde` ⟶ `Norm`
- 🔴 Verwijderd: `Omgevingswaarderegel` ⟶ `Juridische Regel`
- 🔴 Verwijderd: `Regel voor Iedereen` ⟶ `Juridische Regel`

<a id="structureel-delfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingomgevingswetmodel-omgevingswetmodel-toepasbare-regels"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Omgevingswet/Model Omgevingswet/Model Toepasbare Regels

#### Classes

##### `Conclusie` — 🔴 Verwijderd

##### `Indieningsvereisten` — 🔴 Verwijderd

##### `Maatregelen` — 🔴 Verwijderd

##### `Toepasbare Regel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheid` — Verwijderd
- 🔴 `datumEindeGeldigheid` — Verwijderd
- 🔴 `domein` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `soortAansluitpunt` — Verwijderd
- 🔴 `toestemming` — Verwijderd

##### `ToepasbareRegelBestand` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumEindeGeldigheid` — Verwijderd
- 🔴 `datumStart` — Verwijderd

##### `Uitvoeringsregel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `regel` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `Toepasbare Regel` «betreft» → `Activiteit`
- 🔴 Verwijderd: `Toepasbare Regel` «betreft» → `Locatie`
- 🔴 Verwijderd: `Toepasbare Regel` «heeft» → `ToepasbareRegelBestand`
- 🔴 Verwijderd: `Toepasbare Regel` «heeft» → `Uitvoeringsregel`
- 🔴 Verwijderd: `Toepasbare Regel` «komt voort uit» → `Juridische Regel`
- 🔴 Verwijderd: `ToepasbareRegelBestand` «bevat» → `Uitvoeringsregel`

#### Generalisaties

- 🔴 Verwijderd: `Conclusie` ⟶ `Toepasbare Regel`
- 🔴 Verwijderd: `Indieningsvereisten` ⟶ `Toepasbare Regel`
- 🔴 Verwijderd: `Maatregelen` ⟶ `Toepasbare Regel`

<a id="structureel-delfts-gemeentelijk-gegevensmodel9-interne-organisatiefinancienmodel-financien"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/Financien/Model Financien

#### Classes

##### `Activa` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Activasoort` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Bankafschrift` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datum` — Verwijderd
- 🔴 `nummer` — Verwijderd

##### `Bankafschriftregel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bedrag` — Verwijderd
- 🔴 `bij` — Verwijderd
- 🔴 `datum` — Verwijderd
- 🔴 `rekeningVan` — Verwijderd

##### `Bankrekening` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bank` — Verwijderd
- 🔴 `nummer` — Verwijderd
- 🔴 `tennaamstelling` — Verwijderd

##### `Batch` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datum` — Verwijderd
- 🔴 `nummer` — Verwijderd
- 🔴 `tijd` — Verwijderd

##### `Batchregel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bedrag` — Verwijderd
- 🔴 `datumBetaling` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `rekeningNaar` — Verwijderd
- 🔴 `rekeningVan` — Verwijderd

##### `Begroting` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `nummer` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Begrotingregel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `batenLasten` — Verwijderd
- 🔴 `bedrag` — Verwijderd
- 🔴 `soortRegel` — Verwijderd

##### `Debiteur` — 🔴 Verwijderd

##### `Doelstelling` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `nummer` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Factuur` — 🔴 Verwijderd

**Attributen:**

- 🔴 `betaalbaarPer` — Verwijderd
- 🔴 `betaaltermijn` — Verwijderd
- 🔴 `code` — Verwijderd
- 🔴 `datumFactuur` — Verwijderd
- 🔴 `factuurbedragBTW` — Verwijderd
- 🔴 `factuurbedragExclusiefBTW` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Factuurregel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aantal` — Verwijderd
- 🔴 `bedragBTW` — Verwijderd
- 🔴 `bedragExBTW` — Verwijderd
- 🔴 `BTWPercentage` — Verwijderd
- 🔴 `nummer` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Hoofdrekening` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `nummer` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `PIAHoofcategorieOmschrijving` — Verwijderd
- 🔴 `PIAHoofdcategorieCode` — Verwijderd
- 🔴 `subcode` — Verwijderd
- 🔴 `subcodeOmschrijving` — Verwijderd

##### `Hoofdstuk` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `nummer` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Inkooporder` — 🔴 Verwijderd

**Attributen:**

- 🔴 `artikelcode` — Verwijderd
- 🔴 `betalingMeerdereJaren` — Verwijderd
- 🔴 `betreft` — Verwijderd
- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumIngediend` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `goederencode` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `ordernummer` — Verwijderd
- 🔴 `saldo` — Verwijderd
- 🔴 `totaalNettoBedrag` — Verwijderd
- 🔴 `wijzeVanAanbesteden` — Verwijderd

##### `Kostenplaats` — 🔴 Verwijderd

**Attributen:**

- 🔴 `BTWCode` — Verwijderd
- 🔴 `BTWOmschrijving` — Verwijderd
- 🔴 `kostenplaatssoortCode` — Verwijderd
- 🔴 `kostenplaatssoortOmschrijving` — Verwijderd
- 🔴 `kostenplaatstypeCode` — Verwijderd
- 🔴 `kostenplaatstypeOmschrijving` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Mutatie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bedrag` — Verwijderd
- 🔴 `datum` — Verwijderd

##### `Opdrachtgever` — 🔴 Verwijderd

**Attributen:**

- 🔴 `clustercode` — Verwijderd
- 🔴 `clusterOmschrijving` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `nummer` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Opdrachtnemer` — 🔴 Verwijderd

**Attributen:**

- 🔴 `clustercode` — Verwijderd
- 🔴 `clustercodeOmschrijving` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `nummer` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Product` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `nummer` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Subrekening` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `nummer` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Taakveld` — 🔴 Verwijderd

**Attributen:**

- 🔴 `functiecodeIV3` — Verwijderd
- 🔴 `functieomschrijvingIV3` — Verwijderd
- 🔴 `hoofdfunctie` — Verwijderd
- 🔴 `hoofdfunctieOmschrijving` — Verwijderd
- 🔴 `subtaakveldCode` — Verwijderd
- 🔴 `subtaakveldOmschrijving` — Verwijderd
- 🔴 `taakveldcode` — Verwijderd
- 🔴 `taakveldOmschrijving` — Verwijderd

##### `Werkorder` — 🔴 Verwijderd

**Attributen:**

- 🔴 `code` — Verwijderd
- 🔴 `documentnummer` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `werkordertype` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `Activa` «is soort» → `Activasoort`
- 🔴 Verwijderd: `Bankafschrift` «heeft» → `Bankafschriftregel`
- 🔴 Verwijderd: `Bankafschriftregel` «leidt tot» → `Mutatie`
- 🔴 Verwijderd: `Bankrekening` «heeft» → `Bankafschrift`
- 🔴 Verwijderd: `Bankrekening` «naar» → `Betaling`
- 🔴 Verwijderd: `Bankrekening` «van» → `Betaling`
- 🔴 Verwijderd: `Batch` «heeft herkomst» → `ExterneBron`
- 🔴 Verwijderd: `Batch` «heeft» → `Batchregel`
- 🔴 Verwijderd: `Batchregel` «leidt tot» → `Mutatie`
- 🔴 Verwijderd: `Begroting` «heeft» → `Begrotingregel`
- 🔴 Verwijderd: `Begroting` «valt binnen» → `Periode`
- 🔴 Verwijderd: `Begrotingregel` «betreft» → `Doelstelling`
- 🔴 Verwijderd: `Begrotingregel` «betreft» → `Hoofdrekening`
- 🔴 Verwijderd: `Begrotingregel` «betreft» → `Hoofdstuk`
- 🔴 Verwijderd: `Begrotingregel` «betreft» → `Kostenplaats`
- 🔴 Verwijderd: `Begrotingregel` «betreft» → `Product`
- 🔴 Verwijderd: `Debiteur` «heeft» → `Factuur`
- 🔴 Verwijderd: `Doelstelling` «heeft» → `Product`
- 🔴 Verwijderd: `Doelstelling` «is opdrachtgever» → `Opdrachtgever`
- 🔴 Verwijderd: `Factuur` «crediteur» → `Leverancier`
- 🔴 Verwijderd: `Factuur` «gedekt via» → `Inkooporder`
- 🔴 Verwijderd: `Factuur` «heeft» → `Factuurregel`
- 🔴 Verwijderd: `Factuur` «schrijft op» → `Kostenplaats`
- 🔴 Verwijderd: `Factuurregel` «leidt tot» → `Mutatie`
- 🔴 Verwijderd: `Hoofdrekening` «heeft» → `Activa`
- 🔴 Verwijderd: `Hoofdrekening` «heeft» → `Kostenplaats`
- 🔴 Verwijderd: `Hoofdrekening` «heeft» → `Subrekening`
- 🔴 Verwijderd: `Hoofdrekening` «heeft» → `Werkorder`
- 🔴 Verwijderd: `Hoofdrekening` «valt binnen» → `Hoofdrekening`
- 🔴 Verwijderd: `Hoofdstuk` «binnen» → `Periode`
- 🔴 Verwijderd: `Hoofdstuk` «heeft» → `Doelstelling`
- 🔴 Verwijderd: `Inkooporder` «betreft» → `Contract`
- 🔴 Verwijderd: `Inkooporder` «gerelateerd» → `Inkooporder`
- 🔴 Verwijderd: `Inkooporder` «heeft» → `Inkooppakket`
- 🔴 Verwijderd: `Inkooporder` «hoort bij» → `Werkbon`
- 🔴 Verwijderd: `Inkooporder` «oorspronkelijk» → `Inkooporder`
- 🔴 Verwijderd: `Inkooporder` «verplichting aan» → `Leverancier`
- 🔴 Verwijderd: `Inkooporder` «wordt geschreven op» → `Hoofdrekening`
- 🔴 Verwijderd: `Kostenplaats` «heeft» → `Inkooporder`
- 🔴 Verwijderd: `Kostenplaats` «heeft» → `Subrekening`
- 🔴 Verwijderd: `Kostenplaats` «heeft» → `Taakveld`
- 🔴 Verwijderd: `Kostenplaats` «heeft» → `Vastgoedobject`
- 🔴 Verwijderd: `Kostenplaats` «heeft» → `Werkorder`
- 🔴 Verwijderd: `Kostenplaats` «is budgetverantwoordelijk» → `Opdrachtnemer`
- 🔴 Verwijderd: `Mutatie` «heeft betrekking op» → `Kostenplaats`
- 🔴 Verwijderd: `Mutatie` «naar» → `Hoofdrekening`
- 🔴 Verwijderd: `Mutatie` «van» → `Hoofdrekening`
- 🔴 Verwijderd: `Opdrachtgever` «is opdrachtgever» → `Product`
- 🔴 Verwijderd: `Opdrachtgever` «uitgevoerd door» → `Functie`
- 🔴 Verwijderd: `Opdrachtnemer` «is opdrachtnemer» → `Product`
- 🔴 Verwijderd: `Opdrachtnemer` «uitgevoerd door» → `Functie`
- 🔴 Verwijderd: `Product` «heeft» → `Kostenplaats`

#### Generalisaties

- 🔴 Verwijderd: `Debiteur` ⟶ `Rechtspersoon`

<a id="structureel-delfts-gemeentelijk-gegevensmodel9-interne-organisatiehrmodel-hr"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/HR/Model HR

#### Classes

##### `Beoordeling` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datum` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `oordeel` — Verwijderd

##### `Declaratie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bedrag` — Verwijderd
- 🔴 `betreft` — Verwijderd
- 🔴 `datumDeclaratie` — Verwijderd
- 🔴 `datumIndiening` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Declaratiesoort` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Dienstverband` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `periodiek` — Verwijderd
- 🔴 `salaris` — Verwijderd
- 🔴 `schaal` — Verwijderd
- 🔴 `urenPerWeek` — Verwijderd

##### `Disciplinaire Maatregel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumGeconstateerd` — Verwijderd
- 🔴 `datumOpgelegd` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `reden` — Verwijderd

##### `Formatieplaats` — 🔴 Verwijderd

**Attributen:**

- 🔴 `uren per week` — Verwijderd

##### `Functie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Code` — Verwijderd
- 🔴 `Naam` — Verwijderd
- 🔴 `Omschrijving` — Verwijderd
- 🔴 `Schaal` — Verwijderd
- 🔴 `Taken` — Verwijderd

##### `Functiehuis` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `GenotenOpleiding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `datumToewijzing` — Verwijderd
- 🔴 `prijs` — Verwijderd
- 🔴 `verrekenen` — Verwijderd

##### `Geweldsincident` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datum` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `type` — Verwijderd

##### `Individueel Keuzebudget` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bedrag` — Verwijderd
- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `datumToekenning` — Verwijderd

##### `Inzet` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBegin` — Verwijderd
- 🔴 `datumEinde` — Verwijderd
- 🔴 `percentage` — Verwijderd
- 🔴 `uren` — Verwijderd

##### `KeuzebudgetBesteding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bedrag` — Verwijderd
- 🔴 `datum` — Verwijderd

##### `KeuzebudgetBestedingsoort` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `NormProfiel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `code` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `schaal` — Verwijderd

##### `Onderwijsinstituut` — 🔴 Verwijderd

##### `Opleiding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `instituut` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `prijs` — Verwijderd

##### `OrganisatorischeEenheidHR` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `type` — Verwijderd

##### `Relatie` — 🔴 Verwijderd

##### `Rol` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBegin` — Verwijderd
- 🔴 `datumEinde` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Sollicitant` — 🔴 Verwijderd

##### `Sollicitatie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datum` — Verwijderd

##### `Sollicitatiegesprek` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aangenomen` — Verwijderd
- 🔴 `datum` — Verwijderd
- 🔴 `opmerkingen` — Verwijderd
- 🔴 `volgendGesprek` — Verwijderd

##### `SoortDisciplinaireMaatregel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Uren` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aantal` — Verwijderd

##### `Vacature` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumGesloten` — Verwijderd
- 🔴 `datumOpengesteld` — Verwijderd
- 🔴 `deeltijd` — Verwijderd
- 🔴 `extern` — Verwijderd
- 🔴 `intern` — Verwijderd
- 🔴 `vastedienst` — Verwijderd

##### `Verlof` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumAanvraag` — Verwijderd
- 🔴 `datumtijdEinde` — Verwijderd
- 🔴 `datumtijdStart` — Verwijderd
- 🔴 `datumToekenning` — Verwijderd
- 🔴 `goedgekeurd` — Verwijderd

##### `Verlofsoort` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Verzuim` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumtijdEinde` — Verwijderd
- 🔴 `datumtijdStart` — Verwijderd

##### `Verzuimsoort` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Werknemer` — 🔴 Verwijderd

**Attributen:**

- 🔴 `geboortedatum` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `voornaam` — Verwijderd
- 🔴 `woonplaats` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `Declaratie` «soort declaratie» → `Declaratiesoort`
- 🔴 Verwijderd: `Dienstverband` «dienstverband conform functie» → `Functie`
- 🔴 Verwijderd: `Dienstverband` «is op vestiging» → `VestigingVanZaakbehandelendeOrganisatie`
- 🔴 Verwijderd: `Dienstverband` «onderdeel van» → `OrganisatorischeEenheidHR`
- 🔴 Verwijderd: `Disciplinaire Maatregel` «soort maatregel» → `SoortDisciplinaireMaatregel`
- 🔴 Verwijderd: `Formatieplaats` «functie van formatieplaats» → `Functie`
- 🔴 Verwijderd: `Formatieplaats` «onderdeel van» → `OrganisatorischeEenheidHR`
- 🔴 Verwijderd: `Formatieplaats` «toegewezen aan» → `Dienstverband`
- 🔴 Verwijderd: `Functie` «gebaseerd op» → `NormProfiel`
- 🔴 Verwijderd: `GenotenOpleiding` «soort opleiding» → `Opleiding`
- 🔴 Verwijderd: `Individueel Keuzebudget` «besteding» → `KeuzebudgetBesteding`
- 🔴 Verwijderd: `Individueel Keuzebudget` «heeft individueel keuzebudget» → `Werknemer`
- 🔴 Verwijderd: `Inzet` «aantal volgens inzet» → `Dienstverband`
- 🔴 Verwijderd: `Inzet` «inzet bij» → `OrganisatorischeEenheidHR`
- 🔴 Verwijderd: `Inzet` «inzet voor functie» → `Functie`
- 🔴 Verwijderd: `KeuzebudgetBesteding` «soort besteding» → `KeuzebudgetBestedingsoort`
- 🔴 Verwijderd: `NormProfiel` «onderdeel van» → `Functiehuis`
- 🔴 Verwijderd: `Opleiding` «wordt gegeven door» → `Onderwijsinstituut`
- 🔴 Verwijderd: `Relatie` «is kind van» → `Werknemer`
- 🔴 Verwijderd: `Rol` «hoort bij» → `OrganisatorischeEenheidHR`
- 🔴 Verwijderd: `Sollicitant` «solliciteert op functie» → `Sollicitatie`
- 🔴 Verwijderd: `Sollicitatie` «op vacature» → `Vacature`
- 🔴 Verwijderd: `Sollicitatiegesprek` «doet sollicitatiegesprek» → `Werknemer`
- 🔴 Verwijderd: `Sollicitatiegesprek` «in kader van» → `Sollicitatie`
- 🔴 Verwijderd: `Sollicitatiegesprek` «kandidaat» → `Sollicitant`
- 🔴 Verwijderd: `Uren` «aantal volgens inzet» → `Dienstverband`
- 🔴 Verwijderd: `Vacature` «vacature bij functie» → `Functie`
- 🔴 Verwijderd: `Verlof` «soort verlof» → `Verlofsoort`
- 🔴 Verwijderd: `Verzuim` «soort verzuim» → `Verzuimsoort`
- 🔴 Verwijderd: `Werknemer` «Beoordeeld door» → `Beoordeling`
- 🔴 Verwijderd: `Werknemer` «beoordeling van» → `Beoordeling`
- 🔴 Verwijderd: `Werknemer` «dient in» → `Declaratie`
- 🔴 Verwijderd: `Werknemer` «heeft genoten» → `GenotenOpleiding`
- 🔴 Verwijderd: `Werknemer` «heeft maatregel» → `Disciplinaire Maatregel`
- 🔴 Verwijderd: `Werknemer` «heeft ondergaan» → `Geweldsincident`
- 🔴 Verwijderd: `Werknemer` «heeft verlof» → `Verlof`
- 🔴 Verwijderd: `Werknemer` «heeft verzuim» → `Verzuim`
- 🔴 Verwijderd: `Werknemer` «heeft» → `Rol`
- 🔴 Verwijderd: `Werknemer` «is partner van» → `Relatie`
- 🔴 Verwijderd: `Werknemer` «medewerker heeft dienstverband» → `Dienstverband`
- 🔴 Verwijderd: `Werknemer` «solliciteert» → `Sollicitatie`

#### Generalisaties

- 🔴 Verwijderd: `Onderwijsinstituut` ⟶ `NietNatuurlijkPersoon`
- 🔴 Verwijderd: `OrganisatorischeEenheidHR` ⟶ `OrganisatorischeEenheid`
- 🔴 Verwijderd: `Relatie` ⟶ `NatuurlijkPersoon`
- 🔴 Verwijderd: `Sollicitant` ⟶ `NatuurlijkPersoon`
- 🔴 Verwijderd: `Werknemer` ⟶ `Medewerker`

<a id="structureel-delfts-gemeentelijk-gegevensmodel9-interne-organisatieictdiagram"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/ICT/Diagram

#### Classes

##### `MIMDomein` — 🔴 Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodel9-interne-organisatieictmodel-ict"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/ICT/Model ICT

#### Classes

##### `Aanvraag` — 🔴 Verwijderd

##### `Applicatie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `applicatieURL` — Verwijderd
- 🔴 `beheerstatus` — Verwijderd
- 🔴 `beleidsdomein` — Verwijderd
- 🔴 `categorie` — Verwijderd
- 🔴 `guid` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `packagingstatus` — Verwijderd

##### `Attribuutsoort` — 🔴 Verwijderd

**Attributen:**

- 🔴 `authentiek` — Verwijderd
- 🔴 `datumOpname` — Verwijderd
- 🔴 `definitie` — Verwijderd
- 🔴 `domein` — Verwijderd
- 🔴 `ea_guid` — Verwijderd
- 🔴 `herkomst` — Verwijderd
- 🔴 `herkomstDefinitie` — Verwijderd
- 🔴 `id` — Verwijderd
- 🔴 `identificerend` — Verwijderd
- 🔴 `indicatieAfleidbaar` — Verwijderd
- 🔴 `indicatieMaterieleHistorie` — Verwijderd
- 🔴 `kardinaliteit` — Verwijderd
- 🔴 `lengte` — Verwijderd
- 🔴 `mogelijkGeenWaarde` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `patroon` — Verwijderd
- 🔴 `precisie` — Verwijderd
- 🔴 `stereotype` — Verwijderd
- 🔴 `toelichting` — Verwijderd

##### `Classificatie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bevatPersoonsgegevens` — Verwijderd
- 🔴 `gerelateerdPersoonsgegevens` — Verwijderd

##### `CMDB-item` — 🔴 Verwijderd

**Attributen:**

- 🔴 `beschrijving` — Verwijderd
- 🔴 `naam` — Verwijderd

##### `Database` — 🔴 Verwijderd

**Attributen:**

- 🔴 `architectuur` — Verwijderd
- 🔴 `databaseInstantie` — Verwijderd
- 🔴 `databaseVersie` — Verwijderd
- 🔴 `DBMS` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `OTAP` — Verwijderd
- 🔴 `vlan` — Verwijderd

##### `Datatype` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumOpname` — Verwijderd
- 🔴 `definitie` — Verwijderd
- 🔴 `domein` — Verwijderd
- 🔴 `ea_guid` — Verwijderd
- 🔴 `herkomst` — Verwijderd
- 🔴 `id` — Verwijderd
- 🔴 `kardinaliteit` — Verwijderd
- 🔴 `lengte` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `patroon` — Verwijderd
- 🔴 `toelichting` — Verwijderd

##### `Dienst` — 🔴 Verwijderd

##### `Domein/Taakveld` — 🔴 Verwijderd

##### `Externe Bron` — 🔴 Verwijderd

**Attributen:**

- 🔴 `guid` — Verwijderd
- 🔴 `naam` — Verwijderd

##### `Gegeven` — 🔴 Verwijderd

**Attributen:**

- 🔴 `alias` — Verwijderd
- 🔴 `ea_guid` — Verwijderd
- 🔴 `id` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `stereotype` — Verwijderd
- 🔴 `toelichting` — Verwijderd

##### `Generalisatie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumOpname` — Verwijderd
- 🔴 `definitie` — Verwijderd
- 🔴 `ea_guid` — Verwijderd
- 🔴 `herkomst` — Verwijderd
- 🔴 `herkomstDefinitie` — Verwijderd
- 🔴 `id` — Verwijderd
- 🔴 `indicatieMaterieleHistorie` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `toelichting` — Verwijderd

##### `Hardware` — 🔴 Verwijderd

##### `Inventaris` — 🔴 Verwijderd

##### `Koppeling` — 🔴 Verwijderd

**Attributen:**

- 🔴 `beschrijving` — Verwijderd
- 🔴 `direct` — Verwijderd
- 🔴 `toelichting` — Verwijderd

##### `Licentie` — 🔴 Verwijderd

##### `Linkbaar CMDB-item` — 🔴 Verwijderd

##### `Log` — 🔴 Verwijderd

**Attributen:**

- 🔴 `korteOmschrijving` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `tijd` — Verwijderd

##### `Melding` — 🔴 Verwijderd

##### `Nertwerkcomponent` — 🔴 Verwijderd

##### `Notitie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datum` — Verwijderd
- 🔴 `inhoud` — Verwijderd

##### `Objecttype` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumOpname` — Verwijderd
- 🔴 `definitie` — Verwijderd
- 🔴 `ea_guid` — Verwijderd
- 🔴 `herkomst` — Verwijderd
- 🔴 `herkomstDefinitie` — Verwijderd
- 🔴 `id` — Verwijderd
- 🔴 `indicatieAbstract` — Verwijderd
- 🔴 `kwaliteit` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `populatie` — Verwijderd
- 🔴 `stereotype` — Verwijderd
- 🔴 `supertype` — Verwijderd
- 🔴 `toelichting` — Verwijderd
- 🔴 `uniekeAanduiding` — Verwijderd

##### `Onderwerp` — 🔴 Verwijderd

##### `Package` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `proces` — Verwijderd
- 🔴 `project` — Verwijderd
- 🔴 `status` — Verwijderd
- 🔴 `toelichting` — Verwijderd

##### `Prijzenboek` — 🔴 Verwijderd

##### `Product` — 🔴 Verwijderd

##### `Relatiesoort` — 🔴 Verwijderd

**Attributen:**

- 🔴 `authentiek` — Verwijderd
- 🔴 `datumOpname` — Verwijderd
- 🔴 `definitie` — Verwijderd
- 🔴 `ea_guid` — Verwijderd
- 🔴 `herkomst` — Verwijderd
- 🔴 `herkomstDefinitie` — Verwijderd
- 🔴 `id` — Verwijderd
- 🔴 `indicatieAfleidbaar` — Verwijderd
- 🔴 `indicatieMaterieleHistorie` — Verwijderd
- 🔴 `kardinaliteit` — Verwijderd
- 🔴 `mogelijkGeenWaarde` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `toelichting` — Verwijderd
- 🔴 `unidirectioneel` — Verwijderd

##### `Server` — 🔴 Verwijderd

**Attributen:**

- 🔴 `actief` — Verwijderd
- 🔴 `IPAdres` — Verwijderd
- 🔴 `locatie` — Verwijderd
- 🔴 `organisatie` — Verwijderd
- 🔴 `serienummer` — Verwijderd
- 🔴 `serverID` — Verwijderd
- 🔴 `servertype` — Verwijderd
- 🔴 `vlan` — Verwijderd

##### `Software` — 🔴 Verwijderd

##### `Storing` — 🔴 Verwijderd

##### `Telefoniegegevens` — 🔴 Verwijderd

##### `Toegangsmiddel` — 🔴 Verwijderd

##### `Versie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aantal` — Verwijderd
- 🔴 `datumEindeSupport` — Verwijderd
- 🔴 `kosten` — Verwijderd
- 🔴 `licentie` — Verwijderd
- 🔴 `status` — Verwijderd
- 🔴 `versienummer` — Verwijderd

##### `Vervoersmiddel` — 🔴 Verwijderd

##### `Wijzigingsverzoek` — 🔴 Verwijderd

#### Enumeraties

##### `Applicatiecategorie` — 🔴 Verwijderd

**Literals:**

- 🔴 `BBA` — Verwijderd
- 🔴 `Beheer en systeem` — Verwijderd
- 🔴 `KA Basis` — Verwijderd
- 🔴 `KA Extra` — Verwijderd
- 🔴 `Kernapplicatie` — Verwijderd
- 🔴 `Niet ingedeeld` — Verwijderd

##### `Beheerstatus` — 🔴 Verwijderd

**Literals:**

- 🔴 `Beschikbaar Stellen` — Verwijderd
- 🔴 `Functioneel Ondersteunen` — Verwijderd
- 🔴 `Intern Ontwikkeld` — Verwijderd
- 🔴 `Niet ingedeeld` — Verwijderd
- 🔴 `Technisch ondersteunen` — Verwijderd
- 🔴 `Volledig Beheer` — Verwijderd

##### `Gebruikerrol` — 🔴 Verwijderd

**Literals:**

- 🔴 `Eigenaar` — Verwijderd
- 🔴 `Functioneel beheerder` — Verwijderd
- 🔴 `Gebruiker` — Verwijderd
- 🔴 `Gegevensbeheerder` — Verwijderd
- 🔴 `Superuser` — Verwijderd

##### `Packagingstatus` — 🔴 Verwijderd

**Literals:**

- 🔴 `API Mogelijk???` — Verwijderd
- 🔴 `Alleen Aanbieden` — Verwijderd
- 🔴 `Handmatig Installeren` — Verwijderd
- 🔴 `Niet aanbieden` — Verwijderd
- 🔴 `Niet ingedeeld` — Verwijderd
- 🔴 `Packagen en distribueren` — Verwijderd

##### `Servertypes` — 🔴 Verwijderd

**Literals:**

- 🔴 `niet virtueel` — Verwijderd
- 🔴 `virtueel` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `Applicatie` «bevat» → `Gegeven`
- 🔴 Verwijderd: `Applicatie` «heeft documenten» → `Document`
- 🔴 Verwijderd: `Applicatie` «heeft herkomst» → `Batch`
- 🔴 Verwijderd: `Applicatie` «heeft leverancier» → `Leverancier`
- 🔴 Verwijderd: `Applicatie` «heeft notities» → `Notitie`
- 🔴 Verwijderd: `Applicatie` «heeft packages» → `Package`
- 🔴 Verwijderd: `Applicatie` «heeft versies» → `Versie`
- 🔴 Verwijderd: `Attribuutsoort` «heeft» → `Datatype`
- 🔴 Verwijderd: `CMDB-item ` «heeft changelog» → `Log`
- 🔴 Verwijderd: `Database` «server van database» → `Server`
- 🔴 Verwijderd: `Dienst` «betreft» → `Product`
- 🔴 Verwijderd: `Dienst` «heeft» → `Onderwerp`
- 🔴 Verwijderd: `Dienst` «start» → `Zaaktype`
- 🔴 Verwijderd: `Dienst` «valt binnen» → `Domein/Taakveld`
- 🔴 Verwijderd: `Domein/Taakveld` «valt binnen» → `Onderwerp`
- 🔴 Verwijderd: `Domein/Taakveld` «valt binnen» → `Product`
- 🔴 Verwijderd: `Externe Bron` «levert» → `Gegeven`
- 🔴 Verwijderd: `Gegeven` «geclassificeerd als» → `Classificatie`
- 🔴 Verwijderd: `Gegeven` «gedefinieerd door» → `Objecttype`
- 🔴 Verwijderd: `Koppeling` «link naar» → `Linkbaar CMDB-item`
- 🔴 Verwijderd: `Linkbaar CMDB-item` «link van» → `Koppeling`
- 🔴 Verwijderd: `Notitie` «auteur» → `Medewerker`
- 🔴 Verwijderd: `Objecttype` «bezit» → `Attribuutsoort`
- 🔴 Verwijderd: `Objecttype` «bezit» → `Relatiesoort`
- 🔴 Verwijderd: `Objecttype` → `Generalisatie`
- 🔴 Verwijderd: `Prijzenboek` «heeft prijs» → `Product`
- 🔴 Verwijderd: `Product` «betreft» → `Zaaktype`
- 🔴 Verwijderd: `Relatiesoort` «gerelateerdObjecttype» → `Objecttype`
- 🔴 Verwijderd: `Server` «heeft leverancier» → `Leverancier`

#### Generalisaties

- 🔴 Verwijderd: `Applicatie` ⟶ `Linkbaar CMDB-item`
- 🔴 Verwijderd: `Database` ⟶ `Linkbaar CMDB-item`
- 🔴 Verwijderd: `Hardware` ⟶ `CMDB-item `
- 🔴 Verwijderd: `Inventaris` ⟶ `CMDB-item `
- 🔴 Verwijderd: `Licentie` ⟶ `CMDB-item `
- 🔴 Verwijderd: `Linkbaar CMDB-item` ⟶ `CMDB-item `
- 🔴 Verwijderd: `Nertwerkcomponent` ⟶ `CMDB-item `
- 🔴 Verwijderd: `Server` ⟶ `Linkbaar CMDB-item`
- 🔴 Verwijderd: `Software` ⟶ `CMDB-item `
- 🔴 Verwijderd: `Toegangsmiddel` ⟶ `CMDB-item `
- 🔴 Verwijderd: `Vervoersmiddel` ⟶ `CMDB-item `

<a id="structureel-delfts-gemeentelijk-gegevensmodel9-interne-organisatieinkoopmodel-inkoop"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/Inkoop/Model Inkoop

#### Classes

##### `Aanbesteding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumPublicatie` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `digitaal` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `procedure` — Verwijderd
- 🔴 `referentienummer` — Verwijderd
- 🔴 `scoreMaximaal` — Verwijderd
- 🔴 `status` — Verwijderd
- 🔴 `tendernedKenmerk` — Verwijderd
- 🔴 `type` — Verwijderd
- 🔴 `volgendeSluiting` — Verwijderd

##### `Aanbesteding Inhuur` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aanvraagGesloten` — Verwijderd
- 🔴 `aanvraagnummer` — Verwijderd
- 🔴 `datumCreatie` — Verwijderd
- 🔴 `datumOpeningKluis` — Verwijderd
- 🔴 `datumSluiting` — Verwijderd
- 🔴 `datumVerzending` — Verwijderd
- 🔴 `fase` — Verwijderd
- 🔴 `hoogsteTarief` — Verwijderd
- 🔴 `laagsteTarief` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `perceel` — Verwijderd
- 🔴 `procedure` — Verwijderd
- 🔴 `projectnaam` — Verwijderd
- 🔴 `projectreferentie` — Verwijderd
- 🔴 `publicatie` — Verwijderd
- 🔴 `referentie` — Verwijderd
- 🔴 `status` — Verwijderd
- 🔴 `titel` — Verwijderd
- 🔴 `type` — Verwijderd

##### `Aankondiging` — 🔴 Verwijderd

**Attributen:**

- 🔴 `beschrijving` — Verwijderd
- 🔴 `categorie` — Verwijderd
- 🔴 `datum` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `type` — Verwijderd

##### `Aanvraag Inkooporder` — 🔴 Verwijderd

**Attributen:**

- 🔴 `betalingOverMeerJaren` — Verwijderd
- 🔴 `correspondentienummer` — Verwijderd
- 🔴 `inhuurAnders` — Verwijderd
- 🔴 `leveringOfDienst` — Verwijderd
- 🔴 `nettoTotaalBedrag` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `onderwerp` — Verwijderd
- 🔴 `reactie` — Verwijderd
- 🔴 `status` — Verwijderd
- 🔴 `wijzeVanInhuur` — Verwijderd

##### `Categorie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `code` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Contract` — 🔴 Verwijderd

**Attributen:**

- 🔴 `autorisatiegroep` — Verwijderd
- 🔴 `beschrijving` — Verwijderd
- 🔴 `categorie` — Verwijderd
- 🔴 `classificatie` — Verwijderd
- 🔴 `contractRevisie` — Verwijderd
- 🔴 `datumCreatie` — Verwijderd
- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `groep` — Verwijderd
- 🔴 `internContractID` — Verwijderd
- 🔴 `internContractRevisie` — Verwijderd
- 🔴 `opmerkingen` — Verwijderd
- 🔴 `status` — Verwijderd
- 🔴 `type` — Verwijderd
- 🔴 `voorwaarde` — Verwijderd
- 🔴 `zoekwoorden` — Verwijderd

##### `CPV-code` — 🔴 Verwijderd

**Attributen:**

- 🔴 `code` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `FormulierInhuur` — 🔴 Verwijderd

**Attributen:**

- 🔴 `akkoordFinancieelAdviseur` — Verwijderd
- 🔴 `akkoordHRAdviseur` — Verwijderd
- 🔴 `datumIngangInhuur` — Verwijderd
- 🔴 `functienaamInhuur` — Verwijderd

##### `FormulierVerlengingInhuur` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumEindeNieuw` — Verwijderd
- 🔴 `indicatieRedenInhuurGewijzigd` — Verwijderd
- 🔴 `indicatieVerhogenInkooporder` — Verwijderd
- 🔴 `toelichting` — Verwijderd

##### `Gunning` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bericht` — Verwijderd
- 🔴 `datumGunning` — Verwijderd
- 🔴 `datumPublicatie` — Verwijderd
- 🔴 `datumVoorlopigeGunning` — Verwijderd
- 🔴 `gegundePrijs` — Verwijderd

##### `Inkooppakket` — 🔴 Verwijderd

**Attributen:**

- 🔴 `code` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `type` — Verwijderd

##### `Inschrijving` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datum` — Verwijderd
- 🔴 `prijs` — Verwijderd
- 🔴 `score` — Verwijderd

##### `Kandidaat` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumIngestuurd` — Verwijderd

##### `Kwalificatie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `eindeGeldigheid` — Verwijderd
- 🔴 `startGeldigheid` — Verwijderd

##### `Leverancier` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `nummer` — Verwijderd

##### `Offerte` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumOfferte` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `prijs` — Verwijderd

##### `Offerteaanvraag` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumAanvraag` — Verwijderd
- 🔴 `datumSluiting` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `SelectietabelAanbesteding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aanbestedingsoort` — Verwijderd
- 🔴 `drempelbedragTot` — Verwijderd
- 🔴 `drempelbedragVanaf` — Verwijderd
- 🔴 `opdrachtcategorie` — Verwijderd
- 🔴 `openbaar` — Verwijderd

##### `StartformulierAanbesteden` — 🔴 Verwijderd

**Attributen:**

- 🔴 `beoogdeLooptijd` — Verwijderd
- 🔴 `beoogdeTotaleOpdrachtwaarde` — Verwijderd
- 🔴 `indicatieAanvullendeOpdrachtLeverancier` — Verwijderd
- 🔴 `indicatieBeoogdeAanbestedingOnderhands` — Verwijderd
- 🔴 `indicatieBeoogdeProcKomtOvereen` — Verwijderd
- 🔴 `indicatieEenmaligeLos` — Verwijderd
- 🔴 `indicatieMeerjarigeRaamovereenkomst` — Verwijderd
- 🔴 `indicatieMeerjarigRepeterend` — Verwijderd
- 🔴 `indicatorOverkoepelendProject` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `opdrachtcategorie` — Verwijderd
- 🔴 `opdrachtsoort` — Verwijderd
- 🔴 `toelichtingAanvullendeOpdracht` — Verwijderd
- 🔴 `toelichtingEenmaligOfRepeterend` — Verwijderd

##### `Uitnodiging` — 🔴 Verwijderd

**Attributen:**

- 🔴 `afgewezen` — Verwijderd
- 🔴 `datum` — Verwijderd
- 🔴 `geaccepteerd` — Verwijderd

#### Enumeraties

##### `Aanbestedingsoort` — 🔴 Verwijderd

**Literals:**

- 🔴 `Enkelvoudig onderhands` — Verwijderd
- 🔴 `Europese aanbesteding` — Verwijderd
- 🔴 `Meervoudig onderhands` — Verwijderd
- 🔴 `Nationale aanbesteding` — Verwijderd

##### `Inkooprol` — 🔴 Verwijderd

**Literals:**

- 🔴 `Beheerder` — Verwijderd
- 🔴 `Eigenaar` — Verwijderd
- 🔴 `Inkoopadviseur` — Verwijderd

##### `Opdrachtcategorie` — 🔴 Verwijderd

**Literals:**

- 🔴 `Diensten - regulier` — Verwijderd
- 🔴 `Diensten - sociale of specifieke diensten` — Verwijderd
- 🔴 `Leveringen` — Verwijderd
- 🔴 `Werken` — Verwijderd

##### `Opdrachtsoort` — 🔴 Verwijderd

**Literals:**

- 🔴 `Inhuur extern personeel` — Verwijderd
- 🔴 `Opdracht voor levering, diensten of werken` — Verwijderd
- 🔴 `Subsidies` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `Aanbesteding Inhuur` «eigenaar» → `Medewerker`
- 🔴 Verwijderd: `Aanbesteding Inhuur` «mondt uit» → `Gunning`
- 🔴 Verwijderd: `Aanbesteding Inhuur` «valt binnen» → `Categorie`
- 🔴 Verwijderd: `Aanbesteding Inhuur` «valt onder» → `CPV-code`
- 🔴 Verwijderd: `Aanbesteding` «betreft» → `Zaak`
- 🔴 Verwijderd: `Aanbesteding` «mondt uit» → `Gunning`
- 🔴 Verwijderd: `Aanbesteding` «procesleider» → `Medewerker`
- 🔴 Verwijderd: `Aankondiging` «mondt uit» → `Aanbesteding`
- 🔴 Verwijderd: `Aanvraag Inkooporder` «afgehandeld door» → `OrganisatorischeEenheid`
- 🔴 Verwijderd: `Aanvraag Inkooporder` «afhandeling» → `Zaak`
- 🔴 Verwijderd: `Aanvraag Inkooporder` «betreft» → `Contract`
- 🔴 Verwijderd: `Aanvraag Inkooporder` «betreft» → `Leverancier`
- 🔴 Verwijderd: `Aanvraag Inkooporder` «ingediend bij» → `Medewerker`
- 🔴 Verwijderd: `Aanvraag Inkooporder` «mondt uit in» → `Inkooporder`
- 🔴 Verwijderd: `Contract` «bevat» → `Tarief`
- 🔴 Verwijderd: `Contract` «bovenliggend» → `Contract`
- 🔴 Verwijderd: `CPV-code` «valt onder» → `Aanbesteding`
- 🔴 Verwijderd: `FormulierInhuur` «aanvrager» → `Medewerker`
- 🔴 Verwijderd: `FormulierInhuur` «heeft» → `Kostenplaats`
- 🔴 Verwijderd: `FormulierInhuur` «mondt uit in» → `Aanbesteding Inhuur`
- 🔴 Verwijderd: `FormulierVerlengingInhuur` «aanvrager» → `Medewerker`
- 🔴 Verwijderd: `FormulierVerlengingInhuur` «betreft» → `Inkooporder`
- 🔴 Verwijderd: `FormulierVerlengingInhuur` «betreft» → `Medewerker`
- 🔴 Verwijderd: `FormulierVerlengingInhuur` «ingehuurd via» → `Leverancier`
- 🔴 Verwijderd: `Gunning` «betreft» → `Inschrijving`
- 🔴 Verwijderd: `Gunning` «betreft» → `Kandidaat`
- 🔴 Verwijderd: `Gunning` «betreft» → `Offerte`
- 🔴 Verwijderd: `Gunning` «inhuur» → `Medewerker`
- 🔴 Verwijderd: `Inkooppakket` «heeft» → `CPV-code`
- 🔴 Verwijderd: `Inschrijving` «betreft» → `Aanbesteding`
- 🔴 Verwijderd: `Kandidaat` «betreft» → `NatuurlijkPersoon`
- 🔴 Verwijderd: `Kandidaat` «ingediend voor» → `Aanbesteding Inhuur`
- 🔴 Verwijderd: `Kwalificatie` «betreft» → `Aanbesteding`
- 🔴 Verwijderd: `Leverancier` «biedt aan» → `Kandidaat`
- 🔴 Verwijderd: `Leverancier` «contractant» → `Contract`
- 🔴 Verwijderd: `Leverancier` «gekwalificeerd» → `Categorie`
- 🔴 Verwijderd: `Leverancier` «heeft gekwalificeerd» → `Aanbesteding Vastgoed`
- 🔴 Verwijderd: `Leverancier` «heeft» → `Inschrijving`
- 🔴 Verwijderd: `Leverancier` «heeft» → `Kwalificatie`
- 🔴 Verwijderd: `Leverancier` «voert werk uit conform» → `Werkbon`
- 🔴 Verwijderd: `Offerte` «betreft» → `Aanbesteding`
- 🔴 Verwijderd: `Offerte` «ingediend door» → `Leverancier`
- 🔴 Verwijderd: `Offerteaanvraag` «betreft» → `Aanbesteding`
- 🔴 Verwijderd: `Offerteaanvraag` «gericht aan» → `Leverancier`
- 🔴 Verwijderd: `StartformulierAanbesteden` «betreft» → `Zaak`
- 🔴 Verwijderd: `StartformulierAanbesteden` «mondt uit» → `Aanbesteding`
- 🔴 Verwijderd: `StartformulierAanbesteden` «mondt uit» → `Aankondiging`
- 🔴 Verwijderd: `Uitnodiging` «betreft» → `Aanbesteding Inhuur`
- 🔴 Verwijderd: `Uitnodiging` «gericht aan» → `Leverancier`

#### Generalisaties

- 🔴 Verwijderd: `Leverancier` ⟶ `Rechtspersoon`

<a id="structureel-delfts-gemeentelijk-gegevensmodel9-interne-organisatieorganisatie-indelingmodel-organisatie"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/Organisatie-indeling/Model Organisatie

#### Classes

##### `Programma` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd

##### `Project` — 🔴 Verwijderd

#### Associaties

- 🔴 Verwijderd: `Programma` «binnen programma» → `Plan`
- 🔴 Verwijderd: `Project` «heeft» → `Kostenplaats`

<a id="structureel-delfts-gemeentelijk-gegevensmodel9-interne-organisatiesubsidiesmodel-subsidies"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/Subsidies/Model Subsidies

#### Classes

##### `Betaalmoment` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bedrag` — Verwijderd
- 🔴 `datum` — Verwijderd
- 🔴 `voorschot` — Verwijderd

##### `Rapportagemoment` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datum` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `termijn` — Verwijderd

##### `Sector` — 🔴 Verwijderd

**Attributen:**

- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Subsidie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `accountantscontrole` — Verwijderd
- 🔴 `coFinanciering` — Verwijderd
- 🔴 `datumBehandeltermijn` — Verwijderd
- 🔴 `datumBewaartermijn` — Verwijderd
- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `datumSubsidievaststelling` — Verwijderd
- 🔴 `datumVerzendingEindeafrekening` — Verwijderd
- 🔴 `deadlineIndiening` — Verwijderd
- 🔴 `doelstelling` — Verwijderd
- 🔴 `gerealiseerdeProjectkosten` — Verwijderd
- 🔴 `hoogteSubsidie` — Verwijderd
- 🔴 `niveau` — Verwijderd
- 🔴 `onderwerp` — Verwijderd
- 🔴 `ontvangenBedrag` — Verwijderd
- 🔴 `opmerkingen` — Verwijderd
- 🔴 `opmerkingenVoorschotten` — Verwijderd
- 🔴 `prestatiesubsidie` — Verwijderd
- 🔴 `socialReturnBedrag` — Verwijderd
- 🔴 `socialReturnNagekomen` — Verwijderd
- 🔴 `socialReturnVerplichting` — Verwijderd
- 🔴 `status` — Verwijderd
- 🔴 `subsidiebedrag` — Verwijderd
- 🔴 `subsidiesoort` — Verwijderd
- 🔴 `subsidievaststellingBedrag` — Verwijderd
- 🔴 `uitgaandeSubsidie` — Verwijderd
- 🔴 `verantwoordenOp` — Verwijderd

##### `Subsidieaanvraag` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aangevraagdBedrag` — Verwijderd
- 🔴 `datumIndiening` — Verwijderd
- 🔴 `kenmerk` — Verwijderd
- 🔴 `ontvangstbevestiging` — Verwijderd
- 🔴 `verwachteBeschikking` — Verwijderd

##### `Subsidiebeschikking` — 🔴 Verwijderd

**Attributen:**

- 🔴 `beschikkingsnummer` — Verwijderd
- 🔴 `beschiktBedrag` — Verwijderd
- 🔴 `besluit` — Verwijderd
- 🔴 `internKenmerk` — Verwijderd
- 🔴 `kenmerk` — Verwijderd
- 🔴 `ontvangen` — Verwijderd
- 🔴 `opmerkingen` — Verwijderd

##### `Subsidiecomponent` — 🔴 Verwijderd

**Attributen:**

- 🔴 `gereserveerdBedrag` — Verwijderd
- 🔴 `toegekendBedrag` — Verwijderd

##### `Subsidieprogramma` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `programmabegroting` — Verwijderd

##### `Taak` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `taakomschrijving` — Verwijderd
- 🔴 `termijn` — Verwijderd

#### Enumeraties

##### `Subsidieniveau` — 🔴 Verwijderd

**Literals:**

- 🔴 `Europees` — Verwijderd
- 🔴 `Gemeente` — Verwijderd
- 🔴 `Nationaal` — Verwijderd
- 🔴 `Provincie` — Verwijderd
- 🔴 `Regionaal` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `Rapportagemoment` «heeft» → `Document`
- 🔴 Verwijderd: `Subsidie` «behandelaar» → `Medewerker`
- 🔴 Verwijderd: `Subsidie` «heeft» → `Document`
- 🔴 Verwijderd: `Subsidie` «heeft» → `Kostenplaats`
- 🔴 Verwijderd: `Subsidie` «heeft» → `Rapportagemoment`
- 🔴 Verwijderd: `Subsidie` «heeft» → `Taak`
- 🔴 Verwijderd: `Subsidie` «heeft» → `Zaak`
- 🔴 Verwijderd: `Subsidie` «valt binnen» → `Sector`
- 🔴 Verwijderd: `Subsidie` «verstrekker» → `Rechtspersoon`
- 🔴 Verwijderd: `Subsidieaanvraag` «betreft» → `Subsidie`
- 🔴 Verwijderd: `Subsidieaanvraag` «mondt uit» → `Subsidiebeschikking`
- 🔴 Verwijderd: `Subsidiebeschikking` «betreft» → `Subsidie`
- 🔴 Verwijderd: `Subsidiecomponent` «heeft» → `Betaalmoment`
- 🔴 Verwijderd: `Subsidiecomponent` «heeft» → `Kostenplaats`
- 🔴 Verwijderd: `Subsidieprogramma` «gaat over» → `Subsidie`
- 🔴 Verwijderd: `Subsidieprogramma` «verantwoordelijk voor» → `OrganisatorischeEenheid`
- 🔴 Verwijderd: `Taak` «projectleider» → `Rechtspersoon`

<a id="structureel-delfts-gemeentelijk-gegevensmodel9-interne-organisatievastgoedmodel-vastgoed"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/Vastgoed/Model Vastgoed

#### Classes

##### `Aanbesteding Vastgoed` — 🔴 Verwijderd

##### `Adresaanduiding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `adres` — Verwijderd

##### `Bouwdeel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `code` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `Bouwdeelelement` — 🔴 Verwijderd

**Attributen:**

- 🔴 `code` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `CultuurOnbebouwd` — 🔴 Verwijderd

**Attributen:**

- 🔴 `cultuurcodeOnbebouwd` — Verwijderd

##### `Eigenaar` — 🔴 Verwijderd

##### `Gebruiksdoel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `gebruiksdoelGebouwdObject` — Verwijderd

##### `Huurder` — 🔴 Verwijderd

##### `Inspectie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bevindingen` — Verwijderd
- 🔴 `datum` — Verwijderd

##### `KpBetrokkenBij` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheid` — Verwijderd
- 🔴 `datumEindeGeldigheid` — Verwijderd

##### `KpOnstaanUit` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheid` — Verwijderd
- 🔴 `datumEindeGeldigheid` — Verwijderd

##### `LocatieaanduidingWozObject` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheid` — Verwijderd
- 🔴 `datumEindeGeldigheid` — Verwijderd
- 🔴 `locatieOmschrijving` — Verwijderd
- 🔴 `primair` — Verwijderd

##### `Locatieonroerendezaak` — 🔴 Verwijderd

**Attributen:**

- 🔴 `adrestype` — Verwijderd
- 🔴 `cultuurcodeBebouwd` — Verwijderd
- 🔴 `datumBeginGeldigheid` — Verwijderd
- 🔴 `datumEindeGeldigheid` — Verwijderd
- 🔴 `geometrie` — Verwijderd
- 🔴 `locatieOmschrijving` — Verwijderd

##### `MJOP` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datum` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `MJOP-Item` — 🔴 Verwijderd

**Attributen:**

- 🔴 `code` — Verwijderd
- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumOpzeggingAanbieder` — Verwijderd
- 🔴 `datumOpzeggingOntvanger` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `kosten` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `opzegtermijnAanbieder` — Verwijderd
- 🔴 `opzegtermijnOntvanger` — Verwijderd

##### `NADAanvullingBRP` — 🔴 Verwijderd

**Attributen:**

- 🔴 `opmerkingen` — Verwijderd

##### `Objectrelatie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `rol` — Verwijderd

##### `Offerte` — 🔴 Verwijderd

##### `Pachter` — 🔴 Verwijderd

##### `Prijzenboekitem` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumEindeGeldigheid` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `prijs` — Verwijderd
- 🔴 `verrichting` — Verwijderd

##### `Vastgoed Contract` — 🔴 Verwijderd

**Attributen:**

- 🔴 `beschrijving` — Verwijderd
- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `identificatie` — Verwijderd
- 🔴 `maandbedrag` — Verwijderd
- 🔴 `opzegtermijn` — Verwijderd
- 🔴 `status` — Verwijderd
- 🔴 `type` — Verwijderd

##### `Vastgoedcontractregel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bedrag` — Verwijderd
- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `frequentie` — Verwijderd
- 🔴 `identificatie` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `status` — Verwijderd
- 🔴 `type` — Verwijderd

##### `Vastgoedobject` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aantalEtages` — Verwijderd
- 🔴 `aantalParkeerplaatsen` — Verwijderd
- 🔴 `aantalRioleringen` — Verwijderd
- 🔴 `adresaanduiding` — Verwijderd
- 🔴 `afgekochteErfpacht` — Verwijderd
- 🔴 `afgesprokenConditiescore` — Verwijderd
- 🔴 `afkoopwaarde` — Verwijderd
- 🔴 `asbestrapportageAanwezig` — Verwijderd
- 🔴 `bedragAankoop` — Verwijderd
- 🔴 `bestemmingsplan` — Verwijderd
- 🔴 `boekwaarde` — Verwijderd
- 🔴 `bouwjaar` — Verwijderd
- 🔴 `bouwwerk` — Verwijderd
- 🔴 `bovenliggendNiveau` — Verwijderd
- 🔴 `bovenliggendNiveaucode` — Verwijderd
- 🔴 `brutoVloeroppervlakte` — Verwijderd
- 🔴 `CO2Uitstoot` — Verwijderd
- 🔴 `conditiescore` — Verwijderd
- 🔴 `datumAfstoten` — Verwijderd
- 🔴 `datumBerekeningOppervlak` — Verwijderd
- 🔴 `datumEigendom` — Verwijderd
- 🔴 `datumVerkoop` — Verwijderd
- 🔴 `deelportefeuille` — Verwijderd
- 🔴 `energiekosten` — Verwijderd
- 🔴 `energielabel` — Verwijderd
- 🔴 `energieverbruik` — Verwijderd
- 🔴 `fiscaleWaarde` — Verwijderd
- 🔴 `foto` — Verwijderd
- 🔴 `gearchiveerd` — Verwijderd
- 🔴 `herbouwwaarde` — Verwijderd
- 🔴 `hoofdstuk` — Verwijderd
- 🔴 `identificatie` — Verwijderd
- 🔴 `jaarLaatsteRenovatie` — Verwijderd
- 🔴 `kostenplaats` — Verwijderd
- 🔴 `locatie` — Verwijderd
- 🔴 `marktwaarde` — Verwijderd
- 🔴 `monument` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `objectstatus` — Verwijderd
- 🔴 `objectstatuscode` — Verwijderd
- 🔴 `objecttype` — Verwijderd
- 🔴 `objecttypecode` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `onderhoudscategorie` — Verwijderd
- 🔴 `oppervlakteKantoor` — Verwijderd
- 🔴 `portefeuille` — Verwijderd
- 🔴 `portefeuillecode` — Verwijderd
- 🔴 `provincie` — Verwijderd
- 🔴 `toelichting` — Verwijderd
- 🔴 `verhuurbaarVloeroppervlak` — Verwijderd
- 🔴 `verkoopbaarheid` — Verwijderd
- 🔴 `verkoopbedrag` — Verwijderd
- 🔴 `verzekerdeWaarde` — Verwijderd
- 🔴 `waardeGrond` — Verwijderd
- 🔴 `waardeOpstal` — Verwijderd
- 🔴 `wijk` — Verwijderd
- 🔴 `WOZWaarde` — Verwijderd

##### `Verhuurbaar Eenheid` — 🔴 Verwijderd

**Attributen:**

- 🔴 `adres` — Verwijderd
- 🔴 `afmeting` — Verwijderd
- 🔴 `bezetting` — Verwijderd
- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `datumWerkelijkBegin` — Verwijderd
- 🔴 `datumWerkelijkEinde` — Verwijderd
- 🔴 `huurprijs` — Verwijderd
- 🔴 `identificatie` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `nettoOmtrek` — Verwijderd
- 🔴 `nettoOppervlak` — Verwijderd
- 🔴 `opmerkingen` — Verwijderd
- 🔴 `type` — Verwijderd

##### `Werkbon` — 🔴 Verwijderd

##### `WOZ-Belang` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheid` — Verwijderd
- 🔴 `datumEindeGeldigheid` — Verwijderd
- 🔴 `eigenaarGebruiker` — Verwijderd

##### `Zakelijk Recht` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `kosten` — Verwijderd
- 🔴 `soort` — Verwijderd

#### Enumeraties

##### `aanduidingEigenaarGebruiker` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `eigenaar` — Verwijderd
- 🔴 `eigenaar-gebruiker` — Verwijderd
- 🔴 `gebruiker` — Verwijderd
- 🔴 `medebelanghebbende` — Verwijderd

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

##### `Energielabel Gebouwen` — 🔴 Verwijderd

**Literals:**

- 🔴 `A` — Verwijderd
- 🔴 `A+` — Verwijderd
- 🔴 `A++` — Verwijderd
- 🔴 `B` — Verwijderd
- 🔴 `C` — Verwijderd
- 🔴 `D` — Verwijderd
- 🔴 `E` — Verwijderd
- 🔴 `F` — Verwijderd
- 🔴 `G` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `gebruiksdoel` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `bijeenkomstfunctie` — Verwijderd
- 🔴 `celfunctie` — Verwijderd
- 🔴 `gezondheidszorgfunctie` — Verwijderd
- 🔴 `industriefunctie` — Verwijderd
- 🔴 `kantoorfunctie` — Verwijderd
- 🔴 `logiesfunctie` — Verwijderd
- 🔴 `onderwijsfunctie` — Verwijderd
- 🔴 `overige gebruiksfunctie` — Verwijderd
- 🔴 `sportfunctie` — Verwijderd
- 🔴 `winkelfunctie` — Verwijderd
- 🔴 `woonfunctie` — Verwijderd

##### `Monumenttypering` — 🔴 Verwijderd

**Literals:**

- 🔴 `Beschermd Stadsgezicht` — Verwijderd
- 🔴 `Deels rijksmonument` — Verwijderd
- 🔴 `Geen monument` — Verwijderd
- 🔴 `Gemeentelijk monument` — Verwijderd
- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Rijksmonument` — Verwijderd

##### `NEN2767 Conditiescore` — 🔴 Verwijderd

**Literals:**

- 🔴 `1` — Verwijderd
- 🔴 `2` — Verwijderd
- 🔴 `3` — Verwijderd
- 🔴 `4` — Verwijderd
- 🔴 `5` — Verwijderd
- 🔴 `6` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `Objectrelatierol` — 🔴 Verwijderd

**Literals:**

- 🔴 `accountmanager` — Verwijderd
- 🔴 `accountmanager verkoop (jurist)` — Verwijderd
- 🔴 `beheerder` — Verwijderd
- 🔴 `service provider` — Verwijderd
- 🔴 `taxateur` — Verwijderd
- 🔴 `technisch beheerder` — Verwijderd

##### `TypeAdresseerbaarObject` — 🔴 Verwijderd

**Literals:**

- 🔴 `KADbinnenlandsadres` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Ligplaats` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Standplaats` — Verwijderd
- 🔴 `Verblijfsobject` — Verwijderd

##### `Zakelijkrecht` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `eigendom` — Verwijderd
- 🔴 `huur` — Verwijderd
- 🔴 `pacht` — Verwijderd
- 🔴 `recht van opstal` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `Aanbesteding Vastgoed` «uitvoering van» → `Werkbon`
- 🔴 Verwijderd: `Bouwdeel` «bestaat uit» → `Bouwdeelelement`
- 🔴 Verwijderd: `Huurder` «heeft huurrecht» → `Zakelijk Recht`
- 🔴 Verwijderd: `Inspectie` «leidt tot» → `MJOP`
- 🔴 Verwijderd: `KpBetrokkenBij` «is betrokken bij» → `ZakelijkRecht`
- 🔴 Verwijderd: `KpBetrokkenBij` → `Appartementsrechtsplitsing`
- 🔴 Verwijderd: `KpOnstaanUit` «is ontstaan uit» → `ZakelijkRecht`
- 🔴 Verwijderd: `KpOnstaanUit` → `Appartementsrechtsplitsing`
- 🔴 Verwijderd: `LocatieaanduidingWozObject` «heeft» → `WOZ-object`
- 🔴 Verwijderd: `Locatieonroerendezaak` «heeft Adresseerbaar object» → `AdresseerbaarObject`
- 🔴 Verwijderd: `Locatieonroerendezaak` «heeft adres» → `KadastraleOnroerendeZaak`
- 🔴 Verwijderd: `MJOP-Item` «betreft» → `Bouwdeel`
- 🔴 Verwijderd: `MJOP-Item` «betreft» → `Bouwdeelelement`
- 🔴 Verwijderd: `MJOP-Item` «betreft» → `Vastgoedobject`
- 🔴 Verwijderd: `MJOP-Item` «op basis van» → `Prijzenboekitem`
- 🔴 Verwijderd: `MJOP` «bestaat uit» → `MJOP-Item`
- 🔴 Verwijderd: `MJOP` «betreft» → `Vastgoedobject`
- 🔴 Verwijderd: `MJOP` «gerealiseerd door» → `Werkbon`
- 🔴 Verwijderd: `Vastgoed Contract` «heeft» → `Rechtspersoon`
- 🔴 Verwijderd: `Vastgoedcontractregel` «heeft» → `Vastgoed Contract`
- 🔴 Verwijderd: `Vastgoedobject` «bestaat uit» → `Bouwdeel`
- 🔴 Verwijderd: `Vastgoedobject` «betreft» → `Inspectie`
- 🔴 Verwijderd: `Vastgoedobject` «betreft» → `KadastraalPerceel`
- 🔴 Verwijderd: `Vastgoedobject` «betreft» → `KadastraleOnroerendeZaak`
- 🔴 Verwijderd: `Vastgoedobject` «betreft» → `Pand`
- 🔴 Verwijderd: `Vastgoedobject` «betreft» → `Zakelijk Recht`
- 🔴 Verwijderd: `Vastgoedobject` «heeft» → `Objectrelatie`
- 🔴 Verwijderd: `Vastgoedobject` «heeft» → `Vastgoedcontractregel`
- 🔴 Verwijderd: `Vastgoedobject` «heeft» → `Verhuurbaar Eenheid`
- 🔴 Verwijderd: `Verhuurbaar Eenheid` «betreft» → `Vastgoedcontractregel`
- 🔴 Verwijderd: `Werkbon` «betreft» → `Bouwdeel`
- 🔴 Verwijderd: `Werkbon` «betreft» → `Bouwdeelelement`
- 🔴 Verwijderd: `Werkbon` «betreft» → `Vastgoedobject`
- 🔴 Verwijderd: `Zakelijk Recht` «heeft eigenaar» → `Eigenaar`
- 🔴 Verwijderd: `Zakelijk Recht` «heeft» → `Kostenplaats`
- 🔴 Verwijderd: `Zakelijk Recht` «pacht» → `Pachter`

#### Generalisaties

- 🔴 Verwijderd: `Aanbesteding Vastgoed` ⟶ `Aanbesteding`
- 🔴 Verwijderd: `Eigenaar` ⟶ `Rechtspersoon`
- 🔴 Verwijderd: `Huurder` ⟶ `Rechtspersoon`
- 🔴 Verwijderd: `NADAanvullingBRP` ⟶ `Nummeraanduiding`
- 🔴 Verwijderd: `Pachter` ⟶ `Rechtspersoon`
- 🔴 Verwijderd: `Zakelijk Recht` ⟶ `ZakelijkRecht`

<a id="structureel-delfts-gemeentelijk-gegevensmodel99-kernbagmodel-bag"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/99 Kern/BAG/Model BAG

#### Classes

##### `AdresseerbaarObject` — 🔴 Verwijderd

**Attributen:**

- 🔴 `identificatie` — Verwijderd
- 🔴 `typeAdresseerbaarObject` — Verwijderd
- 🔴 `versie` — Verwijderd

##### `BinnenlandsAdres` — 🔴 Verwijderd

**Attributen:**

- 🔴 `BAGID` — Verwijderd
- 🔴 `gemeentenaam` — Verwijderd
- 🔴 `huisletter` — Verwijderd
- 🔴 `huisnummer` — Verwijderd
- 🔴 `huisnummertoevoeging` — Verwijderd
- 🔴 `postcode` — Verwijderd
- 🔴 `straatnaam` — Verwijderd

##### `Buurt` — 🔴 Verwijderd

**Attributen:**

- 🔴 `beginGeldigheid` — Verwijderd
- 🔴 `code` — Verwijderd
- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumIngang` — Verwijderd
- 🔴 `eindGeldigheid` — Verwijderd
- 🔴 `Geconstateerd` — Verwijderd
- 🔴 `geometrie` — Verwijderd
- 🔴 `identificatie` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `status` — Verwijderd
- 🔴 `versie` — Verwijderd

##### `Gemeente` — 🔴 Verwijderd

**Attributen:**

- 🔴 `beginGeldigheid` — Verwijderd
- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumIngang` — Verwijderd
- 🔴 `eindGeldigheid` — Verwijderd
- 🔴 `Geconstateerd` — Verwijderd
- 🔴 `gemeentecode` — Verwijderd
- 🔴 `gemeentenaam` — Verwijderd
- 🔴 `gemeentenaam NEN` — Verwijderd
- 🔴 `geometrie` — Verwijderd
- 🔴 `identificatie` — Verwijderd
- 🔴 `nieuwe gemeente` — Verwijderd
- 🔴 `versie` — Verwijderd

##### `Ligplaats` — 🔴 Verwijderd

**Attributen:**

- 🔴 `beginGeldigheid` — Verwijderd
- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumIngang` — Verwijderd
- 🔴 `documentdatum` — Verwijderd
- 🔴 `documentnummer` — Verwijderd
- 🔴 `eindGeldigheid` — Verwijderd
- 🔴 `geconstateerd` — Verwijderd
- 🔴 `geometrie` — Verwijderd
- 🔴 `identificatie` — Verwijderd
- 🔴 `status` — Verwijderd
- 🔴 `versie` — Verwijderd

##### `Nummeraanduiding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `beginGeldigheid` — Verwijderd
- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumIngang` — Verwijderd
- 🔴 `documentdatum` — Verwijderd
- 🔴 `documentnummer` — Verwijderd
- 🔴 `eindeGeldigheid` — Verwijderd
- 🔴 `geconstateerd` — Verwijderd
- 🔴 `geometrie` — Verwijderd
- 🔴 `huisletter` — Verwijderd
- 🔴 `huisnummer` — Verwijderd
- 🔴 `huisnummertoevoeging` — Verwijderd
- 🔴 `identificatie` — Verwijderd
- 🔴 `postcode` — Verwijderd
- 🔴 `status` — Verwijderd
- 🔴 `typeAdresseerbaarObject` — Verwijderd
- 🔴 `versie` — Verwijderd

##### `Onderzoek` — 🔴 Verwijderd

**Attributen:**

- 🔴 `beginGeldigheid` — Verwijderd
- 🔴 `datumActueelTot` — Verwijderd
- 🔴 `documentdatum` — Verwijderd
- 🔴 `documentnummer` — Verwijderd
- 🔴 `eindGeldigheid` — Verwijderd
- 🔴 `eindRegistratie` — Verwijderd
- 🔴 `identificatie` — Verwijderd
- 🔴 `inOnderzoek` — Verwijderd
- 🔴 `kenmerk` — Verwijderd
- 🔴 `objectIdentificatie` — Verwijderd
- 🔴 `objecttype` — Verwijderd
- 🔴 `tijdstipRegistratie` — Verwijderd
- 🔴 `volgnummer` — Verwijderd

##### `OpenbareRuimte` — 🔴 Verwijderd

**Attributen:**

- 🔴 `begingeldigheid` — Verwijderd
- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumIngang` — Verwijderd
- 🔴 `documentdatum` — Verwijderd
- 🔴 `documentnummer` — Verwijderd
- 🔴 `eindGeldigheid` — Verwijderd
- 🔴 `geconstateerd` — Verwijderd
- 🔴 `geometrie` — Verwijderd
- 🔴 `Huisnummerrange even en oneven nummers` — Verwijderd
- 🔴 `Huisnummerrange even nummers` — Verwijderd
- 🔴 `Huisnummerrange oneven nummers` — Verwijderd
- 🔴 `identificatie` — Verwijderd
- 🔴 `labelNaam` — Verwijderd
- 🔴 `naamOpenbareruimte` — Verwijderd
- 🔴 `status` — Verwijderd
- 🔴 `straatcode` — Verwijderd
- 🔴 `straatnaam` — Verwijderd
- 🔴 `typeOpenbareruimte` — Verwijderd
- 🔴 `versie` — Verwijderd
- 🔴 `wegsegment` — Verwijderd

##### `Pand` — 🔴 Verwijderd

**Attributen:**

- 🔴 `beginGeldigheid` — Verwijderd
- 🔴 `brutoInhoudPand` — Verwijderd
- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumIngang` — Verwijderd
- 🔴 `documentdatum` — Verwijderd
- 🔴 `documentnummer` — Verwijderd
- 🔴 `eindGeldigheid` — Verwijderd
- 🔴 `geconstateerd` — Verwijderd
- 🔴 `geometrieBovenaanzicht` — Verwijderd
- 🔴 `geometrieMaaiveld` — Verwijderd
- 🔴 `geometriePunt` — Verwijderd
- 🔴 `hoogsteBouwlaag` — Verwijderd
- 🔴 `identificatie` — Verwijderd
- 🔴 `laagsteBouwlaag` — Verwijderd
- 🔴 `oorspronkelijkBouwjaar` — Verwijderd
- 🔴 `oppervlakte` — Verwijderd
- 🔴 `relatieveHoogteligging` — Verwijderd
- 🔴 `status` — Verwijderd
- 🔴 `statusVoortgangBouw` — Verwijderd
- 🔴 `versie` — Verwijderd

##### `Standplaats` — 🔴 Verwijderd

**Attributen:**

- 🔴 `beginGeldigheid` — Verwijderd
- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumIngang` — Verwijderd
- 🔴 `documentdatum` — Verwijderd
- 🔴 `documentnummer` — Verwijderd
- 🔴 `eindGeldigheid` — Verwijderd
- 🔴 `Geconstateerd` — Verwijderd
- 🔴 `Geometrie` — Verwijderd
- 🔴 `Identificatie` — Verwijderd
- 🔴 `Status` — Verwijderd
- 🔴 `Versie` — Verwijderd

##### `Verblijfsobject` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aantalKamers` — Verwijderd
- 🔴 `beginGeldigheid` — Verwijderd
- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumIngang` — Verwijderd
- 🔴 `documentdatum` — Verwijderd
- 🔴 `documentnummer` — Verwijderd
- 🔴 `eindGeldigheid` — Verwijderd
- 🔴 `gebruiksdoel` — Verwijderd
- 🔴 `geconstateerd` — Verwijderd
- 🔴 `geometrie` — Verwijderd
- 🔴 `hoogsteBouwlaag` — Verwijderd
- 🔴 `identificatie` — Verwijderd
- 🔴 `laagsteBouwlaag` — Verwijderd
- 🔴 `ontsluitingVerdieping` — Verwijderd
- 🔴 `oppervlakte` — Verwijderd
- 🔴 `soortWoonobject` — Verwijderd
- 🔴 `status` — Verwijderd
- 🔴 `toegangBouwlaag` — Verwijderd
- 🔴 `Versie` — Verwijderd

##### `Wijk` — 🔴 Verwijderd

**Attributen:**

- 🔴 `beginGeldigheid` — Verwijderd
- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumIngang` — Verwijderd
- 🔴 `eindGeldigheid` — Verwijderd
- 🔴 `Geconstateerd` — Verwijderd
- 🔴 `geometrie` — Verwijderd
- 🔴 `identificatie` — Verwijderd
- 🔴 `status` — Verwijderd
- 🔴 `versie` — Verwijderd
- 🔴 `wijkcode` — Verwijderd
- 🔴 `wijknaam` — Verwijderd

##### `Woonplaats` — 🔴 Verwijderd

**Attributen:**

- 🔴 `beginGeldigheid` — Verwijderd
- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumIngang` — Verwijderd
- 🔴 `documentdatum` — Verwijderd
- 🔴 `documentnummer` — Verwijderd
- 🔴 `eindGeldigheid` — Verwijderd
- 🔴 `eindRegistratie` — Verwijderd
- 🔴 `geconstateerd` — Verwijderd
- 🔴 `geometrie` — Verwijderd
- 🔴 `identificatie` — Verwijderd
- 🔴 `status` — Verwijderd
- 🔴 `tijdstipActief` — Verwijderd
- 🔴 `tijdstipRegistratie` — Verwijderd
- 🔴 `versie` — Verwijderd
- 🔴 `voorkomen` — Verwijderd
- 🔴 `woonplaatsnaam` — Verwijderd
- 🔴 `woonplaatsnaamNEN` — Verwijderd

#### Enumeraties

##### `Boolean` — 🔴 Verwijderd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `gebruiksdoel` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `bijeenkomstfunctie` — Verwijderd
- 🔴 `celfunctie` — Verwijderd
- 🔴 `gezondheidszorgfunctie` — Verwijderd
- 🔴 `industriefunctie` — Verwijderd
- 🔴 `kantoorfunctie` — Verwijderd
- 🔴 `logiesfunctie` — Verwijderd
- 🔴 `onderwijsfunctie` — Verwijderd
- 🔴 `overige gebruiksfunctie` — Verwijderd
- 🔴 `sportfunctie` — Verwijderd
- 🔴 `winkelfunctie` — Verwijderd
- 🔴 `woonfunctie` — Verwijderd

##### `ontsluitingswijzeVerdieping` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `lift` — Verwijderd
- 🔴 `roltrap` — Verwijderd
- 🔴 `trap` — Verwijderd

##### `soortWoonobject` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `bijzonder woongebouw` — Verwijderd
- 🔴 `overig woonverblijf` — Verwijderd
- 🔴 `recreatiewoning` — Verwijderd
- 🔴 `woning` — Verwijderd
- 🔴 `wooneenheid` — Verwijderd

##### `statusLigplaats` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `plaats aangewezen` — Verwijderd
- 🔴 `plaats ingetrokken` — Verwijderd

##### `statusNummeraanduiding` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `naamgeving ingetrokken` — Verwijderd
- 🔴 `naamgeving uitgegeven` — Verwijderd

##### `statusOpenbareRuimte` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `naamgeving ingetrokken` — Verwijderd
- 🔴 `naamgeving uitgegeven` — Verwijderd

##### `statusPand` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `bouw gestart` — Verwijderd
- 🔴 `bouwaanvraag ontvangen` — Verwijderd
- 🔴 `bouwvergunning verleend` — Verwijderd
- 🔴 `niet gerealiseerd pand` — Verwijderd
- 🔴 `pand buiten gebruik` — Verwijderd
- 🔴 `pand gesloopt` — Verwijderd
- 🔴 `pand in gebruik` — Verwijderd
- 🔴 `pand in gebruik (niet ingemeten)` — Verwijderd
- 🔴 `pand ten onrechte opgevoerd` — Verwijderd
- 🔴 `sloopvergunning verleend` — Verwijderd
- 🔴 `verbouwing pand` — Verwijderd

##### `statusStandplaats` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `plaats aangewezen` — Verwijderd
- 🔴 `plaats ingetrokken` — Verwijderd

##### `statusVerblijfsobject` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `niet gerealiseerd verblijfsobject` — Verwijderd
- 🔴 `verblijfsobject buiten gebruik` — Verwijderd
- 🔴 `verblijfsobject gevormd` — Verwijderd
- 🔴 `verblijfsobject in gebruik` — Verwijderd
- 🔴 `verblijfsobject in gebruik (niet ingemeten)` — Verwijderd
- 🔴 `verblijfsobject ingetrokken` — Verwijderd
- 🔴 `verblijfsobject verbouwing` — Verwijderd

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

##### `statusWoonplaats` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `woonplaats aangewezen` — Verwijderd
- 🔴 `woonplaats ingetrokken` — Verwijderd

##### `TypeAdresseerbaarObject` — 🔴 Verwijderd

**Literals:**

- 🔴 `Ligplaats` — Verwijderd
- 🔴 `Standplaats` — Verwijderd
- 🔴 `Verblijfsobject` — Verwijderd

##### `typeringOpenbareRuimte` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `administratief gebied` — Verwijderd
- 🔴 `functioneel gebied` — Verwijderd
- 🔴 `kunstwerk` — Verwijderd
- 🔴 `landschappelijk gebied` — Verwijderd
- 🔴 `spoorbaan` — Verwijderd
- 🔴 `terrein` — Verwijderd
- 🔴 `water` — Verwijderd
- 🔴 `weg` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `AdresseerbaarObject` «Heeft als hoofdadres» → `Nummeraanduiding`
- 🔴 Verwijderd: `AdresseerbaarObject` «Heeft als Nevenadres» → `Nummeraanduiding`
- 🔴 Verwijderd: `AdresseerbaarObject` «heeft» → `Winkelvloeroppervlak`
- 🔴 Verwijderd: `Buurt` «ligt in» → `Wijk`
- 🔴 Verwijderd: `Gemeente` «is overgegaan in» → `Gemeente`
- 🔴 Verwijderd: `Nummeraanduiding` «heeft als locatie-adres» → `Vestiging`
- 🔴 Verwijderd: `Nummeraanduiding` «Ligt aan» → `OpenbareRuimte`
- 🔴 Verwijderd: `Nummeraanduiding` «Ligt in» → `Buurt`
- 🔴 Verwijderd: `Nummeraanduiding` «ligt in» → `Gebied`
- 🔴 Verwijderd: `Nummeraanduiding` «Ligt in» → `Woonplaats`
- 🔴 Verwijderd: `Nummeraanduiding` «verwijst naar» → `LocatieaanduidingWozObject`
- 🔴 Verwijderd: `Onderzoek` «objectidentificatie» → `Ligplaats`
- 🔴 Verwijderd: `Onderzoek` «objectidentificatie» → `Nummeraanduiding`
- 🔴 Verwijderd: `Onderzoek` «objectidentificatie» → `OpenbareRuimte`
- 🔴 Verwijderd: `Onderzoek` «objectidentificatie» → `Pand`
- 🔴 Verwijderd: `Onderzoek` «objectidentificatie» → `Standplaats`
- 🔴 Verwijderd: `Onderzoek` «objectidentificatie» → `Verblijfsobject`
- 🔴 Verwijderd: `Onderzoek` «objectidentificatie» → `Woonplaats`
- 🔴 Verwijderd: `OpenbareRuimte` «Ligt in» → `Buurt`
- 🔴 Verwijderd: `OpenbareRuimte` «ligt in» → `Buurt`
- 🔴 Verwijderd: `OpenbareRuimte` «Ligt in» → `Woonplaats`
- 🔴 Verwijderd: `Pand` «heeft» → `Vastgoedobject`
- 🔴 Verwijderd: `Pand` «zonder verblijfsobject ligt in» → `Buurt`
- 🔴 Verwijderd: `Pand` «zonder verblijfsobject ligt in» → `Buurt`
- 🔴 Verwijderd: `Verblijfsobject` «heeft» → `Vastgoedobject`
- 🔴 Verwijderd: `Verblijfsobject` «Maakt deel uit van» → `Pand`
- 🔴 Verwijderd: `Wijk` «Ligt in» → `Woonplaats`
- 🔴 Verwijderd: `Woonplaats` «Ligt in» → `Gemeente`

#### Generalisaties

- 🔴 Verwijderd: `AdresseerbaarObject` ⟶ `Object`
- 🔴 Verwijderd: `Ligplaats` ⟶ `AdresseerbaarObject`
- 🔴 Verwijderd: `Pand` ⟶ `Geo-Object`
- 🔴 Verwijderd: `Standplaats` ⟶ `AdresseerbaarObject`
- 🔴 Verwijderd: `Verblijfsobject` ⟶ `AdresseerbaarObject`

<a id="structureel-delfts-gemeentelijk-gegevensmodel99-kerndimensiesmodel"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/99 Kern/Dimensies/Model

#### Classes

##### `Periode` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodel99-kerngeneriekmodel-generiek"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/99 Kern/Generiek/Model Generiek

#### Classes

##### `Foto` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bestandsgrootte` — Verwijderd
- 🔴 `bestandsnaam` — Verwijderd
- 🔴 `bestandstype` — Verwijderd
- 🔴 `datumtijd` — Verwijderd
- 🔴 `locatie` — Verwijderd
- 🔴 `pixelsX` — Verwijderd
- 🔴 `pixelsY` — Verwijderd

##### `Gebied` — 🔴 Verwijderd

**Attributen:**

- 🔴 `gebiedsAanduiding` — Verwijderd

##### `Gebiedengroep` — 🔴 Verwijderd

##### `Lijn` — 🔴 Verwijderd

**Attributen:**

- 🔴 `lijnLocatie` — Verwijderd

##### `Lijnengroep` — 🔴 Verwijderd

##### `Locatie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `hoogte` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `NEN3610ID` — Verwijderd

##### `Punt` — 🔴 Verwijderd

**Attributen:**

- 🔴 `puntLocatie` — Verwijderd

##### `Puntengroep` — 🔴 Verwijderd

##### `Video-opname` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bestandsgrootte` — Verwijderd
- 🔴 `datumtijd` — Verwijderd
- 🔴 `lengte` — Verwijderd
- 🔴 `videoformaat` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `Foto` «betreft» → `Erfgoed Object`
- 🔴 Verwijderd: `Gebiedengroep` «omvat» → `Gebied`
- 🔴 Verwijderd: `Lijnengroep` «omvat» → `Lijn`
- 🔴 Verwijderd: `Puntengroep` «omvat» → `Punt`
- 🔴 Verwijderd: `Video-opname` «betreft» → `Agendapunt`
- 🔴 Verwijderd: `Video-opname` «betreft» → `Erfgoed Object`

#### Generalisaties

- 🔴 Verwijderd: `Gebied` ⟶ `Locatie`
- 🔴 Verwijderd: `Gebiedengroep` ⟶ `Locatie`
- 🔴 Verwijderd: `Lijn` ⟶ `Locatie`
- 🔴 Verwijderd: `Lijnengroep` ⟶ `Locatie`
- 🔴 Verwijderd: `Punt` ⟶ `Locatie`
- 🔴 Verwijderd: `Puntengroep` ⟶ `Locatie`

<a id="structureel-delfts-gemeentelijk-gegevensmodel99-kernrgbzplusdiagramview-zaakobjecten"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/99 Kern/RGBZPlus/Diagram/View (Zaak)objecten

#### Classes

##### `RSGB` — 🔴 Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodel99-kernrgbzplusdiagramview-betrokkene"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/99 Kern/RGBZPlus/Diagram/View Betrokkene

#### Classes

##### `RSGB` — 🔴 Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodel99-kernrgbzplusmodel-rgbzenumeratiesoort"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/99 Kern/RGBZPlus/Model RGBZ/Enumeratiesoort

#### Enumeraties

##### `Geslachtsaanduiding MEDEWERKER` — 🔴 Verwijderd

**Literals:**

- 🔴 `Man` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Vrouw` — Verwijderd

##### `Soorten Klantcontact` — 🔴 Verwijderd

**Literals:**

- 🔴 `balie` — Verwijderd
- 🔴 `brief` — Verwijderd
- 🔴 `internet` — Verwijderd
- 🔴 `selfserviceloket` — Verwijderd
- 🔴 `telefonisch` — Verwijderd

##### `Vertrouwelijk aanduiding DOCUMENT` — 🔴 Verwijderd

**Literals:**

- 🔴 `BEPERKT OPENBAAR` — Verwijderd
- 🔴 `CONFIDENTIEEL` — Verwijderd
- 🔴 `GEHEIM` — Verwijderd
- 🔴 `INTERN` — Verwijderd
- 🔴 `OPENBAAR` — Verwijderd
- 🔴 `VERTROUWELIJK` — Verwijderd
- 🔴 `ZAAKVERTROUWELIJK` — Verwijderd
- 🔴 `ZEER GEHEIM` — Verwijderd

##### `Vervalreden BESLUIT` — 🔴 Verwijderd

**Literals:**

- 🔴 `Besluit ingetrokken door overheid` — Verwijderd
- 🔴 `Besluit ingetrokken o.v.v. belanghebbende` — Verwijderd
- 🔴 `Besluit met tijdelijke werking` — Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodel99-kernrgbzplusmodel-rgbzgroepattribuutsoort"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/99 Kern/RGBZPlus/Model RGBZ/Groepattribuutsoort

#### Classes

##### `AfwijkendBuitenlandsCorrespondentieadresRol` — 🔴 Verwijderd

**Attributen:**

- 🔴 `adresBuitenland1` — Verwijderd
- 🔴 `adresBuitenland2` — Verwijderd
- 🔴 `adresBuitenland3` — Verwijderd
- 🔴 `landPostadres` — Verwijderd

##### `AfwijkendCorrespondentiePostadresRol` — 🔴 Verwijderd

**Attributen:**

- 🔴 `postadresType` — Verwijderd
- 🔴 `postbusOfAntwoordnummer` — Verwijderd
- 🔴 `postcodePostadres` — Verwijderd

##### `AnderZaakobjectZaak` — 🔴 Verwijderd

**Attributen:**

- 🔴 `anderZaakobjectAanduiding` — Verwijderd
- 🔴 `anderZaakobjectLocatie` — Verwijderd
- 🔴 `anderZaakobjectOmschrijving` — Verwijderd
- 🔴 `anderZaakobjectRegistratie` — Verwijderd

##### `ContactpersoonRol` — 🔴 Verwijderd

**Attributen:**

- 🔴 `contactpersoonEmailadres` — Verwijderd
- 🔴 `contactpersoonFunctie` — Verwijderd
- 🔴 `Contactpersoonnaam` — Verwijderd
- 🔴 `contactpersoonTelefoonnummer` — Verwijderd

##### `KenmerkenZaak` — 🔴 Verwijderd

**Attributen:**

- 🔴 `kenmerk` — Verwijderd
- 🔴 `kenmerkBron` — Verwijderd

##### `OpschortingZaak` — 🔴 Verwijderd

**Attributen:**

- 🔴 `indicatieOpschorting` — Verwijderd
- 🔴 `redenOpschorting` — Verwijderd

##### `VerlengingZaak` — 🔴 Verwijderd

**Attributen:**

- 🔴 `duurVerlenging` — Verwijderd
- 🔴 `redenVerlenging` — Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodel99-kernrgbzplusmodel-rgbzmetagegevens"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/99 Kern/RGBZPlus/Model RGBZ/Metagegevens

#### Classes

##### `Brondocumenten` — 🔴 Verwijderd

**Attributen:**

- 🔴 `akteGemeente` — Verwijderd
- 🔴 `datumDocument` — Verwijderd
- 🔴 `documentGemeente` — Verwijderd
- 🔴 `documentIdentificatie` — Verwijderd
- 🔴 `documentOmschrijving` — Verwijderd

##### `FormeleHistorie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `tijdstipRegistratieGegevens` — Verwijderd

##### `InOnderzoek` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aanduidingGegevensInOnderzoek` — Verwijderd

##### `MaterieleHistorie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheidGegevens` — Verwijderd
- 🔴 `datumEindeGeldigheidGegevens` — Verwijderd

##### `StrijdigheidOfNietigheid` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aanduidingStrijdigheidNietigheid` — Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodel99-kernrgbzplusmodel-rgbzmodel-kern-rgbz"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/99 Kern/RGBZPlus/Model RGBZ/Model Kern RGBZ

#### Classes

##### `Bedrijfsproces` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Afgerond` — Verwijderd
- 🔴 `Datum_eind` — Verwijderd
- 🔴 `Datum_start` — Verwijderd
- 🔴 `Naam` — Verwijderd
- 🔴 `Omschrijving` — Verwijderd

##### `Bedrijfsprocestype` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Omschrijving` — Verwijderd

##### `Besluit` — 🔴 Verwijderd

**Attributen:**

- 🔴 `besluitidentificatie` — Verwijderd
- 🔴 `besluittoelichting` — Verwijderd
- 🔴 `datumBesluit` — Verwijderd
- 🔴 `datumPublicatie` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `datumUiterlijkeReactie` — Verwijderd
- 🔴 `datumVerval` — Verwijderd
- 🔴 `datumVerzending` — Verwijderd
- 🔴 `document` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `redenVerval` — Verwijderd
- 🔴 `type` — Verwijderd
- 🔴 `zaak` — Verwijderd

##### `Besluittype` — 🔴 Verwijderd

**Attributen:**

- 🔴 `besluitcategorie` — Verwijderd
- 🔴 `besluittypeOmschrijving` — Verwijderd
- 🔴 `besluittypeOmschrijvingGeneriek` — Verwijderd
- 🔴 `datumBeginGeldigheidBesluittype` — Verwijderd
- 🔴 `datumEindeGeldigheidBesluittype` — Verwijderd
- 🔴 `indicatiePublicatie` — Verwijderd
- 🔴 `publicatietekst` — Verwijderd
- 🔴 `publicatietermijn` — Verwijderd
- 🔴 `reactietermijn` — Verwijderd

##### `Betaling` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bedrag` — Verwijderd
- 🔴 `datumtijd` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `valuta` — Verwijderd

##### `Betrokkene` — 🔴 Verwijderd

**Attributen:**

- 🔴 `adresBinnenland` — Verwijderd
- 🔴 `adresBuitenland` — Verwijderd
- 🔴 `betrokkene` — Verwijderd
- 🔴 `identificatie` — Verwijderd
- 🔴 `medewerker` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `organisatorische eenheid` — Verwijderd
- 🔴 `rol` — Verwijderd
- 🔴 `vestiging` — Verwijderd

##### `Deelproces` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Datum_afgehandeld` — Verwijderd
- 🔴 `Datum_gepland` — Verwijderd

##### `Deelprocestype` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Omschrijving` — Verwijderd

##### `Document` — 🔴 Verwijderd

**Attributen:**

- 🔴 `cocumentBeschrijving` — Verwijderd
- 🔴 `datumCreatieDocument` — Verwijderd
- 🔴 `datumOntvangstdocument` — Verwijderd
- 🔴 `datumVerzendingDocument` — Verwijderd
- 🔴 `documentAuteur` — Verwijderd
- 🔴 `documentIdentificatie` — Verwijderd
- 🔴 `documentTitel` — Verwijderd
- 🔴 `type` — Verwijderd
- 🔴 `vertrouwelijkAanduiding` — Verwijderd

##### `Documenttype` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheidDocumenttype` — Verwijderd
- 🔴 `datumEindeGeldigheidDocumenttype` — Verwijderd
- 🔴 `documentCategorie` — Verwijderd
- 🔴 `documenttypeOmschrijving` — Verwijderd
- 🔴 `documenttypeOmschrijvingGeneriek` — Verwijderd
- 🔴 `documenttypeTrefwoord` — Verwijderd

##### `EnkelvoudigDocument` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bestandsnaam` — Verwijderd
- 🔴 `documentFormaat` — Verwijderd
- 🔴 `documentInhoud` — Verwijderd
- 🔴 `documentLink` — Verwijderd
- 🔴 `documentStatus` — Verwijderd
- 🔴 `documentTaal` — Verwijderd
- 🔴 `documentVersie` — Verwijderd

##### `Heffing` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bedrag` — Verwijderd
- 🔴 `code` — Verwijderd
- 🔴 `datumIndiening` — Verwijderd
- 🔴 `gefactureerd` — Verwijderd
- 🔴 `inrekening` — Verwijderd
- 🔴 `nummer` — Verwijderd
- 🔴 `runnummer` — Verwijderd

##### `Identificatiekenmerk` — 🔴 Verwijderd

**Attributen:**

- 🔴 `kenmerk` — Verwijderd

##### `Klantcontact` — 🔴 Verwijderd

**Attributen:**

- 🔴 `eindtijd` — Verwijderd
- 🔴 `kanaal` — Verwijderd
- 🔴 `notitie` — Verwijderd
- 🔴 `starttijd` — Verwijderd
- 🔴 `tijdsduur` — Verwijderd
- 🔴 `toelichting` — Verwijderd
- 🔴 `wachttijdTotaal` — Verwijderd

##### `Medewerker` — 🔴 Verwijderd

**Attributen:**

- 🔴 `achternaam` — Verwijderd
- 🔴 `datumInDienst` — Verwijderd
- 🔴 `datumUitDienst` — Verwijderd
- 🔴 `emailadres` — Verwijderd
- 🔴 `extern` — Verwijderd
- 🔴 `functie` — Verwijderd
- 🔴 `geslachtsaanduiding` — Verwijderd
- 🔴 `medewerkerIdentificatie` — Verwijderd
- 🔴 `medewerkerToelichting` — Verwijderd
- 🔴 `organisatorische eenheid` — Verwijderd
- 🔴 `organisatorische eenheid` — Verwijderd
- 🔴 `roepnaam` — Verwijderd
- 🔴 `telefoonnummer` — Verwijderd
- 🔴 `voorletters` — Verwijderd
- 🔴 `voorvoegselAchternaam` — Verwijderd

##### `Object` — 🔴 Verwijderd

**Attributen:**

- 🔴 `adresBinnenland` — Verwijderd
- 🔴 `adresBuitenland` — Verwijderd
- 🔴 `besluit` — Verwijderd
- 🔴 `domein` — Verwijderd
- 🔴 `geometrie` — Verwijderd
- 🔴 `huishouden` — Verwijderd
- 🔴 `identificatie` — Verwijderd
- 🔴 `indicatieRisico` — Verwijderd
- 🔴 `kadastraleAanduiding` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `objecttype` — Verwijderd
- 🔴 `toelichting` — Verwijderd

##### `Offerte` — 🔴 Verwijderd

##### `OrganisatorischeEenheid` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumOntstaan` — Verwijderd
- 🔴 `datumOpheffing` — Verwijderd
- 🔴 `emailadres` — Verwijderd
- 🔴 `faxnummer` — Verwijderd
- 🔴 `Formatie` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `naamVerkort` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `organisatieIdentificatie` — Verwijderd
- 🔴 `telefoonnummer` — Verwijderd
- 🔴 `toelichting` — Verwijderd
- 🔴 `vestiging` — Verwijderd
- 🔴 `zaaktype` — Verwijderd

##### `SamengesteldDocument` — 🔴 Verwijderd

**Attributen:**

- 🔴 `document` — Verwijderd

##### `Status` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumStatusGezet` — Verwijderd
- 🔴 `indicatieIaatstGezetteStatus` — Verwijderd
- 🔴 `statustoelichting` — Verwijderd
- 🔴 `type` — Verwijderd

##### `Statustype` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheidStatustype` — Verwijderd
- 🔴 `datumEindeGeldigheidStatustype` — Verwijderd
- 🔴 `doorlooptijdStatus` — Verwijderd
- 🔴 `statustypeOmschrijving` — Verwijderd
- 🔴 `statustypeOmschrijvingGeneriek` — Verwijderd
- 🔴 `statustypeVolgnummer` — Verwijderd

##### `VestigingVanZaakbehandelendeOrganisatie` — 🔴 Verwijderd

##### `Zaak` — 🔴 Verwijderd

**Attributen:**

- 🔴 `archiefnominatie` — Verwijderd
- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumEindeGepland` — Verwijderd
- 🔴 `datumEindeUiterlijkeAfdoening` — Verwijderd
- 🔴 `datumLaatsteBetaling` — Verwijderd
- 🔴 `datumPublicatie` — Verwijderd
- 🔴 `datumRegistratie` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `datumVernietigingDossier` — Verwijderd
- 🔴 `document` — Verwijderd
- 🔴 `duurVerlenging` — Verwijderd
- 🔴 `indicatieBetaling` — Verwijderd
- 🔴 `indicatieDeelzaken` — Verwijderd
- 🔴 `indicatieOpschorting` — Verwijderd
- 🔴 `leges` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `omschrijvingResultaat` — Verwijderd
- 🔴 `redenOpschorting` — Verwijderd
- 🔴 `redenVerlenging` — Verwijderd
- 🔴 `status` — Verwijderd
- 🔴 `toelichting` — Verwijderd
- 🔴 `toelichtingResultaat` — Verwijderd
- 🔴 `type` — Verwijderd
- 🔴 `vertrouwelijkheid` — Verwijderd
- 🔴 `zaakidentificatie` — Verwijderd
- 🔴 `zaakniveau` — Verwijderd

##### `ZAAK - Origineel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `anderZaakobject` — Verwijderd
- 🔴 `archiefnominatie` — Verwijderd
- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumEindeGepland` — Verwijderd
- 🔴 `datumEindeUiterlijkeAfdoening` — Verwijderd
- 🔴 `datumLaatsteBetaling` — Verwijderd
- 🔴 `datumPublicatie` — Verwijderd
- 🔴 `datumRegistratie` — Verwijderd
- 🔴 `datumStart` — Verwijderd
- 🔴 `datumVernietigingDossier` — Verwijderd
- 🔴 `indicatieBetaling` — Verwijderd
- 🔴 `indicatieDeelzaken` — Verwijderd
- 🔴 `kenmerk` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `omschrijvingResultaat` — Verwijderd
- 🔴 `opschorting` — Verwijderd
- 🔴 `toelichting` — Verwijderd
- 🔴 `toelichtingResultaat` — Verwijderd
- 🔴 `verlenging` — Verwijderd
- 🔴 `zaakidentificatie` — Verwijderd
- 🔴 `zaakniveau` — Verwijderd

##### `Zaaktype` — 🔴 Verwijderd

**Attributen:**

- 🔴 `archiefcode` — Verwijderd
- 🔴 `datumBeginGeldigheidZaaktype` — Verwijderd
- 🔴 `datumEindeGeldigheidZaaktype` — Verwijderd
- 🔴 `doorlooptijdBehandeling` — Verwijderd
- 🔴 `indicatiePublicatie` — Verwijderd
- 🔴 `publicatietekst` — Verwijderd
- 🔴 `servicenormBehandeling` — Verwijderd
- 🔴 `statustype` — Verwijderd
- 🔴 `trefwoord` — Verwijderd
- 🔴 `vertrouwelijkAanduiding` — Verwijderd
- 🔴 `zaakcategorie` — Verwijderd
- 🔴 `zaaktypeOmschrijving` — Verwijderd
- 🔴 `zaaktypeOmschrijvingGeneriek` — Verwijderd

#### Enumeraties

##### `Boolean` — 🔴 Verwijderd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `Heffingsoort` — 🔴 Verwijderd

**Literals:**

- 🔴 `leges` — Verwijderd
- 🔴 `precario` — Verwijderd

##### `Soorten Klantcontact` — 🔴 Verwijderd

**Literals:**

- 🔴 `balie` — Verwijderd
- 🔴 `brief` — Verwijderd
- 🔴 `internet` — Verwijderd
- 🔴 `selfserviceloket` — Verwijderd
- 🔴 `telefonisch` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `Bedrijfsproces` «is van» → `Bedrijfsprocestype`
- 🔴 Verwijderd: `Bedrijfsproces` «uitgevoerd binnen» → `Zaak`
- 🔴 Verwijderd: `Bedrijfsprocestype` «heeft» → `Producttype`
- 🔴 Verwijderd: `Bedrijfsprocestype` «heeft» → `Zaaktype`
- 🔴 Verwijderd: `Bedrijfsprocestype` «is onderdeel van» → `Bedrijfsprocestype`
- 🔴 Verwijderd: `Besluit` «is uitkomst van» → `Zaak`
- 🔴 Verwijderd: `Besluit` «is van» → `Besluittype`
- 🔴 Verwijderd: `Besluit` «is vastgelegd in» → `Document`
- 🔴 Verwijderd: `Besluit` «kan vastgelegd zijn als» → `Document`
- 🔴 Verwijderd: `Betaling` «komt voor op» → `Bankafschriftregel`
- 🔴 Verwijderd: `Betrokkene` «doet» → `Klantbeoordeling`
- 🔴 Verwijderd: `Betrokkene` «is» → `Medewerker`
- 🔴 Verwijderd: `Betrokkene` «is» → `NatuurlijkPersoon`
- 🔴 Verwijderd: `Betrokkene` «is» → `NietNatuurlijkPersoon`
- 🔴 Verwijderd: `Betrokkene` «is» → `OrganisatorischeEenheid`
- 🔴 Verwijderd: `Betrokkene` «oefent uit» → `Zaak`
- 🔴 Verwijderd: `Deelproces` «is deel van» → `Bedrijfsproces`
- 🔴 Verwijderd: `Deelproces` «is van» → `Deelprocestype`
- 🔴 Verwijderd: `Deelprocestype` «is deel van» → `Bedrijfsprocestype`
- 🔴 Verwijderd: `Document` «heeft kenmerk» → `Identificatiekenmerk`
- 🔴 Verwijderd: `Document` «is van» → `Documenttype`
- 🔴 Verwijderd: `Heffing` «betreft» → `Vorderingregel`
- 🔴 Verwijderd: `Heffing` «heeft grondslag» → `Heffinggrondslag`
- 🔴 Verwijderd: `Klantcontact` «betreft» → `ProductOfDienst`
- 🔴 Verwijderd: `Klantcontact` «heeft betrekking op» → `Zaak`
- 🔴 Verwijderd: `Klantcontact` «heeft klantcontacten» → `Betrokkene`
- 🔴 Verwijderd: `Klantcontact` «is gevoerd door» → `Medewerker`
- 🔴 Verwijderd: `Klantcontact` «kan leiden tot» → `AanvraagOfMelding`
- 🔴 Verwijderd: `Klantcontact` «locatie» → `VestigingVanZaakbehandelendeOrganisatie`
- 🔴 Verwijderd: `Medewerker` «aanvrager» → `Subsidie`
- 🔴 Verwijderd: `Medewerker` «dient in» → `StartformulierAanbesteden`
- 🔴 Verwijderd: `Medewerker` «geleverd via» → `Leverancier`
- 🔴 Verwijderd: `Medewerker` «gewijzigd door» → `Stremming`
- 🔴 Verwijderd: `Medewerker` «hoort bij» → `OrganisatorischeEenheid`
- 🔴 Verwijderd: `Medewerker` «ingevoerd door» → `Stremming`
- 🔴 Verwijderd: `Medewerker` «is contactpersoon voor» → `OrganisatorischeEenheid`
- 🔴 Verwijderd: `Medewerker` «is verantwoordelijk voor» → `OrganisatorischeEenheid`
- 🔴 Verwijderd: `Medewerker` «is verantwoordelijke voor» → `Zaaktype`
- 🔴 Verwijderd: `Medewerker` «verleent» → `Proces-verbaal-MOOR-melding`
- 🔴 Verwijderd: `Medewerker` «voert uit» → `Schouwronde`
- 🔴 Verwijderd: `Medewerker` «vraagt aan» → `Aanvraag Inkooporder`
- 🔴 Verwijderd: `Medewerker` «werkt bij» → `Uitvoerende instantie`
- 🔴 Verwijderd: `Object` «betreft» → `Zaak`
- 🔴 Verwijderd: `Object` «is» → `Besluit`
- 🔴 Verwijderd: `Object` «is» → `Buurt`
- 🔴 Verwijderd: `Object` «is» → `Buurt`
- 🔴 Verwijderd: `Object` «is» → `Huishouden`
- 🔴 Verwijderd: `Object` «Is» → `Ingezetene`
- 🔴 Verwijderd: `Object` «is» → `Inrichtingselement`
- 🔴 Verwijderd: `Object` «is» → `KadastraalPerceel`
- 🔴 Verwijderd: `Object` «is» → `KadastraleOnroerendeZaak`
- 🔴 Verwijderd: `Object` «is» → `Kunstwerkdeel`
- 🔴 Verwijderd: `Object` «is» → `Ligplaats`
- 🔴 Verwijderd: `Object` «is» → `Ligplaats`
- 🔴 Verwijderd: `Object` «is» → `MaatschappelijkeActiviteit`
- 🔴 Verwijderd: `Object` «is» → `NatuurlijkPersoon`
- 🔴 Verwijderd: `Object` «is» → `NietNatuurlijkPersoon`
- 🔴 Verwijderd: `Object` «is» → `OpenbareRuimte`
- 🔴 Verwijderd: `Object` «is» → `OpenbareRuimte`
- 🔴 Verwijderd: `Object` «is» → `Pand`
- 🔴 Verwijderd: `Object` «is» → `Pand`
- 🔴 Verwijderd: `Object` «is» → `Standplaats`
- 🔴 Verwijderd: `Object` «is» → `Standplaats`
- 🔴 Verwijderd: `Object` «is» → `Vaartuig`
- 🔴 Verwijderd: `Object` «is» → `Voertuig`
- 🔴 Verwijderd: `Object` «is» → `Waterdeel`
- 🔴 Verwijderd: `OrganisatorischeEenheid` «heeft» → `Klantbeoordeling`
- 🔴 Verwijderd: `OrganisatorischeEenheid` «heeft» → `Kostenplaats`
- 🔴 Verwijderd: `OrganisatorischeEenheid` «Is deel van» → `OrganisatorischeEenheid`
- 🔴 Verwijderd: `OrganisatorischeEenheid` «is gehuisvest in» → `VestigingVanZaakbehandelendeOrganisatie`
- 🔴 Verwijderd: `OrganisatorischeEenheid` «is verantwoordelijke voor» → `Zaaktype`
- 🔴 Verwijderd: `SamengesteldDocument` «omvat» → `EnkelvoudigDocument`
- 🔴 Verwijderd: `Status` «is van» → `Statustype`
- 🔴 Verwijderd: `ZAAK - Origineel` «heeft betrekking op andere» → `ZAAK - Origineel`
- 🔴 Verwijderd: `ZAAK - Origineel` «is deelzaak van» → `ZAAK - Origineel`
- 🔴 Verwijderd: `Zaak` «afhandelend medewerker» → `Medewerker`
- 🔴 Verwijderd: `Zaak` «betreft» → `Project`
- 🔴 Verwijderd: `Zaak` «heeft betaling» → `Betaling`
- 🔴 Verwijderd: `Zaak` «heeft betrekking op andere» → `Zaak`
- 🔴 Verwijderd: `Zaak` «heeft kenmerken» → `KenmerkenZaak`
- 🔴 Verwijderd: `Zaak` «heeft product» → `Producttype`
- 🔴 Verwijderd: `Zaak` «heeft» → `Heffing`
- 🔴 Verwijderd: `Zaak` «heeft» → `Klantbeoordeling`
- 🔴 Verwijderd: `Zaak` «heeft» → `Status`
- 🔴 Verwijderd: `Zaak` «is deelzaak van» → `Zaak`
- 🔴 Verwijderd: `Zaak` «is van» → `Zaaktype`
- 🔴 Verwijderd: `Zaak` «kent» → `Document`
- 🔴 Verwijderd: `Zaaktype` «heeft» → `Heffinggrondslag`
- 🔴 Verwijderd: `Zaaktype` «heeft» → `Producttype`
- 🔴 Verwijderd: `Zaaktype` «heeft» → `Statustype`

#### Generalisaties

- 🔴 Verwijderd: `Betrokkene` ⟶ `Rechtspersoon`
- 🔴 Verwijderd: `EnkelvoudigDocument` ⟶ `Document`
- 🔴 Verwijderd: `SamengesteldDocument` ⟶ `Document`

<a id="structureel-delfts-gemeentelijk-gegevensmodel99-kernrsgbplusdiagram"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/Diagram

#### Classes

##### `OverigeGeoObjecten` — 🔴 Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodel99-kernrsgbplusdiagram-rsgbcatalogus-rsgbtekenwijze"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/Diagram RSGB/Catalogus RSGB/Tekenwijze

#### Classes

##### `None` — 🔴 Verwijderd

##### `ObjecttypeA` — 🔴 Verwijderd

##### `ObjecttypeB` — 🔴 Verwijderd

##### `ObjecttypeC` — 🔴 Verwijderd

##### `ObjecttypeD` — 🔴 Verwijderd

##### `ObjecttypeE` — 🔴 Verwijderd

##### `ObjecttypeF` — 🔴 Verwijderd

##### `ObjecttypeG` — 🔴 Verwijderd

#### Associaties

- 🔴 Verwijderd: `ObjecttypeA` «naam1 (werkwoord)» → `ObjecttypeB`
- 🔴 Verwijderd: `ObjecttypeD` «naam2 (werkwoord)» → `ObjecttypeB`
- 🔴 Verwijderd: `ObjecttypeE` «naam3» → `ObjecttypeF`
- 🔴 Verwijderd: `ObjecttypeE` «naam4» → `ObjecttypeG`

#### Generalisaties

- 🔴 Verwijderd: `ObjecttypeA` ⟶ `ObjecttypeC`

<a id="structureel-delfts-gemeentelijk-gegevensmodel99-kernrsgbplusdiagram-rsgbdiagrammen-intern-gebruiksemantische-relaties"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/Diagram RSGB/Diagrammen intern gebruik/Semantische relaties

#### Classes

##### `DetailleringAdressenGebouwenEnTerreinen` — 🔴 Verwijderd

##### `DetailleringKadastraleOnroerendZaken` — 🔴 Verwijderd

##### `DetailleringSubjecten` — 🔴 Verwijderd

##### `DetailleringWOZObjecttypen` — 🔴 Verwijderd

##### `OverigImgeo` — 🔴 Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelcomplex-datatype"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Complex datatype

#### Datatypes

##### `BAGObjectnummering` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `gemeentecode` — Verwijderd
- 🔴 `objecttypecode` — Verwijderd
- 🔴 `objectvolgnummer` — Verwijderd

##### `CompositeID` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Lokaal id` — Verwijderd
- 🔴 `Namspace` — Verwijderd
- 🔴 `Versie` — Verwijderd

##### `TypeBedrag` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `som` — Verwijderd
- 🔴 `valutasoort` — Verwijderd

##### `TypeBreuk` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `noemer` — Verwijderd
- 🔴 `teller` — Verwijderd

##### `TypeKadastraleAanduiding` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `appartementsrechtvolgnummer` — Verwijderd
- 🔴 `kadastraleGemeentecode` — Verwijderd
- 🔴 `perceelnummer` — Verwijderd
- 🔴 `sectie` — Verwijderd

##### `TypeKoopsom` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `bedrag` — Verwijderd
- 🔴 `koopjaar` — Verwijderd
- 🔴 `meerOnroerendGoed` — Verwijderd

##### `TypeLabel` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `labelPositie` — Verwijderd
- 🔴 `labelTekst` — Verwijderd

##### `TypeLabelpositie` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `hoek` — Verwijderd
- 🔴 `plaatsingspunt` — Verwijderd

##### `TypeLandinrichtingsrente` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `bedrag` — Verwijderd
- 🔴 `eindjaar` — Verwijderd

#### Enumeraties

##### `typeObjectcode` — 🔴 Verwijderd

**Literals:**

- 🔴 `ligplaats` — Verwijderd
- 🔴 `nummeraanduiding` — Verwijderd
- 🔴 `openbare ruimte` — Verwijderd
- 🔴 `overig adreseerbaar object aanduiding` — Verwijderd
- 🔴 `overig benoemd terrein` — Verwijderd
- 🔴 `overig gebouwd object` — Verwijderd
- 🔴 `pand` — Verwijderd
- 🔴 `standplaats` — Verwijderd
- 🔴 `verblijfsobject` — Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelenumeratiesoort"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Enumeratiesoort

#### Enumeraties

##### `aanduidingEigenaarGebruiker` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `eigenaar` — Verwijderd
- 🔴 `eigenaar-gebruiker` — Verwijderd
- 🔴 `gebruiker` — Verwijderd
- 🔴 `medebelanghebbende` — Verwijderd

##### `aanduidingInhoudingVermissingReisdocument` — 🔴 Verwijderd

**Literals:**

- 🔴 `Ingehouden, ingeleverd` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Rechtswege` — Verwijderd
- 🔴 `Vermist` — Verwijderd

##### `aangever` — 🔴 Verwijderd

**Literals:**

- 🔴 `Echtgenoot/geregistreerd partner` — Verwijderd
- 🔴 `Gezaghouder` — Verwijderd
- 🔴 `Hoofd instelling` — Verwijderd
- 🔴 `Ingeschrevene` — Verwijderd
- 🔴 `Inwonend ouder voor meerderjarig kind` — Verwijderd
- 🔴 `Meerderjarig gemachtigde` — Verwijderd
- 🔴 `Meerderjarig inwonend kind voor ouder` — Verwijderd
- 🔴 `Verzorger` — Verwijderd

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

##### `Boolean` — 🔴 Verwijderd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `bouwkundigeBestemming` — 🔴 Verwijderd

**Literals:**

- 🔴 `CAI` — Verwijderd
- 🔴 `aanleunwoonverblijf` — Verwijderd
- 🔴 `academisch onderwijs` — Verwijderd
- 🔴 `akkerbouw` — Verwijderd
- 🔴 `algemeen voortgezet onderwijs` — Verwijderd
- 🔴 `andere doeleinden van openbaar nut` — Verwijderd
- 🔴 `basisschool` — Verwijderd
- 🔴 `begraafplaats/crematorium` — Verwijderd
- 🔴 `bejaardenwoning` — Verwijderd
- 🔴 `bejaardenwoonverblijf (in bejaardenoord, centrale keuken)` — Verwijderd
- 🔴 `bibliotheek` — Verwijderd
- 🔴 `bijzonder onderwijs` — Verwijderd
- 🔴 `bioscoop` — Verwijderd
- 🔴 `brandweer` — Verwijderd
- 🔴 `cafe/bar/restaurant` — Verwijderd
- 🔴 `congres` — Verwijderd
- 🔴 `dagverblijf` — Verwijderd
- 🔴 `defensie` — Verwijderd
- 🔴 `detailhandel` — Verwijderd
- 🔴 `dienstwoning` — Verwijderd
- 🔴 `dierenverzorging` — Verwijderd
- 🔴 `doeleinden voor agrarisch bedrijf` — Verwijderd
- 🔴 `doeleinden voor cultuur` — Verwijderd
- 🔴 `doeleinden voor gezondheidszorg` — Verwijderd
- 🔴 `doeleinden voor handel, horeca en bedrijf` — Verwijderd
- 🔴 `doeleinden voor niet-wonen` — Verwijderd
- 🔴 `doeleinden voor nutsvoorzieningen` — Verwijderd
- 🔴 `doeleinden voor onderwijs` — Verwijderd
- 🔴 `doeleinden voor recreatie` — Verwijderd
- 🔴 `doeleinden voor verkeer` — Verwijderd
- 🔴 `doeleinden voor wonen` — Verwijderd
- 🔴 `eengezinswoning` — Verwijderd
- 🔴 `elektriciteit` — Verwijderd
- 🔴 `expositie` — Verwijderd
- 🔴 `fabricage en productie` — Verwijderd
- 🔴 `gas` — Verwijderd
- 🔴 `gehandicaptenwooneenheid` — Verwijderd
- 🔴 `gemeentehuis` — Verwijderd
- 🔴 `gemengd bedrijf` — Verwijderd
- 🔴 `gevangenis/gesticht` — Verwijderd
- 🔴 `godsdienst (kerk, klooster e.d.)` — Verwijderd
- 🔴 `hoger beroepsonderwijs` — Verwijderd
- 🔴 `hotel/logies` — Verwijderd
- 🔴 `jongerenwooneenheid` — Verwijderd
- 🔴 `kantoor` — Verwijderd
- 🔴 `kinderopvang` — Verwijderd
- 🔴 `laboratoria` — Verwijderd
- 🔴 `luchtvaart` — Verwijderd
- 🔴 `meergezinswoning` — Verwijderd
- 🔴 `musea` — Verwijderd
- 🔴 `natuur en landschap` — Verwijderd
- 🔴 `onderhoud en reparatie` — Verwijderd
- 🔴 `opslag en distributie` — Verwijderd
- 🔴 `overige andere doeleinden van openbaar nut` — Verwijderd
- 🔴 `overige doeleinden voor agrarisch bedrijf` — Verwijderd
- 🔴 `overige doeleinden voor cultuur` — Verwijderd
- 🔴 `overige doeleinden voor gezondheidszorg` — Verwijderd
- 🔴 `overige doeleinden voor niet-wonen` — Verwijderd
- 🔴 `overige doeleinden voor nutsvoorzieningen` — Verwijderd
- 🔴 `overige doeleinden voor onderwijs` — Verwijderd
- 🔴 `overige doeleinden voor recreatie` — Verwijderd
- 🔴 `overige doeleinden voor verkeer` — Verwijderd
- 🔴 `polikliniek` — Verwijderd
- 🔴 `politie` — Verwijderd
- 🔴 `praktijkruimte` — Verwijderd
- 🔴 `psychiatrische inrichting` — Verwijderd
- 🔴 `recreatie` — Verwijderd
- 🔴 `recreatiewoning` — Verwijderd
- 🔴 `scheepvaart` — Verwijderd
- 🔴 `spoorwegverkeer` — Verwijderd
- 🔴 `sport binnen` — Verwijderd
- 🔴 `sport buiten` — Verwijderd
- 🔴 `stalling (fietsen/auto's)` — Verwijderd
- 🔴 `telecommunicatie` — Verwijderd
- 🔴 `theater en concert` — Verwijderd
- 🔴 `tuinbouw` — Verwijderd
- 🔴 `veeteelt` — Verwijderd
- 🔴 `verpleegtehuis` — Verwijderd
- 🔴 `verzorgingstehuis en bejaardentehuis` — Verwijderd
- 🔴 `vrijetijds onderwijs` — Verwijderd
- 🔴 `waternuts doeleinden` — Verwijderd
- 🔴 `waterschaps en waterverdediging` — Verwijderd
- 🔴 `wegverkeer` — Verwijderd
- 🔴 `wijk-/buurt-/verenigingsactiviteiten` — Verwijderd
- 🔴 `wijkverzorging` — Verwijderd
- 🔴 `ziekenhuis` — Verwijderd
- 🔴 `zorgwoonverblijf` — Verwijderd
- 🔴 `zwembad` — Verwijderd

##### `bronAdresBuitenland` — 🔴 Verwijderd

**Literals:**

- 🔴 `aangewezen bestuursorgaan` — Verwijderd
- 🔴 `college` — Verwijderd

##### `burgelijkeStaat` — 🔴 Verwijderd

**Literals:**

- 🔴 `achtergebeleven partner` — Verwijderd
- 🔴 `gehuwd` — Verwijderd
- 🔴 `gescheiden` — Verwijderd
- 🔴 `onbekend` — Verwijderd
- 🔴 `ongehuwd en nooit gehuwd geweest` — Verwijderd
- 🔴 `parnetschap beeeindigd` — Verwijderd
- 🔴 `partnerschap` — Verwijderd
- 🔴 `weduwe / weduwnaar` — Verwijderd

##### `codeExploitant` — 🔴 Verwijderd

**Literals:**

- 🔴 `derden (niet zijnde gemeente` — Verwijderd
- 🔴 `erfpacht uitgegeven` — Verwijderd
- 🔴 `erfpacht verkregen` — Verwijderd
- 🔴 `gedeeltelijk eigendom` — Verwijderd
- 🔴 `onbekend/handmatig oplossen` — Verwijderd
- 🔴 `overige zakelijk rechten verkregen` — Verwijderd
- 🔴 `overige zakelijk rechten verleend` — Verwijderd
- 🔴 `recht van opstal verkregen` — Verwijderd
- 🔴 `recht van opstal verleend` — Verwijderd
- 🔴 `vol eigendom` — Verwijderd

##### `functieOndersteunendWegdeel` — 🔴 Verwijderd

**Literals:**

- 🔴 `berm` — Verwijderd
- 🔴 `verkeerseiland` — Verwijderd

##### `functieSpoor` — 🔴 Verwijderd

**Literals:**

- 🔴 `(haven)kraan` — Verwijderd
- 🔴 `sneltram` — Verwijderd
- 🔴 `tram` — Verwijderd
- 🔴 `trein` — Verwijderd

##### `functieWeg` — 🔴 Verwijderd

**Literals:**

- 🔴 `OV-baan` — Verwijderd
- 🔴 `baan voor vliegverkeer` — Verwijderd
- 🔴 `fietspad` — Verwijderd
- 🔴 `inrit` — Verwijderd
- 🔴 `overweg` — Verwijderd
- 🔴 `parkeervlak` — Verwijderd
- 🔴 `rijbaan autosnelweg` — Verwijderd
- 🔴 `rijbaan autoweg` — Verwijderd
- 🔴 `rijbaan lokale weg` — Verwijderd
- 🔴 `rijbaan regionale weg` — Verwijderd
- 🔴 `ruiterpad` — Verwijderd
- 🔴 `spoorbaan` — Verwijderd
- 🔴 `voetgangersgebied` — Verwijderd
- 🔴 `voetpad` — Verwijderd
- 🔴 `voetpad op trap` — Verwijderd
- 🔴 `woonerf` — Verwijderd

##### `functieWegPlus` — 🔴 Verwijderd

**Literals:**

- 🔴 `calamiteitendoorstee` — Verwijderd
- 🔴 `verbindingsweg` — Verwijderd
- 🔴 `verkeersdrempel` — Verwijderd

##### `fysiekVoorkomenBegroeidTerrein` — 🔴 Verwijderd

**Literals:**

- 🔴 `boomteelt` — Verwijderd
- 🔴 `bouwland` — Verwijderd
- 🔴 `duin` — Verwijderd
- 🔴 `fruitteelt` — Verwijderd
- 🔴 `gemengd bos` — Verwijderd
- 🔴 `grasland agrarisch` — Verwijderd
- 🔴 `grasland overig` — Verwijderd
- 🔴 `groenvoorziening` — Verwijderd
- 🔴 `heide` — Verwijderd
- 🔴 `houtwal` — Verwijderd
- 🔴 `kwelder` — Verwijderd
- 🔴 `loofbos` — Verwijderd
- 🔴 `moeras` — Verwijderd
- 🔴 `naaldbos` — Verwijderd
- 🔴 `rietland` — Verwijderd
- 🔴 `struiken` — Verwijderd

##### `fysiekVoorkomenBegroeidTerreinPlus` — 🔴 Verwijderd

**Literals:**

- 🔴 `akkerbouw` — Verwijderd
- 🔴 `bodembedekkers` — Verwijderd
- 🔴 `bollenteelt` — Verwijderd
- 🔴 `bosplantsoen` — Verwijderd
- 🔴 `braakliggend` — Verwijderd
- 🔴 `gesloten duinvegetatie` — Verwijderd
- 🔴 `gras en kruidachtigen` — Verwijderd
- 🔴 `grien en hakhout` — Verwijderd
- 🔴 `heesters` — Verwijderd
- 🔴 `hoogstam boomgaarden` — Verwijderd
- 🔴 `klein fruit` — Verwijderd
- 🔴 `laagstam boomgaarden` — Verwijderd
- 🔴 `open duinvegetatie` — Verwijderd
- 🔴 `planten` — Verwijderd
- 🔴 `struikrozen` — Verwijderd
- 🔴 `vollegrondsteelt` — Verwijderd
- 🔴 `wijngaarden` — Verwijderd

##### `fysiekVoorkomenOnbegroeidTerrein` — 🔴 Verwijderd

**Literals:**

- 🔴 `Gesloten verharding` — Verwijderd
- 🔴 `erf` — Verwijderd
- 🔴 `half verhard` — Verwijderd
- 🔴 `onverhard` — Verwijderd
- 🔴 `open verharding` — Verwijderd
- 🔴 `zand` — Verwijderd

##### `fysiekVoorkomenOnbegroeidTerreinPlus` — 🔴 Verwijderd

**Literals:**

- 🔴 `asfalt` — Verwijderd
- 🔴 `betonelement` — Verwijderd
- 🔴 `betonstraatstenen` — Verwijderd
- 🔴 `boomschors` — Verwijderd
- 🔴 `cementbeton` — Verwijderd
- 🔴 `gebakken klinkers` — Verwijderd
- 🔴 `grasklinkers` — Verwijderd
- 🔴 `gravel` — Verwijderd
- 🔴 `grind` — Verwijderd
- 🔴 `kunststof` — Verwijderd
- 🔴 `puin` — Verwijderd
- 🔴 `schelpen` — Verwijderd
- 🔴 `sierbestrating` — Verwijderd
- 🔴 `strand en strandwal` — Verwijderd
- 🔴 `tegels` — Verwijderd
- 🔴 `zand` — Verwijderd
- 🔴 `zandverstuiving` — Verwijderd

##### `fysiekVoorkomenOndersteunendWegdeel` — 🔴 Verwijderd

**Literals:**

- 🔴 `gesloten verharding` — Verwijderd
- 🔴 `groenvoorziening` — Verwijderd
- 🔴 `half verhard` — Verwijderd
- 🔴 `onverhard` — Verwijderd

##### `fysiekVoorkomenOndersteunendWegdeelPlus` — 🔴 Verwijderd

**Literals:**

- 🔴 `asfalt` — Verwijderd
- 🔴 `beton element` — Verwijderd
- 🔴 `betonstraatstenen` — Verwijderd
- 🔴 `bodembedekkers` — Verwijderd
- 🔴 `boomschors` — Verwijderd
- 🔴 `bosplantsoen` — Verwijderd
- 🔴 `cementbeton` — Verwijderd
- 🔴 `gebakken klinkers` — Verwijderd
- 🔴 `gras- en kruidachtigen` — Verwijderd
- 🔴 `grasklinkers` — Verwijderd
- 🔴 `gravel` — Verwijderd
- 🔴 `grind` — Verwijderd
- 🔴 `heesters` — Verwijderd
- 🔴 `planten` — Verwijderd
- 🔴 `puin` — Verwijderd
- 🔴 `schelpen` — Verwijderd
- 🔴 `sierbestrating` — Verwijderd
- 🔴 `struikrozen` — Verwijderd
- 🔴 `tegels` — Verwijderd
- 🔴 `zand` — Verwijderd

##### `fysiekVoorkomenWeg` — 🔴 Verwijderd

**Literals:**

- 🔴 `gesloten verharding` — Verwijderd
- 🔴 `half verhard` — Verwijderd
- 🔴 `onverhard` — Verwijderd
- 🔴 `open verharding` — Verwijderd

##### `fysiekVoorkomenWegPlus` — 🔴 Verwijderd

**Literals:**

- 🔴 `asfalt` — Verwijderd
- 🔴 `beton element` — Verwijderd
- 🔴 `betonstraatstenen` — Verwijderd
- 🔴 `boomschors` — Verwijderd
- 🔴 `cementbeton` — Verwijderd
- 🔴 `gebakken klinkers` — Verwijderd
- 🔴 `grasklinkers` — Verwijderd
- 🔴 `gravel` — Verwijderd
- 🔴 `grind` — Verwijderd
- 🔴 `puin` — Verwijderd
- 🔴 `schelpen` — Verwijderd
- 🔴 `sierbestrating` — Verwijderd
- 🔴 `tegels` — Verwijderd
- 🔴 `zand` — Verwijderd

##### `gebruiksdoel` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `bijeenkomstfunctie` — Verwijderd
- 🔴 `celfunctie` — Verwijderd
- 🔴 `gezondheidszorgfunctie` — Verwijderd
- 🔴 `industriefunctie` — Verwijderd
- 🔴 `kantoorfunctie` — Verwijderd
- 🔴 `logiesfunctie` — Verwijderd
- 🔴 `onderwijsfunctie` — Verwijderd
- 🔴 `overige gebruiksfunctie` — Verwijderd
- 🔴 `sportfunctie` — Verwijderd
- 🔴 `winkelfunctie` — Verwijderd
- 🔴 `woonfunctie` — Verwijderd

##### `geslacht` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Man` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Vrouw` — Verwijderd

##### `Gezinsrelatie` — 🔴 Verwijderd

**Literals:**

- 🔴 `Alleenstaand/Samenwonend` — Verwijderd
- 🔴 `Echtgenote binnen gezin` — Verwijderd
- 🔴 `Hoofd gezin met kind(eren)` — Verwijderd
- 🔴 `Hoofd gezin zonder kind(eren)` — Verwijderd
- 🔴 `Hoofd huwelijk gelijk geslacht` — Verwijderd
- 🔴 `Hoofd partnerrelatie` — Verwijderd
- 🔴 `Kind` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Ouder met kind(eren)` — Verwijderd

##### `Huishoudensoort` — 🔴 Verwijderd

**Literals:**

- 🔴 `2 personen, vaste partners, een of meer thuiswonende kinderen` — Verwijderd
- 🔴 `2 personen, vaste partners, geen thuiswonende kinderen` — Verwijderd
- 🔴 `alleenstaand (inclusief andere personen die in hetzelfde object wonen, maar een eigen huishouding voeren)` — Verwijderd
- 🔴 `eenoudergezin, ouder met een of meer thuiswonende kinderen` — Verwijderd
- 🔴 `institutioneel huishouden` — Verwijderd
- 🔴 `overig particulier huishouden (samenwoning van personen die geen partnerrelatie onderhouden of een ouder-kindrelatie hebben, maar wel gezamenlijk een huishouding voeren)` — Verwijderd

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

##### `inwinningsmethodeOppervlakte` — 🔴 Verwijderd

**Literals:**

- 🔴 `gemeten op basis van de bouwtekening` — Verwijderd
- 🔴 `initiële vulling d.m.v. conversietabel inhoud-oppervlak` — Verwijderd
- 🔴 `initiële vulling d.m.v. gegevens bouw- en woningtoezicht` — Verwijderd
- 🔴 `initiële vulling d.m.v. gegevens woningbouwvereniging` — Verwijderd
- 🔴 `initiële vulling d.m.v. oppervlaktegegevens WOZ-administratie` — Verwijderd
- 🔴 `initiële vulling d.m.v. overige brongegevens` — Verwijderd
- 🔴 `overgenomen uit bouwaanvraag` — Verwijderd
- 🔴 `ter plaatse ingemeten` — Verwijderd

##### `naamgebruik` — 🔴 Verwijderd

**Literals:**

- 🔴 `Eigen` — Verwijderd
- 🔴 `Eigen, partner` — Verwijderd
- 🔴 `Partner` — Verwijderd
- 🔴 `Partner, eigen` — Verwijderd

##### `ontsluitingswijzeVerdieping` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `lift` — Verwijderd
- 🔴 `roltrap` — Verwijderd
- 🔴 `trap` — Verwijderd

##### `predicaat` — 🔴 Verwijderd

**Literals:**

- 🔴 `Hare Hoogheid` — Verwijderd
- 🔴 `Hare Koninklijke Hoogheid` — Verwijderd
- 🔴 `Zijne Hoogheid` — Verwijderd
- 🔴 `Zijne Koninklijke Hoogheid` — Verwijderd
- 🔴 `jonkheer` — Verwijderd
- 🔴 `jonkvrouw` — Verwijderd

##### `redenEindeRelatie` — 🔴 Verwijderd

**Literals:**

- 🔴 `Echtscheiding, ontbinding of eindigen conform Nederlands recht` — Verwijderd
- 🔴 `Naar vreemd recht anders beëindigd` — Verwijderd
- 🔴 `Nietigverklaring` — Verwijderd
- 🔴 `Omzetting van soort verbintenis` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Overlijden partner` — Verwijderd
- 🔴 `Rechtsvermoeden van overlijden partner` — Verwijderd
- 🔴 `Vermissing van een persoon gevolgd door andere verbintenis` — Verwijderd

##### `redenWijzigingAdres` — 🔴 Verwijderd

**Literals:**

- 🔴 `Aangifte door persoon` — Verwijderd
- 🔴 `Ambtshalve` — Verwijderd
- 🔴 `Infrastructurele wijziging` — Verwijderd
- 🔴 `Ministerieel besluit` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Technische wijzigingen i.v.m. BAG` — Verwijderd

##### `soortBewind` — 🔴 Verwijderd

**Literals:**

- 🔴 `onder bewind` — Verwijderd
- 🔴 `provisioneel bewind` — Verwijderd

##### `soortBijzondereRechtstoestandNatuurlijkPersoon` — 🔴 Verwijderd

**Literals:**

- 🔴 `faillissement` — Verwijderd
- 🔴 `schuldsanering` — Verwijderd
- 🔴 `surseanse van betaling` — Verwijderd

##### `soortBijzondereRechtstoestandNietNatuurlijkPersoon` — 🔴 Verwijderd

**Literals:**

- 🔴 `faillissement` — Verwijderd
- 🔴 `surseanse van betaling` — Verwijderd

##### `soortGebruik` — 🔴 Verwijderd

**Literals:**

- 🔴 `boerderij` — Verwijderd
- 🔴 `niet-woning` — Verwijderd
- 🔴 `niet-woning deels in gebruik als woning` — Verwijderd
- 🔴 `recreatiewoning en overige woningen` — Verwijderd
- 🔴 `sluimerend WOZ-object` — Verwijderd
- 🔴 `terrein` — Verwijderd
- 🔴 `uitgezonderd gebouwd object` — Verwijderd
- 🔴 `uitgezonderd ongebouwd object` — Verwijderd
- 🔴 `woning dienend tot hoofdverblijf` — Verwijderd
- 🔴 `woning met praktijkruimte` — Verwijderd

##### `soortMigratie` — 🔴 Verwijderd

**Literals:**

- 🔴 `Emigratie` — Verwijderd
- 🔴 `Immigratie` — Verwijderd

##### `soortPubliekrechtelijkRechtsvorm` — 🔴 Verwijderd

**Literals:**

- 🔴 `Adviescollege` — Verwijderd
- 🔴 `Baten en Lastendienst de Staat` — Verwijderd
- 🔴 `Bedrijfsvoeringsorganisatie` — Verwijderd
- 🔴 `Gemeente` — Verwijderd
- 🔴 `Lichaam met grondwettelijke bevoegdheid` — Verwijderd
- 🔴 `Ministerie de Staat` — Verwijderd
- 🔴 `Openbaar Lichaam` — Verwijderd
- 🔴 `Provincie` — Verwijderd
- 🔴 `Rechtspersoon met wettelijke taak` — Verwijderd
- 🔴 `Universiteit of academisch ziekenhuis` — Verwijderd
- 🔴 `Waterschap` — Verwijderd
- 🔴 `Zelfstandig Bestuursorgaan` — Verwijderd

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

##### `soortWoonobject` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `bijzonder woongebouw` — Verwijderd
- 🔴 `overig woonverblijf` — Verwijderd
- 🔴 `recreatiewoning` — Verwijderd
- 🔴 `woning` — Verwijderd
- 🔴 `wooneenheid` — Verwijderd

##### `StatLigplaatsStandplaats` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `plaats aangewezen` — Verwijderd
- 🔴 `plaats ingetrokken` — Verwijderd

##### `statusGeoObject` — 🔴 Verwijderd

**Literals:**

- 🔴 `bestaand` — Verwijderd
- 🔴 `historie` — Verwijderd
- 🔴 `plan` — Verwijderd

##### `statusNummeraanduiding` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `naamgeving ingetrokken` — Verwijderd
- 🔴 `naamgeving uitgegeven` — Verwijderd

##### `statusOpenbareRuimte` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `naamgeving ingetrokken` — Verwijderd
- 🔴 `naamgeving uitgegeven` — Verwijderd

##### `statusPand` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `bouw gestart` — Verwijderd
- 🔴 `bouwaanvraag ontvangen` — Verwijderd
- 🔴 `bouwvergunning verleend` — Verwijderd
- 🔴 `niet gerealiseerd pand` — Verwijderd
- 🔴 `pand buiten gebruik` — Verwijderd
- 🔴 `pand gesloopt` — Verwijderd
- 🔴 `pand in gebruik` — Verwijderd
- 🔴 `pand in gebruik (niet ingemeten)` — Verwijderd
- 🔴 `pand ten onrechte opgevoerd` — Verwijderd
- 🔴 `sloopvergunning verleend` — Verwijderd
- 🔴 `verbouwing pand` — Verwijderd

##### `statusVerblijfsobject` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `niet gerealiseerd verblijfsobject` — Verwijderd
- 🔴 `verblijfsobject buiten gebruik` — Verwijderd
- 🔴 `verblijfsobject gevormd` — Verwijderd
- 🔴 `verblijfsobject in gebruik` — Verwijderd
- 🔴 `verblijfsobject in gebruik (niet ingemeten)` — Verwijderd
- 🔴 `verblijfsobject ingetrokken` — Verwijderd

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

##### `statusWoonplaats` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `woonplaats aangewezen` — Verwijderd
- 🔴 `woonplaats ingetrokken` — Verwijderd

##### `statusWOZ(Deel)Object` — 🔴 Verwijderd

**Literals:**

- 🔴 `actief` — Verwijderd
- 🔴 `beëindigd` — Verwijderd
- 🔴 `gevormd, niet actief` — Verwijderd
- 🔴 `ten onrechte opgevoerd` — Verwijderd

##### `statusWOZ-Beschikking` — 🔴 Verwijderd

**Literals:**

- 🔴 `arrest Hoge Raad, beschikking gehandhaafd` — Verwijderd
- 🔴 `arrest Hoge Raad, geding verwezen` — Verwijderd
- 🔴 `arrest Hoge Raad, vastgestelde waarde veranderd` — Verwijderd
- 🔴 `beroep aangetekend` — Verwijderd
- 🔴 `beschikking genomen` — Verwijderd
- 🔴 `bezwaar afgehandeld, beschikking gehandhaafd` — Verwijderd
- 🔴 `bezwaar afgehandeld, vastgestelde waarde veranderd` — Verwijderd
- 🔴 `bezwaar ingediend` — Verwijderd
- 🔴 `cassatie ingesteld` — Verwijderd
- 🔴 `herzieningsbeschikking` — Verwijderd
- 🔴 `hoger beroep aangetekend` — Verwijderd
- 🔴 `uitspraak beroep, beschikking gehandhaafd` — Verwijderd
- 🔴 `uitspraak beroep, vastgestelde waarde veranderd` — Verwijderd
- 🔴 `uitspraak hoger beroep, beschikking gehandhaafd` — Verwijderd
- 🔴 `uitspraak hoger beroep, vastgestelde waarde veranderd` — Verwijderd
- 🔴 `vernietiging beschikking` — Verwijderd
- 🔴 `waarde ambtshalve verminderd` — Verwijderd
- 🔴 `waarde te gebruiken voor voorlopige aanslag` — Verwijderd

##### `typeObjectcode` — 🔴 Verwijderd

**Literals:**

- 🔴 `ligplaats` — Verwijderd
- 🔴 `nummeraanduiding` — Verwijderd
- 🔴 `openbare ruimte` — Verwijderd
- 🔴 `overig adreseerbaar object aanduiding` — Verwijderd
- 🔴 `overig benoemd terrein` — Verwijderd
- 🔴 `overig gebouwd object` — Verwijderd
- 🔴 `pand` — Verwijderd
- 🔴 `standplaats` — Verwijderd
- 🔴 `verblijfsobject` — Verwijderd

##### `typeOverbrugging` — 🔴 Verwijderd

**Literals:**

- 🔴 `aquaduct` — Verwijderd
- 🔴 `brug` — Verwijderd
- 🔴 `ecoduct` — Verwijderd
- 🔴 `fly-over` — Verwijderd
- 🔴 `viaduct` — Verwijderd

##### `typeringAppartementsrechtsplitsing` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `hoofdsplitsing` — Verwijderd
- 🔴 `ondersplitsing` — Verwijderd
- 🔴 `splitsingafkooperfpacht` — Verwijderd

##### `typeringFunctie` — 🔴 Verwijderd

**Literals:**

- 🔴 `beheerder` — Verwijderd
- 🔴 `bestuurder` — Verwijderd
- 🔴 `bevoegd functionaris` — Verwijderd
- 🔴 `bewaarder boeken en bescheiden` — Verwijderd
- 🔴 `bewindvoerder` — Verwijderd
- 🔴 `boekhouder` — Verwijderd
- 🔴 `commissaris` — Verwijderd
- 🔴 `curator` — Verwijderd
- 🔴 `enig aandeelhouder` — Verwijderd
- 🔴 `functionaris volgens buitenlands recht` — Verwijderd
- 🔴 `gevolmachtigde` — Verwijderd
- 🔴 `handelsagent` — Verwijderd
- 🔴 `houder niet volgestorte aandelen` — Verwijderd
- 🔴 `lid EESV` — Verwijderd
- 🔴 `lid rederij` — Verwijderd
- 🔴 `lid toezichthoudend orgaan` — Verwijderd
- 🔴 `lid van het besturend orgaan` — Verwijderd
- 🔴 `lid van het leidinggevend orgaan` — Verwijderd
- 🔴 `maat` — Verwijderd
- 🔴 `mede-eigenaar` — Verwijderd
- 🔴 `persoon krachten statuten bevoegd bij ontstentenis of belet van de bestuurders` — Verwijderd
- 🔴 `privaatrechtelijk gevolmachtigde` — Verwijderd
- 🔴 `publiekrechtelijke rechtspersoon` — Verwijderd
- 🔴 `rechter commissaris` — Verwijderd
- 🔴 `vennoot` — Verwijderd
- 🔴 `vereffenaar` — Verwijderd

##### `typeringFunctionaris` — 🔴 Verwijderd

**Literals:**

- 🔴 `Aansprakelijke` — Verwijderd
- 🔴 `Bestuursfunctie` — Verwijderd
- 🔴 `Functionaris bijzondere status` — Verwijderd
- 🔴 `Gemachtigde` — Verwijderd
- 🔴 `Overig functionaris` — Verwijderd
- 🔴 `Publiekrechtelijke functionaris` — Verwijderd

##### `typeringFunctioneelGebied` — 🔴 Verwijderd

**Literals:**

- 🔴 `bedrijvigheid` — Verwijderd
- 🔴 `begraafplaats` — Verwijderd
- 🔴 `benzinestation` — Verwijderd
- 🔴 `bewoning` — Verwijderd
- 🔴 `bushalte` — Verwijderd
- 🔴 `carpoolplaats` — Verwijderd
- 🔴 `functioneel beheer` — Verwijderd
- 🔴 `functioneel beheer:hondenuitlaatplaats` — Verwijderd
- 🔴 `infrastructuur verkeer en vervoer` — Verwijderd
- 🔴 `infrastructuur waterstaatswerken` — Verwijderd
- 🔴 `kering` — Verwijderd
- 🔴 `landbouw` — Verwijderd
- 🔴 `maatschappelijke en / of publieksvoorziening` — Verwijderd
- 🔴 `natuur & landschap` — Verwijderd
- 🔴 `recreatie` — Verwijderd
- 🔴 `recreatie:bungalowpark` — Verwijderd
- 🔴 `recreatie:camping` — Verwijderd
- 🔴 `recreatie:park` — Verwijderd
- 🔴 `recreatie:speeltuin` — Verwijderd
- 🔴 `recreatie:sportterrein` — Verwijderd
- 🔴 `recreatie:volkstuin` — Verwijderd
- 🔴 `verzorgingsplaats` — Verwijderd
- 🔴 `waterbergingsgebied` — Verwijderd

##### `typeringGebouwinstallatie` — 🔴 Verwijderd

**Literals:**

- 🔴 `bordes` — Verwijderd
- 🔴 `luifel` — Verwijderd
- 🔴 `toegangstrap` — Verwijderd

##### `typeringIngeschrevenNietNatuurlijkPersoon` — 🔴 Verwijderd

**Literals:**

- 🔴 `buitenlandse vennootschap` — Verwijderd
- 🔴 `eenmanszaak met meerdere eigenaren` — Verwijderd
- 🔴 `rechtspersoon` — Verwijderd
- 🔴 `rechtspersoon i.o.` — Verwijderd
- 🔴 `samenwerkingsverband` — Verwijderd

##### `typeringInrichtingselement` — 🔴 Verwijderd

**Literals:**

- 🔴 `bak` — Verwijderd
- 🔴 `bord` — Verwijderd
- 🔴 `installatie` — Verwijderd
- 🔴 `kast` — Verwijderd
- 🔴 `mast` — Verwijderd
- 🔴 `paal` — Verwijderd
- 🔴 `put` — Verwijderd
- 🔴 `sensor` — Verwijderd
- 🔴 `straatmeubilair` — Verwijderd
- 🔴 `waterinrichtingselement` — Verwijderd
- 🔴 `weginrichtingselement` — Verwijderd

##### `typeringInrichtingselementPlus` — 🔴 Verwijderd

**Literals:**

- 🔴 `CAI-kast` — Verwijderd
- 🔴 `GMS kast` — Verwijderd
- 🔴 `GMS sensor` — Verwijderd
- 🔴 `abri` — Verwijderd
- 🔴 `afsluitpaal` — Verwijderd
- 🔴 `afval aparte plaats` — Verwijderd
- 🔴 `afvalbak` — Verwijderd
- 🔴 `balustrade` — Verwijderd
- 🔴 `bank` — Verwijderd
- 🔴 `benzine- / olieput` — Verwijderd
- 🔴 `betaalautomaat` — Verwijderd
- 🔴 `betonning` — Verwijderd
- 🔴 `bloembak` — Verwijderd
- 🔴 `bolder` — Verwijderd
- 🔴 `boomspiegel` — Verwijderd
- 🔴 `bovenleidingmast` — Verwijderd
- 🔴 `brandkraan / -put` — Verwijderd
- 🔴 `brievenbus` — Verwijderd
- 🔴 `camera` — Verwijderd
- 🔴 `container` — Verwijderd
- 🔴 `debietmeter` — Verwijderd
- 🔴 `detectielus` — Verwijderd
- 🔴 `dijkpaal` — Verwijderd
- 🔴 `drainageput` — Verwijderd
- 🔴 `drinkbak` — Verwijderd
- 🔴 `drukknoppaal` — Verwijderd
- 🔴 `dynamische snelheidsindicator` — Verwijderd
- 🔴 `elektrakast` — Verwijderd
- 🔴 `fietsenkluis` — Verwijderd
- 🔴 `fietsenrek` — Verwijderd
- 🔴 `flitser` — Verwijderd
- 🔴 `fontein` — Verwijderd
- 🔴 `gaskast` — Verwijderd
- 🔴 `gasput` — Verwijderd
- 🔴 `geleideconstructie` — Verwijderd
- 🔴 `geleidewerk` — Verwijderd
- 🔴 `grensmarkering` — Verwijderd
- 🔴 `haltepaal` — Verwijderd
- 🔴 `hectometerpaal` — Verwijderd
- 🔴 `herdenkingsmonument` — Verwijderd
- 🔴 `hoogtedetectieapparaat` — Verwijderd
- 🔴 `hoogtemerk` — Verwijderd
- 🔴 `informatiebord` — Verwijderd
- 🔴 `inspectie- / rioolput` — Verwijderd
- 🔴 `kolk` — Verwijderd
- 🔴 `kunstobject` — Verwijderd
- 🔴 `laagspanningsmast` — Verwijderd
- 🔴 `lichtcel` — Verwijderd
- 🔴 `lichtmast` — Verwijderd
- 🔴 `lichtpunt` — Verwijderd
- 🔴 `lijnafwatering` — Verwijderd
- 🔴 `meerpaal` — Verwijderd
- 🔴 `molgoot` — Verwijderd
- 🔴 `openbaar toilet` — Verwijderd
- 🔴 `openbare verlichtingskast` — Verwijderd
- 🔴 `parkeerbeugel` — Verwijderd
- 🔴 `picknicktafel` — Verwijderd
- 🔴 `plaatsnaambord` — Verwijderd
- 🔴 `poller` — Verwijderd
- 🔴 `pomp` — Verwijderd
- 🔴 `portaal` — Verwijderd
- 🔴 `praatpaal` — Verwijderd
- 🔴 `radar detector` — Verwijderd
- 🔴 `radarmast` — Verwijderd
- 🔴 `reclamebord` — Verwijderd
- 🔴 `reclamezuil` — Verwijderd
- 🔴 `remmingswerk` — Verwijderd
- 🔴 `rioolkast` — Verwijderd
- 🔴 `scheepvaartbord` — Verwijderd
- 🔴 `sirene` — Verwijderd
- 🔴 `slagboom` — Verwijderd
- 🔴 `speelvoorziening` — Verwijderd
- 🔴 `straalzender` — Verwijderd
- 🔴 `straatnaambord` — Verwijderd
- 🔴 `telecom kast` — Verwijderd
- 🔴 `telefooncel` — Verwijderd
- 🔴 `telkast` — Verwijderd
- 🔴 `telpaal` — Verwijderd
- 🔴 `verblindingswering` — Verwijderd
- 🔴 `verkeersbord` — Verwijderd
- 🔴 `verkeersbordpaal` — Verwijderd
- 🔴 `verkeersregelinstallatiekast` — Verwijderd
- 🔴 `verkeersregelinstallatiepaal` — Verwijderd
- 🔴 `verklikker transportleiding` — Verwijderd
- 🔴 `vlaggenmast` — Verwijderd
- 🔴 `vuilvang` — Verwijderd
- 🔴 `waarschuwingshek` — Verwijderd
- 🔴 `waterleidingput` — Verwijderd
- 🔴 `waterstandmeter` — Verwijderd
- 🔴 `weerstation` — Verwijderd
- 🔴 `wegmarkering` — Verwijderd
- 🔴 `wegwijzer` — Verwijderd
- 🔴 `wildrooster` — Verwijderd
- 🔴 `windmeter` — Verwijderd
- 🔴 `zand- / zoutbak` — Verwijderd
- 🔴 `zendmast` — Verwijderd
- 🔴 `zonnepaneel` — Verwijderd

##### `typeringKunstwerk` — 🔴 Verwijderd

**Literals:**

- 🔴 `bodemval` — Verwijderd
- 🔴 `coupure` — Verwijderd
- 🔴 `duiker` — Verwijderd
- 🔴 `faunavoorziening` — Verwijderd
- 🔴 `gemaal` — Verwijderd
- 🔴 `hoogspanningsmast` — Verwijderd
- 🔴 `keermuur` — Verwijderd
- 🔴 `overkluizing` — Verwijderd
- 🔴 `perron` — Verwijderd
- 🔴 `ponton` — Verwijderd
- 🔴 `sluis` — Verwijderd
- 🔴 `steiger` — Verwijderd
- 🔴 `strekdam` — Verwijderd
- 🔴 `stuw` — Verwijderd
- 🔴 `vispassage` — Verwijderd
- 🔴 `voorde` — Verwijderd

##### `typeringOndersteunendWater` — 🔴 Verwijderd

**Literals:**

- 🔴 `oever, slootkant` — Verwijderd
- 🔴 `slik` — Verwijderd

##### `typeringOpenbareRuimte` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `administratief gebied` — Verwijderd
- 🔴 `functioneel gebied` — Verwijderd
- 🔴 `kunstwerk` — Verwijderd
- 🔴 `landschappelijk gebied` — Verwijderd
- 🔴 `spoorbaan` — Verwijderd
- 🔴 `terrein` — Verwijderd
- 🔴 `water` — Verwijderd
- 🔴 `weg` — Verwijderd

##### `typeringOverbruggingsdeel` — 🔴 Verwijderd

**Literals:**

- 🔴 `dek` — Verwijderd
- 🔴 `landhoofd` — Verwijderd
- 🔴 `pijler` — Verwijderd
- 🔴 `pyloon` — Verwijderd
- 🔴 `sloof` — Verwijderd

##### `typeringOverigBouwwerk` — 🔴 Verwijderd

**Literals:**

- 🔴 `bassin` — Verwijderd
- 🔴 `bezinkbak` — Verwijderd
- 🔴 `bunker` — Verwijderd
- 🔴 `lage trafo` — Verwijderd
- 🔴 `open loods` — Verwijderd
- 🔴 `opslagtank` — Verwijderd
- 🔴 `overkapping` — Verwijderd
- 🔴 `schuur` — Verwijderd
- 🔴 `voedersilo` — Verwijderd
- 🔴 `windturbine` — Verwijderd

##### `typeringOverigeScheiding` — 🔴 Verwijderd

**Literals:**

- 🔴 `draadraster` — Verwijderd
- 🔴 `faunaraster` — Verwijderd

##### `typeringScheiding` — 🔴 Verwijderd

**Literals:**

- 🔴 `damwand` — Verwijderd
- 🔴 `geluidsscherm` — Verwijderd
- 🔴 `hek` — Verwijderd
- 🔴 `kademuur` — Verwijderd
- 🔴 `muur` — Verwijderd
- 🔴 `walbescherming` — Verwijderd

##### `typeringVegetatieobject` — 🔴 Verwijderd

**Literals:**

- 🔴 `boom` — Verwijderd
- 🔴 `haag` — Verwijderd

##### `typeringWater` — 🔴 Verwijderd

**Literals:**

- 🔴 `greppel, droge sloot` — Verwijderd
- 🔴 `waterloop` — Verwijderd
- 🔴 `watervlakte` — Verwijderd
- 🔴 `zee` — Verwijderd

##### `typeringWaterPlus` — 🔴 Verwijderd

**Literals:**

- 🔴 `beek` — Verwijderd
- 🔴 `bron` — Verwijderd
- 🔴 `gracht` — Verwijderd
- 🔴 `haven` — Verwijderd
- 🔴 `kanaal` — Verwijderd
- 🔴 `meer, plas, ven, vijver` — Verwijderd
- 🔴 `rivier` — Verwijderd
- 🔴 `sloot` — Verwijderd

##### `typeringZekerheidsrecht` — 🔴 Verwijderd

**Literals:**

- 🔴 `beslag` — Verwijderd
- 🔴 `recht van hypotheek` — Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelgroepattribuutsoort"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Groepattribuutsoort

#### Classes

##### `Adresaanduiding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `BAGID` — Verwijderd
- 🔴 `gemeentenaam` — Verwijderd
- 🔴 `huisletter` — Verwijderd
- 🔴 `huisnummer` — Verwijderd
- 🔴 `huisnummertoevoeging` — Verwijderd
- 🔴 `postcode` — Verwijderd
- 🔴 `straatnaam` — Verwijderd

##### `CorrespondentieadresBuitenland` — 🔴 Verwijderd

**Attributen:**

- 🔴 `adresBuitenland1` — Verwijderd
- 🔴 `adresBuitenland2` — Verwijderd
- 🔴 `adresBuitenland3` — Verwijderd
- 🔴 `adresBuitenland4` — Verwijderd
- 🔴 `adresBuitenland5` — Verwijderd
- 🔴 `adresBuitenland6` — Verwijderd
- 🔴 `landCorrespondentieadres` — Verwijderd

##### `GeboorteIngeschrevenNatuurlijkPersoon` — 🔴 Verwijderd

**Attributen:**

- 🔴 `buitenlandsePlaatsGeboorte` — Verwijderd
- 🔴 `buitenlandseRegioGeboorte` — Verwijderd
- 🔴 `datumGeboorte` — Verwijderd
- 🔴 `gemeenteGeboorte` — Verwijderd
- 🔴 `landOfGebiedGeboorte` — Verwijderd
- 🔴 `omschrijvingLocatieGeboorte` — Verwijderd

##### `GeboorteIngeschrevenPersoon` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumGeboorte` — Verwijderd
- 🔴 `geboorteland` — Verwijderd
- 🔴 `geboorteplaats` — Verwijderd

##### `HandelsnamenMaatschappelijkeActiviteit` — 🔴 Verwijderd

**Attributen:**

- 🔴 `handelsnaam` — Verwijderd
- 🔴 `verkorteNaam` — Verwijderd
- 🔴 `volgorde` — Verwijderd

##### `HandelsnamenVestiging` — 🔴 Verwijderd

**Attributen:**

- 🔴 `handelsnaam` — Verwijderd
- 🔴 `verkorteNaam` — Verwijderd
- 🔴 `volgorde` — Verwijderd

##### `KoopsomKadastraleOnroerendeZaak` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumTransactie` — Verwijderd
- 🔴 `koopsom` — Verwijderd

##### `LocatieKadastraleOnroerendeZaak` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aardCultuurBebouwd` — Verwijderd
- 🔴 `locatieOmschrijving` — Verwijderd

##### `MigratieIngeschrevenNatuurlijkPersoon` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aangeverMigratie` — Verwijderd
- 🔴 `redenWijzigingMigratie` — Verwijderd
- 🔴 `soortMigratie` — Verwijderd

##### `NaamAanschrijvingNatuurlijkPersoon` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aanhefAanschrijving` — Verwijderd
- 🔴 `geslachtsnaamAanschrijving` — Verwijderd
- 🔴 `voorlettersAanschrijving` — Verwijderd
- 🔴 `voornamenAanschrijving` — Verwijderd

##### `NaamgebruikNatuurlijkPersoon` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aanhefAanschrijving` — Verwijderd
- 🔴 `adellijkeTitelNaamgebruik` — Verwijderd
- 🔴 `geslachtsnaamstamNaamgebruik` — Verwijderd

##### `NaamNatuurlijkPersoon` — 🔴 Verwijderd

**Attributen:**

- 🔴 `adellijkeTitelOfPredikaat` — Verwijderd
- 🔴 `geslachtsnaam` — Verwijderd
- 🔴 `voornamen` — Verwijderd
- 🔴 `voorvoegselGeslachtsnaam` — Verwijderd

##### `NationaliteitIngeschrevenNatuurlijkPersoon` — 🔴 Verwijderd

**Attributen:**

- 🔴 `buitenlandsPersoonsnummer` — Verwijderd
- 🔴 `nationaliteit` — Verwijderd
- 🔴 `redenVerkrijging` — Verwijderd
- 🔴 `redenVerlies` — Verwijderd

##### `NederlandseNationaliteitIngeschrevenPersoon` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aanduidingBijzonderNederlanderschap` — Verwijderd
- 🔴 `nationaliteit` — Verwijderd
- 🔴 `redenVerkrijgingNederlandseNationaliteit` — Verwijderd
- 🔴 `redenVerliesNederlandseNationaliteit` — Verwijderd

##### `OntbindingHuwelijk/geregistreerdPartnerschap` — 🔴 Verwijderd

**Attributen:**

- 🔴 `buitenlandsePlaatsEinde` — Verwijderd
- 🔴 `buitenlandseRegioEinde` — Verwijderd
- 🔴 `datumEinde` — Verwijderd
- 🔴 `gemeenteEinde` — Verwijderd
- 🔴 `landOfGebiedEinde` — Verwijderd
- 🔴 `omschrijvingLocatieEinde` — Verwijderd
- 🔴 `redenEinde` — Verwijderd

##### `OverlijdenIngeschrevenNatuurlijkPersoon` — 🔴 Verwijderd

**Attributen:**

- 🔴 `buitenlandsePlaatsOverlijden` — Verwijderd
- 🔴 `buitenlandseRegioOverlijden` — Verwijderd
- 🔴 `datumOverlijden` — Verwijderd
- 🔴 `gemeenteOverlijden` — Verwijderd
- 🔴 `landOfGebiedOverlijden` — Verwijderd
- 🔴 `omschrijvingLocatieOverlijden` — Verwijderd

##### `OverlijdenIngeschrevenPersoon` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumOverlijden` — Verwijderd
- 🔴 `landOverlijden` — Verwijderd
- 🔴 `overlijdensplaats` — Verwijderd

##### `Postadres` — 🔴 Verwijderd

**Attributen:**

- 🔴 `postadresType` — Verwijderd
- 🔴 `postbusOfAntwoordnummer` — Verwijderd
- 🔴 `postcodePostadres` — Verwijderd

##### `Rekeningnummer` — 🔴 Verwijderd

**Attributen:**

- 🔴 `BIC` — Verwijderd
- 🔴 `IBAN` — Verwijderd

##### `SamengesteldeNaamNatuurlijkPersoon` — 🔴 Verwijderd

**Attributen:**

- 🔴 `adellijkeTitel` — Verwijderd
- 🔴 `geslachtsnaamstam` — Verwijderd
- 🔴 `namenreeks` — Verwijderd
- 🔴 `predicaat` — Verwijderd
- 🔴 `scheidingsteken` — Verwijderd
- 🔴 `voornamen` — Verwijderd
- 🔴 `voorvoegsel` — Verwijderd

##### `SBIActiviteitVestiging` — 🔴 Verwijderd

**Attributen:**

- 🔴 `indicatieHoofdactiviteit` — Verwijderd
- 🔴 `SBICode` — Verwijderd

##### `SluitingOfAangaanHuwelijkOfGeregistreerdPartnerschap` — 🔴 Verwijderd

**Attributen:**

- 🔴 `buitenlandsePlaatsAanvang` — Verwijderd
- 🔴 `buitenlandseRegioAanvang` — Verwijderd
- 🔴 `datumAanvang` — Verwijderd
- 🔴 `gemeenteAanvang` — Verwijderd
- 🔴 `landOfGebiedAanvang` — Verwijderd
- 🔴 `omschrijvingLocatieAanvang` — Verwijderd

##### `SoortFunctioneelGebied` — 🔴 Verwijderd

**Attributen:**

- 🔴 `indicatiePlusBRPopulatie` — Verwijderd
- 🔴 `typeFunctioneelGebied` — Verwijderd

##### `SoortKunstwerk` — 🔴 Verwijderd

**Attributen:**

- 🔴 `indicatiePlusBRPopulatie` — Verwijderd
- 🔴 `typeKunstwerk` — Verwijderd

##### `SoortOverigBouwwerk` — 🔴 Verwijderd

**Attributen:**

- 🔴 `indicatiePlusBRPopulatie` — Verwijderd
- 🔴 `typeOverigBouwwerk` — Verwijderd

##### `SoortScheiding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `indicatiePlusBRPopulatie` — Verwijderd
- 🔴 `typeScheiding` — Verwijderd

##### `SoortSpoor` — 🔴 Verwijderd

**Attributen:**

- 🔴 `functieSpoor` — Verwijderd
- 🔴 `indicatiePlusBRPopulatie` — Verwijderd

##### `SplitsingstekeningReferentie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bronorganisatie` — Verwijderd
- 🔴 `datumCreatie` — Verwijderd
- 🔴 `identificatieTekening` — Verwijderd
- 🔴 `titel` — Verwijderd

##### `VerblijfadresIngeschrevenNatuurlijkPersoon` — 🔴 Verwijderd

**Attributen:**

- 🔴 `adresHerkomst` — Verwijderd
- 🔴 `beschrijvingLocatie` — Verwijderd

##### `VerblijfadresIngeschrevenPersoon` — 🔴 Verwijderd

**Attributen:**

- 🔴 `adresHerkomst` — Verwijderd
- 🔴 `beschrijvingLocatie` — Verwijderd

##### `VerblijfBuitenland` — 🔴 Verwijderd

**Attributen:**

- 🔴 `adresregelBuitenland1` — Verwijderd
- 🔴 `adresregelBuitenland2` — Verwijderd
- 🔴 `adresregelBuitenland3` — Verwijderd
- 🔴 `adresregelBuitenland4` — Verwijderd
- 🔴 `adresregelBuitenland5` — Verwijderd
- 🔴 `adresregelBuitenland6` — Verwijderd
- 🔴 `landOfGebiedVerblijfadres` — Verwijderd

##### `VerblijfBuitenlandSubject` — 🔴 Verwijderd

**Attributen:**

- 🔴 `adresBuitenland1` — Verwijderd
- 🔴 `adresBuitenland2` — Verwijderd
- 🔴 `adresBuitenland3` — Verwijderd
- 🔴 `landVerblijfadres` — Verwijderd

##### `VerblijfsrechtIngeschrevenNatuurlijkPersoon` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aanduidingVerblijfsrecht` — Verwijderd
- 🔴 `datumAanvangVerblijfsrecht` — Verwijderd
- 🔴 `datumMededelingVerblijfsrecht` — Verwijderd
- 🔴 `datumVoorzienEindeVerblijfsrecht` — Verwijderd

##### `VerstrekkingsbeperkingPartieelIngeschrevenNatuurlijkPersoon` — 🔴 Verwijderd

**Attributen:**

- 🔴 `gemeenteVerordening` — Verwijderd
- 🔴 `omschrijvingDerde` — Verwijderd
- 🔴 `partij` — Verwijderd

#### Enumeraties

##### `aangever` — 🔴 Verwijderd

**Literals:**

- 🔴 `Echtgenoot/geregistreerd partner` — Verwijderd
- 🔴 `Gezaghouder` — Verwijderd
- 🔴 `Hoofd instelling` — Verwijderd
- 🔴 `Ingeschrevene` — Verwijderd
- 🔴 `Inwonend ouder voor meerderjarig kind` — Verwijderd
- 🔴 `Meerderjarig gemachtigde` — Verwijderd
- 🔴 `Meerderjarig inwonend kind voor ouder` — Verwijderd
- 🔴 `Verzorger` — Verwijderd

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

##### `functieSpoor` — 🔴 Verwijderd

**Literals:**

- 🔴 `(haven)kraan` — Verwijderd
- 🔴 `sneltram` — Verwijderd
- 🔴 `tram` — Verwijderd
- 🔴 `trein` — Verwijderd

##### `predicaat` — 🔴 Verwijderd

**Literals:**

- 🔴 `Hare Hoogheid` — Verwijderd
- 🔴 `Hare Koninklijke Hoogheid` — Verwijderd
- 🔴 `Zijne Hoogheid` — Verwijderd
- 🔴 `Zijne Koninklijke Hoogheid` — Verwijderd
- 🔴 `jonkheer` — Verwijderd
- 🔴 `jonkvrouw` — Verwijderd

##### `redenEindeRelatie` — 🔴 Verwijderd

**Literals:**

- 🔴 `Echtscheiding, ontbinding of eindigen conform Nederlands recht` — Verwijderd
- 🔴 `Naar vreemd recht anders beëindigd` — Verwijderd
- 🔴 `Nietigverklaring` — Verwijderd
- 🔴 `Omzetting van soort verbintenis` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Overlijden partner` — Verwijderd
- 🔴 `Rechtsvermoeden van overlijden partner` — Verwijderd
- 🔴 `Vermissing van een persoon gevolgd door andere verbintenis` — Verwijderd

##### `redenWijzigingAdres` — 🔴 Verwijderd

**Literals:**

- 🔴 `Aangifte door persoon` — Verwijderd
- 🔴 `Ambtshalve` — Verwijderd
- 🔴 `Infrastructurele wijziging` — Verwijderd
- 🔴 `Ministerieel besluit` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Technische wijzigingen i.v.m. BAG` — Verwijderd

##### `soortMigratie` — 🔴 Verwijderd

**Literals:**

- 🔴 `Emigratie` — Verwijderd
- 🔴 `Immigratie` — Verwijderd

##### `typeringFunctioneelGebied` — 🔴 Verwijderd

**Literals:**

- 🔴 `bedrijvigheid` — Verwijderd
- 🔴 `begraafplaats` — Verwijderd
- 🔴 `benzinestation` — Verwijderd
- 🔴 `bewoning` — Verwijderd
- 🔴 `bushalte` — Verwijderd
- 🔴 `carpoolplaats` — Verwijderd
- 🔴 `functioneel beheer` — Verwijderd
- 🔴 `functioneel beheer:hondenuitlaatplaats` — Verwijderd
- 🔴 `infrastructuur verkeer en vervoer` — Verwijderd
- 🔴 `infrastructuur waterstaatswerken` — Verwijderd
- 🔴 `kering` — Verwijderd
- 🔴 `landbouw` — Verwijderd
- 🔴 `maatschappelijke en / of publieksvoorziening` — Verwijderd
- 🔴 `natuur & landschap` — Verwijderd
- 🔴 `recreatie` — Verwijderd
- 🔴 `recreatie:bungalowpark` — Verwijderd
- 🔴 `recreatie:camping` — Verwijderd
- 🔴 `recreatie:park` — Verwijderd
- 🔴 `recreatie:speeltuin` — Verwijderd
- 🔴 `recreatie:sportterrein` — Verwijderd
- 🔴 `recreatie:volkstuin` — Verwijderd
- 🔴 `verzorgingsplaats` — Verwijderd
- 🔴 `waterbergingsgebied` — Verwijderd

##### `typeringKunstwerk` — 🔴 Verwijderd

**Literals:**

- 🔴 `bodemval` — Verwijderd
- 🔴 `coupure` — Verwijderd
- 🔴 `duiker` — Verwijderd
- 🔴 `faunavoorziening` — Verwijderd
- 🔴 `gemaal` — Verwijderd
- 🔴 `hoogspanningsmast` — Verwijderd
- 🔴 `keermuur` — Verwijderd
- 🔴 `overkluizing` — Verwijderd
- 🔴 `perron` — Verwijderd
- 🔴 `ponton` — Verwijderd
- 🔴 `sluis` — Verwijderd
- 🔴 `steiger` — Verwijderd
- 🔴 `strekdam` — Verwijderd
- 🔴 `stuw` — Verwijderd
- 🔴 `vispassage` — Verwijderd
- 🔴 `voorde` — Verwijderd

##### `typeringOverigBouwwerk` — 🔴 Verwijderd

**Literals:**

- 🔴 `bassin` — Verwijderd
- 🔴 `bezinkbak` — Verwijderd
- 🔴 `bunker` — Verwijderd
- 🔴 `lage trafo` — Verwijderd
- 🔴 `open loods` — Verwijderd
- 🔴 `opslagtank` — Verwijderd
- 🔴 `overkapping` — Verwijderd
- 🔴 `schuur` — Verwijderd
- 🔴 `voedersilo` — Verwijderd
- 🔴 `windturbine` — Verwijderd

##### `typeringScheiding` — 🔴 Verwijderd

**Literals:**

- 🔴 `damwand` — Verwijderd
- 🔴 `geluidsscherm` — Verwijderd
- 🔴 `hek` — Verwijderd
- 🔴 `kademuur` — Verwijderd
- 🔴 `muur` — Verwijderd
- 🔴 `walbescherming` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `Adresaanduiding` «verwijst naar» → `Nummeraanduiding`
- 🔴 Verwijderd: `Adresaanduiding` «verwijst naar» → `Nummeraanduiding`
- 🔴 Verwijderd: `GeboorteIngeschrevenNatuurlijkPersoon` «heeft plaatsgevonden in» → `Woonplaats`
- 🔴 Verwijderd: `GeboorteIngeschrevenNatuurlijkPersoon` «heeft plaatsgevonden in» → `Woonplaats`
- 🔴 Verwijderd: `OntbindingHuwelijk/geregistreerdPartnerschap` «is ontbonden in» → `Woonplaats`
- 🔴 Verwijderd: `OntbindingHuwelijk/geregistreerdPartnerschap` «is ontbonden in» → `Woonplaats`
- 🔴 Verwijderd: `OverlijdenIngeschrevenNatuurlijkPersoon` «heeft plaatsegevonden in» → `Woonplaats`
- 🔴 Verwijderd: `OverlijdenIngeschrevenNatuurlijkPersoon` «heeft plaatsgevonden in» → `Woonplaats`
- 🔴 Verwijderd: `Postadres` «heeft als correspondentieadres postadres in» → `Woonplaats`
- 🔴 Verwijderd: `Postadres` «heeft als correspondentieadres postadres in» → `Woonplaats`
- 🔴 Verwijderd: `SluitingOfAangaanHuwelijkOfGeregistreerdPartnerschap` «is gesloten/aangegaan in» → `Woonplaats`
- 🔴 Verwijderd: `SluitingOfAangaanHuwelijkOfGeregistreerdPartnerschap` «is gesloten/aangegaan in» → `Woonplaats`
- 🔴 Verwijderd: `VerblijfadresIngeschrevenNatuurlijkPersoon` «is ingeschreven op» → `AdresseerbaarObject`
- 🔴 Verwijderd: `VerblijfadresIngeschrevenNatuurlijkPersoon` «is ingeschreven op» → `AdresseerbaarObjectAanduiding`
- 🔴 Verwijderd: `VerblijfadresIngeschrevenNatuurlijkPersoon` «verblijft in» → `Verblijfsobject`
- 🔴 Verwijderd: `VerblijfadresIngeschrevenNatuurlijkPersoon` «verblijft in» → `Verblijfsobject`
- 🔴 Verwijderd: `VerblijfadresIngeschrevenNatuurlijkPersoon` «verblijft op locatie in» → `Woonplaats`
- 🔴 Verwijderd: `VerblijfadresIngeschrevenNatuurlijkPersoon` «verblijft op» → `Ligplaats`
- 🔴 Verwijderd: `VerblijfadresIngeschrevenNatuurlijkPersoon` «verblijft op» → `Ligplaats`
- 🔴 Verwijderd: `VerblijfadresIngeschrevenNatuurlijkPersoon` «verblijft op» → `Standplaats`
- 🔴 Verwijderd: `VerblijfadresIngeschrevenNatuurlijkPersoon` «verblijft op» → `Standplaats`
- 🔴 Verwijderd: `VerblijfadresIngeschrevenNatuurlijkPersoon` «verblijft op» → `Woonplaats`

<a id="structureel-delfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelmodel-kern-rsgb"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Model Kern RSGB

#### Classes

##### `Aantekening` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aard` — Verwijderd
- 🔴 `begrenzing` — Verwijderd
- 🔴 `betreftGedeelteVanPerceel` — Verwijderd
- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumEindeRecht` — Verwijderd
- 🔴 `identificatie` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `AdresBuitenland` — 🔴 Verwijderd

**Attributen:**

- 🔴 `adresregelBuitenland1` — Verwijderd
- 🔴 `adresregelBuitenland2` — Verwijderd
- 🔴 `adresregelBuitenland3` — Verwijderd
- 🔴 `datumAanvangAdresBuitenland` — Verwijderd
- 🔴 `datumInschrijvingGemeente` — Verwijderd
- 🔴 `datumVestigingNederland` — Verwijderd
- 🔴 `gemeenteVanInschrijving` — Verwijderd
- 🔴 `landAdresBuitenland` — Verwijderd
- 🔴 `landWaarvandaanIngeschreven` — Verwijderd
- 🔴 `omschrijvingVanDeAangifteAdreshouding` — Verwijderd

##### `Appartementsrecht` — 🔴 Verwijderd

##### `Appartementsrechtsplitsing` — 🔴 Verwijderd

**Attributen:**

- 🔴 `ddentificatieAppartementsrechtsplitsing` — Verwijderd
- 🔴 `typeSplitsing` — Verwijderd

##### `BegroeidTerreindeel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheid` — Verwijderd
- 🔴 `datumEindeGeldigheid` — Verwijderd
- 🔴 `fysiekVoorkomen` — Verwijderd
- 🔴 `geometrie` — Verwijderd
- 🔴 `identificatie` — Verwijderd
- 🔴 `kruinlijngeometrie` — Verwijderd
- 🔴 `LOD0Geometrie` — Verwijderd
- 🔴 `opTalud` — Verwijderd
- 🔴 `plusFysiekVoorkomen` — Verwijderd
- 🔴 `relatieveHoogteligging` — Verwijderd
- 🔴 `status` — Verwijderd

##### `Briefadres` — 🔴 Verwijderd

**Attributen:**

- 🔴 `adresFunctie` — Verwijderd
- 🔴 `datumAanvang` — Verwijderd
- 🔴 `datumEinde` — Verwijderd
- 🔴 `omschrijvingAangifte` — Verwijderd

##### `FunctioneelGebied` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheidFunctioneelGebied` — Verwijderd
- 🔴 `datumEindeGeldigheidFunctioneelGebied` — Verwijderd
- 🔴 `geometrieFunctioneelGebied` — Verwijderd
- 🔴 `identificatieFunctioneelGebied` — Verwijderd
- 🔴 `naamFunctioneelGebied` — Verwijderd
- 🔴 `statusFunctioneelGebied` — Verwijderd

##### `Gebied` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheidBuurt` — Verwijderd
- 🔴 `datumEindeGeldigheidGebied` — Verwijderd
- 🔴 `gebiedcode` — Verwijderd
- 🔴 `gebiedsoort` — Verwijderd
- 🔴 `geometrie` — Verwijderd
- 🔴 `identificatieIMGeoBRT` — Verwijderd
- 🔴 `naam` — Verwijderd

##### `Gebouwinstallatie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheidGebouwinstallatie` — Verwijderd
- 🔴 `datumEindeGeldigheidGebouwinstallatie` — Verwijderd
- 🔴 `geometrieGebouwinstallatie` — Verwijderd
- 🔴 `identificatieGebouwinstallatie` — Verwijderd
- 🔴 `LOD0GeometrieGebouwinstallatie` — Verwijderd
- 🔴 `relatieveHoogteliggingGebouwinstallatie` — Verwijderd
- 🔴 `statusGebouwinstallatie` — Verwijderd
- 🔴 `typeGebouwinstallatie` — Verwijderd

##### `Huishouden` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheidHuishouden` — Verwijderd
- 🔴 `datumEindeGeldigheidHuishouden` — Verwijderd
- 🔴 `huishoudengrootte` — Verwijderd
- 🔴 `huishoudennummer` — Verwijderd
- 🔴 `huishoudensoort` — Verwijderd
- 🔴 `relatie` — Verwijderd

##### `IngeschrevenPersoon` — 🔴 Verwijderd

**Attributen:**

- 🔴 `adresHerkomst` — Verwijderd
- 🔴 `anummer` — Verwijderd
- 🔴 `beschrijvingLocatie` — Verwijderd
- 🔴 `buitenlandsReisdocument` — Verwijderd
- 🔴 `burgerlijkeStaat` — Verwijderd
- 🔴 `datumBeginGeldigheidVerblijfplaats` — Verwijderd
- 🔴 `datumEindeGeldigheidVerblijfsplaats` — Verwijderd
- 🔴 `datumInschrijvingGemeente` — Verwijderd
- 🔴 `datumOpschortingBijhouding` — Verwijderd
- 🔴 `datumVertrekUitNederland` — Verwijderd
- 🔴 `datumVestigingNederland` — Verwijderd
- 🔴 `gemeenteVanInschrijving` — Verwijderd
- 🔴 `gezinsrelatie` — Verwijderd
- 🔴 `indicatieGeheim` — Verwijderd
- 🔴 `ingezetene` — Verwijderd
- 🔴 `landWaarnaarVertrokken` — Verwijderd
- 🔴 `landWaarvandaanIngeschreven` — Verwijderd
- 🔴 `ouder1` — Verwijderd
- 🔴 `ouder2` — Verwijderd
- 🔴 `partnerID` — Verwijderd
- 🔴 `redenEindeBewoning` — Verwijderd
- 🔴 `redenOpschortingBijhouding` — Verwijderd
- 🔴 `signaleringReisdocument` — Verwijderd
- 🔴 `verblijfstitel` — Verwijderd

##### `Ingezetene` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aanduidingEuropeesKiesrecht` — Verwijderd
- 🔴 `aanduidingUitgeslotenKiesrecht` — Verwijderd
- 🔴 `datumVerkrijgingVerblijfstitel` — Verwijderd
- 🔴 `datumVerliesVerblijfstitel` — Verwijderd
- 🔴 `indicatieBlokkering` — Verwijderd
- 🔴 `indicatieCurateleregister` — Verwijderd
- 🔴 `indicatieGezagMinderjarige` — Verwijderd
- 🔴 `verblijfstitel` — Verwijderd

##### `Inrichtingselement` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheidInrichtingselement` — Verwijderd
- 🔴 `datumEindeGeldigheidInrichtingselement` — Verwijderd
- 🔴 `geometrieInrichtingselement` — Verwijderd
- 🔴 `identificatieInrichtingselement` — Verwijderd
- 🔴 `LOD0GeometrieInrichtingselement` — Verwijderd
- 🔴 `plusTypeInrichtingselement` — Verwijderd
- 🔴 `relatieveHoogteliggingInrichtingselement` — Verwijderd
- 🔴 `statusInrichtingselement` — Verwijderd
- 🔴 `typeInrichtingselement` — Verwijderd

##### `KadastraalPerceel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aanduidingSoortGrootte` — Verwijderd
- 🔴 `begrenzingPerceel` — Verwijderd
- 🔴 `groottePerceel` — Verwijderd
- 🔴 `indicatieDeelperceel` — Verwijderd
- 🔴 `omschrijvingDeelperceel` — Verwijderd
- 🔴 `plaatscoordinatenPerceel` — Verwijderd

##### `KadastraleOnroerendeZaak` — 🔴 Verwijderd

**Attributen:**

- 🔴 `appartementsrechtvolgnummer` — Verwijderd
- 🔴 `begrenzing` — Verwijderd
- 🔴 `cultuurcodeOnbebouwd` — Verwijderd
- 🔴 `datumBeginGeldigheid` — Verwijderd
- 🔴 `datumEindeGeldigheid` — Verwijderd
- 🔴 `identificatie` — Verwijderd
- 🔴 `kadastraleGemeente` — Verwijderd
- 🔴 `kadastraleGemeentecode` — Verwijderd
- 🔴 `koopjaar` — Verwijderd
- 🔴 `koopsom` — Verwijderd
- 🔴 `landInrichtingRenteBedrag` — Verwijderd
- 🔴 `landInrichtingRenteEindejaar` — Verwijderd
- 🔴 `ligging` — Verwijderd
- 🔴 `locatieOmschrijving` — Verwijderd
- 🔴 `oppervlakte` — Verwijderd
- 🔴 `oud` — Verwijderd
- 🔴 `perceelnummer` — Verwijderd
- 🔴 `sectie` — Verwijderd
- 🔴 `valutacode` — Verwijderd

##### `KadastraleOnroerendeZaakAantekening` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aardAantekeningKadastraalObject` — Verwijderd
- 🔴 `beschrijvingAantekeningKadastraalObject` — Verwijderd
- 🔴 `datumBeginAantekeningKadastraalObject` — Verwijderd
- 🔴 `datumEindeAantekeningKadastraalObject` — Verwijderd
- 🔴 `kadasterIdentificatieAantekening` — Verwijderd

##### `Kunstwerkdeel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheidKunstwerkdeel` — Verwijderd
- 🔴 `datumEindeGeldigheidKunstwerkdeel` — Verwijderd
- 🔴 `geometrieKunstwerkdeel` — Verwijderd
- 🔴 `identificatieKunstwerkdeel` — Verwijderd
- 🔴 `LOD0GeometrieKunstwerkdeel` — Verwijderd
- 🔴 `LOD1GeometrieKunstwerkdeel` — Verwijderd
- 🔴 `LOD2GeometrieKunstwerkdeel` — Verwijderd
- 🔴 `lod3GeometrieKunstwerkdeel` — Verwijderd
- 🔴 `relatieveHoogteliggingKunstwerkdeel` — Verwijderd
- 🔴 `statusKunstwerkdeel` — Verwijderd

##### `MaatschappelijkeActiviteit` — 🔴 Verwijderd

**Attributen:**

- 🔴 `adresBinnenland` — Verwijderd
- 🔴 `adresCorrespondentie` — Verwijderd
- 🔴 `datumAanvang` — Verwijderd
- 🔴 `datumEindeGeldig` — Verwijderd
- 🔴 `datumFaillisement` — Verwijderd
- 🔴 `indicatieEconomischActief` — Verwijderd
- 🔴 `KVKnummer` — Verwijderd
- 🔴 `rechtsvorm` — Verwijderd
- 🔴 `RSIN` — Verwijderd
- 🔴 `statutaireNaam` — Verwijderd
- 🔴 `telefoonnummer` — Verwijderd
- 🔴 `URL` — Verwijderd

##### `Nationaliteit` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Buitenlandse nationaliteit` — Verwijderd
- 🔴 `Datum einde geldigheid` — Verwijderd
- 🔴 `Datum ingang geldigheid` — Verwijderd
- 🔴 `Datum opnamen` — Verwijderd
- 🔴 `Datum verlies nationaliteit` — Verwijderd
- 🔴 `Nationaliteitcode` — Verwijderd
- 🔴 `omschrijving` — Verwijderd
- 🔴 `redenVerkrijgingNLNationaliteit` — Verwijderd
- 🔴 `redenVerliesNLNationaliteit` — Verwijderd

##### `NatuurlijkPersoon` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aanduidingNaamgebruik` — Verwijderd
- 🔴 `aanhefAanschrijving` — Verwijderd
- 🔴 `academischeTitel` — Verwijderd
- 🔴 `achternaam` — Verwijderd
- 🔴 `adellijkeTitelOfPredikaat` — Verwijderd
- 🔴 `anummer` — Verwijderd
- 🔴 `bijzonderNederlanderschap` — Verwijderd
- 🔴 `burgerservicenummer` — Verwijderd
- 🔴 `datumGeboorte` — Verwijderd
- 🔴 `datumOverlijden` — Verwijderd
- 🔴 `geboorteland` — Verwijderd
- 🔴 `geboorteplaats` — Verwijderd
- 🔴 `geslachtsaanduiding` — Verwijderd
- 🔴 `geslachtsnaam` — Verwijderd
- 🔴 `geslachtsnaamAanschrijving` — Verwijderd
- 🔴 `handlichting` — Verwijderd
- 🔴 `IndicatieAfschermingPersoonsgegevens` — Verwijderd
- 🔴 `indicatieOverleden` — Verwijderd
- 🔴 `landOverlijden` — Verwijderd
- 🔴 `nationaliteit` — Verwijderd
- 🔴 `overlijdensplaats` — Verwijderd
- 🔴 `voorlettersAanschrijving` — Verwijderd
- 🔴 `voornamen` — Verwijderd
- 🔴 `voornamenAanschrijving` — Verwijderd
- 🔴 `voorvoegselGeslachtsnaam` — Verwijderd

##### `NietNatuurlijkPersoon` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumAanvang` — Verwijderd
- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumUitschrijving` — Verwijderd
- 🔴 `datumVoortzetting` — Verwijderd
- 🔴 `faxnummer` — Verwijderd
- 🔴 `ingeschreven` — Verwijderd
- 🔴 `inOprichting` — Verwijderd
- 🔴 `KVKnummer` — Verwijderd
- 🔴 `NNPID` — Verwijderd
- 🔴 `rechtsvorm` — Verwijderd
- 🔴 `RSINNummer` — Verwijderd
- 🔴 `statutaireNaam` — Verwijderd
- 🔴 `statutaireZetel` — Verwijderd
- 🔴 `websiteURL` — Verwijderd

##### `OnbegroeidTerreindeel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheid` — Verwijderd
- 🔴 `datumEindeGeldigheid` — Verwijderd
- 🔴 `fysiekVoorkomen` — Verwijderd
- 🔴 `geometrie` — Verwijderd
- 🔴 `identificatie` — Verwijderd
- 🔴 `kruinlijngeometrie` — Verwijderd
- 🔴 `onbegroeidTerreindeelOpTalud` — Verwijderd
- 🔴 `plusFysiekVoorkomen` — Verwijderd
- 🔴 `relatieveHoogteligging` — Verwijderd
- 🔴 `status` — Verwijderd

##### `Onbestemd Adres` — 🔴 Verwijderd

**Attributen:**

- 🔴 `huisletter` — Verwijderd
- 🔴 `huisnummer` — Verwijderd
- 🔴 `huisnummertoevoeging` — Verwijderd
- 🔴 `postcode` — Verwijderd
- 🔴 `straatnaam` — Verwijderd

##### `OndersteunendWaterdeel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheid` — Verwijderd
- 🔴 `datumEindeGeldigheid` — Verwijderd
- 🔴 `geometrie` — Verwijderd
- 🔴 `identificatie` — Verwijderd
- 🔴 `plusType` — Verwijderd
- 🔴 `relatieveHoogteligging` — Verwijderd
- 🔴 `status` — Verwijderd
- 🔴 `type` — Verwijderd

##### `OndersteunendWegdeel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheid` — Verwijderd
- 🔴 `datumEindeGeldigheid` — Verwijderd
- 🔴 `functie` — Verwijderd
- 🔴 `fysiekVoorkomen` — Verwijderd
- 🔴 `geometrie` — Verwijderd
- 🔴 `identificatie` — Verwijderd
- 🔴 `kruinlijngeometrie` — Verwijderd
- 🔴 `LOD0Geometrie` — Verwijderd
- 🔴 `opTalud` — Verwijderd
- 🔴 `plusFunctie` — Verwijderd
- 🔴 `plusFysiekVoorkomen` — Verwijderd
- 🔴 `relatieveHoogteligging` — Verwijderd
- 🔴 `status` — Verwijderd

##### `Overbruggingsdeel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheidOverbruggingsdeel` — Verwijderd
- 🔴 `datumEindeGeldigheidOverbruggingsdeel` — Verwijderd
- 🔴 `geometrieOverbruggingsdeel` — Verwijderd
- 🔴 `hoortBijTypeOverbrugging` — Verwijderd
- 🔴 `identificatieOverbruggingsdeel` — Verwijderd
- 🔴 `LOD0GeometrieOverbruggingsdeel` — Verwijderd
- 🔴 `overbruggingIsBeweegbaar` — Verwijderd
- 🔴 `relatieveHoogteliggingOverbruggingsdeel` — Verwijderd
- 🔴 `statusOverbruggingsdeel` — Verwijderd
- 🔴 `typeOverbruggingsdeel` — Verwijderd

##### `OverigBenoemdTerrein` — 🔴 Verwijderd

**Attributen:**

- 🔴 `gebruiksdoelOverigBenoemdTerrein` — Verwijderd
- 🔴 `overigBenoemdTerreinIdentificatie` — Verwijderd

##### `OverigBouwwerk` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheidOverigBouwwerk` — Verwijderd
- 🔴 `datumEindeGeldigheidOverigBouwwerk` — Verwijderd
- 🔴 `geometrieOverigBouwwerk` — Verwijderd
- 🔴 `identificatieOverigBouwwerk` — Verwijderd
- 🔴 `LOD0GeometrieOverigBouwwerk` — Verwijderd
- 🔴 `LOD1GeometrieOverigBouwwerk` — Verwijderd
- 🔴 `LOD2GeometrieOverigBouwwerk` — Verwijderd
- 🔴 `lod3GeometrieOverigBouwwerk` — Verwijderd
- 🔴 `relatieveHoogteliggingOverigBouwwerk` — Verwijderd
- 🔴 `statusOverigBouwwerk` — Verwijderd

##### `OverigeAdresseerbaarObjectAanduiding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `Identificatiecode` — Verwijderd

##### `OverigeScheiding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheidOverigeScheiding` — Verwijderd
- 🔴 `datumEindeGeldigheidOverigeScheiding` — Verwijderd
- 🔴 `geometrieOverigeScheiding` — Verwijderd
- 🔴 `identificatieOverigeScheiding` — Verwijderd
- 🔴 `LOD0GeometrieOverigeScheiding` — Verwijderd
- 🔴 `LOD1GeometrieOverigeScheiding` — Verwijderd
- 🔴 `LOD2GeometrieOverigeScheiding` — Verwijderd
- 🔴 `lod3GeometrieOverigeScheiding` — Verwijderd
- 🔴 `relatieveHoogteliggingOverigeScheiding` — Verwijderd
- 🔴 `statusOverigeScheiding` — Verwijderd
- 🔴 `typeOverigeScheiding` — Verwijderd

##### `OverigGebouwdObject` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bouwjaar` — Verwijderd
- 🔴 `indicatiePlanobject` — Verwijderd
- 🔴 `overigGebouwdObjectIdentificatie` — Verwijderd

##### `Rechtspersoon` — 🔴 Verwijderd

**Attributen:**

- 🔴 `adresBinnenland` — Verwijderd
- 🔴 `adresBuitenland` — Verwijderd
- 🔴 `adresCorrespondentie` — Verwijderd
- 🔴 `emailadres` — Verwijderd
- 🔴 `faxnummer` — Verwijderd
- 🔴 `identificatie` — Verwijderd
- 🔴 `KVKnummer` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `rechtsvorm` — Verwijderd
- 🔴 `rekeningnummer` — Verwijderd
- 🔴 `telefoonnummer` — Verwijderd

##### `Reisdocument` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aanduidingInhoudingVermissing` — Verwijderd
- 🔴 `autoriteitVanAfgifte` — Verwijderd
- 🔴 `datumEindeGeldigheidDocument` — Verwijderd
- 🔴 `datumIngangDocument` — Verwijderd
- 🔴 `datumInhoudingOfVermissing` — Verwijderd
- 🔴 `datumUitgifte` — Verwijderd
- 🔴 `reisdocumentnummer` — Verwijderd
- 🔴 `soort` — Verwijderd

##### `Scheiding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheidScheiding` — Verwijderd
- 🔴 `datumEindeGeldigheidScheiding` — Verwijderd
- 🔴 `geometrieScheiding` — Verwijderd
- 🔴 `identificatieScheiding` — Verwijderd
- 🔴 `LOD0GeometrieScheiding` — Verwijderd
- 🔴 `LOD1GeometrieScheiding` — Verwijderd
- 🔴 `LOD2GeometrieScheiding` — Verwijderd
- 🔴 `lod3GeometrieScheiding` — Verwijderd
- 🔴 `relatieveHoogteliggingScheiding` — Verwijderd
- 🔴 `statusScheiding` — Verwijderd

##### `Spoor` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheidSpoor` — Verwijderd
- 🔴 `datumEindeGeldigheidSpoor` — Verwijderd
- 🔴 `geometrieSpoor` — Verwijderd
- 🔴 `identificatieSpoor` — Verwijderd
- 🔴 `LOD0GeometrieSpoor` — Verwijderd
- 🔴 `relatieveHoogteliggingSpoor` — Verwijderd
- 🔴 `statusSpoor` — Verwijderd

##### `Tenaamstelling` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aandeelInRecht` — Verwijderd
- 🔴 `burgerlijkeStaatTenTijdeVanVerkrijging` — Verwijderd
- 🔴 `datumBeginGeldigheid` — Verwijderd
- 🔴 `datumEindeGeldigheid` — Verwijderd
- 🔴 `exploitantcode` — Verwijderd
- 🔴 `identificatieTenaamstelling` — Verwijderd
- 🔴 `verklaringInzakeDerdenBescherming` — Verwijderd
- 🔴 `verkregenNamensSamenwerkingsverband` — Verwijderd

##### `Tunneldeel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheidTunneldeel` — Verwijderd
- 🔴 `datumEindeGeldigheidTunneldeel` — Verwijderd
- 🔴 `geometrieTunneldeel` — Verwijderd
- 🔴 `identificatieTunneldeel` — Verwijderd
- 🔴 `LOD0GeometrieTunneldeel` — Verwijderd
- 🔴 `relatieveHoogteliggingTunneldeel` — Verwijderd
- 🔴 `statusTunneldeel` — Verwijderd

##### `Vegetatieobject` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheidVegetatieobject` — Verwijderd
- 🔴 `datumEindeGeldigheidVegetatieobject` — Verwijderd
- 🔴 `geometrieVegetatieobject` — Verwijderd
- 🔴 `identificatieVegetatieobject` — Verwijderd
- 🔴 `LOD0GeometrieVegetatieobject` — Verwijderd
- 🔴 `relatieveHoogteliggingVegetatieobject` — Verwijderd
- 🔴 `statusVegetatieobject` — Verwijderd
- 🔴 `typeVegetatieobject` — Verwijderd

##### `Verblijfstitel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aanduidingVerblijfstitel` — Verwijderd
- 🔴 `Datum begin` — Verwijderd
- 🔴 `Datum einde` — Verwijderd
- 🔴 `Datum Opname` — Verwijderd
- 🔴 `datumBeginGeldigheidVerblijfstitel` — Verwijderd
- 🔴 `Verblijfstitel code` — Verwijderd

##### `Vestiging` — 🔴 Verwijderd

**Attributen:**

- 🔴 `commercieleVestiging` — Verwijderd
- 🔴 `datumAanvang` — Verwijderd
- 🔴 `datumEinde` — Verwijderd
- 🔴 `datumVoortzetting` — Verwijderd
- 🔴 `fulltimeWerkzameMannen` — Verwijderd
- 🔴 `fulltimeWerkzameVrouwen` — Verwijderd
- 🔴 `handelsnaam` — Verwijderd
- 🔴 `parttimeWerkzameMannen` — Verwijderd
- 🔴 `parttimeWerkzameVrouwen` — Verwijderd
- 🔴 `toevoegingAdres` — Verwijderd
- 🔴 `totaalWerkzamePersonen` — Verwijderd
- 🔴 `verkorteNaam` — Verwijderd
- 🔴 `vestigingsnummer` — Verwijderd

##### `Waterdeel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheidWaterdeel` — Verwijderd
- 🔴 `datumEindeGeldigheidWaterdeel` — Verwijderd
- 🔴 `geometrieWaterdeel` — Verwijderd
- 🔴 `identificatieWaterdeel` — Verwijderd
- 🔴 `plusTypeWaterdeel` — Verwijderd
- 🔴 `relatieveHoogteliggingWaterdeel` — Verwijderd
- 🔴 `statusWaterdeel` — Verwijderd
- 🔴 `typeWaterdeel` — Verwijderd

##### `Wegdeel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheidWegdeel` — Verwijderd
- 🔴 `datumEindeGeldigheidWegdeel` — Verwijderd
- 🔴 `functieWegdeel` — Verwijderd
- 🔴 `fysiekVoorkomenWegdeel` — Verwijderd
- 🔴 `geometrieWegdeel` — Verwijderd
- 🔴 `identificatieWegdeel` — Verwijderd
- 🔴 `kruinlijngeometrieWegdeel` — Verwijderd
- 🔴 `LOD0GeometrieWegdeel` — Verwijderd
- 🔴 `plusFunctieWegdeel` — Verwijderd
- 🔴 `plusFysiekVoorkomenWegdeel` — Verwijderd
- 🔴 `relatieveHoogteliggingWegdeel` — Verwijderd
- 🔴 `statusWegdeel` — Verwijderd
- 🔴 `wegdeelOpTalud` — Verwijderd

##### `WOZ-deelobject` — 🔴 Verwijderd

**Attributen:**

- 🔴 `codeWOZDeelobject` — Verwijderd
- 🔴 `datumBeginGeldigheidDeelobject` — Verwijderd
- 🔴 `datumEindeGeldigheidDeelobject` — Verwijderd
- 🔴 `statusWOZDeelobject` — Verwijderd
- 🔴 `WOZDeelobjectNummer` — Verwijderd

##### `WOZ-object` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheidWOZObject` — Verwijderd
- 🔴 `datumEindeGeldigheidWOZObject` — Verwijderd
- 🔴 `datumWaardepeiling` — Verwijderd
- 🔴 `gebruikscode` — Verwijderd
- 🔴 `geometrieWOZObject` — Verwijderd
- 🔴 `grondoppervlakte` — Verwijderd
- 🔴 `soortobjectcode` — Verwijderd
- 🔴 `statusWOZObject` — Verwijderd
- 🔴 `vastgesteldeWaarde` — Verwijderd
- 🔴 `WOZObjectnummer` — Verwijderd

##### `WOZ-Waarde` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumPeilingToestand` — Verwijderd
- 🔴 `datumWaardepeiling` — Verwijderd
- 🔴 `statusBeschikking` — Verwijderd
- 🔴 `vastgesteldeWaarde` — Verwijderd

##### `ZakelijkRecht` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aardZakelijkRecht` — Verwijderd
- 🔴 `datumEindeRecht` — Verwijderd
- 🔴 `datumIngangRecht` — Verwijderd
- 🔴 `gestapeld recht` — Verwijderd
- 🔴 `identificatieZakelijkRecht` — Verwijderd
- 🔴 `toelichtingBewaarder` — Verwijderd

##### `Zekerheidsrecht` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aandeelInBetrokkenRecht` — Verwijderd
- 🔴 `datumEindeRecht` — Verwijderd
- 🔴 `datumIngangRecht` — Verwijderd
- 🔴 `identificatieZekerheidsrecht` — Verwijderd
- 🔴 `omschrijvingBetrokkenRecht` — Verwijderd
- 🔴 `typeZekerheidsrecht` — Verwijderd

#### Enumeraties

##### `aanduidingInhoudingVermissingReisdocument` — 🔴 Verwijderd

**Literals:**

- 🔴 `Ingehouden, ingeleverd` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Rechtswege` — Verwijderd
- 🔴 `Vermist` — Verwijderd

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

##### `Boolean` — 🔴 Verwijderd

**Literals:**

- 🔴 `Ja` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Nee` — Verwijderd
- 🔴 `Onbekend` — Verwijderd

##### `burgelijkeStaat` — 🔴 Verwijderd

**Literals:**

- 🔴 `achtergebeleven partner` — Verwijderd
- 🔴 `gehuwd` — Verwijderd
- 🔴 `gescheiden` — Verwijderd
- 🔴 `onbekend` — Verwijderd
- 🔴 `ongehuwd en nooit gehuwd geweest` — Verwijderd
- 🔴 `parnetschap beeeindigd` — Verwijderd
- 🔴 `partnerschap` — Verwijderd
- 🔴 `weduwe / weduwnaar` — Verwijderd

##### `codeExploitant` — 🔴 Verwijderd

**Literals:**

- 🔴 `derden (niet zijnde gemeente` — Verwijderd
- 🔴 `erfpacht uitgegeven` — Verwijderd
- 🔴 `erfpacht verkregen` — Verwijderd
- 🔴 `gedeeltelijk eigendom` — Verwijderd
- 🔴 `onbekend/handmatig oplossen` — Verwijderd
- 🔴 `overige zakelijk rechten verkregen` — Verwijderd
- 🔴 `overige zakelijk rechten verleend` — Verwijderd
- 🔴 `recht van opstal verkregen` — Verwijderd
- 🔴 `recht van opstal verleend` — Verwijderd
- 🔴 `vol eigendom` — Verwijderd

##### `functieOndersteunendWegdeel` — 🔴 Verwijderd

**Literals:**

- 🔴 `berm` — Verwijderd
- 🔴 `verkeerseiland` — Verwijderd

##### `functieWeg` — 🔴 Verwijderd

**Literals:**

- 🔴 `OV-baan` — Verwijderd
- 🔴 `baan voor vliegverkeer` — Verwijderd
- 🔴 `fietspad` — Verwijderd
- 🔴 `inrit` — Verwijderd
- 🔴 `overweg` — Verwijderd
- 🔴 `parkeervlak` — Verwijderd
- 🔴 `rijbaan autosnelweg` — Verwijderd
- 🔴 `rijbaan autoweg` — Verwijderd
- 🔴 `rijbaan lokale weg` — Verwijderd
- 🔴 `rijbaan regionale weg` — Verwijderd
- 🔴 `ruiterpad` — Verwijderd
- 🔴 `spoorbaan` — Verwijderd
- 🔴 `voetgangersgebied` — Verwijderd
- 🔴 `voetpad` — Verwijderd
- 🔴 `voetpad op trap` — Verwijderd
- 🔴 `woonerf` — Verwijderd

##### `functieWegPlus` — 🔴 Verwijderd

**Literals:**

- 🔴 `calamiteitendoorstee` — Verwijderd
- 🔴 `verbindingsweg` — Verwijderd
- 🔴 `verkeersdrempel` — Verwijderd

##### `fysiekVoorkomenBegroeidTerrein` — 🔴 Verwijderd

**Literals:**

- 🔴 `boomteelt` — Verwijderd
- 🔴 `bouwland` — Verwijderd
- 🔴 `duin` — Verwijderd
- 🔴 `fruitteelt` — Verwijderd
- 🔴 `gemengd bos` — Verwijderd
- 🔴 `grasland agrarisch` — Verwijderd
- 🔴 `grasland overig` — Verwijderd
- 🔴 `groenvoorziening` — Verwijderd
- 🔴 `heide` — Verwijderd
- 🔴 `houtwal` — Verwijderd
- 🔴 `kwelder` — Verwijderd
- 🔴 `loofbos` — Verwijderd
- 🔴 `moeras` — Verwijderd
- 🔴 `naaldbos` — Verwijderd
- 🔴 `rietland` — Verwijderd
- 🔴 `struiken` — Verwijderd

##### `fysiekVoorkomenBegroeidTerreinPlus` — 🔴 Verwijderd

**Literals:**

- 🔴 `akkerbouw` — Verwijderd
- 🔴 `bodembedekkers` — Verwijderd
- 🔴 `bollenteelt` — Verwijderd
- 🔴 `bosplantsoen` — Verwijderd
- 🔴 `braakliggend` — Verwijderd
- 🔴 `gesloten duinvegetatie` — Verwijderd
- 🔴 `gras en kruidachtigen` — Verwijderd
- 🔴 `grien en hakhout` — Verwijderd
- 🔴 `heesters` — Verwijderd
- 🔴 `hoogstam boomgaarden` — Verwijderd
- 🔴 `klein fruit` — Verwijderd
- 🔴 `laagstam boomgaarden` — Verwijderd
- 🔴 `open duinvegetatie` — Verwijderd
- 🔴 `planten` — Verwijderd
- 🔴 `struikrozen` — Verwijderd
- 🔴 `vollegrondsteelt` — Verwijderd
- 🔴 `wijngaarden` — Verwijderd

##### `fysiekVoorkomenOnbegroeidTerrein` — 🔴 Verwijderd

**Literals:**

- 🔴 `Gesloten verharding` — Verwijderd
- 🔴 `erf` — Verwijderd
- 🔴 `half verhard` — Verwijderd
- 🔴 `onverhard` — Verwijderd
- 🔴 `open verharding` — Verwijderd
- 🔴 `zand` — Verwijderd

##### `fysiekVoorkomenOnbegroeidTerreinPlus` — 🔴 Verwijderd

**Literals:**

- 🔴 `asfalt` — Verwijderd
- 🔴 `betonelement` — Verwijderd
- 🔴 `betonstraatstenen` — Verwijderd
- 🔴 `boomschors` — Verwijderd
- 🔴 `cementbeton` — Verwijderd
- 🔴 `gebakken klinkers` — Verwijderd
- 🔴 `grasklinkers` — Verwijderd
- 🔴 `gravel` — Verwijderd
- 🔴 `grind` — Verwijderd
- 🔴 `kunststof` — Verwijderd
- 🔴 `puin` — Verwijderd
- 🔴 `schelpen` — Verwijderd
- 🔴 `sierbestrating` — Verwijderd
- 🔴 `strand en strandwal` — Verwijderd
- 🔴 `tegels` — Verwijderd
- 🔴 `zand` — Verwijderd
- 🔴 `zandverstuiving` — Verwijderd

##### `fysiekVoorkomenOndersteunendWegdeel` — 🔴 Verwijderd

**Literals:**

- 🔴 `gesloten verharding` — Verwijderd
- 🔴 `groenvoorziening` — Verwijderd
- 🔴 `half verhard` — Verwijderd
- 🔴 `onverhard` — Verwijderd

##### `fysiekVoorkomenOndersteunendWegdeelPlus` — 🔴 Verwijderd

**Literals:**

- 🔴 `asfalt` — Verwijderd
- 🔴 `beton element` — Verwijderd
- 🔴 `betonstraatstenen` — Verwijderd
- 🔴 `bodembedekkers` — Verwijderd
- 🔴 `boomschors` — Verwijderd
- 🔴 `bosplantsoen` — Verwijderd
- 🔴 `cementbeton` — Verwijderd
- 🔴 `gebakken klinkers` — Verwijderd
- 🔴 `gras- en kruidachtigen` — Verwijderd
- 🔴 `grasklinkers` — Verwijderd
- 🔴 `gravel` — Verwijderd
- 🔴 `grind` — Verwijderd
- 🔴 `heesters` — Verwijderd
- 🔴 `planten` — Verwijderd
- 🔴 `puin` — Verwijderd
- 🔴 `schelpen` — Verwijderd
- 🔴 `sierbestrating` — Verwijderd
- 🔴 `struikrozen` — Verwijderd
- 🔴 `tegels` — Verwijderd
- 🔴 `zand` — Verwijderd

##### `fysiekVoorkomenWeg` — 🔴 Verwijderd

**Literals:**

- 🔴 `gesloten verharding` — Verwijderd
- 🔴 `half verhard` — Verwijderd
- 🔴 `onverhard` — Verwijderd
- 🔴 `open verharding` — Verwijderd

##### `fysiekVoorkomenWegPlus` — 🔴 Verwijderd

**Literals:**

- 🔴 `asfalt` — Verwijderd
- 🔴 `beton element` — Verwijderd
- 🔴 `betonstraatstenen` — Verwijderd
- 🔴 `boomschors` — Verwijderd
- 🔴 `cementbeton` — Verwijderd
- 🔴 `gebakken klinkers` — Verwijderd
- 🔴 `grasklinkers` — Verwijderd
- 🔴 `gravel` — Verwijderd
- 🔴 `grind` — Verwijderd
- 🔴 `puin` — Verwijderd
- 🔴 `schelpen` — Verwijderd
- 🔴 `sierbestrating` — Verwijderd
- 🔴 `tegels` — Verwijderd
- 🔴 `zand` — Verwijderd

##### `gebruiksdoel` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `bijeenkomstfunctie` — Verwijderd
- 🔴 `celfunctie` — Verwijderd
- 🔴 `gezondheidszorgfunctie` — Verwijderd
- 🔴 `industriefunctie` — Verwijderd
- 🔴 `kantoorfunctie` — Verwijderd
- 🔴 `logiesfunctie` — Verwijderd
- 🔴 `onderwijsfunctie` — Verwijderd
- 🔴 `overige gebruiksfunctie` — Verwijderd
- 🔴 `sportfunctie` — Verwijderd
- 🔴 `winkelfunctie` — Verwijderd
- 🔴 `woonfunctie` — Verwijderd

##### `Gezinsrelatie` — 🔴 Verwijderd

**Literals:**

- 🔴 `Alleenstaand/Samenwonend` — Verwijderd
- 🔴 `Echtgenote binnen gezin` — Verwijderd
- 🔴 `Hoofd gezin met kind(eren)` — Verwijderd
- 🔴 `Hoofd gezin zonder kind(eren)` — Verwijderd
- 🔴 `Hoofd huwelijk gelijk geslacht` — Verwijderd
- 🔴 `Hoofd partnerrelatie` — Verwijderd
- 🔴 `Kind` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Ouder met kind(eren)` — Verwijderd

##### `soortGebruik` — 🔴 Verwijderd

**Literals:**

- 🔴 `boerderij` — Verwijderd
- 🔴 `niet-woning` — Verwijderd
- 🔴 `niet-woning deels in gebruik als woning` — Verwijderd
- 🔴 `recreatiewoning en overige woningen` — Verwijderd
- 🔴 `sluimerend WOZ-object` — Verwijderd
- 🔴 `terrein` — Verwijderd
- 🔴 `uitgezonderd gebouwd object` — Verwijderd
- 🔴 `uitgezonderd ongebouwd object` — Verwijderd
- 🔴 `woning dienend tot hoofdverblijf` — Verwijderd
- 🔴 `woning met praktijkruimte` — Verwijderd

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

##### `statusWOZ(Deel)Object` — 🔴 Verwijderd

**Literals:**

- 🔴 `actief` — Verwijderd
- 🔴 `beëindigd` — Verwijderd
- 🔴 `gevormd, niet actief` — Verwijderd
- 🔴 `ten onrechte opgevoerd` — Verwijderd

##### `statusWOZ-Beschikking` — 🔴 Verwijderd

**Literals:**

- 🔴 `arrest Hoge Raad, beschikking gehandhaafd` — Verwijderd
- 🔴 `arrest Hoge Raad, geding verwezen` — Verwijderd
- 🔴 `arrest Hoge Raad, vastgestelde waarde veranderd` — Verwijderd
- 🔴 `beroep aangetekend` — Verwijderd
- 🔴 `beschikking genomen` — Verwijderd
- 🔴 `bezwaar afgehandeld, beschikking gehandhaafd` — Verwijderd
- 🔴 `bezwaar afgehandeld, vastgestelde waarde veranderd` — Verwijderd
- 🔴 `bezwaar ingediend` — Verwijderd
- 🔴 `cassatie ingesteld` — Verwijderd
- 🔴 `herzieningsbeschikking` — Verwijderd
- 🔴 `hoger beroep aangetekend` — Verwijderd
- 🔴 `uitspraak beroep, beschikking gehandhaafd` — Verwijderd
- 🔴 `uitspraak beroep, vastgestelde waarde veranderd` — Verwijderd
- 🔴 `uitspraak hoger beroep, beschikking gehandhaafd` — Verwijderd
- 🔴 `uitspraak hoger beroep, vastgestelde waarde veranderd` — Verwijderd
- 🔴 `vernietiging beschikking` — Verwijderd
- 🔴 `waarde ambtshalve verminderd` — Verwijderd
- 🔴 `waarde te gebruiken voor voorlopige aanslag` — Verwijderd

##### `typeOverbrugging` — 🔴 Verwijderd

**Literals:**

- 🔴 `aquaduct` — Verwijderd
- 🔴 `brug` — Verwijderd
- 🔴 `ecoduct` — Verwijderd
- 🔴 `fly-over` — Verwijderd
- 🔴 `viaduct` — Verwijderd

##### `typeringAppartementsrechtsplitsing` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `hoofdsplitsing` — Verwijderd
- 🔴 `ondersplitsing` — Verwijderd
- 🔴 `splitsingafkooperfpacht` — Verwijderd

##### `typeringGebouwinstallatie` — 🔴 Verwijderd

**Literals:**

- 🔴 `bordes` — Verwijderd
- 🔴 `luifel` — Verwijderd
- 🔴 `toegangstrap` — Verwijderd

##### `typeringInrichtingselement` — 🔴 Verwijderd

**Literals:**

- 🔴 `bak` — Verwijderd
- 🔴 `bord` — Verwijderd
- 🔴 `installatie` — Verwijderd
- 🔴 `kast` — Verwijderd
- 🔴 `mast` — Verwijderd
- 🔴 `paal` — Verwijderd
- 🔴 `put` — Verwijderd
- 🔴 `sensor` — Verwijderd
- 🔴 `straatmeubilair` — Verwijderd
- 🔴 `waterinrichtingselement` — Verwijderd
- 🔴 `weginrichtingselement` — Verwijderd

##### `typeringInrichtingselementPlus` — 🔴 Verwijderd

**Literals:**

- 🔴 `CAI-kast` — Verwijderd
- 🔴 `GMS kast` — Verwijderd
- 🔴 `GMS sensor` — Verwijderd
- 🔴 `abri` — Verwijderd
- 🔴 `afsluitpaal` — Verwijderd
- 🔴 `afval aparte plaats` — Verwijderd
- 🔴 `afvalbak` — Verwijderd
- 🔴 `balustrade` — Verwijderd
- 🔴 `bank` — Verwijderd
- 🔴 `benzine- / olieput` — Verwijderd
- 🔴 `betaalautomaat` — Verwijderd
- 🔴 `betonning` — Verwijderd
- 🔴 `bloembak` — Verwijderd
- 🔴 `bolder` — Verwijderd
- 🔴 `boomspiegel` — Verwijderd
- 🔴 `bovenleidingmast` — Verwijderd
- 🔴 `brandkraan / -put` — Verwijderd
- 🔴 `brievenbus` — Verwijderd
- 🔴 `camera` — Verwijderd
- 🔴 `container` — Verwijderd
- 🔴 `debietmeter` — Verwijderd
- 🔴 `detectielus` — Verwijderd
- 🔴 `dijkpaal` — Verwijderd
- 🔴 `drainageput` — Verwijderd
- 🔴 `drinkbak` — Verwijderd
- 🔴 `drukknoppaal` — Verwijderd
- 🔴 `dynamische snelheidsindicator` — Verwijderd
- 🔴 `elektrakast` — Verwijderd
- 🔴 `fietsenkluis` — Verwijderd
- 🔴 `fietsenrek` — Verwijderd
- 🔴 `flitser` — Verwijderd
- 🔴 `fontein` — Verwijderd
- 🔴 `gaskast` — Verwijderd
- 🔴 `gasput` — Verwijderd
- 🔴 `geleideconstructie` — Verwijderd
- 🔴 `geleidewerk` — Verwijderd
- 🔴 `grensmarkering` — Verwijderd
- 🔴 `haltepaal` — Verwijderd
- 🔴 `hectometerpaal` — Verwijderd
- 🔴 `herdenkingsmonument` — Verwijderd
- 🔴 `hoogtedetectieapparaat` — Verwijderd
- 🔴 `hoogtemerk` — Verwijderd
- 🔴 `informatiebord` — Verwijderd
- 🔴 `inspectie- / rioolput` — Verwijderd
- 🔴 `kolk` — Verwijderd
- 🔴 `kunstobject` — Verwijderd
- 🔴 `laagspanningsmast` — Verwijderd
- 🔴 `lichtcel` — Verwijderd
- 🔴 `lichtmast` — Verwijderd
- 🔴 `lichtpunt` — Verwijderd
- 🔴 `lijnafwatering` — Verwijderd
- 🔴 `meerpaal` — Verwijderd
- 🔴 `molgoot` — Verwijderd
- 🔴 `openbaar toilet` — Verwijderd
- 🔴 `openbare verlichtingskast` — Verwijderd
- 🔴 `parkeerbeugel` — Verwijderd
- 🔴 `picknicktafel` — Verwijderd
- 🔴 `plaatsnaambord` — Verwijderd
- 🔴 `poller` — Verwijderd
- 🔴 `pomp` — Verwijderd
- 🔴 `portaal` — Verwijderd
- 🔴 `praatpaal` — Verwijderd
- 🔴 `radar detector` — Verwijderd
- 🔴 `radarmast` — Verwijderd
- 🔴 `reclamebord` — Verwijderd
- 🔴 `reclamezuil` — Verwijderd
- 🔴 `remmingswerk` — Verwijderd
- 🔴 `rioolkast` — Verwijderd
- 🔴 `scheepvaartbord` — Verwijderd
- 🔴 `sirene` — Verwijderd
- 🔴 `slagboom` — Verwijderd
- 🔴 `speelvoorziening` — Verwijderd
- 🔴 `straalzender` — Verwijderd
- 🔴 `straatnaambord` — Verwijderd
- 🔴 `telecom kast` — Verwijderd
- 🔴 `telefooncel` — Verwijderd
- 🔴 `telkast` — Verwijderd
- 🔴 `telpaal` — Verwijderd
- 🔴 `verblindingswering` — Verwijderd
- 🔴 `verkeersbord` — Verwijderd
- 🔴 `verkeersbordpaal` — Verwijderd
- 🔴 `verkeersregelinstallatiekast` — Verwijderd
- 🔴 `verkeersregelinstallatiepaal` — Verwijderd
- 🔴 `verklikker transportleiding` — Verwijderd
- 🔴 `vlaggenmast` — Verwijderd
- 🔴 `vuilvang` — Verwijderd
- 🔴 `waarschuwingshek` — Verwijderd
- 🔴 `waterleidingput` — Verwijderd
- 🔴 `waterstandmeter` — Verwijderd
- 🔴 `weerstation` — Verwijderd
- 🔴 `wegmarkering` — Verwijderd
- 🔴 `wegwijzer` — Verwijderd
- 🔴 `wildrooster` — Verwijderd
- 🔴 `windmeter` — Verwijderd
- 🔴 `zand- / zoutbak` — Verwijderd
- 🔴 `zendmast` — Verwijderd
- 🔴 `zonnepaneel` — Verwijderd

##### `typeringOndersteunendWater` — 🔴 Verwijderd

**Literals:**

- 🔴 `oever, slootkant` — Verwijderd
- 🔴 `slik` — Verwijderd

##### `typeringOverbruggingsdeel` — 🔴 Verwijderd

**Literals:**

- 🔴 `dek` — Verwijderd
- 🔴 `landhoofd` — Verwijderd
- 🔴 `pijler` — Verwijderd
- 🔴 `pyloon` — Verwijderd
- 🔴 `sloof` — Verwijderd

##### `typeringOverigeScheiding` — 🔴 Verwijderd

**Literals:**

- 🔴 `draadraster` — Verwijderd
- 🔴 `faunaraster` — Verwijderd

##### `typeringVegetatieobject` — 🔴 Verwijderd

**Literals:**

- 🔴 `boom` — Verwijderd
- 🔴 `haag` — Verwijderd

##### `typeringWater` — 🔴 Verwijderd

**Literals:**

- 🔴 `greppel, droge sloot` — Verwijderd
- 🔴 `waterloop` — Verwijderd
- 🔴 `watervlakte` — Verwijderd
- 🔴 `zee` — Verwijderd

##### `typeringWaterPlus` — 🔴 Verwijderd

**Literals:**

- 🔴 `beek` — Verwijderd
- 🔴 `bron` — Verwijderd
- 🔴 `gracht` — Verwijderd
- 🔴 `haven` — Verwijderd
- 🔴 `kanaal` — Verwijderd
- 🔴 `meer, plas, ven, vijver` — Verwijderd
- 🔴 `rivier` — Verwijderd
- 🔴 `sloot` — Verwijderd

##### `typeringZekerheidsrecht` — 🔴 Verwijderd

**Literals:**

- 🔴 `beslag` — Verwijderd
- 🔴 `recht van hypotheek` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `Appartementsrechtsplitsing` → `SplitsingstekeningReferentie`
- 🔴 Verwijderd: `Briefadres` → `Nummeraanduiding`
- 🔴 Verwijderd: `Briefadres` → `Nummeraanduiding`
- 🔴 Verwijderd: `FunctioneelGebied` → `SoortFunctioneelGebied`
- 🔴 Verwijderd: `Gebied` «komt overeen» → `Buurt`
- 🔴 Verwijderd: `Gebied` «komt overeen» → `Buurt`
- 🔴 Verwijderd: `Huishouden` «heeft» → `IngeschrevenPersoon`
- 🔴 Verwijderd: `IngeschrevenPersoon` «gezaghebbende» → `Gezagsverhouding`
- 🔴 Verwijderd: `IngeschrevenPersoon` «heeft als adres» → `Nummeraanduiding`
- 🔴 Verwijderd: `IngeschrevenPersoon` «heeft uitkering» → `Inkomensvoorziening`
- 🔴 Verwijderd: `IngeschrevenPersoon` «is verstrekt aan» → `Reisdocument`
- 🔴 Verwijderd: `IngeschrevenPersoon` «Ouder 1» → `IngeschrevenPersoon`
- 🔴 Verwijderd: `IngeschrevenPersoon` «Ouder 2» → `IngeschrevenPersoon`
- 🔴 Verwijderd: `IngeschrevenPersoon` → `Briefadres`
- 🔴 Verwijderd: `IngeschrevenPersoon` → `Regeling`
- 🔴 Verwijderd: `Ingezetene` «heeft» → `Verblijfstitel`
- 🔴 Verwijderd: `KadastraleOnroerendeZaak` «gerelateerd» → `KadastraleOnroerendeZaak`
- 🔴 Verwijderd: `KadastraleOnroerendeZaak` «heeft adres» → `Adresaanduiding`
- 🔴 Verwijderd: `KadastraleOnroerendeZaak` «heeft» → `CultuurOnbebouwd`
- 🔴 Verwijderd: `KadastraleOnroerendeZaak` «is ontstaan uit andere kadastrale onroerende zaak bij» → `KadastraleOnroerendeZaak`
- 🔴 Verwijderd: `KadastraleOnroerendeZaak` → `KoopsomKadastraleOnroerendeZaak`
- 🔴 Verwijderd: `KadastraleOnroerendeZaak` → `LocatieKadastraleOnroerendeZaak`
- 🔴 Verwijderd: `KadastraleOnroerendeZaakAantekening` «heeft betrekking op» → `KadastraleOnroerendeZaak`
- 🔴 Verwijderd: `Kunstwerkdeel` → `SoortKunstwerk`
- 🔴 Verwijderd: `MaatschappelijkeActiviteit` «heeft als eigenaar» → `Rechtspersoon`
- 🔴 Verwijderd: `MaatschappelijkeActiviteit` «is functionaris van» → `NatuurlijkPersoon`
- 🔴 Verwijderd: `NatuurlijkPersoon` «heeft» → `Nationaliteit`
- 🔴 Verwijderd: `NatuurlijkPersoon` «maakt deel uit van» → `Sociale Groep`
- 🔴 Verwijderd: `NatuurlijkPersoon` «maakt onderdeel uit van» → `Huishouden`
- 🔴 Verwijderd: `NietNatuurlijkPersoon` «contactpersoon» → `NatuurlijkPersoon`
- 🔴 Verwijderd: `NietNatuurlijkPersoon` «gezaghebbende» → `Gezagsverhouding`
- 🔴 Verwijderd: `NietNatuurlijkPersoon` «heeft» → `Vestiging`
- 🔴 Verwijderd: `OverigBenoemdTerrein` «heeft als officieel adres» → `OverigeAdresseerbaarObjectAanduiding`
- 🔴 Verwijderd: `OverigBouwwerk` → `SoortOverigBouwwerk`
- 🔴 Verwijderd: `OverigGebouwdObject` «heeft als equivalent» → `OverigBouwwerk`
- 🔴 Verwijderd: `OverigGebouwdObject` «heeft als officieel adres» → `OverigeAdresseerbaarObjectAanduiding`
- 🔴 Verwijderd: `Rechtspersoon` «aanvrager» → `Subsidie`
- 🔴 Verwijderd: `Rechtspersoon` «betrokkenen» → `KadastraleMutatie`
- 🔴 Verwijderd: `Rechtspersoon` «heeft» → `AdresBuitenland`
- 🔴 Verwijderd: `Rechtspersoon` «heeft» → `Objectrelatie`
- 🔴 Verwijderd: `Rechtspersoon` «heeft» → `Tenaamstelling`
- 🔴 Verwijderd: `Rechtspersoon` «heeft» → `WOZ-Belang`
- 🔴 Verwijderd: `Rechtspersoon` «projectleider» → `Rapportagemoment`
- 🔴 Verwijderd: `Scheiding` → `SoortScheiding`
- 🔴 Verwijderd: `Spoor` → `SoortSpoor`
- 🔴 Verwijderd: `Tenaamstelling` «heeft betrekking op» → `ZakelijkRecht`
- 🔴 Verwijderd: `Tenaamstelling` → `Aantekening`
- 🔴 Verwijderd: `Vestiging` «heeft als locatie-adres» → `Nummeraanduiding`
- 🔴 Verwijderd: `Vestiging` «heeft hoofdlocatie in of op» → `AdresseerbaarObject`
- 🔴 Verwijderd: `Vestiging` «heeft hoofdlocatie in of op» → `BenoemdObject`
- 🔴 Verwijderd: `Vestiging` «heeft nevenlocatie in of op» → `AdresseerbaarObject`
- 🔴 Verwijderd: `Vestiging` «heeft nevenlocatie in of op» → `BenoemdObject`
- 🔴 Verwijderd: `Vestiging` «heeft» → `Werkgelegenheid`
- 🔴 Verwijderd: `Vestiging` «is hoofdvestiging van» → `MaatschappelijkeActiviteit`
- 🔴 Verwijderd: `Vestiging` «uitoefening van activiteiten» → `MaatschappelijkeActiviteit`
- 🔴 Verwijderd: `Vestiging` → `SBIActiviteitVestiging`
- 🔴 Verwijderd: `WOZ-deelobject` «bestaat uit» → `AdresseerbaarObject`
- 🔴 Verwijderd: `WOZ-deelobject` «bestaat uit» → `Pand`
- 🔴 Verwijderd: `WOZ-deelobject` «is onderdeel van» → `WOZ-object`
- 🔴 Verwijderd: `WOZ-object` «bevat» → `KadastraleOnroerendeZaak`
- 🔴 Verwijderd: `WOZ-object` «bevat» → `KadastraleOnroerendeZaak`
- 🔴 Verwijderd: `WOZ-object` «heeft» → `WOZ-Belang`
- 🔴 Verwijderd: `WOZ-object` «ligt aan» → `OpenbareRuimte`
- 🔴 Verwijderd: `WOZ-Waarde` «is voor» → `WOZ-object`
- 🔴 Verwijderd: `ZakelijkRecht` «is belast met» → `ZakelijkRecht`
- 🔴 Verwijderd: `ZakelijkRecht` «is beperkt tot» → `Tenaamstelling`
- 🔴 Verwijderd: `ZakelijkRecht` «rust op» → `KadastraleOnroerendeZaak`
- 🔴 Verwijderd: `Zekerheidsrecht` «bezwaart» → `Tenaamstelling`
- 🔴 Verwijderd: `Zekerheidsrecht` «rust op» → `KadastraleOnroerendeZaak`

#### Generalisaties

- 🔴 Verwijderd: `Appartementsrecht` ⟶ `KadastraleOnroerendeZaak`
- 🔴 Verwijderd: `BegroeidTerreindeel` ⟶ `Geo-Object`
- 🔴 Verwijderd: `FunctioneelGebied` ⟶ `Geo-Object`
- 🔴 Verwijderd: `Gebouwinstallatie` ⟶ `Geo-Object`
- 🔴 Verwijderd: `IngeschrevenPersoon` ⟶ `NatuurlijkPersoon`
- 🔴 Verwijderd: `Ingezetene` ⟶ `IngeschrevenPersoon`
- 🔴 Verwijderd: `Inrichtingselement` ⟶ `Geo-Object`
- 🔴 Verwijderd: `KadastraalPerceel` ⟶ `KadastraleOnroerendeZaak`
- 🔴 Verwijderd: `KadastraleOnroerendeZaak` ⟶ `Object`
- 🔴 Verwijderd: `Kunstwerkdeel` ⟶ `Geo-Object`
- 🔴 Verwijderd: `NatuurlijkPersoon` ⟶ `Rechtspersoon`
- 🔴 Verwijderd: `NietNatuurlijkPersoon` ⟶ `Rechtspersoon`
- 🔴 Verwijderd: `OnbegroeidTerreindeel` ⟶ `Geo-Object`
- 🔴 Verwijderd: `Onbestemd Adres` ⟶ `Object`
- 🔴 Verwijderd: `OndersteunendWaterdeel` ⟶ `Geo-Object`
- 🔴 Verwijderd: `OndersteunendWegdeel` ⟶ `Geo-Object`
- 🔴 Verwijderd: `Overbruggingsdeel` ⟶ `Geo-Object`
- 🔴 Verwijderd: `OverigBenoemdTerrein` ⟶ `AdresseerbaarObject`
- 🔴 Verwijderd: `OverigBenoemdTerrein` ⟶ `Geo-Object`
- 🔴 Verwijderd: `OverigBouwwerk` ⟶ `Geo-Object`
- 🔴 Verwijderd: `OverigeAdresseerbaarObjectAanduiding` ⟶ `Nummeraanduiding`
- 🔴 Verwijderd: `OverigeAdresseerbaarObjectAanduiding` ⟶ `Nummeraanduiding`
- 🔴 Verwijderd: `OverigeAdresseerbaarObjectAanduiding` ⟶ `Nummeraanduiding`
- 🔴 Verwijderd: `OverigeScheiding` ⟶ `Geo-Object`
- 🔴 Verwijderd: `OverigGebouwdObject` ⟶ `AdresseerbaarObject`
- 🔴 Verwijderd: `OverigGebouwdObject` ⟶ `AdresseerbaarObjectAanduiding`
- 🔴 Verwijderd: `OverigGebouwdObject` ⟶ `GebouwdObject`
- 🔴 Verwijderd: `Scheiding` ⟶ `Geo-Object`
- 🔴 Verwijderd: `Spoor` ⟶ `Geo-Object`
- 🔴 Verwijderd: `Tunneldeel` ⟶ `Geo-Object`
- 🔴 Verwijderd: `Vegetatieobject` ⟶ `Geo-Object`
- 🔴 Verwijderd: `Waterdeel` ⟶ `Geo-Object`
- 🔴 Verwijderd: `Wegdeel` ⟶ `Geo-Object`

<a id="structureel-delfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelreferentielijsten"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Referentielijsten

#### Classes

##### `AanduidingVerblijfsrecht` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumAanvangGeldigheidVerblijfsrecht` — Verwijderd
- 🔴 `datumEindeGeldigheidVerblijfsrecht` — Verwijderd
- 🔴 `verblijfsrechtnummer` — Verwijderd
- 🔴 `verblijfsrechtomschrijving` — Verwijderd

##### `AardAantekening` — 🔴 Verwijderd

**Attributen:**

- 🔴 `codeAardAantekening` — Verwijderd
- 🔴 `datumBeginGeldigheidAardAantekening` — Verwijderd
- 🔴 `datumEindeGeldigheidAardAantekening` — Verwijderd
- 🔴 `naamAardAantekening` — Verwijderd

##### `AardFiliatie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `codeAardFiliatie` — Verwijderd
- 🔴 `datumBeginGeldigheidAardFiliatie` — Verwijderd
- 🔴 `datumEindeGeldigheidAardFiliatie` — Verwijderd
- 🔴 `naamAardFiliatie` — Verwijderd

##### `AardZakelijkRecht` — 🔴 Verwijderd

**Attributen:**

- 🔴 `codeAardZakelijkRecht` — Verwijderd
- 🔴 `datumBeginGeldigheidAardZakelijkRecht` — Verwijderd
- 🔴 `datumEindeGeldigheidAardZakelijkRecht` — Verwijderd
- 🔴 `naamAardZakelijkRecht` — Verwijderd

##### `AcademischeTitel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `codeAcademischeTitel` — Verwijderd
- 🔴 `datumBeginGeldigheidTitel` — Verwijderd
- 🔴 `datumEindeGeldigheidTitel` — Verwijderd
- 🔴 `omschrijvingAcademischeTitel` — Verwijderd
- 🔴 `positieAcademischeTitelTOVNaam` — Verwijderd

##### `AkrKadastraleGemeentecode` — 🔴 Verwijderd

**Attributen:**

- 🔴 `AKRCode` — Verwijderd
- 🔴 `codeAKRKadadastraleGemeentecode` — Verwijderd
- 🔴 `datumBeginGeldigheidAKRCode` — Verwijderd
- 🔴 `datumEindeGeldigheidAKRCode` — Verwijderd

##### `AutoriteitAfgifteNederlandsReisdocument` — 🔴 Verwijderd

**Attributen:**

- 🔴 `code` — Verwijderd
- 🔴 `datumBeginGeldigheidAutoriteitVanAfgifte` — Verwijderd
- 🔴 `datumEindeGeldigheidAutoriteitVanAfgifte` — Verwijderd
- 🔴 `omschrijving` — Verwijderd

##### `CultuurcodeBebouwd` — 🔴 Verwijderd

**Attributen:**

- 🔴 `code` — Verwijderd
- 🔴 `datumBeginGeldigheidCultuurcodeBebouwd` — Verwijderd
- 🔴 `datumEindeGeldigheidCultuurcodeBebouwd` — Verwijderd
- 🔴 `naamCultuurcodeBebouwd` — Verwijderd

##### `CultuurcodeOnbebouwd` — 🔴 Verwijderd

**Attributen:**

- 🔴 `code` — Verwijderd
- 🔴 `datumBeginGeldigheidCultuurcodeOnbebouwd` — Verwijderd
- 🔴 `datumEindeGeldigheidCultuurcodeOnbebouwd` — Verwijderd
- 🔴 `naamCultuurcodeOnbebouwd` — Verwijderd

##### `KadastraleGemeente` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheidKadastraleGemeente` — Verwijderd
- 🔴 `datumEindeGeldigheidKadastraleGemeente` — Verwijderd
- 🔴 `kadastraleGemeentecode` — Verwijderd
- 🔴 `naam` — Verwijderd

##### `Land` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumEindeFictief` — Verwijderd
- 🔴 `datumEindeLand` — Verwijderd
- 🔴 `datumIngangLand` — Verwijderd
- 🔴 `landcode` — Verwijderd
- 🔴 `landcodeISODrieletterig` — Verwijderd
- 🔴 `landcodeISOTweeletterig` — Verwijderd
- 🔴 `landnaam` — Verwijderd

##### `LandOfgebied` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumEindeLand` — Verwijderd
- 🔴 `datumIngangLand` — Verwijderd
- 🔴 `landcode` — Verwijderd
- 🔴 `landcodeISO` — Verwijderd
- 🔴 `landnaam` — Verwijderd

##### `Nationaliteit` — 🔴 Verwijderd

**Attributen:**

- 🔴 `codeNationaliteit` — Verwijderd
- 🔴 `datumBeginGeldigheidNationaliteit` — Verwijderd
- 🔴 `datumEindeGeldigheidNationaliteit` — Verwijderd
- 🔴 `nationaliteitOmschrijving` — Verwijderd

##### `Partij` — 🔴 Verwijderd

**Attributen:**

- 🔴 `code` — Verwijderd
- 🔴 `datumAanvangGeldigheidPartij` — Verwijderd
- 🔴 `datumEindeGeldigheidPartij` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `soort` — Verwijderd
- 🔴 `verstrekkingsbeperkingMogelijk` — Verwijderd

##### `Provincie` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumEindeProvincie` — Verwijderd
- 🔴 `datumIngangProvincie` — Verwijderd
- 🔴 `hoofdstad` — Verwijderd
- 🔴 `oppervlakte` — Verwijderd
- 🔴 `oppervlakteLand` — Verwijderd
- 🔴 `provinciecode` — Verwijderd
- 🔴 `provincienaam` — Verwijderd

##### `RedenVerkrijgingNationaliteit` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumAanvangGeldigheidVerkrijging` — Verwijderd
- 🔴 `datumEindeGeldigheidVerkrijging` — Verwijderd
- 🔴 `omschrijvingVerkrijging` — Verwijderd
- 🔴 `redennummerVerkrijging` — Verwijderd

##### `RedenVerliesNationaliteit` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumAanvangGeldigheidVerlies` — Verwijderd
- 🔴 `datumEindeGeldigheidVerlies` — Verwijderd
- 🔴 `omschrijvingVerlies` — Verwijderd
- 🔴 `redennummerVerlies` — Verwijderd

##### `Reisdocumentsoort` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheidReisdocumentsoort` — Verwijderd
- 🔴 `datumEindeGeldigheidReisdocumentsoort` — Verwijderd
- 🔴 `reisdocumentcode` — Verwijderd
- 🔴 `reisdocumentOmschrijving` — Verwijderd

##### `SBIActiviteit` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumEindeSBIActiviteit` — Verwijderd
- 🔴 `datumIngangSBIActiviteit` — Verwijderd
- 🔴 `hoofdniveau` — Verwijderd
- 🔴 `hoofdniveauOmschrijving` — Verwijderd
- 🔴 `naamActiviteit` — Verwijderd
- 🔴 `SBICode` — Verwijderd
- 🔴 `SBIGroep` — Verwijderd
- 🔴 `SBIGroepOmschrijving` — Verwijderd

##### `SoortGrootte` — 🔴 Verwijderd

**Attributen:**

- 🔴 `codeSoortGrootte` — Verwijderd
- 🔴 `datumBeginGeldigheidSoortGrootte` — Verwijderd
- 🔴 `datumEindeGeldigheidSoortGrootte` — Verwijderd
- 🔴 `naamSoortGrootte` — Verwijderd

##### `SoortWOZObject` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheidSoortObjectcode` — Verwijderd
- 🔴 `datumEindeGeldigheidSoortObjectcode` — Verwijderd
- 🔴 `naamSoortObjectcode` — Verwijderd
- 🔴 `opmerkingenSoortObjectcode` — Verwijderd
- 🔴 `soortobjectcode` — Verwijderd

##### `Valuta` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheid` — Verwijderd
- 🔴 `datumEindeGeldigheid` — Verwijderd
- 🔴 `naam` — Verwijderd
- 🔴 `valutacode` — Verwijderd

##### `Valutasoort` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheidValutasoort` — Verwijderd
- 🔴 `datumEindeGeldigheidValutasoort` — Verwijderd
- 🔴 `naamValuta` — Verwijderd
- 🔴 `valutacode` — Verwijderd

##### `Verblijfstitel` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumAanvangGeldigheidVerblijfstitel` — Verwijderd
- 🔴 `datumEindeGeldigheidVerblijfstitel` — Verwijderd
- 🔴 `verblijfstitelNumeriek` — Verwijderd
- 🔴 `verblijfstitelOmschrijving` — Verwijderd

##### `WOZ-Deelobjectcode` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheidDeelojectcode` — Verwijderd
- 🔴 `datumEindeGeldigheidDeelobjectcode` — Verwijderd
- 🔴 `deelobjectcode` — Verwijderd
- 🔴 `naamDeelobjectcode` — Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelrelatieklasse"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Relatieklasse

#### Classes

##### `LocatieaanduidingAdresWOZObject` — 🔴 Verwijderd

**Attributen:**

- 🔴 `locatieOmschrijving` — Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelunion"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Union

#### Datatypes

##### `MultiPuntLijn(Multi)Vlak` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `geometrieLijn` — Verwijderd
- 🔴 `geometrieMultiVlak` — Verwijderd
- 🔴 `geometrieMultPunt1` — Verwijderd
- 🔴 `geometrieVlak` — Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelarchiefmodel-kern-rsgb"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/archief/Model Kern RSGB

#### Classes

##### `AdresseerbaarObjectAanduiding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `identificatie` — Verwijderd

##### `BenoemdObject` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheid` — Verwijderd
- 🔴 `datumEindeGeldigheid` — Verwijderd
- 🔴 `geometriePunt` — Verwijderd
- 🔴 `geometrieVlak` — Verwijderd
- 🔴 `identificatie` — Verwijderd

##### `BenoemdTerrein` — 🔴 Verwijderd

**Attributen:**

- 🔴 `identificatie` — Verwijderd

##### `Buurt` — 🔴 Verwijderd

**Attributen:**

- 🔴 `buurtcode` — Verwijderd
- 🔴 `buurtgeometrie` — Verwijderd
- 🔴 `buurtnaam` — Verwijderd
- 🔴 `datumBeginGeldigheidBuurt` — Verwijderd
- 🔴 `datumEindeGeldigheidBuurt` — Verwijderd
- 🔴 `identificatie` — Verwijderd
- 🔴 `identificatieIMGeoBRT` — Verwijderd

##### `GebouwdObject` — 🔴 Verwijderd

**Attributen:**

- 🔴 `bouwkundigeBestemmingActueel` — Verwijderd
- 🔴 `brutoInhoud` — Verwijderd
- 🔴 `identificatie` — Verwijderd
- 🔴 `inwinningOppervlakte` — Verwijderd
- 🔴 `oppervlakteObject` — Verwijderd
- 🔴 `statusVoortgangBouw` — Verwijderd

##### `Gemeente` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheidGemeente` — Verwijderd
- 🔴 `datumEindeGeldigheidGemeente` — Verwijderd
- 🔴 `gemeentecode` — Verwijderd
- 🔴 `gemeenteGeometrie` — Verwijderd
- 🔴 `gemeentenaam` — Verwijderd
- 🔴 `gemeentenaamNEN` — Verwijderd
- 🔴 `identificatie` — Verwijderd
- 🔴 `nieuwe gemeente` — Verwijderd

##### `Ligplaats` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumDocument` — Verwijderd
- 🔴 `documentNummer` — Verwijderd
- 🔴 `indicatieGeconstateerdeLigplaats` — Verwijderd
- 🔴 `inOnderzoek` — Verwijderd
- 🔴 `ligplaatsidentificatie` — Verwijderd
- 🔴 `ligplaatsstatus` — Verwijderd

##### `Nummeraanduiding` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheidNummeraanduiding` — Verwijderd
- 🔴 `DatumEindeGeldigheidNummeraanduiding` — Verwijderd
- 🔴 `geconstateerd` — Verwijderd
- 🔴 `huisletter` — Verwijderd
- 🔴 `huisnummer` — Verwijderd
- 🔴 `huisnummertoevoeging` — Verwijderd
- 🔴 `identificatie` — Verwijderd
- 🔴 `inOnderzoek` — Verwijderd
- 🔴 `postcode` — Verwijderd
- 🔴 `status` — Verwijderd
- 🔴 `typeAdresseerbaarObject` — Verwijderd

##### `OpenbareRuimte` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheidOpenbareRuimte` — Verwijderd
- 🔴 `datumEindeGeldigheidOpenbareRuimte` — Verwijderd
- 🔴 `huisnummerrangeEvenEnOnevenNummers` — Verwijderd
- 🔴 `huisnummerrangeEvenNummers` — Verwijderd
- 🔴 `HuisnummerrangeOnevenNummers` — Verwijderd
- 🔴 `IdentificatiecodeOpenbareRuimte` — Verwijderd
- 🔴 `identificatieIMGeoOPR` — Verwijderd
- 🔴 `indicatieGeconstateerdeOpenbareRuimte` — Verwijderd
- 🔴 `inOnderzoek` — Verwijderd
- 🔴 `labelNaamOpenbareRuimte` — Verwijderd
- 🔴 `naamOpenbareRuimte` — Verwijderd
- 🔴 `openbareRuimteGeometrie` — Verwijderd
- 🔴 `statusOpenbareRuimte` — Verwijderd
- 🔴 `straatnaam` — Verwijderd
- 🔴 `typeOpenbareRuimte` — Verwijderd
- 🔴 `wegsegment` — Verwijderd

##### `Pand` — 🔴 Verwijderd

**Attributen:**

- 🔴 `brutoInhoudPand` — Verwijderd
- 🔴 `datumBeginGeldigheidPand` — Verwijderd
- 🔴 `datumEindeGeldigheidPand` — Verwijderd
- 🔴 `geometriePunt` — Verwijderd
- 🔴 `hoogsteBouwlaagPand` — Verwijderd
- 🔴 `identificatieBGTPND` — Verwijderd
- 🔴 `indicatieGeconstateerdPand` — Verwijderd
- 🔴 `indicatiePlanobject` — Verwijderd
- 🔴 `inwinningGeometrieBovenaanzicht` — Verwijderd
- 🔴 `inwinningGeometrieMaaiveld` — Verwijderd
- 🔴 `laagsteBouwlaagPand` — Verwijderd
- 🔴 `labelNummeraanduidingreeks` — Verwijderd
- 🔴 `LOD1GeometriePand` — Verwijderd
- 🔴 `LOD2GeometriePand` — Verwijderd
- 🔴 `lod3GeometriePand` — Verwijderd
- 🔴 `oorspronkelijkBouwjaarPand` — Verwijderd
- 🔴 `oppervlaktePand` — Verwijderd
- 🔴 `pandgeometrieBovenaanzicht` — Verwijderd
- 🔴 `pandgeometrieMaaiveld` — Verwijderd
- 🔴 `pandidentificatie` — Verwijderd
- 🔴 `pandstatus` — Verwijderd
- 🔴 `relatieveHoogteliggingPand` — Verwijderd
- 🔴 `statusVoortgangBouw` — Verwijderd

##### `Standplaats` — 🔴 Verwijderd

**Attributen:**

- 🔴 `indicatieGeconstateerdeStandplaats` — Verwijderd
- 🔴 `standplaatsidentificatie` — Verwijderd
- 🔴 `standplaatsstatus` — Verwijderd

##### `Verblijfsobject` — 🔴 Verwijderd

**Attributen:**

- 🔴 `aantalKamers` — Verwijderd
- 🔴 `hoogsteBouwlaagVerblijfsobject` — Verwijderd
- 🔴 `indicatieGeconstateerdVerblijfsobject` — Verwijderd
- 🔴 `inOnderzoek` — Verwijderd
- 🔴 `laagsteBouwlaagVerblijfsobject` — Verwijderd
- 🔴 `ontsluitingVerdieping` — Verwijderd
- 🔴 `soortWoonobject` — Verwijderd
- 🔴 `toegangBouwlaagVerblijfsobject` — Verwijderd
- 🔴 `verblijfsobjectidentificatie` — Verwijderd
- 🔴 `verblijfsobjectstatus` — Verwijderd

##### `Wijk` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheidWijk` — Verwijderd
- 🔴 `datumEindeGeldigheidWijk` — Verwijderd
- 🔴 `geometrieWijk` — Verwijderd
- 🔴 `identificatie` — Verwijderd
- 🔴 `identificatieIMGeoWYK` — Verwijderd
- 🔴 `wijkcode` — Verwijderd
- 🔴 `wijknaam` — Verwijderd

##### `Woonplaats` — 🔴 Verwijderd

**Attributen:**

- 🔴 `datumBeginGeldigheidWoonplaats` — Verwijderd
- 🔴 `datumEindeGeldigheidWoonplaats` — Verwijderd
- 🔴 `geometrieWoonplaats` — Verwijderd
- 🔴 `indicatieGeconstateerdeWoonplaats` — Verwijderd
- 🔴 `inOnderzoek` — Verwijderd
- 🔴 `woonplaatsIdentificatie` — Verwijderd
- 🔴 `woonplaatsNaam` — Verwijderd
- 🔴 `woonplaatsNaamNEN` — Verwijderd
- 🔴 `woonplaatsStatus` — Verwijderd

#### Enumeraties

##### `bouwkundigeBestemming` — 🔴 Verwijderd

**Literals:**

- 🔴 `CAI` — Verwijderd
- 🔴 `aanleunwoonverblijf` — Verwijderd
- 🔴 `academisch onderwijs` — Verwijderd
- 🔴 `akkerbouw` — Verwijderd
- 🔴 `algemeen voortgezet onderwijs` — Verwijderd
- 🔴 `andere doeleinden van openbaar nut` — Verwijderd
- 🔴 `basisschool` — Verwijderd
- 🔴 `begraafplaats/crematorium` — Verwijderd
- 🔴 `bejaardenwoning` — Verwijderd
- 🔴 `bejaardenwoonverblijf (in bejaardenoord, centrale keuken)` — Verwijderd
- 🔴 `bibliotheek` — Verwijderd
- 🔴 `bijzonder onderwijs` — Verwijderd
- 🔴 `bioscoop` — Verwijderd
- 🔴 `brandweer` — Verwijderd
- 🔴 `cafe/bar/restaurant` — Verwijderd
- 🔴 `congres` — Verwijderd
- 🔴 `dagverblijf` — Verwijderd
- 🔴 `defensie` — Verwijderd
- 🔴 `detailhandel` — Verwijderd
- 🔴 `dienstwoning` — Verwijderd
- 🔴 `dierenverzorging` — Verwijderd
- 🔴 `doeleinden voor agrarisch bedrijf` — Verwijderd
- 🔴 `doeleinden voor cultuur` — Verwijderd
- 🔴 `doeleinden voor gezondheidszorg` — Verwijderd
- 🔴 `doeleinden voor handel, horeca en bedrijf` — Verwijderd
- 🔴 `doeleinden voor niet-wonen` — Verwijderd
- 🔴 `doeleinden voor nutsvoorzieningen` — Verwijderd
- 🔴 `doeleinden voor onderwijs` — Verwijderd
- 🔴 `doeleinden voor recreatie` — Verwijderd
- 🔴 `doeleinden voor verkeer` — Verwijderd
- 🔴 `doeleinden voor wonen` — Verwijderd
- 🔴 `eengezinswoning` — Verwijderd
- 🔴 `elektriciteit` — Verwijderd
- 🔴 `expositie` — Verwijderd
- 🔴 `fabricage en productie` — Verwijderd
- 🔴 `gas` — Verwijderd
- 🔴 `gehandicaptenwooneenheid` — Verwijderd
- 🔴 `gemeentehuis` — Verwijderd
- 🔴 `gemengd bedrijf` — Verwijderd
- 🔴 `gevangenis/gesticht` — Verwijderd
- 🔴 `godsdienst (kerk, klooster e.d.)` — Verwijderd
- 🔴 `hoger beroepsonderwijs` — Verwijderd
- 🔴 `hotel/logies` — Verwijderd
- 🔴 `jongerenwooneenheid` — Verwijderd
- 🔴 `kantoor` — Verwijderd
- 🔴 `kinderopvang` — Verwijderd
- 🔴 `laboratoria` — Verwijderd
- 🔴 `luchtvaart` — Verwijderd
- 🔴 `meergezinswoning` — Verwijderd
- 🔴 `musea` — Verwijderd
- 🔴 `natuur en landschap` — Verwijderd
- 🔴 `onderhoud en reparatie` — Verwijderd
- 🔴 `opslag en distributie` — Verwijderd
- 🔴 `overige andere doeleinden van openbaar nut` — Verwijderd
- 🔴 `overige doeleinden voor agrarisch bedrijf` — Verwijderd
- 🔴 `overige doeleinden voor cultuur` — Verwijderd
- 🔴 `overige doeleinden voor gezondheidszorg` — Verwijderd
- 🔴 `overige doeleinden voor niet-wonen` — Verwijderd
- 🔴 `overige doeleinden voor nutsvoorzieningen` — Verwijderd
- 🔴 `overige doeleinden voor onderwijs` — Verwijderd
- 🔴 `overige doeleinden voor recreatie` — Verwijderd
- 🔴 `overige doeleinden voor verkeer` — Verwijderd
- 🔴 `polikliniek` — Verwijderd
- 🔴 `politie` — Verwijderd
- 🔴 `praktijkruimte` — Verwijderd
- 🔴 `psychiatrische inrichting` — Verwijderd
- 🔴 `recreatie` — Verwijderd
- 🔴 `recreatiewoning` — Verwijderd
- 🔴 `scheepvaart` — Verwijderd
- 🔴 `spoorwegverkeer` — Verwijderd
- 🔴 `sport binnen` — Verwijderd
- 🔴 `sport buiten` — Verwijderd
- 🔴 `stalling (fietsen/auto's)` — Verwijderd
- 🔴 `telecommunicatie` — Verwijderd
- 🔴 `theater en concert` — Verwijderd
- 🔴 `tuinbouw` — Verwijderd
- 🔴 `veeteelt` — Verwijderd
- 🔴 `verpleegtehuis` — Verwijderd
- 🔴 `verzorgingstehuis en bejaardentehuis` — Verwijderd
- 🔴 `vrijetijds onderwijs` — Verwijderd
- 🔴 `waternuts doeleinden` — Verwijderd
- 🔴 `waterschaps en waterverdediging` — Verwijderd
- 🔴 `wegverkeer` — Verwijderd
- 🔴 `wijk-/buurt-/verenigingsactiviteiten` — Verwijderd
- 🔴 `wijkverzorging` — Verwijderd
- 🔴 `ziekenhuis` — Verwijderd
- 🔴 `zorgwoonverblijf` — Verwijderd
- 🔴 `zwembad` — Verwijderd

##### `gebruiksdoel` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `bijeenkomstfunctie` — Verwijderd
- 🔴 `celfunctie` — Verwijderd
- 🔴 `gezondheidszorgfunctie` — Verwijderd
- 🔴 `industriefunctie` — Verwijderd
- 🔴 `kantoorfunctie` — Verwijderd
- 🔴 `logiesfunctie` — Verwijderd
- 🔴 `onderwijsfunctie` — Verwijderd
- 🔴 `overige gebruiksfunctie` — Verwijderd
- 🔴 `sportfunctie` — Verwijderd
- 🔴 `winkelfunctie` — Verwijderd
- 🔴 `woonfunctie` — Verwijderd

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

##### `inwinningsmethodeOppervlakte` — 🔴 Verwijderd

**Literals:**

- 🔴 `gemeten op basis van de bouwtekening` — Verwijderd
- 🔴 `initiële vulling d.m.v. conversietabel inhoud-oppervlak` — Verwijderd
- 🔴 `initiële vulling d.m.v. gegevens bouw- en woningtoezicht` — Verwijderd
- 🔴 `initiële vulling d.m.v. gegevens woningbouwvereniging` — Verwijderd
- 🔴 `initiële vulling d.m.v. oppervlaktegegevens WOZ-administratie` — Verwijderd
- 🔴 `initiële vulling d.m.v. overige brongegevens` — Verwijderd
- 🔴 `overgenomen uit bouwaanvraag` — Verwijderd
- 🔴 `ter plaatse ingemeten` — Verwijderd

##### `ontsluitingswijzeVerdieping` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `lift` — Verwijderd
- 🔴 `roltrap` — Verwijderd
- 🔴 `trap` — Verwijderd

##### `soortWoonobject` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `bijzonder woongebouw` — Verwijderd
- 🔴 `overig woonverblijf` — Verwijderd
- 🔴 `recreatiewoning` — Verwijderd
- 🔴 `woning` — Verwijderd
- 🔴 `wooneenheid` — Verwijderd

##### `StatLigplaatsStandplaats` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `plaats aangewezen` — Verwijderd
- 🔴 `plaats ingetrokken` — Verwijderd

##### `StatLigplaatsStandplaats` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `plaats aangewezen` — Verwijderd
- 🔴 `plaats ingetrokken` — Verwijderd

##### `statusNummeraanduiding` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `naamgeving ingetrokken` — Verwijderd
- 🔴 `naamgeving uitgegeven` — Verwijderd

##### `statusOpenbareRuimte` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `naamgeving ingetrokken` — Verwijderd
- 🔴 `naamgeving uitgegeven` — Verwijderd

##### `statusPand` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `bouw gestart` — Verwijderd
- 🔴 `bouwaanvraag ontvangen` — Verwijderd
- 🔴 `bouwvergunning verleend` — Verwijderd
- 🔴 `niet gerealiseerd pand` — Verwijderd
- 🔴 `pand buiten gebruik` — Verwijderd
- 🔴 `pand gesloopt` — Verwijderd
- 🔴 `pand in gebruik` — Verwijderd
- 🔴 `pand in gebruik (niet ingemeten)` — Verwijderd
- 🔴 `pand ten onrechte opgevoerd` — Verwijderd
- 🔴 `sloopvergunning verleend` — Verwijderd
- 🔴 `verbouwing pand` — Verwijderd

##### `statusVerblijfsobject` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `niet gerealiseerd verblijfsobject` — Verwijderd
- 🔴 `verblijfsobject buiten gebruik` — Verwijderd
- 🔴 `verblijfsobject gevormd` — Verwijderd
- 🔴 `verblijfsobject in gebruik` — Verwijderd
- 🔴 `verblijfsobject in gebruik (niet ingemeten)` — Verwijderd
- 🔴 `verblijfsobject ingetrokken` — Verwijderd

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

##### `statusWoonplaats` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `woonplaats aangewezen` — Verwijderd
- 🔴 `woonplaats ingetrokken` — Verwijderd

##### `TypeAdresseerbaarObject` — 🔴 Verwijderd

**Literals:**

- 🔴 `KADbinnenlandsadres` — Verwijderd
- 🔴 `Leeg` — Verwijderd
- 🔴 `Ligplaats` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `Standplaats` — Verwijderd
- 🔴 `Verblijfsobject` — Verwijderd

##### `typeringOpenbareRuimte` — 🔴 Verwijderd

**Literals:**

- 🔴 `Leeg` — Verwijderd
- 🔴 `Onbekend` — Verwijderd
- 🔴 `administratief gebied` — Verwijderd
- 🔴 `functioneel gebied` — Verwijderd
- 🔴 `kunstwerk` — Verwijderd
- 🔴 `landschappelijk gebied` — Verwijderd
- 🔴 `spoorbaan` — Verwijderd
- 🔴 `terrein` — Verwijderd
- 🔴 `water` — Verwijderd
- 🔴 `weg` — Verwijderd

#### Associaties

- 🔴 Verwijderd: `BenoemdObject` «is ontstaan uit / overgegaan in» → `BenoemdObject`
- 🔴 Verwijderd: `Buurt` «ligt in» → `Wijk`
- 🔴 Verwijderd: `GebouwdObject` «heeft» → `Gebruiksdoel`
- 🔴 Verwijderd: `GebouwdObject` «heeft» → `Winkelvloeroppervlak`
- 🔴 Verwijderd: `Gemeente` «is overgegaan in» → `Gemeente`
- 🔴 Verwijderd: `Nummeraanduiding` «heeft als hoofdadres» → `AdresseerbaarObjectAanduiding`
- 🔴 Verwijderd: `Nummeraanduiding` «heeft als nevenadres» → `AdresseerbaarObjectAanduiding`
- 🔴 Verwijderd: `Nummeraanduiding` «ligt aan» → `OpenbareRuimte`
- 🔴 Verwijderd: `Nummeraanduiding` «ligt in» → `Buurt`
- 🔴 Verwijderd: `Nummeraanduiding` «ligt in» → `Gebied`
- 🔴 Verwijderd: `Nummeraanduiding` «ligt in» → `Woonplaats`
- 🔴 Verwijderd: `OpenbareRuimte` «ligt in» → `Woonplaats`
- 🔴 Verwijderd: `Verblijfsobject` «maakt deel uit van» → `Pand`
- 🔴 Verwijderd: `Wijk` «ligt in» → `Gemeente`
- 🔴 Verwijderd: `Wijk` «ligt in» → `Woonplaats`
- 🔴 Verwijderd: `Woonplaats` «ligt in» → `Gemeente`

#### Generalisaties

- 🔴 Verwijderd: `BenoemdObject` ⟶ `Object`
- 🔴 Verwijderd: `BenoemdTerrein` ⟶ `AdresseerbaarObject`
- 🔴 Verwijderd: `BenoemdTerrein` ⟶ `BenoemdObject`
- 🔴 Verwijderd: `GebouwdObject` ⟶ `BenoemdObject`
- 🔴 Verwijderd: `Ligplaats` ⟶ `AdresseerbaarObjectAanduiding`
- 🔴 Verwijderd: `Ligplaats` ⟶ `BenoemdTerrein`
- 🔴 Verwijderd: `Nummeraanduiding` ⟶ `Object`
- 🔴 Verwijderd: `Pand` ⟶ `Geo-Object`
- 🔴 Verwijderd: `Standplaats` ⟶ `AdresseerbaarObjectAanduiding`
- 🔴 Verwijderd: `Standplaats` ⟶ `BenoemdTerrein`
- 🔴 Verwijderd: `Verblijfsobject` ⟶ `AdresseerbaarObjectAanduiding`
- 🔴 Verwijderd: `Verblijfsobject` ⟶ `GebouwdObject`

## Beschrijvende wijzigingen

_Geen beschrijvende wijzigingen._
