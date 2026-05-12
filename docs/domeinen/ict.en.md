# ICT

The data present in the applications is structured according to particular object types. These are elaborated in the domain models in this section.

![Applications and Data][ictApplicatiesEnGegevens]

<em>Diagram (in Dutch): how object types, attributes, data types and relationships are modelled, based on MIM.</em>

The figure above shows how object types are elaborated. An object type represents the definition of a particular object type. Such an object type may have zero or more attributes, each of a particular data type. Object types may have relationships with other object types, of a particular relationship type. Object types may also be a generalisation of another object type, indicating that the one inherits attributes and relationships from the other. The above definition is based on [MIM (Metamodel for Information Models)](https://www.geonovum.nl/geo-standaarden/metamodel-informatiemodellering-mim), from which all relevant definitions are derived.

In addition to the elements that are part of MIM, there is the type *Datum* (Datum/Data Item) which is defined by an *Object type*. A *Datum* may have one or more classifications. The current model uses classifications for personal data:

* No personal data
* General personal data
* Sensitive personal data
* Special personal data

Data may be classified per the list above, both for the data itself and for relationships with other data.
The figure also shows that a *Datum* may have an *Application* as authoritative source, or that data originates from an external source.

![ICT — CMDB Base Model][ictBasismodelCMDB]

<em>Diagram (in Dutch): the base CMDB model — Linkable CMDB items, log items, applications, servers, databases and suppliers.</em>

In the figure above, an elaboration for CMDB items is made. Each CMDB Item may have multiple Log items in which annotations are recorded. *Database*, *Server* and *Application* are special *Linkable CMDB Items* and may therefore have links with other Linkable CMDB Items. Applications and servers may have a *Supplier*.
An *Application* may also have various staff members linked with their own role — functional administrator, application owner, super-user. An Application has one or more versions and may have multiple packages. Documents and notes may also be linked to an *Application*.

In addition to Linkable CMDB Items there are also regular CMDB Items (not linkable to other CMDB Items). These are elaborated in:

![ICT — Other CMDB][ictOverigeCMDB]

<em>Diagram (in Dutch): regular CMDB items derived directly from CMDB Item: Licence, Hardware, Vehicle, Network Component, Access Means, Inventory and Software.</em>

The model has, alongside the Linkable CMDB Items, the following CMDB Items derived directly from CMDB Item: *Licence*, *Hardware*, *Vehicle*, *Network Component*, *Access Means*, *Inventory* and *Software*.

[ictApplicatiesEnGegevens]: image/EAID_A2831A97_91F6_4ed0_896E_3531219E69F0.jpg "ICT Applications and Data"
[ictBasismodelCMDB]: image/EAID_4F14E8D8_5502_4880_9E83_D912BE451EB1.jpg "ICT CMDB Base Model"
[ictOverigeCMDB]: image/EAID_A255BB0C_A1DB_43a5_88B1_C638F6E64B0B.jpg "ICT Other CMDB"
