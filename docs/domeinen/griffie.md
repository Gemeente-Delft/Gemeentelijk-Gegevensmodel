# Griffie

De definities van de objecttypen zijn afgeleid van de in het RIS opgeslagen informatie. Bovendien is er gebruik gemaakt van het informatiemodel uit de Pilots Open Raadsinformatie  die op het moment van schrijven nog in ontwikkeling is. Er is gekozen de gegevens zoals die nu in het RIS van Delft worden geadministreerd als uitgangspunt te nemen, welke op een aantal punten afwijken van het informatiemodel uit de Pilots Open Raadsinformatie. 
In onderstaand figuur is het informatiemodel uitgewerkt. Centraal staan ‘Raadsstuk’ en ‘Vergadering’. De raadsstukken zijn alle stukken die door de gemeenteraad behandeld worden, zoals: amendement, motie, voorstel, antwoord, ingekomen stuk en mededeling. Het ‘Raadsstuk’ is afgeleid van het generieke RGBZ-type ‘DOCUMENT’, en kent de attributen van dit type. In een ‘Vergadering’ worden meerdere agendapunten besproken, waarbinnen steeds een aantal raadsstukken behandeld kunnen worden. Ook kan er bij een bepaald ‘Agendapunt’ een ‘Stemming’ plaatsvinden, die weer een bepaald ‘Raadsstuk betreft’. Stemming is overgenomen uit Pilots Open Raadsinformatie, maar wordt op het moment van schrijven niet vanuit het RIS ondersteund. Er kunnen video-opnames zijn van hele vergaderingen, of van individuele agendapunten van vergaderingen.
Raadsstukken kunnen 0 of meer indieners hebben. Raadstukken met 0 indieners zijn procedurele stukken zoals de agenda en de lijst ingekomen stukken. Een ‘Indiener’ kan een ‘Raadslid’, een ‘Collegelid’ of een generiek ‘RECHTSPERSOON’ zijn. De laatste variant wordt gebruikt als een burger, een bedrijf of een instelling een stuk instuurt. Zowel ‘Raadslid’ als ‘Collegelid’ zijn afgeleid van ‘INGEZETENE’ uit de RSGB. 

![Gegevensmodel Griffie][gegevensmodelGR]

Vergaderingen hebben meerdere Aanwezige Deelnemers. Een ‘Aanwezige Deelnemer’ kan een ‘Collegelid’, een ‘Raadslid’ en een ander ‘NATUURLIJK PERSOON’ zijn. Een ‘NATUURLIJK PERSOON’ wordt gebruikt als een derde (burger of vertegenwoordiger) inspreekt op een vergadering. Hier wordt geen gebruik gemaakt van ‘RECHTSPERSOON’ omdat alleen natuurlijke personen kunnen spreken. Eventuele bedrijven of organisaties die vertegenwoordigd worden staan opgenomen in ‘Deelnemer’.
Commissies kunnen meerdere Raadsleden als lid hebben, bovendien hebben Commissies vergaderingen.
Raadsstukken kennen categorisering om de vindbaarheid te vergroten. Deze is opgenomen in onderstaand figuur. Hierin is te zien dat Raadsstukken bij meerdere dossiers kunnen horen, een ‘Categorie’ kunnen hebben, een ‘Taakveld’ kunnen hebben en kunnen horen bij meerdere Programma’s.

![Gegevensmodel Raadsstukken][gegevensmodelRaadsstukken]

[gegevensmodelGR]: image/EAID_A9F0B77B_05F3_4c36_96A0_8841BBAE47E0.gif "Gegevensmodel Griffie"
[gegevensmodelRaadsstukken]: image/EAID_108224FC_E160_417a_AFC5_68A484B3B8AE.gif "Gegevensmodel Raadsstukken"
