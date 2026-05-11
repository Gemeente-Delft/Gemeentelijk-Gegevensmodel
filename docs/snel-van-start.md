# Technische Quick-Start Guide

> **Implementeer het GGM in jouw technische omgeving.**

Klaar om te bouwen? Deze gids helpt je om binnen een uur de eerste structuren van het GGM in je eigen database of modelleer-omgeving te krijgen.

## Stappenplan

### Stap 1: Voorbereiding
Zorg dat je toegang hebt tot:

1. **Onze GitHub Repository:** [Github GGM](https://github.com/Gemeente-Delft/Gemeentelijk-Gegevensmodel/)
2. **Modelleersoftware:** Bij voorkeur Enterprise Architect (EA), maar de documentatie is ook via de browser toegankelijk.

### Stap 2: Het model verkennen
Download het meest recente ```.eapx``` of ```.qea``` bestand van GitHub. Open dit in Enterprise Architect.

- Navigeer naar de map ```Domeinen```.
- Bekijk de Koppelvlakken om te zien hoe landelijke standaarden (RSGB/RGBZ) zijn geïntegreerd.

### Stap 3: Schema generatie
Wil je een database inrichten op basis van het GGM? Gebruik onze scripts:

- Ga naar de folder ```Scripts/DDL```.
- Kies het script voor jouw database-type (PostgreSQL, SQL Server, of Oracle).
- **Let op:** Je kunt ervoor kiezen om het gehele model te genereren of alleen specifieke domeinen (bijv. 'Inburgering').

### Stap 4: Mappings raadplegen
Hoe krijg je data uit je bronsysteem in deze nieuwe structuur?
- Bekijk de [Mapping-tabel](https://wiewatstatus.web.app/) en [Mapping-pagina](https://github.com/Gemeente-Delft/GGM-Mappings). Hier vind je hoe velden uit populaire gemeentelijke applicaties (bijv. van Centric of PinkRoccade) vertaald worden naar het GGM.

---

## Hulp nodig?
- **Vragen over de techniek?** Open een issue op onze GitHub.
- **Sparren met collega's?** Stel je vraag op de GGM Community op Pleio.
- **Cookbook:** Voor geavanceerde modellering-tips, zie het GGM Cookbook.