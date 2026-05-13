# Sport

To keep good oversight of sport policy, sport locations in the city are administered. A *Sport Location* can be a *Sports Park* with multiple fields, or an *Indoor Venue*. *Line Marking* indicates the kind of markings at the location — football, handball, basketball — because locations with different markings are used for different sports and are not readily usable by every sports club. *Line Marking* therefore belongs to a *Sport*. Only for *Indoor Venues* are *Sport Materials* administered.

![Sport policy][sportbeleid]

<em>Diagram (in Dutch): sport-policy data model — sport locations, line marking, sports and materials.</em>

*Sport Locations* are used by a *Sports Club* and/or a *School*. Often the school rents locations out to the sports club. Schools and sports clubs are *Non-Natural Persons*. A *Sports Club* runs one or more *Sports*.

The next figure shows the relationship of sport object types to *District*, the BAG and inspection reports. *Indoor Venues* serve a particular *District*; *Outdoor Venues* serve the entire municipality. *Indoor Venues* are located in a *Residence Object*, establishing the link with the BAG. *Sports Parks* and *Fields* are on an *Other Named Terrain*.

Inspection reports are recorded in a *Document*.

![Sport locations][sportlocaties]

<em>Diagram (in Dutch): data model linking sport locations to districts, BAG objects and inspection reports.</em>

[sportbeleid]: image/EAID_25BCAA7D_6255_4f3a_8408_DF91881FE29F.jpg "Sport policy"
[sportlocaties]: image/EAID_BA23F316_FE48_49a8_A26D_9B1D14713F76.jpg "Sport locations"
