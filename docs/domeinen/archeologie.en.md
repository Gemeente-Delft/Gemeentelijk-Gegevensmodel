# Archaeology

The data present in the applications translates into the domain model as shown in the figure below. *Project* is central. The entities *Pit* (pit dug by a machine), *Layer* (layer at depth in the pit, indicating a time period), *Trace*, *Fill* and *Find* (objects found) capture the metadata customary in archaeology. A pit has a location, and a *Project* has a location consisting of a polygon (multiple *Locations* as corner points) that can be displayed on a map.

![Archaeology data model][archeologieDatamodel]

<em>Diagram (in Dutch): the data model for archaeological projects, with Project at the centre and entities for pits, layers, traces, fills and finds.</em>

[archeologieDatamodel]: image/EAID_C91D2D84_69FA_4320_BFE0_F10EFEB8F49B.jpg "Archaeology data model"

A *Find* is always of a particular kind (leather, ceramics, glassware, etc.). In addition, a *Project* has various decisions (see earlier text) and multiple documents. Finds are stored in a *Container* with its own location. For metadata, ABR 2 (the Archaeological Base Register) has been applied as much as possible.
