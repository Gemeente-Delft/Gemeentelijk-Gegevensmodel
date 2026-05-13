# Service Delivery

The data definitions for service delivery revolve around the object type *Customer Contact*. A *Customer Contact* is an actual contact between the municipality and a citizen or business. It originates from RGBZ 2.0, which defines:

* Personal contact: an event of a continuous time span in which information is exchanged interactively between at least two parties — at least one a municipal employee and at least one a natural person, possibly in the role of employee of a non-natural person or branch.
* Anonymous customer contact: an event in which information is exchanged interactively between at least two parties — at least one a municipal employee and one or more natural persons who are not identified.
* Information receipt: an event in which information intended for the municipality is received by the municipality (even if the sender is known, the sender is not actively involved).
* Information dispatch: an event in which information intended for a citizen or business is sent by the municipality (even if the addressee is known, the addressee is not actively involved).

In the GGM, *Customer Contact* is filled in more concretely so it can support service-delivery statistics — wait times, hung-up calls, occupancy. Customer contacts can originate from:

1. A *Phone call* — when a citizen, business or other party calls the municipality. If a conversation results, there is a *Customer Contact*; if the caller hangs up beforehand, there is a phone call but no customer contact.
2. A *Counter Appointment* — when a citizen, business or other party has an appointment, this becomes a *Customer Contact* if the appointment actually takes place. Otherwise the counter appointment is still tracked.
3. An *Application or Report* — a message sent by a citizen, business or other party to the municipality, via an electronic form or otherwise. When received, there is always a *Customer Contact*. This object type can also be used for outbound communication.

The next figure shows *Customer Contact* in relation to *Phone calls* and *Counter Appointments*.

![Service Delivery and Customer Contacts][klantcontact]

<em>Diagram (in Dutch): Customer Contact in relation to Phone Calls and Counter Appointments.</em>

A *Customer Contact* may relate to a *Case*, may take place at a particular *Office* of the municipality (empty for electronic contact), and may concern multiple *Product or Service*.

A *Phone call* has a *Phone Status* such as: hung up early, picked up, etc. A *Phone call* may have a *Phone Subject*. If a *Phone call* is transferred, multiple *Customer Contacts* may result.

A *Counter Appointment* is with a *Staff Member* and may concern multiple *Product or Service*. An *Appointment Status* takes values like: *Waiting*, *In progress*, *No-show*, depending on the front-desk system. Several wait-time concepts apply:

* *Gross wait time* — the time someone actually waits after checking in, regardless of the appointment time.
* *Net wait time* — the time someone is helped earlier or later than agreed. Earlier yields negative net wait time; later yields positive.

The next figure shows the elaboration for an *Application or Report*. An *Application or Report* is a message a citizen, business or other party sends to the municipality. It may be a (scanned) letter, a message via the report system or website, or messages from external apps such as Buitenbeter.

*Application or Report* is modelled flexibly: it is submitted with a form of a particular *Form Type*, on which a number of fields are defined as *Form Type Field*. The GGM thus supports arbitrary forms, regardless of the fields on them. Linked to *Form Type Field* and to *Application or Report* is *Application Data* containing the actual contents. An *Application or Report* has one or more *Subjects*, themselves hierarchically organised.

At the Municipality of Delft we use Pivot queries to translate applications and reports into specific forms.

![Application and Report object types][aanvraagEnMelding]

<em>Diagram (in Dutch): object types for Applications and Reports.</em>

The next figure shows the link between *Customer Contact* and *Case* from the RGBZ. A *Customer Contact* may relate to a *Case*; an *Application or Report* may lead to a *Case*.

Compared to the RGBZ, the model is extended with *Payment* and *Levy* — the municipality imposes a *Levy* on many products and services, on which a *Payment* must be made.

![Customer Contact and Cases][klantcontactEnZaak]

<em>Diagram (in Dutch): the link between Customer Contact and Case (RGBZ).</em>

The next figure shows the relationship of *Stakeholder* to *Customer Contact* and *Case*.

![Service Delivery and Stakeholder][dienstverleningEnBetrokkene]

<em>Diagram (in Dutch): Stakeholder in relation to Customer Contact and Case.</em>

[klantcontact]: image/EAID_282A4979_0BBC_4448_B71C_0CE64829083B.jpg "Service Delivery and Customer Contacts"
[aanvraagEnMelding]: image/EAID_5901286A_E9EF_4360_9CE6_32B6FDE1C970.jpg "Application and Report object types"
[klantcontactEnZaak]: image/EAID_48B6C3F9_CCF1_4794_8252_FC6543409B78.jpg "Customer Contact and Cases"
[dienstverleningEnBetrokkene]: image/EAID_1D7802F4_3458_4bb4_8431_16C7F85473FC.jpg "Service Delivery and Stakeholder"
