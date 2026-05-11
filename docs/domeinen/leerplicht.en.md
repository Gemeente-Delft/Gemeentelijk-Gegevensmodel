# Compulsory Education and Pupil Transport

Compulsory Education and Pupil Transport build on the [Education](onderwijs.en.md) model.

Below, the object types specific to compulsory education are elaborated. These are additional to the object types in the general data definitions described earlier.

![Compulsory Education data definitions][leerplicht]

<em>Diagram (in Dutch): data model for Compulsory Education — reports and applications handled by the Compulsory Education Officer.</em>

The diagram shows three kinds of reports and applications that lead to handling by the *Compulsory Education Officer*: *Absence report*, *Leave application* and *Exemption application*. These are abstractly represented by *Application or Report* and always concern a *Pupil* and may concern a *School*. In the case of absolute absence, the *Pupil* has no enrolment at a school.

The *Compulsory Education Officer* handles all these *Applications or Reports* and reaches a *Decision*. The decision always concerns a *Pupil* and may concern a *School*. It can be a general *Decision* or a variant: an *Exemption*, a *Referral to the Public Prosecutor*, a *HALT referral* or an *Official Report*. In the case of an official report, it is directed at the Pupil and/or *Parent or Carer*.

[leerplicht]: image/EAID_26A453D9_47AF_487e_854B_3B4BC6D6A308.jpg "Compulsory Education data definitions"
