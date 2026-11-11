# Enumeraties met dubbele waarden: inventaris en voorstel (4 november 2026)

Bron: `v3.0.0/Gemeentelijk Gegevensmodel.qea`, alle enumeratiewaarden (t_attribute van objecten met
Object_Type Enumeration). Aanleiding: de LOD-export meldt waarden die binnen één enumeratie dezelfde IRI-slug
krijgen en daarom een volgnummer. Script voor het samenvoegen: `tools/fixes/fix_enum_dubbelen.py`.

**Status: doorgevoerd op 4 november 2026 (18:05)**, inclusief IMBOR: 40 overtollige waarden weg uit zes enumeraties, integrity ok, tweede run 0. Back-up: `v3.0.0/Gemeentelijk Gegevensmodel.qea.backup-2026-11-04-voor-enum-dubbelen`. Daarbij ook de verkeerd gecodeerde tekens hersteld met `tools/fixes/fix_mojibake.py`: 154 teksten (36 enumeratiewaarden, 109 toelichtingen van enumeratiewaarden en IMBOR-attributen, de enumeraties enum_Oriëntatie en enum_Plaatsoriëntatie, 4 objecttoelichtingen, 3 objecttags); harde spaties zijn gewone spaties geworden. DefaultEnumeratie heeft nu één waarde; de keuze om dat attribuut CharacterString te maken staat nog open. De slug-aanpassing in crunch_uml is niet gedaan.

## Samenvatting

| Soort | Groepen | Overtollige waarden | Voorstel |
|---|---:|---:|---|
| Exact dezelfde naam | 30 | 39 | samenvoegen |
| Zelfde naam op hoofdletters na | 1 | 1 | samenvoegen |
| Alleen dezelfde LOD-slug (A, A+, A++) | 3 | 0 | laten staan; IRI-vorming in crunch_uml aanpassen |

Negen enumeraties zijn geraakt; de echte dubbelen zitten in zes daarvan.

## Inventaris

| Enumeratie | Pakket | Waarden | Gebruikt door | Dubbel | Toelichting |
|---|---|---:|---|---|---|
| OnderdeelDienstTypeRubriek | 6 Sociaal Domein / Inkomen / Diensten / Datatypes | 204 | Leveringscomponenttype.Rubriek | 7 waarden 2× | identieke rijen, geen toelichting: bijstand instelling gehuwden 21+; bruto Aow afwijkend partner; bruto Aow alleenstaande partner; bruto Aow eenoudergezin partner; Bruto Aow gezin 100% (partner < AOW) partner; bruto Aow gezin 50% partner; norm pers. uitg. gehuwden 18 t/m 20 jr (handm) |
| DefaultEnumeratie | 6 Sociaal Domein / Inkomen / Terug- en invordering / Datatypes | 3 | Uitstel aflossing.Reden uitstel | Nader te bepalen 3× | de enumeratie bestaat alleen uit drie keer dezelfde placeholder |
| SubCategorieVordering | 6 Sociaal Domein / Inkomen / Terug- en invordering / Datatypes | 53 | Terugvorderingsverzoek.Subcategorie, Vordering.Subcategorie | Verwijtbare vordering Ioaw 6×, Verwijtbare vordering Ioaz 6× | identieke rijen; in de bron stond de waarde vermoedelijk per hoofdcategorie |
| CdSzWet | 6 Sociaal Domein / Sociaal Domein Generiek / Inkomsten / Datatypes | 54 | Uitkering.Inkomstensoort uitkering | AOW-Overbruggingsregeling 2×; Wet werk en arbeidsondersteuning jonggehandicapten (Wet Wajong) 2× (één met hoofdletters) | de officiële schrijfwijze is met kleine letters |
| enum_Type | 8 … / Model Basis IMBOR / Enumeratiesoort | 414 | (nog niet gekoppeld) | 7 waarden 2×: Elementenverharding, Halfverharding, Heesters, Klimplant, Onverhard, Planten, Struikrozen | bij Heesters, Klimplant, Planten en Struikrozen heeft één van de twee een toelichting |
| enum_TypePlus | 8 … / Model Basis IMBOR / Enumeratiesoort | 539 | (nog niet gekoppeld) | 12 waarden 2×: Botanische rozen, Cultuurrozen, Fijne sierheester, Geschoren boom, Grove sierheester, Hangbrug, Heesterrozen, Open grond, Vaste planten, Wisselperken, Zand, Zwarte grond | bij Vaste planten en Wisselperken heeft één van de twee een toelichting |
| enum_KwaliteitsniveauGewenst | 8 … / Model Basis IMBOR / Enumeratiesoort | 5 | (nog niet gekoppeld) | A en A+ (zelfde slug) | echte waarden |
| CROW-Kwaliteitsniveaus | 8 … / Model Beheer Openbare Ruimte | 5 | CROW-Melding.kwaliteitsniveau | Niveau A en Niveau A+ (zelfde slug) | echte waarden |
| Energielabel Gebouwen | 9 Interne Organisatie / Vastgoed / Model Vastgoed | 11 | Vastgoedobject.energielabel | A, A+ en A++ (zelfde slug) | echte waarden, elk met eigen toelichting |

De dubbelen in enum_Type en enum_TypePlus komen uit het samenvoegen van de IMBOR-waardelijsten per klasse
(Groenobject en Vegetatieobject hebben allebei Heesters): dezelfde waarde kwam uit twee lijsten mee, de ene keer met en de
andere keer zonder toelichting. Dat pakket is op dit moment onderhanden in de IMBOR-sessie. Terzijde: de toelichting van
Planten bevat verkeerd gecodeerde tekens ("Ã©Ã©n" voor "één"); dat komt uit de IMBOR-import en staat los van de dubbelen.

## Voorstel

1. **Exacte dubbelen en hoofdlettervarianten samenvoegen** tot één waarde per enumeratie: 40 rijen weg uit zes enumeraties.
   Per groep blijft de rij met een toelichting; is er geen toelichting, dan de oudste rij (laagste ID). Bij CdSzWet blijft zo
   de schrijfwijze met kleine letters. Hebben twee rijen elk een andere toelichting (komt nu niet voor), dan worden die
   samengevoegd. Tagged values van de verdwijnende rijen gaan mee weg; de waarden hebben nu geen tags en geen alias of code.
   Verwijzingen vanuit attributen gaan naar de enumeratie, niet naar de waarde, dus er breekt niets.
2. **DefaultEnumeratie** houdt na samenvoeging één waarde, "Nader te bepalen". Dat is geen enumeratie maar een placeholder
   uit de proposal Terug- en invordering; beter is het attribuut Uitstel aflossing.Reden uitstel voorlopig CharacterString te
   maken en DefaultEnumeratie te verwijderen. Keuze aan de beheerder.
3. **A, A+ en A++ laten staan.** Dat zijn verschillende waarden; alleen de slug valt samen omdat crunch_uml het plusteken
   wegstript. Voorstel voor crunch_uml (`lodrenderer.slugify`): "+" vertalen naar "plus" zodat de IRI's stabiel worden
   (`a`, `a-plus`, `a-plus-plus`) en niet van de volgorde afhangen. Tot die tijd krijgen ze een volgnummer, zoals nu.
4. **IMBOR-enumeraties na de IMBOR-sessie**: enum_Type en enum_TypePlus zijn daar onderhanden (ontdubbeling van de
   enumeraties zelf). Het script kan die overslaan met `--zonder-imbor` en later apart draaien.

## Uitvoering

```bash
python3 -I tools/fixes/fix_enum_dubbelen.py "v3.0.0/Gemeentelijk Gegevensmodel.qea"
```

Dry-run (4 nov 2026, 17:55): 40 overtollige waarden in 6 enumeraties, geen samen te voegen toelichtingen. Doorvoeren met
`--apply` (eventueel `--zonder-imbor`), met Enterprise Architect gesloten en na een back-up van de .qea. Daarna
`task import:model generate:lod` en controleren dat de waarschuwingen over gedeelde IRI-slugs alleen nog A/A+/A++ betreffen.
