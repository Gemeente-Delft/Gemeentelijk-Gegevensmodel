# Municipal Real Estate

Municipal real estate concerns cadastral real-estate objects. This object type is taken from the Core: RSGB. For these real-estate objects, the object type *Object* is defined. Objects may consist of building parts and building-part elements. All objects and their building parts and elements are included in a *MJOP* (Multi-year Maintenance Plan). The link in the data model goes via *MJOP items*. When work is actually carried out, a *Work Order* is created and used as the order for work by a *Supplier*. A *Supplier* may have won a tender.

Rental and sale contracts are modelled per Core:RSGB via the object type *Property Right*. A *Property Right* has either an owner or a tenant attached. Both are *LEGAL ENTITY* from Core:RSGB.

The *Object* is linked to a *Cost Centre* from the financial model, and the *Work Order* belongs to an *Obligation* from the financial model — anchoring the link with Finance.

The above is shown in the figures below.

![Real Estate data model][gegevensmodelVastgoed]

<em>Diagram (in Dutch): data model for Municipal Real Estate — Object, MJOP, Work Order, and link to Cost Centre.</em>

The relationship with suppliers is shown below.

![Real Estate — Suppliers][vastgoedLeveranciers]

<em>Diagram (in Dutch): relationship between Work Orders and Suppliers in the real-estate model.</em>

The municipal real-estate object type *Real Estate Object* is linked to *Cadastral Real Estate*. After all, *Real Estate Object* represents ownership of a particular object; ownership of real estate is recorded in the BRK and available through *Cadastral Real Estate*. The link is many-to-many, since one holding may span multiple parcels and one parcel may bear multiple holdings (apartment rights).

*Named Objects* are linked to a *Cadastral Real Estate* — these may be *Other Built Object*, *Residence Object*, *Standplaats*, *Ligplaats* or *Other Named Terrain*. They each have a *Number Designation* that determines the address.

The link to the owner of a *Cadastral Real Estate* runs through *Property Right* and *Name Designation* (Tennaamstelling). Other kinds of property right also exist — right of usufruct, right of way, etc.

The cadastral object types are elaborated in more detail [here](ruimteAlgemeen.en.md#bag-base-registration-of-addresses-and-buildings). Per RSGB 3.0, *Name Designation* sits between *Property Right* and *Legal Entity*. The relationship *Located on* (see the ["Varkensoortje" pattern](../generatie.en.md#example-c)) from *Cadastral Real Estate* to itself has also been added, making it easy to determine on which parcel a given apartment right lies.

![Real Estate — Relationship to RSGB][vastgoedRelatieRSGB]

<em>Diagram (in Dutch): how Municipal Real Estate relates to RSGB — Cadastral Real Estate, Property Right, Named Objects.</em>

[gegevensmodelVastgoed]: image/EAID_00D4246F_6ED7_4690_A180_ACCCD6AB1291.jpg "Real Estate data model"
[vastgoedLeveranciers]: image/EAID_06E44472_8C2A_40eb_9965_DCF91A1322C9.jpg "Real Estate Suppliers"
[vastgoedRelatieRSGB]: image/EAID_EFF3FBED_B92D_4172_B142_567C2B6ACF01.jpg "Real Estate — Relationship to RSGB"
