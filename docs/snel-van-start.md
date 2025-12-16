# Snel van start met het GGM 

De gemakkelijkste manier om te starten met het Gemeentelijk Gegevensmodel is via Enterprice Architect.

1. Installeer Enterprise Architect of de [viewer van Enterprise Architect](https://sparxsystems.com/enterprise_architect_user_guide/17.1/getting_started/ea_lite.html). 
2. Download het bestand 'Gemeentelijk_Gegevensmodel.qea'.
3. Open 'Gemeentelijk_Gegevensmodel.qua' met de Enterprise Architect.

## Installatie en gebruik

Het Gemeentelijk Gegevensmodel is beschikbaar in [XMI-vorm](https://www.omg.org/spec/XMI/About-XMI/), en is ontwikkeld in, en toegepast met [Enterprise Architect](https://sparxsystems.com). Een aantal gemeenten gebruikt het GGM inmiddels ook met [Bizzdesign EnterpriseStudio](https://bizzdesign.com), en ook met [Blue Dolphin](https://www.valueblue.com/bluedolphin).

Gebruik je Enterprise Acrhitect versie 16 of 17 ? In dit geval moet je het bestand 'gemeentelijk gegevensmodel EA.qea' gebruiken. Gebruik je versie 15, laad dan het bestand 'xmi' bestand.

> **Let op**: Het Gemeentetelijk Gegevensmodel is een [UML-model](http://www.uml.org) en bevat daarmee alle benodigde details zoals de attributen en bijbehorende datatypes. Er is ook een [Archimate-versie](https://prod.opengroup.org/archimate-forum/archimate-overview) beschikbaar die gebruikt wordt voor de GEMMA en die gebruikt kan worden voor Enterprise Architectuur; deze bevat echter niet alle details omdat Archimate niet hetzelfde detail kent als UML.    

### Installatie Gemeentelijk Gegevensmodel

Van het Gemeentelijk Gegevensmodel zijn verschillende versies beschikbaar: v1.0.3, v2.0.0, v2.1.0, v2.2.0, v2.3.0 en de courante versie v2.4.0. Je vindt deze in de afzonderlijke versies van de repository. De hierna volgende uitleg betreft de laatste versie van het GGM. Hieronder vind je de installatiebeschrijving bij de verschillende ondersteunde tools:

1. [Enterprise Architect Viewer](https://sparxsystems.com/products/ea/downloads.html) of [Enterprise Architect versie 16 of 17](https://sparxsystems.com/products/ea/17.1/index.html): download hiervoor het bestand [QEA-bestand](./v2.4.0/) en open het in (de viewer van) Enterprise Architect.
2. [Enterprise Architect versie 16](https://sparxsystems.com/products/ea/16.0/): de EAPX van versie 15 wordt niet meer ondersteund in de nieuwe release. Wil je het GGM alsnog in versie 15 laden, dan kan dat via het XMI bestand.
3. Als [XMI-bestand in Enterprise Architect 16 en 17](./v2.4.0/Gemeentelijk%20Gegevensmodel%20XMI2.1.xml), om geladen te worden in een (nieuw) project in Enterprise Architect, of om geladen te worden in andere UML-tooling. Voor installatie-instructies kijk in de [handleiding](./installatie.md).
4. [Bizzdesign](https://bizzdesign.com): voor installatie-instructies kijk in de [handleiding laden in Bizzdesign](./installatie/#installatie-gemeentelijk-gegevensmodel-in-bizzdesign) 
5. [Blue Dolphin](https://www.valueblue.com/bluedolphin): hiervoor gebruik je het [AMEFF-bestand](https://github.com/VNG-Realisatie/GEMMA-GGM-Archi-repository/blob/develop/exports/GEMMA-GGM%20AMEFF.xml) van het GGM uit de GEMMA-repository voor de Architectuur module van BlueDolphin. Als BlueDolphin gebruiker met Beheerderrol kun je AMEFF-bestanden uploaden. Zie hiervoor de [handleiding: AMEFF bestanden importeren](https://support.valueblue.nl/hc/nl/articles/360013407860-AMEFF-bestanden-importeren-naar-BlueDolphin). Bij vragen contacteer jouw ValueBlue account- of customersuccess-manager.

### Installatie Codegeneratietemplates

De installatie van de codegeneratietemplates staat [hier](./generatie#installeren-codegeneratietemplates) beschreven. Voor verdere uitleg rond het gebruik van de codegeneratietemplates kijk [hier](./generatie.md).

De codegeneratietemplates zijn alleen beschikbaar voor Enterprise Architect.

### Versies en gebruikte tooling

Het XMI-bestand van het Gemeentelijk Gegevensmodel is in theorie te gebruiken in andere tools naast Enterprise Architect, maar daar is geen ervaring mee. Ervaringen hierin zijn welkom!

Het Gemeentelijk Gegevensmodel is beschikbaar in:

* [XMI versie 2.1](https://www.omg.org/spec/XMI/About-XMI/)

Het is Getest en gebruikt in de volgende omgevingen:

* [Enterprise Architect versie 16](https://sparxsystems.com/products/ea/16.0/)
* [Enterprise Architect versie 17](https://sparxsystems.com/products/ea/17.0/)
* [Enterprise Architect Viewer](https://sparxsystems.com/products/ea/trial/request.html)
* [Bizzdesign EnterpriseStudio](https://bizzdesign.com)
* [Blue Dolphin](https://www.valueblue.com/bluedolphin)

