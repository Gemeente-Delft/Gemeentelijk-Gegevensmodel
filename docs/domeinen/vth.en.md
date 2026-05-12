# Permits, supervision and enforcement

The data definitions build on the RSGB (municipal information model with, among others, data from the basic registrations), RGBZ (municipal case-oriented working model) and [RiHA 2.0 (Supervision and enforcement data model)](https://samenwerken.pleio.nl/groups/view/8b832827-e91b-476c-bb4f-c228b8e5e934/standaardisatie-toezicht-handhaving-milieu/wiki/view/2b38214e-cfc7-42ff-9d5d-eaf069671c42/riha-referentieinformatiemodel-handhaving). RiHA essentially provides a translation of RGBZ with references to the RSGB, which means the RGBZ object types are not easily reusable generically within the GGM. To maintain consistency within the GGM, we have chosen to use RGBZ as much as possible and supplement it from RiHA. RiHA is shown in the next figure.

![RiHA data model][riha]

<em>Diagram: the RiHA reference information model for supervision and enforcement.</em>

To apply the RiHA object types and align them with the RGBZ, the following choices were made:

1. The RiHA entity *Toestemming* is modelled as the RGBZ object type *Besluit* (Decision).
    1. Added to *Besluit*: attribute *Besluitsoort* to capture the kind of permit, dispensation or notification.
2. The RiHA entity *Handhavingsobject* is modelled as the RGBZ object type *Object*.
    1. Added: *Domein* and *Risico-indicatie* (domain and risk indication).
3. The RiHA subdivision into case types (*Signaalzaak*, *Toezichtzaak*, *Handhavingszaak*, *Andere VTH-zaak*) has not been adopted. Signals are included in the model as *AanvraagOfMelding* (Application or Report) — they form the trigger for the case. The distinction between supervision and enforcement cases, and the inspection type, can be made in the case type. Statutory articles have not been modelled.

## Permit applications

Because of their generic nature, the object types for *Building and Housing* and for other permits are modelled the same way. Handling applications for permits, dispensations and reports in the VTH domain reuses the RGBZ information model. Central are:

* *VOMAanvraagOfMelding* (Permit / Dispensation / Notification — Application or Report): the application or report submitted by the applicant.
* *Zaak* (Case): the case in which the actual handling of the application or report is done.
* *Object*: the object or objects the application concerns.
* *Besluit* (Decision): the decision made within the case in response to the application — the permit or the rejection.

![Data model for permit and enforcement cases][vthHandhaving]

<em>Diagram (in Dutch): data model for permit and enforcement cases — AanvraagOfMelding, Zaak, Object, Besluit.</em>

The figure shows how an *AanvraagOfMelding* may lead to a *CASE*. *AanvraagOfMelding* is the generic object type used for all incoming applications and reports, including VJVs. The VTH-specific *VOMAanvraagOfMelding* is derived from it, from which *WABOAanvraagOfMelding* is derived for things specific to the WABO (Environmental Permits Act).

An application has a *Submitter* which may be a natural or non-natural person (*LEGAL ENTITY*). A *CASE* may have multiple stakeholders, consist of sub-cases, or relate to other cases. A case is of a particular *CASE TYPE*. The case status is recorded in *STATUS*, which is of a particular *STATUS TYPE*. A *DECISION* is the outcome of a case. Applications, cases and decisions can each have one or more documents attached.

Levies are recorded in bylaws such as the *Legesverordening* (fee bylaw) and the *Precarioverordening*, valid for a particular period. *Leges* are also called *retributies*: payments to government for specific services or products. *Precario* are fees for the use of public space. Each *CASE TYPE* has a *Levy Basis* by which a *Levy* is linked to a particular *CASE*. The distinguished levy kinds are: *leges*, *precario*, advertising tax and mooring fees.

![Linking cases to decisions][vthZakenEnBesluiten]

<em>Diagram (in Dutch): how cases link to decisions, including the levy basis per case type.</em>

VTH cases, decisions and applications always concern one or more objects — for example a mooring-dispensation application that refers to a specific vessel and a specific mooring place. This aligns with RiHA (reference to *HANDHAVINGSOBJECT*) and RGBZ.

Example: an application and grant of a mooring dispensation becomes:

* 1 VOMAanvraagOfMelding referring to an Object referring to a vessel.
* 1 Decision of type *Mooring Dispensation*.
* 1 Mooring Dispensation with sticker information.
* 1 Object referring to a LIGPLAATS (mooring place).
* 1 Object referring to a vessel.

The figure below shows how the RGBZ object type *Object* refers to all kinds of object types in the GGM (often the RSGB). In applications, cases and decisions you can thus reference the abstract type *Object* from which various concrete object types can be reached.

![Objects at permit issuance][vthObjectenVergunning]

<em>Diagram (in Dutch): how "Object" in the VTH model links to various object types from the GGM.</em>

## Public order and safety

Reports in the context of public order and safety also refer to the generic object type *Object* and so reach various other object types. A *Report* may reference photos and has a BOA (municipal enforcement officer) as the reporter. Three kinds are distinguished: *Observation*, *Combibon* and *Bike registration*. A *Report* is derived from the generic *AanvraagOfMelding*.

![Objects in broad enforcement][vthObjecttypenBredeHandhaving]

<em>Diagram (in Dutch): object types for broad (public-order and safety) enforcement — Observation, Combibon, Bike Registration, all derived from AanvraagOfMelding.</em>

[vthObjecttypenBredeHandhaving]: image/EAID_EC84A03C_FC04_401a_8263_7809B74179F8.jpg "Object types for broad enforcement"
[vthObjectenVergunning]: image/EAID_C9CE09B7_32EF_40eb_9C82_7FD6EDEA1D9E.jpg "Objects at permit issuance"
[vthZakenEnBesluiten]: image/EAID_A2BA1F0D_8428_42fc_80D6_7184F243D268.jpg "Linking cases to decisions"
[vthHandhaving]: image/EAID_BB52C835_0B2D_4164_AC9D_9D6EDBD7E267.jpg "Data model for permit and enforcement cases"
[riha]: image/riha.png "RiHA data model"
