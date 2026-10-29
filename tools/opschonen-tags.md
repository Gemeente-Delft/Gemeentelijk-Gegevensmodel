# `#NOTES#` in de .qea: onderzoek en voorstel

Onderzoek van 29 oktober 2026 naar de vervuiling van EA-tagwaarden in `v3.0.0/Gemeentelijk Gegevensmodel.qea`,
met een voorstel om ze op te schonen. Script: `tools/opschoon_tags.py` (rapporteert standaard; schrijft alleen met
`--output` een opgeschoonde kopie).

## Hoe EA een tagged value bewaart

Een tagged value staat in `t_objectproperties` (elementen), `t_attributetag` (attributen) of `t_connectortag`
(relaties), met twee kolommen:

| kolom | gewone tag | memo-tag (lange tekst) |
|---|---|---|
| `Value` | de waarde (`BRP`, een URL, een datum) | de placeholder `<memo>` |
| `Notes` | de notities van de tagdefinitie uit het profiel (`Description: ...`, `Values: ...`, `Default: ...`) | de tekst zelf |

De XMI-export van EA plakt beide kolommen aan elkaar: `Value#NOTES#Notes`. Daar komt de scheider vandaan; in de
repository zelf hoort hij niet voor te komen.

## Wat er in de repository staat

Alle vervuiling zit in `t_objectproperties`; de attribuut- en relatietags zijn schoon. Stand sinds minstens
13 september 2026 (commit a4d2c709), onveranderd in de commits daarna.

| patroon | rijen | voorbeeld |
|---|---|---|
| `Value` = `#NOTES#Description: ...` (lege waarde, tagdefinitie in de waardekolom) | 1.683 | Begrip, Datum opname, Herkomst, Herkomst definitie, Kwaliteit |
| `Value` = `#NOTES#tekst` (lege waarde, echte tekst erachter) | 57 | Toelichting, Populatie |
| `Value` = `waarde#NOTES#Description: ...` | 179 | Herkomst = `https://www.nvvk.nl/...#NOTES#Description: De registratie ...` |
| `Value` = `<memo>#NOTES#tekst#NOTES#tekst...` | 41 | Populatie van Wijk en Buurt |
| `Notes` met herhaalde delen (2, 7, 8 of 13 keer dezelfde tekst) | 681 | Populatie van Wijk: 1.631 tekens, dertien keer dezelfde zin |

Samen 1.960 rijen op 402 elementen (1.579 op klassen, 380 op enumeraties, 1 op een pakket), precies de tags
die crunch_uml kent en terugschrijft: Datum opname, Herkomst en Herkomst definitie (elk 401), Begrip (299),
Kwaliteit (208), Toelichting (165), Populatie (84), release (1).

Daarnaast, geen `#NOTES#` maar wel ruis:

- **Dubbele tagrijen op relaties**: in `t_connectortag` staat bij 1.085 (relatie, tag)-paren dezelfde tag
  twee keer, met identieke waarde (62 relaties met alle MIM-relatietags dubbel: Toelichting, Regels, Positie,
  Mogelijk geen waarde, Is afgeleid, de indicaties; Begrip 92 keer). Vermoedelijk is het MIM-profiel twee keer
  toegepast. Op elementen en attributen komen geen dubbele tagrijen voor.
- **Tags van twee profielversies naast elkaar**: 24 elementen hebben zowel `Populatie` als
  `Populatie objecttype`, en zowel `Toelichting` als `Toelichting objecttype` (MIM 1.1-namen naast MIM 1.2).
  crunch_uml kent alleen de 1.2-namen; de oude tags doen niets, maar staan wel in EA.

## Hoe het is ontstaan

De aantallen en de tagnamen wijzen op rondreizen van het model: XMI-export of Excel → crunch_uml-database →
terugschrijven in de repository met `crunch_uml export -t earepo` (TaskFile `util:import-xlsx`, en eerder
`generate:mim`). De database hield de XMI-vorm `Value#NOTES#Notes`, en de terugschrijver zette die string
ongewijzigd in `Value`. Bij de volgende export plakte EA er opnieuw `#NOTES#Notes` achter, en zo verder: 2, 7,
8 en 13 herhalingen zijn het aantal rondreizen van die elementen. De 401 elementen zijn de elementen die bij
die rondreizen in de database zaten.

## Gevolg nu

Sinds crunch_uml 0.8.5 maken de renderers de tekst zelf schoon (elke tekst één keer, tagdefinities weg), dus
documentatie en LOD zijn al schoon. De vervuiling staat alleen nog in EA zelf: wie een element opent ziet
`#NOTES#Description: ...` als waarde, en de memoteksten van Wijk en Buurt dertien keer.

Een tweede bevinding, los van de vervuiling: **memoteksten in `Notes` leest crunch_uml niet.** De qea-parser
leest alleen `Value`. Een memo-tag die EA netjes heeft opgeslagen (`<memo>` in Value, tekst in Notes) komt dus
als `<memo>` in de database en valt weg uit documentatie en LOD: 148 teksten op elementen (Populatie
objecttype, Toelichting objecttype, Unieke aanduiding, Indicatie authentiek, Patroon), 1.586 op attributen
(Toelichting 318, Regels 238, Patroon 217, Indicatie authentiek 252, Waardenverzameling 170) en 160 op
relaties. In de huidige database hebben 669 attributen `toelichting = '<memo>'` en 689 `patroon = '<memo>'`.
De XMI-export van januari had hetzelfde gat (665), dus dit is niet door de overstap naar de `.qea` ontstaan,
maar de `.qea` maakt het wel oplosbaar.

## Voorstel

1. **crunch_uml 0.8.6**, vóór de opschoning:
   - de qea-parser leest `Notes` als `Value` = `<memo>` (alle drie de tagtabellen), zodat memoteksten in
     documentatie en LOD komen; `test_40` krijgt een pariteitstest op tagwaarden;
   - de terugschrijver (`export -t earepo`, `-t eamimrepo`) schrijft nooit meer `#NOTES#` in `Value`: de
     waarde vóór de scheider wordt `Value`, memotekst gaat naar `Notes`, en een lege waarde blijft leeg. Daarmee
     kan de vervuiling niet terugkomen.
2. **Opschonen** met `tools/opschoon_tags.py`, EA dicht, op een kopie:
   - `Value` wordt het deel vóór de eerste `#NOTES#`; bij een lege waarde met echte tekst erachter wordt die
     tekst de waarde (57 rijen Toelichting en Populatie, zoals EA die bij schone rijen ook bewaart);
   - bij `<memo>` wordt `Notes` de tekst: elk deel één keer, zonder tagdefinities (de 41 memo-rijen; Wijk en
     Buurt houden hun zin één keer, de rijen met alleen `Default: <memo>` worden leeg);
   - bij een gewone tag wordt `Notes` het eerste deel (de tagdefinitie, zoals EA die zelf neerzet).
   Het script meldt elke rij waarin tekst verloren zou gaan; in het GGM is dat er geen.
3. **Controleren**: de opgeschoonde kopie importeren met crunch_uml, documentatie en LOD genereren en
   vergelijken met dezelfde uitvoer uit de originele `.qea`. Verwachting: identiek, omdat de renderers sinds
   0.8.5 dezelfde opschoning al doen. Daarna de kopie in EA openen en Wijk, Buurt en een paar klassen met
   Herkomst bekijken.
4. **Vervangen en vastleggen**: de kopie wordt `v3.0.0/Gemeentelijk Gegevensmodel.qea`, commit, en de
   pijplijn draait opnieuw (`task --force import:model`, want `import:model` kijkt alleen naar de datum van de
   `.qea`).
5. **Optioneel, aparte keuze**: de 1.085 identieke dubbele relatietags terugbrengen tot één rij, en de MIM 1.1-tags
   (`... objecttype`, `... attribuutsoort`, `... relatiesoort`, `... referentielijst`) verwijderen waar de
   MIM 1.2-tag bestaat. Dat raakt EA-weergave, niet de uitvoer, en verdient een eigen controle.

## Rapport van het script (dry-run, 29 oktober 2026)

```
1960 tagwaarden met '#NOTES#' te schonen
  t_objectproperties: 53 x lege waarde met tekst erachter: tekst wordt de waarde
  t_objectproperties: 1687 x lege waarde: tagdefinitie uit Value
  t_objectproperties: 41 x memo: tekst in Notes, ontdubbeld
  t_objectproperties: 179 x waarde losgeknipt van de tagdefinitie
  per tag: Datum opname 401, Herkomst 401, Herkomst definitie 401, Begrip 299, Kwaliteit 208,
           Toelichting 165, Populatie 84, Release 1
```

Proefkopie: 1.960 rijen bijgewerkt, 0 rijen met `#NOTES#` over. Vier rijen `Toelichting` hadden achter de
scheider de profielbeschrijving zonder label ("Een inhoudelijke toelichting op de toepassing van het
informatie-element."); het script kent die beschrijvingen (`BEKENDE_DEFINITIES`) en maakt zo'n waarde leeg.

## Controle van de proefkopie (29 oktober 2026)

Origineel en proefkopie zijn allebei geïmporteerd met crunch_uml 0.8.5 en vergeleken op documentatie,
ontologie, shapes en views.

- Shapes gelijk. Er komen 46 toelichtingen en populaties bij die nu leeg zijn: de `#NOTES#tekst`-rijen, waarvan
  de renderer de tekst tot nu toe weggooide omdat die achter de scheider stond.
- Er verdwijnen 41 teksten: de memo-rijen (`<memo>#NOTES#tekst`), zoals "Zie verder de toelichting in de BRP."
  en de populatie van de BR WOZ. Na het opschonen staan die netjes in `Notes`, en juist die kolom leest de
  qea-parser niet. Dat bevestigt de volgorde van het voorstel: eerst crunch_uml 0.8.6 (parser leest `Notes`
  bij `<memo>`), dan opschonen. Met die parserfix komen de 41 terug, plus de 148 + 1.586 + 160 memoteksten die
  nu al ontbreken.

**Meting met een prototype van de parserfix** (branch `memo-notes-0.8.6` in crunch_uml, niet uitgebracht: de
qea-parser geeft bij `<memo>` de tekst uit `Notes` door in de XMI-vorm `<memo>#NOTES#tekst`, zodat `clean_value`
beide bronnen gelijk behandelt).

- Origineel, prototype tegenover 0.8.5: er komen 355 `mim:toelichting` en 211 `mim:patroon` van attributen bij
  in de ontologie, er verdwijnt niets; de documentatie verandert niet (de tabel van attributen toont die velden
  niet). In de database krijgen 318 attributen een toelichting en 217 een patroon die nu `<memo>` zijn.
- Opgeschoond tegenover origineel, beide met het prototype: 46 toelichtingen en populaties komen erbij, en er
  verdwijnen er precies 4: de populatie "Voor objecttypen die deel uitmaken van een (basis)registratie ..." op
  vier klassen, de profielbeschrijving die EA als tekst had neergezet en die het script bewust leegmaakt.
  Verder niets verloren: de 41 memoteksten blijven staan.

Conclusie: de opschoning is veilig zodra de parserfix er is, en de parserfix is op zichzelf al winst.

## Uitgevoerd (29 oktober 2026, na akkoord)

1. crunch_uml 0.8.6 uitgebracht (PR 22): de qea-parser geeft memotekst uit `Notes` door als `<memo>#NOTES#tekst`;
   de terugschrijver (`export -t earepo`/`-t eamimrepo`) zet de waarde vóór de scheider in `Value` en de memotekst in
   `Notes`, en vergelijkt beide kolommen voordat een tag als gewijzigd geldt. `test_55` dekt de rondreis.
2. `v3.0.0/Gemeentelijk Gegevensmodel.qea` vervangen door de opgeschoonde kopie van `tools/opschoon_tags.py`
   (1.960 rijen bijgewerkt, 0 rijen met `#NOTES#` over, `pragma integrity_check` ok). Het origineel staat in git
   (commit 073dd960 en eerder).
3. Pijplijn opnieuw gedraaid met 0.8.6 (`task --force import:model`, docs, LOD, Excel). Tegenover de 0.8.5-uitvoer:
   401 `mim:toelichting` en 211 `mim:patroon` erbij (355 attribuut-toelichtingen, 46 klasse-teksten die achter de
   scheider stonden, 211 patronen), 4 `mim:populatie` weg (de profielbeschrijving op vier klassen), verder niets;
   58 views en 6 definitiepagina's gewijzigd; 0 `#NOTES#` in ontologie en documentatie. In de database hebben nu
   318 attributen een toelichting en 217 een patroon die eerst `<memo>` waren.
4. Nog te doen door de beheerder: de opgeschoonde `.qea` in EA openen en Wijk, Buurt en een paar klassen met Herkomst
   bekijken; `task -y publish:lod` voor de nieuwe views; stap 5 (dubbele relatietags, MIM 1.1-tags) apart beslissen.
