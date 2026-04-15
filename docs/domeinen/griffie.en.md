# Council Office

The definitions of the object types are derived from information stored in the RIS (Council Information System). Use was also made of the information model from the *Open Council Information* pilots, which at the time of writing is still under development. The data as currently administered in Delft's RIS is taken as a starting point, deviating in a few places from the *Open Council Information* model.

The figure below shows the information model. Central are *Council Document* and *Meeting*. Council documents are all documents handled by the council — amendments, motions, proposals, replies, incoming documents and announcements. *Council Document* derives from the generic RGBZ type *DOCUMENT* and inherits its attributes. In a *Meeting*, multiple agenda items are discussed, each of which may handle several council documents. A particular *Agenda Item* may include a *Vote*, which concerns a particular *Council Document*. *Vote* is taken from *Open Council Information* but is not currently supported by the RIS. There may be video recordings of entire meetings or of individual agenda items.

Council documents may have 0 or more submitters. Documents with 0 submitters are procedural items such as the agenda and the list of incoming documents. A *Submitter* may be a *Council Member*, a *Board Member* or a generic *LEGAL ENTITY*. The latter is used when a citizen, business or institution submits a document. Both *Council Member* and *Board Member* are derived from *RESIDENT* in the RSGB.

![Council Office data model][gegevensmodelGR]

<em>Diagram (in Dutch): data model for Council Office (Griffie), centred on Council Documents and Meetings.</em>

Meetings have multiple *Attending Participants*. An *Attending Participant* may be a *Board Member*, a *Council Member* or another *NATURAL PERSON*. *NATURAL PERSON* is used when a third party (citizen or representative) speaks at a meeting. *LEGAL ENTITY* is not used here because only natural persons can speak; companies or organisations being represented are recorded in *Participant*.

Committees may have multiple *Council Members* as members; committees also have meetings.
Council documents have categorisation to improve findability. This is shown in the figure below: council documents may belong to multiple dossiers, may have a *Category*, may have a *Task field*, and may belong to multiple *Programmes*.

![Council Documents data model][gegevensmodelRaadsstukken]

<em>Diagram (in Dutch): data model for Council Documents and their categorisation.</em>

[gegevensmodelGR]: image/EAID_A9F0B77B_05F3_4c36_96A0_8841BBAE47E0.jpg "Council Office data model"
[gegevensmodelRaadsstukken]: image/EAID_108224FC_E160_417a_AFC5_68A484B3B8AE.jpg "Council Documents data model"
