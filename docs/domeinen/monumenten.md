# Monumenten

Als kern in het entiteitenmodel monumenten staat ‘Beschermde Status’ Hierin zijn de gegevens en relaties uitgewerkt die geregistreerd staan over een monument. Dit buiten de gegevens die al de BAG (Basisregistratie Adressen en Gebouwen) en de BRK (Basisregistratie Kadaster). In de volgende figuur is uitgewerkt wat de relatie is met deze basisregistraties.

![Monumenten Gegevensdefinities][gegevensdefinitiesMonumenten]

In ‘Beschermde Status’ staan zaken opgenomen als: rijksmonumentcode en/of gemeentemonumentcode, datum opname in register, omschrijving en soort monument. Aan ‘Beschermde Status’ zijn gekoppeld (met per gekoppeld entiteit de attributen):

* ‘Bouwactiviteit’ (0 of meer): bouwjaar vanaf, bouwjaar tot, indicatie, omschrijving;
* ‘DOCUMENT’ (0 of meer): alle documenten behorende bij het monument;
* ‘Foto’ (0 of meer): alle beeldmateriaal van het monument;
* ‘Ambacht’ (0 of meer): ambachtsoort dat in het monument is uitgevoerd, jaar vanaf en jaar tot;
* ‘Bouwtype’ (0 of meer): hoofdcategorie, subcategorie en toelichting
* ‘Bouwstijl’ (0 of meer): hoofdstijl, substijl, zuiverheid en toelichting
* ‘Oorspronkelijke functie’ (0 of meer): functie, functiesoort en hoofdfunctie, hoofdcategorie, subcategorie en toelichting.

![Monumenten Gegevensdefinities en relatie tot kernentiteiten][gegevensdefinitiesMonumentenOnroerendeZaakpng]

Een ‘Beschermde Status’ kan één of meerdere ‘KADASTRALE ONROERENDE ZAAK’(en) betreffen, en ook één of meer stuk(ken) ‘Openbare Ruimte’ betreffen, zoals een (deel van een) straat of een stuk groen. Zowel ‘KADASTRALE ONROERENDE ZAAK’ als ‘Openbare Ruimte’ komen uit de RSGB en hebben een koppeling met de BAG, waardoor ze te relateren zijn aan informatie uit de basisregistraties. De terminologie uit de RSGB is hier aangehouden om aan te sluiten op de overige onderdelen uit het Gemeentelijk Gegevensmodel en op de basisregistraties. 

[applicatiesMonumenten]: image/Applicaties_Monumenten.png "Applicaties Monumenten"
[aanwijsbeschrijving]: image/Aanwijsbeschrijving.png "Aanwijsbeschrijving"
[monmumentenToezichtEnHandhaven]: image/MonumentenToezichtEnHandhaven.png "Monumenten Toezicht en handhaven"
[applicatiesEnGegevensMonumenten]: image/ApplicatiesEnGegevensMonumenten.png "Monumenten Applicaties en Gegevens"
[gegevensdefinitiesMonumenten]: image/EAID_58EA4966_DBC2_4359_94C4_ABC774DBE5E2.gif "Monumenten Gegevensdefinities"
[gegevensdefinitiesMonumentenOnroerendeZaakpng]: image/EAID_7429E175_1CBE_4336_BF92_6C5029395E69.gif "Monumenten Gegevensdefinities en relatie tot kernentiteiten"
