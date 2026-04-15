# Procurement

For readability, the data definitions are shown in three diagrams. This mirrors the way Procurement services are offered to the municipality, via three forms:

1. Hiring of personnel (Inhuur Personeel)
2. Extending personnel contracts (Verlengen Personeel)
3. Other procurement (no personnel)

Central to hiring personnel is the *Hiring Tender*. It often starts with a *Hiring Form*. A *Document* is linked to the *Hiring Form*, and it has a *Cost centre*.
A *Hiring Tender* falls within a particular *Category* (e.g. *DAS Category / ICT Information Provision*). Suppliers who have qualified for that *Category* receive an *Invitation* to tender. They can accept, decline or not respond. If they respond, they do so with a *Candidate*, to which a *Natural Person* is linked. In the selection procedure a *Candidate* may be selected via an *Award*. Based on the *Award*, the *Candidate* becomes an *Employee* for a period at a particular *Organisational Unit*. After awarding, a *Purchase Order* and *Contract* are created.

![Procurement — Hiring][inkoopInhuur]

<em>Diagram (in Dutch): the data model for hiring of personnel.</em>

When extending personnel hiring, there is already a *Purchase Order* and a *Contract* with a *Supplier*. The applicant fills in the *Extension Form*. Subsequently the contract information is updated. See the next figure.

![Procurement — Extending Hiring][inkoopVerlengenInhuur]

<em>Diagram (in Dutch): the data model for extending a hiring contract.</em>

All other single and multi-private tenders, and national and European tenders, start with the *Tender Start Form*. For private tenders a *Case* is created to which all documents are linked (the link to *Document* is not visible here).
The *Tender Start Form* may lead to a *Tender*. For private tenders, *Quote requests* are sent to *Suppliers*. They respond with a *Quote*; based on the *Quotes*, an *Award* follows. For national or European tenders, an *Announcement* may first be published. Additionally, for non-public tenders, *Suppliers* may qualify and receive a *Qualification*. *Suppliers* register for a *Tender* via a *Submission*. After the procedure, the *Tender* is awarded via an *Award* to one of the bidders.
As with personnel hiring, after award a *Purchase Order* is created for the *Supplier* and the awarded scope, and a *Contract* with the *Supplier* is concluded. During the *Tender*, one of the *Employees* acts as process leader.

![Procurement — Other][inkoopGeenInhuur]

<em>Diagram (in Dutch): the data model for non-personnel procurement and tendering.</em>

For small procurements the tender process is often skipped, but a *Purchase Order* is still created and a *Contract* concluded.

[inkoopInhuur]: image/EAID_1172FBF0_04B4_46c7_9FB5_F34730E060FB.jpg "Procurement Hiring"
[inkoopVerlengenInhuur]: image/EAID_21AD192F_EEF1_493b_9BFD_D37EF6C93236.jpg "Procurement Extending Hiring"
[inkoopGeenInhuur]: image/EAID_6683520C_EE21_4038_A418_D4C957172DF2.jpg "Procurement Other"
