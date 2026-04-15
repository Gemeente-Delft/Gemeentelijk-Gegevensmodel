# Waste

Central to the waste data model are *fractions* and *locations*. A *Fraction* is a kind of waste being collected — for example PMD (plastic, metal, beverage cartons), OPK (paper and cardboard), Glass, or Residual waste. Per *Fraction*, price agreements are recorded in a *Price rule* stating how much it costs or yields per kilogram collected.

To collect certain fractions there are several routes that can be driven by waste-collection vehicles. Such a *Route* visits multiple locations. A *Location* is built from an address and/or X- and Y-coordinates. At the time of writing, Avalex only uses addresses for this; coordinates are included for future support. Routes that are driven for collecting certain waste fractions visit, depending on route type, containers, specific places or addresses:

* Route type — door-to-door: locations with addresses are visited;
* Route type — illegal dumping, bulky waste: locations are visited (optionally with address);
* Route type — containers: locations with containers are visited.

Containers are designed for one *Fraction* (glass container, paper container, residual-waste container, etc.). Per container there can be multiple fill-level measurements recording, per moment, how full (in %) and how heavy (in kg) the container is. Containers are of a certain *Container type* — for example: bottom-emptied container, mini-container or shared container.

Waste vehicles are designed for a particular container type and drive *Trips*. Each *Trip* a vehicle drives follows a particular *Route*. A *Trip* consists of several *Pickup moments* at which a certain quantity of waste is taken in at a specific location at a specific time. A *Container* may be emptied; if not, the waste (such as bulky waste or illegal dumps) is collected from a particular *Location*.

![Waste collection][afvalInzamelen]

<em>Diagram (in Dutch): the data model around routes, vehicles, containers and pickup moments for waste collection.</em>

The next figure shows that an *Address* has a *Pass* attached, valid for one or more *Recycling centres* (in practice usually only one, but exceptions are accommodated). A *Recycling centre* (Dutch: *milieustraat*) is a collection point for multiple fractions. With a *Pass* one can deliver *Drops* (deposits) at a *Recycling centre*. Each *Drop* concerns a single *Fraction* and has a particular weight.

![Recycling centre — Waste][afvalMilieustraat]

<em>Diagram (in Dutch): the data model linking residents (via Address and Pass) to waste drops at recycling centres.</em>

The figure below shows the data model for the reports handled at Avalex.

![Waste reports][afvalMeldingen]

<em>Diagram (in Dutch): the data model for waste-related reports, derived from the generic AanvraagOfMelding type.</em>

A *Report* always has a main category and a sub-category. A *Report* may concern a particular *Fraction* and may concern a particular *Container type*. A *Report* always concerns a particular *Location*. Reports are derived from the generic type *AanvraagOfMelding* (Application or Report).

[afvalInzamelen]: image/EAID_D98AA96C_2EB0_4b46_9E9C_09D55E02FE38.jpg "Waste collection"
[afvalMeldingen]: image/EAID_157F610A_619E_4d1a_BB45_5C1F55178944.jpg "Waste reports"
[afvalMilieustraat]: image/EAID_A00B8121_71AC_466f_B391_E16881240477.jpg "Recycling centre — Waste"
