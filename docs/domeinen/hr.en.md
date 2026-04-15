# HR (Human Resources)

The HR policy domain has the following elaboration.

![HR data model][gegevensmodelHR]

<em>Diagram (in Dutch): the HR data model centred on Employee, Position and Department.</em>

Central is the *Employee*, who has one or more *Appointments*, plus *Leave*, *Absence* and an Individual Choice Budget. The latter three all have master data defining different kinds, for example: maternity leave, parental leave, special leave and regular leave.
An *Appointment* is for a particular function and belongs to a *Department*; this may be at multiple locations. A *Function* belongs to a *Function Structure* describing the makeup of functions for a given period.
An *Employee* may have multiple appraisals, given by a manager (also an *Employee*).

![HR — Applications][sollicitaties]

<em>Diagram (in Dutch): the Applications model — applicants, vacancies and interviews.</em>

The figure above describes *Application*, which is always for a *Vacancy*. A *Vacancy* always belongs to one function and may have multiple vacancy texts. *Applicants* submit *Applications* and may have multiple interviews involving one or more *Employees*.

![HR — Documents][documentenHR]

<em>Diagram (in Dutch): document types in HR — Employment Contract, Personnel Document, Vacancy Text.</em>

The HR model does not use *DOCUMENT* from the RGBZ directly, only derived documents. Different document types can be used: *Employment Contract*, *Personnel Document* (containing personnel agreements; can also be used for other communication) and *Vacancy Text*.

![HR — Persons][personenHR]

<em>Diagram (in Dutch): how persons (Employee and Relation) are modelled in HR, derived from RSGB types.</em>

The HR model does not use persons as defined in the RSGB directly — only derived entities. The figure shows how the *Employee* entity and the linked *Relation* entity are defined.

[gegevensmodelHR]: image/EAID_891372E6_27FB_442d_9CC4_08C2659E8C53.jpg "HR data model"
[sollicitaties]: image/EAID_542C38C9_B92F_48de_87F1_F90F64FB5913.jpg "HR Applications"
[documentenHR]: image/EAID_E8C1CCDA_FF3C_498a_8FC9_FD6E461092FA.jpg "HR Documents"
[personenHR]: image/EAID_6409BBCD_026C_40ea_BC54_EE3B816D8CAB.jpg "HR Persons"
