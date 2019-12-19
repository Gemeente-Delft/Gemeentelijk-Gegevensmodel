# Verkeer

De gegevensdefinities voor verkeer sluiten aan op die van Ruimte. Een aantal objecttypen uit [Informatiemodel Beheer Openbare Ruimte (IMBOR)](https://www.crow.nl/thema-s/management-openbare-ruimte/imbor) worden bij verkeer hergebruikt. Het gaat hier om de beheerobjecten:

1. Paal (verkeerslicht is een verbijzondering van Paal);
2. Sensor (de lussen in het wegdek zijn een verbijzondering van Sensor);
3. Kast (de verkeersregelinstallaties zijn een verbijzondering van Kast).

ovenstaande objecttypen zijn in het GGM uitgewerkt in het onderdeel [Ruimte](ruimteAlgemeen.md#beheerobjecten). In de volgende figuur is te zien hoe het type ‘Verkeerstelling’ en het type V-log-info worden gegenereerd door deze drie objecttypen.

![Gegevensmodel Verkeerstellingen][tellingen]

In de attributen van V-log-info en verkeerstelling is te zien dat V-Log-info meer informatie kan bevatten. In de volgende figuur zijn de verschillende attributen van de V-Log-objecttypes te zien.

![Attributen V-Log][vlog]

Stremmingen staan afgebeeld in de volgende figuur. Het objecttype ‘Stremming’ betreft een aantal wegdelen en wordt ingevoerd of gewijzigd door een ‘Medewerker’. Iedere ‘Stremming’ heeft een aantal kenmerken:

1. Hindercategorie;
2. Aantal gehinderden;
3. Hinderklasse;
4. Stremmingstatus.

![Verkeer Stremmingen][stremmingen]

Verkeersbesluiten zijn vastgelegd in een ‘Document’.

![Gegevensmodel Verkeersbesluiten][verkeersbesluit]

[vlog]: image/vlog.png "Attributen V-Log"
[tellingen]: image/EAID_49A15BF5_AB98_4ab9_AE01_D5636641F455.gif "Gegevensmodel Verkeerstellingen"
[stremmingen]: image/EAID_72A4FC74_EE1B_4bc1_B5BB_540FCE4D04B1.gif "Verkeer Stremmingen"
[tellingen]: image/EAID_49A15BF5_AB98_4ab9_AE01_D5636641F455.gif "Gegevensmodel Verkeerstellingen"
[verkeersbesluit]: image/EAID_280799E6_5FC1_4cd0_90E6_F4DB9C7A78A3.gif "Gegevensmodel Verkeersbesluiten"
