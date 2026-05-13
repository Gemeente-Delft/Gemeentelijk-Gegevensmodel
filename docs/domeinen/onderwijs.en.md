# Education

The figure below shows the data tracked for schools and pupils.

![Education — pupils and schools][onderwijs]

<em>Diagram (in Dutch): data model for schools and pupils — enrolments, educational career steps, start qualifications.</em>

A *Pupil* is a *REGISTERED PERSON* and may have enrolments and de-enrolments at multiple schools. Only one current enrolment may exist (i.e. without a matching de-enrolment). At a *School*, a *Pupil* has an *Educational Career* consisting of multiple career steps, each indicating the kind of education and school year. A pupil may also have a *Starting Qualification* or be marked as a *vulnerable young person*.

A *School* is a *NON-NATURAL PERSON* and has one or more locations. A *Location* is of type *Real Estate Object*, establishing the link to municipal real estate. A *School* also has multiple kinds of education.

[onderwijs]: image/EAID_33E38059_C973_43ff_97EC_B629923074FF.jpg "Education — pupils and schools"
