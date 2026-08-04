---
hide:
  - toc
---

# GGM x Kennispunt Twente: Opensource Tooling

Kennispunt Twente heeft samen met de gemeenten Rijssen-Holten en Oldenzaal gewerkt aan de implementatie van het Gemeentelijk Gegevensmodel (GGM). Beide gemeenten gebruiken dezelfde bronapplicatie voor data in het sociaal domein (Centric Suite voor Sociaal Domein), maar hanteren een andere datawarehouse-architectuur (Postgres versus Microsoft SQL Server). De centrale vraag was: hoe ontwikkelen we één gezamenlijke implementatie-aanpak die herbruikbaar is voor meerdere gemeenten, zelfs als ze een andere data-architectuur hanteren?

Het GGM beschrijft het doelbeeld: welke tabellen en kolommen er zijn en hoe die zich tot elkaar verhouden. Als gemeenten dezelfde bronapplicatie gebruiken, kunnen ze onderling mappings delen (“veld X uit de bron hoort bij veld Y in het GGM”). In de praktijk stopt het daar niet: zo’n mapping moet ook technisch worden uitgevoerd in een ETL/ELT-proces. In deze pilot wilden we daarom niet alleen de mapping delen, maar ook de technische implementatie ervan.

Dat leidde tot ‘SQLMESH_2_GGM’: een open-source datapijplijn naar het GGM, gebouwd met Python en de packages ‘dlt’ (verantwoordelijk voor het laden van de data uit de bronapplicatie) en ‘SQLMesh’ (verantwoordelijk voor het transformeren van de brondata naar het GGM). Omdat beide componenten met diverse SQL-databases overweg kunnen, is dezelfde code inzetbaar bij gemeenten met uiteenlopende datawarehouse-keuzes. Daarmee wordt één gedeelde implementatie haalbaar, ook bij technische verschillen.

Door dit open-source te maken, kan iedere gemeente de tool gebruiken ongeacht welke tooling er al in huis is. Er zijn geen betaalde licenties nodig en code is vrij aanpasbaar als een gemeente bijvoorbeeld een andere selectie tabellen wil of met een andere bron werkt. Tegelijk ontstaat een gedeelde basis: als één partij met deze tool mappings uitbreidt of verbetert, profiteren andere gemeenten daar ook van. De tool is zoveel mogelijk ‘plug-and-play’: nadat je de connectiegegevens van je bronapplicatie en SQL-database hebt ingesteld, kan je direct je gegevens onderbrengen in het GGM.

De rol van Kennispunt Twente is in dit project verbindend. Enerzijds door gemeenten bij elkaar te brengen rond het GGM en gezamenlijk behoeften en use-cases scherp te krijgen, anderzijds door de technische expertise te leveren om van ideeën ook daadwerkelijk werkende, open-source code te maken. Kennispunt Twente bewaakt de opzet als gedeelde, herbruikbare bouwsteen, zorgt dat de pijplijn bruikbaar blijft met verschillende architecturen en beheert de open-source code als centraal punt waar ervaringen, verbeteringen en uitbreidingen kunnen samenkomen.

Het project toont dat één gezamenlijke GGM-implementatie mogelijk is, zelfs met verschillende technische architecturen. Daarmee is door Kennispunt Twente en de gemeenten een gedeelde basis neergelegd, die andere gemeenten hergebruikt kan worden en verder uitgebouwd kan worden.

Ben je benieuwd naar SQLMESH_2_GGM en hoe je dit zou kunnen inzetten? Meer informatie staat op de GitHub-repository. Voor technische vragen: neem contact op met Luka Koning (l.koning@kennispunttwente.nl)  en Joost Barink (j.barink@oldenzaal.nl) of open een issue op de GitHub-repository. Voor vragen inzake (gemeentelijke) samenwerking: neem contact op met Jos Quist (j.quist@kennispunttwente.nl), Fabian Klaster (f.klaster@rijssen-holten.nl) en Joost Barink (j.barink@oldenzaal.nl).