# Monuments

At the heart of the Monuments entity model is *Protected Status*. It holds the data and relationships registered for a monument — beyond the data already in BAG (Base Registration of Addresses and Buildings) and BRK (Cadastral Base Registration). The next figure shows the relationship with these base registrations.

![Monuments Data Definitions][gegevensdefinitiesMonumenten]

<em>Diagram (in Dutch): data definitions for Monuments, centred on "Beschermde Status" (Protected Status).</em>

*Protected Status* contains items such as: national-monument code and/or municipal-monument code, date of inclusion in the register, description and type of monument. Linked to *Protected Status* are (with attributes per linked entity):

* *Building activity* (0 or more): year-from, year-to, indication, description.
* *DOCUMENT* (0 or more): all documents belonging to the monument.
* *Photo* (0 or more): all visual material of the monument.
* *Craftsmanship* (0 or more): kind of craft applied to the monument, year-from and year-to.
* *Building type* (0 or more): main category, sub-category and explanation.
* *Building style* (0 or more): main style, sub-style, purity and explanation.
* *Original function* (0 or more): function, function type and main function, main category, sub-category and explanation.

![Monuments data definitions and link to core entities][gegevensdefinitiesMonumentenOnroerendeZaakpng]

<em>Diagram (in Dutch): the Monuments data model and its links to the core entities (Cadastral Real Estate, Public Space).</em>

A *Protected Status* may concern one or more *Cadastral Real Estate* objects, and may also concern one or more *Public Space* objects (e.g. a (part of a) street or a piece of greenery). Both *Cadastral Real Estate* and *Public Space* originate from the RSGB and are linked to the BAG, so they can be related to information from the base registrations. The RSGB terminology is retained to align with the rest of the GGM and the base registrations.

[applicatiesMonumenten]: image/Applicaties_Monumenten.png "Applications Monuments"
[aanwijsbeschrijving]: image/Aanwijsbeschrijving.png "Designation description"
[monmumentenToezichtEnHandhaven]: image/MonumentenToezichtEnHandhaven.png "Monuments Supervision and Enforcement"
[applicatiesEnGegevensMonumenten]: image/ApplicatiesEnGegevensMonumenten.png "Monuments Applications and Data"
[gegevensdefinitiesMonumenten]: image/EAID_58EA4966_DBC2_4359_94C4_ABC774DBE5E2.jpg "Monuments Data Definitions"
[gegevensdefinitiesMonumentenOnroerendeZaakpng]: image/EAID_7429E175_1CBE_4336_BF92_6C5029395E69.jpg "Monuments data definitions and link to core entities"
