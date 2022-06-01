---
layout: use-case
name: Genes
group: genes
active: true
redirect_from: 
- "/useCases/Genes/"
- "/useCases/Genes"
---

This use cases apply to the following biological types: [Gene](/Gene).

### Findability

As a user, I would like to find as many gene resources as possible when looking by gene entity/name/identifier (ID).

### Summarization

As a user, when I look for a gene, I would like to get a quick summary with information regarding gene entities. Such summary should contain at least the data sources, IDs, names and organisms for the gene entity. Additionally, it could contain alternatively spliced transcript, sequence, citations, protein structure and gene features such as genetic variants (SNPs and mutations), regulatory features (promoter regions, enhancers, transcription factor binding sites, sites for methylation):

1.  Search for a gene or transcript (to include IDs, names, synonyms)
2.  Enable discovery by indexing on free text description
3.  Enable direct access, resolution of gene entity
4.  Allow restriction to specific isoforms (alternatively spliced transcripts)
5.  Search according to a disease linked to that gene, author
6.  Allow restriction to where the gene belongs to (human, mouse – which strain, wheat, etc)

### Link to external resources

As a user, I want to be able to distinguish what is a gene, what is a transcript, whether the gene is protein coding or not, whether it is associated with diseases or other phenotypes, where it has orthologues in other species or paralogs, duplicated versions in the same organism. I also want to be able to gather genetic variation information from as many variation and genomic resources as possible; this would be useful, for instance, to create visualisation tools or to enrich other pages/databases.

### Gene Related Resources

The following is a non-exhaustive list of external resources containing gene related information:

*   Ensembl: genes in vertebrates ( species including human, mice – 16 strains, rat, zebrafish, chicken and ?? more)
*   Ensembl Metazoa: genes in non-vertebrate metazoa (mosquitos, worms, flies)
*   Ensembl Fungi: genes in fungi (e.g. S. cerevisiae)
*   Ensembl Plants: genes in plants (e.g. soybean, wheat, tomato)
*   Ensembl Protists: genes in parasites (e.g. Plasmodium sp)
*   Ensembl Bacteria: genes in ?? K bacteria (these are all intronless, hence 1 gene à 1 transcript, no alternatively spliced transcripts)
*   NCBI EntrezGene
*   UCSC genome browser
*   GeneCards
*   Open Targets Platform
*   Open Targets Genetics
*   DisGeNET
*   Official gene nomenclatures e.g. HGNC (human), MGI (mouse), ZNF (zebrafish), RDG (rat), Wormbase (C. elegans), Yeast (SGD) \* All summarized in Alliance of Genome Resources (AGR) and Monarch Initiative
*   List of agricultural databases ([https://www.agbiodata.org/databases](https://www.agbiodata.org/databases))
*   Wikigenes
*   OMIM
*   Literature search: Europe PMC, PubMed, LINK (literature knowledge graph with semantic relationships for genes among other entities)
*   Cancer Gene Census
*   Gene2Phenotype
*   miRBase (microRNA db)
*   Orphanet, rare disease genes
*   Locus specific databases, such as the Leiden Open Variation Database
*   [MyGene.info](https://mygene.info) API (gene-centric high-performance API, a part of [BioThings API](https://biothings.io) project). A typical gene object from MyGene.info is like this: [http://mygene.info/v3/gene/1017](http://mygene.info/v3/gene/1017).