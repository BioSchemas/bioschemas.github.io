---
layout: use-case
name: Phenotypes
group: phenotypes
active: true
---

This use cases apply to the following biological types: “phenotype”.

The International Mouse Phenotyping Consortium (IMPC) is systematically generating mouse knockouts for every protein-coding gene in the mouse genome (approx. 20,000 genes) and carries out high-throughput phenotyping of each line in order to determine gene function by determining the biological systems affected in the absence of the gene. This dataset contains all the genotype-to-phenotype associations, protocols, parameters and measurements currently generated using this approach. For the IMPC, and other similar consortiums, is important to make their Gene-Phenotype associations findable from the Phenotype perspective. In order to achieve this a Phenotype profile should fulfill the following requirements:*   It should make explicit the relation between a Gene and a Phenotype and specify if the association is significant or not (Does the presence of the Gene A is significant on the occurrence of the Phenotype B?)
*   It should be clear which Procedure (http://bioschemas.org/types/LabProtocol/) was used to make the association. Note that for human disease phenotypes the association is typically made by a physician who links the phenotype to an individual patient and later geneticist use linkages and at later stages sequencing of identified genetic regions to link the disease to genetic variation.
*   It should be clear which allele of the Gene was used to generate the association.
*   It should be clear over which group of mice (individuals) and samples (http://bioschemas.org/types/Sample/) the procedure was applied to make the association.
*   It should allow to perform searches using anatomical terms related to the phenotype occurrence.
*   It should make explicit the respective organism where the defined Phenotyped is present.
