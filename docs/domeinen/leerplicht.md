# Leerplicht en leerlingenvervoer

Leerplicht en leerlingenvervoer bouwen voort op het model van [onderwijs](onderwijs.md).

In onderstaand zijn de verschillende objecttypen uitgewerkt die gericht zijn op de leerplicht. Dit is aanvullend op de objecttypen uit de hiervoor beschreven algemene gegevensdefinities.

![Gegevensdefinities Leerplicht][leerplicht]

In voorgaande figuur zijn drie soorten meldingen en aanvragen te zien die leiden tot afhandeling door de ‘Leerplichtambtenaar’: ‘Verzuimmelding’, ‘Verlofaanvraag’ en ‘Aanvraagvrijstelling’. Deze zijn allemaal abstract weergegeven door ‘AanvraagOfMelding’, en betreffen altijd een ‘Leerling’, en kunnen een ‘School’ betreffen. Bij absoluut verzuim heeft de ‘leerling’ geen inschrijving op een school.
De ‘Leerplichtambtenaar’ handelt al deze ‘AanvraagOfMelding’en af en komt tot een ‘Beslissing’. Deze beslissing betreft altijd een ‘Leerling’ en kan een ‘School’ betreffen. Het kan een algemene ‘Beslissing’ zijn, of een variant van een beslissing: een ‘Vrijstelling’, een ‘Doorgeleiding OM’, een ‘HALT-verwijzing’ of een ‘Procesverbaal’. In het geval van een procesverbaal is deze gericht op Leerling en/of ‘Ouder of Verzorger’.  

[leerplicht]: image/EAID_26A453D9_47AF_487e_854B_3B4BC6D6A308.gif "Gegevensdefinities Leerplicht"