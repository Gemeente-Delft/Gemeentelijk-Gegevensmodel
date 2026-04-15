# Economy

The data definitions for Economy concentrate on company *Branches* (establishments). They have a location in the city and largely determine how the local economy is perceived.

![Economy data model][economie]

<em>Diagram (in Dutch): the data model for Economy and business activity.</em>

Central is *Branch*, which can have a specialisation as *Sales Outlet* (shop) or *Hotel*. For more types of company no specific information is tracked here (generic information is). A *Hotel* can have *Hotel Visits* (overnight stays). A *Branch* performs a *Social Activity* (top relation) and may have a head branch via the *Social Activity*.

Per *Branch*, *Employment* can be tracked, such as the number of male and female employees.

A *Branch* is connected to a *Non-Natural Person* — the company (or other legal entity) the *Branch* belongs to. *Contact Persons* are administered for the company.

![Economy data model with locations][economieLocaties]

<em>Diagram (in Dutch): Economy and locations — link to BAG.</em>

The address of a *Branch* is recorded via *Addressable Object Designation*, linking to the BAG. A specialisation of *Addressable Object Designation* is *Number Designation*. Usually a *Branch* has a *Number Designation* for its address. Only for *Mooring places* and similar is this different — too rare to model here.

For a *Built Object*, the *Retail Floor Area* is tracked. This information comes from specific research. Vacancy is also tracked. The *Built Object* records the number of square metres of floor area (information from BAG). This way, retail research data and BAG data can be compared. A *Built Object* is a specialisation of a *Residence Object*, to which the *Number Designation* is linked to record the house number.

Within an *Area*, multiple *Addressable Objects* lie. An *Area* has different kinds, such as *retail area* and *project-development area*. *Areas* may also correspond to a *Neighbourhood* which together form a *District*. *Area* is an extension of the RSGB because there is no clear way to link *Neighbourhood* (and hence *District*, *Place* and *Municipality*) to *Addressable Objects*.

[economie]: image/EAID_21D78104_E6EA_4d5c_9DBE_AB71F7DC99E7.jpg "Economy data model"
[economieLocaties]: image/EAID_50085E67_46AC_4f54_B204_436786266EE2.jpg "Economy and locations"
