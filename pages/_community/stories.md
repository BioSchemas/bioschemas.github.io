---
layout: default
title: Bioschemas stories
---
# Bioschemas stories

Here are some short stories where Bioschemas has been succesfully used by communities to progress on making their resources more findable and reusable. 

## bio.tools
*the 04th of April 2023*

[Bio.tools](http://bio.tools) is a heavily used registry cataloguing more than 24.000 bioinformatics software, services  and tools. The listings can be searched based on authors, scientific topics or type of data processing entailed, which is underpinned by the [EDAM](http://edamontology.org) ontology. By automatically transforming the database content, it has been possible to produce Schema.org annotations that are nowadays embedded into each bio.tools web page for better findability. 

These annotations can be used as the source for an RDF dataset, containing 550k+ triples, and  which is continuously updated at https://github.com/bio-tools/content/blob/master/datasets/bioschemas-dump.ttl. This dataset can be queried to retrieve useful information, such as the most used licences (GPL-3, MIT), or to identify the top-3 most represented data processing steps  (Visualisation, Standardisation/normalisation, Genotyping)

In addition, bio.tools metadata is further enhanced by providing embedded Bioschemas annotations, which are an opinionated view on native schema.org, but focusing domain specific properties. Thus, the bio.tools registry has made significant progress in the FAIRification of hosted resources, since bioschemas enhances compliance with many of the FAIR principles, particularly concerning metadata. This improvement can be qualified using FAIR assessment tools (F-UJI, FAIR Evaluator, FAIR-Checker). Since workflow registries such as WorkflowHub and educational portals such as TeSS are following the same semantic annotation strategies, new cross-linking and querying opportunities are under active investigation. 

*Further reading: [https://github.com/bio-tools/content/blob/master/doc/bioschemas.md](https://github.com/bio-tools/content/blob/master/doc/bioschemas.md)*

