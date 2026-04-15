# Civil Affairs

The entities used in Civil Affairs are derived directly from the RSGB. The administration of persons is fully placed under *Resident* and *Registered Person*. *Resident* defines residents; *Registered Person* defines residents with Dutch nationality, conferring voting rights and similar entitlements. The elaboration is shown in the figure below.

![Civil Affairs data][burgerzakenGegevens]

<em>Diagram (in Dutch): data model for Civil Affairs (Burgerzaken), derived from RSGB.</em>

Registered persons may have a driver's licence and travel documents (passport or identity card). *Resident* and *Registered Person* are referred to in the RSGB as *subjects*. The above model relies heavily on this. The next figure shows the full elaboration as applied in the GGM.

![Subjects][subjecten]

<em>Diagram (in Dutch): the full RSGB-based subject model used in the GGM.</em>

The elaboration of front-desk activities for Civil Affairs leans heavily on the service-delivery model. The figure shows how *Customer Contact* is linked to *Case* from the RGBZ. A *Customer Contact* may relate to a *Case*; an *Application or Report* may lead to a *Case*.

Compared to the RGBZ, the model is extended with *Payment* and *Levy* — the municipality imposes a *Levy* for many products and services, on which a *Payment* must be made.

![Service Delivery object types][dienstverlening]

<em>Diagram (in Dutch): object types for Service Delivery, including Customer Contact and the link to Case.</em>

The figure below shows the relationship of *Stakeholder* to *Customer Contact* and *Case*.

![Stakeholder object types][betrokkene]

<em>Diagram (in Dutch): the Stakeholder (Betrokkene) object types and their relationships.</em>

[burgerzakenGegevens]: image/EAID_D9511F60_3CA7_43bd_B6C8_F66447D66DBA.jpg "Civil Affairs data"
[subjecten]: image/EAID_30391B0F_CF52_4dc1_BC1B_36D428BF0120.jpg "Subjects"
[dienstverlening]: image/EAID_48B6C3F9_CCF1_4794_8252_FC6543409B78.jpg "Service Delivery object types"
[betrokkene]: image/EAID_1D7802F4_3458_4bb4_8431_16C7F85473FC.jpg "Stakeholder object types"
