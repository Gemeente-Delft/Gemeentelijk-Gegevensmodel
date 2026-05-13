# Changes from v2.4.0 to v2.5.0

Entiteiten worden vergeleken op naam (gekwalificeerd met pakketpad), zodat een nieuwe `ea_guid` voor hetzelfde logische element niet als _Removed + Added_ verschijnt. Verwijzingen naar andere entiteiten (FK-velden zoals `enumeration_id`) worden vergeleken op de naam van het doel — niet op de interne sleutel.

**Structurele wijzigingen** raken het model zelf: toegevoegde of verwijderde elementen, naamswijzigingen, type/verplicht/multipliciteit/lengte/patroon en links tussen elementen. **Beschrijvende wijzigingen** updaten alleen metadata of documentatie (definitie, toelichting, gemma-tags, versie, auteur, herkomst, …) zonder de structuur van het model te veranderen.

## Samenvatting

| Element | + (struct.) | − (struct.) | ~ (struct.) | ~ (beschr.) |
| --- | ---: | ---: | ---: | ---: |
| Classes | 1 | 5 | 16 | 953 |
| Datatypes | 0 | 0 | 0 | 0 |
| Enumeraties | 34 | 2 | 4 | 326 |
| Attributen | 46 | 334 | 487 | 7 |
| Associaties | 1 | 3 | 70 | 0 |
| Generalisaties | 0 | 2 | 1 | 0 |
| Enum-literals | 280 | 20 | — | — |
| Pakketten (metadata) | 0 | 0 | 1 | 97 |

## Geraakte packages

- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/0 Bestuur, Politiek en Ondersteuning** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel0-bestuur-politiek-en-ondersteuning)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/0 Bestuur, Politiek en Ondersteuning/Burgerzaken** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel0-bestuur-politiek-en-ondersteuningburgerzaken)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/0 Bestuur, Politiek en Ondersteuning/Burgerzaken/Model Burgerzaken** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel0-bestuur-politiek-en-ondersteuningburgerzakenmodel-burgerzaken)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/0 Bestuur, Politiek en Ondersteuning/Griffie** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel0-bestuur-politiek-en-ondersteuninggriffie)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/0 Bestuur, Politiek en Ondersteuning/Griffie/Model Griffie** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel0-bestuur-politiek-en-ondersteuninggriffiemodel-griffie) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel0-bestuur-politiek-en-ondersteuninggriffiemodel-griffie)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/1 Veiligheid en Vergunningen** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel1-veiligheid-en-vergunningen)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/1 Veiligheid en Vergunningen/Model VTH** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel1-veiligheid-en-vergunningenmodel-vth) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel1-veiligheid-en-vergunningenmodel-vth)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/10 Dienstverlening** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel10-dienstverlening)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/10 Dienstverlening/Diagram** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel10-dienstverleningdiagram)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/10 Dienstverlening/Model Dienstverlening** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel10-dienstverleningmodel-dienstverlening)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/2 Verkeer, Vervoer en Waterstaat** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel2-verkeer-vervoer-en-waterstaat)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/2 Verkeer, Vervoer en Waterstaat/Mobiliteit/Model Mobiliteit** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel2-verkeer-vervoer-en-waterstaatmobiliteitmodel-mobiliteit) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel2-verkeer-vervoer-en-waterstaatmobiliteitmodel-mobiliteit)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/2 Verkeer, Vervoer en Waterstaat/Parkeren** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel2-verkeer-vervoer-en-waterstaatparkeren)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/2 Verkeer, Vervoer en Waterstaat/Parkeren/Model Parkeren** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel2-verkeer-vervoer-en-waterstaatparkerenmodel-parkeren) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel2-verkeer-vervoer-en-waterstaatparkerenmodel-parkeren)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/3 Economie** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel3-economie)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/3 Economie/Diagram** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel3-economiediagram)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/3 Economie/Model Economie** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel3-economiemodel-economie)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/4 Onderwijs** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel4-onderwijs)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/4 Onderwijs/Leerplicht en Leerlingenvervoer** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel4-onderwijsleerplicht-en-leerlingenvervoer)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/4 Onderwijs/Leerplicht en Leerlingenvervoer/Model Leerplicht en Leerlingenvervoer** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel4-onderwijsleerplicht-en-leerlingenvervoermodel-leerplicht-en-leerlingenvervoer)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/4 Onderwijs/Onderwijs** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel4-onderwijsonderwijs)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/4 Onderwijs/Onderwijs/Diagram** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel4-onderwijsonderwijsdiagram)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/4 Onderwijs/Onderwijs/Model Onderwijs** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel4-onderwijsonderwijsmodel-onderwijs) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel4-onderwijsonderwijsmodel-onderwijs)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatie)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Erfgoed/Archeologie** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatieerfgoedarcheologie)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Erfgoed/Archeologie/Model Archeologie** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatieerfgoedarcheologiemodel-archeologie) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatieerfgoedarcheologiemodel-archeologie)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Erfgoed/Archief** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatieerfgoedarchief)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Erfgoed/Archief/Model Archief** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatieerfgoedarchiefmodel-archief)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Erfgoed/Generieke Entiteiten Erfgoed** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatieerfgoedgenerieke-entiteiten-erfgoed)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Erfgoed/Generieke Entiteiten Erfgoed/Diagram** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatieerfgoedgenerieke-entiteiten-erfgoeddiagram)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Erfgoed/Generieke Entiteiten Erfgoed/Model Erfgoed Generiek** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatieerfgoedgenerieke-entiteiten-erfgoedmodel-erfgoed-generiek)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Erfgoed/Monumenten/Model Monumenten** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatieerfgoedmonumentenmodel-monumenten) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatieerfgoedmonumentenmodel-monumenten)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Musea/Diagram** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatiemuseadiagram)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Musea/Model Musea** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatiemuseamodel-musea) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatiemuseamodel-musea)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Sport** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatiesport)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Sport/Model Sport** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatiesportmodel-sport) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatiesportmodel-sport)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domein)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Dak- en thuislozen** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeindak--en-thuislozen)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Dak- en thuislozen/Diagram** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeindak--en-thuislozendiagram)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Dak- en thuislozen/Model Dak- en thuislozen** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeindak--en-thuislozenmodel-dak--en-thuislozen)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Gemeentebegrafenissen** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeingemeentebegrafenissen)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Gemeentebegrafenissen/Model Gemeentebegrafenissen** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeingemeentebegrafenissenmodel-gemeentebegrafenissen)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Generiek Jeugd en Wmo** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeingeneriek-jeugd-en-wmo)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Generiek Jeugd en Wmo/Model Jeugd en Wmo Generiek** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeingeneriek-jeugd-en-wmomodel-jeugd-en-wmo-generiek) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeingeneriek-jeugd-en-wmomodel-jeugd-en-wmo-generiek)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inburgering/Model Inburgering** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeininburgeringmodel-inburgering) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeininburgeringmodel-inburgering)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Diensten/Model Diensten** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomendienstenmodel-diensten) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomendienstenmodel-diensten)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Model Inkomen** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomenmodel-inkomen) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomenmodel-inkomen)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Normafwijking/Model Normafwijking** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomennormafwijkingmodel-normafwijking) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomennormafwijkingmodel-normafwijking)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Reden aanvraag/Datatypes** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomenreden-aanvraagdatatypes)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Reden aanvraag/Reden aanvraag** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomenreden-aanvraagreden-aanvraag) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomenreden-aanvraagreden-aanvraag)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Terug- en invordering/Model Terug- en invordering** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomenterug--en-invorderingmodel-terug--en-invordering) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomenterug--en-invorderingmodel-terug--en-invordering)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Jeugd** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinjeugd)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Jeugd/Model Jeugd** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinjeugdmodel-jeugd)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Jeugdbescherming en reclassering/Diagram** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinjeugdbescherming-en-reclasseringdiagram)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Jeugdbescherming en reclassering/Model Jeugdbescherming** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinjeugdbescherming-en-reclasseringmodel-jeugdbescherming) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinjeugdbescherming-en-reclasseringmodel-jeugdbescherming)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Schulden/Schuldhulpverlening/Model Schuldhulpverlening** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinschuldenschuldhulpverleningmodel-schuldhulpverlening) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinschuldenschuldhulpverleningmodel-schuldhulpverlening)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Schulden/Vroegsignalering/Model Vroegsignalering** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinschuldenvroegsignaleringmodel-vroegsignalering) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinschuldenvroegsignaleringmodel-vroegsignalering)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiek)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Diagram** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiekdiagram)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiekmodel-sociaal-domein-generiek) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiekmodel-sociaal-domein-generiek)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Inkomsten** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiekmodel-sociaal-domein-generiekinkomsten)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Inkomsten/Datatypes** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiekmodel-sociaal-domein-generiekinkomstendatatypes)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Inkomsten/Model Inkomsten** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiekmodel-sociaal-domein-generiekinkomstenmodel-inkomsten) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiekmodel-sociaal-domein-generiekinkomstenmodel-inkomsten)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Vermogen** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiekmodel-sociaal-domein-generiekvermogen)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Vermogen/Datatypes** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiekmodel-sociaal-domein-generiekvermogendatatypes)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Vermogen/Model Vermogen** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiekmodel-sociaal-domein-generiekvermogenmodel-vermogen) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiekmodel-sociaal-domein-generiekvermogenmodel-vermogen)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociale Teams** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociale-teams)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociale Teams/Model Sociale Teams** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociale-teamsmodel-sociale-teams)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Werk** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinwerk)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Werk/Model Werk** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinwerkmodel-werk) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinwerkmodel-werk)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Wmo** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinwmo)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Wmo/Model Wmo** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinwmomodel-wmo)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel7-volksgezondheid-en-milieu)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel7-volksgezondheid-en-milieuafval)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel7-volksgezondheid-en-milieuafvalmodel-afval) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel7-volksgezondheid-en-milieuafvalmodel-afval)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Beheer Openbare Ruimte** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingbeheer-openbare-ruimte)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Beheer Openbare Ruimte/Model Basis IMBOR/Enumeratiesoort** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingbeheer-openbare-ruimtemodel-basis-imborenumeratiesoort)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Beheer Openbare Ruimte/Model Basis IMBOR/Model IMBOR** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingbeheer-openbare-ruimtemodel-basis-imbormodel-imbor) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingbeheer-openbare-ruimtemodel-basis-imbormodel-imbor)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Beheer Openbare Ruimte/Model Beheer Openbare Ruimte** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingbeheer-openbare-ruimtemodel-beheer-openbare-ruimte) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingbeheer-openbare-ruimtemodel-beheer-openbare-ruimte)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Bouwen en Wonen** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingbouwen-en-wonen)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Bouwen en Wonen/Model Wonen** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingbouwen-en-wonenmodel-wonen) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingbouwen-en-wonenmodel-wonen)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Meldingen Openbare Ruimte** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingmeldingen-openbare-ruimte)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Omgevingswet** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingomgevingswet)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Omgevingswet/Model Omgevingswet** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingomgevingswetmodel-omgevingswet)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Omgevingswet/Model Omgevingswet/Model Aanvragen en Meldingen** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingomgevingswetmodel-omgevingswetmodel-aanvragen-en-meldingen)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Omgevingswet/Model Omgevingswet/Model Officiele Publicaties** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingomgevingswetmodel-omgevingswetmodel-officiele-publicaties)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Omgevingswet/Model Omgevingswet/Model Omgevingswet** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingomgevingswetmodel-omgevingswetmodel-omgevingswet)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Omgevingswet/Model Omgevingswet/Model Toepasbare Regels** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingomgevingswetmodel-omgevingswetmodel-toepasbare-regels)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatie)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/Financien** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatiefinancien)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/Financien/Model Financien** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatiefinancienmodel-financien) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatiefinancienmodel-financien)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/HR** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatiehr)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/HR/Model HR** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatiehrmodel-hr) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatiehrmodel-hr)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/ICT** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatieict)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/ICT/Model ICT** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatieictmodel-ict) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatieictmodel-ict)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/Inkoop** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatieinkoop)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/Inkoop/Diagram** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatieinkoopdiagram)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/Inkoop/Model Inkoop** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatieinkoopmodel-inkoop)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/Organisatie-indeling/Model Organisatie** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatieorganisatie-indelingmodel-organisatie)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/Subsidies** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatiesubsidies)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/Subsidies/Diagram** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatiesubsidiesdiagram)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/Subsidies/Model Subsidies** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatiesubsidiesmodel-subsidies)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/Vastgoed** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatievastgoed)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/Vastgoed/Model Vastgoed** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatievastgoedmodel-vastgoed) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatievastgoedmodel-vastgoed)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kern)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/BAG** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernbag)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/BAG/Model BAG** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernbagmodel-bag) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernbagmodel-bag)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/Dimensies/Model** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kerndimensiesmodel) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kerndimensiesmodel)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/Generiek/Model Generiek** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kerngeneriekmodel-generiek) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kerngeneriekmodel-generiek)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RGBZPlus** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrgbzplus)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RGBZPlus/Diagram** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrgbzplusdiagram)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RGBZPlus/Model RGBZ/Enumeratiesoort** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrgbzplusmodel-rgbzenumeratiesoort)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RGBZPlus/Model RGBZ/Groepattribuutsoort** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrgbzplusmodel-rgbzgroepattribuutsoort) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrgbzplusmodel-rgbzgroepattribuutsoort)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RGBZPlus/Model RGBZ/Metagegevens** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrgbzplusmodel-rgbzmetagegevens) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrgbzplusmodel-rgbzmetagegevens)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RGBZPlus/Model RGBZ/Model Kern RGBZ** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrgbzplusmodel-rgbzmodel-kern-rgbz) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrgbzplusmodel-rgbzmodel-kern-rgbz)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrsgbplus)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/Diagram** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrsgbplusdiagram)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/Diagram RSGB/Catalogus RSGB/Tekenwijze** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrsgbplusdiagram-rsgbcatalogus-rsgbtekenwijze)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Enumeratiesoort** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelenumeratiesoort) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelenumeratiesoort)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Groepattribuutsoort** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelgroepattribuutsoort) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelgroepattribuutsoort)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Model Kern RSGB** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelmodel-kern-rsgb) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelmodel-kern-rsgb)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Referentielijsten** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelreferentielijsten) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelreferentielijsten)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Relatieklasse** — [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelrelatieklasse)
- **Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/archief/Model Kern RSGB** — [structureel](#structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelarchiefmodel-kern-rsgb) · [beschrijvend](#beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelarchiefmodel-kern-rsgb)

## Structurele wijzigingen

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel0-bestuur-politiek-en-ondersteuninggriffiemodel-griffie"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/0 Bestuur, Politiek en Ondersteuning/Griffie/Model Griffie

#### Classes

##### `Aanwezige Deelnemer` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `aanvangAanwezigheid` — Gewijzigd
    - **formele historie**: _(leeg)_ → `Nee`

#### Associaties

- 🟡 Gewijzigd: `Vergadering` → `Aanwezige Deelnemer`
  - **src mult. start**: _(leeg)_ → `1`
  - **src mult. end**: _(leeg)_ → `1`
  - **dst mult. start**: _(leeg)_ → `0`
  - **dst mult. end**: _(leeg)_ → `*`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel1-veiligheid-en-vergunningenmodel-vth"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/1 Veiligheid en Vergunningen/Model VTH

#### Classes

##### `VOMAanvraagOfMelding` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `locatie` — Gewijzigd
    - **primitieve type**: `GML` → `Point`

##### `VTH-Melding` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `locatie` — Gewijzigd
    - **primitieve type**: `GML` → `Point`

#### Associaties

- 🟡 Gewijzigd: `Bevinding` → `Bevinding`
  - **src mult. start**: _(leeg)_ → `1`
  - **src mult. end**: _(leeg)_ → `1`
  - **dst mult. start**: _(leeg)_ → `0`
  - **dst mult. end**: _(leeg)_ → `*`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel2-verkeer-vervoer-en-waterstaatmobiliteitmodel-mobiliteit"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/2 Verkeer, Vervoer en Waterstaat/Mobiliteit/Model Mobiliteit

#### Classes

##### `Strooiroute` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `route` — Gewijzigd
    - **primitieve type**: `MultiCurve` → `GM_MultiCurve`

##### `StrooirouteUitvoering` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `route` — Gewijzigd
    - **primitieve type**: `MultiCurve` → `GM_MultiCurve`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel2-verkeer-vervoer-en-waterstaatparkerenmodel-parkeren"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/2 Verkeer, Vervoer en Waterstaat/Parkeren/Model Parkeren

#### Classes

##### `Parkeerscan` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `coordinaten` — Gewijzigd
    - **primitieve type**: `GML` → `Point`

##### `Parkeervlak` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `coordinaten` — Gewijzigd
    - **primitieve type**: `GML` → `Point`

##### `Parkeerzone` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `geometrie` — Gewijzigd
    - **primitieve type**: `Multivlak` → `GM_MultiSurface`

#### Associaties

- 🟡 Gewijzigd: `Parkeerscan` «verificatie» → `Parkeerrecht`
  - **dst mult. start**: _(leeg)_ → `0`
  - **dst mult. end**: _(leeg)_ → `1`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel4-onderwijsonderwijsmodel-onderwijs"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/4 Onderwijs/Onderwijs/Model Onderwijs

#### Classes

##### `Onderwijssoort` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `onderwijstype` — Gewijzigd
    - **formele historie**: _(leeg)_ → `Nee`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatieerfgoedarcheologiemodel-archeologie"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Erfgoed/Archeologie/Model Archeologie

#### Classes

##### `Kaart` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `content` — Gewijzigd
    - **naam**: `kaart` → `content`

##### `Project` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `coordinaten` — Gewijzigd
    - **primitieve type**: `GML` → `Point`

##### `Vindplaats` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `locatie` — Gewijzigd
    - **primitieve type**: `GML` → `Point`
- 🟡 `vindplaatsOmschrijving` — Gewijzigd
    - **naam**: `vindplaats` → `vindplaatsOmschrijving`

##### `locatie` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `locatiePunt` — Gewijzigd
    - **naam**: `locatie` → `locatiePunt`
    - **primitieve type**: `GML` → `GM_Point`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatieerfgoedmonumentenmodel-monumenten"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Erfgoed/Monumenten/Model Monumenten

#### Associaties

- 🟡 Gewijzigd: `Beschermde Status` «betreft» → `KadastraleOnroerendeZaak`
  - **src mult. start**: _(leeg)_ → `1`
  - **src mult. end**: _(leeg)_ → `1`
  - **dst mult. start**: _(leeg)_ → `0`
  - **dst mult. end**: _(leeg)_ → `*`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatiemuseamodel-musea"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Musea/Model Musea

#### Associaties

- 🟡 Gewijzigd: `Tentoonstelling` → `Zaal`
  - **src mult. start**: _(leeg)_ → `0`
  - **src mult. end**: _(leeg)_ → `*`
  - **dst mult. start**: _(leeg)_ → `0`
  - **dst mult. end**: _(leeg)_ → `*`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatiesportmodel-sport"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Sport/Model Sport

#### Classes

##### `Aantal` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `aantalMateriaal` — Gewijzigd
    - **naam**: `aantal` → `aantalMateriaal`

##### `Binnenlocatie` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `locatie` — Gewijzigd
    - **primitieve type**: `GML` → `Point`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeingeneriek-jeugd-en-wmomodel-jeugd-en-wmo-generiek"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Generiek Jeugd en Wmo/Model Jeugd en Wmo Generiek

#### Classes

##### `Beschikking` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `wet` — Gewijzigd
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Generiek Jeugd en Wmo/Model Jeugd en Wmo Generiek::Wet`

#### Associaties

- 🟡 Gewijzigd: `AOM_AanvraagWmoJeugd` «heeft» → `Client`
  - **src mult. start**: _(leeg)_ → `0`
  - **src mult. end**: _(leeg)_ → `*`
  - **dst mult. start**: _(leeg)_ → `1`
  - **dst mult. end**: _(leeg)_ → `1`
- 🟡 Gewijzigd: `AOMMeldingWmoJeugd` «heeft» → `Client`
  - **src mult. start**: _(leeg)_ → `0`
  - **src mult. end**: _(leeg)_ → `*`
  - **dst mult. start**: _(leeg)_ → `1`
  - **dst mult. end**: _(leeg)_ → `1`
- 🟡 Gewijzigd: `Beschikking` «betreft» → `AOMMeldingWmoJeugd`
  - **src mult. start**: _(leeg)_ → `0`
  - **src mult. end**: _(leeg)_ → `*`
  - **dst mult. start**: _(leeg)_ → `0`
  - **dst mult. end**: _(leeg)_ → `*`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeininburgeringmodel-inburgering"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inburgering/Model Inburgering

#### Classes

##### `KNM` — 🔴 Verwijderd

##### `Onderwijsroute` — 🔴 Verwijderd

##### `ParticipatieComponent` — 🔴 Verwijderd

##### `Taalonderwijs deelname` — 🔴 Verwijderd

##### `Verblijfplaats` — 🔴 Verwijderd

##### `Aandachtspunt` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `aandachtspuntOmschrijving` — Gewijzigd
    - **naam**: `Aandachtspunt` → `aandachtspuntOmschrijving`

##### `Brede Intake` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟢 `AantalUrenAlfabetiseringsOnderwijs` — Toegevoegd
- 🟢 `DatumTot(Peildatum)` — Toegevoegd
- 🟢 `einddatum` — Toegevoegd
- 🟢 `GevolgdeUrenKNMenTaalles` — Toegevoegd
- 🟢 `startdatum` — Toegevoegd
- 🟢 `UrenGeoorloofdVerzuim` — Toegevoegd
- 🟢 `UrenOngeoorloofdVerzuim` — Toegevoegd

##### `Educatie` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `EducatieLand` — Gewijzigd
    - **primitieve type**: `Enum` → _(leeg)_
    - **type (class)**: _(leeg)_ → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Referentielijsten::Land`

##### `Examen` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟢 `ExamenResultaat` — Toegevoegd

##### `Examenonderdeel` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟢 `BehaaldeScore` — Toegevoegd
- 🟢 `DatumRegistratieUitslag` — Toegevoegd
- 🟢 `ExamenOnderdeelSpecificatie` — Toegevoegd
- 🟢 `Ontheffing` — Toegevoegd
- 🟢 `RedenVrijstelling` — Toegevoegd
- 🟢 `Resultaat` — Toegevoegd

##### `Inburgeraar` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `Gedetailleerde Doelgroep` — Gewijzigd
    - **enumeratie**: `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Generiek Jeugd en Wmo/Model Jeugd en Wmo Generiek::Doelgroep` → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inburgering/Model Inburgering::Doelgroep`

##### `InburgeringsAanbod` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `CursusInstelling` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `AN200`
    - **type (class)**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inburgering/Model Inburgering::Onderwijsroute` → _(leeg)_

##### `Inburgeringstraject` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟢 `UItkomstLeerbaarheidstoets` — Toegevoegd

##### `Leerroute` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `geenLeerbaarheidstoetsZB` — Gewijzigd
    - **naam**: `IndicatorLeerbaarheidstoetsOvergeslagenVanwegeZintuigelijkeBeperking` → `geenLeerbaarheidstoetsZB`

##### `MAP` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟢 `DatumEindgesprekMAP` — Toegevoegd
- 🟢 `IndicatorVerwijtbaar` — Toegevoegd
- 🟢 `RedenNietSuccesvolVoltooid` — Toegevoegd
- 🟢 `Resultaat` — Toegevoegd

##### `Ontwikkelwens` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `ontwikkelwensOmschrijving` — Gewijzigd
    - **naam**: `Ontwikkelwens` → `ontwikkelwensOmschrijving`

##### `PIP` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟢 `DagtekeningInitielePIP` — Toegevoegd
- 🟢 `DagtekeningPIP` — Toegevoegd
- 🟢 `EmailContactPersoon` — Toegevoegd
- 🟢 `IndicatorMagOpleidingAfmaken` — Toegevoegd
- 🟢 `NaamContactPersoon` — Toegevoegd

##### `PVT` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟢 `DatumOndertekening PVT` — Toegevoegd
- 🟢 `RedenNietVoldaan` — Toegevoegd
- 🟢 `Resultaat` — Toegevoegd
- 🟢 `VerwijtbaarNietVoldaan` — Toegevoegd

##### `Taalvaardigheid` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `TaalvaardigheidOverall` — Gewijzigd
    - **naam**: `Taalvaardigheid` → `TaalvaardigheidOverall`

##### `Training` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `TrainingGevolgd` — Gewijzigd
    - **naam**: `Training` → `TrainingGevolgd`

##### `Verblijfplaats AZC` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟢 `Huisnummer` — Toegevoegd
- 🟢 `Plaats` — Toegevoegd
- 🟢 `Straatnummer` — Toegevoegd

##### `Verlengingsgrond` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `Verlengingsgrondslag` — Gewijzigd
    - **naam**: `Verlengingsgrond` → `Verlengingsgrondslag`

##### `Z-route` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟢 `AantalGratisExamenpogingenTegoed` — Toegevoegd
- 🟢 `ExamenDatum` — Toegevoegd
- 🟢 `GevolgdeUrenParticipatieActiviteiten` — Toegevoegd
- 🟢 `Niveau` — Toegevoegd
- 🟢 `Onderdeel` — Toegevoegd
- 🟢 `RedenGeenResultaat` — Toegevoegd
- 🟢 `Resultaat` — Toegevoegd

#### Enumeraties

##### `Doelgroep` — 🟢 Toegevoegd

**Literals:**

- 🟢 `Arbeidsmigranten met vestigingsintentie` — Toegevoegd
- 🟢 `EU-burgers` — Toegevoegd
- 🟢 `Expats en kennismigranten` — Toegevoegd
- 🟢 `Gezinsmigranten` — Toegevoegd
- 🟢 `Internationale studenten (blijvers)` — Toegevoegd
- 🟢 `Kwetsbare nieuwkomers` — Toegevoegd
- 🟢 `Nieuwkomers` — Toegevoegd
- 🟢 `Oudkomers` — Toegevoegd

#### Associaties

- 🟢 Toegevoegd: `Z-route` «heeft (onderdeel van)» → `Leerroute`
- 🔴 Verwijderd: `Inburgeraar` → `Taalonderwijs deelname`
- 🔴 Verwijderd: `KNM` «Onderdeel van» → `Leerroute`
- 🔴 Verwijderd: `ParticipatieComponent` «Activiteit van» → `Z-route`
- 🟡 Gewijzigd: `Aanvraag verlenging Inburgeringstermijn` → `Verlengingsgrond`
  - **src mult. start**: _(leeg)_ → `1`
  - **src mult. end**: _(leeg)_ → `1`
  - **dst mult. start**: _(leeg)_ → `1`
  - **dst mult. end**: _(leeg)_ → `*`
- 🟡 Gewijzigd: `Brede Intake` «onderdeel van» → `Inburgeringstraject`
  - **src mult. start**: `0` → `1`
- 🟡 Gewijzigd: `Inburgeraar` «heeft» → `Aandachtspunt `
  - **src mult. start**: _(leeg)_ → `1`
  - **src mult. end**: _(leeg)_ → `1`
- 🟡 Gewijzigd: `Inburgeraar` «heeft» → `Aanvraag verlenging Inburgeringstermijn`
  - **src mult. start**: _(leeg)_ → `1`
  - **src mult. end**: _(leeg)_ → `1`
  - **dst mult. start**: _(leeg)_ → `0`
  - **dst mult. end**: _(leeg)_ → `1`
- 🟡 Gewijzigd: `Inburgeraar` «heeft» → `Hoofddoel`
  - **src mult. start**: _(leeg)_ → `1`
  - **src mult. end**: _(leeg)_ → `1`
- 🟡 Gewijzigd: `Inburgeraar` «heeft» → `Ontwikkelwens `
  - **src mult. start**: _(leeg)_ → `1`
  - **src mult. end**: _(leeg)_ → `1`
- 🟡 Gewijzigd: `Inburgeringsplicht` «heeft» → `Inburgeringstermijn`
  - **naam**: _(leeg)_ → `heeft`
- 🟡 Gewijzigd: `Ontheffing` «ontheffing voor» → `Examenonderdeel`
  - **dst mult. start**: _(leeg)_ → `0`
  - **dst mult. end**: _(leeg)_ → `*`
- 🟡 Gewijzigd: `Voorbereiding op Inburgering` «bestaat uit» → `Introductiemodule`
  - **src mult. start**: _(leeg)_ → `1`
  - **src mult. end**: _(leeg)_ → `1`
  - **dst mult. start**: _(leeg)_ → `1`
  - **dst mult. end**: _(leeg)_ → `*`

#### Generalisaties

- 🔴 Verwijderd: `Onderwijsroute` ⟶ `Leerroute`
- 🔴 Verwijderd: `Z-route` ⟶ `Leerroute`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomendienstenmodel-diensten"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Diensten/Model Diensten

#### Classes

##### `Betalingsblokkade` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Betalingsblokkade.Id` — Verwijderd

##### `Diensttype` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Diensttype.Id` — Verwijderd
- 🟡 `minBetrouwbaarheidsniveau` — Gewijzigd
    - **naam**: `Minimaal vereist betrouwbaarheidsniveau eDienstverlening` → `minBetrouwbaarheidsniveau`

##### `Leveringscomponent` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Leveringscomponent.Id` — Verwijderd
- 🟡 `Bedrag` — Gewijzigd
    - **primitieve type**: `Geldbedrag` → `bedrag`
- 🟡 `Einddatum` — Gewijzigd
    - **primitieve type**: `Geldbedrag` → `bedrag`
- 🟡 `Omschrijving afwijking` — Gewijzigd
    - **primitieve type**: `Geldbedrag` → `bedrag`
- 🟡 `Percentage` — Gewijzigd
    - **primitieve type**: `Geldbedrag` → `bedrag`
- 🟡 `Periode startdatum` — Gewijzigd
    - **primitieve type**: `Geldbedrag` → `bedrag`
- 🟡 `Soort` — Gewijzigd
    - **primitieve type**: `Geldbedrag` → `bedrag`

##### `Leveringscomponenttype` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Leveringscomponenttype.Id` — Verwijderd

##### `Leveringsopdracht` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Leveringsopdracht.Id` — Verwijderd
- 🟡 `Leveringskanaal` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `AN200`
    - **enumeratie**: `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Terug- en invordering/Datatypes::DefaultEnumeratie` → _(leeg)_

##### `Leveringsspecificatie` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Leveringsspecificatie.Id` — Verwijderd

##### `Periodiek dienst Bijz. bijstand` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `PeriodiekDienstBijzBijstand.Id` — Verwijderd

##### `Referteperiode` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Referteperiode.Id` — Verwijderd

##### `Regeling` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Regeling.Id` — Verwijderd

##### `Verstrekkingsvorm` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Verstrekkingsvorm.Id` — Verwijderd

##### `Voorwaarde` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `VoorwaardeId` — Verwijderd
- 🟡 `Verantwoording vaststelling` — Gewijzigd
    - **primitieve type**: `Brontype` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Terug- en invordering/Datatypes::Brontype`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomenmodel-inkomen"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Model Inkomen

#### Classes

##### `Component` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `debetCredit` — Gewijzigd
    - **lengte**: `50` → `50.0`
- 🟡 `groep` — Gewijzigd
    - **lengte**: `50` → `50.0`
- 🟡 `groepcode` — Gewijzigd
    - **lengte**: `20` → `20.0`
- 🟡 `grootboekcode` — Gewijzigd
    - **lengte**: `50` → `50.0`
- 🟡 `grootboekomschrijving` — Gewijzigd
    - **lengte**: `100` → `100.0`
- 🟡 `kostenplaats` — Gewijzigd
    - **lengte**: `50` → `50.0`
- 🟡 `omschrijving` — Gewijzigd
    - **lengte**: `100` → `100.0`
- 🟡 `rekeningNummer` — Gewijzigd
    - **lengte**: `50` → `50.0`
- 🟡 `toelichting` — Gewijzigd
    - **lengte**: `50` → `50.0`

##### `ComponentSoort` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `componentcode` — Gewijzigd
    - **lengte**: `50` → `50.0`
- 🟡 `kolom` — Gewijzigd
    - **lengte**: `50` → `50.0`
- 🟡 `kolomcode` — Gewijzigd
    - **lengte**: `50` → `50.0`
- 🟡 `regeling` — Gewijzigd
    - **lengte**: `100` → `100.0`
- 🟡 `regelingcode` — Gewijzigd
    - **lengte**: `50` → `50.0`

##### `Huisvestingsoort` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `soorthuisvestingCode` — Gewijzigd
    - **lengte**: `4` → `4.0`

##### `Inkomensvoorziening` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `betalingsmomentcode` — Gewijzigd
    - **lengte**: `4` → `4.0`
- 🟡 `code` — Gewijzigd
    - **lengte**: `4` → `4.0`
- 🟡 `groep` — Gewijzigd
    - **lengte**: `100` → `100.0`
- 🟡 `versterkkingsvorm` — Gewijzigd
    - **lengte**: `200` → `200.0`

##### `Inkomensvoorzieningsoort` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `code` — Gewijzigd
    - **lengte**: `20` → `20.0`
- 🟡 `naam` — Gewijzigd
    - **lengte**: `80` → `80.0`
- 🟡 `regeling` — Gewijzigd
    - **lengte**: `200` → `200.0`
- 🟡 `regelingscode` — Gewijzigd
    - **lengte**: `20` → `20.0`
- 🟡 `vergoeding` — Gewijzigd
    - **lengte**: `200` → `200.0`
- 🟡 `vergoedingscode` — Gewijzigd
    - **lengte**: `20` → `20.0`

##### `RedenBlokkering` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `redenBlokkeringCode` — Gewijzigd
    - **lengte**: `4` → `4.0`

##### `RedenInstroom` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `CBS-code` — Gewijzigd
    - **lengte**: `4` → `4.0`
- 🟡 `redenInstroomCode` — Gewijzigd
    - **lengte**: `4` → `4.0`

##### `RedenUitstroom` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `CBS-code` — Gewijzigd
    - **lengte**: `4` → `4.0`
- 🟡 `redenUitstroomCode` — Gewijzigd
    - **lengte**: `4` → `4.0`

##### `Regelingsoort` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `naam` — Gewijzigd
    - **lengte**: `80` → `80.0`

##### `UitkeringsRun` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `frequentie` — Gewijzigd
    - **lengte**: `20` → `20.0`
- 🟡 `periodeRun` — Gewijzigd
    - **lengte**: `20` → `20.0`
- 🟡 `soortRun` — Gewijzigd
    - **lengte**: `50` → `50.0`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomennormafwijkingmodel-normafwijking"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Normafwijking/Model Normafwijking

#### Classes

##### `Afwijkende maatregel` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `Bedrag` — Gewijzigd
    - **primitieve type**: `Geldbedrag` → `Bedrag`
- 🟡 `Code reden afwijking maatregel` — Gewijzigd
    - **primitieve type**: `Geldbedrag` → `Bedrag`
- 🟡 `Motivatie afwijking maatregel` — Gewijzigd
    - **primitieve type**: `Geldbedrag` → `Bedrag`
- 🟡 `Percentage` — Gewijzigd
    - **primitieve type**: `Geldbedrag` → `Bedrag`

##### `Boete` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `Bedrag boete` — Gewijzigd
    - **primitieve type**: `Geldbedrag` → `Bedrag`
- 🟡 `Boetevorm` — Gewijzigd
    - **primitieve type**: `Geldbedrag` → `Bedrag`
- 🟡 `Reden boete` — Gewijzigd
    - **primitieve type**: `Geldbedrag` → `Bedrag`
- 🟡 `Voorwaarde boete` — Gewijzigd
    - **primitieve type**: `Geldbedrag` → `Bedrag`

##### `Maatregel` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `identificatie` — Gewijzigd
    - **naam**: `Maatregel ID` → `identificatie`

##### `Normafwijking` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `identificatie` — Gewijzigd
    - **naam**: `Normafwijking ID` → `identificatie`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomenreden-aanvraagdatatypes"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Reden aanvraag/Datatypes

#### Datatypes

##### `CdRedenAanvraagANWaangevraagd` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Ja, deze is afgewezen` — Verwijderd
- 🔴 `Ja, deze is toegekend` — Verwijderd
- 🔴 `Ja, ik wacht nog op een besluit` — Verwijderd
- 🔴 `Nee` — Verwijderd

##### `CdRedenAanvraagANWafgewezenReden` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Ik ben minder dan 45% arbeidsongeschikt` — Verwijderd
- 🔴 `Ik heb geen minderjarige kinderen` — Verwijderd

##### `CdRedenAanvraagContractperiode` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Ik had een contract van 6 maanden of langer` — Verwijderd
- 🔴 `Ik had een contract van minder dan 6 maanden` — Verwijderd

##### `CdRedenAanvraagEindeBijstand` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Aangaan relatie met nieuwe partner` — Verwijderd
- 🔴 `Andere reden` — Verwijderd
- 🔴 `Verhuizing vanuit andere gemeente` — Verwijderd

##### `CdRedenAanvraagEindeEigenBedrijf` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Andere reden` — Verwijderd
- 🔴 `Bedrijf verkocht` — Verwijderd
- 🔴 `Faillissement` — Verwijderd
- 🔴 `Financiële redenen` — Verwijderd
- 🔴 `Sluiting opgelegd door de gemeente` — Verwijderd
- 🔴 `Zelf gestopt` — Verwijderd

##### `CdRedenAanvraagEindeUitkering` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Andere uitkering` — Verwijderd
- 🔴 `Wao/Wia` — Verwijderd
- 🔴 `Wga` — Verwijderd
- 🔴 `WW` — Verwijderd
- 🔴 `Ziektewet` — Verwijderd

##### `CdRedenAanvraagEindeUitkeringReden` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Andere reden` — Verwijderd
- 🔴 `Arbeidsgeschikt verklaard` — Verwijderd
- 🔴 `Gedeeltelijk arbeidsgeschikt verklaard` — Verwijderd
- 🔴 `Maximale duur uitkering bereikt` — Verwijderd
- 🔴 `Opgelegde maatregel` — Verwijderd

##### `CdRedenAanvraagEindeWerk` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Andere reden` — Verwijderd
- 🔴 `Faillissement bedrijf` — Verwijderd
- 🔴 `Ontslagen` — Verwijderd
- 🔴 `Ontslagen bij een reorganisatie` — Verwijderd
- 🔴 `Tijdelijk contract is afgelopen` — Verwijderd
- 🔴 `Zelf ontslag genomen` — Verwijderd
- 🔴 `Ziekte` — Verwijderd

##### `CdRedenAanvraagOnvoldoendeInkomen` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Ik heb geen werk meer` — Verwijderd
- 🔴 `Ik heb wel inkomsten, maar die zijn te laag` — Verwijderd
- 🔴 `In staking bij werkgever of als groep uitgesloten voor werk` — Verwijderd
- 🔴 `Mijn alimentatie is gestopt` — Verwijderd
- 🔴 `Mijn bijstandsuitkering is stopgezet` — Verwijderd
- 🔴 `Mijn eerdere bijstandsaanvraag is afgewezen of niet in behandeling genomen` — Verwijderd
- 🔴 `Mijn studiefinanciering is gestopt` — Verwijderd
- 🔴 `Mijn uitkering (geen bijstandsuitkering) is stopgezet` — Verwijderd
- 🔴 `Van spaargeld geleefd` — Verwijderd

##### `CdRedenAanvraagVerblijfstatus` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Ik heb een verblijfsvergunning gekregen` — Verwijderd
- 🔴 `Ik heb een verblijfsvergunning gekregen en vertrek uit een asielzoekerscentrum` — Verwijderd

##### `CdRedenAanvraagWWgevraagd` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Ja, ik ontvang nu een WW-uitkering` — Verwijderd
- 🔴 `Ja, ik wacht nog op antwoord` — Verwijderd
- 🔴 `Ja, maar mijn WW-aanvraag is afgewezen` — Verwijderd
- 🔴 `Nee, ik heb geen WW-uitkering aangevraagd` — Verwijderd

##### `CdRedenAanvraagWijzigingGezin` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Ik had een eigen uitkering, maar doe nu een nieuwe aanvraag samen met mijn partner` — Verwijderd
- 🔴 `Mijn partner is overleden` — Verwijderd
- 🔴 `Mijn relatie is verbroken` — Verwijderd

##### `CdRedenAanvraagWwafgewezen` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Ik ben door eigen schuld ontslagen of heb zelf ontslag genomen` — Verwijderd
- 🔴 `Ik ben minder dan 5 uren per week achteruit gegaan in uren` — Verwijderd
- 🔴 `Ik ben niet voldoende beschikbaar voor werk` — Verwijderd
- 🔴 `Ik heb in de periode ervoor onvoldoende gewerkt (wekeneis)` — Verwijderd

##### `CdRedenAanvraagZelfstandige` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Ik ben gestopt met mijn eigen bedrijf` — Verwijderd
- 🔴 `Ik heb een eigen bedrijf, maar onvoldoende inkomen` — Verwijderd

##### `CodeRedenAfwijkendeStartdatum` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Andere reden afwijkende startdatum` — Verwijderd
- 🔴 `Opname instelling` — Verwijderd
- 🔴 `Wachten beslissing instantie` — Verwijderd
- 🔴 `Wachten DigiD` — Verwijderd

##### `RedenKwijtscheldingVordering` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Ambtshalve` — Verwijderd
- 🔴 `Beleid - Nette betaling gedurende afgesproken periode` — Verwijderd
- 🔴 `Beleid - Overig` — Verwijderd
- 🔴 `Externe reden (schuldsanering)` — Verwijderd

#### Enumeraties

##### `CdRedenAanvraagANWaangevraagd` — 🟢 Toegevoegd

**Literals:**

- 🟢 `Ja, deze is afgewezen` — Toegevoegd
- 🟢 `Ja, deze is toegekend` — Toegevoegd
- 🟢 `Ja, ik wacht nog op een besluit` — Toegevoegd
- 🟢 `Nee` — Toegevoegd

##### `CdRedenAanvraagANWafgewezenReden` — 🟢 Toegevoegd

**Literals:**

- 🟢 `Ik ben minder dan 45% arbeidsongeschikt` — Toegevoegd
- 🟢 `Ik heb geen minderjarige kinderen` — Toegevoegd

##### `CdRedenAanvraagContractperiode` — 🟢 Toegevoegd

**Literals:**

- 🟢 `Ik had een contract van 6 maanden of langer` — Toegevoegd
- 🟢 `Ik had een contract van minder dan 6 maanden` — Toegevoegd

##### `CdRedenAanvraagEindeBijstand` — 🟢 Toegevoegd

**Literals:**

- 🟢 `Aangaan relatie met nieuwe partner` — Toegevoegd
- 🟢 `Andere reden` — Toegevoegd
- 🟢 `Verhuizing vanuit andere gemeente` — Toegevoegd

##### `CdRedenAanvraagEindeEigenBedrijf` — 🟢 Toegevoegd

**Literals:**

- 🟢 `Andere reden` — Toegevoegd
- 🟢 `Bedrijf verkocht` — Toegevoegd
- 🟢 `Faillissement` — Toegevoegd
- 🟢 `Financiële redenen` — Toegevoegd
- 🟢 `Sluiting opgelegd door de gemeente` — Toegevoegd
- 🟢 `Zelf gestopt` — Toegevoegd

##### `CdRedenAanvraagEindeUitkering` — 🟢 Toegevoegd

**Literals:**

- 🟢 `Andere uitkering` — Toegevoegd
- 🟢 `WW` — Toegevoegd
- 🟢 `Wao/Wia` — Toegevoegd
- 🟢 `Wga` — Toegevoegd
- 🟢 `Ziektewet` — Toegevoegd

##### `CdRedenAanvraagEindeUitkeringReden` — 🟢 Toegevoegd

**Literals:**

- 🟢 `Andere reden` — Toegevoegd
- 🟢 `Arbeidsgeschikt verklaard` — Toegevoegd
- 🟢 `Gedeeltelijk arbeidsgeschikt verklaard` — Toegevoegd
- 🟢 `Maximale duur uitkering bereikt` — Toegevoegd
- 🟢 `Opgelegde maatregel` — Toegevoegd

##### `CdRedenAanvraagEindeWerk` — 🟢 Toegevoegd

**Literals:**

- 🟢 `Andere reden` — Toegevoegd
- 🟢 `Faillissement bedrijf` — Toegevoegd
- 🟢 `Ontslagen` — Toegevoegd
- 🟢 `Ontslagen bij een reorganisatie` — Toegevoegd
- 🟢 `Tijdelijk contract is afgelopen` — Toegevoegd
- 🟢 `Zelf ontslag genomen` — Toegevoegd
- 🟢 `Ziekte` — Toegevoegd

##### `CdRedenAanvraagOnvoldoendeInkomen` — 🟢 Toegevoegd

**Literals:**

- 🟢 `Ik heb geen werk meer` — Toegevoegd
- 🟢 `Ik heb wel inkomsten, maar die zijn te laag` — Toegevoegd
- 🟢 `In staking bij werkgever of als groep uitgesloten voor werk` — Toegevoegd
- 🟢 `Mijn alimentatie is gestopt` — Toegevoegd
- 🟢 `Mijn bijstandsuitkering is stopgezet` — Toegevoegd
- 🟢 `Mijn eerdere bijstandsaanvraag is afgewezen of niet in behandeling genomen` — Toegevoegd
- 🟢 `Mijn studiefinanciering is gestopt` — Toegevoegd
- 🟢 `Mijn uitkering (geen bijstandsuitkering) is stopgezet` — Toegevoegd
- 🟢 `Van spaargeld geleefd` — Toegevoegd

##### `CdRedenAanvraagVerblijfstatus` — 🟢 Toegevoegd

**Literals:**

- 🟢 `Ik heb een verblijfsvergunning gekregen` — Toegevoegd
- 🟢 `Ik heb een verblijfsvergunning gekregen en vertrek uit een asielzoekerscentrum` — Toegevoegd

##### `CdRedenAanvraagWijzigingGezin` — 🟢 Toegevoegd

**Literals:**

- 🟢 `Ik had een eigen uitkering, maar doe nu een nieuwe aanvraag samen met mijn partner` — Toegevoegd
- 🟢 `Mijn partner is overleden` — Toegevoegd
- 🟢 `Mijn relatie is verbroken` — Toegevoegd

##### `CdRedenAanvraagWwafgewezen` — 🟢 Toegevoegd

**Literals:**

- 🟢 `Ik ben door eigen schuld ontslagen of heb zelf ontslag genomen` — Toegevoegd
- 🟢 `Ik ben minder dan 5 uren per week achteruit gegaan in uren` — Toegevoegd
- 🟢 `Ik ben niet voldoende beschikbaar voor werk` — Toegevoegd
- 🟢 `Ik heb in de periode ervoor onvoldoende gewerkt (wekeneis)` — Toegevoegd

##### `CdRedenAanvraagWWgevraagd` — 🟢 Toegevoegd

**Literals:**

- 🟢 `Ja, ik ontvang nu een WW-uitkering` — Toegevoegd
- 🟢 `Ja, ik wacht nog op antwoord` — Toegevoegd
- 🟢 `Ja, maar mijn WW-aanvraag is afgewezen` — Toegevoegd
- 🟢 `Nee, ik heb geen WW-uitkering aangevraagd` — Toegevoegd

##### `CdRedenAanvraagZelfstandige` — 🟢 Toegevoegd

**Literals:**

- 🟢 `Ik ben gestopt met mijn eigen bedrijf` — Toegevoegd
- 🟢 `Ik heb een eigen bedrijf, maar onvoldoende inkomen` — Toegevoegd

##### `CodeRedenAfwijkendeStartdatum` — 🟢 Toegevoegd

**Literals:**

- 🟢 `Andere reden afwijkende startdatum` — Toegevoegd
- 🟢 `Opname instelling` — Toegevoegd
- 🟢 `Wachten DigiD` — Toegevoegd
- 🟢 `Wachten beslissing instantie` — Toegevoegd

##### `RedenKwijtscheldingVordering` — 🟢 Toegevoegd

**Literals:**

- 🟢 `Ambtshalve` — Toegevoegd
- 🟢 `Beleid - Nette betaling gedurende afgesproken periode` — Toegevoegd
- 🟢 `Beleid - Overig` — Toegevoegd
- 🟢 `Externe reden (schuldsanering)` — Toegevoegd

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomenreden-aanvraagreden-aanvraag"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Reden aanvraag/Reden aanvraag

#### Classes

##### `Andere reden afwijkende startdatum` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `omschrijvingBijzondereReden` — Gewijzigd
    - **naam**: `Specificatie bijzondere reden later ingaan startdatum aanvraag` → `omschrijvingBijzondereReden`

##### `Gestopt betaald werk` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `Afwijsreden WW-aanvraag` — Gewijzigd
    - **primitieve type**: `CdRedenAanvraagWwafgewezen` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Reden aanvraag/Datatypes::CdRedenAanvraagWwafgewezen`
- 🟡 `Contractperiode` — Gewijzigd
    - **primitieve type**: `CdRedenAanvraagContractperiode` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Reden aanvraag/Datatypes::CdRedenAanvraagContractperiode`
- 🟡 `Reden einde werk` — Gewijzigd
    - **primitieve type**: `CdRedenAanvraagEindeWerk` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Reden aanvraag/Datatypes::CdRedenAanvraagEindeWerk`
- 🟡 `WW-uitkering aangevraagd` — Gewijzigd
    - **primitieve type**: `CdRedenAanvraagWWgevraagd` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Reden aanvraag/Datatypes::CdRedenAanvraagWWgevraagd`

##### `Gestopt of verkocht eigen bedrijf` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `Reden eigen bedrijfs gestopt` — Gewijzigd
    - **primitieve type**: `CdRedenAanvraagEindeEigenBedrijf` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Reden aanvraag/Datatypes::CdRedenAanvraagEindeEigenBedrijf`

##### `Gestopte bijstanduitkering` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `Reden einde bijstandsuitkering` — Gewijzigd
    - **primitieve type**: `CdRedenAanvraagEindeBijstand` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Reden aanvraag/Datatypes::CdRedenAanvraagEindeBijstand`

##### `Gestopte of verlaagde alimentatie` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `Nabestaandeuitkering aangevraagd` — Gewijzigd
    - **primitieve type**: `CdRedenAanvraagANWaangevraagd` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Reden aanvraag/Datatypes::CdRedenAanvraagANWaangevraagd`

##### `Gestopte uitkering` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `minderDan35%AO` — Gewijzigd
    - **naam**: `Minder dan 35% arbeidsongeschikt verklaard` → `minderDan35%AO`
- 🟡 `Reden einde uitkering` — Gewijzigd
    - **primitieve type**: `CdRedenAanvraagEindeUitkeringReden` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Reden aanvraag/Datatypes::CdRedenAanvraagEindeUitkeringReden`
- 🟡 `Uitkering` — Gewijzigd
    - **primitieve type**: `CdRedenAanvraagEindeUitkering` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Reden aanvraag/Datatypes::CdRedenAanvraagEindeUitkering`

##### `Overleden partner` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `Reden ANW afgewezen` — Gewijzigd
    - **primitieve type**: `CdRedenAanvraagANWafgewezenReden` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Reden aanvraag/Datatypes::CdRedenAanvraagANWafgewezenReden`

##### `Reden aanvraag Levensonderhoud` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `Onvoldoende inkomen` — Gewijzigd
    - **primitieve type**: `CdRedenAanvraagOnvoldoendeInkomen` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Reden aanvraag/Datatypes::CdRedenAanvraagOnvoldoendeInkomen`
- 🟡 `Reden` — Gewijzigd
    - **primitieve type**: `RedenKwijtscheldingVordering` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Reden aanvraag/Datatypes::RedenKwijtscheldingVordering`
- 🟡 `Verblijfstatus` — Gewijzigd
    - **primitieve type**: `CdRedenAanvraagVerblijfstatus` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Reden aanvraag/Datatypes::CdRedenAanvraagVerblijfstatus`
- 🟡 `Wijziging gezin` — Gewijzigd
    - **primitieve type**: `CdRedenAanvraagWijzigingGezin` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Reden aanvraag/Datatypes::CdRedenAanvraagWijzigingGezin`
- 🟡 `Zelfstandige` — Gewijzigd
    - **primitieve type**: `CdRedenAanvraagZelfstandige` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Reden aanvraag/Datatypes::CdRedenAanvraagZelfstandige`

##### `Reden afwijkende startdatum` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `RedenAfwijkendeStartdatumType` — Gewijzigd
    - **primitieve type**: `CodeRedenAfwijkendeStartdatum` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Reden aanvraag/Datatypes::CodeRedenAfwijkendeStartdatum`

##### `Vertrek uit asielzoekerscentrum` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `Bedrag weekgeld COA` — Gewijzigd
    - **primitieve type**: `Geldbedrag` → `bedrag`
- 🟡 `Einddatum weekgeld COA` — Gewijzigd
    - **primitieve type**: `Geldbedrag` → `bedrag`
- 🟡 `Ingangsdatum huurcontract` — Gewijzigd
    - **primitieve type**: `Geldbedrag` → `bedrag`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomenterug--en-invorderingmodel-terug--en-invordering"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Terug- en invordering/Model Terug- en invordering

#### Classes

##### `Aflossing` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Aflossing.Id` — Verwijderd

##### `Aflossingsafspraak` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Aflossingsafspraak.Id` — Verwijderd

##### `Aflossingsplan` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Aflossingsplan.Id` — Verwijderd

##### `Afschrijving` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Afschrijving.Id` — Verwijderd
- 🟡 `Reden afschrijving` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `CharacterString`
    - **enumeratie**: `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Terug- en invordering/Datatypes::DefaultEnumeratie` → _(leeg)_

##### `Betaalcomponent` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Betaalcomponent.Id` — Verwijderd
- 🟡 `Bedrag` — Gewijzigd
    - **primitieve type**: `Geldbedrag` → `bedrag`
- 🟡 `Boekingsdatum` — Gewijzigd
    - **primitieve type**: `Geldbedrag` → `Date`

##### `Boetevordering` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Boetevordering.Id` — Verwijderd

##### `Conservatoir beslag` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `ConservatoirBeslag.Id` — Verwijderd

##### `Correctie` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Correctie.Id` — Verwijderd

##### `Debiteur` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Debiteur.Id` — Verwijderd

##### `Incassokostenvordering` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Incassokostenvordering.Id` — Verwijderd

##### `Interventie` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Interventie.Id` — Verwijderd

##### `Interventieverzoek` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Interventieverzoek.Id` — Verwijderd

##### `Krediethypotheek` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Krediethypotheek.Id` — Verwijderd

##### `Krediethypotheekvordering` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Krediethypotheekvordering.Id` — Verwijderd

##### `Kwijtschelding` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Kwijtschelding.Id` — Verwijderd

##### `Leenbijstand` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Leenbijstand.Id` — Verwijderd

##### `Leenbijstandvordering` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Leenbijstandvordering.Id` — Verwijderd

##### `Loonbeslagafspraak` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Loonbeslagafspraak.Id` — Verwijderd

##### `Rechtmaand` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Rechtmaand.Id` — Verwijderd

##### `Rentevordering` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Rentevordering.Id` — Verwijderd

##### `Restitutie` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Restitutie.Id` — Verwijderd

##### `Terugvorderingsverzoek` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Terugvorderingsverzoek.Id` — Verwijderd

##### `Uitstel aflossing` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `UitstelAflossing.Id` — Verwijderd

##### `Vermindering terugvordering` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `VerminderingTerugvordering.Id` — Verwijderd

##### `Verrekening` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Verrekening.Id` — Verwijderd

##### `Verwijtbare vordering` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `VerwijtbareVordering.Id` — Verwijderd

##### `Vordering` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Vordering.Id` — Verwijderd

##### `Vorderingscomponent` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Vorderingscomponent.Id` — Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinjeugdbescherming-en-reclasseringmodel-jeugdbescherming"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Jeugdbescherming en reclassering/Model Jeugdbescherming

#### Classes

##### `Leefgebied` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `leefgebiedOmschrijving` — Gewijzigd
    - **naam**: `leefgebied` → `leefgebiedOmschrijving`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinschuldenschuldhulpverleningmodel-schuldhulpverlening"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Schulden/Schuldhulpverlening/Model Schuldhulpverlening

#### Classes

##### `Begeleiding` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `soort` — Gewijzigd
    - **stereotype**: _(leeg)_ → `enum`

##### `Begeleidingssoort` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `soort` — Gewijzigd
    - **stereotype**: _(leeg)_ → `enum`
    - **primitieve type**: `BegeleidingsoortEnum` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Schulden/Schuldhulpverlening/Model Schuldhulpverlening::EnumBegeleidingssoort`

##### `Oplossing` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `soort` — Gewijzigd
    - **stereotype**: _(leeg)_ → `enum`

##### `Oplossingssoort` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `soort` — Gewijzigd
    - **stereotype**: _(leeg)_ → `enum`
    - **primitieve type**: `SchuldregelingsoortEnum` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Schulden/Schuldhulpverlening/Model Schuldhulpverlening::EnumSchuldensoort`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinschuldenvroegsignaleringmodel-vroegsignalering"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Schulden/Vroegsignalering/Model Vroegsignalering

#### Enumeraties

##### `EnumContactsoort` — 🟡 Gewijzigd

**Literals:**

- 🟢 `Administratief` — Toegevoegd
- 🟢 `Afspraak op locatie` — Toegevoegd
- 🔴 `Overige` — Verwijderd

##### `EnumEindresultaat` — 🟡 Gewijzigd

**Literals:**

- 🟢 `Definitief geen contact kunnen krijgen` — Toegevoegd
- 🟢 `Geen reactie na eerder contact` — Toegevoegd
- 🟢 `Inwoner heeft zelf al betaald/betalingsregeling getroffen` — Toegevoegd
- 🟢 `Inwoner hoeft geen hulp vanuit vroegsignalering` — Toegevoegd
- 🟢 `Inwoner is overleden` — Toegevoegd
- 🟢 `Niet opgepakt: andere reden` — Toegevoegd
- 🟢 `Niet opgepakt: herhaalde melding` — Toegevoegd
- 🟢 `Niet opgepakt: onterecht signaal` — Toegevoegd
- 🟢 `Persoon is geen inwoner (meer) in de gemeente` — Toegevoegd
- 🟢 `Vervolghulp en/of verwijzing financieel` — Toegevoegd
- 🟢 `Vervolghulp en/of verwijzing niet financieel` — Toegevoegd
- 🟢 `Verwijzing zonder contact` — Toegevoegd
- 🔴 `Geen contact (meer) kunnen krijgen` — Verwijderd
- 🔴 `Inwoner heeft betaald/betalingsregeling getroffen voor oppakken melding` — Verwijderd
- 🔴 `Inwoner heeft zelf betaald/betalingsregeling getroffen na oppakken melding` — Verwijderd
- 🔴 `Inwoner probeert het zelf op te lossen` — Verwijderd
- 🔴 `Inwoner wil geen hulp` — Verwijderd
- 🔴 `Niet opgepakt` — Verwijderd
- 🔴 `Niet opgepakt: BRP-uitsluiting` — Verwijderd
- 🔴 `Niet opgepakt: geen capaciteit` — Verwijderd
- 🔴 `Niet opgepakt: inwoner wil geen contact` — Verwijderd
- 🔴 `Verwijzing financieel` — Verwijderd
- 🔴 `Verwijzing niet-financieel` — Verwijderd
- 🔴 `Voorzien van informatie` — Verwijderd

##### `EnumSignaalstatus` — 🟡 Gewijzigd

**Literals:**

- 🟢 `Inwoner is overleden` — Toegevoegd
- 🟢 `Niet opgepakt: andere reden` — Toegevoegd
- 🟢 `Niet opgepakt: herhaalde melding` — Toegevoegd
- 🟢 `Niet opgepakt: onterecht signaal` — Toegevoegd
- 🟢 `Persoon is geen inwoner (meer) in de gemeente` — Toegevoegd
- 🔴 `Herhaalde melding` — Verwijderd
- 🔴 `Niet opgepakt` — Verwijderd
- 🔴 `Onterecht signaal` — Verwijderd
- 🔴 `Opgepakt` — Verwijderd
- 🔴 `Overleden` — Verwijderd
- 🔴 `Woont niet in gemeente` — Verwijderd
- 🔴 `Woont op een ander adres binnen gemeente` — Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiekmodel-sociaal-domein-generiek"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek

#### Classes

##### `Incident` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `locatie` — Gewijzigd
    - **primitieve type**: `Locatie` → `GM_Point`
- 🟡 `soort` — Gewijzigd
    - **primitieve type**: `Incidenttype` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Jeugdbescherming en reclassering/Model Jeugdbescherming::enum_Incidenttype`

##### `Relatiesoort` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟢 `Omschrijving` — Toegevoegd

##### `Sociale Groep` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `typering` — Gewijzigd
    - **primitieve type**: `Groep` → `Text`

##### `Sociale Relatie` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `typering` — Gewijzigd
    - **primitieve type**: `Relatie` → `text`

#### Associaties

- 🟡 Gewijzigd: `Client` «valt binnen» → `Doelgroep`
  - **src mult. start**: _(leeg)_ → `0`
  - **src mult. end**: _(leeg)_ → `*`
  - **dst mult. start**: _(leeg)_ → `0`
  - **dst mult. end**: _(leeg)_ → `*`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiekmodel-sociaal-domein-generiekinkomstendatatypes"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Inkomsten/Datatypes

#### Datatypes

##### `BrutoNettoInkomsten` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Bruto` — Verwijderd
- 🔴 `Netto` — Verwijderd

##### `CdSrtInkomstenverhouding` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `11 Loon of salaris ambtenaren in de zin van de Ambtenarenwet` — Verwijderd
- 🔴 `11 Loon of salaris ambtenaren in de zin van de Ambtenarenwet 1929` — Verwijderd
- 🔴 `12 Loon of salaris werknemers van gepremieerde, gesubsidieerde of gebudgetteerde instellingen, inclusief uitvoeringsorganen sociale zekerheden` — Verwijderd
- 🔴 `13 Loon of salaris directeuren van een nv/bv, wel verzekerd voor de werknemersverzekeringen` — Verwijderd
- 🔴 `14 Loon of salaris overige werknemers niet verzekerd voor de Wet Werk en inkomen naar Arbeidsvermogen (WIA) of WAO` — Verwijderd
- 🔴 `15 Loon of salaris niet onder te brengen onder 11 tot en met 14 of 17` — Verwijderd
- 🔴 `15 Loon of salaris niet onder te brengen onder 11, 13 of 17` — Verwijderd
- 🔴 `17 Loon of salaris directeuren van een nv/bv, niet verzekerd voor de werknemersverzekeringen` — Verwijderd
- 🔴 `18 Wachtgeld van een overheidsinstelling` — Verwijderd
- 🔴 `21 Overige pensioenen, lijfrenten, enz. (niet 23 (Oorlogs- en verzetspensioenen))` — Verwijderd
- 🔴 `22 Uitkering in het kader van de Algemene Ouderdomswet (AOW)` — Verwijderd
- 🔴 `23 Oorlogs- en verzetspensioenen` — Verwijderd
- 🔴 `24 Uitkering in het kader van de Algemene nabestaandenwet (ANW)` — Verwijderd
- 🔴 `31 Uitkering in het kader van de Ziektewet (ZW) en vrijwillige verzekering Ziektewet` — Verwijderd
- 🔴 `32 Uitkering in het kader van de Wet op de Arbeids-ongeschiktheidsverzekering (WAO) en particuliere verzekering ziekte, invaliditeit en ongeval` — Verwijderd
- 🔴 `33 Uitkering in het kader van de Nieuwe Werkloosheidswet (nWW)` — Verwijderd
- 🔴 `34 Uitkering in het kader van de Wet inkomensvoorziening oudere en gedeeltelijk arbeidsongeschikte werkloze werknemers (IOAW)` — Verwijderd
- 🔴 `35 Vervolguitkering in het kader van de Nieuwe Werkloosheidswet (nWW)` — Verwijderd
- 🔴 `36 Uitkering in het kader van de Wet arbeidsongeschiktheidsverzekering zelfstandigen (Waz)` — Verwijderd
- 🔴 `37 Wet arbeidsongeschiktheidsvoorziening jonggehandicapten (Wajong)` — Verwijderd
- 🔴 `37 Wet werk en ondersteuning jonggehandicapten (Wajong)` — Verwijderd
- 🔴 `38 Samenloop (gelijktijdig of volgtijdelijk) van uitkeringen van Wajong met Waz, WAO/IVA of WGA` — Verwijderd
- 🔴 `39 Uitkering in het kader van de Regeling inkomensvoorziening volledig arbeidsongeschikten (IVA)` — Verwijderd
- 🔴 `40 Uitkering in het kader van de Regeling werkhervatting gedeeltelijk arbeidsgeschikten WGA)` — Verwijderd
- 🔴 `42 Uitkering in het kader van bijstandsbesluit Zelfstandigen (Bbz)` — Verwijderd
- 🔴 `43 Uitkering in het kader van de Participatiewet` — Verwijderd
- 🔴 `43 Uitkering in het kader van de Participatiewet (voorheen WWB)` — Verwijderd
- 🔴 `44 Uitkering in het kader van de Wet Werk en Inkomen (WWIK)` — Verwijderd
- 🔴 `45 Uitkering in het kader van de Wet inkomensvoorziening oudere en gedeeltelijk arbeidsongeschikte gewezen zelfstandigen (IOAZ)` — Verwijderd
- 🔴 `46 Uitkering uit hoofde van de Toeslagenwet` — Verwijderd
- 🔴 `50 Uitkeringen in het kader van overige sociale verzekeringswetten, hieronder vallen tevens: Ongevallenwet 1921, Land- en tuinbouwongevallenwet 1922 en Zeeongevallenwet 1919 (niet 22 of 24 tot en met 45)` — Verwijderd
- 🔴 `50 Uitkeringen in het kader van overige sociale verzekeringswetten, hieronder vallen tevens: Ongevallenwet 1921, Land- en tuinbouwongevallenwet 1922 en Zeeongevallenwet 1919 (niet 22, 24 tot en met 45, 51 of 52)` — Verwijderd
- 🔴 `51 Uitkering in het kader van de Wet Investeren in Jongeren (WIJ)` — Verwijderd
- 🔴 `52 Uitkering in het kader van de wet Inkomensvoorziening Oudere Werklozen (IOW)` — Verwijderd
- 🔴 `53 Uitkering in het kader van de vitaliteitsregeling` — Verwijderd
- 🔴 `54 Opname levenslooptegoed door een werknemer die op 1 januari 61 jaar of ouder is` — Verwijderd
- 🔴 `55 Uitkering in het kader van de Algemene Pensioenwet Politieke Ambtsdragers (APPA)` — Verwijderd
- 🔴 `56 Ouderdomspensioen dat via de werkgever is opgebouwd` — Verwijderd
- 🔴 `56 Ouderdomspensioen dat via de werkgever is opgebouwd of ouderdomspensioen opgebouwd via een verplichte beroepspensioenregeling/ bedrijfstakpensioenregeling` — Verwijderd
- 🔴 `57 Nabestaandenpensioen dat via de werkgever is opgebouwd` — Verwijderd
- 🔴 `57 Nabestaandenpensioen dat via de werkgever is opgebouwd of nabestaandenpensioen opgebouwd via een verplichte beroepspensioenregeling/ bedrijfstakpensioenregeling` — Verwijderd
- 🔴 `58 Arbeidsongeschiktheidspensioen dat via de werkgever is opgebouwd` — Verwijderd
- 🔴 `58 Arbeidsongeschiktheidspensioen dat via de werkgever is opgebouwd of arbeidsongeschiktheidspensioen opgebouwd via een verplichte beroepspensioenregeling/ bedrijfstakpensioenregeling` — Verwijderd
- 🔴 `59 Lijfrenten die zijn afgesloten in het kader van een individuele of collectieve arbeidsovereenkomst` — Verwijderd
- 🔴 `60 Lijfrenten die niet zijn afgesloten in het kader van een individuele of collectieve arbeidsovereenkomst` — Verwijderd
- 🔴 `61 Aanvulling van de werkgever aan een werknemer op een uitkering werknemersverzekeringen, terwijl de dienstbetrekking is beëindigd` — Verwijderd
- 🔴 `62 Ontslagvergoeding / transitievergoeding` — Verwijderd
- 🔴 `63 Overige, niet hiervoor aangegeven, pensioenen of samenloop van meerdere pensioenen/lijfrenten of een betaling op grond van een afspraak na einde dienstbetrekking` — Verwijderd

##### `CdSzWet` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `(Tijdelijke Wet) Beperking Inkomensgevolgen Arbeidsongeschiktheidscriteria` — Verwijderd
- 🔴 `(voormalige) Algemene Arbeidsongeschiktheidswet` — Verwijderd
- 🔴 `(voormalige) Algemene Weduwen en Wezenwet` — Verwijderd
- 🔴 `(voormalige) Rijksgroepregeling Werkloze Werknemers` — Verwijderd
- 🔴 `Algemene bijstand (regeling)` — Verwijderd
- 🔴 `Algemene Bijstandswet` — Verwijderd
- 🔴 `Algemene Kinderbijslagwet` — Verwijderd
- 🔴 `Algemene Nabestaandenwet` — Verwijderd
- 🔴 `Algemene Ouderdomswet` — Verwijderd
- 🔴 `Algemene Wet Bijzondere Ziektekosten` — Verwijderd
- 🔴 `AOW-Overbruggingsregeling` — Verwijderd
- 🔴 `AOW-Overbruggingsregeling` — Verwijderd
- 🔴 `Besluit Bijstandverlening Zelfstandigen` — Verwijderd
- 🔴 `Besluit Bijstandverlening Zelfstandigen – Bedrijfskapitaal` — Verwijderd
- 🔴 `Besluit Bijstandverlening Zelfstandigen – Bijzondere Bijstand` — Verwijderd
- 🔴 `Besluit Bijstandverlening Zelfstandigen – Levensonderhoud` — Verwijderd
- 🔴 `Bijzondere Bijstand` — Verwijderd
- 🔴 `Coördinatiewet Sociale Verzekering` — Verwijderd
- 🔴 `Internationale wetten` — Verwijderd
- 🔴 `Koninklijk besluit en aanverwante regelingen` — Verwijderd
- 🔴 `Kopjesregeling` — Verwijderd
- 🔴 `Organisatiewet Sociale Verzekering` — Verwijderd
- 🔴 `Participatiewet Wajong` — Verwijderd
- 🔴 `pensioenwetten` — Verwijderd
- 🔴 `Regeling Inkomensvoorziening Volledig Arbeidsongeschikten` — Verwijderd
- 🔴 `Regeling Werkhervatting Gedeeltelijk Arbeidsgeschikten` — Verwijderd
- 🔴 `Remigratiewet` — Verwijderd
- 🔴 `Tijdelijke Regeling Inkomensgevolgen herbeoordeelde arbeidsongeschikten` — Verwijderd
- 🔴 `Toeslagenwet` — Verwijderd
- 🔴 `VUT-regeling` — Verwijderd
- 🔴 `Werkhervattingskas` — Verwijderd
- 🔴 `Werkloosheidswet` — Verwijderd
- 🔴 `Werkloosheidswet Faillissementen` — Verwijderd
- 🔴 `Wet Arbeid en Zorg` — Verwijderd
- 🔴 `Wet Arbeidsongeschiktheidsverzekering Zelfstandigen` — Verwijderd
- 🔴 `Wet Arbeidsongeschiktheidsvoorziening Jonggehandicapten (WAJONG)` — Verwijderd
- 🔴 `Wet Arbeidsongeschiktheidsvoorziening Militairen` — Verwijderd
- 🔴 `Wet Inkomensvoorziening Oudere en gedeeltelijk Arbeidsongeschikte gewezen Zelfstandigen` — Verwijderd
- 🔴 `Wet Inkomensvoorziening Oudere en gedeeltelijk Arbeidsongeschikte Werkloze Werknemers` — Verwijderd
- 🔴 `Wet Inkomensvoorziening Oudere Werklozen` — Verwijderd
- 🔴 `Wet Investeren in Jongeren` — Verwijderd
- 🔴 `Wet Maatschappelijke Ondersteuning` — Verwijderd
- 🔴 `Wet op de (RE)integratie Arbeidsgehandicapten` — Verwijderd
- 🔴 `Wet op de Arbeidsongeschiktheidsverzekering` — Verwijderd
- 🔴 `Wet Sociale Werkvooriening` — Verwijderd
- 🔴 `Wet Voorzieningen Gehandicapten` — Verwijderd
- 🔴 `Wet werk en arbeidsondersteuning jonggehandicapten (Wet Wajong)` — Verwijderd
- 🔴 `Wet Werk en Arbeidsondersteuning Jonggehandicapten (Wet Wajong)` — Verwijderd
- 🔴 `Wet Werk en Bijstand` — Verwijderd
- 🔴 `Wet Werk en Inkomen Kunstenaars` — Verwijderd
- 🔴 `Wet Werk en Inkomen naar Arbeidsvermogen` — Verwijderd
- 🔴 `Ziekenfondswet` — Verwijderd
- 🔴 `Ziektewet` — Verwijderd
- 🔴 `Zorgverzekeringswet` — Verwijderd

##### `CdUitkeringsperiode` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `2 weken` — Verwijderd
- 🔴 `4 weken (13 maanden)` — Verwijderd
- 🔴 `5 weken` — Verwijderd
- 🔴 `dag` — Verwijderd
- 🔴 `eenmalig` — Verwijderd
- 🔴 `jaar` — Verwijderd
- 🔴 `kwartaal` — Verwijderd
- 🔴 `maand` — Verwijderd
- 🔴 `niet van toepassing` — Verwijderd
- 🔴 `week` — Verwijderd

##### `CodeSoortVrijlating` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Inkomstenvrijlating 12,5% - Art. 31 lid 2r` — Verwijderd
- 🔴 `Inkomstenvrijlating 15,0% - Art. 31 lid 2y` — Verwijderd
- 🔴 `Inkomstenvrijlating 25,0% - Art. 31 lid 2n` — Verwijderd

##### `Inkomstencomponenttype` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Alimentatie` — Verwijderd
- 🔴 `Ander inkomen` — Verwijderd
- 🔴 `Betaald werk` — Verwijderd
- 🔴 `Eigen bedrijf` — Verwijderd
- 🔴 `Heffingskorting` — Verwijderd
- 🔴 `Hobby` — Verwijderd
- 🔴 `Inkomstenvermindering` — Verwijderd
- 🔴 `Pensioen` — Verwijderd
- 🔴 `Stage` — Verwijderd
- 🔴 `Studiefinanciering` — Verwijderd
- 🔴 `Uitkering` — Verwijderd
- 🔴 `Vergoeding` — Verwijderd

##### `InkomstensoortAlimentatie` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Alimentatie ex-echtgenote/echtgenootg (geindexeerd)` — Verwijderd
- 🔴 `Alimentatie ex-echtgenote/echtgenootg (niet geindexeerd)` — Verwijderd
- 🔴 `Alimentatie kinderen (geindexeerd)` — Verwijderd
- 🔴 `Alimentatie kinderen (niet geindexeerd)` — Verwijderd

##### `InkomstensoortBetaaldWerk` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Betaald werk` — Verwijderd
- 🔴 `Zelfstandige / ZZP` — Verwijderd

##### `InkomstensoortPensioen` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Bedrijfspensioen` — Verwijderd
- 🔴 `Buitenlands pensioen` — Verwijderd
- 🔴 `Invaliditeitspensioen` — Verwijderd
- 🔴 `Nabestaandepensioen (weduwe/weduwnaar)` — Verwijderd
- 🔴 `Nabestaandepensioen (wezen)` — Verwijderd
- 🔴 `Pensioen ivm oorlog` — Verwijderd

##### `InkomstensoortStudiefinanciering` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `WSF` — Verwijderd
- 🔴 `WTOS` — Verwijderd

##### `JsonRuledGroupType` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `allOf` — Verwijderd
- 🔴 `anyOf` — Verwijderd
- 🔴 `oneOf` — Verwijderd

##### `Onderhoudsplichttype` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Kind` — Verwijderd
- 🔴 `Partner` — Verwijderd

##### `SoortContract` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `0-uren contract` — Verwijderd
- 🔴 `Op oproepbasis` — Verwijderd
- 🔴 `Uitzendbureau` — Verwijderd
- 🔴 `Vast contract` — Verwijderd
- 🔴 `Voor bepaalde tijd` — Verwijderd

#### Enumeraties

##### `BrutoNettoInkomsten` — 🟢 Toegevoegd

**Literals:**

- 🟢 `Bruto` — Toegevoegd
- 🟢 `Netto` — Toegevoegd

##### `CdSrtInkomstenverhouding` — 🟢 Toegevoegd

**Literals:**

- 🟢 `11 Loon of salaris ambtenaren in de zin van de Ambtenarenwet` — Toegevoegd
- 🟢 `11 Loon of salaris ambtenaren in de zin van de Ambtenarenwet 1929` — Toegevoegd
- 🟢 `12 Loon of salaris werknemers van gepremieerde, gesubsidieerde of gebudgetteerde instellingen, inclusief uitvoeringsorganen sociale zekerheden` — Toegevoegd
- 🟢 `13 Loon of salaris directeuren van een nv/bv, wel verzekerd voor de werknemersverzekeringen` — Toegevoegd
- 🟢 `14 Loon of salaris overige werknemers niet verzekerd voor de Wet Werk en inkomen naar Arbeidsvermogen (WIA) of WAO` — Toegevoegd
- 🟢 `15 Loon of salaris niet onder te brengen onder 11 tot en met 14 of 17` — Toegevoegd
- 🟢 `15 Loon of salaris niet onder te brengen onder 11, 13 of 17` — Toegevoegd
- 🟢 `17 Loon of salaris directeuren van een nv/bv, niet verzekerd voor de werknemersverzekeringen` — Toegevoegd
- 🟢 `18 Wachtgeld van een overheidsinstelling` — Toegevoegd
- 🟢 `21 Overige pensioenen, lijfrenten, enz. (niet 23 (Oorlogs- en verzetspensioenen))` — Toegevoegd
- 🟢 `22 Uitkering in het kader van de Algemene Ouderdomswet (AOW)` — Toegevoegd
- 🟢 `23 Oorlogs- en verzetspensioenen` — Toegevoegd
- 🟢 `24 Uitkering in het kader van de Algemene nabestaandenwet (ANW)` — Toegevoegd
- 🟢 `31 Uitkering in het kader van de Ziektewet (ZW) en vrijwillige verzekering Ziektewet` — Toegevoegd
- 🟢 `32 Uitkering in het kader van de Wet op de Arbeids-ongeschiktheidsverzekering (WAO) en particuliere verzekering ziekte, invaliditeit en ongeval` — Toegevoegd
- 🟢 `33 Uitkering in het kader van de Nieuwe Werkloosheidswet (nWW)` — Toegevoegd
- 🟢 `34 Uitkering in het kader van de Wet inkomensvoorziening oudere en gedeeltelijk arbeidsongeschikte werkloze werknemers (IOAW)` — Toegevoegd
- 🟢 `35 Vervolguitkering in het kader van de Nieuwe Werkloosheidswet (nWW)` — Toegevoegd
- 🟢 `36 Uitkering in het kader van de Wet arbeidsongeschiktheidsverzekering zelfstandigen (Waz)` — Toegevoegd
- 🟢 `37 Wet arbeidsongeschiktheidsvoorziening jonggehandicapten (Wajong)` — Toegevoegd
- 🟢 `37 Wet werk en ondersteuning jonggehandicapten (Wajong)` — Toegevoegd
- 🟢 `38 Samenloop (gelijktijdig of volgtijdelijk) van uitkeringen van Wajong met Waz, WAO/IVA of WGA` — Toegevoegd
- 🟢 `39 Uitkering in het kader van de Regeling inkomensvoorziening volledig arbeidsongeschikten (IVA)` — Toegevoegd
- 🟢 `40 Uitkering in het kader van de Regeling werkhervatting gedeeltelijk arbeidsgeschikten WGA)` — Toegevoegd
- 🟢 `42 Uitkering in het kader van bijstandsbesluit Zelfstandigen (Bbz)` — Toegevoegd
- 🟢 `43 Uitkering in het kader van de Participatiewet` — Toegevoegd
- 🟢 `43 Uitkering in het kader van de Participatiewet (voorheen WWB)` — Toegevoegd
- 🟢 `44 Uitkering in het kader van de Wet Werk en Inkomen (WWIK)` — Toegevoegd
- 🟢 `45 Uitkering in het kader van de Wet inkomensvoorziening oudere en gedeeltelijk arbeidsongeschikte gewezen zelfstandigen (IOAZ)` — Toegevoegd
- 🟢 `46 Uitkering uit hoofde van de Toeslagenwet` — Toegevoegd
- 🟢 `50 Uitkeringen in het kader van overige sociale verzekeringswetten, hieronder vallen tevens: Ongevallenwet 1921, Land- en tuinbouwongevallenwet 1922 en Zeeongevallenwet 1919 (niet 22 of 24 tot en met 45)` — Toegevoegd
- 🟢 `50 Uitkeringen in het kader van overige sociale verzekeringswetten, hieronder vallen tevens: Ongevallenwet 1921, Land- en tuinbouwongevallenwet 1922 en Zeeongevallenwet 1919 (niet 22, 24 tot en met 45, 51 of 52)` — Toegevoegd
- 🟢 `51 Uitkering in het kader van de Wet Investeren in Jongeren (WIJ)` — Toegevoegd
- 🟢 `52 Uitkering in het kader van de wet Inkomensvoorziening Oudere Werklozen (IOW)` — Toegevoegd
- 🟢 `53 Uitkering in het kader van de vitaliteitsregeling` — Toegevoegd
- 🟢 `54 Opname levenslooptegoed door een werknemer die op 1 januari 61 jaar of ouder is` — Toegevoegd
- 🟢 `55 Uitkering in het kader van de Algemene Pensioenwet Politieke Ambtsdragers (APPA)` — Toegevoegd
- 🟢 `56 Ouderdomspensioen dat via de werkgever is opgebouwd` — Toegevoegd
- 🟢 `56 Ouderdomspensioen dat via de werkgever is opgebouwd of ouderdomspensioen opgebouwd via een verplichte beroepspensioenregeling/ bedrijfstakpensioenregeling` — Toegevoegd
- 🟢 `57 Nabestaandenpensioen dat via de werkgever is opgebouwd` — Toegevoegd
- 🟢 `57 Nabestaandenpensioen dat via de werkgever is opgebouwd of nabestaandenpensioen opgebouwd via een verplichte beroepspensioenregeling/ bedrijfstakpensioenregeling` — Toegevoegd
- 🟢 `58 Arbeidsongeschiktheidspensioen dat via de werkgever is opgebouwd` — Toegevoegd
- 🟢 `58 Arbeidsongeschiktheidspensioen dat via de werkgever is opgebouwd of arbeidsongeschiktheidspensioen opgebouwd via een verplichte beroepspensioenregeling/ bedrijfstakpensioenregeling` — Toegevoegd
- 🟢 `59 Lijfrenten die zijn afgesloten in het kader van een individuele of collectieve arbeidsovereenkomst` — Toegevoegd
- 🟢 `60 Lijfrenten die niet zijn afgesloten in het kader van een individuele of collectieve arbeidsovereenkomst` — Toegevoegd
- 🟢 `61 Aanvulling van de werkgever aan een werknemer op een uitkering werknemersverzekeringen, terwijl de dienstbetrekking is beëindigd` — Toegevoegd
- 🟢 `62 Ontslagvergoeding / transitievergoeding` — Toegevoegd
- 🟢 `63 Overige, niet hiervoor aangegeven, pensioenen of samenloop van meerdere pensioenen/lijfrenten of een betaling op grond van een afspraak na einde dienstbetrekking` — Toegevoegd

##### `CdSzWet` — 🟢 Toegevoegd

**Literals:**

- 🟢 `(Tijdelijke Wet) Beperking Inkomensgevolgen Arbeidsongeschiktheidscriteria` — Toegevoegd
- 🟢 `(voormalige) Algemene Arbeidsongeschiktheidswet` — Toegevoegd
- 🟢 `(voormalige) Algemene Weduwen en Wezenwet` — Toegevoegd
- 🟢 `(voormalige) Rijksgroepregeling Werkloze Werknemers` — Toegevoegd
- 🟢 `AOW-Overbruggingsregeling` — Toegevoegd
- 🟢 `Algemene Bijstandswet` — Toegevoegd
- 🟢 `Algemene Kinderbijslagwet` — Toegevoegd
- 🟢 `Algemene Nabestaandenwet` — Toegevoegd
- 🟢 `Algemene Ouderdomswet` — Toegevoegd
- 🟢 `Algemene Wet Bijzondere Ziektekosten` — Toegevoegd
- 🟢 `Algemene bijstand (regeling)` — Toegevoegd
- 🟢 `Besluit Bijstandverlening Zelfstandigen` — Toegevoegd
- 🟢 `Besluit Bijstandverlening Zelfstandigen – Bedrijfskapitaal` — Toegevoegd
- 🟢 `Besluit Bijstandverlening Zelfstandigen – Bijzondere Bijstand` — Toegevoegd
- 🟢 `Besluit Bijstandverlening Zelfstandigen – Levensonderhoud` — Toegevoegd
- 🟢 `Bijzondere Bijstand` — Toegevoegd
- 🟢 `Coördinatiewet Sociale Verzekering` — Toegevoegd
- 🟢 `Internationale wetten` — Toegevoegd
- 🟢 `Koninklijk besluit en aanverwante regelingen` — Toegevoegd
- 🟢 `Kopjesregeling` — Toegevoegd
- 🟢 `Organisatiewet Sociale Verzekering` — Toegevoegd
- 🟢 `Participatiewet Wajong` — Toegevoegd
- 🟢 `Regeling Inkomensvoorziening Volledig Arbeidsongeschikten` — Toegevoegd
- 🟢 `Regeling Werkhervatting Gedeeltelijk Arbeidsgeschikten` — Toegevoegd
- 🟢 `Remigratiewet` — Toegevoegd
- 🟢 `Tijdelijke Regeling Inkomensgevolgen herbeoordeelde arbeidsongeschikten` — Toegevoegd
- 🟢 `Toeslagenwet` — Toegevoegd
- 🟢 `VUT-regeling` — Toegevoegd
- 🟢 `Werkhervattingskas` — Toegevoegd
- 🟢 `Werkloosheidswet` — Toegevoegd
- 🟢 `Werkloosheidswet Faillissementen` — Toegevoegd
- 🟢 `Wet Arbeid en Zorg` — Toegevoegd
- 🟢 `Wet Arbeidsongeschiktheidsverzekering Zelfstandigen` — Toegevoegd
- 🟢 `Wet Arbeidsongeschiktheidsvoorziening Jonggehandicapten (WAJONG)` — Toegevoegd
- 🟢 `Wet Arbeidsongeschiktheidsvoorziening Militairen` — Toegevoegd
- 🟢 `Wet Inkomensvoorziening Oudere Werklozen` — Toegevoegd
- 🟢 `Wet Inkomensvoorziening Oudere en gedeeltelijk Arbeidsongeschikte Werkloze Werknemers` — Toegevoegd
- 🟢 `Wet Inkomensvoorziening Oudere en gedeeltelijk Arbeidsongeschikte gewezen Zelfstandigen` — Toegevoegd
- 🟢 `Wet Investeren in Jongeren` — Toegevoegd
- 🟢 `Wet Maatschappelijke Ondersteuning` — Toegevoegd
- 🟢 `Wet Sociale Werkvooriening` — Toegevoegd
- 🟢 `Wet Voorzieningen Gehandicapten` — Toegevoegd
- 🟢 `Wet Werk en Arbeidsondersteuning Jonggehandicapten (Wet Wajong)` — Toegevoegd
- 🟢 `Wet Werk en Bijstand` — Toegevoegd
- 🟢 `Wet Werk en Inkomen Kunstenaars` — Toegevoegd
- 🟢 `Wet Werk en Inkomen naar Arbeidsvermogen` — Toegevoegd
- 🟢 `Wet op de (RE)integratie Arbeidsgehandicapten` — Toegevoegd
- 🟢 `Wet op de Arbeidsongeschiktheidsverzekering` — Toegevoegd
- 🟢 `Wet werk en arbeidsondersteuning jonggehandicapten (Wet Wajong)` — Toegevoegd
- 🟢 `Ziekenfondswet` — Toegevoegd
- 🟢 `Ziektewet` — Toegevoegd
- 🟢 `Zorgverzekeringswet` — Toegevoegd
- 🟢 `pensioenwetten` — Toegevoegd

##### `CdUitkeringsperiode` — 🟢 Toegevoegd

**Literals:**

- 🟢 `2 weken` — Toegevoegd
- 🟢 `4 weken (13 maanden)` — Toegevoegd
- 🟢 `5 weken` — Toegevoegd
- 🟢 `dag` — Toegevoegd
- 🟢 `eenmalig` — Toegevoegd
- 🟢 `jaar` — Toegevoegd
- 🟢 `kwartaal` — Toegevoegd
- 🟢 `maand` — Toegevoegd
- 🟢 `niet van toepassing` — Toegevoegd
- 🟢 `week` — Toegevoegd

##### `CodeSoortVrijlating` — 🟢 Toegevoegd

**Literals:**

- 🟢 `Inkomstenvrijlating 12,5% - Art. 31 lid 2r` — Toegevoegd
- 🟢 `Inkomstenvrijlating 15,0% - Art. 31 lid 2y` — Toegevoegd
- 🟢 `Inkomstenvrijlating 25,0% - Art. 31 lid 2n` — Toegevoegd

##### `Inkomstencomponenttype` — 🟢 Toegevoegd

**Literals:**

- 🟢 `Alimentatie` — Toegevoegd
- 🟢 `Ander inkomen` — Toegevoegd
- 🟢 `Betaald werk` — Toegevoegd
- 🟢 `Eigen bedrijf` — Toegevoegd
- 🟢 `Heffingskorting` — Toegevoegd
- 🟢 `Hobby` — Toegevoegd
- 🟢 `Inkomstenvermindering` — Toegevoegd
- 🟢 `Pensioen` — Toegevoegd
- 🟢 `Stage` — Toegevoegd
- 🟢 `Studiefinanciering` — Toegevoegd
- 🟢 `Uitkering` — Toegevoegd
- 🟢 `Vergoeding` — Toegevoegd

##### `InkomstensoortAlimentatie` — 🟢 Toegevoegd

**Literals:**

- 🟢 `Alimentatie ex-echtgenote/echtgenootg (geindexeerd)` — Toegevoegd
- 🟢 `Alimentatie ex-echtgenote/echtgenootg (niet geindexeerd)` — Toegevoegd
- 🟢 `Alimentatie kinderen (geindexeerd)` — Toegevoegd
- 🟢 `Alimentatie kinderen (niet geindexeerd)` — Toegevoegd

##### `InkomstensoortBetaaldWerk` — 🟢 Toegevoegd

**Literals:**

- 🟢 `Betaald werk` — Toegevoegd
- 🟢 `Zelfstandige / ZZP` — Toegevoegd

##### `InkomstensoortPensioen` — 🟢 Toegevoegd

**Literals:**

- 🟢 `Bedrijfspensioen` — Toegevoegd
- 🟢 `Buitenlands pensioen` — Toegevoegd
- 🟢 `Invaliditeitspensioen` — Toegevoegd
- 🟢 `Nabestaandepensioen (weduwe/weduwnaar)` — Toegevoegd
- 🟢 `Nabestaandepensioen (wezen)` — Toegevoegd
- 🟢 `Pensioen ivm oorlog` — Toegevoegd

##### `InkomstensoortStudiefinanciering` — 🟢 Toegevoegd

**Literals:**

- 🟢 `WSF` — Toegevoegd
- 🟢 `WTOS` — Toegevoegd

##### `JsonRuledGroupType` — 🟢 Toegevoegd

**Literals:**

- 🟢 `allOf` — Toegevoegd
- 🟢 `anyOf` — Toegevoegd
- 🟢 `oneOf` — Toegevoegd

##### `Onderhoudsplichttype` — 🟢 Toegevoegd

**Literals:**

- 🟢 `Kind` — Toegevoegd
- 🟢 `Partner` — Toegevoegd

##### `SoortContract` — 🟢 Toegevoegd

**Literals:**

- 🟢 `0-uren contract` — Toegevoegd
- 🟢 `Op oproepbasis` — Toegevoegd
- 🟢 `Uitzendbureau` — Toegevoegd
- 🟢 `Vast contract` — Toegevoegd
- 🟢 `Voor bepaalde tijd` — Toegevoegd

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiekmodel-sociaal-domein-generiekinkomstenmodel-inkomsten"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Inkomsten/Model Inkomsten

#### Classes

##### `Alimentatie` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Alimentatie.Id` — Verwijderd
- 🟡 `Bedrag aan andere rekeningen` — Gewijzigd
    - **primitieve type**: `Geldbedrag` → `Bedrag`
- 🟡 `Bedrag in convenant` — Gewijzigd
    - **primitieve type**: `StdIndJN` → `Boolean`
- 🟡 `BijdrageExPartnerAndereRekeningen` — Gewijzigd
    - **naam**: `Bijdrage ex partner voor andere rekeningen` → `BijdrageExPartnerAndereRekeningen`
    - **primitieve type**: `StdIndJN` → `Boolean`
- 🟡 `Inkomstensoort alimentatie` — Gewijzigd
    - **primitieve type**: `InkomstensoortAlimentatie` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Inkomsten/Datatypes::InkomstensoortAlimentatie`
- 🟡 `Juiste bedrag betaald door ex partner` — Gewijzigd
    - **primitieve type**: `StdIndJN` → `Boolean`
- 🟡 `LBIO ingeschakeld` — Gewijzigd
    - **primitieve type**: `StdIndJN` → `Boolean`

##### `Ander inkomen` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `AnderInkomen.Id` — Verwijderd

##### `Betaald werk` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `BetaaldWerk.Id` — Verwijderd
- 🟡 `Arbeidscontract` — Gewijzigd
    - **primitieve type**: `StdIndJN` → `Boolean`
- 🟡 `Inkomsten uit IKB-regeling` — Gewijzigd
    - **primitieve type**: `StdIndJN` → `Boolean`
- 🟡 `Inkomstensoort betaald werk` — Gewijzigd
    - **primitieve type**: `InkomstensoortBetaaldWerk` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Inkomsten/Datatypes::InkomstensoortBetaaldWerk`
- 🟡 `Loondienst` — Gewijzigd
    - **primitieve type**: `StdIndJN` → `Boolean`
- 🟡 `Periodiciteit uitbetaling loon` — Gewijzigd
    - **primitieve type**: `CdUitkeringsperiode` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Inkomsten/Datatypes::CdUitkeringsperiode`
- 🟡 `Soort contract` — Gewijzigd
    - **primitieve type**: `SoortContract` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Inkomsten/Datatypes::SoortContract`

##### `Dertiende maand - eindejaarsuitkering` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `DertiendeMaandEindejaarsuitkering.Id` — Verwijderd

##### `Draagkracht` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Draagkracht.Id` — Verwijderd

##### `Draagkrachtregime` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Draagkrachtregime.Id` — Verwijderd
- 🟡 `Initiele draagkracht` — Gewijzigd
    - **primitieve type**: `Geldbedrag` → `Bedrag`
- 🟡 `Resterende draagkracht` — Gewijzigd
    - **primitieve type**: `Geldbedrag` → `Bedrag`

##### `Eigen bedrijf` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `EigenBedrijf.Id` — Verwijderd
- 🟡 `Ingeschreven bij KvK` — Gewijzigd
    - **primitieve type**: `StdIndJN` → `Boolean`
- 🟡 `Recht op zelfstandigenaftrek` — Gewijzigd
    - **primitieve type**: `StdIndJN` → `Boolean`
- 🟡 `Toestemming gemeente parttime ondernemen` — Gewijzigd
    - **primitieve type**: `StdIndJN` → `Boolean`

##### `Heffingskorting` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Heffingskorting.Id` — Verwijderd
- 🟡 `Algemene heffingskorting` — Gewijzigd
    - **primitieve type**: `StdIndJN` → `Boolean`
- 🟡 `Inkomensafhankelijke combinatiekorting` — Gewijzigd
    - **primitieve type**: `StdIndJN` → `Boolean`

##### `Hobby` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Hobby.Id` — Verwijderd

##### `Inkomstencomponent` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Inkomstencomponent.Id` — Verwijderd
- 🟡 `Bijgevoegd bewijs` — Gewijzigd
    - **primitieve type**: `StdIndJN` → `Boolean`
- 🟡 `Bruto-Netto` — Gewijzigd
    - **primitieve type**: `BrutoNettoInkomsten` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Inkomsten/Datatypes::BrutoNettoInkomsten`
- 🟡 `Inkomsten` — Gewijzigd
    - **primitieve type**: `Geldbedrag` → `Bedrag`
- 🟡 `Inkomstencomponenttype` — Gewijzigd
    - **primitieve type**: `Inkomstencomponenttype` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Inkomsten/Datatypes::Inkomstencomponenttype`

##### `Inkomstenverhouding` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Inkomstenverhouding.Id` — Verwijderd
- 🟡 `Categorie Inkomsten` — Gewijzigd
    - **primitieve type**: `CdSrtInkomstenverhouding` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Inkomsten/Datatypes::CdSrtInkomstenverhouding`

##### `Inkomstenvermindering` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Inkomstenvermindering.Id` — Verwijderd

##### `Kostencomponent` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Kostencomponent.Id` — Verwijderd
- 🟡 `Bedrag` — Gewijzigd
    - **primitieve type**: `Geldbedrag` → `Bedrag`

##### `Loonbeslag` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Loonbeslag.Id` — Verwijderd

##### `Maaltijdvergoeding` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Maaltijdvergoeding.Id` — Verwijderd

##### `Onderhoudsplicht` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Onderhoudsplicht.Id` — Verwijderd
- 🟡 `Bijdrage` — Gewijzigd
    - **primitieve type**: `Geldbedrag` → `Bedrag`
- 🟡 `Onderhoudsplichttype` — Gewijzigd
    - **primitieve type**: `Onderhoudsplichttype` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Inkomsten/Datatypes::Onderhoudsplichttype`

##### `Onderhoudsverhouding` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Onderhoudsverhouding.Id` — Verwijderd

##### `Onkostenvergoeding` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Onkostenvergoeding.Id` — Verwijderd

##### `Pensioen` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Pensioen.Id` — Verwijderd
- 🟡 `Beslag op pensioen` — Gewijzigd
    - **primitieve type**: `StdIndJN` → `Boolean`
- 🟡 `Inkomstensoort pensioen` — Gewijzigd
    - **primitieve type**: `InkomstensoortPensioen` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Inkomsten/Datatypes::InkomstensoortPensioen`
- 🟡 `Loonheffingskorting` — Gewijzigd
    - **primitieve type**: `StdIndJN` → `Boolean`
- 🟡 `Periodiciteit uitbetaling pensioen` — Gewijzigd
    - **primitieve type**: `CdUitkeringsperiode` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Inkomsten/Datatypes::CdUitkeringsperiode`

##### `Primair inkomstencomponent` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `PrimairInkomstencomponent.Id` — Verwijderd

##### `Reiskostenvergoeding` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Reiskostenvergoeding.Id` — Verwijderd

##### `Secundair inkomstencomponent` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `SecundairInkomstencomponent.Id` — Verwijderd

##### `Stage` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Stage.Id` — Verwijderd
- 🟡 `Maaltijdvergoeding` — Gewijzigd
    - **primitieve type**: `StdIndJN` → `Boolean`
- 🟡 `Onkostenvergoeding` — Gewijzigd
    - **primitieve type**: `StdIndJN` → `Boolean`
- 🟡 `Periodiciteit uitbetaling loon` — Gewijzigd
    - **primitieve type**: `CdUitkeringsperiode` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Inkomsten/Datatypes::CdUitkeringsperiode`
- 🟡 `Reiskostenvergoeding` — Gewijzigd
    - **primitieve type**: `StdIndJN` → `Boolean`
- 🟡 `Vergoeding in natura` — Gewijzigd
    - **primitieve type**: `StdIndJN` → `Boolean`

##### `Studiefinanciering` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Studiefinanciering.Id` — Verwijderd
- 🟡 `Daadwerkelijk Genoten` — Gewijzigd
    - **primitieve type**: `StdIndJN` → `Boolean`
- 🟡 `Inkomstensoort studiefinanciering` — Gewijzigd
    - **primitieve type**: `InkomstensoortStudiefinanciering` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Inkomsten/Datatypes::InkomstensoortStudiefinanciering`

##### `Uitkering` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Uitkering.Id` — Verwijderd
- 🟡 `Beslag op uitkering` — Gewijzigd
    - **primitieve type**: `StdIndJN` → `Boolean`
- 🟡 `Inkomstensoort uitkering` — Gewijzigd
    - **primitieve type**: `CdSzWet` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Inkomsten/Datatypes::CdSzWet`
- 🟡 `Loonheffingskorting` — Gewijzigd
    - **primitieve type**: `StdIndJN` → `Boolean`
- 🟡 `Periodiciteit uitbetaling uitkering` — Gewijzigd
    - **primitieve type**: `CdUitkeringsperiode` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Inkomsten/Datatypes::CdUitkeringsperiode`
- 🟡 `Toeslag op uitkering` — Gewijzigd
    - **primitieve type**: `StdIndJN` → `Boolean`
- 🟡 `Uitkering verlaagd door boete` — Gewijzigd
    - **primitieve type**: `StdIndJN` → `Boolean`
- 🟡 `Uitkering verlaagd door maatregel` — Gewijzigd
    - **primitieve type**: `StdIndJN` → `Boolean`
- 🟡 `Vakantiegeld jaarlijks ontvangen` — Gewijzigd
    - **primitieve type**: `StdIndJN` → `Boolean`

##### `Vakantiegeld` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Vakantiegeld.Id` — Verwijderd

##### `Vergoeding` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Vergoeding.Id` — Verwijderd

##### `Vergoeding in natura` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `VergoedingInNatura.Id` — Verwijderd

##### `Verlaging door boete` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `VerlagingDoorBoete.Id` — Verwijderd

##### `Verlaging door maatregel` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `VerlagingDoorMaatregel.Id` — Verwijderd

##### `Vrijlating inkomsten` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `VrijlatingInkomsten.Id` — Verwijderd
- 🟡 `Doelgroep` — Gewijzigd
    - **primitieve type**: `JsonRuledGroupType` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Inkomsten/Datatypes::JsonRuledGroupType`
- 🟡 `Medisch` — Gewijzigd
    - **primitieve type**: `StdIndJN` → `Boolean`
- 🟡 `Soort vrijlating` — Gewijzigd
    - **primitieve type**: `CodeSoortVrijlating` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Inkomsten/Datatypes::CodeSoortVrijlating`
- 🟡 `Vrijgelaten bedrag` — Gewijzigd
    - **primitieve type**: `Geldbedrag` → `Bedrag`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiekmodel-sociaal-domein-generiekvermogendatatypes"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Vermogen/Datatypes

#### Datatypes

##### `AdresType` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Adres buitenland` — Verwijderd
- 🔴 `Adres Nederland` — Verwijderd

##### `CdSrtVermogenscomponent` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Aandeel onverdeelde boedel` — Verwijderd
- 🔴 `Aanspraak op erfenis binnen zes maanden` — Verwijderd
- 🔴 `Antiek/sieraden` — Verwijderd
- 🔴 `Bank-/Girorekening` — Verwijderd
- 🔴 `Beleggingsproduct (Aandeel, Lease, Effect, Obligatie, e.d.)` — Verwijderd
- 🔴 `Caravans` — Verwijderd
- 🔴 `Contanten` — Verwijderd
- 🔴 `Digitale valuta (cryptomunten)` — Verwijderd
- 🔴 `Eigen woning (huis/woonschip/woonwagen in eigendom)` — Verwijderd
- 🔴 `Hypotheek eigen woning` — Verwijderd
- 🔴 `Leningen aan derden` — Verwijderd
- 🔴 `Levensverzekering` — Verwijderd
- 🔴 `Levensverzekering/belegging gekoppeld aan hypotheek` — Verwijderd
- 🔴 `Levensverzekering/belegging niet gekoppeld aan hypotheek` — Verwijderd
- 🔴 `Motorvoertuigen` — Verwijderd
- 🔴 `Overig onroerend goed` — Verwijderd
- 🔴 `Overige bezittingen` — Verwijderd
- 🔴 `Schulden` — Verwijderd
- 🔴 `Schulden uitgezonderd studieschuld` — Verwijderd
- 🔴 `Studieschuld` — Verwijderd
- 🔴 `Waardepapieren` — Verwijderd

##### `CdSrtVoertuig` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Aanhangwagen` — Verwijderd
- 🔴 `Bedrijfsauto` — Verwijderd
- 🔴 `Bromfiets` — Verwijderd
- 🔴 `Driewielig motorrijtuig` — Verwijderd
- 🔴 `Motorfiets` — Verwijderd
- 🔴 `Personenauto` — Verwijderd

##### `CdSrtWaardeVermogenscomponent` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Banksaldo` — Verwijderd
- 🔴 `Beleggingsproductsaldo` — Verwijderd
- 🔴 `Cataloguswaarde` — Verwijderd
- 🔴 `Hypotheekschuld` — Verwijderd
- 🔴 `Marktwaarde` — Verwijderd
- 🔴 `WOZwaarde` — Verwijderd

#### Enumeraties

##### `AdresType` — 🟢 Toegevoegd

**Literals:**

- 🟢 `Adres Nederland` — Toegevoegd
- 🟢 `Adres buitenland` — Toegevoegd

##### `CdSrtVermogenscomponent` — 🟢 Toegevoegd

**Literals:**

- 🟢 `Aandeel onverdeelde boedel` — Toegevoegd
- 🟢 `Aanspraak op erfenis binnen zes maanden` — Toegevoegd
- 🟢 `Antiek/sieraden` — Toegevoegd
- 🟢 `Bank-/Girorekening` — Toegevoegd
- 🟢 `Beleggingsproduct (Aandeel, Lease, Effect, Obligatie, e.d.)` — Toegevoegd
- 🟢 `Caravans` — Toegevoegd
- 🟢 `Contanten` — Toegevoegd
- 🟢 `Digitale valuta (cryptomunten)` — Toegevoegd
- 🟢 `Eigen woning (huis/woonschip/woonwagen in eigendom)` — Toegevoegd
- 🟢 `Hypotheek eigen woning` — Toegevoegd
- 🟢 `Leningen aan derden` — Toegevoegd
- 🟢 `Levensverzekering` — Toegevoegd
- 🟢 `Levensverzekering/belegging gekoppeld aan hypotheek` — Toegevoegd
- 🟢 `Levensverzekering/belegging niet gekoppeld aan hypotheek` — Toegevoegd
- 🟢 `Motorvoertuigen` — Toegevoegd
- 🟢 `Overig onroerend goed` — Toegevoegd
- 🟢 `Overige bezittingen` — Toegevoegd
- 🟢 `Schulden` — Toegevoegd
- 🟢 `Schulden uitgezonderd studieschuld` — Toegevoegd
- 🟢 `Studieschuld` — Toegevoegd
- 🟢 `Waardepapieren` — Toegevoegd

##### `CdSrtVoertuig` — 🟢 Toegevoegd

**Literals:**

- 🟢 `Aanhangwagen` — Toegevoegd
- 🟢 `Bedrijfsauto` — Toegevoegd
- 🟢 `Bromfiets` — Toegevoegd
- 🟢 `Driewielig motorrijtuig` — Toegevoegd
- 🟢 `Motorfiets` — Toegevoegd
- 🟢 `Personenauto` — Toegevoegd

##### `CdSrtWaardeVermogenscomponent` — 🟢 Toegevoegd

**Literals:**

- 🟢 `Banksaldo` — Toegevoegd
- 🟢 `Beleggingsproductsaldo` — Toegevoegd
- 🟢 `Cataloguswaarde` — Toegevoegd
- 🟢 `Hypotheekschuld` — Toegevoegd
- 🟢 `Marktwaarde` — Toegevoegd
- 🟢 `WOZwaarde` — Toegevoegd

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiekmodel-sociaal-domein-generiekvermogenmodel-vermogen"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Vermogen/Model Vermogen

#### Classes

##### `Bankrekening` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `Bankrekening ID` — Verwijderd
- 🟡 `Voorkeur bankrekening` — Gewijzigd
    - **primitieve type**: `StdIndJN` → `Boolean`

##### `Hypotheek` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `Overwaarde` — Gewijzigd
    - **primitieve type**: `Geldbedrag` → `Bedrag`

##### `Motorvoertuig` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `Soort motorvoertuig` — Gewijzigd
    - **primitieve type**: `CdSrtVoertuig` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Vermogen/Datatypes::CdSrtVoertuig`

##### `Onroerend goed` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `Overwaarde` — Gewijzigd
    - **primitieve type**: `Geldbedrag` → `Bedrag`

##### `Vermogenscomponent` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `Code soort vermogenscomponent` — Gewijzigd
    - **primitieve type**: `CdSrtVermogenscomponent` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Vermogen/Datatypes::CdSrtVermogenscomponent`
- 🟡 `identificatie` — Gewijzigd
    - **naam**: `Vermogenscomponent ID` → `identificatie`
- 🟡 `Nog aan te spreken vermogen` — Gewijzigd
    - **primitieve type**: `Geldbedrag` → `Bedrag`
- 🟡 `Vrij te laten vermogen` — Gewijzigd
    - **primitieve type**: `Geldbedrag` → `Bedrag`

##### `Waardepeiling` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `Bijgevoegd bewijs` — Gewijzigd
    - **primitieve type**: `StdIndJN` → `Boolean`
- 🟡 `Waarde vermogenscomponent` — Gewijzigd
    - **primitieve type**: `Geldbedrag` → `Bedrag`
- 🟡 `WaardeSoort vermogenscomponent` — Gewijzigd
    - **primitieve type**: `CdSrtWaardeVermogenscomponent` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Vermogen/Datatypes::CdSrtWaardeVermogenscomponent`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinwerkmodel-werk"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Werk/Model Werk

#### Classes

##### `Arbeidsvermogen` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `CodeArbeidsvermogen` — Gewijzigd
    - **primitieve type**: `Code arbeidsvermogen` → `arbeidsvermogen`

##### `Bemiddelingsactiviteit` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `OmschrijvingSoortContactbemiddeling` — Gewijzigd
    - **primitieve type**: `Kanaal contactmoment` → `contactmoment`

##### `BeschikbaarVoorArbeid` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `DagBeschikbaarheid` — Gewijzigd
    - **primitieve type**: `Dag beschikbaarheid` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Werk/Model Werk::Dag beschikbaarheid`

##### `Flexibliteit` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `IndicatieBereidBuitenBeroepswens` — Gewijzigd
    - **naam**: `IndicatieBereidheidZoekenBuitenBeroepswens` → `IndicatieBereidBuitenBeroepswens`

##### `Mobiliteit` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `CodeVervoermiddel` — Gewijzigd
    - **primitieve type**: `Vervoersmogelijkheden` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Werk/Model Werk::Vervoermiddel`

##### `Ontheffing` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `MotivatieOntheffingsbesluit` — Gewijzigd
    - **primitieve type**: `document` → _(leeg)_
    - **type (class)**: _(leeg)_ → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RGBZPlus/Model RGBZ/Model Kern RGBZ::Document`
- 🟡 `OntheffenVerplichtingen` — Gewijzigd
    - **primitieve type**: `Ontheffingsverplichting` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Werk/Model Werk::Ontheffingsverplichting`
- 🟡 `Ontheffingsbesluit` — Gewijzigd
    - **primitieve type**: `document` → _(leeg)_
    - **type (class)**: _(leeg)_ → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RGBZPlus/Model RGBZ/Model Kern RGBZ::Document`
- 🟡 `SoortOntheffing` — Gewijzigd
    - **primitieve type**: `Soort ontheffing` → `ontheffing`

##### `Opleiding` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `CodeStatusOpleiding` — Gewijzigd
    - **primitieve type**: `StatusOpleiding` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Werk/Model Werk::CodeStatusOpleiding`
- 🟡 `CodeTijdsBeslagOpleiding` — Gewijzigd
    - **primitieve type**: `Code tijdsbeslag opleiding` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Werk/Model Werk::Code tijdsbeslag opleiding`
- 🟡 `Instituutnaam` — Gewijzigd
    - **primitieve type**: `short` → `Text`
- 🟡 `Opleidingstype` — Gewijzigd
    - **stereotype**: _(leeg)_ → `enum`
    - **primitieve type**: `Opleidingstype` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Werk/Model Werk::Opleidingsrichting`

##### `Opleidingsnaam` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `naamOpleiding` — Gewijzigd
    - **naam**: `Opleidingsnaam` → `naamOpleiding`

##### `OpleidingsnaamOngecodeerd` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `naamOpleidingOngecodeerd` — Gewijzigd
    - **naam**: `OpleidingsnaamOngecodeerd` → `naamOpleidingOngecodeerd`

##### `Opleidingsniveau` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `CodeOpleidingsniveauClient` — Gewijzigd
    - **primitieve type**: `Code opleidingsniveau cliënt` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Werk/Model Werk::Code opleidingsniveau cliënt`

##### `Rijbewijs /Certificaat` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `CodeSoortRijbewijs` — Gewijzigd
    - **primitieve type**: `ENUM()` → `AN12`
- 🟡 `NummerCertificaat` — Gewijzigd
    - **primitieve type**: `RegEx` → `varchar`

##### `Taalbeheersing` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `Taalcode` — Gewijzigd
    - **primitieve type**: `ìnt` → `varchar`

##### `Vaardigheidsvaststelling` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `datumLaatsteVaststelling` — Gewijzigd
    - **naam**: `Datum laatste vaststelling van vaardigheid` → `datumLaatsteVaststelling`
- 🟡 `Indicatie mate van vaardigheid` — Gewijzigd
    - **primitieve type**: `Indicatie mate van vaardigheid` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Werk/Model Werk::Taalvaardigheid`

##### `Voorkeur` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `SoortWerk` — Gewijzigd
    - **primitieve type**: `enum` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Werk/Model Werk::SoortWerk`

##### `Werkzaamheden anders dan in arbeidsverhouding` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `aantalUrenGemiddeldWeek` — Gewijzigd
    - **naam**: `Aantal uren werkzaamheden gemiddeld per week` → `aantalUrenGemiddeldWeek`
- 🟡 `PersoonOrganisatieWaarbij` — Gewijzigd
    - **naam**: `Naam persoon of organisatie bij wie of waar` → `PersoonOrganisatieWaarbij`

##### `ZelfredzaamheidScore` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `Domein van Zelfredzaamheid` — Gewijzigd
    - **primitieve type**: `Domein van zelfredzaamheid` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Werk/Model Werk::Domein van zelfredzaamheid`
- 🟡 `KenmerkBeoordelaar` — Gewijzigd
    - **primitieve type**: `Name` → `AN200`
- 🟡 `ZRM score` — Gewijzigd
    - **primitieve type**: `ZRM score` → `score`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel7-volksgezondheid-en-milieuafvalmodel-afval"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval

**Pakket-metadata gewijzigd:**

- **naam**: `Model` → `Model Afval`

#### Classes

##### `Categorie` — 🟡 Gewijzigd

- **package**: `Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model` → `Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval`

**Attributen:**

- 🟡 `code` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Categorie` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Categorie`
- 🟡 `naam` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Categorie` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Categorie`
- 🟡 `omschrijving` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Categorie` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Categorie`

##### `Container` — 🟡 Gewijzigd

- **package**: `Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model` → `Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval`

**Attributen:**

- 🟡 `containercode` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Container` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Container`
- 🟡 `sensorID` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Container` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Container`

##### `Containertype` — 🟡 Gewijzigd

- **package**: `Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model` → `Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval`

**Attributen:**

- 🟡 `naam` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Containertype` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Containertype`
- 🟡 `omschrijving` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Containertype` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Containertype`

##### `Fractie` — 🟡 Gewijzigd

- **package**: `Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model` → `Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval`

**Attributen:**

- 🟡 `naam` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Fractie` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Fractie`
- 🟡 `omschrijving` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Fractie` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Fractie`

##### `Locatie` — 🟡 Gewijzigd

- **package**: `Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model` → `Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval`

**Attributen:**

- 🟡 `adresaanduiding` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Locatie` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Locatie`
- 🟡 `locatiecode` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Locatie` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Locatie`
- 🟡 `locatiePunt` — Gewijzigd
    - **naam**: `locatie` → `locatiePunt`
    - **primitieve type**: `GML` → `GM_Point`
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Locatie` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Locatie`

##### `Melding` — 🟡 Gewijzigd

- **package**: `Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model` → `Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval`

**Attributen:**

- 🟡 `24uurs` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Melding` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Melding`
- 🟡 `datumtijd` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Melding` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Melding`
- 🟡 `illegaal` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Melding` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Melding`
- 🟡 `meldingnummer` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Melding` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Melding`
- 🟡 `omschrijving` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Melding` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Melding`

##### `Milieustraat` — 🟡 Gewijzigd

- **package**: `Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model` → `Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval`

**Attributen:**

- 🟡 `adresaanduiding` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Milieustraat` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Milieustraat`
- 🟡 `naam` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Milieustraat` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Milieustraat`
- 🟡 `omschrijving` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Milieustraat` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Milieustraat`

##### `Ophaalmoment` — 🟡 Gewijzigd

- **package**: `Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model` → `Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval`

**Attributen:**

- 🟡 `gewichtstoename` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Ophaalmoment` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Ophaalmoment`
- 🟡 `tijdstip` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Ophaalmoment` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Ophaalmoment`

##### `Pas` — 🟡 Gewijzigd

- **package**: `Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model` → `Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval`

**Attributen:**

- 🟡 `adresaanduiding` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Pas` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Pas`
- 🟡 `pasnummer` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Pas` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Pas`

##### `Prijsafspraak` — 🟡 Gewijzigd

- **package**: `Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model` → `Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval`

**Attributen:**

- 🟡 `datumEinde` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Prijsafspraak` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Prijsafspraak`
- 🟡 `datumStart` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Prijsafspraak` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Prijsafspraak`
- 🟡 `titel` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Prijsafspraak` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Prijsafspraak`

##### `Prijsregel` — 🟡 Gewijzigd

- **package**: `Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model` → `Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval`

**Attributen:**

- 🟡 `bedrag` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Prijsregel` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Prijsregel`
- 🟡 `credit` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Prijsregel` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Prijsregel`

##### `Rit` — 🟡 Gewijzigd

- **package**: `Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model` → `Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval`

**Attributen:**

- 🟡 `eindtijd` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Rit` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Rit`
- 🟡 `ritcode` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Rit` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Rit`
- 🟡 `starttijd` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Rit` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Rit`

##### `Route` — 🟡 Gewijzigd

- **package**: `Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model` → `Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval`

**Attributen:**

- 🟡 `geometrie` — Gewijzigd
    - **primitieve type**: `GML` → `Point`
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Route` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Route`
- 🟡 `routecode` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Route` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Route`
- 🟡 `routesoort` — Gewijzigd
    - **enumeratie**: `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Routesoort` → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Routesoort`
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Route` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Route`

##### `Storting` — 🟡 Gewijzigd

- **package**: `Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model` → `Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval`

**Attributen:**

- 🟡 `datumtijd` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Storting` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Storting`
- 🟡 `gewicht` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Storting` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Storting`

##### `Vuilniswagen` — 🟡 Gewijzigd

- **package**: `Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model` → `Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval`

**Attributen:**

- 🟡 `code` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Vuilniswagen` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Vuilniswagen`
- 🟡 `kenteken` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Vuilniswagen` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Vuilniswagen`
- 🟡 `type` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Vuilniswagen` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Vuilniswagen`

##### `Vulgraadmeting` — 🟡 Gewijzigd

- **package**: `Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model` → `Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval`

**Attributen:**

- 🟡 `tijdstip` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Vulgraadmeting` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Vulgraadmeting`
- 🟡 `vulgraad` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Vulgraadmeting` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Vulgraadmeting`
- 🟡 `vullingGewicht` — Gewijzigd
    - **class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Vulgraadmeting` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Vulgraadmeting`

#### Enumeraties

##### `Routesoort` — 🟡 Gewijzigd

- **package**: `Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model` → `Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval`

#### Associaties

- 🟡 Gewijzigd: `Container` «geschikt voor» → `Fractie`
  - **src class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Container` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Container`
  - **dst class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Fractie` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Fractie`
- 🟡 Gewijzigd: `Container` «heeft» → `Locatie`
  - **src class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Container` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Container`
  - **dst class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Locatie` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Locatie`
- 🟡 Gewijzigd: `Container` «heeft» → `Vulgraadmeting`
  - **src class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Container` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Container`
  - **dst class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Vulgraadmeting` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Vulgraadmeting`
- 🟡 Gewijzigd: `Container` «soort» → `Containertype`
  - **src class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Container` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Container`
  - **dst class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Containertype` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Containertype`
- 🟡 Gewijzigd: `Melding` «betreft» → `Containertype`
  - **src class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Melding` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Melding`
  - **dst class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Containertype` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Containertype`
- 🟡 Gewijzigd: `Melding` «betreft» → `Fractie`
  - **src class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Melding` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Melding`
  - **dst class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Fractie` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Fractie`
- 🟡 Gewijzigd: `Melding` «betreft» → `Locatie`
  - **src class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Melding` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Melding`
  - **dst class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Locatie` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Locatie`
- 🟡 Gewijzigd: `Melding` «hoofdcategorie» → `Categorie`
  - **src class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Melding` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Melding`
  - **dst class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Categorie` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Categorie`
- 🟡 Gewijzigd: `Melding` «subcategorie» → `Categorie`
  - **src class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Melding` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Melding`
  - **dst class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Categorie` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Categorie`
- 🟡 Gewijzigd: `Milieustraat` «inzamelpunt van» → `Fractie`
  - **src class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Milieustraat` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Milieustraat`
  - **dst class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Fractie` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Fractie`
- 🟡 Gewijzigd: `Ophaalmoment` «gelost» → `Container`
  - **src class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Ophaalmoment` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Ophaalmoment`
  - **dst class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Container` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Container`
- 🟡 Gewijzigd: `Ophaalmoment` «gestopt op» → `Locatie`
  - **src class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Ophaalmoment` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Ophaalmoment`
  - **dst class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Locatie` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Locatie`
- 🟡 Gewijzigd: `Pas` «geldig voor» → `Milieustraat`
  - **src class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Pas` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Pas`
  - **dst class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Milieustraat` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Milieustraat`
- 🟡 Gewijzigd: `Pas` «uitgevoerde storting» → `Storting`
  - **src class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Pas` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Pas`
  - **dst class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Storting` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Storting`
- 🟡 Gewijzigd: `Prijsafspraak` «heeft» → `Prijsregel`
  - **src class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Prijsafspraak` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Prijsafspraak`
  - **dst class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Prijsregel` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Prijsregel`
- 🟡 Gewijzigd: `Prijsregel` «betreft» → `Fractie`
  - **src class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Prijsregel` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Prijsregel`
  - **dst class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Fractie` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Fractie`
- 🟡 Gewijzigd: `Rit` «heeft» → `Ophaalmoment`
  - **src class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Rit` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Rit`
  - **dst class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Ophaalmoment` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Ophaalmoment`
- 🟡 Gewijzigd: `Rit` «uitgevoerd met» → `Vuilniswagen`
  - **src class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Rit` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Rit`
  - **dst class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Vuilniswagen` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Vuilniswagen`
- 🟡 Gewijzigd: `Rit` «volgens» → `Route`
  - **src class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Rit` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Rit`
  - **dst class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Route` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Route`
- 🟡 Gewijzigd: `Route` «gaat langs» → `Locatie`
  - **src class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Route` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Route`
  - **dst class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Locatie` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Locatie`
- 🟡 Gewijzigd: `Route` «ophalen» → `Fractie`
  - **src class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Route` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Route`
  - **dst class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Fractie` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Fractie`
- 🟡 Gewijzigd: `Storting` «bij» → `Milieustraat`
  - **src class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Storting` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Storting`
  - **dst class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Milieustraat` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Milieustraat`
- 🟡 Gewijzigd: `Storting` «fractie» → `Fractie`
  - **src class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Storting` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Storting`
  - **dst class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Fractie` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Fractie`
- 🟡 Gewijzigd: `Vuilniswagen` «geschikt voor» → `Containertype`
  - **src class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Vuilniswagen` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Vuilniswagen`
  - **dst class**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Containertype` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Containertype`

#### Generalisaties

- 🟡 Gewijzigd: `Melding` ⟶ `AanvraagOfMelding`
  - **subclass**: `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model::Melding` → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval::Melding`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingbeheer-openbare-ruimtemodel-basis-imbormodel-imbor"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Beheer Openbare Ruimte/Model Basis IMBOR/Model IMBOR

#### Classes

##### `Beheerobject` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `beheerobjectMemo` — Gewijzigd
    - **primitieve type**: `Memo` → `Tekst`

##### `Groenobject` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `opTalud` — Gewijzigd
    - **primitieve type**: `nee` → `Boolean`

##### `Installatie` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `installateur` — Gewijzigd
    - **primitieve type**: `Installateur` → _(leeg)_
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Beheer Openbare Ruimte/Model Basis IMBOR/Enumeratiesoort::enum_Installateur`

##### `Leiding` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `verhoogdRisico` — Gewijzigd
    - **primitieve type**: `nee` → `Boolean`

##### `Put` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `bovengrondsZichtbaar` — Gewijzigd
    - **primitieve type**: `nee` → `Boolean`

##### `Terreindeel` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `opTalud` — Gewijzigd
    - **primitieve type**: `nee` → `Boolean`

##### `Verhardingsobject` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `opTalud` — Gewijzigd
    - **primitieve type**: `nee` → `Boolean`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingbeheer-openbare-ruimtemodel-beheer-openbare-ruimte"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Beheer Openbare Ruimte/Model Beheer Openbare Ruimte

#### Classes

##### `Areaal` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `geometrie` — Gewijzigd
    - **primitieve type**: `MultiSurface` → `GM_MultiSurface`

##### `Melding` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `locatie` — Gewijzigd
    - **primitieve type**: `Locatie` → `GM_Point`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingbouwen-en-wonenmodel-wonen"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Bouwen en Wonen/Model Wonen

#### Classes

##### `Plan` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `percelen` — Gewijzigd
    - **primitieve type**: `MultiSurface` → `GM_MultiSurface`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatiefinancienmodel-financien"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/Financien/Model Financien

#### Associaties

- 🟡 Gewijzigd: `Begroting` «valt binnen» → `Periode`
  - **dst mult. start**: _(leeg)_ → `1`
  - **dst mult. end**: _(leeg)_ → `*`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatiehrmodel-hr"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/HR/Model HR

#### Classes

##### `Rol` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `omschrijving` — Gewijzigd
    - **naam**: `rol` → `omschrijving`

#### Associaties

- 🟡 Gewijzigd: `Formatieplaats` «functie van formatieplaats» → `Functie`
  - **src mult. start**: _(leeg)_ → `0`
  - **src mult. end**: _(leeg)_ → `*`
  - **dst mult. start**: _(leeg)_ → `1`
  - **dst mult. end**: _(leeg)_ → `*`
- 🟡 Gewijzigd: `Formatieplaats` «toegewezen aan» → `Dienstverband`
  - **src mult. start**: _(leeg)_ → `0`
  - **src mult. end**: _(leeg)_ → `*`
  - **dst mult. start**: _(leeg)_ → `0`
  - **dst mult. end**: _(leeg)_ → `*`
- 🟡 Gewijzigd: `Functie` «gebaseerd op» → `NormProfiel`
  - **src mult. start**: _(leeg)_ → `1`
  - **src mult. end**: _(leeg)_ → `1`
  - **dst mult. start**: _(leeg)_ → `1`
  - **dst mult. end**: _(leeg)_ → `1`
- 🟡 Gewijzigd: `Inzet` «inzet voor functie» → `Functie`
  - **src mult. start**: _(leeg)_ → `1`
  - **src mult. end**: _(leeg)_ → `1`
  - **dst mult. start**: _(leeg)_ → `1`
  - **dst mult. end**: _(leeg)_ → `1`
- 🟡 Gewijzigd: `NormProfiel` «onderdeel van» → `Functiehuis`
  - **src mult. start**: _(leeg)_ → `1`
  - **src mult. end**: _(leeg)_ → `*`
  - **dst mult. start**: _(leeg)_ → `1`
  - **dst mult. end**: _(leeg)_ → `1`
- 🟡 Gewijzigd: `Relatie` «is kind van» → `Werknemer`
  - **dst mult. start**: _(leeg)_ → `1`
  - **dst mult. end**: _(leeg)_ → `1`
- 🟡 Gewijzigd: `Rol` «hoort bij» → `OrganisatorischeEenheidHR`
  - **src mult. start**: _(leeg)_ → `0`
  - **src mult. end**: _(leeg)_ → `*`
  - **dst mult. start**: _(leeg)_ → `0`
  - **dst mult. end**: _(leeg)_ → `1`
- 🟡 Gewijzigd: `Werknemer` «Beoordeeld door» → `Beoordeling`
  - **naam**: `Beoordeelt door` → `Beoordeeld door`
- 🟡 Gewijzigd: `Werknemer` «is partner van» → `Relatie`
  - **src mult. start**: _(leeg)_ → `1`
  - **src mult. end**: _(leeg)_ → `1`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatieictmodel-ict"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/ICT/Model ICT

#### Classes

##### `Classificatie` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `id` — Verwijderd
- 🟡 `bevatPersoonsgegevens` — Gewijzigd
    - **primitieve type**: `Persoonsgegevens` → `boolean`
- 🟡 `gerelateerdPersoonsgegevens` — Gewijzigd
    - **primitieve type**: `Persoonsgegevens` → `AN200`

##### `Database` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `databaseInstantie` — Gewijzigd
    - **naam**: `database` → `databaseInstantie`
- 🟡 `OTAP` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Boolean`

#### Associaties

- 🟡 Gewijzigd: `Prijzenboek` «heeft prijs» → `Product`
  - **src mult. start**: _(leeg)_ → `0`
  - **src mult. end**: _(leeg)_ → `*`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatievastgoedmodel-vastgoed"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/Vastgoed/Model Vastgoed

#### Classes

##### `Adresaanduiding` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `adres` — Gewijzigd
    - **naam**: `adresaanduiding` → `adres`

##### `Locatieonroerendezaak` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `geometrie` — Gewijzigd
    - **primitieve type**: `Vlak` → `GM_Surface`

##### `Vastgoedobject` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `afgekochteErfpacht` — Gewijzigd
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Enumeratiesoort::Boolean`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernbagmodel-bag"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/BAG/Model BAG

#### Classes

##### `BinnenlandsAdres` — 🟢 Toegevoegd

**Attributen:**

- 🟢 `BAGID` — Toegevoegd
- 🟢 `gemeentenaam` — Toegevoegd
- 🟢 `huisletter` — Toegevoegd
- 🟢 `huisnummer` — Toegevoegd
- 🟢 `huisnummertoevoeging` — Toegevoegd
- 🟢 `postcode` — Toegevoegd
- 🟢 `straatnaam` — Toegevoegd

##### `Buurt` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `geometrie` — Gewijzigd
    - **primitieve type**: `MultiSurface` → `GM_MultiSurface`

##### `Gemeente` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `geometrie` — Gewijzigd
    - **primitieve type**: `Surface` → `GM_Surface`

##### `Ligplaats` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `geometrie` — Gewijzigd
    - **primitieve type**: `Surface` → `GM_Surface`

##### `Nummeraanduiding` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `postcode` — Gewijzigd
    - **primitieve type**: `char` → `AN6`

##### `OpenbareRuimte` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `geometrie` — Gewijzigd
    - **primitieve type**: `MultiSurface` → `GM_MultiSurface`
- 🟡 `wegsegment` — Gewijzigd
    - **primitieve type**: `Curve` → `GM_Curve`

##### `Pand` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `geometrieBovenaanzicht` — Gewijzigd
    - **primitieve type**: `Surface` → `GM_Surface`
- 🟡 `geometrieMaaiveld` — Gewijzigd
    - **primitieve type**: `MultiSurface` → `GM_MultiSurface`
- 🟡 `oorspronkelijkBouwjaar` — Gewijzigd
    - **primitieve type**: `JAAR` → `N4`

##### `Standplaats` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `Geometrie` — Gewijzigd
    - **primitieve type**: `Surface` → `GM_Surface`

##### `Wijk` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `geometrie` — Gewijzigd
    - **primitieve type**: `MultiSurface` → `GM_MultiSurface`

##### `Woonplaats` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `geometrie` — Gewijzigd
    - **primitieve type**: `Surface` → `GM_Surface`

#### Associaties

- 🟡 Gewijzigd: `Gemeente` «is overgegaan in» → `Gemeente`
  - **src mult. start**: _(leeg)_ → `0`
  - **src mult. end**: _(leeg)_ → `*`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kerndimensiesmodel"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/Dimensies/Model

#### Classes

##### `Periode` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `omschrijving` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `AN255`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kerngeneriekmodel-generiek"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/Generiek/Model Generiek

#### Classes

##### `Foto` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `locatie` — Gewijzigd
    - **primitieve type**: `GML` → `GM_Point`

##### `Gebied` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `gebiedsAanduiding` — Gewijzigd
    - **naam**: `gebied` → `gebiedsAanduiding`
    - **primitieve type**: `Polygoon` → `GM_MultiSurface`

##### `Lijn` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `lijnLocatie` — Gewijzigd
    - **naam**: `lijn` → `lijnLocatie`
    - **primitieve type**: `Lijn` → `GM_Lijn`

##### `Punt` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `puntLocatie` — Gewijzigd
    - **naam**: `punt` → `puntLocatie`
    - **primitieve type**: `Punt` → `GM_Punt`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrgbzplusmodel-rgbzgroepattribuutsoort"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RGBZPlus/Model RGBZ/Groepattribuutsoort

#### Classes

##### `AfwijkendBuitenlandsCorrespondentieadresRol` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `adresBuitenland1` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `AN200`
- 🟡 `adresBuitenland2` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `AN200`
- 🟡 `adresBuitenland3` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `AN200`

##### `AnderZaakobjectZaak` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `anderZaakobjectLocatie` — Gewijzigd
    - **primitieve type**: `GML` → `GM_Point`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrgbzplusmodel-rgbzmetagegevens"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RGBZPlus/Model RGBZ/Metagegevens

#### Classes

##### `Brondocumenten` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `datumDocument` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`

##### `FormeleHistorie` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `tijdstipRegistratieGegevens` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `DateTime`

##### `MaterieleHistorie` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `datumBeginGeldigheidGegevens` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`
- 🟡 `datumEindeGeldigheidGegevens` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrgbzplusmodel-rgbzmodel-kern-rgbz"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RGBZPlus/Model RGBZ/Model Kern RGBZ

#### Classes

##### `Bedrijfsprocestype` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `Omschrijving` — Gewijzigd
    - **primitieve type**: `AM200` → `AN200`

##### `Besluit` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `datumBesluit` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`
- 🟡 `datumPublicatie` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`
- 🟡 `datumStart` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`
- 🟡 `datumUiterlijkeReactie` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`
- 🟡 `datumVerval` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`
- 🟡 `datumVerzending` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`
- 🟡 `omschrijving` — Gewijzigd
    - **naam**: `besluit` → `omschrijving`
- 🟡 `redenVerval` — Gewijzigd
    - **primitieve type**: `X40` → `AN40`

##### `Betrokkene` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `rol` — Verwijderd
- 🟡 `adresBinnenland` — Gewijzigd
    - **type (class)**: _(leeg)_ → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/BAG/Model BAG::BinnenlandsAdres`
- 🟡 `adresBuitenland` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `AN200`

##### `Document` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `datumCreatieDocument` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`
- 🟡 `datumOntvangstdocument` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`
- 🟡 `datumVerzendingDocument` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`

##### `EnkelvoudigDocument` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `documentInhoud` — Gewijzigd
    - **primitieve type**: `Documentformaat` → `AN255`

##### `Medewerker` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `datumUitDienst` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`
- 🟡 `extern` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Boolean`

##### `Object` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `adresBinnenland` — Gewijzigd
    - **type (class)**: _(leeg)_ → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/BAG/Model BAG::BinnenlandsAdres`
- 🟡 `adresBuitenland` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `AN200`
- 🟡 `geometrie` — Gewijzigd
    - **primitieve type**: `GML` → `GM_Point`
- 🟡 `indicatieRisico` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Boolean`
- 🟡 `toelichting` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Tekst`

##### `OrganisatorischeEenheid` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `datumOntstaan` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`
- 🟡 `datumOpheffing` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`
- 🟡 `Formatie` — Gewijzigd
    - **stereotype**: _(leeg)_ → `Attribuutsoort`
    - **primitieve type**: _(leeg)_ → `AN255`
    - **authentiek**: _(leeg)_ → `Authentiek`

##### `Status` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `datumStatusGezet` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`

##### `ZAAK - Origineel` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `datumEinde` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`
- 🟡 `datumEindeGepland` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`
- 🟡 `datumEindeUiterlijkeAfdoening` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`
- 🟡 `datumLaatsteBetaling` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`
- 🟡 `datumRegistratie` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`
- 🟡 `datumStart` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`
- 🟡 `datumVernietigingDossier` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`
- 🟡 `indicatieDeelzaken` — Gewijzigd
    - **primitieve type**: `A1` → `Boolean`

##### `Zaak` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `attribute` — Verwijderd
- 🔴 `document` — Verwijderd
- 🟡 `datumEinde` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`
- 🟡 `datumEindeGepland` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`
- 🟡 `datumEindeUiterlijkeAfdoening` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`
- 🟡 `datumLaatsteBetaling` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`
- 🟡 `datumRegistratie` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`
- 🟡 `datumStart` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`
- 🟡 `datumVernietigingDossier` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`
- 🟡 `indicatieDeelzaken` — Gewijzigd
    - **primitieve type**: `A1` → `Boolean`

#### Associaties

- 🟡 Gewijzigd: `Bedrijfsprocestype` «is onderdeel van» → `Bedrijfsprocestype`
  - **src mult. start**: _(leeg)_ → `0`
  - **src mult. end**: _(leeg)_ → `*`
  - **dst mult. start**: _(leeg)_ → `0`
  - **dst mult. end**: _(leeg)_ → `*`
- 🟡 Gewijzigd: `Zaak` «heeft betrekking op andere» → `Zaak`
  - **src mult. start**: _(leeg)_ → `1`
  - **src mult. end**: _(leeg)_ → `1`
- 🟡 Gewijzigd: `Zaak` «is deelzaak van» → `Zaak`
  - **src mult. start**: _(leeg)_ → `1`
  - **src mult. end**: _(leeg)_ → `1`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelenumeratiesoort"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Enumeratiesoort

#### Enumeraties

##### `functieOndersteunendWegdeelPlus` — 🔴 Verwijderd

##### `typeringOndersteunendWaterPlus` — 🔴 Verwijderd

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelgroepattribuutsoort"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Groepattribuutsoort

#### Classes

##### `GeboorteIngeschrevenNatuurlijkPersoon` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `datumGeboorte` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`

##### `GeboorteIngeschrevenPersoon` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `datumGeboorte` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`
- 🟡 `geboorteplaats` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `AN200`

##### `KoopsomKadastraleOnroerendeZaak` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `datumTransactie` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`

##### `NaamNatuurlijkPersoon` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `geslachtsnaam` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `AN255`
- 🟡 `voornamen` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `AN200`
- 🟡 `voorvoegselGeslachtsnaam` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `AN255`

##### `NederlandseNationaliteitIngeschrevenPersoon` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `aanduidingBijzonderNederlanderschap` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `boolean`
- 🟡 `redenVerkrijgingNederlandseNationaliteit` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `AN200`
- 🟡 `redenVerliesNederlandseNationaliteit` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `AN200`

##### `OntbindingHuwelijk/geregistreerdPartnerschap` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `datumEinde` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`

##### `OverlijdenIngeschrevenNatuurlijkPersoon` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `datumOverlijden` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`

##### `OverlijdenIngeschrevenPersoon` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `datumOverlijden` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`
- 🟡 `overlijdensplaats` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `AN200`

##### `Postadres` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `postadresType` — Gewijzigd
    - **primitieve type**: `postadresType` → `AN255`
- 🟡 `postcodePostadres` — Gewijzigd
    - **primitieve type**: `POSTCODE` → `AN6`

##### `SamengesteldeNaamNatuurlijkPersoon` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `namenreeks` — Gewijzigd
    - **primitieve type**: `INDIC` → `boolean`
- 🟡 `scheidingsteken` — Gewijzigd
    - **primitieve type**: `VOORVOEGSEL` → `AN255`
- 🟡 `voorvoegsel` — Gewijzigd
    - **primitieve type**: `VOORVOEGSEL` → `AN255`

##### `SluitingOfAangaanHuwelijkOfGeregistreerdPartnerschap` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `datumAanvang` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`

##### `SoortFunctioneelGebied` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `indicatiePlusBRPopulatie` — Gewijzigd
    - **primitieve type**: `INDIC` → `Boolean`

##### `SoortKunstwerk` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `indicatiePlusBRPopulatie` — Gewijzigd
    - **primitieve type**: `INDIC` → `Boolean`

##### `SoortOverigBouwwerk` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `indicatiePlusBRPopulatie` — Gewijzigd
    - **primitieve type**: `INDIC` → `Boolean`

##### `SoortScheiding` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `indicatiePlusBRPopulatie` — Gewijzigd
    - **primitieve type**: `INDIC` → `Boolean`

##### `SoortSpoor` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `indicatiePlusBRPopulatie` — Gewijzigd
    - **primitieve type**: `INDIC` → `Boolean`

##### `VerblijfBuitenlandSubject` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `adresBuitenland1` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `AN200`
- 🟡 `adresBuitenland2` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `AN200`
- 🟡 `adresBuitenland3` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `AN200`

##### `VerblijfadresIngeschrevenPersoon` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `beschrijvingLocatie` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `AN255`

##### `VerblijfsrechtIngeschrevenNatuurlijkPersoon` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `datumAanvangVerblijfsrecht` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`
- 🟡 `datumMededelingVerblijfsrecht` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`
- 🟡 `datumVoorzienEindeVerblijfsrecht` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelmodel-kern-rsgb"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Model Kern RSGB

#### Classes

##### `Aantekening` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `begrenzing` — Gewijzigd
    - **primitieve type**: `Surface` → `GM_Surface`

##### `Appartementsrechtsplitsing` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `typeSplitsing` — Gewijzigd
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Enumeratiesoort::typeringAppartementsrechtsplitsing`

##### `BegroeidTerreindeel` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `datumBeginGeldigheid` — Gewijzigd
    - **naam**: `datumBeginGeldigheidBegroeidTerreindeel` → `datumBeginGeldigheid`
- 🟡 `datumEindeGeldigheid` — Gewijzigd
    - **naam**: `datumEindeGeldigheidBegroeidTerreindeel` → `datumEindeGeldigheid`
- 🟡 `fysiekVoorkomen` — Gewijzigd
    - **naam**: `fysiekVoorkomenBegroeidTerreindeel` → `fysiekVoorkomen`
- 🟡 `geometrie` — Gewijzigd
    - **naam**: `geometrieBegroeidTerreindeel` → `geometrie`
    - **primitieve type**: `Surface` → `GM_Surface`
- 🟡 `identificatie` — Gewijzigd
    - **naam**: `identificatieBegroeidTerreindeel` → `identificatie`
- 🟡 `kruinlijngeometrie` — Gewijzigd
    - **naam**: `kruinlijngeometrieBegroeidTerreindeel` → `kruinlijngeometrie`
    - **primitieve type**: `Curve` → `GM_Curve`
- 🟡 `LOD0Geometrie` — Gewijzigd
    - **naam**: `LOD0GeometrieBegroeidTerreindeel` → `LOD0Geometrie`
    - **primitieve type**: `MultiSurface` → `GM_MultiSurface`
- 🟡 `opTalud` — Gewijzigd
    - **naam**: `begroeidTerreindeelOpTalud` → `opTalud`
    - **primitieve type**: `INDIC` → `boolean`
- 🟡 `plusFysiekVoorkomen` — Gewijzigd
    - **naam**: `plusFysiekVoorkomenBegroeidTerreindeel` → `plusFysiekVoorkomen`
- 🟡 `relatieveHoogteligging` — Gewijzigd
    - **naam**: `relatieveHoogteliggingBegroeidTerreindeel` → `relatieveHoogteligging`
- 🟡 `status` — Gewijzigd
    - **naam**: `statusBegroeidTerreindeel` → `status`

##### `Briefadres` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `adresFunctie` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `An200`
- 🟡 `omschrijvingAangifte` — Gewijzigd
    - **primitieve type**: `Text` → `AN255`

##### `FunctioneelGebied` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `geometrieFunctioneelGebied` — Gewijzigd
    - **primitieve type**: `Surface` → `GM_Surface`

##### `Gebied` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `geometrie` — Gewijzigd
    - **primitieve type**: `MultiSurface` → `GM_MultiSurface`

##### `Gebouwinstallatie` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `geometrieGebouwinstallatie` — Gewijzigd
    - **primitieve type**: `Surface` → `GM_Surface`
- 🟡 `LOD0GeometrieGebouwinstallatie` — Gewijzigd
    - **primitieve type**: `Surface` → `GM_Surface`

##### `Huishouden` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `relatie` — Verwijderd

##### `Inrichtingselement` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `geometrieInrichtingselement` — Gewijzigd
    - **primitieve type**: `PuntLijnVlak` → `GM_Surface`
- 🟡 `LOD0GeometrieInrichtingselement` — Gewijzigd
    - **primitieve type**: `PuntLijnVlak` → `GM_Surface`

##### `KadastraalPerceel` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `begrenzingPerceel` — Gewijzigd
    - **primitieve type**: `Surface` → `GM_Surface`
- 🟡 `indicatieDeelperceel` — Gewijzigd
    - **primitieve type**: `INDIC` → `boolean`

##### `KadastraleOnroerendeZaak` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `attribute` — Verwijderd
- 🔴 `oud` — Verwijderd
- 🟡 `appartementsrechtvolgnummer` — Gewijzigd
    - **stereotype**: `Data element` → `Attribuutsoort`
- 🟡 `begrenzing` — Gewijzigd
    - **primitieve type**: `Surface` → `GM_Surface`
- 🟡 `datumBeginGeldigheid` — Gewijzigd
    - **naam**: `datumBeginGeldigheidKadastraleOnroerendeZaak` → `datumBeginGeldigheid`
- 🟡 `datumEindeGeldigheid` — Gewijzigd
    - **naam**: `datumEindeGeldigheidKadastraleOnroerendeZaak` → `datumEindeGeldigheid`
- 🟡 `perceelnummer` — Gewijzigd
    - **stereotype**: `Data element` → `Attribuutsoort`

##### `Kunstwerkdeel` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `LOD0GeometrieKunstwerkdeel` — Gewijzigd
    - **primitieve type**: `PuntLijnVlak` → `GM_Surface`

##### `MaatschappelijkeActiviteit` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `adresBinnenland` — Gewijzigd
    - **primitieve type**: `AN257` → _(leeg)_
    - **type (class)**: _(leeg)_ → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/BAG/Model BAG::BinnenlandsAdres`
- 🟡 `indicatieEconomischActief` — Gewijzigd
    - **primitieve type**: `INDIC` → `boolean`

##### `Nationaliteit` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `omschrijving` — Gewijzigd
    - **naam**: `Nationaliteit` → `omschrijving`
- 🟡 `redenVerkrijgingNLNationaliteit` — Gewijzigd
    - **naam**: `Reden verkrijging Nederlandse nationaliteit` → `redenVerkrijgingNLNationaliteit`
- 🟡 `redenVerliesNLNationaliteit` — Gewijzigd
    - **naam**: `Reden verlies Nederlandse nationaliteit` → `redenVerliesNLNationaliteit`

##### `NatuurlijkPersoon` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `attribute` — Verwijderd
- 🟡 `bijzonderNederlanderschap` — Gewijzigd
    - **naam**: `aanduidingBijzonderNederlanderschapPersoon` → `bijzonderNederlanderschap`
- 🟡 `geslachtsaanduiding` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `A1`
    - **enumeratie**: `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Enumeratiesoort::geslacht` → _(leeg)_

##### `OnbegroeidTerreindeel` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `datumBeginGeldigheid` — Gewijzigd
    - **naam**: `datumBeginGeldigheidOnbegroeidTerreindeel` → `datumBeginGeldigheid`
- 🟡 `datumEindeGeldigheid` — Gewijzigd
    - **naam**: `datumEindeGeldigheidOnbegroeidTerreindeel` → `datumEindeGeldigheid`
- 🟡 `fysiekVoorkomen` — Gewijzigd
    - **naam**: `fysiekVoorkomenOnbegroeidTerreindeel` → `fysiekVoorkomen`
- 🟡 `geometrie` — Gewijzigd
    - **naam**: `geometrieOnbegroeidTerreindeel` → `geometrie`
    - **primitieve type**: `Surface` → `GM_Surface`
- 🟡 `identificatie` — Gewijzigd
    - **naam**: `identificatieOnbegroeidTerreindeel` → `identificatie`
- 🟡 `kruinlijngeometrie` — Gewijzigd
    - **naam**: `kruinlijngeometrieOnbegroeidTerreindeel` → `kruinlijngeometrie`
    - **primitieve type**: `Curve` → `GM_Curve`
- 🟡 `onbegroeidTerreindeelOpTalud` — Gewijzigd
    - **primitieve type**: `INDIC` → `boolean`
- 🟡 `plusFysiekVoorkomen` — Gewijzigd
    - **naam**: `plusFysiekVoorkomenOnbegroeidTerreindeel` → `plusFysiekVoorkomen`
- 🟡 `relatieveHoogteligging` — Gewijzigd
    - **naam**: `relatieveHoogteliggingOnbegroeidTerreindeel` → `relatieveHoogteligging`
- 🟡 `status` — Gewijzigd
    - **naam**: `statusOnbegroeidTerreindeel` → `status`

##### `Onbestemd Adres` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `postcode` — Gewijzigd
    - **primitieve type**: `postcode` → `AN6`

##### `OndersteunendWaterdeel` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `datumBeginGeldigheid` — Gewijzigd
    - **naam**: `datumBeginGeldigheidOndersteunendWaterdeel` → `datumBeginGeldigheid`
- 🟡 `datumEindeGeldigheid` — Gewijzigd
    - **naam**: `datumEindeGeldigheidOndersteunendWaterdeel` → `datumEindeGeldigheid`
- 🟡 `geometrie` — Gewijzigd
    - **naam**: `geometrieOndersteunendWaterdeel` → `geometrie`
    - **primitieve type**: `Surface` → `GM_Surface`
- 🟡 `identificatie` — Gewijzigd
    - **naam**: `identificatieOndersteunendWaterdeel` → `identificatie`
- 🟡 `plusType` — Gewijzigd
    - **naam**: `plusTypeOndersteunendWaterdeel` → `plusType`
    - **primitieve type**: _(leeg)_ → `typeringOndersteunendWaterPlus`
    - **enumeratie**: `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Enumeratiesoort::typeringOndersteunendWaterPlus` → _(leeg)_
- 🟡 `relatieveHoogteligging` — Gewijzigd
    - **naam**: `relatieveHoogteliggingOndersteunendWaterdeel` → `relatieveHoogteligging`
- 🟡 `status` — Gewijzigd
    - **naam**: `statusOndersteunendWaterdeel` → `status`
- 🟡 `type` — Gewijzigd
    - **naam**: `typeOndersteunendWaterdeel` → `type`

##### `OndersteunendWegdeel` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `datumBeginGeldigheid` — Gewijzigd
    - **naam**: `datumBeginGeldigheidOndersteunendWegdeel` → `datumBeginGeldigheid`
- 🟡 `datumEindeGeldigheid` — Gewijzigd
    - **naam**: `datumEindeGeldigheidOndersteunendWegdeel` → `datumEindeGeldigheid`
- 🟡 `functie` — Gewijzigd
    - **naam**: `functieOndersteunendWegdeel` → `functie`
- 🟡 `fysiekVoorkomen` — Gewijzigd
    - **naam**: `fysiekVoorkomenOndersteunendWegdeel` → `fysiekVoorkomen`
- 🟡 `geometrie` — Gewijzigd
    - **naam**: `geometrieOndersteunendWegdeel` → `geometrie`
    - **primitieve type**: `Surface` → `GM_Surface`
- 🟡 `identificatie` — Gewijzigd
    - **naam**: `identificatieOndersteunendWegdeel` → `identificatie`
- 🟡 `kruinlijngeometrie` — Gewijzigd
    - **naam**: `kruinlijngeometrieOndersteunendWegdeel` → `kruinlijngeometrie`
    - **primitieve type**: `Curve` → `GM_Curve`
- 🟡 `LOD0Geometrie` — Gewijzigd
    - **naam**: `LOD0GeometrieOndersteunendWegdeel` → `LOD0Geometrie`
    - **primitieve type**: `Surface` → `GM_Surface`
- 🟡 `opTalud` — Gewijzigd
    - **naam**: `ondersteunendWegdeelOpTalud` → `opTalud`
    - **primitieve type**: `INDIC` → `boolean`
- 🟡 `plusFunctie` — Gewijzigd
    - **naam**: `plusFunctieOndersteunendWegdeel` → `plusFunctie`
    - **primitieve type**: _(leeg)_ → `functieOndersteunendWegdeelPlus`
    - **enumeratie**: `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Enumeratiesoort::functieOndersteunendWegdeelPlus` → _(leeg)_
- 🟡 `plusFysiekVoorkomen` — Gewijzigd
    - **naam**: `plusFysiekVoorkomenOndersteunendWegdeel` → `plusFysiekVoorkomen`
- 🟡 `relatieveHoogteligging` — Gewijzigd
    - **naam**: `relatieveHoogteliggingOndersteunendWegdeel` → `relatieveHoogteligging`
- 🟡 `status` — Gewijzigd
    - **naam**: `statusOndersteunendWegdeel` → `status`

##### `Overbruggingsdeel` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `geometrieOverbruggingsdeel` — Gewijzigd
    - **primitieve type**: `Surface` → `GM_Surface`
- 🟡 `LOD0GeometrieOverbruggingsdeel` — Gewijzigd
    - **primitieve type**: `Surface` → `GM_Surface`
- 🟡 `overbruggingIsBeweegbaar` — Gewijzigd
    - **primitieve type**: `INDIC` → `Boolean`

##### `OverigBouwwerk` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `LOD0GeometrieOverigBouwwerk` — Gewijzigd
    - **primitieve type**: `PuntLijnVlak` → `GM_Surface`

##### `OverigGebouwdObject` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `bouwjaar` — Gewijzigd
    - **primitieve type**: `JAAR` → `N4`
- 🟡 `indicatiePlanobject` — Gewijzigd
    - **primitieve type**: `INDIC` → `boolean`

##### `OverigeAdresseerbaarObjectAanduiding` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `Identificatiecode` — Gewijzigd
    - **naam**: `IdentificatiecodeOverigAdresseerbaarObjectAanduiding` → `Identificatiecode`

##### `OverigeScheiding` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `LOD0GeometrieOverigeScheiding` — Gewijzigd
    - **primitieve type**: `PuntLijnVlak` → `GM_Surface`

##### `Rechtspersoon` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `adresBinnenland` — Gewijzigd
    - **primitieve type**: `AN257` → _(leeg)_
    - **type (class)**: _(leeg)_ → `Class: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/BAG/Model BAG::BinnenlandsAdres`

##### `Reisdocument` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `datumEindeGeldigheidDocument` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`
- 🟡 `datumIngangDocument` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`
- 🟡 `datumInhoudingOfVermissing` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`
- 🟡 `datumUitgifte` — Gewijzigd
    - **primitieve type**: _(leeg)_ → `Datum`

##### `Scheiding` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `LOD0GeometrieScheiding` — Gewijzigd
    - **primitieve type**: `PuntLijnVlak` → `GM_Surface`

##### `Spoor` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `geometrieSpoor` — Gewijzigd
    - **primitieve type**: `Curve` → `GM_Curve`
- 🟡 `LOD0GeometrieSpoor` — Gewijzigd
    - **primitieve type**: `Curve` → `GM_Curve`

##### `Tunneldeel` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `geometrieTunneldeel` — Gewijzigd
    - **primitieve type**: `Surface` → `GM_Surface`
- 🟡 `LOD0GeometrieTunneldeel` — Gewijzigd
    - **primitieve type**: `Surface` → `GM_Surface`

##### `Vegetatieobject` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `geometrieVegetatieobject` — Gewijzigd
    - **primitieve type**: `PuntLijnVlak` → `GM_Surface`
- 🟡 `LOD0GeometrieVegetatieobject` — Gewijzigd
    - **primitieve type**: `PuntLijnVlak` → `GM_Surface`

##### `WOZ-object` — 🟡 Attributen gewijzigd

**Attributen:**

- 🔴 `attribute` — Verwijderd
- 🟡 `geometrieWOZObject` — Gewijzigd
    - **primitieve type**: `Surface` → `GM_Surface`

##### `Waterdeel` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `geometrieWaterdeel` — Gewijzigd
    - **primitieve type**: `Surface` → `GM_Surface`

##### `Wegdeel` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `geometrieWegdeel` — Gewijzigd
    - **primitieve type**: `Surface` → `GM_Surface`
- 🟡 `kruinlijngeometrieWegdeel` — Gewijzigd
    - **primitieve type**: `Curve` → `GM_Curve`
- 🟡 `LOD0GeometrieWegdeel` — Gewijzigd
    - **primitieve type**: `Surface` → `GM_Surface`
- 🟡 `wegdeelOpTalud` — Gewijzigd
    - **primitieve type**: `INDIC` → `boolean`

##### `Zekerheidsrecht` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `omschrijvingBetrokkenRecht` — Gewijzigd
    - **primitieve type**: `AN` → `AN255`

#### Associaties

- 🟡 Gewijzigd: `Appartementsrechtsplitsing` → `SplitsingstekeningReferentie`
  - **src mult. start**: _(leeg)_ → `1`
  - **src mult. end**: _(leeg)_ → `1`
- 🟡 Gewijzigd: `FunctioneelGebied` → `SoortFunctioneelGebied`
  - **src mult. start**: _(leeg)_ → `0`
  - **src mult. end**: _(leeg)_ → `*`
- 🟡 Gewijzigd: `IngeschrevenPersoon` «Ouder 1» → `IngeschrevenPersoon`
  - **src mult. start**: _(leeg)_ → `1`
  - **src mult. end**: _(leeg)_ → `1`
  - **dst mult. start**: _(leeg)_ → `1`
  - **dst mult. end**: _(leeg)_ → `1`
- 🟡 Gewijzigd: `IngeschrevenPersoon` «Ouder 2» → `IngeschrevenPersoon`
  - **src mult. start**: _(leeg)_ → `1`
  - **src mult. end**: _(leeg)_ → `1`
  - **dst mult. start**: _(leeg)_ → `1`
  - **dst mult. end**: _(leeg)_ → `1`
- 🟡 Gewijzigd: `KadastraleOnroerendeZaak` → `KoopsomKadastraleOnroerendeZaak`
  - **src mult. start**: _(leeg)_ → `1`
  - **src mult. end**: _(leeg)_ → `1`
- 🟡 Gewijzigd: `KadastraleOnroerendeZaak` → `LocatieKadastraleOnroerendeZaak`
  - **src mult. start**: _(leeg)_ → `1`
  - **src mult. end**: _(leeg)_ → `1`
- 🟡 Gewijzigd: `Kunstwerkdeel` → `SoortKunstwerk`
  - **src mult. start**: _(leeg)_ → `0`
  - **src mult. end**: _(leeg)_ → `*`
- 🟡 Gewijzigd: `OverigBouwwerk` → `SoortOverigBouwwerk`
  - **src mult. start**: _(leeg)_ → `0`
  - **src mult. end**: _(leeg)_ → `*`
- 🟡 Gewijzigd: `Scheiding` → `SoortScheiding`
  - **src mult. start**: _(leeg)_ → `0`
  - **src mult. end**: _(leeg)_ → `*`
- 🟡 Gewijzigd: `Spoor` → `SoortSpoor`
  - **src mult. start**: _(leeg)_ → `0`
  - **src mult. end**: _(leeg)_ → `*`
- 🟡 Gewijzigd: `Vestiging` → `SBIActiviteitVestiging`
  - **src mult. start**: _(leeg)_ → `1`
  - **src mult. end**: _(leeg)_ → `1`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelreferentielijsten"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Referentielijsten

#### Classes

##### `AardAantekening` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `naamAardAantekening` — Gewijzigd
    - **primitieve type**: `AN` → `AN255`

##### `AardFiliatie` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `naamAardFiliatie` — Gewijzigd
    - **primitieve type**: `AN` → `AN255`

##### `AardZakelijkRecht` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `naamAardZakelijkRecht` — Gewijzigd
    - **primitieve type**: `AN` → `AN255`

##### `AkrKadastraleGemeentecode` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `AKRCode` — Gewijzigd
    - **primitieve type**: `AN` → `AN255`

##### `AutoriteitAfgifteNederlandsReisdocument` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `omschrijving` — Gewijzigd
    - **primitieve type**: `AN` → `AN255`

##### `CultuurcodeBebouwd` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `code` — Gewijzigd
    - **naam**: `cultuurcodeBebouwd` → `code`
- 🟡 `naamCultuurcodeBebouwd` — Gewijzigd
    - **primitieve type**: `AN` → `AN255`

##### `CultuurcodeOnbebouwd` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `code` — Gewijzigd
    - **naam**: `cultuurcodeOnbebouwd` → `code`
- 🟡 `naamCultuurcodeOnbebouwd` — Gewijzigd
    - **primitieve type**: `AN` → `AN255`

##### `Partij` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `verstrekkingsbeperkingMogelijk` — Gewijzigd
    - **primitieve type**: `INDIC` → `Boolean`

##### `SoortGrootte` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `naamSoortGrootte` — Gewijzigd
    - **primitieve type**: `AN` → `AN255`

##### `SoortWOZObject` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `naamSoortObjectcode` — Gewijzigd
    - **primitieve type**: `AN` → `AN255`
- 🟡 `opmerkingenSoortObjectcode` — Gewijzigd
    - **primitieve type**: `AN` → `AN255`

##### `Valutasoort` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `naamValuta` — Gewijzigd
    - **primitieve type**: `AN` → `AN255`

##### `WOZ-Deelobjectcode` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `naamDeelobjectcode` — Gewijzigd
    - **primitieve type**: `AN` → `AN255`

<a id="structureel-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelarchiefmodel-kern-rsgb"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/archief/Model Kern RSGB

#### Classes

##### `BenoemdObject` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `geometrieVlak` — Gewijzigd
    - **primitieve type**: `Surface` → `GM_Surface`

##### `Buurt` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `buurtgeometrie` — Gewijzigd
    - **primitieve type**: `MultiSurface` → `GM_MultiSurface`

##### `GebouwdObject` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `statusVoortgangBouw` — Gewijzigd
    - **enumeratie**: _(leeg)_ → `Enumeratie: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/BAG/Model BAG::statusVoortgangBouw`

##### `Gemeente` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `gemeenteGeometrie` — Gewijzigd
    - **primitieve type**: `Surface` → `GM_Surface`

##### `Ligplaats` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `indicatieGeconstateerdeLigplaats` — Gewijzigd
    - **primitieve type**: `INDIC` → `boolean`

##### `Nummeraanduiding` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `geconstateerd` — Gewijzigd
    - **primitieve type**: `INDIC` → `boolean`
- 🟡 `postcode` — Gewijzigd
    - **primitieve type**: `POSTCODE` → `AN6`

##### `OpenbareRuimte` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `openbareRuimteGeometrie` — Gewijzigd
    - **primitieve type**: `MultiSurface` → `GM_MultiSurface`
- 🟡 `wegsegment` — Gewijzigd
    - **primitieve type**: `Curve` → `GM_Curve`

##### `Pand` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `indicatieGeconstateerdPand` — Gewijzigd
    - **primitieve type**: `INDIC` → `boolean`
- 🟡 `indicatiePlanobject` — Gewijzigd
    - **primitieve type**: `INDIC` → `boolean`
- 🟡 `oorspronkelijkBouwjaarPand` — Gewijzigd
    - **primitieve type**: `JAAR` → `N4`
- 🟡 `pandgeometrieBovenaanzicht` — Gewijzigd
    - **primitieve type**: `Surface` → `GM_Surface`
- 🟡 `pandgeometrieMaaiveld` — Gewijzigd
    - **primitieve type**: `MultiSurface` → `GM_MultiSurface`

##### `Standplaats` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `indicatieGeconstateerdeStandplaats` — Gewijzigd
    - **primitieve type**: `INDIC` → `boolean`

##### `Wijk` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `geometrieWijk` — Gewijzigd
    - **primitieve type**: `MultiSurface` → `GM_MultiSurface`

##### `Woonplaats` — 🟡 Attributen gewijzigd

**Attributen:**

- 🟡 `geometrieWoonplaats` — Gewijzigd
    - **primitieve type**: `Surface` → `GM_Surface`

#### Associaties

- 🟡 Gewijzigd: `BenoemdObject` «is ontstaan uit / overgegaan in» → `BenoemdObject`
  - **src mult. start**: _(leeg)_ → `1`
  - **src mult. end**: _(leeg)_ → `*`
- 🟡 Gewijzigd: `Gemeente` «is overgegaan in» → `Gemeente`
  - **src mult. start**: _(leeg)_ → `1`
  - **src mult. end**: _(leeg)_ → `*`

## Beschrijvende wijzigingen

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel

**Pakket-metadata gewijzigd:**

- **versie**: `2.4.0` → `2.5.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel0-bestuur-politiek-en-ondersteuning"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/0 Bestuur, Politiek en Ondersteuning

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel0-bestuur-politiek-en-ondersteuningburgerzaken"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/0 Bestuur, Politiek en Ondersteuning/Burgerzaken

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel0-bestuur-politiek-en-ondersteuningburgerzakenmodel-burgerzaken"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/0 Bestuur, Politiek en Ondersteuning/Burgerzaken/Model Burgerzaken

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel0-bestuur-politiek-en-ondersteuninggriffie"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/0 Bestuur, Politiek en Ondersteuning/Griffie

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel0-bestuur-politiek-en-ondersteuninggriffiemodel-griffie"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/0 Bestuur, Politiek en Ondersteuning/Griffie/Model Griffie

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.3.0`

#### Classes

##### `Aanwezige Deelnemer` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Agendapunt` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Categorie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Collegelid` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Dossier` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Indiener` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Programma` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Raadscommissie` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `Raadslid` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `Raadsstuk` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.13.0`
- **populatie**: `<memo>` → `<memo>#NOTES#Voor objecttypen die deel uitmaken van een (basis)registratie betreft dit de beschrijving van de exemplaren van het gedefinieerde objecttype die in de desbetreffende (basis)-registratie voorhanden zijn.#NOTES#Voor objecttype…`

##### `Stemming` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Taakveld` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Vergadering` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.14.0`
- **populatie**: `<memo>` → `<memo>#NOTES#Voor objecttypen die deel uitmaken van een (basis)registratie betreft dit de beschrijving van de exemplaren van het gedefinieerde objecttype die in de desbetreffende (basis)-registratie voorhanden zijn.#NOTES#Voor objecttype…`

#### Enumeraties

##### `Deelnemersrol` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `Stemmingsresultaattype` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `Stemmingstype` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel1-veiligheid-en-vergunningen"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/1 Veiligheid en Vergunningen

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel1-veiligheid-en-vergunningenmodel-vth"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/1 Veiligheid en Vergunningen/Model VTH

#### Classes

##### `Activiteit Omgevingswet` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **populatie**: `<memo>` → _(leeg)_

##### `AOMStatus` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`
- **populatie**: `<memo>` → _(leeg)_

##### `Bevinding` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`
- **definitie**: _(leeg)_ → `Een *bevinding* is de uitkomst van een waarneming of onderzoek die aangeeft wat is geconstateerd bij beoordeling of inspectie.`
- **toelichting**: _(leeg)_ → `In algemene en bestuurlijke contexten verwijst *bevinding* naar wat er naar voren komt uit onderzoek, inspectie of waarneming, bijvoorbeeld tijdens een controle, audit of beoordeling van een situatie. Het is het resultaat dat aangeeft wa…`
- **herkomst definitie**: _(leeg)_ → `https://nl.wiktionary.org/wiki/bevinding`
- **populatie**: `<memo>` → _(leeg)_

##### `BOA` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **populatie**: `<memo>` → _(leeg)_

##### `Combibon` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: `Arjen deze  is voor jou` → `Een Combibon is een modelformulier dat handhavende ambtenaren gebruiken om geconstateerde overtredingen en de gekozen afdoeningsmodaliteit (bijv. bekeuring of strafbeschikking) vast te leggen.`
- **toelichting**: _(leeg)_ → `•	Het formulier is opgenomen in de Regeling modellen en formulieren ten behoeve van de handhaving Justitie en kan worden toegepast bij verschillende sanctiemodaliteiten zoals kennisgeving van bekeuring, aankondiging van strafbeschikking …`
- **herkomst**: _(leeg)_ → `https://toezichttafel.wordpress.com/kenniskaart/handhaving-en-interventies/combibon/`
- **herkomst definitie**: _(leeg)_ → `https://toezichttafel.wordpress.com/kenniskaart/handhaving-en-interventies/combibon/`
- **populatie**: `<memo>` → _(leeg)_

##### `Fietsregistratie` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **populatie**: `<memo>` → _(leeg)_

##### `Grondslag` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `Een *grondslag* is de juridische of normatieve basis waarop een besluit, handeling of rechtspraak steunt; het is hetgeen zijn **basis vindt in wetgeving of andere geldende rechtsregels**.`
- **toelichting**: _(leeg)_ → `In (bestuurs)recht en regelgeving verwijst *grondslag* naar de **wet, regel of rechtsbron** waarop een besluit of maatregel is gebaseerd. Het duidt op de formele reden waarom een bestuursorgaan, rechter of andere instantie bevoegd is om …`
- **herkomst definitie**: _(leeg)_ → `https://www.juridischwoordenboek.nl/zoek/grondslag`
- **populatie**: `<memo>` → _(leeg)_

##### `Heffinggrondslag` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **populatie**: `<memo>` → _(leeg)_

##### `Heffingsverordening` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `Een *heffingsverordening* is een door de gemeenteraad vastgestelde verordening die de **heffing en invordering van gemeentelijke belastingen en rechten** regelt, zoals afvalstoffenheffing, precariobelasting of marktgelden.`
- **toelichting**: _(leeg)_ → `Gemeenten mogen alleen heffingen vaststellen binnen de kaders die de wet hen geeft. Een heffingsverordening bevat de regels over **welke belastingen of rechten worden geheven, wie belastingplichtig is, wat de maatstaf en tarieven zijn, e…`
- **herkomst definitie**: _(leeg)_ → `https://www.rijksoverheid.nl/onderwerpen/gemeenten/vraag-en-antwoord/welke-belastingen-heft-de-gemeente`
- **populatie**: `<memo>` → _(leeg)_

##### `Indiener` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **populatie**: `<memo>` → _(leeg)_

##### `Inspectie` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`
- **populatie**: `<memo>` → _(leeg)_

##### `Kosten` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`
- **definitie**: _(leeg)_ → `*Kosten* zijn de prijs of uitgaven die men moet betalen voor het gebruik, verkrijgen of verbruiken van een product, dienst of middel, doorgaans uitgedrukt in geld.`
- **toelichting**: _(leeg)_ → `Het begrip *kosten* verwijst naar wat iemand moet **betalen of besteden** om iets te verkrijgen, te gebruiken of te laten uitvoeren. Kosten kunnen betrekking hebben op directe betalingen, zoals de aanschafprijs van een product of dienst,…`
- **herkomst definitie**: _(leeg)_ → `https://www.ensie.nl/betekenis/kosten`
- **populatie**: `<memo>` → _(leeg)_

##### `Leges_Grondslag` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`
- **definitie**: _(leeg)_ → `*Leges_Grondslag* is de basis of maatstaf waarop de heffing van leges wordt berekend, zoals de omvang van de werkzaamheden, bouwkosten of andere relevante parameters die in de legesverordening zijn vastgelegd.`
- **toelichting**: _(leeg)_ → `In een *legesverordening* van een gemeente of provincie staat welke diensten leges plegen te worden geheven en **op welke grondslagen** dat gebeurt. De grondslag bepaalt de **maatstaf voor de berekening van het legesbedrag** (bijvoorbeel…`
- **herkomst definitie**: _(leeg)_ → `https://www.igg.nl/expertises/leges-kostendekkendheid/grondslag/`
- **populatie**: `<memo>` → _(leeg)_

##### `Ligplaatsontheffing` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **populatie**: `<memo>` → _(leeg)_

##### `MORAanvraagOfMelding` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`
- **definitie**: _(leeg)_ → `*MORAanvraagOfMelding* is een aanvraag of melding die een burger of organisatie doet bij de gemeente om een **situatie in de openbare ruimte te melden of te laten beoordelen**, zoals schade, overlast, gevaarlijke situaties of onderhoudsp…`
- **toelichting**: _(leeg)_ → `In gemeenten wordt met *MORA* (Melding Openbare Ruimte, soms ook Melding Openbare Ruimte Amsterdam) een dienst aangeduid waarbij inwoners, organisaties of bedrijven kunnen doorgeven wat er in de openbare ruimte **niet in orde is** of **o…`
- **herkomst definitie**: _(leeg)_ → `https://www.almere.nl/wonen/beheer-en-onderhoud/melding-openbare-ruimte-mor`
- **populatie**: `<memo>` → _(leeg)_

##### `OpenbareActiviteit` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **populatie**: `<memo>` → _(leeg)_

##### `Precario` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **populatie**: `<memo>` → _(leeg)_

##### `Producttype` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `Een *producttype* is een categorie of variant van producten die dezelfde aard of kenmerken delen, waarmee producten binnen een groep worden ingedeeld op basis van gemeenschappelijke eigenschappen.`
- **toelichting**: _(leeg)_ → `Het begrip *producttype* verwijst naar de classificatie van producten binnen een bepaalde groep of categorie. In economische en administratieve contexten wordt dit gebruikt om producten te onderscheiden en te groeperen, bijvoorbeeld vers…`
- **herkomst definitie**: _(leeg)_ → `https://nl.wikipedia.org/wiki/Producttype`
- **populatie**: `<memo>` → _(leeg)_

##### `SubProducttype` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `*SubProducttype* is een afgeleide of meer specifieke categorie binnen een *Producttype* die producten verder onderscheidt op basis van gedetailleerde kenmerken.`
- **toelichting**: _(leeg)_ → `Waar een *Producttype* een groep varianten van een product beschrijft (bijv. melk als producttype met varianten als magere melk, volle melk enz.) kan een *SubProducttype* een **nog fijnmaziger indeling** zijn binnen dat type. SubProductt…`
- **herkomst definitie**: _(leeg)_ → `https://nl.wikipedia.org/wiki/Producttype`
- **populatie**: `<memo>` → _(leeg)_

##### `Vaartuig` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **populatie**: `<memo>` → _(leeg)_

##### `VOMAanvraagOfMelding` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **populatie**: `<memo>` → _(leeg)_

##### `Vordering` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`
- **definitie**: _(leeg)_ → `Een *vordering* is een juridisch recht dat een schuldeiser heeft om van een andere partij (schuldenaar) een prestatie te ontvangen, zoals een geldbedrag, levering van goederen of uitvoering van een dienst.`
- **toelichting**: _(leeg)_ → `In de juridische context verwijst een vordering naar de **eis of aanspraak** die een persoon of organisatie tegenover een ander heeft op grond van een overeenkomst, wettelijke verplichting of andere rechtsgrond. Een vordering kan bestaan…`
- **herkomst definitie**: _(leeg)_ → `https://incasso.nl/wiki/incassotermen/wat-is-een-vordering`
- **populatie**: `<memo>` → _(leeg)_

##### `Vorderingregel` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `Een *vorderingregel* is een afzonderlijke regel of entry in een gegevensset of lijst die een specifieke *vordering* beschrijft, inclusief kenmerken zoals de omvang, datum, type en status van de vordering.`
- **toelichting**: _(leeg)_ → `In administratieve en financiële gegevensverzamelingen (zoals lijsten van terugvorderingen in het sociaal domein) vormt een *vorderingregel* een enkele record waarin alle relevante gegevens van één specifieke vordering staan. Dit kan bij…`
- **herkomst definitie**: _(leeg)_ → `https://incasso.nl/wiki/incassotermen/wat-is-een-vordering`
- **populatie**: `<memo>` → _(leeg)_

##### `VTH-Melding` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **populatie**: `<memo>` → _(leeg)_

##### `VTHAanvraagOfMelding` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **populatie**: `<memo>` → _(leeg)_

##### `VTHzaak` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`
- **definitie**: _(leeg)_ → `Een *VTHzaak* is een zaak of dossier binnen de gemeentelijke administratie die betrekking heeft op **vergunningverlening, toezicht en handhaving (VTH)** van regels en voorschriften in de fysieke leefomgeving.`
- **toelichting**: _(leeg)_ → `*VTH* staat voor *Vergunningverlening, Toezicht en Handhaving*, de samenhangende taken waarmee gemeenten (en bevoegde overheden) controleren of activiteiten voldoen aan wettelijke eisen, vergunningen verlenen, toezicht houden en handhave…`
- **herkomst definitie**: _(leeg)_ → `Model VTH uit het Gemeentelijk Gegevensmodel (GEMMA/GBI), waarin *VTH* staat voor Vergunning, Toezicht en Handhaving en gekoppeld is aan de registratie van bijbehorende aanvragen of meldingen.`
- **populatie**: `<memo>` → _(leeg)_

##### `Waarneming` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **populatie**: `<memo>` → _(leeg)_

##### `WABOAanvraagOfMelding` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **populatie**: `<memo>` → _(leeg)_

##### `WoonfraudeAanvraagOfMelding` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`
- **populatie**: `<memo>` → _(leeg)_

##### `WoonoverlastAanvraagOfMelding` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`
- **populatie**: `<memo>` → _(leeg)_

#### Enumeraties

##### `Beoordelingsoort` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `Heffingsoort` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `StatusOpenbareActiviteit` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel10-dienstverlening"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/10 Dienstverlening

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel10-dienstverleningdiagram"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/10 Dienstverlening/Diagram

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel10-dienstverleningmodel-dienstverlening"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/10 Dienstverlening/Model Dienstverlening

**Pakket-metadata gewijzigd:**

- **versie**: `1.3` → `1.12.0`

#### Classes

##### `Aanvraagdata` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `crossover` → `Arjen Brienen`

##### `AanvraagOfMelding` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Afspraakstatus` — 🟡 Gewijzigd

- **versie**: `1.7` → `1.14.0`

##### `Artikel` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `crossover` → `Arjen Brienen`

##### `Balieafspraak` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `ExterneBron` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Formuliersoort` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Formuliersoortveld` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `crossover` → `Arjen Brienen`

##### `Klantbeoordeling` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`

##### `Klantbeoordelingreden` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`

##### `MOR-AanvraagOfMelding` — 🟡 Gewijzigd

- **versie**: `1.6` → `1.13.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`

##### `Onderwerp` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `ProductOfDienst` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Telefoononderwerp` — 🟡 Gewijzigd

- **versie**: `1.7` → `1.14.0`

##### `Telefoonstatus` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Telefoontje` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel2-verkeer-vervoer-en-waterstaat"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/2 Verkeer, Vervoer en Waterstaat

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel2-verkeer-vervoer-en-waterstaatmobiliteitmodel-mobiliteit"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/2 Verkeer, Vervoer en Waterstaat/Mobiliteit/Model Mobiliteit

**Pakket-metadata gewijzigd:**

- **versie**: `1.3` → `1.12.0`

#### Classes

##### `Stremming` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Strooidag` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Strooiroute` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `StrooirouteUitvoering` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Verkeersbesluit` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Verkeerstelling` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `VLogInfo` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

#### Enumeraties

##### `Aantal Gehinderden` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `Hindercategorie` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `Hinderklasse` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `Stremmingstatus` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel2-verkeer-vervoer-en-waterstaatparkeren"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/2 Verkeer, Vervoer en Waterstaat/Parkeren

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel2-verkeer-vervoer-en-waterstaatparkerenmodel-parkeren"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/2 Verkeer, Vervoer en Waterstaat/Parkeren/Model Parkeren

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

#### Classes

##### `Belprovider` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `MulderFeit` — 🟡 Gewijzigd

- **versie**: `1.6` → `1.13.0`

##### `Naheffing` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `Parkeergarage` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Parkeerrecht` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Parkeerscan` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Parkeervergunning` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Parkeervlak` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Parkeerzone` — 🟡 Gewijzigd

- **versie**: `1.7` → `1.14.0`

##### `Productgroep` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Productsoort` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Straatsectie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Voertuig` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

#### Enumeraties

##### `Doelgroepenplaatsen` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `Zonesoort` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel3-economie"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/3 Economie

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel3-economiediagram"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/3 Economie/Diagram

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel3-economiemodel-economie"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/3 Economie/Model Economie

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

#### Classes

##### `Contact` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `abrienen` → `Arjen Brienen`

##### `Hotel` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `abrienen` → `Arjen Brienen`

##### `Hotelbezoek` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `abrienen` → `Arjen Brienen`

##### `Verkooppunt` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `abrienen` → `Arjen Brienen`

##### `Werkgelegenheid` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `abrienen` → `Arjen Brienen`

##### `Winkelvloeroppervlak` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `abrienen` → `Arjen Brienen`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel4-onderwijs"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/4 Onderwijs

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel4-onderwijsleerplicht-en-leerlingenvervoer"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/4 Onderwijs/Leerplicht en Leerlingenvervoer

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel4-onderwijsleerplicht-en-leerlingenvervoermodel-leerplicht-en-leerlingenvervoer"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/4 Onderwijs/Leerplicht en Leerlingenvervoer/Model Leerplicht en Leerlingenvervoer

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

#### Classes

##### `Aanvraag Leerlingenvervoer` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `AanvraagOfMelding` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `AanvraagVrijstelling` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Beschikking Leerlingenvervoer` — 🟡 Gewijzigd

- **versie**: `1.7` → `1.14.0`

##### `Beslissing` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `Doorgeleiding OM` — 🟡 Gewijzigd

- **versie**: `1.7` → `1.14.0`

##### `HALT-verwijzing` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Klacht Leerlingenvervoer` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Leerplichtambtenaar` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Procesverbaal Onderwijs` — 🟡 Gewijzigd

- **versie**: `1.7` → `1.14.0`
- **auteur**: `crossover` → `Arjen Brienen`

##### `Verlofaanvraag` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Vervoerder` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Verzuimmelding` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `crossover` → `Arjen Brienen`

##### `Vrijstelling` — 🟡 Gewijzigd

- **versie**: `1.7` → `1.14.0`
- **auteur**: `crossover` → `Arjen Brienen`

##### `Ziekmelding Leerlingenvervoer` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

#### Enumeraties

##### `Sanctiesoort` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `Verzuimsoort` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `Vrijstellingsoort` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel4-onderwijsonderwijs"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/4 Onderwijs/Onderwijs

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel4-onderwijsonderwijsdiagram"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/4 Onderwijs/Onderwijs/Diagram

**Pakket-metadata gewijzigd:**

- **versie**: `1.3` → `1.12.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel4-onderwijsonderwijsmodel-onderwijs"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/4 Onderwijs/Onderwijs/Model Onderwijs

**Pakket-metadata gewijzigd:**

- **versie**: `1.3` → `1.12.0`

#### Classes

##### `Inschrijving` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `crossover` → `Arjen Brienen`

##### `Leerjaar` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `crossover` → `Arjen Brienen`

##### `Leerling` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `Locatie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Loopbaanstap` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `crossover` → `Arjen Brienen`

##### `Onderwijsloopbaan` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `crossover` → `Arjen Brienen`

##### `Onderwijsniveau` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Onderwijssoort` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `crossover` → `Arjen Brienen`

##### `Ouder Of Verzorger` — 🟡 Gewijzigd

- **versie**: `1.7` → `1.14.0`

##### `School` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `crossover` → `Arjen Brienen`

##### `Startkwalificatie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `crossover` → `Arjen Brienen`

##### `Uitschrijving` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `crossover` → `Arjen Brienen`

#### Enumeraties

##### `Onderwijstype` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatie"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatieerfgoedarcheologie"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Erfgoed/Archeologie

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatieerfgoedarcheologiemodel-archeologie"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Erfgoed/Archeologie/Model Archeologie

**Pakket-metadata gewijzigd:**

- **versie**: `1.3` → `1.12.0`

#### Classes

##### `Archeologiebesluit` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Artefact` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `Artefactsoort` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `boring` — 🟡 Gewijzigd

- **versie**: `1.7` → `1.14.0`

##### `Doos` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Kaart` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `locatie` — 🟡 Gewijzigd

- **versie**: `1.7` → `1.14.0`

##### `Magazijnlocatie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Magazijnplaatsing` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Project` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Put` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Spoor` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `Stelling` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `Vindplaats` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `Vlak` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Vondst` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `Vulling` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatieerfgoedarchief"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Erfgoed/Archief

**Pakket-metadata gewijzigd:**

- **versie**: `1.3` → `1.12.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatieerfgoedarchiefmodel-archief"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Erfgoed/Archief/Model Archief

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

#### Classes

##### `Aanvraag` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Archief` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Archiefcategorie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Archiefstuk` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `Auteur` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Bezoeker` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Depot` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `DigitaalBestand` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Indeling` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `Index` — 🟡 Gewijzigd

- **versie**: `1.3` → `1.10.0`

##### `Kast` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Nadere Toegang` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Ordeningsschema` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Plank` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Rechthebbende` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Stelling` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Uitgever` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Vindplaats` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatieerfgoedgenerieke-entiteiten-erfgoed"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Erfgoed/Generieke Entiteiten Erfgoed

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatieerfgoedgenerieke-entiteiten-erfgoeddiagram"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Erfgoed/Generieke Entiteiten Erfgoed/Diagram

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatieerfgoedgenerieke-entiteiten-erfgoedmodel-erfgoed-generiek"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Erfgoed/Generieke Entiteiten Erfgoed/Model Erfgoed Generiek

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

#### Classes

##### `Erfgoed Object` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `Arjen` → `Arjen Brienen`

##### `Historisch Persoon` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `Arjen` → `Arjen Brienen`

##### `Objectclassificatie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `Arjen` → `Arjen Brienen`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatieerfgoedmonumentenmodel-monumenten"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Erfgoed/Monumenten/Model Monumenten

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

#### Classes

##### `Ambacht` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Beschermde Status` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Bouwactiviteit` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Bouwstijl` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Bouwtype` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `OorspronkelijkeFunctie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

#### Enumeraties

##### `TypeMonument` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatiemuseadiagram"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Musea/Diagram

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatiemuseamodel-musea"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Musea/Model Musea

**Pakket-metadata gewijzigd:**

- **versie**: `1.1` → `1.10.0`

#### Classes

##### `Activiteit` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `Arjen` → `Arjen Brienen`

##### `Activiteitsoort` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `Arjen` → `Arjen Brienen`

##### `Balieverkoop` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `Arjen` → `Arjen Brienen`

##### `Balieverkoop Entreekaart` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `Arjen` → `Arjen Brienen`

##### `Belanghebbende` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `Arjen` → `Arjen Brienen`

##### `Bruikleen` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `Arjen` → `Arjen Brienen`

##### `Collectie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `Arjen` → `Arjen Brienen`

##### `Doelgroep` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `Arjen` → `Arjen Brienen`

##### `Entreekaart` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`
- **auteur**: `Arjen` → `Arjen Brienen`

##### `Incident` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `Arjen` → `Arjen Brienen`

##### `Lener` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `Arjen` → `Arjen Brienen`

##### `Mailing` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `Arjen` → `Arjen Brienen`

##### `Museumobject` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `Arjen` → `Arjen Brienen`

##### `Museumrelatie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `Arjen` → `Arjen Brienen`

##### `Omzetgroep` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `Arjen` → `Arjen Brienen`

##### `Prijs` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `Arjen` → `Arjen Brienen`

##### `Product` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `Arjen` → `Arjen Brienen`

##### `Productgroep` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `Arjen` → `Arjen Brienen`

##### `Productie-eenheid` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `Arjen` → `Arjen Brienen`

##### `Programma` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `Arjen` → `Arjen Brienen`

##### `Programmasoort` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `Arjen` → `Arjen Brienen`

##### `Reservering` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `Arjen` → `Arjen Brienen`

##### `Rondleiding` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `Arjen` → `Arjen Brienen`

##### `Samensteller` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `Arjen` → `Arjen Brienen`

##### `Standplaats` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `Arjen` → `Arjen Brienen`

##### `Tentoonstelling` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `Arjen` → `Arjen Brienen`

##### `Voorziening` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `Arjen` → `Arjen Brienen`

##### `Winkelverkoopgroep` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `Arjen` → `Arjen Brienen`

##### `Winkelvoorraaditem` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `Arjen` → `Arjen Brienen`

##### `Zaal` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `Arjen` → `Arjen Brienen`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatiesport"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Sport

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel5-sport-cultuur-en-recreatiesportmodel-sport"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/5 Sport, Cultuur en Recreatie/Sport/Model Sport

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

#### Classes

##### `Belijning` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Bezetting` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Binnenlocatie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Onderhoudskosten` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Sportlocatie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Sportmateriaal` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Sportpark` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `Sportvereniging` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Veld` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domein"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeindak--en-thuislozen"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Dak- en thuislozen

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeindak--en-thuislozendiagram"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Dak- en thuislozen/Diagram

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeindak--en-thuislozenmodel-dak--en-thuislozen"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Dak- en thuislozen/Model Dak- en thuislozen

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

#### Classes

##### `Dakloosheid` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **populatie**: `<memo>` → `<memo>#NOTES#Voor objecttypen die deel uitmaken van een (basis)registratie betreft dit de beschrijving van de exemplaren van het gedefinieerde objecttype die in de desbetreffende (basis)-registratie voorhanden zijn.#NOTES#Voor objecttype…`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeingemeentebegrafenissen"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Gemeentebegrafenissen

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeingemeentebegrafenissenmodel-gemeentebegrafenissen"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Gemeentebegrafenissen/Model Gemeentebegrafenissen

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

#### Classes

##### `Gemeentebegrafenis` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeingeneriek-jeugd-en-wmo"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Generiek Jeugd en Wmo

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeingeneriek-jeugd-en-wmomodel-jeugd-en-wmo-generiek"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Generiek Jeugd en Wmo/Model Jeugd en Wmo Generiek

**Pakket-metadata gewijzigd:**

- **versie**: `1.3` → `1.12.0`

#### Classes

##### `AOM_AanvraagWmoJeugd` — 🟡 Gewijzigd

- **versie**: `1.3` → `1.10.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`
- **definitie**: _(leeg)_ → `*AOM_AanvraagWmoJeugd* is een objecttype in het gegevensmodel voor Wmo en Jeugd dat een **aanvraagtraject voor ondersteuning onder de Wet maatschappelijke ondersteuning (Wmo) en/of Jeugdwet** representeert.`
- **toelichting**: _(leeg)_ → `In het *Model Jeugd en Wmo Generiek* binnen het gemeentelijke gegevenslandschap beschrijft **AOM_AanvraagWmoJeugd** het proces rond een individuele **aanvraag van een cliënt** voor Wmo- en/of jeugdhulpvoorzieningen. Dit omvat gegevens zo…`

##### `AOMMeldingWmoJeugd` — 🟡 Gewijzigd

- **versie**: `1.3` → `1.10.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`
- **definitie**: _(leeg)_ → `*AOMMeldingWMOJeugd* is een objecttype in het gemeentelijk gegevensmodel dat een **melding van een situatie of hulpvraag binnen het kader van de Wet maatschappelijke ondersteuning (Wmo) en/of Jeugdwet** representeert.`
- **toelichting**: _(leeg)_ → `**Toelichting:**   In het *Model Jeugd en Wmo Generiek* komt *AOMMeldingWMOJeugd* voor als één van de kernentiteiten naast *AOM_AanvraagWmoJeugd*. Het type representeert **meldingen die cliënten (of hun vertegenwoordigers/aanmelder) doen…`

##### `Beperking` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Beperkingscategorie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `crossover` → `Arjen Brienen`

##### `Beperkingscore` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Beperkingscoresoort` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `crossover` → `Arjen Brienen`

##### `Beschikking` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Beschikkingsoort` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Beschikte Voorziening` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Budgetuitputting` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Declaratie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`

##### `Declaratieregel` — 🟡 Gewijzigd

- **versie**: `1.3` → `1.10.0`
- **definitie**: _(leeg)_ → `Een *declaratieregel* is de **administratieve regel** waarin het **volume van één product of geleverde prestatie** binnen een bepaalde declaratieperiode voor één cliënt wordt vastgelegd.`
- **toelichting**: _(leeg)_ → `Een declaratieregel vormt een afzonderlijke **regelpost binnen een declaratie** en omvat de specificatie van wat er is geleverd (bijvoorbeeld een zorgprestatie of een dienst), **hoeveelheid/volume** daarvan en de periode waarvoor deze le…`
- **herkomst definitie**: _(leeg)_ → `https://www.istandaarden.nl/over-istandaarden/istandaarden/begrippenlijst`

##### `Leefgebied` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Levering` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `crossover` → `Arjen Brienen`

##### `Leveringsvorm` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `crossover` → `Arjen Brienen`

##### `Melding Eigen bijdrage` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `PGB-Toekenning` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Score` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Scoresoort` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Tarief` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Team` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Toewijzing` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Verplichting Wmo Jeugd` — 🟡 Gewijzigd

- **versie**: `1.3` → `1.10.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`
- **definitie**: _(leeg)_ → `*Verplichting Wmo Jeugd* is de wettelijke plicht van gemeenten om inwoners ondersteuning, hulp of zorg te bieden wanneer zij dat nodig hebben op grond van de Wet maatschappelijke ondersteuning (Wmo) en de Jeugdwet.`
- **toelichting**: _(leeg)_ → `Onder de **Wmo 2015** zijn gemeenten verplicht om **maatschappelijke ondersteuning en jeugdhulp** te bieden aan inwoners die niet op eigen kracht zelfredzaam zijn of ondersteuning nodig hebben om mee te doen in de samenleving. Voor de **…`
- **herkomst definitie**: _(leeg)_ → `https://lokaleregelgeving.overheid.nl/CVDR672737/1`

##### `Verzoek om Toewijzing` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Voorziening` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Voorzieningsoort` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Zelfredzaamheidmatrix` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

#### Enumeraties

##### `Doelgroep` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `Eenheid` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `Frequentie` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `Leveringsvorm` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `Soort Verwijzer` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `Wet` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeininburgeringmodel-inburgering"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inburgering/Model Inburgering

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

#### Classes

##### `Aandachtspunt` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **toelichting**: `<memo>` → `•	Het betreft hier signalen of omstandigheden die invloed kunnen hebben op de voortgang, begeleiding of ondersteuning. 	•	In het model wordt Aandachtspunt gekoppeld aan onder meer de objecttypen Traject en Ondersteuningsactiviteit. 	•	Mo…`
- **populatie**: `<memo>` → _(leeg)_

##### `Aanvraag verlenging Inburgeringstermijn` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **toelichting**: `<memo>` → `•	De aanvraag wordt ingediend bij de gemeente waarin de inburgeringsplichtige woont. 	•	Redenen voor verlenging kunnen onder andere zijn: medische beperkingen, zwangerschap, mantelzorg, psychische problematiek of detentie. 	•	De verlengi…`
- **populatie**: `<memo>` → _(leeg)_

##### `Asielstatushouder` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`

##### `B1-route` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **toelichting**: `<memo>` → `•	De B1-route is bedoeld voor inburgeringsplichtigen die voldoende leervermogen hebben om Nederlands op B1-niveau te leren (Europees Referentiekader). 	•	De route omvat onder andere taallessen, KNM (Kennis van de Nederlandse Maatschappij…`
- **populatie**: `<memo>` → _(leeg)_

##### `Brede Intake` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.3.0`

##### `Diplomawaardering` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Educatie` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Examen` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.3.0`

##### `Examenonderdeel` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.3.0`

##### `Gezinsmigrant en Overige migrant` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.3.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`

##### `Hoofddoel` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **toelichting**: `<memo>` → `•	Het hoofddoel geeft richting aan de inrichting van het persoonlijk plan inburgering en participatie (PIP), zoals bedoeld in artikel 17 van de Wet inburgering 2021. 	•	De gemeente stelt het hoofddoel vast in samenspraak met de inburgeri…`
- **populatie**: `<memo>` → _(leeg)_

##### `ICT-Vaardigheid` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Inburgeraar` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`

##### `InburgeringsAanbod` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Inburgeringsplicht` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Inburgeringstermijn` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Inburgeringstraject` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.3.0`

##### `Introductiemodule` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **toelichting**: `<memo>` → `•	De introductiemodule wordt georganiseerd door de gemeente en dient als startpunt voor het inburgeringstraject (zie artikel 17, tweede lid, van de Wet inburgering 2021). 	•	De module informeert over rechten en plichten, verwachtingen va…`
- **populatie**: `<memo>` → _(leeg)_

##### `Leerroute` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **populatie**: `<memo>` → _(leeg)_

**Attributen:**

- 🟡 `geenLeerbaarheidstoetsZB` — Gewijzigd
    - **definitie**: _(leeg)_ → `<font color="#0e0e0e"><i>Indicator die aangeeft of de leerbaarheidstoets niet is afgenomen vanwege een zintuigelijke beperking van de inburgeraar.</i></font>`

##### `MAP` — 🟡 Gewijzigd

- **versie**: `1.3` → `1.3.0`

##### `Ontheffing` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **toelichting**: `<memo>` → `•	Er zijn verschillende typen ontheffingen binnen de Wet inburgering 2021, onder andere: 	•	Medische ontheffing (artikel 7.4): bij fysieke of psychische belemmeringen; 	•	Ontheffing wegens aantoonbare inspanning (artikel 7.5): als iemand…`
- **populatie**: `<memo>` → _(leeg)_

##### `Ontwikkelwens` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `PIP` — 🟡 Gewijzigd

- **versie**: `1.3` → `1.3.0`

##### `PVT` — 🟡 Gewijzigd

- **versie**: `1.3` → `1.3.0`

##### `Subdoel Aandachtspunt` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Subdoel Ontwikkelwens` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Taalvaardigheid` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **toelichting**: `<memo>` → `•	De Wet inburgering 2021 vereist dat inburgeringsplichtigen taalvaardigheid verwerven op ten minste niveau B1 (B1-route en Onderwijsroute) of niveau A1/A2 (Z-route), afhankelijk van leervermogen en leerroute (artikel 23 van het Besluit …`
- **populatie**: `<memo>` → _(leeg)_

##### `Training` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **toelichting**: `<memo>` → `•	Een training maakt geen verplicht onderdeel uit van het wettelijk minimumaanbod, maar wordt vaak als aanvullende voorziening ingezet door gemeenten, bijvoorbeeld in de Z-route of als maatwerk binnen de B1-route. 	•	Voorbeelden zijn: so…`
- **populatie**: `<memo>` → _(leeg)_

##### `Verblijfplaats AZC` — 🟡 Gewijzigd

- **versie**: `1.2` → `1.3.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`

##### `Verlengingsgrond` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **toelichting**: `<memo>` → `•	De standaard inburgeringstermijn is drie jaar, maar deze kan op verzoek van de inburgeringsplichtige worden verlengd als er sprake is van bijzondere omstandigheden. 	•	Wettelijk geldige verlengingsgronden zijn onder andere: 	•	Zwangers…`
- **populatie**: `<memo>` → _(leeg)_

##### `Voorbereiding op Inburgering` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **toelichting**: `<memo>` → `•	Deze voorbereiding vindt doorgaans plaats tijdens het verblijf in een AZC, nog vóór de inschrijving in de BRP en het officiële begin van de inburgeringstermijn. 	•	Het doel is om inburgeringsplichtigen een betere startpositie te geven …`
- **populatie**: `<memo>` → _(leeg)_

##### `Vreemdeling` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`

##### `Vrijstelling` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Werk` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Z-route` — 🟡 Gewijzigd

- **alias**: `Zelfredzaamheidsroute` → _(leeg)_
- **versie**: `1.2` → `1.2.0`
- **auteur**: `mkampen` → `Eigenaar`
- **definitie**: `<font color="#0e0e0e">De </font><font color="#0e0e0e"><b>Z-route</b></font><font color="#0e0e0e"> (zelfredzaamheidsroute) is &#233;&#233;n van de drie leerroutes binnen het inburgeringsstelsel, bedoeld voor inburgeringsplichtigen met bep…` → `De *Z-route* (Zelfredzaamheidsroute) is een van de drie leerroutes onder de Nederlandse Wet inburgering 2021 en is bedoeld voor inburgeringsplichtigen met een lage leerbaarheid die moeite hebben met het leren van de Nederlandse taal, ger…`
- **toelichting**: `•	De Z-route is bedoeld voor inburgeraars die naar verwachting het taalniveau B1 niet kunnen behalen binnen de gestelde termijn (artikel 18 van de Wet inburgering 2021 en artikel 23 van het Besluit inburgering 2021). 	•	De route richt zi…` → `De Z-route is een intensief traject voor inburgeraars voor wie het behalen van taalniveau B1 of het volgen van een onderwijsroute niet haalbaar wordt geacht. De route omvat minimaal 800 uur Nederlandse taalles inclusief eventuele alfabet…`
- **herkomst definitie**: _(leeg)_ → `https://www.divosa.nl/publicaties/handreiking-leerroutes/de-zelfredzaamheidsroute-z-route/wat-de-z-route`

#### Enumeraties

##### `Aandachtspunt` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `BeoordelingAanvraagVerlenging` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `ClassificatieArmTotUitstekend` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `ClassificatieVoldoendeOnvoldoende` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `Doel` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `EindoordeelVrijstelling` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `Ontwikkelwens` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `Opleidingsniveau` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `ParticipatieDeelname` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `PresentieTaalles` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `SETU job category` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Beroepscategorie&#235;n volgens de SETU-standaard. Voorbeelden: <i>Engineering</i>, <i>Healthcare</i>, <i>ICT</i>.</font>`
- **toelichting**: _(leeg)_ → `#NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Descript…`

##### `SoortWerk` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Soorten werkzaamheden die iemand uitvoert of nastreeft. Voorbeelden: <i>maken</i>, <i>helpen</i>, <i>vervoeren</i>.</font>`
- **toelichting**: _(leeg)_ → `#NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Descript…`

##### `Subdoel betaald werken` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `Subdoel betaald werken met een opleiding` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `Subdoel betaald werken naar vermogen` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `Subdoel digitale vaardigheden` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `Subdoel eenzaamheid` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `Subdoel Financien` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `Subdoel Justitie` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `Subdoel lichamelijke gezondheid` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `Subdoel ondernemen` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `Subdoel opleiding volgen` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `Subdoel passende dagbesteding hebben (maatschappelijk fit worden)` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `Subdoel psychische gezondheid` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `Subdoel Taal` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `Subdoel taalvaardigheden opdoen` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `Subdoel verslaving` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `Subdoel vrijwilligerswerk doen (maatschappelijk fit worden)` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `Subdoel Werkervaring opdoen (werkfit worden)` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `Subdoel Werknemersvaardigheden ontwikkelen (werkfit worden)` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `Subdoel woonsituatie` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `Subdoel zorgtaken` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `UitkomstLeerbaarheidstoets` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `WordtBehandeldAls` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomendienstenmodel-diensten"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Diensten/Model Diensten

#### Classes

##### `Aanvraag` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Aanvraagtype` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Beschikking` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Besluit` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Betalingsblokkade` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Dienst` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Diensttype` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Individuele plicht` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Leveringscomponent` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Leveringscomponenttype` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Leveringsopdracht` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Leveringsspecificatie` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Onderdeel beschikking` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Periodiek dienst Bijz. bijstand` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Recht` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Referteperiode` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Regeling` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Uitsluitingsgrond` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Verstrekkingsvorm` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Voorliggende voorziening` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Voorwaarde` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Voorwaardetype` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomenmodel-inkomen"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Model Inkomen

**Pakket-metadata gewijzigd:**

- **versie**: `1.1.0` → `1.4.0`

#### Classes

##### `Component` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`
- **definitie**: _(leeg)_ → `Een *inkomenscomponent* is een afzonderlijk onderdeel of bron van inkomen, zoals loon, winst uit onderneming, uitkeringen of andere inkomensbronnen, die samen het totale inkomen van een persoon of huishouden vormen.`
- **toelichting**: _(leeg)_ → `In inkomensstatistiek wordt inkomen vaak opgebouwd uit verschillende componenten (zoals arbeid, uitkeringen, kapitaalinkomen, etc.), waarbij elke component een **bron of type inkomen** vertegenwoordigt. Door inkomens te decomponeren in c…`
- **herkomst definitie**: _(leeg)_ → `https://ec.europa.eu/eurostat/cache/metadata/EN/ilc_simsilc_fr.htm (Eurostat – *income components* in de context van inkomensstatistiek)`
- **populatie**: `<memo>` → _(leeg)_

##### `ComponentSoort` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`
- **definitie**: _(leeg)_ → `*ComponentSoort* is de classificatie of het type van een inkomenscomponent binnen een inkomen- of financiële administratie, waarmee wordt bepaald welke categorie of soort een specifieke component behoort.`
- **toelichting**: _(leeg)_ → `In gegevensmodellen zoals het **Gemeentelijk Gegevensmodel (GGM)** maakt *ComponentSoort* het mogelijk inkomens- of financiële componenten verder te categoriseren. Dit helpt bij het structureren, analyseren en rapporteren van verschillen…`
- **populatie**: `<memo>` → _(leeg)_

##### `Huisvestingsoort` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **auteur**: `arjen` → `Arjen Brienen`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Inkomensvoorziening` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **auteur**: `crossover` → `Arjen Brienen`
- **populatie**: `<memo>` → _(leeg)_

##### `Inkomensvoorzieningsoort` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **auteur**: `crossover` → `Arjen Brienen`
- **populatie**: `<memo>` → _(leeg)_

##### `RedenBlokkering` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **auteur**: `arjen` → `Arjen Brienen`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `RedenInstroom` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **auteur**: `arjen` → `Arjen Brienen`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `RedenUitstroom` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **auteur**: `arjen` → `Arjen Brienen`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Regeling` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **auteur**: `crossover` → `Arjen Brienen`
- **populatie**: `<memo>` → _(leeg)_

##### `Regelingsoort` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **auteur**: `crossover` → `Arjen Brienen`
- **populatie**: `<memo>` → _(leeg)_

##### `UitkeringsRun` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`
- **definitie**: _(leeg)_ → `Een *UitkeringsRun* is een geautomatiseerde verwerking in een financieel of administratief systeem waarbij **een groep uitkeringen of betalingen tegelijk wordt berekend en uitgevoerd** als onderdeel van een periodieke batch-verwerking.`
- **toelichting**: _(leeg)_ → `In financiële systemen en salaris-/uitkeringsadministraties verwijst een *run* naar het **proces van uitvoeren van een set berekeningen en betalingen** op een gepland moment (bijv. maandelijks of wekelijks). Een *uitkeringsrun* omvat nor…`
- **herkomst definitie**: _(leeg)_ → `https://onpay.com/glossary/payroll-run/`
- **populatie**: `<memo>` → _(leeg)_

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomennormafwijkingmodel-normafwijking"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Normafwijking/Model Normafwijking

#### Classes

##### `Afwijkende maatregel` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **definitie**: _(leeg)_ → `Een *afwijkende maatregel* is een maatregel die afwijkt van de standaardregel of wettelijke norm en die op basis van een wettelijke grondslag, beleidsregel of gemotiveerde beslissing in een concreet geval wordt toegepast.`
- **toelichting**: `<memo>` → `In de bestuursrechtelijke en juridische context duidt een afwijkende maatregel op een *uitzondering* van de reguliere toepassing van een wettelijke regeling of standaardprocedure, waarbij een bestuursorgaan in bijzondere gevallen kiest v…`
- **herkomst definitie**: _(leeg)_ → `Algemene uitleg bestuursrechtelijke toepassing van afwijkingen van regels in Nederlandse wet- en regelgeving (interpretatie; geen vaste CBS-definitie beschikbaar).`
- **populatie**: `<memo>` → _(leeg)_

##### `Boete` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Maatregel` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **definitie**: _(leeg)_ → `Een *maatregel* is een besluit of handeling waarmee een bestuursorgaan of rechter ingrijpt om een doel te bereiken, een probleem op te lossen of een regel te handhaven.`
- **toelichting**: `<memo>` → `In (bestuurs)recht en beleid duidt *maatregel* op een actie, handeling of besluit van een overheid of instantie dat gericht is op het beïnvloeden van gedrag, de toepassing van regels of de situatie van betrokkenen. Dit kan variëren van e…`
- **herkomst definitie**: _(leeg)_ → `https://www.ensie.nl/meaning/maatregel`
- **populatie**: `<memo>` → _(leeg)_

**Attributen:**

- 🟡 `identificatie` — Gewijzigd
    - **definitie**: _(leeg)_ → `Voorheen: Maatregel ID Opmerking: Attribuut is een identificatie maar van het type Date?`

##### `Maatregel op uitkering` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **definitie**: _(leeg)_ → `Een *maatregel op uitkering* is een sanctie van een uitvoerend orgaan (zoals een gemeente) waarbij de hoogte van een uitkering tijdelijk wordt verlaagd of aangepast omdat de uitkeringsgerechtigde niet heeft voldaan aan de aan de uitkerin…`
- **toelichting**: `<memo>` → `In het kader van bijstandsuitkeringen (Participatiewet/Wet werk en bijstand) kan een maatregel worden toegepast als iemand bijvoorbeeld niet of onvoldoende meewerkt aan verplichtingen zoals het zoeken naar werk of het voldoen aan informa…`
- **herkomst definitie**: _(leeg)_ → `https://lokaleregelgeving.overheid.nl/CVDR210284`
- **populatie**: `<memo>` → _(leeg)_

##### `Normafwijking` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **definitie**: _(leeg)_ → `Een *normafwijking* (in het kader van bijstand) is het constateren dat een bijstandsgerechtigde **afwijkt van de normatieve verplichtingen** die verbonden zijn aan het recht op bijstand (bijv. arbeids- of inlichtingenplicht), wat aanleid…`
- **toelichting**: `<memo>` → `In de uitvoering van de Participatiewet moet een bijstandsgerechtigde voldoen aan verschillende normen en verplichtingen (zoals het zoeken naar werk, voldoen aan inlichtingen- en medewerkingsplichten, of andere door de gemeente opgelegde…`
- **herkomst definitie**: _(leeg)_ → `https://lokaleregelgeving.overheid.nl/CVDR358905/1`
- **populatie**: `<memo>` → _(leeg)_

**Attributen:**

- 🟡 `identificatie` — Gewijzigd
    - **definitie**: _(leeg)_ → `Voorheen: Normafwijking ID Opmerking: Dit attribuut heeft datatype Date maar is een identificatie?`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomenreden-aanvraagreden-aanvraag"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Reden aanvraag/Reden aanvraag

#### Classes

##### `Andere reden afwijkende startdatum` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.2.0`
- **definitie**: _(leeg)_ → `*Andere reden afwijkende startdatum* is een omschrijving van een **reden waarom de startdatum van een dienst of uitkering afwijkt van de standaard startdatum**, voor zover deze reden niet onder de standaardcategorieën valt.`
- **toelichting**: _(leeg)_ → `In het GBI-model voor *Reden aanvraag* geeft *Andere reden afwijkende startdatum* een aanvullende aanduiding van een bijzondere reden waarom de startdatum van een dienst (zoals een uitkering) niet samenvalt met de eerste melding of stand…`

##### `Andere reden verzoek` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.2.0`
- **definitie**: _(leeg)_ → `*Andere reden verzoek* is een categorie voor een **overige reden** waarom een aanvraag wordt gedaan die niet onder de standaard-redencategorieën valt binnen het *Reden aanvraag*-model.`
- **toelichting**: _(leeg)_ → `Binnen het GBI-Ontologiemodel *Reden aanvraag* worden standaardredenen voor een aanvraag (zoals gestopt werk, overlijdenssituaties of veranderingen in inkomenssituaties) onderscheiden. *Andere reden verzoek* omvat **restcategorieën van o…`

##### `Diensten::Aanvraag` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **definitie**: _(leeg)_ → `Een aanvraag is een verzoek van een burger, bedrijf of organisatie aan een overheid om een specifieke dienst te verkrijgen of een besluit te ontvangen (bijv. vergunning, subsidie, paspoort of beschikkingsbesluit).`
- **toelichting**: _(leeg)_ → `•	In de context van diensten bij de overheid betreft een aanvraag het formele indienen van informatie of documenten door een aanvrager zodat de overheid een dienst kan verlenen of een besluit kan nemen. 	•	Diensten omvatten dienstverleni…`
- **herkomst**: _(leeg)_ → `https://www.overheid.nl/help/producten-en-diensten`
- **herkomst definitie**: _(leeg)_ → `https://www.overheid.nl/help/producten-en-diensten`

##### `Diensten::Aanvraag levensonderhoud` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **definitie**: _(leeg)_ → `Een aanvraag levensonderhoud is het formele verzoek van een persoon aan een gemeentelijke of overheidsinstantie om een uitkering of financiële ondersteuning te verkrijgen die het inkomen aanvult zodat in het basislevensonderhoud kan word…`
- **toelichting**: _(leeg)_ → `•	Het begrip verwijst in de praktijk meestal naar de aanvraag van een bijstandsuitkering of andere sociale uitkering die bedoeld is om een tekort aan inkomen voor noodzakelijke kosten van bestaan (zoals voedsel, huisvesting en basisbehoe…`
- **herkomst definitie**: _(leeg)_ → `ttps://www.rijksoverheid.nl/onderwerpen/bijstand/regels-voor-bijstand`

##### `Gestopt betaald werk` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.2.0`
- **definitie**: _(leeg)_ → `*Gestopt betaald werk* is de situatie waarin iemand **zijn of haar betaalde arbeidsrelatie heeft beëindigd**, waardoor het reguliere inkomen uit werk is komen te vervallen en dit relevant is voor de beoordeling van een uitkeringsaanvraag…`
- **toelichting**: _(leeg)_ → `Binnen gemeentelijke inkomens- en bijstandsadministraties (zoals onder de Participatiewet) speelt de situatie *gestopt betaald werk* een rol bij de vaststelling van rechten en verplichtingen. Het duidt op het moment waarop een persoon ni…`

##### `Gestopt of verkocht eigen bedrijf` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.2.0`
- **definitie**: _(leeg)_ → `*Gestopt of verkocht eigen bedrijf* is de situatie waarin een persoon zijn of haar **bedrijf volledig beëindigt of overdraagt/verkoopt**, waardoor de zelfstandige activiteit ophoudt en de reguliere inkomsten uit de onderneming verdwijnen.`
- **toelichting**: _(leeg)_ → `Deze aanduiding wordt gebruikt in inkomens- of uitkeringsadministraties om aan te geven dat iemand **niet langer actief is als ondernemer** doordat het bedrijf is gestopt (bijvoorbeeld definitieve beëindiging van de bedrijfsactiviteiten …`

##### `Gestopte bijstanduitkering` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.2.0`
- **definitie**: _(leeg)_ → `*Gestopte bijstandsuitkering* is een reden van aanvraag binnen de GBI-Ontologie die aanduidt dat een cliënt een inkomensdienst aanvraagt omdat **een eerder ontvangen bijstandsuitkering is beëindigd**.`
- **toelichting**: _(leeg)_ → `Binnen het GBI-model voor *Reden aanvraag* fungeert *Gestopte bijstandsuitkering* als een specifieke **categorie van terugkerende instroomreden**. Het beschrijft de situatie waarin een persoon **weer inkomensondersteuning aanvraagt** nad…`

##### `Gestopte detentie` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.2.0`
- **definitie**: _(leeg)_ → `*Gestopte detentie* is een reden van aanvraag binnen het GBI-model die aangeeft dat een persoon **vrij is gekomen uit detentie**, waardoor de detentie-periode is beëindigd en dit relevant is voor de beoordeling van een nieuwe aanvraag of…`
- **toelichting**: _(leeg)_ → `Binnen het GBI-Ontologiemodel (bijv. *Reden aanvraag* of *Reden instroom*) geeft *Gestopte detentie* aan dat de vorige situatie van detentie **afgelopen is** en dat dit de aanleiding vormt voor een nieuwe aanvraag, bijvoorbeeld voor inko…`

##### `Gestopte of verlaagde alimentatie` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.2.0`
- **definitie**: _(leeg)_ → `*Gestopte of verlaagde alimentatie* is een reden van aanvraag binnen het GBI-Ontologiemodel die aangeeft dat een persoon een inkomensdienst aanvraagt omdat **alimentatiebetalingen zijn gestopt of verlaagd**, waardoor het reguliere onders…`
- **toelichting**: _(leeg)_ → `Binnen het GBI-model *Reden aanvraag* fungeert *Gestopte of verlaagde alimentatie* als een **specifieke instroomreden** voor inkomensondersteuning (zoals bijstand). Het duidt op een situatie waarin alimentatie — bijvoorbeeld partneralime…`

##### `Gestopte studiefinanciering` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.2.0`
- **definitie**: _(leeg)_ → `*Gestopte studiefinanciering* is een reden van aanvraag binnen de GBI-Ontologie die aangeeft dat een persoon een inkomensdienst aanvraagt omdat **de studiefinanciering is beëindigd of gestopt**, waardoor het (studie)inkomen wegvalt en in…`
- **toelichting**: _(leeg)_ → `Binnen het **GBI-model ‘Reden aanvraag’** functioneert *Gestopte studiefinanciering* als een **specifieke subtype-reden** voor het aanvragen van een gemeentelijke inkomensvoorziening (zoals bijstand of andere ondersteuning). De term duid…`

##### `Gestopte uitkering` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.2.0`
- **definitie**: _(leeg)_ → `*Gestopte uitkering* is een subtype van **Reden aanvraag** binnen het GBI-Ontologiemodel dat aangeeft dat een cliënt een inkomensdienst aanvraagt omdat **een eerdere uitkering is beëindigd**, waardoor opnieuw inkomensondersteuning nodig is.`
- **toelichting**: _(leeg)_ → `In het GBI-model *Reden aanvraag* worden meerdere specifieke **aanvraagredenen** onderscheiden om te registreren waarom iemand een inkomensvoorziening aanvraagt. *Gestopte uitkering* duidt op de situatie waarin een vorige uitkering (bijv…`

##### `Ingang bijstandsuitkering` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.7.0`

##### `Levenssituatie::Levenssituatie` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **definitie**: _(leeg)_ → `De levenssituatie is de kwaliteit van de omgeving en omstandigheden waarin een persoon leeft en functioneert op een bepaald moment.`
- **toelichting**: _(leeg)_ → `•	Levenssituatie beschrijft de samenhang van persoonlijke omstandigheden zoals inkomen, woonomgeving, gezinssituatie, gezondheid, werk en sociale relaties die samen de leefwereld van een individu bepalen. 	•	Het begrip wordt gebruikt in …`
- **herkomst definitie**: _(leeg)_ → `https://nl.wiktionary.org/wiki/levenssituatie`

##### `Opname instelling` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.2.0`
- **definitie**: _(leeg)_ → `*Opname instelling* is een reden van aanvraag binnen de GBI-Ontologie die aangeeft dat een persoon een inkomensdienst aanvraagt omdat hij of zij **(net) is opgenomen in of vrijgekomen uit een instelling**, wat financiële gevolgen heeft v…`
- **toelichting**: _(leeg)_ → `Binnen het GBI-model *Reden aanvraag* functioneert *Opname instelling* als een specifieke categorie om vast te leggen dat de aanvraag voor een inkomensvoorziening voortkomt uit een situatie rond verblijf in een **instelling** (bijvoorbee…`

##### `Overleden partner` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.2.0`
- **definitie**: _(leeg)_ → `*Overleden partner* is een subtype van **Reden aanvraag** binnen het GBI-Ontologiemodel dat aangeeft dat een persoon een inkomensdienst aanvraagt omdat **de partner is overleden**, met als gevolg dat het huishoudinkomen is verminderd.`
- **toelichting**: _(leeg)_ → `Binnen het GBI-model *Reden aanvraag* fungeert *Overleden partner* als een specifieke reden voor het aanvragen van een inkomensvoorziening (zoals bijstand of andere ondersteuning). Het duidt op de situatie waarin het overlijden van een p…`

##### `Reden aanvraag Levensonderhoud` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.2.0`
- **definitie**: _(leeg)_ → `*Reden aanvraag Levensonderhoud* is een categorie binnen het GBI-Ontologiemodel die aangeeft dat een cliënt een inkomensdienst aanvraagt vanwege een situatie waarin **middelen voor levensonderhoud ontbreken of zijn weggevallen**, en deze…`
- **toelichting**: _(leeg)_ → `Binnen het GBI-model *Reden aanvraag* worden verschillende specifieke redenen gegroepeerd onder *Levensonderhoud* om vast te leggen waarom een persoon inkomensondersteuning aanvraagt. Dit omvat situaties waarin het inkomen is weggevallen…`

##### `Reden afwijkende startdatum` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.2.0`
- **definitie**: _(leeg)_ → `*Reden afwijkende startdatum* is een categorie binnen het GBI-Ontologiemodel die aangeeft **waarom de ingangsdatum van een dienst of uitkering afwijkt van de standaard startdatum** (bijv. de datum van eerste melding).`
- **toelichting**: _(leeg)_ → `In het **GBI-model *Reden aanvraag*** representeert *Reden afwijkende startdatum* situaties waarin de **startdatum van een dienst (zoals een bijstandsuitkering)** niet samenvalt met de datum van eerste melding of aanvraag. Dit kan bijvoo…`

##### `Verbroken relatie` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.2.0`
- **definitie**: _(leeg)_ → `*Verbroken relatie* is een subtype van **Reden aanvraag** binnen het GBI-Ontologiemodel dat aangeeft dat een persoon een inkomensdienst aanvraagt doordat **de (huwelijkse/samenlevings)relatie is beëindigd**, met financiële gevolgen voor …`
- **toelichting**: _(leeg)_ → `In het GBI-model *Reden aanvraag* representeert *Verbroken relatie* een specifieke reden waarom iemand inkomensondersteuning aanvraagt, namelijk omdat het beëindigen van een relatie (bijvoorbeeld echtscheiding of einde van een geregistre…`

##### `Vertrek uit asielzoekerscentrum` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.2.0`
- **definitie**: _(leeg)_ → `*Vertrek uit asielzoekerscentrum* is een subtype van **Reden aanvraag** in het GBI-Ontologiemodel dat aangeeft dat een persoon een inkomensdienst aanvraagt omdat hij of zij **recentelijk een asielzoekerscentrum heeft verlaten**, waardoor…`
- **toelichting**: _(leeg)_ → `Binnen het GBI-model *Reden aanvraag* functioneert *Vertrek uit asielzoekerscentrum* als een specifieke reden voor het aanvragen van inkomensondersteuning (zoals bijstand). Het duidt op de situatie waarin iemand **niet langer verblijft i…`

##### `Wachten beslissing instantie` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.2.0`
- **definitie**: _(leeg)_ → `*Wachten beslissing instantie* is een subtype van **Reden aanvraag** binnen het GBI-Ontologiemodel dat aangeeft dat een persoon een inkomensdienst aanvraagt omdat hij of zij **moet wachten op een besluit van een externe instantie**, waar…`
- **toelichting**: _(leeg)_ → `Binnen het GBI-model *Reden aanvraag* representeert *Wachten beslissing instantie* een specifieke *Reden afwijkende startdatum*. Het duidt op situaties waarin de ingangsdatum van een bijstandsuitkering of andere inkomensdienst **wordt ui…`

##### `Wachten DigiD` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.2.0`
- **definitie**: _(leeg)_ → `*Wachten DigiD* is een subtype van **Reden afwijkende startdatum** binnen het GBI-Ontologiemodel dat aangeeft dat de ingangsdatum van een inkomensdienst **vertraging oploopt doordat een DigiD nog niet is aangevraagd, geactiveerd of bruik…`
- **toelichting**: _(leeg)_ → `In het **GBI-model *Reden aanvraag*** wordt *Wachten DigiD* gebruikt om te registreren dat de startdatum van een uitkering of andere inkomensdienst **niet gelijk kan zijn aan de datum van eerste melding** omdat de cliënt moet wachten op …`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeininkomenterug--en-invorderingmodel-terug--en-invordering"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Inkomen/Terug- en invordering/Model Terug- en invordering

#### Classes

##### `Aflossing` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Aflossingsafspraak` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Aflossingsplan` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Afschrijving` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Betaalcomponent` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Boetevordering` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Conservatoir beslag` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Correctie` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Debiteur` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Incassokostenvordering` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Interventie` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Interventieverzoek` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Invorderingsbasis` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Krediethypotheek` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Krediethypotheekvordering` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Kwijtschelding` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Leenbijstand` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Leenbijstandvordering` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Loonbeslagafspraak` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Rechtmaand` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Rentevordering` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Restitutie` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Terugvorderingsverzoek` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Uitstel aflossing` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Vermindering terugvordering` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Verrekening` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Verwijtbare vordering` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Vordering` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Vorderingscomponent` — 🟡 Gewijzigd

- **versie**: `1.1.0` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinjeugd"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Jeugd

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinjeugdmodel-jeugd"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Jeugd/Model Jeugd

**Pakket-metadata gewijzigd:**

- **versie**: `1.3` → `1.12.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinjeugdbescherming-en-reclasseringdiagram"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Jeugdbescherming en reclassering/Diagram

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinjeugdbescherming-en-reclasseringmodel-jeugdbescherming"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Jeugdbescherming en reclassering/Model Jeugdbescherming

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

#### Classes

##### `Informering` — 🟡 Gewijzigd

- **versie**: `1.2` → `1.8.0`
- **auteur**: `arjen` → `Arjen Brienen`

##### `Leefgebied` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`
- **auteur**: `arjen` → `Arjen Brienen`

##### `Zorgelijke Situatie` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`
- **auteur**: `arjen` → `Arjen Brienen`

##### `Zorgmelding` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`
- **auteur**: `arjen` → `Arjen Brienen`

#### Enumeraties

##### `Enum Sociale Groep` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `Enum Sociale Relatie` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Incidenttype` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Leefgebied` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Verzoeksoort` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinschuldenschuldhulpverleningmodel-schuldhulpverlening"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Schulden/Schuldhulpverlening/Model Schuldhulpverlening

**Pakket-metadata gewijzigd:**

- **versie**: `1.3` → `1.12.0`

#### Classes

##### `Aanmelding` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `arjen` → `Arjen Brienen`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Begeleiding` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `arjen` → `Arjen Brienen`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Begeleidingssoort` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `arjen` → `Arjen Brienen`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Contactpersoon` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `arjen` → `Arjen Brienen`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Crisisinterventie` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `arjen` → `Arjen Brienen`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `InformatieEnAdvies` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `arjen` → `Arjen Brienen`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `https://www.nvvk.nl/kennisbank-detail/2022/04/20/Module-Informatie--Advies?originNode=1401` → `https://www.nvvk.nl/kennisbank-detail/2022/04/20/Module-Informatie--Advies?originNode=1401#NOTES#Description: De registratie of het informatiemodel waaraan het modelelement ontleend is dan wel de eigen organisatie indien het door de eige…`
- **populatie**: `<memo>` → _(leeg)_

##### `Inkomen` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `arjen` → `Arjen Brienen`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Intake` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `arjen` → `Arjen Brienen`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Leefsituatie` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **populatie**: `<memo>` → _(leeg)_

##### `Moratorium` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `arjen` → `Arjen Brienen`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Nazorg` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `arjen` → `Arjen Brienen`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Ondernemer` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `arjen` → `Arjen Brienen`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Oplossing` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `arjen` → `Arjen Brienen`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Oplossingssoort` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `arjen` → `Arjen Brienen`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Partner` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `arjen` → `Arjen Brienen`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `PlanVanAanpak` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `arjen` → `Arjen Brienen`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Schuld` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `arjen` → `Arjen Brienen`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Schuldeiser` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `arjen` → `Arjen Brienen`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Schuldhulporganisatie` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `arjen` → `Arjen Brienen`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Schuldhulptraject` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **populatie**: `<memo>` → _(leeg)_

##### `Schuldregeling` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `arjen` → `Arjen Brienen`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Stabilisatie` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `arjen` → `Arjen Brienen`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Uitstroom` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **populatie**: `<memo>` → _(leeg)_

##### `VoorlopigeVoorziening` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `arjen` → `Arjen Brienen`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Woningbezit` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `arjen` → `Arjen Brienen`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `WSNP-traject` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `arjen` → `Arjen Brienen`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `WSNP-verklaring` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `arjen` → `Arjen Brienen`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

#### Enumeraties

##### `EnumBegeleidingssoort` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `EnumBeschikkingssoort` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `EnumHuishoudenssoort` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `EnumOplossingssoort` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `EnumSchuldensoort` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `EnumUitstroomreden` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

##### `EnumWoningbezit` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinschuldenvroegsignaleringmodel-vroegsignalering"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Schulden/Vroegsignalering/Model Vroegsignalering

#### Classes

##### `AanleverendeOrganisatie` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `arjen` → `Arjen Brienen`
- **definitie**: _(leeg)_ → `Organisatie de data aanlevert aan het CBS. Het kan hier gaan om de gemeente zelf, of een partij die namens de gemeente uitvoering geeft aan de afhandeling van vroegsignalen.`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Contactpersoon` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `arjen` → `Arjen Brienen`
- **definitie**: `Contactpersoon van een organisatie` → `Contactpersoon bij de aanleverende organisatie.`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Contactpoging` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `arjen` → `Arjen Brienen`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Signaalpartner` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `arjen` → `Arjen Brienen`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Vroegsignaal` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `arjen` → `Arjen Brienen`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Vroegsignaalzaak` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `arjen` → `Arjen Brienen`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

#### Enumeraties

##### `EnumContactsoort` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `arjen` → `Arjen Brienen`

##### `EnumDagdeel` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `arjen` → `Arjen Brienen`

##### `EnumEindresultaat` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `arjen` → `Arjen Brienen`

##### `EnumSignaalpartner` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `arjen` → `Arjen Brienen`

##### `EnumSignaalstatus` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **auteur**: `arjen` → `Arjen Brienen`
- **toelichting**: _(leeg)_ → `#NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding.`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiek"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiekdiagram"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Diagram

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiekmodel-sociaal-domein-generiek"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

#### Classes

##### `AanvraagStadspas` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`
- **auteur**: `crossover` → `Arjen Brienen`

##### `Client` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`

##### `Clientbegeleider` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Gerechtelijke uitspraak` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`
- **auteur**: `arjen` → `Arjen Brienen`

##### `Gezagsverhouding` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`
- **auteur**: `arjen` → `Arjen Brienen`

##### `Huishouden` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`
- **auteur**: `crossover` → `Arjen Brienen`

##### `Incident` — 🟡 Gewijzigd

- **versie**: `1.2` → `1.9.0`
- **auteur**: `arjen` → `Arjen Brienen`
- **definitie**: _(leeg)_ → `Een *incident* is een afzonderlijke gebeurtenis of voorval dat plaatsvindt en kan afwijken van de normale gang van zaken, vaak onverwacht of onvoorzien.`
- **toelichting**: _(leeg)_ → `Het begrip *incident* duidt op een **feitelijke gebeurtenis of voorval** dat is gebeurd en als een op zichzelf staande situatie kan worden beschreven. In algemene taal- en beleidscontexten wordt het gebruikt voor situaties die onverwacht…`
- **herkomst definitie**: _(leeg)_ → `https://www.woorden.org/woord/incident`

##### `Leverancier` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `crossover` → `Arjen Brienen`

##### `Profiel` — 🟡 Gewijzigd

- **versie**: `1.2` → `1.8.0`
- **auteur**: `arjen` → `Arjen Brienen`

##### `Relatie` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `Relatiesoort` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `Sociale Groep` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`
- **auteur**: `arjen` → `Arjen Brienen`

##### `Sociale Relatie` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`
- **auteur**: `arjen` → `Arjen Brienen`

##### `Stadspas` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`
- **auteur**: `crossover` → `Arjen Brienen`
- **definitie**: `Te specifiek, voorstel "gemeentepas"?` → `Te specifiek, voorstel gemeentepas?`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiekmodel-sociaal-domein-generiekinkomsten"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Inkomsten

**Pakket-metadata gewijzigd:**

- **versie**: `1.3` → `1.6.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiekmodel-sociaal-domein-generiekinkomstenmodel-inkomsten"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Inkomsten/Model Inkomsten

#### Classes

##### `Alimentatie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Ander inkomen` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Beslag op inkomen` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Betaald werk` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Dertiende maand - eindejaarsuitkering` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Draagkracht` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Draagkrachtregime` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Eigen bedrijf` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Eigen bijdrage` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Heffingskorting` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Hobby` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Inkomstencomponent` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Inkomstenverhouding` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Inkomstenvermindering` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Kostencomponent` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Loonbeslag` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Maaltijdvergoeding` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Onderhoudsplicht` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Onderhoudsverhouding` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Onkostenvergoeding` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Pensioen` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Primair inkomstencomponent` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Reiskosten naar het werk` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Reiskostenvergoeding` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Secundair inkomstencomponent` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Stage` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Studiefinanciering` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Te betalen alimentatie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Uitkering` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Vakantiegeld` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Vergoeding` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Vergoeding in natura` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Verlaging door boete` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Verlaging door maatregel` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Vrijlating inkomsten` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiekmodel-sociaal-domein-generiekvermogen"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Vermogen

**Pakket-metadata gewijzigd:**

- **versie**: `1.3` → `1.12.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociaal-domein-generiekmodel-sociaal-domein-generiekvermogenmodel-vermogen"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociaal Domein Generiek/Model Sociaal Domein Generiek/Vermogen/Model Vermogen

#### Classes

##### `Bankrekening` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Hypotheek` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Motorvoertuig` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Onroerend goed` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Vermogenscomponent` — 🟡 Gewijzigd

- **versie**: `1.3` → `1.10.0`
- **definitie**: _(leeg)_ → `Een *vermogenscomponent* is een **onderdeel van het totale vermogen** van een persoon of huishouden, dat afzonderlijk wordt weergegeven (zoals spaargeld, beleggingen, eigen woning netto of pensioenvermogen).`
- **toelichting**: _(leeg)_ → `In statistische en economische analyses wordt vermogen gezien als het **saldo van bezittingen minus schulden** van een persoon of huishouden. Het totale vermogen kan worden opgesplitst in verschillende componenten — bijvoorbeeld financië…`
- **herkomst definitie**: _(leeg)_ → `https://www.cbs.nl/nl-nl/onze-diensten/methoden/begrippen/vermogen`

**Attributen:**

- 🟡 `identificatie` — Gewijzigd
    - **definitie**: _(leeg)_ → `Voorheen: Vermogenscomponent ID Attribuut is een identificatie maar van het type Integer?`

##### `Waardepeiling` — 🟡 Gewijzigd

- **versie**: `1.3` → `1.10.0`
- **definitie**: _(leeg)_ → `*Waardepeiling* is een **bepaling of schatting van de waarde van een object, goed of situatie**, verkregen door middel van peiling of inschatting van wat het waard zou zijn.`
- **toelichting**: _(leeg)_ → `De term *waardepeiling* volgt uit de woorddelen: *waarde* (de bepaling van de waarde van iets) en *peiling* (een systematische inschatting of meting). In gebruik (bijvoorbeeld in online fora) betekent het dat iemand vraagt **wat iets vol…`
- **herkomst definitie**: _(leeg)_ → `De betekenis van *waarde* als bepaling van waarde is afgeleid van het lemma *waardebepaling* — de bepaling van de waarde van iets.  [oai_citation:1‡WikiWoordenboek](https://nl.wiktionary.org/wiki/waardebepaling)`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociale-teams"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociale Teams

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinsociale-teamsmodel-sociale-teams"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Sociale Teams/Model Sociale Teams

**Pakket-metadata gewijzigd:**

- **versie**: `1.3` → `1.12.0`

#### Classes

##### `Behandeling` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Behandelsoort` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Bijzonderheid` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Bijzonderheidsoort` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Caseaanmelding` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Doelstelling` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Doelstellingsoort` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `SociaalTeamDossier` — 🟡 Gewijzigd

- **versie**: `1.3` → `1.10.0`
- **definitie**: _(leeg)_ → `SociaalTeamDossier* is een dossier-entiteit binnen het Model Sociale Teams dat de **geïntegreerde registratie van gegevens over ondersteuning, gesprekken, interventies en casusontwikkeling van een sociaal team** voor een inwoner of gezin…`
- **toelichting**: _(leeg)_ → `In het *Model Sociale Teams* van het gemeentelijke gegevenslandschap representeert *SociaalTeamDossier* het **centrale dossier** dat ontstaat rond een casus die een sociaal team oppakt. Sociale teams — zoals wijkteams of gebiedsteams — b…`

##### `SociaalteamDossiersoort` — 🟡 Gewijzigd

- **versie**: `1.3` → `1.10.0`
- **definitie**: _(leeg)_ → `*SociaalteamDossiersoort* is de classificatie van een *SociaalTeamDossier* die aangeeft **het type of de categorie van het dossier** binnen de context van sociale ondersteuning en casemanagement in een sociaal team.`
- **toelichting**: _(leeg)_ → `In het *Model Sociale Teams* van het gemeentelijke gegevenslandschap wordt *SociaalteamDossiersoort* gebruikt om **dossiers van sociale teams te typeren** naar aard of categorie, bijvoorbeeld om verschillende trajecten of casustypen te o…`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinwerk"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Werk

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinwerkmodel-werk"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Werk/Model Werk

#### Classes

##### `Arbeidsmarktkwalificaties` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Een verzameling formele en informele kwalificaties, vaardigheden en eigenschappen die relevant zijn voor de inzetbaarheid van een persoon op de arbeidsmarkt.</font>`

##### `Arbeidsperiode` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Een aaneengesloten periode waarin een persoon arbeid heeft verricht, met begin- en einddatum.</font>`

##### `Arbeidsverhouding` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Een relatie waarin sprake is van afspraken tussen een werknemer en een werkgever over het verrichten van arbeid.</font>`

##### `Arbeidsvermogen` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Een inschatting van wat iemand op basis van fysieke, mentale en sociale capaciteiten aan arbeid kan verrichten.</font>`

##### `Bemiddelingsactiviteit` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Een activiteit in het kader van arbeidstoeleiding waarbij de gemeente of uitvoeringsinstantie gericht handelt om de persoon in contact te brengen met een werkgever of werkplek.</font>`

##### `Bemiddelingsberoep` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Het beoogde beroep waarvoor een persoon wordt begeleid of bemiddeld in een traject.</font>`

##### `Bemiddelingstraject` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Een traject waarin een persoon begeleid wordt naar passend werk, bijvoorbeeld door een gemeente of uitvoeringsinstantie.</font>`

##### `BeschikbaarVoorArbeid` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Een indicatie of iemand op dit moment inzetbaar is voor arbeid, los van begeleiding of ondersteuning.</font>`

##### `BeschikbaarVoorBemiddeling` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Een indicatie dat een persoon beschikbaar is voor bemiddeling richting arbeid, waarbij wordt gekeken naar inzetbaarheid, bereidheid en eventuele beperkingen.</font>`

##### `Doelgroep` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Een specifieke groep personen met gedeelde kenmerken (zoals afstand tot de arbeidsmarkt) die in aanmerking komt voor bepaalde voorzieningen of aangepaste begeleiding.</font>`

##### `Doelgroepenregister` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Een landelijk register waarin mensen met een afstand tot de arbeidsmarkt worden opgenomen, vaak ten behoeve van loonkostensubsidie of andere voorzieningen.</font>`

##### `DoelReintegratievoorziening` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Het beoogde effect van een ingezette voorziening, bijvoorbeeld toeleiding naar werk, dagbesteding of maatschappelijke participatie.</font>`

##### `Flexibliteit` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">De mate waarin een persoon flexibel inzetbaar is qua werktijden, werkplek of werkzaamheden.</font>`

##### `Loonkostensubsidie` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Een tegemoetkoming aan een werkgever voor het in dienst nemen van een werknemer met verminderde loonwaarde.</font>`

##### `Mobiliteit` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">De bereikbaarheid van werkplekken voor een persoon, afhankelijk van vervoermiddel, rijbewijs en fysieke mogelijkheden.</font>`

##### `Ontheffing` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Een formele vrijstelling van verplichtingen rond arbeidsparticipatie, zoals beschikbaarheid of tegenprestatie, op basis van persoonlijke of juridische gronden.</font>`

##### `Opleiding` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Een formeel of informeel leertraject dat een persoon heeft gevolgd met als doel het verwerven van kennis, vaardigheden of competenties.</font>`

##### `Opleidingsnaam` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">De naam waarmee een gevolgde opleiding aangeduid wordt. Dit kan een offici&#235;le (gecodeerde) of vrije tekst zijn.</font>`

##### `OpleidingsnaamGecodeerd` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `Een OpleidingsnaamGecodeerd is een versleutelde/coderende aanduiding van de naam van een opleiding zoals vastgelegd in onderwijs-microdata, bedoeld om de opleiding te identificeren zonder de volledige tekstuele naam direct in de dataset …`
- **toelichting**: _(leeg)_ → `•	Deze variabele representeert de opleidingsnaam in gecodeerde vorm, waarbij de feitelijke naam van de opleiding niet als open tekst in het microdata bestand staat. 	•	De gecodeerde naam wordt gebruikt om consistent te koppelen met refer…`
- **herkomst definitie**: _(leeg)_ → `https://www.cbs.nl/nl-nl/onze-diensten/maatwerk-en-microdata/microdata-zelf-onderzoek-doen/microdatabestanden/gebruikershandleiding-onderwijsinformatie?utm_source=chatgpt.com`

##### `OpleidingsnaamOngecodeerd` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `*OpleidingsnaamOngecodeerd* is de tekstuele naam van een opleiding zoals geregistreerd in CBS-onderwijsdata, weergegeven zonder codering om de opleidingsidentificatie leesbaar te maken.`
- **toelichting**: _(leeg)_ → `In CBS-microdata-bestanden over onderwijs worden opleidingskenmerken vaak vastgelegd via referentietabellen met een opleidingsnummer (bijv. OPLNR) dat gekoppeld kan worden aan meerdere beschrijvende variabelen:   - *OpleidingsnaamOngecod…`
- **herkomst definitie**: _(leeg)_ → `https://www.cbs.nl/-/media/cbs-op-maat/microdatabestanden/documents/2025/08/onderwijsinschrtab.pdf`

##### `Opleidingsniveau` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Het abstractieniveau waarop de opleiding is ingeschaald, vaak gebaseerd op landelijke of Europese onderwijsclassificaties.</font>`

##### `Reintegratievoorziening` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Een voorziening of dienst die wordt ingezet om de kansen van een persoon op arbeidsparticipatie te vergroten.</font>`

##### `Rijbewijs /Certificaat` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Een door een bevoegde instantie afgegeven document dat aangeeft dat een persoon bevoegd is tot het besturen van bepaalde typen voertuigen.</font>`

##### `Taalbeheersing` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Het Europese of Nederlandse taalniveau (zoals A1 t/m C2) waarop de taalvaardigheid van een persoon is ingeschaald.</font>`

##### `TaalbeheersingNederlands` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">De mate waarin een persoon de Nederlandse taal beheerst, inclusief mondelinge en schriftelijke vaardigheden.</font>`

##### `Vaardigheidsvaststelling` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Het proces waarin specifieke vaardigheden van een persoon worden beoordeeld of gemeten, vaak ter ondersteuning van een werkprofiel of plaatsingsbeslissing.</font>`

##### `Voorkeur` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e"><b>Voorkeur</b></font><font color="#0e0e0e"> is een door de klant geuite wens of voorkeur met betrekking tot werk, opleiding of ondersteuning, waarmee bij de invulling van het re-integratie- of participatietraject r…`
- **toelichting**: `•	Een voorkeur kan betrekking hebben op type werkzaamheden, branche, werkomgeving, werktijden, opleidingsrichting of gewenste ondersteuning.` → `•	Een voorkeur kan betrekking hebben op type werkzaamheden, branche, werkomgeving, werktijden, opleidingsrichting of gewenste ondersteuning.#NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of na…`

##### `VrijstellingArbeidsplicht` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Geeft aan of en waarom iemand tijdelijk of structureel is vrijgesteld van de plicht om arbeid te verrichten.</font>`

##### `Werkervaring` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Eerdere functies of werkzaamheden van een persoon, inclusief sector, duur en aard van de werkzaamheden.</font>`

##### `Werkzaamheden als mantelzorger` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Activiteiten die een persoon uitvoert in de rol van mantelzorger, buiten een formele arbeidsverhouding, maar met mogelijke invloed op beschikbaarheid voor arbeid.</font>`

##### `Werkzaamheden anders dan in arbeidsverhouding` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Taken of activiteiten die een persoon verricht zonder dat sprake is van een formele arbeidsovereenkomst, zoals vrijwilligerswerk of mantelzorg.</font>`

##### `Werkzoekende` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Een generiek werkprofiel van een persoon waarin diens arbeidspositie, bemiddelbaarheid en begeleidingsbehoefte worden vastgelegd, als basis voor begeleiding naar arbeid.</font>`

##### `ZelfredzaamheidScore` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Een gekwantificeerde weergave van het niveau van zelfstandigheid van een persoon op meerdere levensgebieden, vaak volgens de methodiek van de ZRM (Zelfredzaamheidsmatrix).</font>`

#### Enumeraties

##### `Code arbeidsvermogen` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Indeling van het arbeidsvermogen van een persoon in functionele categorie&#235;n zoals “kan werken”, “kan beperkt werken”, of “is (tijdelijk) niet inzetbaar voor arbeid”.</font>`
- **toelichting**: _(leeg)_ → `#NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Descript…`

##### `Code maatschappelijke context werkzaamheden anders dan in arbeidsverhouding` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Typologie van werkzaamheden buiten formeel dienstverband, zoals mantelzorg, vrijwilligerswerk of informele zorg.</font>`
- **toelichting**: _(leeg)_ → `#NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Descript…`

##### `Code opleidingsniveau cliënt` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Schatting van het opleidingsniveau van de cli&#235;nt, vaak gebaseerd op zelfrapportage. Voorbeelden: <i>vmbo / praktijkonderwijs</i>, <i>mbo-2</i>, <i>hbo</i>.</font>`
- **toelichting**: _(leeg)_ → `#NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Descript…`

##### `Code tijdsbeslag opleiding` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Geeft aan hoeveel tijd een opleiding per week vraagt, zoals voltijd, deeltijd of duaal.</font>`
- **toelichting**: _(leeg)_ → `#NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Descript…`

##### `CodeLeerwegMBO` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Geeft de leerweg aan binnen het mbo. Voorbeelden: <i>BOL</i>, <i>BBL</i></font>`
- **toelichting**: _(leeg)_ → `#NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Descript…`

##### `CodeNiveauOpleiding` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Opleidingsniveau volgens NLQF/ISCED-systematiek. Voorbeelden: <i>mbo-3</i>, <i>hbo</i>, <i>wo-bachelor</i>.</font>`
- **toelichting**: _(leeg)_ → `#NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Descript…`

##### `CodeOpleidingsnaam` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Gecodeerde of vrije naam van een opleiding. Voorbeeld: <i>Sociaal Werk (mbo-4)</i>.</font>`
- **toelichting**: _(leeg)_ → `#NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Descript…`

##### `CodeSoortOpleidingsnaam` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Geeft het type naamgebruik aan. Voorbeelden: <i>referentie</i>, <i>synoniem</i>.</font>`
- **toelichting**: _(leeg)_ → `#NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Descript…`

##### `CodeStatusOpleiding` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">tatus van de opleiding op het moment van registratie. Waarden zijn onder andere <i>bezig</i>, <i>afgerond</i>, <i>gestopt</i>.</font>`
- **toelichting**: _(leeg)_ → `#NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Descript…`

##### `Dag beschikbaarheid` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Beschikbare dagen in de week voor werk of activiteiten. Voorbeelden: <i>maandag</i>, <i>vrijdag</i>.</font>`
- **toelichting**: _(leeg)_ → `#NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Descript…`

##### `Domein van zelfredzaamheid` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Levensgebied waarop zelfredzaamheid wordt beoordeeld. Voorbeelden: <i>Financi&#235;n</i>, <i>Psychische gezondheid</i>, <i>Dagbesteding</i>.</font>`
- **toelichting**: _(leeg)_ → `#NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Descript…`

##### `Hulp aanwezig` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Geeft aan of er op een domein hulp wordt ontvangen. Waarden zijn: <i>ja</i>, <i>nee</i>, <i>onbekend</i>.</font>`
- **toelichting**: _(leeg)_ → `#NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Descript…`

##### `Indicatie doelgroepenregister` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Geeft aan of iemand valt onder het doelgroepregister voor de banenafspraak. Voorbeelden: <i>Wajong</i>, <i>Participatiewet</i>.</font>`
- **toelichting**: _(leeg)_ → `#NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Descript…`

##### `Indicatie mate van vaardigheid` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Schatting van het vaardigheidsniveau op een bepaald gebied. Voorbeelden: <i>voldoende</i>, <i>goed</i>.</font>`
- **toelichting**: _(leeg)_ → `#NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Descript…`

##### `Interval opzegtermijn` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">De geldende opzegtermijn bij een arbeidsverhouding. Voorbeelden: <i>1 maand</i>, <i>2 weken</i>.</font>`
- **toelichting**: _(leeg)_ → `#NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Descript…`

##### `Kanaal contactmoment` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Het gebruikte communicatiekanaal bij een contactmoment. Voorbeelden: <i>telefoon</i>, <i>email</i>, <i>huisbezoek</i>.</font>`
- **toelichting**: _(leeg)_ → `#NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Descript…`

##### `Ontheffingsverplichting` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Geeft aan of een persoon verplicht is tot arbeidsparticipatie. Voorbeelden: <i>geen ontheffing</i>, <i>medische gronden</i>.</font>`
- **toelichting**: _(leeg)_ → `#NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Descript…`

##### `Opleidingsrichting` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Het vakgebied waarop een opleiding betrekking heeft. </font>`
- **toelichting**: _(leeg)_ → `#NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Descript…`

##### `SETU job category` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Beroepscategorie&#235;n volgens de SETU-standaard. Voorbeelden: <i>Engineering</i>, <i>Healthcare</i>, <i>ICT</i>.</font>`
- **toelichting**: _(leeg)_ → `#NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Descript…`

##### `Soort ontheffing` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Het type ontheffing van arbeidsplicht. Voorbeelden: <i>structureel</i>, <i>tijdelijk</i>.</font>`
- **toelichting**: _(leeg)_ → `#NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Descript…`

##### `SoortWerk` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Soorten werkzaamheden die iemand uitvoert of nastreeft. Voorbeelden: <i>maken</i>, <i>helpen</i>, <i>vervoeren</i>.</font>`
- **toelichting**: _(leeg)_ → `#NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Descript…`

##### `Taalvaardigheid` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Beheersingsniveau van de Nederlandse taal. </font>`
- **toelichting**: _(leeg)_ → `#NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Descript…`

##### `Vervoermiddel` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Beschikbare of gebruikte vervoermiddelen. Voorbeelden: <i>fiets</i>, <i>openbaar vervoer</i>, <i>auto</i>.</font>`
- **toelichting**: _(leeg)_ → `#NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Descript…`

##### `Vervoersmogelijkheden` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Mate waarin iemand zich kan verplaatsen naar werk of activiteiten.</font>`
- **toelichting**: _(leeg)_ → `#NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Descript…`

##### `ZRM-score` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.9.0`
- **definitie**: _(leeg)_ → `<font color="#0e0e0e">Zelfredzaamheidsscore op een domein volgens de ZRM. Voorbeelden: <i>onvoldoende</i>, <i>voldoende</i>, <i>volledig zelfredzaam</i>.</font>`
- **toelichting**: _(leeg)_ → `#NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Description: MIM 1.1: Een inhoudelijke toelichting op de definitie, ter verheldering of nadere duiding. #NOTES#Descript…`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinwmo"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Wmo

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel6-sociaal-domeinwmomodel-wmo"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/6 Sociaal Domein/Wmo/Model Wmo

**Pakket-metadata gewijzigd:**

- **versie**: `1.3` → `1.12.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel7-volksgezondheid-en-milieu"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel7-volksgezondheid-en-milieuafval"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel7-volksgezondheid-en-milieuafvalmodel-afval"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/7 Volksgezondheid en Milieu/Afval/Model Afval

**Pakket-metadata gewijzigd:**

- **versie**: `1.1` → `1.2.0`

#### Classes

##### `Categorie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Container` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Containertype` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Fractie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Locatie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Melding` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Milieustraat` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Ophaalmoment` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Pas` — 🟡 Gewijzigd

- **versie**: `1.7` → `1.14.0`

##### `Prijsafspraak` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Prijsregel` — 🟡 Gewijzigd

- **versie**: `1.3` → `1.10.0`
- **definitie**: _(leeg)_ → `Een *prijsregel* is een **regel die aangeeft hoe de prijs van een product, dienst of prestatie wordt vastgesteld of toegepast**, bijvoorbeeld binnen een declaratie- of tariefstructuur.`
- **toelichting**: _(leeg)_ → `In administratieve en financiële systemen geeft een *prijsregel* aan **welke tarieven of prijsinstellingen** gehanteerd moeten worden voor het berekenen van het te factureren bedrag bij een levering of prestatie. Het kan bijvoorbeeld de …`
- **herkomst definitie**: _(leeg)_ → `https://www.zorgprestatiemodel.nl/content/uploads/2023/07/20230628-Spelregels-correct-registreren-en-declareren_definitief.pdf`

##### `Rit` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Route` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Storting` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Vuilniswagen` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Vulgraadmeting` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

#### Enumeraties

##### `Routesoort` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingbeheer-openbare-ruimte"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Beheer Openbare Ruimte

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingbeheer-openbare-ruimtemodel-basis-imborenumeratiesoort"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Beheer Openbare Ruimte/Model Basis IMBOR/Enumeratiesoort

#### Enumeraties

##### `enum_AanOfVrijliggend` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Afmeting` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Bedienaar` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Beheergebied` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_BeheerobjectGebruiksfunctie` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Belasting` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_BelastingklasseNieuw` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_BelastingklasseOud` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Beleidsstatus` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_BeoogdeOmlooptijd` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Bereikbaarheid` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_BereikbaarheidKolk` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Boombeeld` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Boomgroep` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_BoomhoogteklasseActueel` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_BoomTypeBeschermingsstatusPlus` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Boomveiligheidsklasse` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Boomvoorziening` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_BreedteklasseHaag` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Certificeringsinstantie` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Constructielaagsoort` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Constructietype` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Controlefrequentie` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_CultuurhistorischWaardevol` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Doelsoort` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Fabrikant` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Formaat` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_FunderingLeiding` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Gebiedstype` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_GewenstSluitingspercentage` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Groeifase` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_GroenobjectBereikbaarheidPlus` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Grondsoort` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_GrondsoortPlus` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_HoogteklasseHaag` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_IMKLThema` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Installateur` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Kleur` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_KroondiameterklasseActueel` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_KwaliteitsniveauGewenst` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Kweker` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_LengteKunstgras` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Leverancier` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_LiningType` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Markeringsbreedte` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Markeringsoort` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Markeringspatroon` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Materiaal` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Ondergroei` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Onderhoudsplichtige` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Onderhoudsregime` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Ondersteuningsvorm` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_OriÃ«ntatie` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `enum_OverbruggingsobjectModaliteit` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_PlaatsoriÃ«ntatie` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `enum_RioolputConstructieonderdeel` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Snoeifase` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Soortnaam` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_SoortPlantenbak` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_SoortVoeg` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_SpeelterreinLeeftijdDoelgroep` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_SpeeltoestelToestelonderdeel` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_SportterreinTypeSport` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Stamdiameterklasse` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Status` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_TakvrijeStam` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Taludsteilte` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Toestelgroep` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Type` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_TypeAfdekking` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_TypeAsbesthoudend` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_TypeBediening` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_TypeBeheerder` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_TypeBeheerderPlus` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_TypeBeschermingsstatus` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_TypeBewerking` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_TypeBouwdeel` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_TypeBovenkantKademuur` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_TypeCommunicatie` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_TypeConstructie` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_TypeDeurbediening` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_TypeEigenaar` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_TypeEigenaarPlus` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_TypeElement` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_TypeFundering` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_TypeLigging` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_TypeMantel` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_TypeMonument` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_TypeNivelleerschijf` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_TypeOmgevingsrisicoklasse` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_TypeOnderdeelMetPomp` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_TypePlus` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_TypeSlot` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_TypeStandplaats` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_TypeStandplaatsPlus` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_TypeTeerhoudend` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_TypeVaarwater` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_TypeVermeerderingsvorm` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_TypeVoeg` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_TypeVoegvulling` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_TypeWaaier` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_TypeWaterplant` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Vegen` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Verbindingstype` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_VerhardingsobjectWegfunctie` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Vorm` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_VrijeDoorrijhoogte` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_VrijeTakval` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_VulmateriaalKunstgras` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Waterdoorlatendheid` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_WegasTypeRoute` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_WegcategorieDV` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_WegtypeBestaand` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_Zettingsgevoeligheid` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `enum_ZettingsgevoeligheidPlus` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingbeheer-openbare-ruimtemodel-basis-imbormodel-imbor"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Beheer Openbare Ruimte/Model Basis IMBOR/Model IMBOR

#### Classes

##### `Aansluitput` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Afvalbak` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Bak` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Bank` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Beheerobject` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Bemalingsgebied` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Bergingsbassin` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Boom` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Bord` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Bouwwerk` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Brug` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Drainageput` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Ecoduct` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Fietsparkeervoorziening` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Filterput` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Flyover` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `FunctioneelGebied` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Geluidsscherm` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Gemaal` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Groenobject` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Infiltratieput` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Installatie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Kademuur` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Kast` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Keermuur` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Klimplant` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Kolk` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Kunstwerk` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Leiding` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Leidingelement` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Mast` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Meubilair` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Overbruggingsobject` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Overstortconstructie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Paal` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Pomp` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Put` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Putdeksel` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Rioleringsgebied` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Rioolput` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Scheiding` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Sensor` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `SolitairePlant` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Speelterrein` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Speeltoestel` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Sportterrein` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Stuwgebied` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Terreindeel` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Tunnelobject` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Uitlaatconstructie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Vegetatieobject` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Verhardingsobject` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Verkeersdrempel` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Verlichtingsobject` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Viaduct` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Waterinrichtingsobject` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Waterobject` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Weginrichtingsobject` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingbeheer-openbare-ruimtemodel-beheer-openbare-ruimte"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Beheer Openbare Ruimte/Model Beheer Openbare Ruimte

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

#### Classes

##### `Actie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Areaal` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `CROW-Melding` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `Deelplan/Veld` — 🟡 Gewijzigd

- **versie**: `1.2` → `1.8.0`

##### `Fase/Oplevering` — 🟡 Gewijzigd

- **versie**: `1.2` → `1.8.0`

##### `Geo-Object` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Grondbeheerder` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Inspectie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `KadastraleMutatie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Kwaliteitscatalogus Openbare Ruimte` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Kwaliteitskenmerken` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Logboek` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Melding` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `MeldingOngeval` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `MOOR-melding` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Omgevingsvergunning` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Onderhoud` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Opbreking` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Proces-verbaal-MOOR-melding` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Schouwronde` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Storing` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Taak` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Uitvoerder Graafwerkzaamheden` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Verkeerslicht` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

#### Enumeraties

##### `CROW-Kwaliteitsniveaus` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `Energielabel` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `Oppervlakte Woning` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingbouwen-en-wonen"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Bouwen en Wonen

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingbouwen-en-wonenmodel-wonen"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Bouwen en Wonen/Model Wonen

#### Classes

##### `Gebouw` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Huurwoningen` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Koopwoningen` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Plan` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Projectleider` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Projectontwikkelaar` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Studentenwoningen` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingmeldingen-openbare-ruimte"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Meldingen Openbare Ruimte

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingomgevingswet"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Omgevingswet

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingomgevingswetmodel-omgevingswet"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Omgevingswet/Model Omgevingswet

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingomgevingswetmodel-omgevingswetmodel-aanvragen-en-meldingen"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Omgevingswet/Model Omgevingswet/Model Aanvragen en Meldingen

#### Classes

##### `Bevoegd Gezag` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Gemachtigde` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Initiatiefnemer` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Project` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Projectactiviteit` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Projectlocatie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Specificatie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Uitvoerende instantie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Verzoek` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

#### Enumeraties

##### `Doel verzoek` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `Type Verzoek` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `Vraag Classificatie` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingomgevingswetmodel-omgevingswetmodel-officiele-publicaties"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Omgevingswet/Model Omgevingswet/Model Officiele Publicaties

#### Classes

##### `Omgevingsdocument` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Regeltekst` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingomgevingswetmodel-omgevingswetmodel-omgevingswet"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Omgevingswet/Model Omgevingswet/Model Omgevingswet

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

#### Classes

##### `Activiteit` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Beperkingsgebied` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `Functie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Gebiedsaanwijzing` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Idealisatie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Instructieregel` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Juridische Regel` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Norm` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Normwaarde` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Omgevingsnorm` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Omgevingswaarde` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Omgevingswaarderegel` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Regel voor Iedereen` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Thema` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwingomgevingswetmodel-omgevingswetmodel-toepasbare-regels"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing/Omgevingswet/Model Omgevingswet/Model Toepasbare Regels

#### Classes

##### `Conclusie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Indieningsvereisten` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Maatregelen` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Toepasbare Regel` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `ToepasbareRegelBestand` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Uitvoeringsregel` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatie"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatiefinancien"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/Financien

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatiefinancienmodel-financien"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/Financien/Model Financien

**Pakket-metadata gewijzigd:**

- **versie**: `1.3` → `1.12.0`

#### Classes

##### `Activa` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Activasoort` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Bankafschrift` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Bankafschriftregel` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Bankrekening` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Batch` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Batchregel` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Begroting` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Begrotingregel` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Debiteur` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `Doelstelling` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Factuur` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Factuurregel` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Hoofdrekening` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Hoofdstuk` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Inkooporder` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Kostenplaats` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Mutatie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Opdrachtgever` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Opdrachtnemer` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Product` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Subrekening` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Taakveld` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`

##### `Werkorder` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatiehr"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/HR

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatiehrmodel-hr"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/HR/Model HR

**Pakket-metadata gewijzigd:**

- **versie**: `1.3` → `1.12.0`

#### Classes

##### `Beoordeling` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Declaratie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Declaratiesoort` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Dienstverband` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Disciplinaire Maatregel` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Formatieplaats` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`

##### `Functie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Functiehuis` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `crossover` → `Arjen Brienen`

##### `GenotenOpleiding` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Geweldsincident` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `crossover` → `Arjen Brienen`

##### `Individueel Keuzebudget` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `crossover` → `Arjen Brienen`

##### `Inzet` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`

##### `KeuzebudgetBesteding` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `crossover` → `Arjen Brienen`

##### `KeuzebudgetBestedingsoort` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `crossover` → `Arjen Brienen`

##### `NormProfiel` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`

##### `Onderwijsinstituut` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `Opleiding` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `OrganisatorischeEenheidHR` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`

##### `Relatie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Rol` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`

##### `Sollicitant` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Sollicitatie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `crossover` → `Arjen Brienen`

##### `Sollicitatiegesprek` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `crossover` → `Arjen Brienen`

##### `SoortDisciplinaireMaatregel` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Uren` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Vacature` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `crossover` → `Arjen Brienen`

##### `Verlof` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `crossover` → `Arjen Brienen`

##### `Verlofsoort` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `crossover` → `Arjen Brienen`

##### `Verzuim` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `crossover` → `Arjen Brienen`

##### `Verzuimsoort` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `crossover` → `Arjen Brienen`

##### `Werknemer` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatieict"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/ICT

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatieictmodel-ict"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/ICT/Model ICT

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

#### Classes

##### `Aanvraag` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `Applicatie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Attribuutsoort` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `Classificatie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `CMDB-item` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Database` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Datatype` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Dienst` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Domein/Taakveld` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Externe Bron` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Gebruikerrol` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.1.0`

##### `Gegeven` — 🟡 Gewijzigd

- **versie**: `1.7` → `1.14.0`

##### `Generalisatie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Hardware` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Inventaris` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Koppeling` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Licentie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Linkbaar CMDB-item` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Log` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Melding` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `Nertwerkcomponent` — 🟡 Gewijzigd

- **versie**: `1.3` → `1.10.0`
- **definitie**: _(leeg)_ → `Een *netwerkcomponent* is een hardware- of softwareonderdeel dat een **specifieke functie vervult binnen een netwerk** om communicatie, gegevensuitwisseling of het beheer van netwerkverkeer mogelijk te maken.`
- **toelichting**: _(leeg)_ → `Een netwerk bestaat uit meerdere onderdelen die samenwerken om **gegevens tussen apparaten te versturen, te ontvangen en te beheren**. Dit kunnen fysieke apparaten zijn zoals routers, switches, netwerkkaarten en access points, maar ook s…`
- **herkomst definitie**: _(leeg)_ → `https://www.shiksha.com/online-courses/articles/network-component/`

##### `Notitie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Objecttype` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Onderwerp` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Package` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Prijzenboek` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Product` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Relatiesoort` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Server` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Software` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Storing` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Telefoniegegevens` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Toegangsmiddel` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Versie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Vervoersmiddel` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `Wijzigingsverzoek` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

#### Enumeraties

##### `Applicatiecategorie` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `Beheerstatus` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `Gebruikerrol` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `Packagingstatus` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `Servertypes` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatieinkoop"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/Inkoop

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatieinkoopdiagram"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/Inkoop/Diagram

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatieinkoopmodel-inkoop"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/Inkoop/Model Inkoop

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

#### Classes

##### `Aanbesteding` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `abrienen` → `Arjen Brienen`

##### `Aanbesteding Inhuur` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `abrienen` → `Arjen Brienen`

##### `Aankondiging` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`
- **auteur**: `abrienen` → `Arjen Brienen`

##### `Aanvraag Inkooporder` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `abrienen` → `Arjen Brienen`

##### `Categorie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `abrienen` → `Arjen Brienen`

##### `Contract` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `abrienen` → `Arjen Brienen`

##### `CPV-code` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `abrienen` → `Arjen Brienen`

##### `FormulierInhuur` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `abrienen` → `Arjen Brienen`

##### `FormulierVerlengingInhuur` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `abrienen` → `Arjen Brienen`

##### `Gunning` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `abrienen` → `Arjen Brienen`

##### `Inkooppakket` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`

##### `Inschrijving` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `abrienen` → `Arjen Brienen`

##### `Kandidaat` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`
- **auteur**: `abrienen` → `Arjen Brienen`

##### `Kwalificatie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `abrienen` → `Arjen Brienen`

##### `Leverancier` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Offerte` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `abrienen` → `Arjen Brienen`

##### `Offerteaanvraag` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `abrienen` → `Arjen Brienen`

##### `SelectietabelAanbesteding` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `abrienen` → `Arjen Brienen`

##### `StartformulierAanbesteden` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `abrienen` → `Arjen Brienen`

##### `Uitnodiging` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`
- **auteur**: `abrienen` → `Arjen Brienen`

#### Enumeraties

##### `Aanbestedingsoort` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `Inkooprol` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `Opdrachtcategorie` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `Opdrachtsoort` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatieorganisatie-indelingmodel-organisatie"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/Organisatie-indeling/Model Organisatie

**Pakket-metadata gewijzigd:**

- **versie**: `1.3` → `1.12.0`

#### Classes

##### `Programma` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Project` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatiesubsidies"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/Subsidies

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatiesubsidiesdiagram"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/Subsidies/Diagram

**Pakket-metadata gewijzigd:**

- **versie**: `1.4` → `1.13.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatiesubsidiesmodel-subsidies"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/Subsidies/Model Subsidies

**Pakket-metadata gewijzigd:**

- **versie**: `1.4` → `1.13.0`

#### Classes

##### `Betaalmoment` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`
- **auteur**: `arjen` → `Arjen Brienen`

##### `Rapportagemoment` — 🟡 Gewijzigd

- **versie**: `1.6` → `1.13.0`
- **auteur**: `abrienen` → `Arjen Brienen`

##### `Sector` — 🟡 Gewijzigd

- **versie**: `1.6` → `1.13.0`
- **auteur**: `abrienen` → `Arjen Brienen`

##### `Subsidie` — 🟡 Gewijzigd

- **versie**: `1.6` → `1.13.0`
- **auteur**: `abrienen` → `Arjen Brienen`

##### `Subsidieaanvraag` — 🟡 Gewijzigd

- **versie**: `1.6` → `1.13.0`
- **auteur**: `abrienen` → `Arjen Brienen`

##### `Subsidiebeschikking` — 🟡 Gewijzigd

- **versie**: `1.6` → `1.13.0`
- **auteur**: `abrienen` → `Arjen Brienen`

##### `Subsidiecomponent` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`
- **auteur**: `arjen` → `Arjen Brienen`

##### `Subsidieprogramma` — 🟡 Gewijzigd

- **versie**: `1.6` → `1.13.0`
- **auteur**: `abrienen` → `Arjen Brienen`

##### `Taak` — 🟡 Gewijzigd

- **versie**: `1.6` → `1.13.0`
- **auteur**: `abrienen` → `Arjen Brienen`

#### Enumeraties

##### `Subsidieniveau` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatievastgoed"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/Vastgoed

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.9.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel9-interne-organisatievastgoedmodel-vastgoed"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/9 Interne Organisatie/Vastgoed/Model Vastgoed

**Pakket-metadata gewijzigd:**

- **versie**: `1.3` → `1.12.0`

#### Classes

##### `Aanbesteding Vastgoed` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Adresaanduiding` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `Arjen` → `Arjen Brienen`

##### `Bouwdeel` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Bouwdeelelement` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `CultuurOnbebouwd` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`

##### `Eigenaar` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Gebruiksdoel` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`

##### `Huurder` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Inspectie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `KpBetrokkenBij` — 🟡 Gewijzigd

- **versie**: `1.3` → `1.10.0`

##### `KpOnstaanUit` — 🟡 Gewijzigd

- **versie**: `1.3` → `1.10.0`

##### `LocatieaanduidingWozObject` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`

##### `Locatieonroerendezaak` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`

##### `MJOP` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `MJOP-Item` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `NADAanvullingBRP` — 🟡 Gewijzigd

- **versie**: `1.3` → `1.10.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`

##### `Objectrelatie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Offerte` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Pachter` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Prijzenboekitem` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Vastgoed Contract` — 🟡 Gewijzigd

- **versie**: `1.7` → `1.14.0`

##### `Vastgoedcontractregel` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`

##### `Vastgoedobject` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Verhuurbaar Eenheid` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Werkbon` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `WOZ-Belang` — 🟡 Gewijzigd

- **versie**: `1.6` → `1.13.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`

##### `Zakelijk Recht` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

#### Enumeraties

##### `Energielabel Gebouwen` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `Monumenttypering` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `NEN2767 Conditiescore` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `Objectrelatierol` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `TypeAdresseerbaarObject` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `Zakelijkrecht` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kern"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.7.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernbag"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/BAG

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.7.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernbagmodel-bag"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/BAG/Model BAG

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.7.0`

#### Classes

##### `AdresseerbaarObject` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Buurt` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: _(leeg)_ → `Het betreft hier de in overleg met het CBS bepaalde indeling van wijken in buurten.#NOTES#Het betreft hier de in overleg met het CBS bepaalde indeling van wijken in buurten.#NOTES#Het betreft hier de in overleg met het CBS bepaalde indel…`
- **herkomst**: `IMBAG` → _(leeg)_
- **herkomst definitie**: `IMBAG` → _(leeg)_
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`
- **populatie**: `<memo>` → `<memo>#NOTES#Alleen bestaande buurten maken deel uit van de populatie BUURT. Plantopografie maakt geen onderdeel uit van de populatie.  #NOTES#Alleen bestaande buurten maken deel uit van de populatie BUURT. Plantopografie maakt geen onde…`

##### `Gemeente` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **herkomst**: `Door KING toegevoegd objecttype,ontleend aan het GFO BG (maakt geen deel uit van enige basisregistratie).` → `Door KING toegevoegd objecttype,ontleend aan het GFO BG (maakt geen deel uit van enige basisregistratie).#NOTES#Description: De basisregistratie in wiens catalogus het objecttype is gespecificeerd (oftewel de basisregistratie waar het ob…`
- **herkomst definitie**: `IMBAG` → _(leeg)_
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`
- **populatie**: `<memo>` → _(leeg)_

##### `Ligplaats` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Nummeraanduiding` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Onderzoek` — 🟡 Gewijzigd

- **versie**: `1.0` → `1.7.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `OpenbareRuimte` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

**Attributen:**

- 🟡 `Huisnummerrange even en oneven nummers` — Gewijzigd
    - **definitie**: _(leeg)_ → `Het laagste en het hoogste huisnummer van de objecten waaraan NUMMERAANDUIDINGen zijn toegekend die gerelateerd zijn aan de OPENBARE RUIMTE in die gevallen dat aan één of beide zijden van de OPENBARE RUIMTE zowel even als oneven huisnumm…`
- 🟡 `Huisnummerrange even nummers` — Gewijzigd
    - **definitie**: _(leeg)_ → `Het laagste en het hoogste huisnummer, zijnde even getallen, van de objecten waaraan NUMMERAANDUIDINGen zijn toegekend die gerelateerd zijn aan de OPENBARE RUIMTE en die gelegen zijn aan één van beide zijden van de OPENBARE RUIMTE.`
- 🟡 `Huisnummerrange oneven nummers` — Gewijzigd
    - **definitie**: _(leeg)_ → `Het laagste en het hoogste huisnummer, zijnde oneven getallen, van de objecten waaraan NUMMERAANDUIDINGen zijn toegekend die gerelateerd zijn aan de OPENBARE RUIMTE en die gelegen zijn aan één van beide zijden van de OPENBARE RUIMTE.`

##### `Pand` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Standplaats` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Verblijfsobject` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Wijk` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: _(leeg)_ → `Het betreft hier de in overleg met het CBS bepaalde indeling van de gemeente in wijken. #NOTES#Het betreft hier de in overleg met het CBS bepaalde indeling van de gemeente in wijken. #NOTES#Het betreft hier de in overleg met het CBS bepa…`
- **herkomst**: `IMBAG` → _(leeg)_
- **herkomst definitie**: `IMBAG` → _(leeg)_
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`
- **populatie**: `<memo>` → `<memo>#NOTES#Alleen bestaande wijken maken deel uit van de populatie WIJK. Plantopografie maakt geen onderdeel uit van de populatie.#NOTES#Alleen bestaande wijken maken deel uit van de populatie WIJK. Plantopografie maakt geen onderdeel …`

##### `Woonplaats` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

#### Enumeraties

##### `Boolean` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `gebruiksdoel` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `ontsluitingswijzeVerdieping` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `soortWoonobject` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `statusLigplaats` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `statusNummeraanduiding` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `statusOpenbareRuimte` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `statusPand` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `statusStandplaats` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `statusVerblijfsobject` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `statusVoortgangBouw` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `statusWoonplaats` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `TypeAdresseerbaarObject` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

##### `typeringOpenbareRuimte` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kerndimensiesmodel"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/Dimensies/Model

#### Classes

##### `Periode` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kerngeneriekmodel-generiek"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/Generiek/Model Generiek

#### Classes

##### `Foto` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Gebied` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Gebiedengroep` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Lijn` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Lijnengroep` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Locatie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Punt` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Puntengroep` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Video-opname` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrgbzplus"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RGBZPlus

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.7.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrgbzplusdiagram"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RGBZPlus/Diagram

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.7.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrgbzplusmodel-rgbzenumeratiesoort"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RGBZPlus/Model RGBZ/Enumeratiesoort

#### Enumeraties

##### `Geslachtsaanduiding MEDEWERKER` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `Soorten Klantcontact` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `Vertrouwelijk aanduiding DOCUMENT` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `Vervalreden BESLUIT` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrgbzplusmodel-rgbzgroepattribuutsoort"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RGBZPlus/Model RGBZ/Groepattribuutsoort

#### Classes

##### `AfwijkendBuitenlandsCorrespondentieadresRol` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `AfwijkendCorrespondentiePostadresRol` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `AnderZaakobjectZaak` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `ContactpersoonRol` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `KenmerkenZaak` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `OpschortingZaak` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `VerlengingZaak` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrgbzplusmodel-rgbzmetagegevens"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RGBZPlus/Model RGBZ/Metagegevens

#### Classes

##### `Brondocumenten` — 🟡 Gewijzigd

- **versie**: `1.6` → `1.13.0`

##### `FormeleHistorie` — 🟡 Gewijzigd

- **versie**: `1.6` → `1.13.0`

##### `InOnderzoek` — 🟡 Gewijzigd

- **versie**: `1.6` → `1.13.0`

##### `MaterieleHistorie` — 🟡 Gewijzigd

- **versie**: `1.6` → `1.13.0`

##### `StrijdigheidOfNietigheid` — 🟡 Gewijzigd

- **versie**: `1.6` → `1.13.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrgbzplusmodel-rgbzmodel-kern-rgbz"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RGBZPlus/Model RGBZ/Model Kern RGBZ

#### Classes

##### `Bedrijfsproces` — 🟡 Gewijzigd

- **versie**: `1.7` → `1.14.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`

##### `Bedrijfsprocestype` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`

##### `Besluit` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Besluittype` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Betaling` — 🟡 Gewijzigd

- **versie**: `1.7` → `1.14.0`
- **auteur**: `crossover` → `Arjen Brienen`

##### `Betrokkene` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Deelproces` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`

##### `Deelprocestype` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`

##### `Document` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.11.0`
- **populatie**: `<memo>` → `<memo>#NOTES#Voor objecttypen die deel uitmaken van een (basis)registratie betreft dit de beschrijving van de exemplaren van het gedefinieerde objecttype die in de desbetreffende (basis)-registratie voorhanden zijn.#NOTES#Voor objecttype…`

##### `Documenttype` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `EnkelvoudigDocument` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Heffing` — 🟡 Gewijzigd

- **versie**: `1.7` → `1.14.0`

##### `Identificatiekenmerk` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Klantcontact` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `crossover` → `Arjen Brienen`

##### `Medewerker` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Object` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Offerte` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `abrienen` → `Arjen Brienen`

##### `OrganisatorischeEenheid` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `SamengesteldDocument` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Status` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Statustype` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `VestigingVanZaakbehandelendeOrganisatie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Zaak` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `ZAAK - Origineel` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Zaaktype` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrsgbplus"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.7.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrsgbplusdiagram"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/Diagram

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.7.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrsgbplusdiagram-rsgbcatalogus-rsgbtekenwijze"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/Diagram RSGB/Catalogus RSGB/Tekenwijze

#### Classes

##### `ObjecttypeA` — 🟡 Gewijzigd

- **versie**: `1.3` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → `<memo>#NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #…`

##### `ObjecttypeB` — 🟡 Gewijzigd

- **versie**: `1.3` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → `<memo>#NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #…`

##### `ObjecttypeC` — 🟡 Gewijzigd

- **versie**: `1.3` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → `<memo>#NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #…`

##### `ObjecttypeD` — 🟡 Gewijzigd

- **versie**: `1.3` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → `<memo>#NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #…`

##### `ObjecttypeE` — 🟡 Gewijzigd

- **versie**: `1.3` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → `<memo>#NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #…`

##### `ObjecttypeF` — 🟡 Gewijzigd

- **versie**: `1.3` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → `<memo>#NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #…`

##### `ObjecttypeG` — 🟡 Gewijzigd

- **versie**: `1.3` → `1.10.0`
- **toelichting**: `<memo>` → _(leeg)_
- **populatie**: `<memo>` → `<memo>#NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #NOTES#Default: <memo> #…`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelenumeratiesoort"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Enumeratiesoort

#### Enumeraties

##### `aanduidingEigenaarGebruiker` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `aanduidingInhoudingVermissingReisdocument` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `aangever` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `adelijkeTitel` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `Boolean` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `bouwkundigeBestemming` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `bronAdresBuitenland` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `burgelijkeStaat` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `codeExploitant` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `functieOndersteunendWegdeel` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `functieSpoor` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `functieWeg` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `functieWegPlus` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `fysiekVoorkomenBegroeidTerrein` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `fysiekVoorkomenBegroeidTerreinPlus` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `fysiekVoorkomenOnbegroeidTerrein` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `fysiekVoorkomenOnbegroeidTerreinPlus` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `fysiekVoorkomenOndersteunendWegdeel` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `fysiekVoorkomenOndersteunendWegdeelPlus` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `fysiekVoorkomenWeg` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `fysiekVoorkomenWegPlus` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `gebruiksdoel` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.11.0`

##### `geslacht` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `Gezinsrelatie` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `Huishoudensoort` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `inwinningsmethodeGeometrie` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `inwinningsmethodeOppervlakte` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `naamgebruik` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `ontsluitingswijzeVerdieping` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `predicaat` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `redenEindeRelatie` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `redenWijzigingAdres` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `soortBewind` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `soortBijzondereRechtstoestandNatuurlijkPersoon` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `soortBijzondereRechtstoestandNietNatuurlijkPersoon` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `soortGebruik` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `soortMigratie` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `soortPubliekrechtelijkRechtsvorm` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `soortRechtsvorm` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `soortWoonobject` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `StatLigplaatsStandplaats` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `statusGeoObject` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `statusNummeraanduiding` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `statusOpenbareRuimte` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `statusPand` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `statusVerblijfsobject` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `statusVoortgangBouw` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `statusWoonplaats` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `statusWOZ(Deel)Object` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `statusWOZ-Beschikking` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `typeObjectcode` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `typeOverbrugging` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `typeringAppartementsrechtsplitsing` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `typeringFunctie` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `typeringFunctionaris` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `typeringFunctioneelGebied` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `typeringGebouwinstallatie` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `typeringIngeschrevenNietNatuurlijkPersoon` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `typeringInrichtingselement` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `typeringInrichtingselementPlus` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `typeringKunstwerk` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `typeringOndersteunendWater` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `typeringOpenbareRuimte` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `typeringOverbruggingsdeel` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `typeringOverigBouwwerk` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `typeringOverigeScheiding` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `typeringScheiding` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `typeringVegetatieobject` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `typeringWater` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `typeringWaterPlus` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

##### `typeringZekerheidsrecht` — 🟡 Gewijzigd

- **versie**: `1.4` → `1.10.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelgroepattribuutsoort"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Groepattribuutsoort

#### Classes

##### `Adresaanduiding` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `CorrespondentieadresBuitenland` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `KING` → _(leeg)_
- **herkomst definitie**: `KING` → _(leeg)_

##### `GeboorteIngeschrevenNatuurlijkPersoon` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `BRP` → _(leeg)_
- **herkomst definitie**: `KING o.b.v. BRP` → _(leeg)_
- **datum opname**: `1 november 2008` → `2008-11-01 00:00:00`

##### `GeboorteIngeschrevenPersoon` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `HandelsnamenMaatschappelijkeActiviteit` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `HandelsnamenVestiging` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `KoopsomKadastraleOnroerendeZaak` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `BRK` → _(leeg)_
- **herkomst definitie**: `BRK` → _(leeg)_
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`

##### `LocatieKadastraleOnroerendeZaak` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `KING o.b.v. BRK` → _(leeg)_
- **herkomst definitie**: `KING` → _(leeg)_
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`

##### `MigratieIngeschrevenNatuurlijkPersoon` — 🟡 Gewijzigd

- **versie**: `3.5` → `3.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `BRP` → _(leeg)_
- **herkomst definitie**: `KING op basis van BRP` → _(leeg)_

##### `NaamAanschrijvingNatuurlijkPersoon` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `NaamgebruikNatuurlijkPersoon` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `BRP` → _(leeg)_
- **herkomst definitie**: `KING o.b.v. BRP` → _(leeg)_
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`

##### `NaamNatuurlijkPersoon` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `NationaliteitIngeschrevenNatuurlijkPersoon` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → `<memo>#NOTES#Zie verder de toelichting in de BRP.#NOTES#Zie verder de toelichting in de BRP.#NOTES#Zie verder de toelichting in de BRP.#NOTES#Zie verder de toelichting in de BRP.#NOTES#Zie verder de toelichting in de BRP.#NOTES#Zie verde…`
- **herkomst**: `BRP` → _(leeg)_
- **herkomst definitie**: `KING o.b.v. BRP` → _(leeg)_
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`

##### `NederlandseNationaliteitIngeschrevenPersoon` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `OntbindingHuwelijk/geregistreerdPartnerschap` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `BRP` → _(leeg)_
- **herkomst definitie**: `KING o.b.v. BRP` → _(leeg)_
- **datum opname**: `1 mei 2008` → `1 mei 2016`

##### `OverlijdenIngeschrevenNatuurlijkPersoon` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → `<memo>#NOTES#Zie verder de toelichting in de BRP.#NOTES#Zie verder de toelichting in de BRP.#NOTES#Zie verder de toelichting in de BRP.#NOTES#Zie verder de toelichting in de BRP.#NOTES#Zie verder de toelichting in de BRP.#NOTES#Zie verde…`
- **herkomst**: `BRP` → _(leeg)_
- **herkomst definitie**: `KING o.b.v. BRP` → _(leeg)_
- **datum opname**: `18 november 2008` → `2008-11-18 00:00:00`

##### `OverlijdenIngeschrevenPersoon` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Postadres` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `KING` → _(leeg)_
- **herkomst definitie**: `KING` → _(leeg)_
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`

##### `Rekeningnummer` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `KING` → _(leeg)_
- **herkomst definitie**: `KING` → _(leeg)_

##### `SamengesteldeNaamNatuurlijkPersoon` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → `<memo>#NOTES#Zie de BRP voor verdere toelichting#NOTES#Zie de BRP voor verdere toelichting#NOTES#Zie de BRP voor verdere toelichting#NOTES#Zie de BRP voor verdere toelichting#NOTES#Zie de BRP voor verdere toelichting#NOTES#Zie de BRP voo…`
- **herkomst**: `BRP` → _(leeg)_
- **herkomst definitie**: `KING op basis van BRP` → _(leeg)_
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`

##### `SBIActiviteitVestiging` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `NHR` → _(leeg)_
- **herkomst definitie**: `KING` → _(leeg)_

##### `SluitingOfAangaanHuwelijkOfGeregistreerdPartnerschap` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `BRP` → _(leeg)_
- **herkomst definitie**: `KING o.b.v. BRP` → _(leeg)_
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`

##### `SoortFunctioneelGebied` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `KING` → _(leeg)_
- **herkomst definitie**: `KING` → _(leeg)_

##### `SoortKunstwerk` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `KING` → _(leeg)_
- **herkomst definitie**: `KING` → _(leeg)_

##### `SoortOverigBouwwerk` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `KING` → _(leeg)_
- **herkomst definitie**: `KING` → _(leeg)_

##### `SoortScheiding` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `KING` → _(leeg)_
- **herkomst definitie**: `KING` → _(leeg)_

##### `SoortSpoor` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `KING` → _(leeg)_
- **herkomst definitie**: `KING` → _(leeg)_

##### `SplitsingstekeningReferentie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `KING` → _(leeg)_
- **herkomst definitie**: `KING` → _(leeg)_

##### `VerblijfadresIngeschrevenNatuurlijkPersoon` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `BRP` → _(leeg)_
- **herkomst definitie**: `KING o.b.v. BRP` → _(leeg)_
- **datum opname**: `1 november 2008` → `2008-11-01 00:00:00`

##### `VerblijfadresIngeschrevenPersoon` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `VerblijfBuitenland` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `KING op basis van BRP` → _(leeg)_
- **herkomst definitie**: `KING op basis van BRP` → _(leeg)_
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`

##### `VerblijfBuitenlandSubject` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `VerblijfsrechtIngeschrevenNatuurlijkPersoon` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `BRP` → _(leeg)_
- **herkomst definitie**: `KING op basis van LO BRP` → _(leeg)_

##### `VerstrekkingsbeperkingPartieelIngeschrevenNatuurlijkPersoon` — 🟡 Gewijzigd

- **versie**: `3.5` → `3.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `BRP` → _(leeg)_
- **herkomst definitie**: `KING` → _(leeg)_

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelmodel-kern-rsgb"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Model Kern RSGB

**Pakket-metadata gewijzigd:**

- **versie**: `1.3` → `1.10.0`

#### Classes

##### `Aantekening` — 🟡 Gewijzigd

- **versie**: `1.6` → `1.13.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`

##### `AdresBuitenland` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`

##### `Appartementsrecht` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: _(leeg)_ → `Een aandeel in een recht op een gebouw en daarmee onlosmakelijk verbonden het uitsluitend gebruiksrecht van een bepaald privé-gedeelte in dat gebouw. Dat kan ook een garage of een parkeerplaats zijn. De privé-gedeelten zijn dus niet alti…`
- **herkomst**: `BRK` → _(leeg)_
- **herkomst definitie**: `BRK` → _(leeg)_
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`
- **populatie**: `<memo>` → _(leeg)_

##### `Appartementsrechtsplitsing` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: _(leeg)_ → `Een appartementsrechtsplitsing is een object dat beoogt ten behoeve van een splitsing in appartementsrechten, de in de splitsing betrokken rechten administratief samen te voegen. De appartementsrechtsplitsing omvat het geheel van rechten…`
- **herkomst**: `BRK` → _(leeg)_
- **herkomst definitie**: `BRK` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `BegroeidTerreindeel` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `BGT` → _(leeg)_
- **herkomst definitie**: `BGT` → _(leeg)_
- **populatie**: `<memo>` → `<memo>#NOTES#Begroeid terreindeel objecten met status plan en een einddatum maken geen deel uit van de verzameling begroeide terreindelen.   Zie verder BGT en IMGeo #NOTES#Begroeid terreindeel objecten met status plan en een einddatum ma…`

##### `Briefadres` — 🟡 Gewijzigd

- **versie**: `1.7` → `1.14.0`
- **auteur**: `abrienen` → `Arjen Brienen`

##### `FunctioneelGebied` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `IMGeo` → _(leeg)_
- **herkomst definitie**: `BRT` → _(leeg)_
- **populatie**: `<memo>` → `<memo>#NOTES#Functioneel gebied objecten met status plan en een einddatum maken geen deel uit van de verzameling functionele gebieden.   Zie verder BGT en IMGeo  #NOTES#Functioneel gebied objecten met status plan en een einddatum maken g…`

##### `Gebied` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `GFO BG` → _(leeg)_
- **herkomst definitie**: `GFO BG` → _(leeg)_
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`
- **populatie**: `<memo>` → `<memo>#NOTES#Alleen bestaande buurten maken deel uit van de populatie BUURT. Plantopografie maakt geen onderdeel uit van de populatie.  #NOTES#Alleen bestaande buurten maken deel uit van de populatie BUURT. Plantopografie maakt geen onde…`

##### `Gebouwinstallatie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `IMGeo` → _(leeg)_
- **herkomst definitie**: `CityGML` → _(leeg)_
- **populatie**: `<memo>` → `<memo>#NOTES#Gebouwinstallatie objecten met status plan en een einddatum maken geen deel uit van de verzameling gebouwinstallaties.   Zie ver IMGeo.#NOTES#Gebouwinstallatie objecten met status plan en een einddatum maken geen deel uit va…`

##### `Huishouden` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `IngeschrevenPersoon` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Ingezetene` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Inrichtingselement` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `IMGeo` → _(leeg)_
- **herkomst definitie**: `NEN3610` → _(leeg)_
- **populatie**: `<memo>` → `<memo>#NOTES#Inrichtingselement objecten met status plan en een einddatum maken geen deel uit van de verzameling inrichtingselementen. #NOTES#Inrichtingselement objecten met status plan en een einddatum maken geen deel uit van de verzame…`

##### `KadastraalPerceel` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: _(leeg)_ → `Een KADASTRAAL PERCEEL behoort tezamen met het APPARTEMENTSRECHT tot de generalisatie KADASTRALE ONROERENDE ZAAK.  Percelen worden cartografisch gerepresenteerd door een tweedimensionale vlakbegrenzing. Tussen alle kadastrale percelen in…`
- **herkomst**: `BRK.` → _(leeg)_
- **herkomst definitie**: `KING op basis van BRK` → `KING op basis van BRK#NOTES#Description: Voor objecttypen die deel uitmaken van een basisregistratie is de definitie hieruit overgenomen. De herkomst van de definitie wordt dan ook alleen vermeld indien het een door KING toegevoegd objec…`
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`
- **populatie**: `<memo>` → _(leeg)_

##### `KadastraleOnroerendeZaak` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: _(leeg)_ → `Zie de catalogus BRK. Daarin is sprake van een ‘onroerende zaak’ zijnde een ‘perceel’, ‘appartementsrecht’ of ‘leidingnetwerk’. Geoordeeld is dat alleen de eerste twee objecttypen zodanig van belang zijn voor de gemeentelijke taakuitoefe…`
- **herkomst**: `BRK` → _(leeg)_
- **herkomst definitie**: `KING O.B.V. BRK` → `KING O.B.V. BRK#NOTES#Description: Voor objecttypen die deel uitmaken van een basisregistratie is de definitie hieruit overgenomen. De herkomst van de definitie wordt dan ook alleen vermeld indien het een door KING toegevoegd objecttype …`
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`
- **populatie**: `<memo>` → _(leeg)_

##### `KadastraleOnroerendeZaakAantekening` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: _(leeg)_ → `Toegevoegd ten opzichte van de BRK is de begindatum. Aangezien een aantekening niet gewijzigd kan worden, bepaalt de begin- en einddatum de materiele historie van alle attribuutsoortensoorten. Deze hebben dan ook materiele historie ‘Nee’…`
- **herkomst**: `BRK` → _(leeg)_
- **herkomst definitie**: `BRK` → _(leeg)_
- **datum opname**: `1 november 2008` → `2008-11-01 00:00:00`
- **populatie**: `<memo>` → _(leeg)_

##### `Kunstwerkdeel` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `BGT` → _(leeg)_
- **herkomst definitie**: `IMGeo` → _(leeg)_
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`
- **populatie**: `<memo>` → `<memo>#NOTES#Kunstwerkdeel objecten met status plan en een einddatum maken geen deel uit van de verzameling kunstwerkdelen.   Zie verder BGT en IMGeo.#NOTES#Kunstwerkdeel objecten met status plan en een einddatum maken geen deel uit van …`

##### `MaatschappelijkeActiviteit` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **herkomst**: `NHR` → _(leeg)_
- **herkomst definitie**: `KING o.b.v NHR` → `KING o.b.v NHR#NOTES#Description: Voor objecttypen die deel uitmaken van een basisregistratie is de definitie hieruit overgenomen. De herkomst van de definitie wordt dan ook alleen vermeld indien het een door KING toegevoegd objecttype b…`
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`
- **populatie**: `<memo>` → _(leeg)_

##### `Nationaliteit` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`

##### `NatuurlijkPersoon` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `NietNatuurlijkPersoon` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `OnbegroeidTerreindeel` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `BGT` → _(leeg)_
- **herkomst definitie**: `BGT` → _(leeg)_
- **populatie**: `<memo>` → `<memo>#NOTES#Onbegroeide terreindeel objecten met status plan en een einddatum maken geen deel uit van de verzameling onbegroeide terreindelen.   Zie verder BGT en IMGeo.#NOTES#Onbegroeide terreindeel objecten met status plan en een eind…`

##### `Onbestemd Adres` — 🟡 Gewijzigd

- **versie**: `1.3` → `1.10.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`
- **definitie**: _(leeg)_ → `*Onbestemd Adres* is een adres-aanduiding die officieel door een bevoegde gemeentelijke instantie is vastgelegd, maar waarbij niet kan worden vastgesteld dat het een regulier woon- of verblijfsadres betreft.`
- **toelichting**: _(leeg)_ → `In gemeentelijke en basisregistratiecontexten (zoals in het RSGB/GBI-model en de BAG/BRP-administraties) wordt een *Onbestemd Adres* gebruikt voor adressen die wel geregistreerd zijn, maar **niet eenduidig kunnen worden gekoppeld aan een…`

##### `OndersteunendWaterdeel` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `BGT` → _(leeg)_
- **herkomst definitie**: `BGT` → _(leeg)_
- **populatie**: `<memo>` → `<memo>#NOTES#Ondersteunende waterdeel objecten met status plan en een einddatum maken geen deel uit van de verzameling ondersteunende waterdelen.   Zie verder BGT.#NOTES#Ondersteunende waterdeel objecten met status plan en een einddatum …`

##### `OndersteunendWegdeel` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `BGT` → _(leeg)_
- **herkomst definitie**: `CityGML` → _(leeg)_
- **populatie**: `<memo>` → `<memo>#NOTES#Ondersteunende wegdelen met status plan en een einddatum maken geen deel uit van de verzameling ondersteunend wegdelen.   Zie verder BGT.#NOTES#Ondersteunende wegdelen met status plan en een einddatum maken geen deel uit van…`

##### `Overbruggingsdeel` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `BGT` → _(leeg)_
- **herkomst definitie**: `BGT` → _(leeg)_
- **populatie**: `<memo>` → `<memo>#NOTES#Overbruggingsdeel objecten met status plan en een einddatum maken geen deel uit van de verzameling overbruggingsdelen.   Zie verder IMGeo #NOTES#Overbruggingsdeel objecten met status plan en een einddatum maken geen deel uit…`

##### `OverigBenoemdTerrein` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `Door KING toegevoegd objecttype (maakt geen deel uit van enige basisregistratie).` → `Door KING toegevoegd objecttype (maakt geen deel uit van enige basisregistratie).#NOTES#Description: De basisregistratie in wiens catalogus het objecttype is gespecificeerd (oftewel de basisregistratie waar het objecttype deel van uitmaa…`
- **herkomst definitie**: `KING` → _(leeg)_
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`
- **populatie**: `<memo>` → _(leeg)_

##### `OverigBouwwerk` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `BGT` → _(leeg)_
- **herkomst definitie**: `BGT` → _(leeg)_
- **populatie**: `<memo>` → `<memo>#NOTES#Overige bouwwerk objecten met status plan en een einddatum maken geen deel uit van de verzameling overige bouwwerken.   Zie verder BGT en IMGeo.#NOTES#Overige bouwwerk objecten met status plan en een einddatum maken geen dee…`

##### `OverigeAdresseerbaarObjectAanduiding` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: _(leeg)_ → `Het betreft alle gegevens en relaties van een officieel vastgesteld adres (van een overig gebouwd object of een overig benoemd terrein) zijnde geen NUMMERAANDUIDING zoals deze in de BAG gedefinieerd is. OVERIGE ADRESSEERBAAR OBJECT AANDU…`
- **herkomst**: `Door KING toegevoegd objecttype (maakt geen deel uit van enige basisregistratie).` → `Door KING toegevoegd objecttype (maakt geen deel uit van enige basisregistratie).#NOTES#Description: De basisregistratie in wiens catalogus het objecttype is gespecificeerd (oftewel de basisregistratie waar het objecttype deel van uitmaa…`
- **herkomst definitie**: `KING` → _(leeg)_
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`
- **populatie**: `<memo>` → _(leeg)_

##### `OverigeScheiding` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `IMGeo` → _(leeg)_
- **herkomst definitie**: `IMGeo` → _(leeg)_
- **populatie**: `<memo>` → `<memo>#NOTES#Overige scheidingsobjecten met status plan en een einddatum maken geen deel uit van de verzameling overige scheidingen.   Zie verder IMGeo.#NOTES#Overige scheidingsobjecten met status plan en een einddatum maken geen deel ui…`

##### `OverigGebouwdObject` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `KING` → _(leeg)_
- **herkomst definitie**: `KING` → _(leeg)_
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`
- **populatie**: `<memo>` → `<memo>#NOTES#Is deelpopulatie van OVERIG BOUWWERK#NOTES#Is deelpopulatie van OVERIG BOUWWERK#NOTES#Is deelpopulatie van OVERIG BOUWWERK#NOTES#Is deelpopulatie van OVERIG BOUWWERK#NOTES#Is deelpopulatie van OVERIG BOUWWERK#NOTES#Is deelpo…`

##### `Rechtspersoon` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Reisdocument` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **herkomst**: `BRP` → _(leeg)_
- **herkomst definitie**: `KING` → _(leeg)_
- **datum opname**: `1 mei 2008` → `1 mei 2016`
- **populatie**: `<memo>` → `<memo>#NOTES#Het gaat hier om verstrekte Nederlandse reisdocumenten, zoals een paspoort of identiteitskaart.#NOTES#Het gaat hier om verstrekte Nederlandse reisdocumenten, zoals een paspoort of identiteitskaart.#NOTES#Het gaat hier om ver…`

##### `Scheiding` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `BGT` → _(leeg)_
- **herkomst definitie**: `BGT` → _(leeg)_
- **populatie**: `<memo>` → `<memo>#NOTES#Terreinobjecten met status plan en een einddatum maken geen deel uit van de verzameling scheidingen.   Zie verder BGT en IMGeo.#NOTES#Terreinobjecten met status plan en een einddatum maken geen deel uit van de verzameling sc…`

##### `Spoor` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `BGT` → _(leeg)_
- **herkomst definitie**: `IMGeo` → _(leeg)_
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`
- **populatie**: `<memo>` → `<memo>#NOTES#Spoorobjecten met status plan en een einddatum maken geen deel uit van de verzameling sporen.   Zie verder BGT en IMGeo.#NOTES#Spoorobjecten met status plan en een einddatum maken geen deel uit van de verzameling sporen.   Z…`

##### `Tenaamstelling` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: _(leeg)_ → `Een tenaamstelling heeft betrekking op de eigendom van die Persoon van één Kadastraal object of op een beperkt recht van die Persoon op één Kadastraal object. Met een beperkt recht op een Kadastraal object wordt erfpacht, opstal, e.d. be…`
- **herkomst**: `BRK` → _(leeg)_
- **herkomst definitie**: `BRK` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

##### `Tunneldeel` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `BGT` → _(leeg)_
- **herkomst definitie**: `BGT` → _(leeg)_
- **populatie**: `<memo>` → `<memo>#NOTES#Tunneldeelobjecten met status plan en een einddatum maken geen deel uit van de verzameling tunneldelen.   Zie verder BGT.#NOTES#Tunneldeelobjecten met status plan en een einddatum maken geen deel uit van de verzameling tunne…`

##### `Vegetatieobject` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `IMGeo` → _(leeg)_
- **herkomst definitie**: `CityGML` → _(leeg)_
- **populatie**: `<memo>` → `<memo>#NOTES#Vegetatieobjecten met status plan en een einddatum maken geen deel uit van de verzameling vegetatieobjecten.   Zie verder IMGeo.#NOTES#Vegetatieobjecten met status plan en een einddatum maken geen deel uit van de verzameling…`

##### `Verblijfstitel` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Vestiging` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: _(leeg)_ → `Ofschoon de definitie in het NHR doet vermoeden dat het hier om een ruimtelijk object gaat, beschouwen we een VESTIGING in het RSGB als een specialisatie van SUBJECT. De toelichting in de catalogus NHR lijkt dit te bevestigen: “De vestig…`
- **herkomst**: `NHR` → _(leeg)_
- **herkomst definitie**: `NHR` → _(leeg)_
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`
- **populatie**: `<memo>` → _(leeg)_

##### `Waterdeel` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `BGT` → _(leeg)_
- **herkomst definitie**: `BGT` → _(leeg)_
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`
- **populatie**: `<memo>` → `<memo>#NOTES#Waterdeelobjecten met status plan en een einddatum maken geen deel uit van de verzameling waterdelen.   Zie verder BGT en IMGeo.#NOTES#Waterdeelobjecten met status plan en een einddatum maken geen deel uit van de verzameling…`

##### `Wegdeel` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `BGT` → _(leeg)_
- **herkomst definitie**: `BGT` → _(leeg)_
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`
- **populatie**: `<memo>` → `<memo>#NOTES#Wegdeelobjecten met status plan en een einddatum maken geen deel uit van de verzameling wegdelen  Zie verder BGT en IMGeo.#NOTES#Wegdeelobjecten met status plan en een einddatum maken geen deel uit van de verzameling wegdele…`

##### `WOZ-deelobject` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: _(leeg)_ → `Het betreft zowel (delen van) gebouwde objecten, benoemde terreinen en panden als (delen van) andersoortige objecten. Het is vooral bedoeld om de doorsnede van WOZ-OBJECTen met VERBLIJFSOBJECTen en PANDen te kunnen maken. WOZDEELOBJECT- …`
- **herkomst**: `Gegevenswoordenboek WOZ` → `Gegevenswoordenboek WOZ#NOTES#Description: De basisregistratie in wiens catalogus het objecttype is gespecificeerd (oftewel de basisregistratie waar het objecttype deel van uitmaakt). #NOTES#Description: De basisregistratie in wiens cata…`
- **herkomst definitie**: `Gegevenswoordenboek WOZ` → `Gegevenswoordenboek WOZ#NOTES#Description: Voor objecttypen die deel uitmaken van een basisregistratie is de definitie hieruit overgenomen. De herkomst van de definitie wordt dan ook alleen vermeld indien het een door KING toegevoegd obj…`
- **datum opname**: `1 februari 2008` → `2009-02-02 00:00:00`
- **populatie**: `<memo>` → _(leeg)_

##### `WOZ-object` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: _(leeg)_ → `Dit objecttype komt voort uit de objectafbakeningsvoorschriften van artikel 16 van de Wet WOZ. De unieke identificatie van het WOZ-object is het WOZ-objectnummer. De WOZ-object-aanduiding, een secundaire identificatie, wordt samengesteld…`
- **herkomst**: `BRWOZ` → _(leeg)_
- **herkomst definitie**: `BRWOZ` → _(leeg)_
- **datum opname**: `1 februari 2008` → `2009-02-02 00:00:00`
- **populatie**: `<memo>` → `<memo>#NOTES#De BR WOZ bevat die onroerende zaken als bedoeld in artikel 16 van de wet WOZ waarvoor op grond van artikel 7  Uitvoeringsbesluit kostenverrekening en gegevensuitwisseling Wet waardering onroerende zaken gegevens worden gere…`

##### `WOZ-Waarde` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `BRWOZ` → _(leeg)_
- **herkomst definitie**: `BRWOZ` → _(leeg)_
- **datum opname**: `2 februari 2009` → `2009-02-02 00:00:00`
- **populatie**: `<memo>` → `<memo>#NOTES#De BR WOZ bevat voor alle geregistreerde WOZ-objecten de waarde naar de opeenvolgende waardepeildata, wanneer voor dat WOZ-object en die waardepeildatum een WOZ beschikking is genomen.#NOTES#De BR WOZ bevat voor alle geregis…`

##### `ZakelijkRecht` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: _(leeg)_ → `Zie de catalogus van de BRK. Daarin is sprake van een zowel rechten als zekerheidsrechten op onroerende zaken (zie de toelichting bij KADASTRALE ONROERENDE ZAAK). Geoordeeld is dat alleen de rechten zodanig van belang zijn voor de gemeen…`
- **herkomst**: `BRK` → _(leeg)_
- **herkomst definitie**: `<niet gespecificeerd>` → _(leeg)_
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`
- **populatie**: `<memo>` → _(leeg)_

##### `Zekerheidsrecht` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **herkomst**: `BRK` → _(leeg)_
- **herkomst definitie**: `BRK` → _(leeg)_
- **populatie**: `<memo>` → _(leeg)_

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelreferentielijsten"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Referentielijsten

#### Classes

##### `AanduidingVerblijfsrecht` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **herkomst**: `BRP` → _(leeg)_
- **herkomst definitie**: `KING o.b.v. BRP` → `KING o.b.v. BRP#NOTES#Description: De basisregistratie of het informatiemodel waaruit de definitie is overgenomen dan wel een aanduiding die aangeeft uit welke bronnen de defintie is samengesteld. #NOTES#Description: De basisregistratie …`

##### `AardAantekening` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → `<memo>#NOTES#zie http://www.kadaster.nl/schemas/waardelijsten/AardAantekening#NOTES#zie http://www.kadaster.nl/schemas/waardelijsten/AardAantekening#NOTES#zie http://www.kadaster.nl/schemas/waardelijsten/AardAantekening#NOTES#zie http://…`
- **herkomst**: `BRK` → _(leeg)_
- **herkomst definitie**: `KING` → _(leeg)_

##### `AardFiliatie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `BRK` → _(leeg)_
- **herkomst definitie**: `KING` → _(leeg)_

##### `AardZakelijkRecht` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `BRK` → _(leeg)_
- **herkomst definitie**: `KING` → _(leeg)_

##### `AcademischeTitel` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `AkrKadastraleGemeentecode` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **herkomst**: `BRK` → _(leeg)_
- **herkomst definitie**: `KING` → _(leeg)_

##### `AutoriteitAfgifteNederlandsReisdocument` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `CultuurcodeBebouwd` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **herkomst**: `BRK` → _(leeg)_
- **herkomst definitie**: `KING` → _(leeg)_

##### `CultuurcodeOnbebouwd` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **herkomst**: `BRK` → _(leeg)_
- **herkomst definitie**: `KING` → _(leeg)_

##### `KadastraleGemeente` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **herkomst**: `BRK` → _(leeg)_
- **herkomst definitie**: `KING o.b.v. BRK` → `KING o.b.v. BRK#NOTES#Description: Voor referentielijsten die deel uitmaken van een basisregistratie is de definitie hieruit overgenomen. De herkomst van de definitie wordt dan ook alleen vermeld indien het een door KING toegevoegde refe…`

##### `Land` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `LandOfgebied` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **herkomst**: `GFO BG` → _(leeg)_
- **herkomst definitie**: `GFO BG` → `GFO BG#NOTES#Description: Voor referentielijsten die deel uitmaken van een basisregistratie is de definitie hieruit overgenomen. De herkomst van de definitie wordt dan ook alleen vermeld indien het een door KING toegevoegde referentielij…`
- **datum opname**: `1 november 2008` → `2008-11-01 00:00:00`

##### `Nationaliteit` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Partij` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: _(leeg)_ → `Het gaat hier om partijen die onder andere verantwoordelijk zijn van de bijhouding van gegevens en gekozen kunnen zijn i.v.m. verstrekkingsbeperkingen.  #NOTES#Het gaat hier om partijen die onder andere verantwoordelijk zijn van de bijho…`
- **herkomst**: `BRP` → _(leeg)_
- **herkomst definitie**: `KING o.b.v. BRP` → _(leeg)_

##### `Provincie` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **herkomst**: `GFO BG` → _(leeg)_
- **herkomst definitie**: `GFO BG` → `GFO BG#NOTES#Description: Voor referentielijsten die deel uitmaken van een basisregistratie is de definitie hieruit overgenomen. De herkomst van de definitie wordt dan ook alleen vermeld indien het een door KING toegevoegde referentielij…`
- **datum opname**: `1 november 2008` → `2008-11-01 00:00:00`

##### `RedenVerkrijgingNationaliteit` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **herkomst**: `BRP` → _(leeg)_
- **herkomst definitie**: `KING` → _(leeg)_

##### `RedenVerliesNationaliteit` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **herkomst**: `BRP` → _(leeg)_
- **herkomst definitie**: `KING` → _(leeg)_

##### `Reisdocumentsoort` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `BRP` → _(leeg)_
- **herkomst definitie**: `GBA` → _(leeg)_
- **datum opname**: `1 maart 2009` → `1 mei 2016`

##### `SBIActiviteit` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `CBS` → _(leeg)_
- **herkomst definitie**: `KING o.b.v. CBS` → _(leeg)_

##### `SoortGrootte` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `BRK` → _(leeg)_
- **herkomst definitie**: `KING` → _(leeg)_

##### `SoortWOZObject` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `BRWOZ` → _(leeg)_
- **herkomst definitie**: `KING` → _(leeg)_

##### `Valuta` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

##### `Valutasoort` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `BRK` → _(leeg)_
- **herkomst definitie**: `KING` → _(leeg)_

##### `Verblijfstitel` — 🟡 Gewijzigd

- **versie**: `1.6` → `1.13.0`
- **auteur**: `aashkpour` → `Ashkan Ashkpour`

##### `WOZ-Deelobjectcode` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `BRWOZ` → _(leeg)_
- **herkomst definitie**: `KING` → _(leeg)_

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelrelatieklasse"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/Relatieklasse

#### Classes

##### `LocatieaanduidingAdresWOZObject` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`

<a id="beschrijvend-delfts-gemeentelijk-gegevensmodeldelfts-gemeentelijk-gegevensmodel99-kernrsgbplusrsgb-modelarchiefmodel-kern-rsgb"></a>
### Package: Delfts Gemeentelijk Gegevensmodel/Delfts Gemeentelijk Gegevensmodel/99 Kern/RSGBPlus/RSGB Model/archief/Model Kern RSGB

**Pakket-metadata gewijzigd:**

- **versie**: `1.0` → `1.7.0`

#### Classes

##### `AdresseerbaarObjectAanduiding` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: _(leeg)_ → `Zie de toelichting in de Catalogus BAG. In aanvulling hierop het volgende. Het betreft alle gegevens en relaties van de NUMMERAANDUIDING zoals deze in de BAG gedefinieerd zijn. NUMMERAANDUIDING is gemodelleerd als een specialisatie van A…`
- **herkomst**: `BAG` → _(leeg)_
- **herkomst definitie**: `<niet gespecificeerd>` → _(leeg)_
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`
- **populatie**: `<memo>` → _(leeg)_

##### `BenoemdObject` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: _(leeg)_ → `Het objecttype betreft alle objecten die van een, al dan niet authentieke, nummeraanduiding voorzien worden. Anders gezegd, alle objecten ‘met een adres’. Het is aldus de generalisatie van zowel GEBOUWD OBJECT en BENOEMD TERREIN en daarm…`
- **herkomst**: `KING` → _(leeg)_
- **herkomst definitie**: `KING` → _(leeg)_
- **datum opname**: `1 maart 2009` → `1 mei 2016`
- **populatie**: `<memo>` → _(leeg)_

##### `BenoemdTerrein` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: _(leeg)_ → `Een benoemd terrein is de groepering van de authentieke stand- en ligplaatsen en de overige benoemde terreinen en modelleert daarmee de terreinen op het niveau van stand- en ligplaatsen en daarmee vergelijkbare onbe- en ongebouwde object…`
- **herkomst**: `Door KING toegevoegd objecttype (maakt geen deel uit van enige basisregistratie).` → `Door KING toegevoegd objecttype (maakt geen deel uit van enige basisregistratie).#NOTES#Description: De basisregistratie in wiens catalogus het objecttype is gespecificeerd (oftewel de basisregistratie waar het objecttype deel van uitmaa…`
- **herkomst definitie**: `KING` → _(leeg)_
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`
- **populatie**: `<memo>` → _(leeg)_

##### `Buurt` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: _(leeg)_ → `Het betreft hier de in overleg met het CBS bepaalde indeling van wijken in buurten.#NOTES#Het betreft hier de in overleg met het CBS bepaalde indeling van wijken in buurten.#NOTES#Het betreft hier de in overleg met het CBS bepaalde indel…`
- **herkomst**: `GFO BG` → _(leeg)_
- **herkomst definitie**: `GFO BG` → _(leeg)_
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`
- **populatie**: `<memo>` → `<memo>#NOTES#Alleen bestaande buurten maken deel uit van de populatie BUURT. Plantopografie maakt geen onderdeel uit van de populatie.  #NOTES#Alleen bestaande buurten maken deel uit van de populatie BUURT. Plantopografie maakt geen onde…`

##### `GebouwdObject` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: _(leeg)_ → `Een gebouwd object is de groepering van de authentieke verblijfsobjecten en de overige bouwwerken en modelleert daarmee de gebouwde omgeving op het niveau van het verblijfsobject en daarmee vergelijkbare objecten voor zover dat door de g…`
- **herkomst**: `Door KING toegevoegd objecttype (maakt geen deel uit van enige basisregistratie).` → `Door KING toegevoegd objecttype (maakt geen deel uit van enige basisregistratie).#NOTES#Description: De basisregistratie in wiens catalogus het objecttype is gespecificeerd (oftewel de basisregistratie waar het objecttype deel van uitmaa…`
- **herkomst definitie**: `KING` → _(leeg)_
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`
- **populatie**: `<memo>` → _(leeg)_

##### `Gemeente` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **herkomst**: `Door KING toegevoegd objecttype, ontleend aan het GFO BG (maakt geen deel uit van enige basisregistratie).` → `Door KING toegevoegd objecttype, ontleend aan het GFO BG (maakt geen deel uit van enige basisregistratie).#NOTES#Description: De basisregistratie in wiens catalogus het objecttype is gespecificeerd (oftewel de basisregistratie waar het o…`
- **herkomst definitie**: `GFO BG` → _(leeg)_
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`
- **populatie**: `<memo>` → _(leeg)_

##### `Ligplaats` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `BAG` → _(leeg)_
- **herkomst definitie**: `KING o.b.v. BAG` → _(leeg)_
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`
- **populatie**: `<memo>` → _(leeg)_

##### `Nummeraanduiding` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: _(leeg)_ → `Het betreft de verzameling van, tot de BAG behorende, officieel vastgestelde nummeraanduidingen (van verblijfsobjecten, stand- en ligplaatsen, in de BAG gezamenlijk aangeduid als adresseerbare objecten) en overige, eveneens officieel doo…`
- **herkomst**: `Door KING toegevoegd objecttype (maakt geen deel uit van enige basisregistratie).` → `Door KING toegevoegd objecttype (maakt geen deel uit van enige basisregistratie).#NOTES#Description: De basisregistratie in wiens catalogus het objecttype is gespecificeerd (oftewel de basisregistratie waar het objecttype deel van uitmaa…`
- **herkomst definitie**: `KING` → _(leeg)_
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`
- **populatie**: `<memo>` → _(leeg)_

##### `OpenbareRuimte` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **herkomst**: `BAG` → _(leeg)_
- **herkomst definitie**: `<niet gespecificeerd>` → _(leeg)_
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`
- **populatie**: `<memo>` → _(leeg)_

##### `Pand` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: _(leeg)_ → `Objecttype PAND  is het equivalent van het city gml objecttype BUILDING PART.   #NOTES#Objecttype PAND  is het equivalent van het city gml objecttype BUILDING PART.   #NOTES#Objecttype PAND  is het equivalent van het city gml objecttype …`
- **herkomst**: `BAG` → _(leeg)_
- **herkomst definitie**: `BAG` → _(leeg)_
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`
- **populatie**: `<memo>` → _(leeg)_

##### `Standplaats` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: `<memo>` → _(leeg)_
- **herkomst**: `BAG` → _(leeg)_
- **herkomst definitie**: `<niet gespecificeerd>` → _(leeg)_
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`
- **populatie**: `<memo>` → _(leeg)_

##### `Verblijfsobject` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: _(leeg)_ → `Zie de catalogus BAG. #NOTES#Zie de catalogus BAG. #NOTES#Zie de catalogus BAG. #NOTES#Zie de catalogus BAG. #NOTES#Zie de catalogus BAG. #NOTES#Zie de catalogus BAG. #NOTES#Zie de catalogus BAG.`
- **herkomst**: `BAG` → _(leeg)_
- **herkomst definitie**: `BAG` → _(leeg)_
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`
- **populatie**: `<memo>` → _(leeg)_

##### `Wijk` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: _(leeg)_ → `Het betreft hier de in overleg met het CBS bepaalde indeling van de gemeente in wijken. #NOTES#Het betreft hier de in overleg met het CBS bepaalde indeling van de gemeente in wijken. #NOTES#Het betreft hier de in overleg met het CBS bepa…`
- **herkomst**: `GFO BG` → _(leeg)_
- **herkomst definitie**: `GFO BG` → _(leeg)_
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`
- **populatie**: `<memo>` → `<memo>#NOTES#Alleen bestaande wijken maken deel uit van de populatie WIJK. Plantopografie maakt geen onderdeel uit van de populatie.#NOTES#Alleen bestaande wijken maken deel uit van de populatie WIJK. Plantopografie maakt geen onderdeel …`

##### `Woonplaats` — 🟡 Gewijzigd

- **versie**: `1.5` → `1.12.0`
- **toelichting**: _(leeg)_ → `In incidentele gevallen komt het voor dat een woonplaats (in de zin van het gebied dat in de praktijk aangeduid wordt met dezelfde woonplaatsnaam) doorsneden wordt door een gemeentegrens. Volgens de definitie zou dit niet kunnen c.q. is …`
- **herkomst**: `BAG` → _(leeg)_
- **herkomst definitie**: `BAG` → _(leeg)_
- **datum opname**: `9 april 2007` → `2007-04-09 00:00:00`
- **populatie**: `<memo>` → _(leeg)_
