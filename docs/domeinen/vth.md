# Vergunningverlening, toezicht en handhaving

Voor de gegevensdefinities wordt voortgebouwd op het RSGB (Gemeentelijk informatiemodel met ondermeer gegevens uit de basisregistraties), RGBZ (Gemeentelijk gegevensmodel voor zaakgericht werken), en [RiHA 2.0  (Gegevensmodel toezicht en handhaven)](https://www.pleio.nl/pages/view/52755822/riha-referentieinformatiemodel-handhaving). Het gegevensmodel RiHA biedt feitelijk een vertaling van het RGBZ met verwijzingen naar het RSGB, waardoor de objecttypen uit het RGBZ niet goed generiek herbruikbaar zijn binnen het Gemeentelijk Gegevensmodel. Om binnen het Gemeentelijk Gegevensmodel zoveel mogelijk eenduidigheid te houden is gekozen om zoveel mogelijk het RGBZ te gebruiken en aanvullingen te doen vanuit het RiHA. RiHa is te zien in het volgende figuur.

![Aanpak GGM 1][riha]

Om de objecttypen uit RiHA zo goed mogelijk toe te passen, en te laten aansluiten op het RGBZ zijn de volgende keuzes gemaakt:

1. Entiteit Toestemming uit RiHA gemodelleerd als RGBZ-objecttype Besluit
    1. Toegevoegd aan Besluit attribuut Besluitsoort om type vergunning, ontheffing of melding in kwijt te kunnen. 
2. Entiteit Handhavingsobject uit RiHA gemodelleerd in RGBZ-objecttype Object
    1. Toegevoegd: Domein en Risico-indicatie
3. Onderverdeling in zaaktypen (Signaalzaak, Toezichtzaak,Handhavingszaak en Andere VTH-zaak) is niet overgenomen. Signalen zijn in model opgenomen in de vorm van AanvraagOfMelding, deze vormt de aanleiding voor de zaak. Onderscheid in toezicht- en handhavingszaken, en ook inspectietype, kan worden gemaakt in zaaktype. Wetsartikelen zijn niet gemodelleerd.

## Vergunningaanvragen

Vanwege het generiek karakter worden zijn de objecttypen in het kader van 'Bouwen en Wonen' en de overige vergunningen op dezelfde manier gemodelleerd. De afhandeling van aanvragen voor vergunningen, ontheffingen en meldingen binnen het VTH-domein maakt hergebruik van het informatiemodel uit de RGBZ. Centraal staan:

* VOMAanvraagOfMelding (Vergunning Ontheffing Melding Aanvraag of Melding): de aanvraag of de melding die door de indiener wordt ingediend;
* Zaak: de zaak waarin feitelijke afhandeling van de aanvraag of melding wordt gedaan;
* Object: het object, of de objecten, waar de aanvraag om gaat;
* Besluit: het besluit dat binnen de zaak n.a.v. aanvraag wordt gedaan, de vergunning of de afwijzing.

![Gegevensmodel vergunnings- en handhavingszaken][vthHandhaving]

In de voorgaande figuur is te zien hoe een ‘AanvraagOfMelding’ kan leiden tot een ‘ZAAK’. ‘AanvraagOfMelding’ is het generieke objecttype dat wordt gebruikt voor alle binnenkomende aanvragen en meldingen, waaronder de VJV’s. Hiervan is het VTH-specifieke ‘VOMAanvraagOfMelding’ afgeleid, waarvan weer ‘WABOAanvraagOfMelding’ is afgeleid specifiek voor alles in het kader van de WABO.
Een aanvraag heeft een ‘Indiener’ wat weer een natuurlijk of niet natuurlijk persoon kan zijn (‘RECHTSPERSOON’). Een ‘ZAAK’ kan meerdere betrokkenen hebben, en uit verschillende deelzaken bestaan, of betrekking hebben op andere zaken. Een zaak is van een bepaald ‘ZAAKTYPE’. De status van een ‘ZAAK’ wordt vastgelegd in ‘STATUS’ dat van een bepaald ‘STATUSTYPE’ is. Een BESLUIT is de uitkomst van een zaak. Zowel de aanvragen, de zaken en de besluiten kunnen een of meer documenten gekoppeld hebben.
  
Heffingen zijn vastgelegd in de Verordeningen, zoals de legesverordening en de precarioverordening die geldig zijn voor een bepaalde periode. Leges worden ook wel retributies genoemd. Een retributie wil zeggen een betaling aan de overheid waar een individueel aanwijsbare tegenprestatie van die overheid tegenover staat. Het gaat om een bedrag dat betaald moet worden aan de overheid (of aan een bevoegd gezag) voor het gebruik van hun diensten of producten. Precario zijn de vergoedingen die worden geheven voor het gebruik van openbare ruimte. Aan ieder ‘ZAAKTYPE’ is een ‘Heffingsgrondslag’ gekoppeld, op basis waarvan een ‘Heffing aan een bepaalde ‘ZAAK’ wordt gekoppeld.  De volgende soorten heffingen worden onderscheiden: leges, precario, reclamebelasting en liggelden.

![Koppeling zaken aan besluiten][vthZakenEnBesluiten]

De VTH-zaken, besluiten en aanvragen betreffen steeds een of meerdere objecten. Denk hierbij aan een aanvraag voor een ligplaatsontheffing. Deze verwijst naar een bepaald vaartuig en naar een bepaalde ligplaats. Dit in lijn met de opzet van RiHA (verwijzing naar HANDHAVINGSOBJECT) en RGBZ.  
Voorbeeld: een aanvraag en toekenning ligplaatsontheffing wordt het volgende:

* 1 VOMAanvraagOfMelding dat verwijst naar een Object met verwijzing naar een vaartuig.
* 1 Besluit van het type Ligplaatsontheffing
* 1 Ligplaatsontheffing met sticker-informatie
* 1 Object met verwijzing naar een LIGPLAATS
* 1 Object met verwijzing naar een Vaartuig

In Figuur 10 is te zien hoe het RGBZ-objecttype ‘Object’ verwijst naar allerlei objecttypen uit het Gemeentelijk Gegevensmodel (en vaak het RSGB). Op deze manier kan er in aanvragen, zaken en besluiten verwezen worden naar het abstracte type ‘Object’ waarvandaan naar allerlei concrete objecttypen verwezen kan worden.

![Objecten bij vergunningverlening][vthObjectenVergunning]

## Brede Handhaving

Ook meldingen in het kader van brede handhaving verwijzen naar het generieke objecttype ‘Object’, en zo dus weer naar allerlei andere objecttypen. Een ‘Melding’ kan verwijzingen naar foto’s hebben en heeft een BOA als verbalisant. Er worden drie soorten meldingen onderscheiden: ‘Waarneming’, ‘Combibon’ en ‘Fietsregistratie’. Een ‘Melding’ is afgeleid van het generieke ‘AanvraagOfMelding’.

![Objecten bij brede handhaving][vthObjecttypenBredeHandhaving]

[vthObjecttypenBredeHandhaving]: image/EAID_EC84A03C_FC04_401a_8263_7809B74179F8.gif "Objecttypen bij brede handhaving"
[vthObjectenVergunning]: image/EAID_C9CE09B7_32EF_40eb_9C82_7FD6EDEA1D9E.gif "Objecttypen bij vergunningverlening"
[vthZakenEnBesluiten]: image/EAID_A2BA1F0D_8428_42fc_80D6_7184F243D268.gif "Koppeling zaken aan besluiten"
[vthHandhaving]: image/EAID_BB52C835_0B2D_4164_AC9D_9D6EDBD7E267.gif "Gegevensmodel vergunnings- en handhavingszaken"
[riha]: image/riha.png "Gegevensmodel RiHa"