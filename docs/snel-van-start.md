# Technische Quick-Start Guide

> **Implementeer het GGM in jouw technische omgeving.**

Klaar om te bouwen? Deze gids helpt je om binnen een uur de eerste structuren van het GGM in je eigen database of modelleer-omgeving te krijgen.

## Stappenplan

### Stap 1: Voorbereiding
Zorg dat je toegang hebt tot:

1. **Onze GitHub Repository:** [Github GGM](https://github.com/Gemeente-Delft/Gemeentelijk-Gegevensmodel/)
2. **Modelleersoftware:** Bij voorkeur Enterprise Architect (EA), maar de documentatie is ook via de browser toegankelijk.

### Stap 2: Het model verkennen
Download het meest recente ```.qea``` bestand van GitHub. Open dit in Enterprise Architect (Gemeentelijk_Gegevensmodel.qea).

- Navigeer naar de map ```Domeinen```.
- Bekijk de verschillende domeinen of kies één domein waarmee je van start wilt 

Het Gemeentelijk Gegevensmodel is beschikbaar in [XMI-vorm](https://www.omg.org/spec/XMI/About-XMI/), en is ontwikkeld in, en toegepast met [Enterprise Architect](https://sparxsystems.com). Een aantal gemeenten gebruikt het GGM inmiddels ook met [Bizzdesign EnterpriseStudio](https://bizzdesign.com), en ook met [Blue Dolphin](https://www.valueblue.com/bluedolphin).

Gebruik je Enterprise Acrhitect versie 16 of 17:

- Gebruik het bestand: 'gemeentelijk gegevensmodel EA.qea' gebruiken. 

Gebruik je versie 15:

-  Gebruik het 'xmi' bestand.

> **Let op**: Het Gemeentetelijk Gegevensmodel is een [UML-model](http://www.uml.org) en bevat daarmee alle benodigde details zoals de attributen en bijbehorende datatypes. Er is ook een [Archimate-versie](https://prod.opengroup.org/archimate-forum/archimate-overview) beschikbaar die gebruikt wordt voor de GEMMA en die gebruikt kan worden voor Enterprise Architectuur; deze bevat echter niet alle details omdat Archimate niet hetzelfde detail kent als UML.    


### Stap 3: Schema generatie
Wil je een database inrichten op basis van het GGM? Gebruik onze scripts:

- Ga naar de folder ```Scripts/DDL```.
- Kies het script voor jouw database-type (PostgreSQL, SQL Server, of Oracle).
- **Let op:** Je kunt ervoor kiezen om het gehele model te genereren of alleen specifieke domeinen (bijv. 'Inburgering').

Voor het genereren van fysieke datamodellen op basis van het GGM is een set [codegeneratie templates](generatie.md) beschikbaar. Deze templates zijn ontwikkeld voor het [Code Template Framework](https://sparxsystems.com/enterprise_architect_user_guide/15.0/model_domains/codetemplates_2.html) van Enterprise Architect, en ondersteunen het genereren van DDL voor verschillende relationele databasesystemen (RDBMS’en), waaronder Oracle en MySQL. Waar nodig zijn aanvullende uitbreidingen gemaakt om het model praktisch toepasbaar te maken in diverse technische omgevingen.

> Het XMI-bestand van het Gemeentelijk Gegevensmodel is in theorie te gebruiken in andere tools naast Enterprise Architect, maar daar is geen ervaring mee. Ervaringen hierin zijn welkom!

### Stap 4: Mappings raadplegen
Hoe krijg je data uit je bronsysteem in deze nieuwe structuur? Hiervoor maken we gebruik van mappings. Hierin wordt beschreven welk veld in de bron-database terecht komt in het veld van een GGM-entiteit. 

Je kan gebruik maken van mappings die door gemeenten en/of leveranciers zijn opgesteld. Een lijst van mappings die al gemaakt zijn vind je in de [Mapping-tabel](https://wiewatstatus.web.app/). Voor sommige applicaties zijn de mappings al gepubliceerd, deze staan op GitHub [mappings](https://github.com/Gemeente-Delft/GGM-Mappings). 

---

## Hulp nodig?
- **Vragen over de techniek?** Open een issue op onze GitHub.
- **Sparren met collega's?** Stel je vraag op de [GGM Community op Pleio](https://kennisnetwerkdata.pleio.nl/groups/view/1e7df5c5-e537-46cd-9d09-de2ef29beef8/gemeentelijk-gegevensmodel-ggm).
- **Cookbook:** Voor modellering-tips, zie het [GGM Cookbook](cookbook/inleiding_en_uitgangspunten.md).