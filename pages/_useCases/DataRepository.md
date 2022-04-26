---
layout: use-case
name: Data Repositories
group: datarepositories
active: true
redirect_from: 
- "/useCases/DataRepositories/"
- "/useCases/DataRepositories"
---

### Data entity Identifiers

1.  If the identifier resolution is broken we need to know who to contact.
2.  Data repositories might change their identifier pattern. Resolution services do not have a way to know about these changes. Identifiers.org needs to know about these changes in order to resolve new patterns (n2t.net does not need to know about changes in order to resolve new patterns).
3.  For ids that are meant to resolve, need to check if the service is running with a test identifier.

### Release

1.  Services integrating data (e.g. Intermine) need to know when new data is updated.
2.  Data analysis, e.g. genomic data analysis needs stable archives to allow comparison and translation of datasets.
3.  As a data integrator I need to know the license of the data to know how I can use the data.

### Search and Browse

1.  To know what the resource is called, address etc. And to increase consistency in the data.
2.  As a researcher I would like to find all the data repositories providing molecular interactions information for a specific species.

### Data Access/Interfaces

1.  eg. intermine needs to know where to download data or where to find the programatic interfaces to access data. I need to know if there is any change in the structure of these interfaces.

### Citation

1.  I am a researcher and I want to acknowledge I am using a data repository. How should I cite the repository?

### Data provenance

1.  Capture the interdependencies between databases - where does the data come from?

### Type

1.  Knowledgebase or Archive? Maybe other types? Distinction between Knowledge Base and database (CG insists the best inspiration is to follow EXCELERATE approach)

### Formats

1.  What standards (including versions) are used in the database? Ideally referencing the BioSharing format in the URL.

### Metric

1.  User wants to know content statistics, data turnover, usage statistics (community adoption).

### Tools

1.  People want to know what tools are available and how to access them.

### Data repository identifier

1.  I need a way to reference the data resource using an identifier. Ideally this identifier should be assign by identifier.org.

### Datasets

1.  What are the data collections of data (datasets eg: predicted:trembl and curated:uniprot in uniprot) available in a data repository?
