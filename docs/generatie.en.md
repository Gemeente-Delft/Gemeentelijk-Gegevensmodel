---
description: "Generating database schemas (DDL) from the Municipal Information Model: ready-made DDL files and code-generation templates for Enterprise Architect."
---

# Database schemas

## Ready-made database schemas

From release v2.4.0 of the Delft Municipal Data Model (Dutch: *Gemeentelijk Gegevensmodel*, abbreviated **GGM**) onwards, a complete set of [DDL files (Data Definition Language)](https://en.wikipedia.org/wiki/Data_definition_language) is also available — 488 DDLs in total, automatically generated using a batch version of the UML Database Generator (which will soon be released to a wider audience). This batch generator processes all relevant diagrams and exports the corresponding DDL scripts per diagram in several database formats:

* MySQL
* MSSQL
* Oracle
* PostgreSQL

This gives you ready-made schemas for these common databases. The DDLs are intended for developers, data architects and administrators who want to apply the GGM in their own systems or environments. Thanks to this set, it is now possible to work with the GGM data models **without using Enterprise Architect — fully tool-independent**. The DDL files can be loaded or modified directly with standard SQL tools and editors.
Note: this is an early version of the generator. Some imperfections may still occur in the generated files. Feedback is welcome.

You will find the DDLs for the listed databases in the [`ddl` directory of the release directory](https://github.com/Gemeente-Delft/Gemeentelijk-Gegevensmodel/tree/master/v2.5.0/ddl%20(early%20release)).

## Code generation based on the GGM

If you want to generate DDL yourself with Enterprise Architect, the GGM ships with a set of code-generation templates for use within Enterprise Architect to generate [Data Definition Language (DDL)](https://en.wikipedia.org/wiki/Data_definition_language). With this you can directly create tables in an RDBMS. Various templates are available for generating database tables and program code (for example: Python, C# and Java). Code generation works for all supported RDBMSs, except for some specific items such as enumerations. We have developed those for:

1. Oracle
2. MySQL (untested)
3. We warmly invite developers to use these and improve their suitability for the GGM.

The supplied templates are extensions to the standard templates of [Enterprise Architect](https://sparxsystems.com), as part of the [Code Template Framework](https://sparxsystems.com/enterprise_architect_user_guide/17.0/modeling_domains/codetemplates_2.html).

### Installing the code-generation templates

1. Download the file [CodegeneratieTemplates.xml](https://github.com/Gemeente-Delft/Gemeentelijk-Gegevensmodel/blob/master/v2.5.0/CodegeneratieTemplates.xml).
2. Start Enterprise Architect.
3. (Optional) Create a new project.
4. Choose *Import Reference Data*.

![Import Reference Data][importRefData]

<em>Screenshot (in Dutch / Enterprise Architect UI): the "Import Reference Data" option.</em>

5\. Select the just-downloaded `CodegeneratieTemplates.xml`, select all templates and press *Import*.

![Import Templates][kiesTemplates]

<em>Screenshot: selecting all templates in the import dialog.</em>

6\. The templates are ready to use; you find them under *Transform*.

![Use Templates][gebruikTemplates]

<em>Screenshot: the imported templates available under the Transform menu.</em>

7\. Done!

### Using the code-generation templates

Generating DDL from the GGM consists of two steps:

1. Transforming the logical model into a logical table representation.
2. Generating DDL from the logical table representation.

#### Before you start

First make sure your project has, alongside the GGM, a place where you can write the tables. We use a separate node next to the root node — in the example, the folder `<<DataModel>> Tables/Ruimte/Afval`.

![Create a place to generate the tables][tablesAfval]

<em>Screenshot (in Dutch / Enterprise Architect UI): folder structure for generated tables.</em>

Then make sure the default RDBMS is selected in Enterprise Architect. Go to *Preferences*.

![Go to Preferences to select the default RDBMS][kiesPreferences]

<em>Screenshot: the Preferences menu.</em>

Then under *Source Code Engineering / Code Editors* choose *Default Database*. In our example, Oracle.

![Select the default RDBMS][selecteerDefaultRDBMS]

<em>Screenshot: setting Oracle as the default database.</em>

#### Steps to generate DDL

To generate DDL, take the following steps:

1\. Select the part of the model you want to generate. In the example, the folder `Gemeentelijk Gegevensmodel/Ruimte/Afval/Model`. You can also select the desired object types in a diagram.

![Select the folder in the model][selecteerInModel]

<em>Screenshot: the model folder selected for generation.</em>

2\. For the first step in generation, choose *Apply Transformation*.

![Choose Apply Transformation][applyTransformation]

<em>Screenshot: the Apply Transformation menu option.</em>

3\. On the right side of the popup, select *Tables* in the *Transformations* area. Make sure all object types that should be generated are selected on the left side.

![Choose Tables under Transformation][kiesTables]

<em>Screenshot: the Transformations dialog with "Tables" selected.</em>

4\. In the new *Select Target Package* popup, select the place you created to write the tables. In our example, `<<DataModel>> Tables/Ruimte/Afval`.

![Choose Target Package][selectTargetPackage]

<em>Screenshot: target package selection dialog.</em>

5\. To start the first step, click *Do Transform*.

![Choose Do Transform][selectDoTransform]

<em>Screenshot: "Do Transform" button highlighted.</em>

6\. Wait a moment — the first generation step has been performed: the tables in Enterprise Architect have been created. A "logical" RDBMS-independent version of the tables now exists.

![Wait a moment… and the tables have been created][tabellenAangemaakt]

<em>Screenshot: the generated logical tables visible in the Project Browser.</em>

7\. In the next step, you generate DDL from the "logical" RDBMS-independent table version. Select the folder containing the tables that were just generated.

![Select the folder with the tables you want to generate][selecteerTabellen]

<em>Screenshot: selecting the table folder in the Project Browser.</em>

8\. Under *Develop / Datamodelling*, choose *Generate*.

![Under "Develop / Datamodelling" choose "Generate"][kiesGenerate]

<em>Screenshot: the Generate option in the Datamodelling menu.</em>

9\. Enter a file name and folder, and press *Generate*.

![Press Generate][kiesGenerateDDL]

<em>Screenshot: the Generate DDL dialog with file name filled in.</em>

10\. Wait a moment — the DDL is ready. Done!

### How it works internally

The capabilities of the code-generation templates limit what you can do when modelling in the GGM. Data types and relationships not supported by the templates cannot be (automatically) converted to tables, and cannot be used well when applied. The following describes what you can use in the logical model and how it transforms to tables.

#### Object types (Classes)

When generating table names, the following order applies (all names are truncated to a maximum of 30 characters):

1. Alias
2. Object-type name

If the folder containing the object type has an Alias, it is used as a prefix for the table name. In addition, two columns are added to every table (intended to be filled when populating the data warehouse):

1. `DWH_Bronsysteem` (name of the source system from which data was loaded)
2. `DWH_DatumTijdGeladen` (system date/time when data was loaded)
3. `DWH_DatumTijdGeldigVanaf` (for history: date and time **from** which the record is valid)
4. `DWH_DatumTijdGeldigTotMet` (for history: date and time **up to and including** which the record is valid)

If an object type has a Stereotype, it is used as follows:

* `enumeration` (Oracle and MySQL only): converted to a table with a `_ENUM_` table-name prefix. The table always has the columns: ID, value and description. The various attributes are converted to INSERT statements so the table is filled. Attribute fields map as follows:

    * ID: attribute field *Alias*
    * value: attribute field *Name*
    * description: attribute field *Comment*

* `referentielijst`: table with table-name prefix `_LST_`.

#### Attributes

The code-generation templates convert the various attributes of GGM object types based on *Datatype* and *Stereotype*. These extend the [Code Template Framework](https://sparxsystems.com/enterprise_architect_user_guide/15.0/model_domains/codetemplates_2.html) of Enterprise Architect. For attribute (column) names the order is:

1. Alias
2. Attribute name

Attributes are converted by data type as follows (case-insensitive):

* `Datumtijd` or `Datetime`: attribute with both date and time (Oracle: DATE field).
* `Datum` or `Date`: date only.
* `Tijd` or `Time`: time only.
* `ANxxx`: text field (alphanumeric) of length xxx. If no length is given, length 80 is used.
* `Integer` or `Int`: numeric field (integers only).
* `Double`: numeric values with decimals.
* `Bedrag`: amount field (max 10 digits, 2 after the decimal).
* `Tekst` or `Text`: text field for long memo fields.
* `Boolean`: Boolean (Oracle numeric field: 'J'=1, 'N'=2, 'Other'=-1, 'Unknown'=null).
* `GUID`: text field of 40 characters.
* `GML` or `Punt`: location — split into two fields for [WGS84 coordinates](https://nl.wikipedia.org/wiki/WGS_84) (`<fieldname>_lat` and `<fieldname>_long`) and two fields for [Dutch RD coordinates](https://zakelijk.kadaster.nl/rijksdriehoeksstelsel) (`<fieldname>_rdx` and `<fieldname>_rdy`). All fields are doubles.

Attributes are converted by Stereotype:

* `Adresaanduiding` (address designation): the field is replaced by: municipality name, street name, house number, house letter, house-number suffix, postal code and BAG ID.
* `enumeration`: a reference to the enumeration is included. See Example D.

#### Relationships

Translating relationships in the logical model is not always straightforward — particularly for the naming of [foreign keys](https://en.wikipedia.org/wiki/Foreign_key) and [foreign-key constraints](https://www.w3schools.com/sql/sql_foreignkey.asp). Three examples follow.

##### Example A

The first example shows 4 object types/classes with three relationships:

1. Relationship A: 1:N
2. Relationship B: N:M
3. Generalisation of Class A relative to Child Class A

![Example A before generating to tables][voorbeeldA]

<em>Diagram: four classes with three relationships before transformation to tables.</em>

After transformation, these relationships translate as follows:

1. Relationship A: column `ClassAID` in table `ClassB` with a foreign key to table `ClassA`.
2. Relationship B: a junction table `KP_classa_classc` with foreign-key relationships to `ClassA` and `ClassB`.
3. Generalisation: the two tables remain separate; columns are not copied into the *child*. A regular 1:N relationship is created, like Relationship A.

![Example A after generating to tables][voorbeeldATabellen]

<em>Diagram: the resulting tables with foreign-key columns and a junction table.</em>

##### Example B

The naming of foreign keys, foreign-key constraints and junction tables can be influenced through relationship names and aliases. This avoids duplicate constraints and unreadable or overly long names. The order used (in priority) is:

1. Alias of Source/Target
2. Alias of relationship
3. Relationship name
4. Concatenation of Source and Target names

The example covers:

1. Relationship `Class A`–`Class B`: relationship name = "Relatienaam".
2. Relationship `Class C`–`Class D`: relationship has Alias "Aliasnaam".
3. Relationship `Class E`–`Class F`: both Source and Target have their own alias.
4. Relationship `Class G`–`Class H`: relationship has no name and no aliases.
5. Relationship `Class I`–`Class J`: same as 4 but Source and Target swapped.

![Example B before generating to tables][voorbeeldB]

<em>Diagram: the five relationship variants before transformation.</em>

After transformation:

1. First: table `ClassA` gets column `ClassBID` (with index) and a foreign-key constraint (using the relationship name) on the relationship to `ClassB`.
2. Second: table `ClassC` gets column `ClassCID` (with index) and a foreign-key constraint (using the alias) on the relationship to `ClassC`.
3. Third: table `ClassE` gets column `AliasSourceCID` (with index) and a foreign-key constraint (using source/target aliases) on the relationship to `ClassF`.
4. Fourth: table `ClassG` gets column `ClassHID` (with index) and a foreign-key constraint (using table names) on the relationship to `ClassH`.
5. Fifth: table `ClassI` gets column `ClassJID` (with index) and a foreign-key constraint (using table names) on the relationship to `ClassJ` (same as 4).

![Example B after generating to tables][voorbeeldBTabellen]

<em>Diagram: resulting tables for the five relationship variants.</em>

##### Example C

Cases that need special attention because the transformation process otherwise produces errors:

1. Self-relationships (e.g. *pig sub-type* / *Varkensoortje*).
2. Multiple relationships between the same object types.

![Example C before generating to tables][voorbeeldC]

<em>Diagram (in Dutch): the "Varkensoortje" example showing a self-relationship.</em>

To make these work in the transformation, you must provide an Alias on the Source of the relationship. The example shows it for *Varkensoortje*. You can also use this for multiple relationships. Due to Enterprise Architect's internals, the cardinality on the source side must be 0..1 or 1, otherwise the relationship is not generated correctly.

![Enter an alias on the Source of "Varkensoortje"][varkensoortje]

<em>Screenshot (in Dutch / Enterprise Architect UI): setting the Source alias on the self-relationship.</em>

After transformation, the alias is used for the foreign keys and constraints, ensuring unique names.

![Example C after generating to tables][voorbeeldCTabellen]

<em>Diagram: the resulting tables with alias-based foreign-key naming.</em>

##### Example D

Finally, an example with enumerations:

[Enumerations](https://en.wikipedia.org/wiki/Enumerated_type) are an enumeration of possible values for a given attribute. They allow you to constrain attribute values within a set range in the GGM. To make these work in the transformation process, you must provide an Alias on the Source of the relationship. The example shows it for *Varkensoortje*; you can also use this for multiple relationships. The following shows how to define an enumeration.

![Example Enumeration][voorbeeldD]

<em>Diagram (in Dutch): an enumeration with two possible values (Optie 1, Optie 2), referenced by attribute B.</em>

The enumeration has two possible values: Option 1 and Option 2; attribute B refers to this enumeration.

![Coupling enumeration][voorbeeldDStereotype]

<em>Screenshot (in Dutch / Enterprise Architect UI): linking an attribute to an enumeration via the "enumeration" stereotype.</em>

The screenshot shows how to link an attribute to an enumeration. It is important to set the stereotype value to `enumeration`.

![Creating value lists for enumerations][voorbeeldDAtt]

<em>Screenshot (in Dutch / Enterprise Architect UI): defining the value list of an enumeration as attributes.</em>

The figure shows how to define value lists for an enumeration in Enterprise Architect. In the example the value list consists of two values: Optie 1 and Optie 2, defined as attributes of the class *Enumeration A*. Fill them in as follows:

1. Name: in the *Name* field of the attribute (always fill in to avoid errors).
2. Index: in the *Alias* field (always a unique integer to avoid errors).
3. Description: in the *Notes* field.
4. Stereotype: always `enum`.

After transformation, both the class and the enumeration become tables, linked by a foreign-key constraint.

![Generating enumerations][voorbeeldDTabellen]

<em>Diagram: the generated tables for the class and its enumeration, linked via a foreign key.</em>

In the generated model, the value lists are still attributes of the enumeration. Only when generating physical database schemas are they converted to value lists in the table.

### Customising templates yourself

Once the templates are loaded in Enterprise Architect you can customise them to match your needs. Note that DDL generation runs in two steps, so you can adjust at two levels.

1. First step: customise templates that generate database-independent tables.
2. Second step: customise the generation of database-independent tables to DDL.

#### First generation step

Go to *Transform templates*.

![Customising templates step 1][templatesAanpassenStap1]

<em>Screenshot: opening the Transform Templates editor.</em>

After opening, choose the language *Tables*. This collection of templates is used to convert to tables. All template parts used during generation are shown. The next screenshot shows the conversion from a Class.

![Customising templates step 2][templatesAanpassenStap2]

<em>Screenshot: editing the Class-to-Table transformation template.</em>

You are now ready to make your own changes. For more details see the [Sparx documentation on transformation templates](https://sparxsystems.com/enterprise_architect_user_guide/16.1/modeling_fundamentals/transformationtemplates.html).

### Second generation step

To customise the templates that convert database-independent tables to DDL for specific databases, on the *Design* tab choose *Templates*. Once opened, you can pick different database types. The figure below shows Oracle, with the scripts that generate the DDL.

![Templates for DDL generation][ddlgeneratieaanpassen]

<em>Screenshot (in Dutch / Enterprise Architect UI): the DDL generation templates for Oracle.</em>

We have customised the standard Enterprise Architect behaviour for Oracle and MySQL.


[tablesAfval]: image/TablesAfval.png "Create a place to generate the tables"
[selecteerInModel]: image/SelecteerInModel.png "Select the folder in the model"
[applyTransformation]: image/ApplyTransformation.png "Apply Transformation"
[kiesTables]: image/KiesTables.png "Choose Tables under Transformation"
[selectTargetPackage]: image/SelectTargetPackage.png "Choose Target Package"
[selectDoTransform]: image/SelectDoTransform.png "Choose Do Transform"
[tabellenAangemaakt]: image/TabellenAangemaakt.png "Tables created"
[kiesPreferences]: image/KiesPreferences.png "Go to Preferences"
[selecteerDefaultRDBMS]: image/SelecteerDefaultRDBMS.png "Select default RDBMS"
[selecteerTabellen]: image/SelecteerTabellen.png "Select tables to generate"
[kiesGenerate]: image/KiesGenerate.png "Generate"
[kiesGenerateDDL]: image/KiesGenerateDDL.png "Generate DDL"
[importRefData]: image/ImportRefData.png "Import Reference Data"
[kiesTemplates]: image/KiesTemplates.png "Choose templates"
[gebruikTemplates]: image/GebruikTemplates.png "Use templates"
[voorbeeldB]: image/EAID_6FCF9303_410D_4ff2_A577_C323F426A500.gif "Example B before generation"
[voorbeeldCTabellen]: image/EAID_15C4CFF6_5DC6_456a_AE2B_0298FA9CDB6F.gif "Example C after generation"
[voorbeeldC]: image/EAID_135DA4FB_69A6_4191_84A3_3B9F16641289.gif "Example C before generation"
[voorbeeldBTabellen]: image/EAID_0435B59E_F272_4227_BE64_F7A8FC9A30EE.gif "Example B after generation"
[voorbeeldATabellen]: image/EAID_9259B8B6_DD2F_4632_9CAE_8A0D9F30DF1F.gif "Example A after generation"
[voorbeeldA]: image/EAID_E7F774F3_E0B3_438e_80DC_4B2F2CD3C60B.gif "Example A before generation"
[varkensoortje]: image/Varkensoortje.png
[voorbeeldD]: image/VoorbeeldD.png "Example D — using enumerations"
[voorbeeldDAtt]: image/VoorbeeldD_EnumAttributen.png "Example D — enumeration attributes"
[voorbeeldDTabellen]: image/VoorbeeldD_Tables.png "Example D — generating tables"
[voorbeeldDStereotype]: image/VoorbeeldD_Stereotype.png "Example D — stereotype usage"
[templatesAanpassenStap1]: image/templatesaanpassen_stap1.png "Customising templates step 1"
[templatesAanpassenStap2]: image/templatesaanpassen_stap2.png "Customising templates step 2"
[ddlgeneratieaanpassen]: image/ddlgeneratieaanpassen.png "DDL generation templates"
