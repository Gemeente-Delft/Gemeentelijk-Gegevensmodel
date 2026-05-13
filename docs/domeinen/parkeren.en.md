# Parking

Data definitions for parking concentrate on *Parking Right*. A parking right records in which *Parking Zone* a particular *Vehicle* may park and during which period. Parking rights are issued by a *Mobile-payment Provider* or arise from a *Parking Permit*. This is elaborated in the figure below.

![Parking data model][parkeren]

<em>Diagram (in Dutch): data model for parking — parking rights, zones, vehicles, permits.</em>

Parking permits are of a particular *Product Type* and *Product Group*, shown as an example in the next figure. A *Parking Permit* is issued to a *Legal Entity* as holder. Parking permits and their rights apply to a particular *Parking Zone*. Parking zones have a number of parking spaces and properties such as tariff and the times during which the tariff applies. Parking garages are also modelled as *Parking Zone*. Parking zones may contain a number of street sections, which in turn contain parking bays. A *Parking Bay* has a GPS location as a polygon, and it is indicated whether the tariff is charged fiscally.

Checking parked vehicles is done with a scan car or a handheld device. The scan vehicle scans the number plate and the parking bay where the vehicle is standing, so it can check whether the vehicle has a right for that bay.

The handheld scans the number plate and the staff member receives all rights issued for the plate. The staff member interprets the info and decides whether to impose an additional tax assessment.

![Parking product groups][productgroepenparkeren]

<em>Diagram (in Dutch): example of parking product groups and permit types.</em>

[parkeren]: image/EAID_84B6B75B_2B58_455d_B019_C9B1E71717C2.jpg "Parking data model"
[productgroepenparkeren]: image/productgroepenparkeren.png "Parking product groups"
