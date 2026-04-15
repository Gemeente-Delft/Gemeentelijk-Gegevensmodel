# Employment

The *Employment* sub-domain describes a person's situation regarding (paid) work, job orientation and participation. It records whether someone is or has been in work, is available for work, receives support with routes to work or social participation, or whether exemption or special circumstances apply. Historical data on job-application activities, trajectories, work experience, skills and fitness for work are also modelled here.

The *Employment* sub-domain is relevant to municipalities under the Participation Act (*Participatiewet*) and other social-security laws. It aligns with national concept frameworks such as the Participation Act Concept Framework and data models such as GWSW. It is substantively linked with the *Person*, *Health*, *Education* and *Regulation* domains. Together these provide insight into the living situation and support needs of residents — essential for integrated municipal service delivery.

![Employment data model][werk]

<em>Diagram (in Dutch): data model for Employment, centred on Arbeidssituatie (Employment Situation).</em>

[werk]: image/EAID_96927C60_9F7B_4e67_806A_02EE0191983D.jpg "Employment data model"

## About the diagram

The diagram shows the information model of the *Employment* sub-domain. Central is the object type **Arbeidssituatie** (Employment Situation), describing a person's current or historical situation regarding paid work, availability for work, or participation activities. This is the starting point for registering a wide range of relevant data.

The following object types are shown:

* **Arbeidssituatie (Employment Situation)** — whether someone works, is looking for work, receives support, or is exempt from a labour obligation.
* **Beschikbaarheid voor bemiddeling (Availability for mediation)** — whether and when someone is available for mediation towards work.
* **Bemiddelingsactiviteit (Mediation activity)** — concrete activities such as job applications, networking meetings or training.
* **Ontheffing (Exemption)** — whether and why someone is temporarily exempted from obligations, e.g. for medical reasons.
* **Participatiecomponent (Participation component)** — data on social participation that is not direct work, such as volunteering.
* **Ontwikkelwens (Development wish)** — learning and development needs.
* **Werkzaamheden als mantelzorger (Informal caregiving activities)** — whether someone is an informal carer, and the form and extent.
* **Zelfredzaamheidscore (Self-reliance score)** — assessment of the extent to which someone can function independently in daily life.
* **Vaardigheidsvaststelling (Skill assessment)** — assessment outcomes for basic skills such as language, numeracy and digital skills.
* **Rijbewijs (Driver's licence)** — possession, type and validity.
* **Certificaat (Certificate)** — certificates obtained outside formal education routes.
* **Doelgroep (Target group)** — which target group a person belongs to, for additional support or provisions.
* **Ondersteuningsbehoefte (Support need)** — what support someone needs to move towards work or participation.
* **Arbeidsmarktkans (Labour-market opportunity)** — estimated chance of work on the regular labour market.
* **Vaststelling werkervaring (Work-experience assessment)** — work experience, including outside paid work.
* **Vaststelling opleiding (Education assessment)** — assessment of education received, including diploma valuation.
* **Vaststelling taalvaardigheid (Language-proficiency assessment)** — level of language proficiency based on testing or estimation.
* **Vaststelling ICT-vaardigheid (Digital-skills assessment)** — digital skills, such as using computers or online forms.
* **Ondersteuningsactiviteit (Support activity)** — activities aimed at guidance, coaching or training, independent of trajectories.
* **Verwachting arbeidsparticipatie (Expected labour participation)** — the extent to which someone can be expected to participate in work soon.
* **Verzameluitspraak ondersteunbaarheid (Aggregate assessment of supportability)** — summarises multiple data points into a judgment on support need.
* **Verzameluitspraak loonwaarde (Aggregate wage-value assessment)** — estimated wage value of a person in a work setting.

The model uses standardised value lists (enumerations) for kinds of activity, development-wish goals, forms of participation and support categories. These enable reliable and consistent exchange between systems.

Through the relationships between these object types, a coherent picture emerges of a resident's employment situation and support needs — enabling municipalities to deliver data-driven, integrated services.
