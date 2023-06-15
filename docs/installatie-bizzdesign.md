# Installatie Gemeentelijk Gegevensmodel in Bizzdesign

Het Gemeentelijk Gegevensmodel (GGM) kan als [XMI-vorm](https://www.omg.org/spec/XMI/About-XMI/) worden geïmporteerd in een bestaand project in [Bizzdesign](https://bizzdesign.com). Hiervoor wordt een apart script gebruikt dat Bizzdesign speciaal voor het GGM beschikbaar heeft gesteld.

## GGM importeren in Bizzdesign

Hieronder de te nemen stappen om het in een nieuw 
project binnen Bizzdesign te importeren.

1\. Download het bestand [Gemeentelijk Gegevensmodel XMI2.1.2](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/Gemeentelijk%20Gegevensmodel%20XMI2.1.2.xml)

2\. Start Bizzdesign

3\. Open een nieuw modelpackage met een leeg UML-model, of voeg een leeg UML-model toe aan een bestaand modelpackage

![Open een nieuw modelpackage][Bizzdesign_stap1]

4\. Selecteer het UML-model, en open de query-editor met ctrl-Q. Kopieer de inhoud van het scriptbestand [UML XMI import Bizzdesign.txt](https://gemeente-delft.github.io/Gemeentelijk-Gegevensmodel/UML%20XMI%20import%20Bizzdesign.txt) in de query-editor. Sla eventueel het script op in het model.

![Selecteer het UML-model][Bizzdesign_stap2]

5\. Voer het script uit via de Execute-knop van de query-editor, en kies het XMI-bestand 'Gemeentelijk Gegevensmodel XMI2.1.2' dat je net hebt gedownload. De inhoud wordt geïmporteerd in het geselecteerde UML-model.

6\. Even wachten….

7\. Succes!

[Bizzdesign_stap1]: image/Bizzdesign_stap1.png "Open een nieuw modelpackage"
[Bizzdesign_stap2]: image/Bizzdesign_stap2.png "Selecteer het UML-model"
