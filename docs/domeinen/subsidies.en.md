# Subsidies

The subsidies data model centres on *Subsidy*, representing an incoming or outgoing subsidy. A *Subsidy* always has a *Subsidy Application* and may have a *Subsidy Decision* attached. Depending on whether it is incoming or outgoing, a municipal *Staff Member* is applicant or handler (via the relationships). Likewise, depending on direction, an (external) *Legal Entity* is applicant or grantor. As applicant, the party may be a natural person or a non-natural person. A grantor may be any subsidy-granting party.

Based on a *Subsidy*, multiple advances may be received or paid, and multiple tasks may sit with a municipal *Staff Member*. Multiple reporting moments may also be linked to a subsidy.

A *Subsidy* may fall within a *Subsidy Project* in which the programme's objective is recorded. A *Subsidy Project* falls within a *Subsidy Programme* linked to a *Cost Centre* and an *Organisational Unit* (Department). Subsidies fall within a particular *Sector*. A subsidy dossier may span multiple budget items; a budget item has multiple subsidy dossiers hanging under it.

*Component* lets us split a subsidy across multiple cost centres.

![Subsidies data definitions][subsidies]

<em>Diagram (in Dutch): data definitions for Subsidies — applications, decisions, projects, programmes and components.</em>

[subsidies]: image/EAID_F408BDED_51D4_4204_9B95_F0C6C2474DC3.jpg "Subsidies data definitions"
