# Generic Social Domain Definitions

Within the Social Domain there is a single object type *Client* to which all services are linked. This way the social domain is decoupled from other domains and person-bound information can be made accessible separately.

## Household

A *Household* contains at least one *Natural Person*, and a *Natural Person* has at most one household. A *Household* always has exactly one address. The household is linked to *Natural Person* so that non-registered persons can also be part of a household. *Marriage* and *Registered Partnership* are linked to *Natural Person*, and the group-attribute kinds *Solemnisation* and *Dissolution* are linked to *Marriage*.

![Data model — Client, Household and Marriage][huishouden]

<em>Diagram (in Dutch): data model for Client, Household and Marriage.</em>

## Social Relations and Social Groups

*Social Relation* and *Social Group* are introduced and linked to *Natural Person*. We also introduce the role someone has in a *Social Relation* with someone else:
- The neighbour
- Group of youths hanging out at the shopping centre
- Member of a football club
- Member of a motor gang
- The scope of the people this case or plan concerns

![Social relations data model][socialerelaties]

<em>Diagram (in Dutch): data model for Social Relations and Social Groups.</em>

## Authority relationship

The authority relationship defines authority over a person. It is important to distinguish between authority over a minor and over an adult. The relationship may be based on a court order.

![Authority relationship data model][gezagsverhouding]

<em>Diagram (in Dutch): data model for authority relationships.</em>

### Authority over minors

In the Netherlands, several forms of authority over a child are possible, determining who is responsible for the child's care and upbringing, who may legally represent the child and decide on important matters such as education and medical treatment. The main forms are:

1. **Parental authority** — the most common, exercised by one or both parents. May be exercised jointly or by one parent depending on the situation (e.g. after divorce).
2. **Guardianship** — when neither parent can or may exercise authority (e.g. due to death or dismissal from parental authority), a guardian can be appointed.
3. **Joint authority by a parent and a non-parent** — in addition to the parents, a non-parent can exercise joint authority. This must be assigned by the court — for example in the case of a stepparent or other person closely involved in the upbringing.
4. **Shared authority by two non-parents** — exceptionally, authority may be assigned to two persons who are not the biological parents. This also requires a court decision.

Each form of authority is intended to protect and safeguard the child's welfare and interests and is recorded in the authority register kept by the court.
In the Netherlands, at most two persons can have authority over a child. This can be a combination of parents (biological or adoptive) or of a parent and non-parent (e.g. a stepparent) who jointly exercise authority, or exceptionally two non-parents. The law is designed to ensure no more than two persons hold authority over a child simultaneously, keeping decision-making and responsibility clear.
In the Netherlands, authority over a child may also be assigned to an institution, not only to natural persons. This takes the form of guardianship. When neither parent can exercise authority and no suitable individual guardian can be found, an institution can be appointed guardian by the court. Such institutions are often specialised in the care of minors — for example a youth-care institution or another government-designated organisation.

### Authority over adults

For adults in the Netherlands, we do not speak of authority but of *mentorship*, *administration* (bewindvoering) or *curatorship*. These measures protect adults who cannot (fully or partially) take care of themselves or their finances. They can be instituted for persons whose mental state, or wastefulness or problematic debts, limit their capacity to look after their interests.

1. **Mentorship** — for people unable to make decisions themselves about personal matters such as care, nursing, treatment or supervision. A mentor makes these decisions on their behalf.
2. **Administration** (*bewindvoering*) — focuses on financial matters and is instituted for people unable to manage their finances. An administrator manages the person's assets.
3. **Curatorship** — a combination of mentorship and administration, the most far-reaching measure. A person under curatorship is legally declared incompetent to decide on personal and financial matters. The curator decides on both.

These measures must be instituted by the court, and a natural person or a professional institution (e.g. a foundation) may take on the role of mentor, administrator or curator. The aim is to protect and promote the adult's interests.

[sockern]: image/EAID_D7287848_8118_4aab_8823_D555A599063C.jpg "Generic entity — relations to Core"
[socclient]: image/EAID_FD6966FF_E4FC_437d_983E_71B33445A62C.jpg "Generic entity — Client, household and relations"
[huishouden]: image/EAID_CABB9F3F_A6ED_479a_A175_6F61BE2BE8F8.jpg "Household data model"
[gezagsverhouding]: image/EAID_227EBDFE_6FD0_4a47_85A4_FAC4AEFE003E.jpg "Authority relationship data model"
[socialerelaties]: image/EAID_69607C8F_8048_4516_BE75_80C681DFEAC0.jpg "Social relations data model"
