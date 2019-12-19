# Gemeentelijk Vastgoed

Het vastgoed van de gemeente betreft kadastrale onroerende zaken. Dit objecttype is overgenomen uit de Kern:RSGB. Voor deze onroerende zaken is het objecttype ‘Object’ gedefinieerd. Deze objecten kunnen uit bouwdelen en bouwdeelelementen bestaan. Alle objecten en bijbehorende bouwdelen en bouwdeelelementen worden opgenomen in een MJOP (Meerjarig Onderhoudsplan). Koppeling in het gegevensmodel verloopt via de MJOP-Items. Bij het feitelijk uitvoeren van werkzaamheden wordt een ‘Werkbon’ aangemaakt die de wordt gebruikt als opdracht voor werkzaamheden door een ‘Leverancier’. Een ‘Leverancier’ kan een aanbesteding hebben gewonnen.
Huurcontracten en koopcontracten worden volgens Kern:RSGB gemodelleerd via het objecttype ‘Zakelijk Recht’. Hieraan is danwel een eigenaar danwel een huurder gekoppeld. Beiden zijn ‘RECHTSPERSOON’ uit de Kern: RSGB.
Het ‘Object’ is gekoppeld aan een ‘Kostenplaats’ uit het financiële model en de ‘Werkbon’ hoort bij een ‘Verplichting’ uit het financiële model. Zo is de koppeling met financiën verankerd.
Bovenstaande is weergegeven in onderstaande figuren.

![Gegevensmodel Vastgoed][gegevensmodelVastgoed]

De relatie met leveranciers is weergegeven in onderstaand figuur.

![Vastgoed Leveranciers][vastgoedLeveranciers]

Het gemeentelijk vastgoed objecttype 'Vastgoedobject' is gekoppeld aan 'Kadastrale Onroerende Zaak'. Immers met het objecttype 'Vastgoedobject' wordt het bezit van een bepaald object weergegeven. Bezit van onroerende zaken is vastgelegd in de BRK, en beschikbaar via 'Kadastrale Onroerende Zaak'. Deze koppeling verloopt via een meer-op-meer-relatie, aangezien een bezit meerdere percelen kan beslaan, en er meerdere bezittingen op een perceel kunnen liggen (in het geval van appartementsrechten).
Aan een 'Kadastrale Onroerende Zaak' zijn 'Benoemde Objecten' gekoppeld, dit kunnen: 'Overig Gebouwd Object, Verblijfsobject', 'Standplaats', 'Ligplaats' of 'Overig Benoemd Terrein' zijn. Deze hebben op hun beurt een 'Nummeraanduiding', waarmee het adres kan worden bepaald.
De koppeling naar de eigenaar van een 'Kadastrale Onroerende Zaak' verloopt via het 'Zakelijk Recht' en de 'Tennaamstelling'. Er bestaan overigens ook andere soorten zakelijkrecht, zoals: recht van vruchtgebruik en recht van overpad.  

De Kadastrale objecttypen zijn [hier](ruimteAlgemeen.md#bag-basisregistratie-adressen-en-gebouwen) verder uitgewerkt, dus ik verwijs hier voor verdere informatie. Conform RSGB 3.0 ligt de 'Tennaamstelling' tussen 'Zakelijk Recht' en 'Rechtspersoon'. Ook is de relatie toegevoegd: 'Gesitueerd op' ([varkensoortje](../generatie.md#voorbeeld-c)) van 'Kadastrale Onroerende Zaak' met zichzelf. Dit om het gemakkelijk mogelijk te maken de bepalen op welk perceel een bepaald appartementsrecht ligt.

![Vastgoed Relatie tot RSGB][vastgoedRelatieRSGB]

[gegevensmodelVastgoed]: image/EAID_00D4246F_6ED7_4690_A180_ACCCD6AB1291.gif "Gegevensmodel Vastgoed"
[vastgoedLeveranciers]: image/EAID_06E44472_8C2A_40eb_9965_DCF91A1322C9.gif "Vastgoed Leveranciers"
[vastgoedRelatieRSGB]: image/EAID_35F1950E_923C_4a25_90B5_C67423B2C029.gif "Vastgoed Relatie tot RSGB"