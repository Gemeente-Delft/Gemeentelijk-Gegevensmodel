# Generieke definities Sociaal Domein

Binnen het Sociaal Domein is één objecttype ‘Client’ waaraan alle dienstverlening is gekoppeld. Zo is het sociaal domein losgekoppeld van de andere domeinen en kan persoonsgebonden informatie apart toegankelijk gemaakt worden. 

## Huishouden

Er maakt tenminste 1 Natuurlijk Persoon deel uit van een Huishouden, en een Natuurlijk Persoon heeft maximaal 1 huishouden. Een Huishouden heeft altijd precies 1 adres. Er is gekozen het huishouden te koppelen aan Natuurlijk Persoon zodat ook niet geregistreerde personen deel kunnen uitmaken van een huishouden. Daarnaast is het Huwelijk of Geregistreerd partnerschap gekoppeld aan Natuurlijk Persoon en zijn de Groepsattribuutsoorten Sluiting en Ontbinding aan het Huwelijk gekoppeld.

![Gegevensmodel Client, Huishouden en huwelijk][huishouden]

## Sociale Relaties en Sociale Groepen

We introduceren Sociale Relatie en Sociale Groep en koppelen die aan Natuurlijk Persoon. We introduceren de rol die iemand in de Sociale Relatie met iemand anders heeft.
-	De buurman
-	Hangjongerengroep in het winkelcentrum
-	Lid van voetbalvereniging
-	Lid van motorbende
-	De scope van de mensen waar deze casus, dit plan betrekking op heeft

![Gegevensmodel Sociale relaties][socialerelaties]

## Gezagsverhouding

De gezagsverhouding definieert het gezag over een persoon. Hierbij is het belangrijk onderscheid te maken tussen gezag over een minderjarige en over een meerderjarige. De gezagsverhouding kan gebaseerd zijn op een Gerechtelijke uitspraak.

![Gegevensmodel Gezagsverhouding][gezagsverhouding]

### Gezag minderjarige

In Nederland zijn er verschillende vormen van gezag mogelijk over een kind, die bepalen wie verantwoordelijk is voor de verzorging en opvoeding van het kind, wie het kind wettelijk mag vertegenwoordigen en beslissingen mag nemen over belangrijke zaken zoals onderwijs en medische behandelingen. De belangrijkste vormen van gezag zijn:

1.	Ouderlijk gezag: Dit is het meest voorkomende type gezag, uitgeoefend door één of beide ouders. Ouderlijk gezag kan gezamenlijk door beide ouders worden uitgeoefend of alleen door één ouder, afhankelijk van de situatie na bijvoorbeeld een scheiding.
2.	Voogdij: Wanneer geen van de ouders het gezag kan of mag uitoefenen, bijvoorbeeld door overlijden of ontzetting uit het ouderlijk gezag, kan een voogd worden aangewezen. De voogd neemt dan de verantwoordelijkheid voor de verzorging en opvoeding van het kind op zich.
3.	Gezamenlijk gezag door ouder en niet-ouder: Naast de ouders kan ook een niet-ouder gezamenlijk gezag over een kind uitoefenen. Dit moet dan wel door de rechter worden toegewezen, bijvoorbeeld in het geval van een stiefouder of een andere nauw betrokken persoon bij de opvoeding van het kind.
4.	Gedeeld gezag door twee niet-ouders: In uitzonderlijke gevallen kan het gezag over een kind ook worden toegekend aan twee personen die niet de biologische ouders zijn. Ook dit vereist een beslissing van de rechter.

Elke vorm van gezag is bedoeld om het welzijn en de belangen van het kind te beschermen en te waarborgen, en wordt vastgelegd in het gezagsregister dat wordt beheerd door de Rechtbank.
In Nederland kunnen maximaal twee personen gezag hebben over een kind. Dit kan een combinatie zijn van ouders (biologisch of adoptief) of een ouder en een niet-ouder (bijvoorbeeld een stiefouder) die gezamenlijk gezag uitoefenen, of in uitzonderlijke gevallen twee niet-ouders. De wet is ingericht om ervoor te zorgen dat er niet meer dan twee personen tegelijkertijd het gezag over een kind uitoefenen, om de besluitvorming en verantwoordelijkheid duidelijk en overzichtelijk te houden.
In Nederland kan het gezag over een kind inderdaad ook aan een instantie worden toegekend, niet alleen aan natuurlijke personen. Dit gebeurt in de vorm van voogdij. Wanneer geen van de ouders het gezag kan uitoefenen en er geen geschikte voogd onder de natuurlijke personen gevonden kan worden, kan een instelling door de rechter worden benoemd tot voogd. Dergelijke instellingen zijn vaak gespecialiseerd in de zorg voor minderjarigen en kunnen bijvoorbeeld een jeugdzorginstelling of een andere door de overheid aangewezen organisatie zijn. Deze vorm van voogdij zorgt ervoor dat het kind de nodige verzorging en opvoeding krijgt, ook als er geen geschikte individuele voogd beschikbaar is.

### Gezag meerderjarige 

Bij meerderjarigen in Nederland wordt niet gesproken over gezag, maar over mentorschap, bewindvoering, of curatele. Deze maatregelen zijn bedoeld om volwassenen te beschermen die niet in staat zijn om geheel of gedeeltelijk voor zichzelf te zorgen of hun financiële zaken te regelen. Deze maatregelen kunnen worden ingesteld voor personen die vanwege hun geestelijke toestand of wegens verkwisting of het hebben van problematische schulden, beperkt zijn in hun capaciteit om hun belangen behoorlijk waar te nemen.
1.	Mentorschap is bedoeld voor mensen die niet in staat zijn om zelf beslissingen te maken over persoonlijke zaken, zoals verzorging, verpleging, behandeling, of begeleiding. Een mentor neemt in deze zaken beslissingen namens de betrokkene.
2.	Bewindvoering richt zich op financiële zaken en wordt ingesteld voor mensen die hun financiën niet zelf kunnen beheren. Een bewindvoerder beheert dan het vermogen van de betrokkene.
3.	Curatele is een combinatie van mentorschap en bewindvoering en is de meest vergaande maatregel. Een persoon onder curatele wordt juridisch onbekwaam verklaard om over persoonlijke zaken en financiële zaken te beslissen. De curator neemt beslissingen over zowel de financiële als persoonlijke zaken van de betrokkene.

Deze maatregelen moeten door de rechter worden ingesteld, en het is mogelijk dat een natuurlijke persoon of een professionele instantie (zoals een stichting) de rol van mentor, bewindvoerder, of curator op zich neemt. Het doel van deze maatregelen is om de belangen van de meerderjarige te beschermen en te bevorderen.

[sockern]: image/EAID_D7287848_8118_4aab_8823_D555A599063C.jpg "Gegevensmodel Generieke entiteit Relaties tot kern"
[socclient]: image/EAID_FD6966FF_E4FC_437d_983E_71B33445A62C.jpg "Gegevensmodel Generieke entiteit Client, huishouden en relaties"
[huishouden]: image/EAID_CABB9F3F_A6ED_479a_A175_6F61BE2BE8F8.jpg "Gegevensmodel Huishouden"
[gezagsverhouding]: image/EAID_227EBDFE_6FD0_4a47_85A4_FAC4AEFE003E.jpg "Gegevensmodel Gezagsverhouding"
[socialerelaties]: image/EAID_69607C8F_8048_4516_BE75_80C681DFEAC0.jpg "Gegevensmodel Sociale relaties"
