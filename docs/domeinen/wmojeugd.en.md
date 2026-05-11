# Data Definitions — Wmo and Youth

Since the data definitions of the Wmo (Social Support Act) and the Youth Act are very similar, a generic data model is used for both. Like the other models in the social domain, the Wmo / Youth data model is built around the [*Client*](socdomeingeneriek.en.md) object type.

The next figure shows this generic data model. The applicable act is distinguished via the attribute *wet*, included in the following entities: *Beschikking*, *Voorziening*, *Toewijzing*, *Voorzieningssoort*, *Voorzieningscategorie*, *Prijs*, *Leveringsvorm*, *Beperking*, *Beperkingsscore*, *Beperkingssoort* and *Beperkingsscoresoort*.

![Decisions and provisions Wmo and Youth][sociaalBeschikkingenEnVoorzieningen]

<em>Diagram (in Dutch): data model for Wmo and Youth — Decisions, Provisions, Assignments, Deliveries, Declarations.</em>

In the *Decision* (Beschikking), together with the linked *Granted Provisions*, the municipality indicates which provisions the client may use. Via *Assignment* the granted care is assigned to a *Supplier* who, based on that assignment, does *Deliveries* and submits *Declarations*. *Granted Provisions* are of a particular *Provision* (such as home help, a scoot-mobile or a home adaptation), for which price agreements are made with the *Supplier*, recorded in *Tariff*.

The municipality sends an *Own-contribution Notification* to the CAK so the CAK collects the monthly own contribution. This is based on the system introduced in 2019 where a four-weekly own contribution of at most €17.50 per month is due (raised to €19.00) — i.e. no more own contributions tied to the provision.

A *Granted Provision* has a particular delivery form: ZIN (*Zorg in Natura* / care-in-kind) or PGB (*Persoonsgebonden Budget* / personal budget). If the care is provided as PGB, the client receives a budget (recorded in *Granted Provision* in euros). For processing, the municipality sends a TBK message to the SVB for further handling. This information is recorded in *PGB Grant*, with associated periodic *Budget Usage*.

![Limitations in Wmo and Youth][sociaalBeperkingen]

<em>Diagram (in Dutch): limitations and their scoring in the Wmo/Youth model.</em>

A *Client* may have multiple *Decisions* based on one or more limitations scored via a *Limitation Score*. Both *Limitation* and the score come from a reference table. In Wmo decisions, one or more provisions are granted from the list of provisions the Municipality of Delft supports.

At the time of writing, Delft does not use the limitations, but because they are formally part of the underlying standards, the definitions are included.

The Wmo/Youth domain model builds on the generic social-domain data model. It relies on data definitions from [iWmo](https://www.istandaarden.nl/iwmo), [iJw](https://www.istandaarden.nl/ijw) and [iPgb](https://www.istandaarden.nl/ipgb), which describe message traffic between municipalities and care providers.

[sociaalBeperkingen]: image/EAID_9B278A50_862A_4085_B362_C41392101916.jpg "Limitations in Wmo and Youth"
[sociaalBeschikkingenEnVoorzieningen]: image/EAID_5AE29494_3572_4924_B2B8_3206E55D71BB.jpg "Decisions and provisions Wmo and Youth"
