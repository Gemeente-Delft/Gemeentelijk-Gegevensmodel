# Income

This sub-domain is based on [GBI (Generic Basic Processes for Income)](https://vngr-gbi.gitlab.io/ontologie-inkomen/), of which several parts have been incorporated into the GGM:

1. *Norm deviation* — about lawfulness, i.e. measures and fines on deviations.
2. *Recovery and collection* — detailed model containing all claims and other corrections on persons.
3. *Reason for application* — the underlying reason for an income-provision application.
4. *Service model* — generic model with which income-related services can be shaped.

The basis of this sub-domain is `Income (Basic object types)`, supplemented with the GBI sub-models. These are described in the sections below.

!!! danger "Observation"

    The GBI Service model is not a concrete model. It needs further specification for specific municipal income services such as IOAW, IOAZ, social assistance and special social assistance, which are not currently part of the GBI ontology. The GGM does cover these, in a less advanced way, in the *Income (Basic object types)* sub-domain. *Norm deviation* and *Recovery and collection* are concrete models and can be used as-is.

## Income (Basic object types)

The *Income* information model offers a structured view of the data and relationships relevant within the social domain, specifically targeting income provisions. The model supports the administrative processes around benefits and income support. Like the other models in the social domain, it is built around the [object type *Client*](socdomeingeneriek.en.md). A client may have one or more income provisions such as social assistance, special social assistance or IOAZ.

![Income — Base model][inkomenbasis]

<em>Diagram (in Dutch): the base model for Income — UitkeringsRun, Component, Inkomensvoorziening, Regeling.</em>

### Main entities

1. **UitkeringsRun (Benefit Run)** — represents a process in which benefits are calculated and paid. A *UitkeringsRun* contains several components that together make up the benefit.
2. **Component** — a building block of a benefit, which can contain different kinds (allowances, deductions). Each component has a relationship with a *ComponentSoort* specifying its type.
3. **ComponentSoort (Component type)** — defines the type of a component, e.g. a basic benefit or a specific allowance.
4. **Inkomensvoorziening (Income provision)** — the central object representing income support, such as social assistance, special social assistance, IOAW or IOAZ. It consists of one or more components and has a relationship with an *InkomensvoorzieningSoort* indicating the type.
5. **InkomensvoorzieningSoort (Income-provision type)** — describes the various kinds of income provisions.
6. **Regeling (Scheme)** — linked to a registered person (client), describing the specific arrangements or conditions under which income support is granted. Always has a relationship with a *RegelingSoort* specifying the type of scheme.
7. **RegelingSoort (Scheme type)** — defines the type of scheme, e.g. general social assistance or specific support.
8. **Registered Person (Client)** — represents the person entitled to income support and possibly debt counselling.

### Relationships between entities

- A *UitkeringsRun* consists of one or more *Components*.
- A *Component* always has a *ComponentSoort* indicating the kind of building block.
- An *Inkomensvoorziening* consists of one or more *Components* and always has a relationship with one type of provision (*InkomensvoorzieningSoort*).
- A registered person (client) is entitled to one or more schemes (*Regeling*) within the social domain.
- Each scheme has a specific type (*RegelingSoort*).

### Application

The information model supports municipalities in carrying out their tasks under the Participation Act (*Participatiewet*). It provides insight into how income provisions are built up, managed and linked to clients, including the administrative processes around benefits and schemes — enabling consistent and efficient data processing.

### Examples of income provisions

The model covers various income provisions including:
- General social assistance (Bijstand)
- Special social assistance (Bijzondere bijstand)
- IOAW (income provision for older and partially disabled unemployed workers)
- IOAZ (income provision for older and partially disabled self-employed)

## GBI (Generic Basic Processes for Income)

[GBI](https://vngr-gbi.gitlab.io/ontologie-inkomen/) is a standardised set of processes and information flows used within Dutch social security to support the execution of income schemes. The GBI ontology provides a semantic framework defining relevant concepts, entities and their relationships, ensuring that different systems and processes within municipalities can communicate and collaborate uniformly. The ontology focuses on structuring and standardising information exchange, making the management of income processes more efficient and consistent — and enabling integration and reuse of data from different sources, raising service quality. GBI is an ontology translated into an information model. This model has been incorporated into the GGM and linked to generic object types such as persons, organisations and cases.

### GBI and GGM

To accommodate the object types and sub-domains for Income within the Social Domain, an *Income* sub-domain has been created. It contains the following GBI sub-domains:

1. Norm deviation;
2. Reason for application;
3. Recovery and collection;
4. Services.

These sub-domains link to the GGM as follows:

![Relationship between GBI and GGM][gbienggm]

<em>Diagram (in Dutch): how GBI sub-domains hook into the GGM.</em>

### Norm deviation

The *Norm deviation* part focuses on the registration and handling of situations where a deviation from set norms is established for income provisions. The figure visualises the model and the relationships between the object types involved.

![Norm deviation][normafwijking]

<em>Diagram (in Dutch): the Norm-deviation model and its measure subtypes (fine, deviating measure, measure on benefit).</em>

#### Object types and relationships

1. **Normafwijking (Norm deviation)** — central object representing a situation where a deviation from a norm has been established. May lead to one or more measures (*Maatregel*) depending on nature and severity.
2. **Maatregel (Measure)** — an action taken in response to a norm deviation. The model distinguishes:
   - **Afwijkende maatregel (Deviating measure)**: a specific measure deviating from standard procedures.
   - **Maatregel op uitkering (Measure on benefit)**: a measure with direct effect on the client's benefit, e.g. a deduction or adjustment.

   Each measure has a direct relationship to a norm deviation (one norm deviation may lead to at most one measure, *0..1*). A measure also generalises both *Boete* (Fine) and *Afwijkende maatregel*.
3. **Boete (Fine)** — a specific measure imposed as a sanction for a norm deviation, e.g. due to fraud or non-compliance.
4. **Afwijkende maatregel (Deviating measure)** — non-standard measures applied in exceptional situations. Always refers to a *Maatregel op uitkering*, directly linking it to the financial aspects of income provisions.
5. **Maatregel op uitkering (Measure on benefit)** — measures directly affecting the benefit (discount, deduction). Has a 1:1 relationship with both *Afwijkende maatregel* and general measures.

#### Relationships in the model

- A *Normafwijking* leads to at most one *Maatregel*.
- A *Maatregel* generalises both *Boete* and *Afwijkende maatregel* — these are specific kinds of measure.
- An *Afwijkende maatregel* always refers to a *Maatregel op uitkering*, linking deviations to financial actions.

### Reason for application

The *Reason for application* part focuses on the registration and categorisation of why a client applies for an income provision. It enables municipalities to record this in a structured way.

![Reason for application][redenaanvraag]

<em>Diagram (in Dutch): hierarchy of reasons for an income-provision application.</em>

#### Object types and relationships

1. **Reden aanvraag (Reason for application)** — central object representing the general reason for an income application; an umbrella concept generalising specific subtypes.
2. **Levensonderhoud (Subsistence)** — for situations where a client applies due to a lack of means of subsistence. Generalises specific reasons such as:
   1. **Stopped paid work** — the client no longer has work and applies for support.
   2. **Released from detention** — the client has been released and needs support.
   3. **Stopped benefit** — a previous benefit ended; new support is needed.
   4. **Broken relationship** — the client faces a relationship break-up with financial consequences.
   5. **Deceased partner** — the death of a partner causes financial hardship.
3. **Ingang bijstandsuitkering (Start of social-assistance benefit)** — describes the start of a social-assistance benefit and the underlying specific reasons.
4. **Reden afwijkende startdatum (Reason for deviating start date)** — situations where a benefit's start date deviates from the standard process. Generalises specific cases such as:
   1. **Awaiting decision by authority** — the client is waiting for an authority's decision.
   2. **Admission to institution** — the client is admitted to an institution, affecting the start date.
   3. **Awaiting DigiD** — delay due to missing or activating DigiD.
5. **Andere reden verzoek (Other reason)** — other reasons not falling under the standard categories, such as departure from an asylum-seekers centre.

#### Relationships in the model

- *Reden aanvraag* generalises multiple subtypes including *Levensonderhoud*, *Ingang bijstandsuitkering* and *Reden afwijkende startdatum*.
- Each subtype contains specific reasons (stopped work, detention, relationship break-up, …).
- *Reden afwijkende startdatum* is related to specific process situations (awaiting decisions, technical delays).

### Recovery and collection

The *Recovery and Collection* part focuses on the processes and data around recovering and collecting unjustly granted income provisions. The model gives a structured view of the object types and their relationships.

![Recovery and collection][terug]

<em>Diagram (in Dutch): claims, payment components, settlements, fines, repayment plans and debtors.</em>

#### Object types and relationships

1. **Vordering (Claim)** — central object representing a financial amount the municipality recovers from a client. May arise from situations such as wrongly received benefits or breaches of obligations.
   - A claim contains multiple components, such as *Rechtshandeling* (Legal act) and *Betaalcomponent* (Payment component), supporting administrative handling.
   - A claim generalises specific subtypes such as *Verrekening* (Settlement), *Afkoopsomvordering* (Buy-out claim) and *Rentevordering* (Interest claim).
2. **Rechtshandeling (Legal act)** — the legal basis for the claim (decisions or agreements).
3. **Betaalcomponent (Payment component)** — linked to a claim, describing payment specifications such as instalments or amounts.
4. **Verrekening (Settlement)** — a claim form where the amount is offset against other financial rights of the client (e.g. future benefits).
5. **Afkoopsomvordering (Buy-out claim)** — a claim settled via a lump-sum payment to discharge further obligations.
6. **Rentevordering (Interest claim)** — applied when interest is owed on the outstanding amount.
7. **Krediethypotheekovereenkomst (Credit-mortgage agreement)** — an agreement establishing a credit mortgage as security for repayment.
8. **Aflossingsplan (Repayment plan)** — how and when a client will repay; may be linked to multiple claims.
9. **Interventieverzoek (Intervention request)** — submitted when additional measures are needed to collect a claim, e.g. legal action.
10. **Debiteur (Debtor)** — the person responsible for repaying the claim; links the debtor to all relevant financial processes.

#### Relationships in the model

- A *Vordering* contains multiple components such as *Rechtshandeling* and *Betaalcomponent*.
- Subtypes such as *Verrekening*, *Afkoopsomvordering* and *Rentevordering* are generalised by *Vordering*.
- The repayment plan is linked to both intervention requests and specific payment agreements.
- The debtor has direct relationships with credit-mortgage agreements and repayment plans.

### Service model

The *Service model* gives a structured view of the processes and object types involved in delivering services in the social domain. It focuses on the relationships between applications, decisions, rights and conditions on which provisions are based.

![Service model][diensten]

<em>Diagram (in Dutch): Aanvraag → Besluit → Beschikking → Recht; with conditions, delivery components and schemes.</em>

#### Object types and relationships

1. **Aanvraag (Application)** — the start of the process. Represents a client's request for a service or provision. Always leads to a decision.
2. **Besluit (Decision)** — the result of an application; contains the approval or rejection. Initiates a *Beschikking*.
3. **Beschikking (Formal Decision)** — formal document recording the decision, with details on granted rights and conditions.
4. **Recht (Right)** — the right arising from a *Beschikking*, based on conditions; the basis for delivering provisions.
5. **Voorwaarde (Condition)** — criteria to be met to claim a service. May include exclusion grounds, prior provisions or other restrictions.
6. **Leveringscomponent (Delivery component)** — how a service is delivered. Includes:
   1. **Leveringsspecificatie (Delivery specification)** — details of how the provision is delivered.
   2. **Leveringsopdracht (Delivery order)** — the order to deliver the service.
7. **Regeling (Scheme)** — the context in which services are delivered (e.g. social assistance or special social assistance).
8. **Verstrekkingsvorm (Form of provision)** — how a service is provided, e.g. in kind or as financial support.
9. **Uitsluitingsgrond (Exclusion ground)** — specific condition determining when someone cannot claim a provision.
10. **Voorafgaande voorziening (Prior provision)** — previously granted provisions that affect the right to new services.

#### Relationships in the model

- An *Aanvraag* leads to a *Besluit*, which results in a *Beschikking*.
- A *Beschikking* contains rights, based on conditions.
- *Voorwaarde* generalises *Uitsluitingsgrond* and *Voorafgaande voorziening*.
- Delivery components — specifications and orders — are linked to services and forms of provision.
- *Regelingen* form the legal basis for delivering services.

[terug]: image/EAID_CE436DEE_AB15_4f23_B191_FA8A63FB488D.jpg "Recovery and collection"
[gbienggm]: image/EAID_FD4BAB10_5D3E_4d14_8949_24CA09AC42A7.jpg "Relationship between GBI and GGM"
[normafwijking]: image/EAID_1818B773_1463_43c7_BACA_FEE391FE27CD.jpg "Norm deviation"
[redenaanvraag]: image/EAID_B87D7E99_417E_4b99_BEC1_B319BE85AECA.jpg "Reason for application"
[diensten]: image/EAID_49670B34_2BC4_4972_BC7C_3F5793B27A73.jpg "Service model"
[inkomenbasis]: image/EAID_9CEE3C86_9B9F_472f_A104_61FFC01DAC5A.jpg "Income base model"
