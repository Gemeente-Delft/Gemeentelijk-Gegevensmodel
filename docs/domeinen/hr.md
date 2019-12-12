# HR (Human Resources)

Het beleidsdomein HR kent de volgende uitwerking.

![Gegevensmodel HR][gegevensmodelHR]

Centraal staat de ‘Werknemer’ die 1 of meer ‘Aanstellingen’ heeft, en daarnaast: ‘Verlof’, ‘Verzuim’ en een individueel keuzebudget. Deze laatste 3 hebben allemaal stamgegevens, waarin verschillende soorten zijn gedefinieerd. Zoals verschillende soorten verlof: zwangerschapsverlof, ouderschapsverlof, bijzonder verlof en regulier verlof.
Een ‘Aanstelling’ is voor een bepaalde functie en hoort bij een ‘Afdeling’, deze kan op meerdere locaties zijn. Een ‘Functie’ hoort bij een ‘Functiehuis’, waarin de opbouw van de verschillende functies voor een bepaalde periode staat omschreven.  
Een ‘Werknemer’ kan meerdere beoordelingen hebben, welke worden beoordeeld door een leidinggevende, ook een ‘Werknemer’.

![Sollicitaties HR][sollicitaties]

In bovenstaand figuur staat de ‘Sollicitatie’ beschreven, welke altijd is op een ‘Vacature’. Een ‘Vacature’ hoort altijd bij 1 functie en kan meerdere vacatureteksten hebben. ‘Sollicitanten’ doen ‘Sollicitaties’ en kunnen meerdere gesprekken hebben, waarbij 1 of meer ‘Werknemers’ betrokken zijn.

![Documenten HR][documentenHR]

Het HR-model gebruikt niet direct ‘DOCUMENT’ uit RGBZ, maar alleen afgeleide documenten. Er kunnen verschillende typen documenten gebruikt worden: ‘Arbeidsovereenkomst’, ‘Personeelsdocument’ waarin allerlei personeelsafspraken staan vastgelegd en kan gebruikt worden voor andere communicatie en ‘Vacaturetekst’.

![Personen en HR][personenHR]

Het HR-model gebruikt niet direct personen, zoals gedefinieerd in de RSGB, alleen afgeleide entiteiten. In voorgaand figuur is te zien hoe het entiteit ‘Werknemer’ en de daaraan gekoppelde entiteit ‘Relatie’ zijn gedefinieerd.

[gegevensmodelHR]: image/EAID_891372E6_27FB_442d_9CC4_08C2659E8C53.gif "Gegevensmodel HR"
[sollicitaties]: image/EAID_542C38C9_B92F_48de_87F1_F90F64FB5913.gif "Sollicitaties HR"
[documentenHR]: image/EAID_E8C1CCDA_FF3C_498a_8FC9_FD6E461092FA.gif "Documenten HR"
[personenHR]: image/EAID_6409BBCD_026C_40ea_BC54_EE3B816D8CAB.gif "Personen en HR"
