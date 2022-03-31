---
layout: use-case
name: Disease
group: disease
active: true
---

These use cases apply to the following biological types: “disease”.

There are many disease classifications available and many efforts have been recently done to organize diseases systematically into ontologies (like the Human Disease Ontology at EMBL-EBI). On the other hand, medical doctors and the World Health Organization still use different catalogues, like the ICD (International Classification of Diseases). Moreover, medical records do not always follow either bioinformatics ontologies or international standards, making this data very difficult to be collected and analysed properly.

Facing this situation, it is important to make disease records more findable, improving the quality of web searches also for non-experts, and developing guidelines for disease markup. Recently Schema.org released the types MedicalCondition, and its most specific type InfectiousDisease, that could be good starting point for the profile Disease.

In order to achieve this, a Disease profile should fulfil the following requirements:

*   It must have name, id and description (minimum);
*   It should make explicit the relations among Disease and one or more Genes, or Disease and one or more Proteins (recommended);
*   It should have aliases, both in ontologies as well as free text (recommended);
*   It may specify the mode of inheritance;
*   It may specify the related phenotypes;
*   It may specify the related biological process;
*   It may specify the related drugs;
*   It may contain references to specific alleles;
*   It may contain references to the anatomical district of interest;
