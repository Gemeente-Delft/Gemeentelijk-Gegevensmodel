# Afval

Centraal in het gegevensmodel van afval staan de fracties en de locaties. Een ‘Fractie’ is een type afval dat ingezameld wordt, zoals: PMD (Plastic, Metaal, Drank), OPK (Oud Papier Karton), Glas, of Restafval. Per ‘Fractie’ worden prijsafspraken vastgelegd in een ‘Prijsregel’, waarin staat opgenomen hoeveel in inzamelen van een kg kost of oplevert.

Om bepaalde fracties in te zamelen zijn er meerdere routes die door vuilniswagens gereden kunnen worden om deze fractie in te zamelen. Zo’n ‘Route’ gaat langs meerdere locaties. Een ‘Locatie’ is opgebouwd uit een adres en/of een X- en Y-coördinaat. Op het moment van schrijven onderkent Avalex hiervoor alleen adressen. De coördinaten zijn bijgevoegd om deze in de toekomst ook te kunnen ondersteunen. Routes die gereden worden om bepaalde fracties vuilnis op te halen. Afhankelijk van de routesoort worden containers, bepaalde plekken of adressen aangedaan:

* Routesoort, huis-aan-huis: er worden locaties met adressen aangedaan;
* Routesoort, illegale dumping, grofvuil: er worden locaties aangedaan (evt. met adres);
* Routesoort, containers: er worden locaties met containers aangedaan.

Containers zijn geschikt voor één ‘Fractie’ (glascontainer, papiercontainer, restafvalcontainer, etc.). Per container kunnen er meerdere vulgraadmetingen zijn waar per tijdstip is vastgelegd hoeveel procent de container vol is en hoeveel kg dat is. Containers zijn van een bepaald type, bijvoorbeeld: onderlossende container, minicontainer of verzamelcontainer.

Vuilniswagens zijn geschikt voor een bepaald containertype, en rijden ritten. Iedere ‘Rit’ die zo’, wagen rijdt is volgens een bepaalde ‘Route’. Een ‘Rit’ bestaat uit meerdere ophaalmomenten waar een op een bepaalde locatie, op een bepaald tijdstip een bepaalde hoeveelheid afval ingenomen wordt. Hierbij kan een ‘Container’ gelost worden, zo niet dan gaat het om afval (zoals grofvuil of illegale dumpingen) die van een bepaalde ‘Locatie’ gehaald worden.

![Afval Inzamelen][afvalInzamelen]

In de volgende figuur is te zien dat aan een ‘Adres’ een ‘Pas’ gekoppeld is die geldig is voor één of meer milieustraten (in de praktijk slechts één, maar er is rekening gehouden met uitzonderingen). Een ‘Milieustraat’ is inzamelpunt voor meerdere fracties. Met een ‘Pas’ kunnen stortingen gedaan worden bij een ‘Milieustraat’. Iedere ‘Storting’ kan steeds één ‘Fractie’ bevatten en heeft een bepaald gewicht.

![Milieustraat Afval][afvalMilieustraat]

In het hierna volgende figuur is het datamodel opgenomen voor de meldingen die bij Avalex afgehandeld worden.

![Meldingen afval][afvalMeldingen]

Een ‘Melding’ heeft steeds een hoofdcategorie en een subcategorie. Een ‘Melding’ kan een bepaalde ‘Fractie’ betreffen, en kan een bepaald ‘Containertype’ betreffen. Een ‘Melding’ betreft altijd een bepaalde ‘Locatie’. Meldingen zijn afgeleid van het generieke type ‘AanvraagOfMelding’.

[afvalInzamelen]: image/EAID_D98AA96C_2EB0_4b46_9E9C_09D55E02FE38.gif "Afval Inzamelen"
[afvalMeldingen]: image/EAID_157F610A_619E_4d1a_BB45_5C1F55178944.gif "Meldingen afval"
[afvalMilieustraat]: image/EAID_A00B8121_71AC_466f_B391_E16881240477.gif "Milieustraat afval"
