# Civic Integration

The *Civic Integration* sub-domain contains the data municipalities register under the Civic Integration Act 2021 (*Wet inburgering 2021*). The Act obliges municipalities to direct the integration process of newcomers. The information model supports this by recording data on learning route, participation, examination, exemptions, dispensations and progress, providing a coherent and reusable picture of integration trajectories within the municipality.

The sub-domain aligns with the legal framework of the Civic Integration Act and facilitates collaboration between municipalities, DUO, language schools and other involved organisations. The model connects to the *Person*, *Education*, *Health*, *Employment* and *Regulation* domains so that coherent service delivery is possible alongside, for example, employment trajectories, education or social guidance.

![Civic Integration model][inburgering]

<em>Diagram (in Dutch): the data model for Civic Integration, centred on "Inburgeringsplichtige" (person with a duty to integrate).</em>

## About the diagram

The diagram shows the information model of the *Civic Integration* sub-domain. Central is the object type **Inburgeringsplichtige** (person obliged to integrate), which groups all data on a person under the Civic Integration Act. All relevant components of the integration trajectory are linked to it.

The main object types are:

- **Inburgeringsplichtige**: who has the integration obligation, the status of that obligation and the responsible municipality.
- **Startinburgering**: data on the formal start of integration and relevant characteristics such as moment of arrival.
- **Inburgeringsaanbod**: what has been offered to the person — for example language lessons, guidance or participation.
- **PIP (Personal Integration and Participation Plan)**: the plan in which learning route, participation, terms and goals are recorded.
- **Leerroute**: the type of learning route the person follows (B1 route, Z route or education route), with characteristics such as language level and exam goals.
- **B1-route**: additional data specific to this route — results, exam attempts, lesson hours.
- **Z-route**: the route for people with low learnability and limited language skills.
- **Onderwijsroute**: the route aimed at progression to education.
- **KNM (Knowledge of Dutch Society)**: the component testing knowledge of Dutch society.
- **MAP (Module Labour Market and Participation)**: data on the mandatory module preparing newcomers for the Dutch labour market.
- **Participatiecomponent**: how social participation is realised as part of integration — for example volunteering.
- **Voortgangsmeting**: progress within the trajectory at fixed measurement moments.
- **Ontheffing**: whether and why a dispensation has been granted from (parts of) the integration obligation.
- **Vrijstelling**: whether someone is exempt based on previous diplomas or test results.
- **Diplomawaardering**: the valuation of foreign diplomas for determining route or exemption.
- **Voorbereiding op inburgering**: activities before the formal start, e.g. in an asylum-seekers centre (AZC).
- **Introductiemodule**: the introduction period in which the municipality gets to know the newcomer and their situation.
- **ICT-vaardigheid**: assessment of digital skills.
- **Taalvaardigheid**: assessment of language proficiency, the basis for route determination.

Enumerations are used to record standard values such as learning-route categories, exam results and language levels. This enables reliable and consistent registration and data exchange.

The diagram shows how the object types interrelate, so municipalities can record structured information across all phases of integration — from preparation to completion — and use it for monitoring, steering and accountability.

[inburgering]: image/EAID_96927C60_9F7B_4e67_806A_02EE0191983D.jpg "Civic Integration"
