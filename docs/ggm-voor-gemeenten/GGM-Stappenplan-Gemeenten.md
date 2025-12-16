# Stappenplan voor implementatie van het GGM

Dit stappenplan helpt gemeenten bij het gefaseerd en doelgericht implementeren van het Gemeentelijk Gegevensmodel (GGM). Afhankelijk van je situatie kun je onderdelen overslaan of verdiepen.

## 1. Oriëntatie en verkenning

- Verken de principes van het GGM
- Gebruik de beschikbare documentatie 
- Bekijk praktijkvoorbeelden van andere gemeenten
- Bekijk de toepassingen van leveranciers
- Creeër draagvlak binnen de organisatie: Informeer collega’s over het doel en de meerwaarde van het GGM
- Breng de datastromen binnen de gemeenten in kaart 

## 2. Bepaal je vertrekpunt

- Kies een concreet domein en een concrete casus (bijv. vergunningverlening, meldingen openbare ruimte)
- Breng in kaart welke gegevens, processen en systemen hierbij betrokken zijn
- Stel vast welke informatiebehoefte er leeft binnen je organisatie omtrent deze casus
- Isoleer het desbetreffende deel van het GGM

## 3. Van logisch model naar technisch model
Hoe kom je van het logische model (UML) naar een technisch model?

- Met EA kan de tabelstructuur gegenereerd worden - [Lees meer over generatie](../generatie.md)
- Het technische model kan ook zelf ontworpen worden door het logische model te lezen en te interpreteren
- Bepaal welke entiteiten nodig zijn vanuit het model
- Na het genereren van de tabellen in EA vind je onder Tables het tabelschema met de technische tabellen 
- Je hebt dan een technisch model (ERD) van de logische GGM objecten
- Afhankelijk van de relaties tussen de entiteiten genereerd EA ForeignKeys of koppeltabellen
- Technisch kunnen er dus meer tabellen ontstaan dan dat er logisch zijn gemodeleerd 

> Probeer niet in één keer het volledige GGM in te lezen, maar deel met model op per domein. 

## 4. Mappings van bron naar GGM
Uiteindelijk wil je de data vertalen van de bronapplicatie naar het GGM. Dit noemen we mappings - [Lees meer over mappings](Mappings.md). Hierin wordt beschreven welk veld in de bron-database terecht komt in het veld van een GGM-entiteit.  

- Data uit de bronapplicatie moet worden getransformeerd naar de fysieke tabellen volgens het GGM
- Binnen een datawarehouse of dataplatform kan die transformatie op verschillende manieren gedaan worden
- Ook zonder een dataplatform of datawarehouse is deze transformatie prima te realiseren, bijvoorbeeld met behulp van database-views of de transformatie binnen een BI-tool te doen. 

## 5. GGM naar Dashboard
Het GGM is nu fysiek gerealiseerd in tabellen. Dit vormt de business layer of informatielaag in je datawarehouse.

- Gebruik deze laag als basis voor dashboards, rapportages en analyses
- Zorg dat definities en datakwaliteit geborgd zijn
- Koppel visualisaties aan GGM-entiteiten voor transparante verantwoording

 
