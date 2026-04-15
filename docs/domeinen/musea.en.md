# Museums

The data definitions within museums are divided into three sub-areas:

1. Collection
2. Events and Relations
3. Sales

In addition, it builds on generic heritage data definitions to enable data exchange. The museum data model uses the generic heritage object types.

## Collection

Within the *Collection*, the objects that belong to the museum are central. These are called *Museum Object*. Museum objects have a *Location* and may be on loan; in that case they have a *Loan* object attached. A loan links to a *Lender*, who may be the Museum Prinsenhof itself (lending out) or an external lender (borrowing from). Lenders are a *Legal Entity*: natural or non-natural person. Museum objects may also have a *Stakeholder* with a particular role relative to the object.

In addition to the collection, exhibitions are administered, with linked rooms used and exhibition curators. Each exhibition tracks which museum objects are part of it.

Historical persons are also administered, and their relation to museum objects via *Role*. Incidents are administered and linked to the museum objects.

![Collection data model][museumCollectie]

<em>Diagram (in Dutch): data model for the museum Collection — museum objects, locations, loans, exhibitions, historical persons and incidents.</em>

## Events and Relations

Here, activities within programmes for museum contacts are central. A *Programme* consists of 0 or more activities. Each *Activity* may consist of 0 or more sub-activities. An *Activity* is of an *Activity type*. The same goes for a programme (of a *Programme type*). Reservations may be linked to an *Activity* — for rooms, facilities and production units. This is represented by a link from *Reservation* to 0 or more *Room*, *Production unit* and *Facility* objects. A *Production unit* may be an external supplier, in which case there is a link to *Supplier*. An *Activity* may have a *Guided Tour* attached, which may link to an *Exhibition*.

A *Programme* has a cost centre linking it to a *Cost Centre*, securing the link with financial administration.

Within the Prinsenhof data model, relations (persons, businesses, institutions) are modelled as *Museum Relation*. A *Museum Relation* is derived from *Legal Entity*, retaining all required characteristics such as name, address and Chamber-of-Commerce number. Mailings are sent to museum relations, so the *Mailing* object type is linked to *Museum Relation*.

![Museum Events and Relations][museumEventsEnRelaties]

<em>Diagram (in Dutch): data model for Museum Events and Relations.</em>

## Retail sales

In the sales data model, the *Product* to be sold is central. An *Entry Ticket* is derived from product and is modelled as something that can be sold alongside other products. All products have 0 or more product groups and revenue groups. A *Product* may have a *Supplier* and a *Stock Item* recording stock levels. Products may have multiple *Counter Sales*, recording how many and when a given product was sold. A *Counter Sale Entry Ticket* is a derivative of *Counter Sale* and allows capturing ticket-specific information such as start time and validity duration.

![Museum — Retail Sales][museumVerkoop]

<em>Diagram (in Dutch): data model for the Museum retail shop — products, sales, stock and tickets.</em>

[museumVerkoop]: image/EAID_3913ADF8_4B30_48c0_A0AE_59BAAC281EF2.jpg "Museum Retail Sales"
[museumCollectie]: image/EAID_B2D890F1_6B7C_45df_9A70_8C40CE1B3611.jpg "Collection data model"
[museumEventsEnRelaties]: image/EAID_22110445_1906_4602_8004_6BA4D6C063D0.jpg "Museum Events and Relations"
