# Archives

Below, the various entities involved in the archive are elaborated.

![Archive data definitions][archiefGegevensdefinities]

<em>Diagram (in Dutch): the entities and relationships of the Archives data model, centred around "Archiefstuk" (Archive Item).</em>

The central entity within Atlantis and TMS is *Archive Item*. Archive items refer to documents and other things physically stored in the archive. Archive items can be found at a *Location*, which always consists of a *Depot*, a *Stack* within that depot, and within it directly on a *Shelf* or in a *Cabinet* and within that on a *Shelf*. Each has its own number, so the archive item can be traced.

An *Archive Item* is derived from a *Document* in the RGBZ, so it inherits all attributes of *Document*. This ensures consistency between documents in municipal processes and documents to be archived. Additionally, an *Archive Item* has extra attributes for *Publisher*, *Rights holder* and *Author*, each derived from person types in the RSGB (see the next figure).

The RGBZ entity *Document* has attributes from Dublin Core, needed to archive documents correctly.

Archive items are placed in a *Collection* with optional sub-collections and originate from a particular *Period*.

![Archive and visitors][archiefEnBezoekers]

<em>Diagram (in Dutch): visitors can submit requests and pay visits to the archive.</em>

The previous figure shows that visitors can submit requests and pay visits.

![Archive — persons and documents][archiefPersonenEnDocumenten]

<em>Diagram (in Dutch): publishers and rights holders are derived from the RSGB type "Rechtspersoon" (Legal Entity); visitors and authors are always natural persons.</em>

The figure shows that publishers and rights holders derive from the Core RSGB type *Legal Entity* — they may be natural or non-natural persons. Visitors and authors are always natural persons and are therefore derived from the Core RSGB type *Natural Person*.

An *Identification key* has been added to the RGBZ type *Document* so that several kinds of identifiers (URI, URI, DOI, ISBN) are supported.

In future, archiving will be done based on the Core RGBZ entity *Case*, via `case.archiefnominatie`.

[archiefGegevensdefinities]: image/EAID_59241C4B_FD65_484b_88E5_83189334A510.jpg "Archive data definitions"
[archiefEnBezoekers]: image/EAID_8D468696_4B9D_40b4_92F0_3BED39502098.jpg "Archive and visitors"
[archiefPersonenEnDocumenten]: image/EAID_EF872947_BE6B_4af5_8221_2A6AA2A0D4B7.jpg "Archive — persons and documents"
