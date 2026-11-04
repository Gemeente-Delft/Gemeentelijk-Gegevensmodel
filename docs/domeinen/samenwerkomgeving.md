# Samenwerkomgeving

Het beleidsdomein Samenwerkomgeving beschrijft de digitale omgevingen waarin medewerkers van de gemeente, soms samen met externen, in teams samenwerken: Microsoft Teams en SharePoint, en in de toekomst mogelijk ook andere omgevingen zoals Nextcloud. Het model is ingebracht door de gemeente ’s-Hertogenbosch, in openbare consultatie geweest in mei en juni 2026 en op de expertgroep van 12 augustus 2026 aangenomen.

![Gegevensmodel Samenwerkomgeving][gegevensmodelSamenwerkomgeving]

Centraal staat het ‘Team’: een groep personen die samenwerkt in een of meer ‘Samenwerkomgevingen’. Wie in het team zit en met welke rechten, staat in het ‘Teamlidmaatschap’: de koppeling van een ‘Teamlid’ aan een ‘Team’ met een ‘Teamrol’ (eigenaar, lid of gast). Een ‘Teamlid’ kan een ‘Medewerker’ uit de Kern zijn, maar ook een externe; het e-mailadres identificeert beide op dezelfde manier. Als in een team een privékanaal wordt aangemaakt, ontstaat een nieuwe ‘Samenwerkomgeving’ met eigen leden.

Een ‘Samenwerkomgeving’ bestaat uit een of meer ‘Kanalen’, elk gewijd aan een onderwerp of deelgroep, waarin teamleden ‘Chatberichten’ uitwisselen. Daarnaast bevat een ‘Samenwerkomgeving’ ‘Bibliotheken’ met ‘Bestanden’ en ‘Lijsten’. Een ‘Lijst’ heeft een of meer ‘Inhoudstypen’, elk met ‘Kolommen’; de waarden per kenmerk zijn ‘Lijstitems’.

Een ‘Team’ heeft een gezamenlijke ‘Mailbox’ waarin de ‘Emailberichten’, de ‘AgendaItems’ van de teamagenda en de ‘Teamtaken’ van de takenlijst worden vastgelegd. Een ‘Teamtaak’ kan aan een ‘Teamlid’ zijn toegewezen.

Technische sleutels uit de bronapplicatie zijn niet opgenomen: de URL van een samenwerkomgeving, het e-mailadres van een teamlid of mailbox en de naam van een team zijn de functionele sleutels. Alle attributen gebruiken de datatypes uit het [MIM](../cookbook/modelelementen.md#ondersteunde-primitieve-datatypes).

[gegevensmodelSamenwerkomgeving]: image/EAID_8FAD3A01_3E43_4848_8621_B47FE3B5EA4F.jpg "Gegevensmodel Samenwerkomgeving"
