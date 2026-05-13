# Finance

The data definitions for Finance are split into:

1. data for budget responsibility and budgeting;
2. data on commitments and invoices;
3. data on batch processing and mutations.

The figure below shows how the budget is structured and who has responsibility for it.

![Finance — Budget and Budgeting][financienBegrotingEnBudget]

<em>Diagram (in Dutch): the hierarchical budget structure and budget responsibilities.</em>

The *Budget* entity is hierarchical: chapters, objectives, products and cost centres. Each of these budget components has *Budget lines* that add up to a balanced *Budget*. In other words, the sum of all budget lines of the chapters of a *Budget* adds up to the *Budget line* of the *Budget* within a given *Period*. The same applies to objectives versus a *Chapter*, products versus an *Objective* and cost centres versus a *Product*.

Cost centres can have multiple main accounts to distinguish kinds of costs. Examples include: investment cost centre, departmental cost centre, project cost centre and municipal real-estate cost centres.
*Clients* (assigners) can be clients to objectives or products. *Contractors* (assignees) are budget-responsible for products or cost centres. Clients are usually programme managers; contractors are usually heads of department.

The next figure shows how commitments and invoices are structured.

![Finance — Commitments and Invoices][financienVerplichtingenEnFacturen]

<em>Diagram (in Dutch): commitments and invoices, with link to cost centres and main accounts.</em>

To enter a commitment with a *Creditor* (often a supplier), a *Purchase order* is needed. Purchase orders can have multiple cost centres, themselves with different main accounts. From a *Purchase order*, postings are made to one or more main accounts, distinguishing cost types. Incoming invoices are linked to the *Purchase order* and so to the *Cost centre*. The figure also shows how *Assets* are linked to main accounts.

The next figure shows mutations. Mutations are changes from one main account to another — for budget and expenditure from *Budgeted* to *Purchase order* or from *Purchase order* to *Actual*; for income from *Payment in transit* to *Liquid*.
Mutations are based on various events such as: processing an incoming *Batch*, an invoice or a bank statement. Batches, invoices and bank statements each have multiple lines, and per line a *Mutation* is created and funds are written from one main account to another, as described.

![Finance — Mutation Processing][financienVerwerkenMutaties]

<em>Diagram (in Dutch): processing mutations between main accounts based on batches, invoices and bank statements.</em>

Mutations always relate to a *Cost centre* and may be written to a *Work order* (not strictly enforceable) or *Sub-account* (linked to cost centre because of VAT). In addition to the modelled mutations there are various mutations created and posted manually or automatically within GFS, such as:

- Sales-to-receipt.
- Procure-to-pay.
- VAT compensation.
- Fixed assets.

Debtors and creditors derive from *Legal Entity* — they may be natural or non-natural persons. Clients (assigners) and contractors are linked to the *Function*, not to the person, so these responsibilities are decoupled from the actual office holder. See the next figure.

![Finance — Persons][financienPersonen]

<em>Diagram (in Dutch): how persons relate to Finance entities (debtors, creditors, clients, contractors).</em>

[financienBegrotingEnBudget]: image/EAID_42C2960F_FED7_467e_AAB1_5195BED59A39.jpg "Finance Budget and Budgeting"
[financienVerplichtingenEnFacturen]: image/EAID_0723EB5C_4A2C_44d4_B15B_37AC71B5D711.jpg "Finance Commitments and Invoices"
[financienVerwerkenMutaties]: image/EAID_B758018F_CB22_420e_B4E4_E17EB5F71EDA.jpg "Finance Mutation Processing"
[financienPersonen]: image/EAID_CB1E27F6_9539_4037_8A93_07CC937D5D2E.jpg "Finance Persons"
