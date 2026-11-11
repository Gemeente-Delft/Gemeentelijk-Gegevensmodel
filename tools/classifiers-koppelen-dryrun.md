# Koppeling van losse typenamen aan classifiers (dry-run, 2026-11-04 17:48:18)

Bron: `v3.0.0/Gemeentelijk Gegevensmodel.qea`, attributen van klassen met een typetekst zonder classifier. Script: `tools/fixes/fix_classifiers.py`.

**Status: doorgevoerd op 4 november 2026 om 20:50, integraal (inclusief IMBOR).** Met `tools/fixes/fix_classifiers.py --apply` zijn de 222 automatische koppelingen gezet: 222 attributen in 58 klassen hebben nu een classifier, en de typetekst is gelijkgetrokken met de naam van het doelobject (LAND → Land). Back-up vooraf: `v3.0.0/Gemeentelijk Gegevensmodel.qea.backup-2026-11-04-voor-classifiers`. Controle: integrity_check ok, geen classifier wijst naar een onbestaand object, bij alle attributen is de typetekst gelijk aan de naam van de classifier. Herhaalrun van het script: automatisch 0, te beoordelen 39, geen match 28; die 67 losse typenamen hieronder blijven staan tot ze beoordeeld zijn. Controle met `task import:model generate:lod` (20:50): exit 0, 137 views; de waarschuwing "Onbekende datatypes teruggevallen op xsd:string" noemt nog 16 namen, precies de typeteksten uit "Geen match" (Adres, BereikbaarheidPlus, Constructieonderdeel, Enum/enum, Gebruiksfunctie, Kleuren, LeeftijdDoelgroep, Modaliteit, Sluitingspercentage, Toestelonderdeel, TypeBeschermingsstatusPlus, TypeSport, Wegfunctie, functieOndersteunendWegdeelPlus, typeringOndersteunendWaterPlus).


## Samenvatting

| Categorie | IMBOR | Overig | Totaal |
|---|---:|---:|---:|
| automatisch | 211 | 11 | 222 |
| te beoordelen | 4 | 35 | 39 |
| meerduidig | 0 | 0 | 0 |
| geen match | 19 | 9 | 28 |
| **totaal** | 234 | 55 | 289 |

## Automatisch

Classifier wordt het doel; de typetekst wordt de exacte naam van het doel.

| Typetekst nu | Doel | Attributen |
|---|---|---|
| Adresaanduiding | Adresaanduiding (Class, 99 Kern / RSGBPlus / RSGB Model / Groepattribuutsoort) | Binnenlocatie.adres, Sportvereniging.adres |
| CodeLeerwegMBO | CodeLeerwegMBO (Enumeration, 6 Sociaal Domein / Werk / Model Werk) | Opleiding.CodeLeerwegMBO |
| CodeNiveauOpleiding | CodeNiveauOpleiding (Enumeration, 6 Sociaal Domein / Werk / Model Werk) | Opleiding.CodeNiveauOpleiding |
| CodeSoortOpleidingsnaam | CodeSoortOpleidingsnaam (Enumeration, 6 Sociaal Domein / Werk / Model Werk) | OpleidingsnaamGecodeerd.CodeSoortOpleidingsnaam |
| LAND | Land (Class, 99 Kern / RSGBPlus / RSGB Model / Referentielijsten) | AfwijkendBuitenlandsCorrespondentieadresRol.landPostadres, IngeschrevenPersoon.landWaarvandaanIngeschreven, IngeschrevenPersoon.landWaarnaarVertrokken |
| Opleidingsrichting | Opleidingsrichting (Enumeration, 6 Sociaal Domein / Werk / Model Werk) | Opleiding.Opleidingsrichting |
| statusOpenbareRuimte | statusOpenbareRuimte (Enumeration, 99 Kern / BAG / Model BAG) | Buurt.status, Wijk.status |
| AanOfVrijliggend | enum_AanOfVrijliggend (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Verhardingsobject.aanOfVrijliggend |
| Afmeting | enum_Afmeting (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Verhardingsobject.afmeting |
| Bedienaar | enum_Bedienaar (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Brug.bedienaar, Gemaal.bedienaar |
| Beheergebied | enum_Beheergebied (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Beheerobject.beheergebied |
| Belasting | enum_Belasting (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Verhardingsobject.belasting |
| BelastingklasseNieuw | enum_BelastingklasseNieuw (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Brug.belastingklasseNieuw, Flyover.belastingklasseNieuw, Kademuur.belastingklasseNieuw, Keermuur.belastingklasseNieuw, Viaduct.belastingklasseNieuw |
| BelastingklasseOud | enum_BelastingklasseOud (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Brug.belastingklasseOud, Flyover.belastingklasseOud, Kademuur.belastingklasseOud, Keermuur.belastingklasseOud, Viaduct.belastingklasseOud |
| Beleidsstatus | enum_Beleidsstatus (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Boom.beleidsstatus |
| BeoogdeOmlooptijd | enum_BeoogdeOmlooptijd (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Boom.beoogdeOmlooptijd |
| Bereikbaarheid | enum_Bereikbaarheid (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Groenobject.bereikbaarheid, Kunstwerk.bereikbaarheid, Overbruggingsobject.bereikbaarheid, Vegetatieobject.bereikbaarheid |
| BereikbaarheidKolk | enum_BereikbaarheidKolk (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Kolk.bereikbaarheidKolk |
| Boombeeld | enum_Boombeeld (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Boom.boombeeld |
| Boomgroep | enum_Boomgroep (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Boom.boomgroep |
| BoomhoogteklasseActueel | enum_BoomhoogteklasseActueel (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Boom.boomhoogteklasseActueel, Boom.boomhoogteklasseEindebeeld |
| Boomveiligheidsklasse | enum_Boomveiligheidsklasse (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Boom.veiligheidsklasseBoom, Groenobject.veiligheidsklasseBoom |
| Boomvoorziening | enum_Boomvoorziening (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Boom.boomvoorziening |
| BreedteklasseHaag | enum_BreedteklasseHaag (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Groenobject.breedteklasseHaag |
| Certificeringsinstantie | enum_Certificeringsinstantie (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Speeltoestel.certificeringsinstantie |
| Constructietype | enum_Constructietype (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Kunstwerk.constructietype |
| Controlefrequentie | enum_Controlefrequentie (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Boom.controlefrequentie |
| CultuurhistorischWaardevol | enum_CultuurhistorischWaardevol (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Groenobject.cultuurhistorischWaardevol, Terreindeel.cultuurhistorischWaardevol |
| Fabrikant | enum_Fabrikant (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Bouwwerk.fabrikant, Installatie.fabrikant, Kast.fabrikant, Meubilair.fabrikant |
| Formaat | enum_Formaat (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Verhardingsobject.formaat |
| Gebiedstype | enum_Gebiedstype (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Beheerobject.gebiedstype |
| Groeifase | enum_Groeifase (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Boom.groeifase |
| Grondsoort | enum_Grondsoort (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Beheerobject.grondsoort |
| GrondsoortPlus | enum_GrondsoortPlus (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Beheerobject.grondsoortPlus |
| HoogteklasseHaag | enum_HoogteklasseHaag (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Groenobject.hoogteklasseHaag |
| IMKLThema | enum_IMKLThema (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Leiding.themaIMKL, Leidingelement.themaIMKL |
| Installateur | enum_Installateur (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Kast.installateur, Kunstwerk.installateur, Meubilair.installateur, Overbruggingsobject.installateur |
| KroondiameterklasseActueel | enum_KroondiameterklasseActueel (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Boom.kroondiameterklasseActueel, Boom.kroondiameterklasseEindebeeld |
| KwaliteitsniveauGewenst | enum_KwaliteitsniveauGewenst (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Bak.kwaliteitsniveauGewenst, Groenobject.kwaliteitsniveauGewenst, Kunstwerk.kwaliteitsniveauGewenst, Meubilair.kwaliteitsniveauGewenst, Overbruggingsobject.kwaliteitsniveauGewenst, Paal.kwaliteitsniveauGewenst … (10) |
| Kweker | enum_Kweker (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Vegetatieobject.kweker |
| LengteKunstgras | enum_LengteKunstgras (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Verhardingsobject.lengteKunstgras |
| Leverancier | enum_Leverancier (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Bord.leverancier, Bouwwerk.leverancier, Groenobject.leverancier, Installatie.leverancier, Kast.leverancier, Kunstwerk.leverancier … (17) |
| Materiaal | enum_Materiaal (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Bak.materiaal, Bord.materiaal, Bouwwerk.bouwwerkMateriaal, Kademuur.materiaalBovenkantKademuur, Kunstwerk.kunstwerkMateriaal, Leiding.materiaal … (15) |
| Ondergroei | enum_Ondergroei (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Groenobject.ondergroei |
| Onderhoudsplichtige | enum_Onderhoudsplichtige (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Beheerobject.onderhoudsplichtige |
| Onderhoudsregime | enum_Onderhoudsregime (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Kunstwerk.onderhoudsregime, Overbruggingsobject.onderhoudsregime |
| Ondersteuningsvorm | enum_Ondersteuningsvorm (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Klimplant.ondersteuningsvorm |
| Snoeifase | enum_Snoeifase (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Boom.snoeifase |
| Soortnaam | enum_Soortnaam (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Groenobject.groenobjectSoortnaam, Terreindeel.terreindeelSoortnaam, Vegetatieobject.soortnaam |
| SoortVoeg | enum_SoortVoeg (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Verhardingsobject.soortVoeg |
| StamdiameterKlasse | enum_Stamdiameterklasse (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Boom.stamdiameterklasse |
| Status | enum_Status (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Beheerobject.status |
| TakvrijeStam | enum_TakvrijeStam (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Boom.takvrijeStam |
| Taludsteilte | enum_Taludsteilte (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Groenobject.taludsteilte |
| Toestelgroep | enum_Toestelgroep (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Speeltoestel.toestelgroep |
| Type | enum_Type (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Aansluitput.type, Afvalbak.type, Bank.type, Boom.type, Brug.type, Drainageput.type … (30) |
| TypeAfdekking | enum_TypeAfdekking (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Put.typeAfdekking |
| TypeBeheerder | enum_TypeBeheerder (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Beheerobject.typeBeheerder |
| TypeBeheerderPlus | enum_TypeBeheerderPlus (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Beheerobject.typeBeheerderPlus |
| TypeBeschermingsstatus | enum_TypeBeschermingsstatus (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Boom.typeBeschermingsstatus |
| TypeBewerking | enum_TypeBewerking (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Groenobject.typeBewerking, Terreindeel.typeBewerking |
| TypeBovenkantKademuur | enum_TypeBovenkantKademuur (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Kademuur.typeBovenkantKademuur |
| TypeCommunicatie | enum_TypeCommunicatie (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Installatie.typeCommunicatie, Kast.typeCommunicatie |
| TypeConstructie | enum_TypeConstructie (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Verhardingsobject.typeConstructie |
| TypeEigenaar | enum_TypeEigenaar (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Beheerobject.typeEigenaar |
| TypeEigenaarPlus | enum_TypeEigenaarPlus (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Beheerobject.typeEigenaarPlus |
| TypeFundering | enum_TypeFundering (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Bouwwerk.typeFundering, Kademuur.typeFundering, Kast.typeFundering, Kunstwerk.typeFundering, Meubilair.typeFundering, Overbruggingsobject.typeFundering … (7) |
| TypeLigging | enum_TypeLigging (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Beheerobject.typeLigging |
| TypeMonument | enum_TypeMonument (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Kunstwerk.typeMonument |
| TypeOmgevingsrisicoklasse | enum_TypeOmgevingsrisicoklasse (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Boom.typeOmgevingsrisicoklasse, Groenobject.typeOmgevingsrisicoklasse |
| TypeOnderdeelMetPomp | enum_TypeOnderdeelMetPomp (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Pomp.typeOnderdeelMetPomp |
| TypePlus | enum_TypePlus (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Afvalbak.typePlus, Bank.typePlus, Boom.typePlus, Brug.typePlus, Fietsparkeervoorziening.typePlus, Groenobject.typePlus … (15) |
| TypeSlot | enum_TypeSlot (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Kast.typeSlot |
| TypeStandplaats | enum_TypeStandplaats (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Vegetatieobject.typeStandplaats |
| TypeStandplaatsPlus | enum_TypeStandplaatsPlus (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Vegetatieobject.typeStandplaatsPlus |
| TypeVaarwater | enum_TypeVaarwater (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Waterobject.typeVaarwater |
| TypeVermeerderingsvorm | enum_TypeVermeerderingsvorm (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Boom.typeVermeerderingsvorm |
| TypeVoeg | enum_TypeVoeg (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Verhardingsobject.typeVoeg |
| TypeVoegvulling | enum_TypeVoegvulling (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Verhardingsobject.typeVoegvulling |
| TypeWaaier | enum_TypeWaaier (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Pomp.typeWaaier |
| TypeWaterplant | enum_TypeWaterplant (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Waterobject.typeWaterplant |
| Vegen | enum_Vegen (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Verhardingsobject.vegen |
| Vorm | enum_Vorm (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Bak.vorm, Bergingsbassin.vorm, Bord.vorm, Overstortconstructie.vormDrempel, Paal.vorm, Put.vorm … (8) |
| VrijeDoorrijhoogte | enum_VrijeDoorrijhoogte (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Boom.vrijeDoorrijhoogte, Boom.vrijeDoorrijhoogtePrimair, Boom.vrijeDoorrijhoogteSecundair |
| VrijeTakval | enum_VrijeTakval (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Boom.vrijeTakval |
| VulmateriaalKunstgras | enum_VulmateriaalKunstgras (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Verhardingsobject.vulmateriaalKunstgras |
| Waterdoorlatendheid | enum_Waterdoorlatendheid (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Verhardingsobject.waterdoorlatendheid |
| WegcategorieDV | enum_WegcategorieDV (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Verhardingsobject.wegcategorieDV, Verhardingsobject.wegcategorieDVPlus |
| WegtypeBestaand | enum_WegtypeBestaand (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Verhardingsobject.wegtypeBestaand |
| Zettingsgevoeligheid | enum_Zettingsgevoeligheid (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Beheerobject.zettingsgevoeligheid |
| ZettingsgevoeligheidPlus | enum_ZettingsgevoeligheidPlus (Enumeration, 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Enumeratiesoort) | Beheerobject.zettingsgevoeligheidPlus |

## Te beoordelen

Niet automatisch gekoppeld; het voorgestelde doel staat erbij. Oordeel per regel.

| Klasse.attribuut | Typetekst | Voorgesteld doel | Reden |
|---|---|---|---|
| Voorliggende voorziening.Voorliggende voorziening Id (6 Sociaal Domein / Inkomen / Diensten / Model Diensten) | CdTypeVerstrekkingsvorm | CdTypeVerstrekkingsvorm (Enumeration, 6 Sociaal Domein / Inkomen / Diensten / Datatypes) | attribuutnaam lijkt niet op de typenaam |
| Voorwaarde.Conclusie (6 Sociaal Domein / Inkomen / Diensten / Model Diensten) | Brontype | Brontype (Enumeration, 6 Sociaal Domein / Inkomen / Terug- en invordering / Datatypes) | attribuutnaam lijkt niet op de typenaam |
| Voorwaarde.Vastleggingsdatum (6 Sociaal Domein / Inkomen / Diensten / Model Diensten) | Brontype | Brontype (Enumeration, 6 Sociaal Domein / Inkomen / Terug- en invordering / Datatypes) | attribuutnaam lijkt niet op de typenaam |
| Maatregel op uitkering.Motivatie vermindering maatregel (6 Sociaal Domein / Inkomen / Normafwijking / Model Normafwijking) | CodeRedenMaatregel | CodeRedenMaatregel (Enumeration, 6 Sociaal Domein / Inkomen / Normafwijking / Datatypes) | attribuutnaam lijkt niet op de typenaam |
| Maatregel op uitkering.Percentage maatregel (6 Sociaal Domein / Inkomen / Normafwijking / Model Normafwijking) | CodeRedenMaatregel | CodeRedenMaatregel (Enumeration, 6 Sociaal Domein / Inkomen / Normafwijking / Datatypes) | attribuutnaam lijkt niet op de typenaam |
| Gestopt betaald werk.Bedrijfsadres (6 Sociaal Domein / Inkomen / Reden aanvraag / Reden aanvraag) | CdRedenAanvraagWwafgewezen | CdRedenAanvraagWwafgewezen (Enumeration, 6 Sociaal Domein / Inkomen / Reden aanvraag / Datatypes) | attribuutnaam lijkt niet op de typenaam |
| Gestopt betaald werk.Bedrijfstelefoonnummer (6 Sociaal Domein / Inkomen / Reden aanvraag / Reden aanvraag) | CdRedenAanvraagWwafgewezen | CdRedenAanvraagWwafgewezen (Enumeration, 6 Sociaal Domein / Inkomen / Reden aanvraag / Datatypes) | attribuutnaam lijkt niet op de typenaam |
| Gestopt betaald werk.Laatste salarisdatum (6 Sociaal Domein / Inkomen / Reden aanvraag / Reden aanvraag) | CdRedenAanvraagWwafgewezen | CdRedenAanvraagWwafgewezen (Enumeration, 6 Sociaal Domein / Inkomen / Reden aanvraag / Datatypes) | attribuutnaam lijkt niet op de typenaam |
| Gestopt betaald werk.Naam bedrijf (6 Sociaal Domein / Inkomen / Reden aanvraag / Reden aanvraag) | CdRedenAanvraagWwafgewezen | CdRedenAanvraagWwafgewezen (Enumeration, 6 Sociaal Domein / Inkomen / Reden aanvraag / Datatypes) | attribuutnaam lijkt niet op de typenaam |
| Gestopt betaald werk.Specificatie reden einde werk (6 Sociaal Domein / Inkomen / Reden aanvraag / Reden aanvraag) | CdRedenAanvraagWwafgewezen | CdRedenAanvraagWwafgewezen (Enumeration, 6 Sociaal Domein / Inkomen / Reden aanvraag / Datatypes) | attribuutnaam lijkt niet op de typenaam |
| Gestopte bijstanduitkering.Specificatie reden einde bijstand (6 Sociaal Domein / Inkomen / Reden aanvraag / Reden aanvraag) | CdRedenAanvraagEindeBijstand | CdRedenAanvraagEindeBijstand (Enumeration, 6 Sociaal Domein / Inkomen / Reden aanvraag / Datatypes) | attribuutnaam lijkt niet op de typenaam |
| Gestopte bijstanduitkering.Specificatie wijziging situatie (6 Sociaal Domein / Inkomen / Reden aanvraag / Reden aanvraag) | CdRedenAanvraagEindeBijstand | CdRedenAanvraagEindeBijstand (Enumeration, 6 Sociaal Domein / Inkomen / Reden aanvraag / Datatypes) | attribuutnaam lijkt niet op de typenaam |
| Vordering.Periode einddatum (6 Sociaal Domein / Inkomen / Terug- en invordering / Model Terug- en invordering) | CategorieAnderInkomen | CategorieAnderInkomen (Enumeration, 6 Sociaal Domein / Inkomen / Terug- en invordering / Datatypes) | attribuutnaam lijkt niet op de typenaam |
| Vordering.Periode startdatum (6 Sociaal Domein / Inkomen / Terug- en invordering / Model Terug- en invordering) | CategorieAnderInkomen | CategorieAnderInkomen (Enumeration, 6 Sociaal Domein / Inkomen / Terug- en invordering / Datatypes) | attribuutnaam lijkt niet op de typenaam |
| Vordering.Priotype (6 Sociaal Domein / Inkomen / Terug- en invordering / Model Terug- en invordering) | CategorieAnderInkomen | CategorieAnderInkomen (Enumeration, 6 Sociaal Domein / Inkomen / Terug- en invordering / Datatypes) | attribuutnaam lijkt niet op de typenaam |
| Vordering.Stuitingsvoortgangsindicator (6 Sociaal Domein / Inkomen / Terug- en invordering / Model Terug- en invordering) | CategorieAnderInkomen | CategorieAnderInkomen (Enumeration, 6 Sociaal Domein / Inkomen / Terug- en invordering / Datatypes) | attribuutnaam lijkt niet op de typenaam |
| Vordering.Vaststeldatum terugvordering (6 Sociaal Domein / Inkomen / Terug- en invordering / Model Terug- en invordering) | CategorieAnderInkomen | CategorieAnderInkomen (Enumeration, 6 Sociaal Domein / Inkomen / Terug- en invordering / Datatypes) | attribuutnaam lijkt niet op de typenaam |
| Vordering.Verjaringsdatum (6 Sociaal Domein / Inkomen / Terug- en invordering / Model Terug- en invordering) | CategorieAnderInkomen | CategorieAnderInkomen (Enumeration, 6 Sociaal Domein / Inkomen / Terug- en invordering / Datatypes) | attribuutnaam lijkt niet op de typenaam |
| Huishouden.soort (6 Sociaal Domein / Sociaal Domein Generiek / Model Sociaal Domein Generiek) | EnumHuishoudenssoort | EnumHuishoudenssoort (Enumeration, 6 Sociaal Domein / Schulden / Schuldhulpverlening / Model Schuldhulpverlening) | kandidaat in een ander model (6 Sociaal Domein / Schulden / Schuldhulpverlening / Model Schuldhulpverlening) |
| Ander inkomen.Categorie (6 Sociaal Domein / Sociaal Domein Generiek / Model Sociaal Domein Generiek / Inkomsten / Model Inkomsten) | CategorieVorderingCBS | CategorieVorderingCBS (Enumeration, 6 Sociaal Domein / Inkomen / Terug- en invordering / Datatypes) | kandidaat in een ander model (6 Sociaal Domein / Inkomen / Terug- en invordering / Datatypes) |
| Bankrekening.Brontype (6 Sociaal Domein / Sociaal Domein Generiek / Model Sociaal Domein Generiek / Vermogen / Model Vermogen) | Brontype | Brontype (Enumeration, 6 Sociaal Domein / Inkomen / Terug- en invordering / Datatypes) | kandidaat in een ander model (6 Sociaal Domein / Inkomen / Terug- en invordering / Datatypes) |
| Bankrekening.Rekeningtype (6 Sociaal Domein / Sociaal Domein Generiek / Model Sociaal Domein Generiek / Vermogen / Model Vermogen) | Rekeningtype | Rekeningtype (Enumeration, 6 Sociaal Domein / Inkomen / Terug- en invordering / Datatypes) | kandidaat in een ander model (6 Sociaal Domein / Inkomen / Terug- en invordering / Datatypes) |
| Waardepeiling.Brontype (6 Sociaal Domein / Sociaal Domein Generiek / Model Sociaal Domein Generiek / Vermogen / Model Vermogen) | Brontype | Brontype (Enumeration, 6 Sociaal Domein / Inkomen / Terug- en invordering / Datatypes) | kandidaat in een ander model (6 Sociaal Domein / Inkomen / Terug- en invordering / Datatypes) |
| Arbeidsmarktkwalificaties.Code taalbeheersing mondeling (6 Sociaal Domein / Werk / Model Werk) | Taalvaardigheid | Taalvaardigheid (Enumeration, 6 Sociaal Domein / Werk / Model Werk) | attribuutnaam lijkt niet op de typenaam |
| Arbeidsmarktkwalificaties.Code taalbeheersing schriftelijk (6 Sociaal Domein / Werk / Model Werk) | Taalvaardigheid | Taalvaardigheid (Enumeration, 6 Sociaal Domein / Werk / Model Werk) | attribuutnaam lijkt niet op de typenaam |
| Arbeidsmarktkwalificaties.Code werk en denkniveau (6 Sociaal Domein / Werk / Model Werk) | Taalvaardigheid | Taalvaardigheid (Enumeration, 6 Sociaal Domein / Werk / Model Werk) | attribuutnaam lijkt niet op de typenaam |
| Arbeidsvermogen.CodeArbeidsvermogen (6 Sociaal Domein / Werk / Model Werk) | arbeidsvermogen | Arbeidsvermogen (Class, 6 Sociaal Domein / Werk / Model Werk) | verwijst naar de eigen klasse |
| Ontheffing.SoortOntheffing (6 Sociaal Domein / Werk / Model Werk) | ontheffing | Ontheffing (Class, 6 Sociaal Domein / Werk / Model Werk) | verwijst naar de eigen klasse |
| Ontheffing.ResultaatInstrumentbeoordeling (6 Sociaal Domein / Werk / Model Werk) | document | Document (Class, 99 Kern / RGBZPlus / Model RGBZ / Model Kern RGBZ) | attribuutnaam lijkt niet op de typenaam |
| TaalbeheersingNederlands.SpreeksvaardigheidNederlands (6 Sociaal Domein / Werk / Model Werk) | Taalvaardigheid | Taalvaardigheid (Enumeration, 6 Sociaal Domein / Werk / Model Werk) | attribuutnaam lijkt niet op de typenaam |
| TaalbeheersingNederlands.LuistervaardigheidNederlands (6 Sociaal Domein / Werk / Model Werk) | Taalvaardigheid | Taalvaardigheid (Enumeration, 6 Sociaal Domein / Werk / Model Werk) | attribuutnaam lijkt niet op de typenaam |
| TaalbeheersingNederlands.LeesvaardigheidNederlands (6 Sociaal Domein / Werk / Model Werk) | Taalvaardigheid | Taalvaardigheid (Enumeration, 6 Sociaal Domein / Werk / Model Werk) | attribuutnaam lijkt niet op de typenaam |
| TaalbeheersingNederlands.SchrijfvaardigheidNederlands (6 Sociaal Domein / Werk / Model Werk) | Taalvaardigheid | Taalvaardigheid (Enumeration, 6 Sociaal Domein / Werk / Model Werk) | attribuutnaam lijkt niet op de typenaam |
| TaalbeheersingNederlands.GespreksvaardigheidNederlands (6 Sociaal Domein / Werk / Model Werk) | Taalvaardigheid | Taalvaardigheid (Enumeration, 6 Sociaal Domein / Werk / Model Werk) | attribuutnaam lijkt niet op de typenaam |
| ZelfredzaamheidScore.ZRM score (6 Sociaal Domein / Werk / Model Werk) | score | Score (Class, 6 Sociaal Domein / Generiek Jeugd en Wmo / Model Jeugd en Wmo Generiek) | kandidaat in een ander model (6 Sociaal Domein / Generiek Jeugd en Wmo / Model Jeugd en Wmo Generiek) |
| Groenobject.knipfrequentie (8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Model IMBOR) | Frequentie | Frequentie (Enumeration, 6 Sociaal Domein / Generiek Jeugd en Wmo / Model Jeugd en Wmo Generiek) | kandidaat in een ander model (6 Sociaal Domein / Generiek Jeugd en Wmo / Model Jeugd en Wmo Generiek) |
| Groenobject.maaifrequentie (8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Model IMBOR) | Frequentie | Frequentie (Enumeration, 6 Sociaal Domein / Generiek Jeugd en Wmo / Model Jeugd en Wmo Generiek) | kandidaat in een ander model (6 Sociaal Domein / Generiek Jeugd en Wmo / Model Jeugd en Wmo Generiek) |
| Klimplant.knipfrequentie (8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Model IMBOR) | Frequentie | Frequentie (Enumeration, 6 Sociaal Domein / Generiek Jeugd en Wmo / Model Jeugd en Wmo Generiek) | kandidaat in een ander model (6 Sociaal Domein / Generiek Jeugd en Wmo / Model Jeugd en Wmo Generiek) |
| Speeltoestel.controlefrequentie (8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing / Beheer Openbare Ruimte / Model Basis IMBOR / Model IMBOR) | Frequentie | Frequentie (Enumeration, 6 Sociaal Domein / Generiek Jeugd en Wmo / Model Jeugd en Wmo Generiek) | kandidaat in een ander model (6 Sociaal Domein / Generiek Jeugd en Wmo / Model Jeugd en Wmo Generiek) |

## Meerduidig

| Klasse.attribuut | Typetekst | Kandidaten |
|---|---|---|

## Geen match

Geen klasse, enumeratie of datatype met deze naam in het model.

| Typetekst | Attributen |
|---|---|
| Adres | Locatie.adres |
| BereikbaarheidPlus | Groenobject.groenobjectBereikbaarheidPlus, Kunstwerk.kunstwerkBereikbaarheidPlus, Vegetatieobject.vegetatieobjectBereikbaarheidPlus |
| Constructieonderdeel | Rioolput.rioolputConstructieonderdeel |
| Enum | Leerroute.LeerrouteType, Leerroute.Niveau, Leerroute.GeschatteIntensiteitB1Route, Leerroute.IndicatorToestemmingExamenA2, Rijbewijs /Certificaat.VerstrekkendePartij |
| enum | Rijbewijs /Certificaat.NaamCertificaat |
| functieOndersteunendWegdeelPlus | OndersteunendWegdeel.plusFunctie |
| Gebruiksfunctie | Beheerobject.beheerobjectGebruiksfunctie |
| Kleuren | Kast.kleur, Kunstwerk.kleur, Meubilair.kleur, Overbruggingsobject.kleur, Verhardingsobject.kleur |
| LeeftijdDoelgroep | Speelterrein.speelterreinLeeftijdDoelgroep |
| Modaliteit | Overbruggingsobject.overbruggingsobjectModaliteit, Verhardingsobject.verhardingsobjectModaliteit |
| Sluitingspercentage | Groenobject.gewenstSluitingspercentage |
| Toestelonderdeel | Speeltoestel.speeltoestelToestelonderdeel |
| TypeBeschermingsstatusPlus | Boom.boomTypeBeschermingsstatusPlus |
| typeringOndersteunendWaterPlus | OndersteunendWaterdeel.plusType |
| TypeSport | Sportterrein.sportterreinTypeSport |
| Wegfunctie | Verhardingsobject.verhardingsobjectWegfunctie, Weginrichtingsobject.weginrichtingsobjectWegfunctie |
