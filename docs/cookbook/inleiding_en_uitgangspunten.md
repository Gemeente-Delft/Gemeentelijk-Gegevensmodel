# GGM Cookbook: inleiding en uitgangspunten

Het Gemeentelijk Gegevensmodel (GGM) wordt steeds beter gemaakt en aangepast aan nieuwe behoeften en inzichten. Aanpassingen en uitbreidingen zijn essentieel om te passen bij de behoefte van de gebruikers, en ook om aan te sluiten bij steeds vernieuwend beleid en wetgeving en veranderende standaarden. 

Om te zorgen voor een kwalitatief hoogwaardig en beheersbaar model hanteren we uitgangspunten, die zijn verwoord in het **GGM Cookbook**. Deze uitgangspunten zijn vertaald in [toegepaste patronen](patronen.md), [toegepaste modelelementen](modelelementen.md) en afgeleide ontwerpregels. In de volgende onderdelen worden deze stap voor stap geïntroduceerd.

## Uitgangspunten kwaliteit

De belangrijkste uitgangspunten op het gebied van kwaliteit zijn:

1. **Een kwalitatief hoogwaardig, beheerbaar en uitbreidbaar GGM** door: 

    - **Eenduidigheid:** alle modelleurs werken volgens dezelfde standaarden en richtlijnen, waardoor het model begrijpelijk en uniform blijft.
    - **Kwaliteitsborging:** alle modelleurs werken volgende dezelfde standaarden en richtlijnen, wat de bruikbaarheid en betrouwbaarheid van het model vergroot.
    - **Beheersbaarheid:** uitbreidingen en wijzigingen kunnen eenvoudig worden beoordeeld, getoetst en opgenomen zonder de samenhang te verliezen. Ook zijn de verschillende domeinen zo gestructureerd dat ze makkelijk uit te breiden en te vervangen zijn. 
    - **Begrijpelijkheid:** door op dezelfde en op een voorspelbare manier te werken blijft het GGM leesbaar en bruikbaar voor alle gebruikers. 

## Uitgangspunten voor tooling

De belangrijkste uitgangspunten op het gebied van tooling zijn:

2. **Aansluiting bij de gebruikte tooling** waardoor deze de verwachte output genereert. Houden aan standaarden en richtlijnen zorgt ervoor dat het volgende correct blijft:

    - **DDL-/Linked Data-generatie:** de regels sluiten aan op de DDL-generator en andere tooling; deze ondersteunt bepaalde constructies wel en andere niet.  
    - **Documentatie:** documentatie wordt automatisch en op een consistente manier gegenereerd, wat de bruikbaarheid en betrouwbaarheid van het model vergroot.
    - **Koppeling GEMMA:** de koppeling met GEMMA werkt automatisch. Afwijkingen van standaarden en richtlijnen zorgt ervoor dat deze koppeling niet meer goed werkt.
    - **Vertalingen:** vertalingen naar andere talen gebeuren automatisch en zijn afhankelijk van de standaarden en richtlijnen.
