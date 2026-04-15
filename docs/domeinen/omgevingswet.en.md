# Environment Act

The data definitions for the Dutch *Omgevingswet* (Environment and Planning Act) are divided by the functions described in the previous section and the associated information models.
The following standards and information models have been used:

* [Standard and Information Model for Applicable Rules (STTR/IMTR)](https://aandeslagmetdeomgevingswet.nl/digitaal-stelsel/technisch-aansluiten/koppelvlakken/toepasbare-regels/standaard/) version 1.02. Used for the Environment Act question-tree functionality of the *Omgevingsloket*. Adopted partially due to limited scope.
* [Standard and Information Model for Applications and Reports (STAM/IMAM)](https://aandeslagmetdeomgevingswet.nl/digitaal-stelsel/technisch-aansluiten/koppelvlakken/vergunningen/standaard/) version 0.9. STAM and IMAM support the submission of permit applications or notifications under the Environment Act.
* [Standard for Official Publications (STOP/TPOD)](https://aandeslagmetdeomgevingswet.nl/digitaal-stelsel/technisch-aansluiten/koppelvlakken/omgevingsdocumenten/standaard-officiele/) version 0.98beta — for validating and publishing Environment Act decisions. Adopted partially due to limited scope.
* [Conceptual Information Model for the Environment Act (CIMOW)](https://geonovum.github.io/TPOD/CIMOW/CIMOW_v2.1.0.pdf) version CIMOW v0.98-core. Describes the Environment Act domain — the information recorded, established and exchanged via the digital system (DSO).

## Generic Location

Locations play a central role in the Environment Act and have their place in all information models. They are therefore described generically.

![Generic Location][locatie]

<em>Diagram (in Dutch): six kinds of generic Location — Point, Line, Area, and groupings thereof.</em>

Six kinds of *Location* are distinguished: *Point*, *Line*, *Area*, and groupings of the three preceding kinds. References always go to *Location*; in practice that can be one of these six kinds. All six can be displayed on a map.

## Maintaining and publishing spatial plans

Spatial plans are drawn up and communicated to the DSO-LV in accordance with the Standard for Official Publications (STOP). For the Environment Act a specification of STOP is recorded in the Conceptual Information Model for the Environment Act (CIMOW).

The figure below shows the relationship between *Regulation texts* from STOP, the *Environmental Document*, the *Legal Rule*, the *Location* and *Themes*.

![Environment Act STOP/TPOD][stop]

<em>Diagram (in Dutch): relationship between STOP regulation texts, the Environmental Document, legal rules, locations and themes.</em>

Per STOP, an *Environmental Document* consists of multiple *Regulation Text* objects, which may relate to each other or may have other regulation texts as working area. These text elements are annotated, and *Legal Rule*, *Location*, *Themes* and other CIMOW object types are generated from the annotation. Because this is not a regular relationship but generation based on annotation, the relationship is marked as *abstract*.

The next figure shows all object types generated from environmental documents via annotation, representing the legal reality around environmental plans.

![Conceptual Information Model for the Environment Act (CIMOW)][cimow]

<em>Diagram (in Dutch): the full CIMOW — activities, rules, functions, restriction areas, environmental values and norms.</em>

This diagram overviews all recognised object types — activity, rule, function, and so on. Information is maintained about them, and different kinds are distinguished. For example, the function "hospitality in the city centre" is not the same as the function "nature reserve with water", but both are a function and are treated from an information perspective as of like kind — namely a function with a freely chosen name.

A *Regulation Text* is the smallest independent unit of (one or more) related legal rules in a text with Article structure — an article or a paragraph. A *Legal Rule* is included in a *Regulation Text* (abstract, because based on annotation). A *Legal Rule* is a rule with legal effect. Within the Environment Act, a rule often concerns activities, and/or norms and/or area designations. Three kinds of legal rule are distinguished:

1. *Rule for everyone* — a generally applicable rule with direct effect for everyone in the Netherlands, including the competent authorities themselves.
2. *Instruction rule* — a legal rule that gives instructions to other authorities, targeting external environmental documents or a task execution.
3. *Environmental-value rule* — a legal rule imposing obligations on the competent authority that adopts it.

A *Legal Rule* has one or more *Locations* as working area and always applies to one or more activities. An *activity* is any human act, or any human failure to act, that causes or can cause a change or effect in the physical living environment. For example: discharging waste water, constructing high-rise buildings, operating a marina.

An *Area Designation* is an area designated by rules or policy, indicating how the area is to be regarded under those rules or policy. Specific area designations are *Function* and *Restriction Area*. A *Function* is the use or the special property that a part of the physical living environment has in a given location — for example: city centre, business park. A *Restriction Area* is an area designated by or pursuant to law, where rules apply because of the presence of a work or object, restricting activities that may have an impact on it — for example: an airport, a railway or a motorway.

*Environmental Value* is the norm that fixes the desired state or quality of (part of) the physical living environment, the permissible load from activities and/or the permissible concentration or deposition of substances as a policy goal. An *Environmental Norm* is a norm expressible as a measurable value (other than an environmental value) that the competent authority wishes to give different values on different locations — for example: maximum building height, maximum number of parking spaces, maximum noise load, maximum number of visitors.

A *Norm* is an environmental value or an environmental norm, of a normative nature, described by means of norm values. A norm value may be qualitative or quantitative. A norm may consist of multiple norm values, each applying to separate areas — for example: the norm *maximum building height* consists of two norm values: maximum 10 metres applying to a number of locations.

## Maintaining and publishing applicable rules

Applicable rules are held in an *Applicable Rules file*, containing multiple *Execution Rules*. An *Execution Rule* contains a part of the interaction with an end-user as they are led through the question tree.

An *Applicable Rule* (we use the term *Applicable Rule* instead of *Rule Management Object* for readability) links to a coherent set of rules to enable a derivation. The *Applicable Rule* "conclusion façade adjustment" can answer a question like: *"Do I need a permit to change a window, window filling or façade panel?"* The rule-management object "discharge report" answers: *"What information (data and documents) must I provide when discharging from private households?"* The rule-management object "Storing gasoline, lubricating oil or waste oil in an above-ground storage tank" indicates which measures must be taken. The *Applicable Rule* is part of the functional structure; the rule set is defined in the applicable-rules file.

![Applicable Rules][toepas]

<em>Diagram (in Dutch): data model for Applicable Rules (conclusions, submission requirements, measures).</em>

There are various types of applicable rule:

* *Conclusion*
* *Submission requirements*
* *Measures*

*Conclusion* represents the conclusion of a check question — e.g. the answer to whether a notification or permit is required for a given activity.

*Submission requirements* specify what the applicant must provide to enable assessment — the set of information (data and/or attachments) that must be added to an application for a given permit or notification.

*Measures* describe how applicable rules can be complied with. Regulations describe what the applicant must adhere to while performing a given activity.

Applicable rules cover one or more legal rules and thus relate to one or more locations and one or more activities.

The basis for IMTR is the [DMN (Decision Model and Notation)](https://www.omg.org/dmn/) standard version 1.1. This open standard is published by the Object Management Group (OMG) and is the industry standard for decision-making on business rules. For the operation of the rule system, see DMN.

## Reports, applications and case handling

Central to the model is *Request* (*Verzoek*). A submitted *Request* is a permit application or notification, a supplement to a permit application, or a withdrawal of a permit application. To relate supplements or withdrawals to the original request (or earlier supplement), *Request* has a self-relationship ("relates to").

A *Request* comes from an *Initiator* who is responsible for submitting it. Actual submission can be done by the initiator or by an *Authorised Agent* (Gemachtigde), authorised by the Initiator. There is no recursive relationship between Authorised Agent and itself — an Agent cannot authorise someone else; only the Initiator can. Note that an Agent is bound to a Request (authorisation is per request).

![Reports, applications and case handling][aanvraag]

<em>Diagram (in Dutch): data model for submissions, applications and case handling under the Environment Act.</em>

One or more *Documents* may be added to a Request. A *Document* fills in one or more *Requested Attachments*, or may be added separately. A *Requested Attachment* has a characteristic — e.g. that it is a site sketch, a building drawing, or a complex answer to a previously asked question that does not fit the standard answer structure. Requested Attachments are part of the submission requirements of a Request. A Requested Attachment always belongs to exactly one *Project Activity*.

A Request is always assigned to exactly one *Competent Authority* responsible for handling it. This also applies when not all Project Activities in the Request fall under that Competent Authority — for example, because the activity type is not under that authority's responsibility, or the activity falls outside the area of responsibility. In such cases the authority is expected to coordinate with the authority that *is* responsible for the activity on that location.

From a *Request*, a *CASE* may result, within which a *STAFF MEMBER* of the *Executing Organisation* carries out further handling.

## Coherence

The figure below shows the coherence between the previous parts.

![Environment Act coherence][samenhang]

<em>Diagram (in Dutch): coherence overview — Activities and Locations linking permit requests, legal rules, area designations and applicable rules.</em>

Central are *Activity* and *Location*. Permit requests are submitted to perform a particular activity at a particular location. Legal rules apply to activities at particular locations, generated from annotation of regulation texts that are part of environmental documents. Area designations are linked to these legal rules, determining a function or imposing a restriction area.

To build understandable question trees for applicants, applicable rules are drawn up for activities at locations.

[samenhang]: image/EAID_30B09C29_F649_4248_97FC_35A5F9331BBF.jpg "Environment Act coherence"
[aanvraag]: image/EAID_0485D200_55DD_437e_B02F_314979270840.jpg "Reports, applications and case handling"
[toepas]: image/EAID_B9209AD2_0648_4482_BB24_135F27C2FECC.jpg "Applicable Rules"
[cimow]: image/EAID_0AC65EDC_5C77_4fd6_8548_98FCF09F72D0.jpg "CIMOW"
[locatie]: image/EAID_8DBF3226_FD39_4d9b_8101_633FF36CA47E.jpg "Generic Location"
[stop]: image/EAID_0A914AB1_6EA7_4087_BEB1_DB786FB5D810.jpg "Environment Act STOP/TPOD"
