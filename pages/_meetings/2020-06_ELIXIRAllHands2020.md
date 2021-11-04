---
layout: meeting
name: ELIXIR All Hands 2020
title: ELIXIR All Hands 2020
dates: 8-11 June 2020
start_date: 2020-06-08
end_date: 2020-06-11
venue: Virtual (<del>Eye Filmmuseum, IJpromenade 1, Amsterdam, 1031 KT, Netherlands</del>)
meeting-name: ELIXIR All Hands 2020
meeting-url: https://elixir-europe.org/events/elixir-all-hands-2020
agenda-doc: https://docs.google.com/document/d/1XielRIo0MTuoUSImH6NMmR-Zp0JDQ2sMSrd0knTthX4/edit?usp=sharing
contact-people:
    - AlasdairGray
attendees:
    - AlasdairGray
---

During the ELIXIR All Hands Meeting 2020, the Interoperability Platform session will be dedicated to matters relating to the Bioschemas Strategic Implementation Study. Details of this session are in the [agenda document]({{agenda-doc}}).

We have had two abstracts and one poster accepted for presentation at the ELIXIR All Hands Meeting 2020. The full abstracts are included below.

- [Exploiting Bioschemas Markup to Support ELIXIR Communities](#exploiting-bioschemas-markup-to-support-elixir-communities) accepted into the short talks session taking place on Wednesday 10 June at 10:00 (CEST)
- [Discovering Biodiversity Resources on the Web](#discovering-biodiversity-resources-on-the-web) accepted into the [Biodiversity mini-symposium](https://docs.google.com/document/d/11NDVkT5baCmFfA0bUdIxCauiKhfQofQPiXkJsnVAbP0/edit?usp=sharing) taking place on Monday 8 June at 12:00 (CEST)
- [eDGAR and PhenPath resources join the Bioschemas Community](#edgar-and-phenpath-resources-join-the-bioschemas-community-poster)


## Exploiting Bioschemas Markup to Support ELIXIR Communities

_Alasdair Gray and the Bioschemas Community_

Bioschemas aims to make life sciences resources more discoverable by exploiting widely deployed web search optimisation approaches. Specifically, the Bioschemas approach is to embed machine-readable markup using the Schema.org vocabulary within the web page about the resource. To achieve this, Bioschemas has focused on extending the Schema.org vocabulary to include life sciences types, such as Gene and Protein, and providing usage profiles that state how to markup a resource of a particular type; focusing on recommending a small number of properties that are most useful for search purposes. These types and profiles have been developed in conjunction with deployments of these on web sites where more than 11 million pages have been marked up by over 70 sites (November 2019).

In January 2020, the Bioschemas Strategic Implementation Study started with the goal of exploiting Bioschemas markup to the benefit of ELIXIR communities. This is being demonstrated in 3 communities: Rare Diseases, Plants, and Intrinsically Disordered Proteins (IDP). In each of these communities, we are enhancing the content of a community focused portal by automating the aggregation of data content from a large number of community resources. The approach lowers the bar for resources getting their content into the community portal as Bioschemas markup can easily be embedded in existing web pages without the need to deploy a complex web service implementing a community API. For example, in the Plants community the FAIDARE portal aggregates data from a small number of web services that implement the BrAPI standard. However, this means that the large number of resources which are available on the web, e.g. WheatIS or ORBITRAP, are not discoverable through FAIDARE. By adding Bioschemas markup into these sites, we are able to extend the content available through FAIDARE meaning that the community can more easily discover resources of interest.

To aggregate content from a large number of web resources, the community portals need to be able to extract the Bisochemas markup. This markup has been embedded on web sites that are deployed using a wide variety of frameworks and alternative markup formats (i.e. JSON-LD and RDFa). Increasingly websites are being deployed as single page applications where the HTML is rendered dynamically on the client’s machine based on the interaction of the user. This makes extracting markup a non-trivial task. B-MUSE has been developed to extract Bioschemas markup from web pages and deliver the structured content to the community portals. B-MUSE pulls content from a known list of web pages, rather than being a general web crawler. This enables the portal developers to focus on supporting their communities search for content within their portal.

## Discovering Biodiversity Resources on the Web

_Alasdair Gray, Franck Michel, Quentin Groom, and the Bioschemas Community_

There is an ever increasing quantity of data being published on the web. Within the area of Biodiversity there are large sequencing projects, e.g. Tree of Life, Barcode of Life, i5K, that are making vast quantities of data available. This makes discovering data and deciding its relevance increasingly challenging.

Bioschemas is an approach to make life sciences resources more discoverable by exploiting widely deployed web search optimisation approaches. Specifically, the Bioschemas approach is to embed machine-readable markup using the Schema.org vocabulary within the web page about the resource. To achieve this, Bioschemas has focused on extending the Schema.org vocabulary to include life sciences types and providing usage profiles that state how to markup a resource of a particular type; focusing on recommending a small number of properties that are most useful for search purposes. These types and profiles have been developed in conjunction with deployments of these on web sites where more than 11 million pages have been marked up by over 70 sites (November 2019). Deploying Bioschemas markup does not require special frameworks or to provide a Web API. The markup is embedded in existing web pages; making the human readable content of the pages understandable to machines.

The Bioschemas community now has proposals for 17 types that extend the Schema.org vocabulary to enable it to be used by the life sciences community. These include types such as Taxon, BioSample, and Phenotype, that are directly relevant to the Biodiversity community. There are deployments of these at the National Museum of Natural History of Paris and the Botanical Collections at the Meise Botanic Garden, Belgium.

To enable ELIXIR communities to exploit Bioschemas markup to populate community search portals, we have developed the B-MUSE directed crawler. B-MUSE will extract Bioschemas markup from a given set of pages or identifier pattern and make the structured content available for search. This approach has been demonstrated using the ELIXIR TeSS training portal, and is in active development in other ELIXIR communities, viz Rare Diseases, Plants, and Intrinsically Disordered Proteins.

## eDGAR and PhenPath resources join the Bioschemas Community ([poster](https://f1000research.com/posters/9-569))

_Giulia Babbi, Leyla Garcia, Alasdair Gray, Pier Luigi Martelli, and Rita Casadio_

Modern sequencing technologies allow dissecting the genetic component of phenotypic traits, particularly in relation to diseases. The number of known associations between genes and diseases or phenotypes is increasing; however, the information is still sparse among different resources. The integrative analysis of different data is fundamental for the elucidation of the molecular mechanisms at the basis of the pathogenesis. To support this type of research, we recently developed eDGAR (edgar.biocomp.unibo.it) and PhenPath (phenpath.biocomp.unibo.it).

eDGAR is a database collecting and organizing data on gene/disease associations as derived from OMIM, Humsavar and ClinVar. eDGAR lists 2672 diseases related to 3658 different genes, for a total of 5729 gene-disease associations. eDGAR provides analysis on the sets of genes involved in the same disease, in terms of physical, functional, and regulatory interactions, as derived from PDB, BIOGRID, STRING, CORUM, and TRRUST. Moreover, eDGAR exploits the network-based enrichment algorithm NET-GE (net-ge.biocomp.unibo.it/enrich) to provide a functional characterization of these gene sets in terms of Gene Ontology terms and Pathways from KEGG and Reactome. With a similar idea, PhenPath extends the analysis to phenotypes associated with different diseases following the Human Phenotype Ontology and of the OMIM Clinical Synopsys. With our resource, researchers and physicians can easily associate genes to more than 7000 phenotypes and characterize biological pathways/processes for a deeper understanding of molecular mechanisms and possible cures.

To make resources fully exploitable, to improve the FAIRness of the data and analyses they provide, we marked them up with Bioschemas markup; an extension of the Schema.org vocabulary for the life sciences. The inclusion of Bioschemas markup enables data interoperability and findability, allowing search engines and other resources to index and retrieve relevant information.

Both resources have been endowed with Bioschemas markup conforming with profiles for different entities. In particular:
1. Dataset, DataCatalog, Gene, and Protein are marked-up for eDGAR
1. Dataset, DataCatalog, and Phenotypes are marked up for PhenPath.

The latest versions of the Bioschemas profiles have been adopted; in particular, this work represents the first adoption of the Phenotype profile. The profile for Phenotype was developed in a preliminary draft form in 2018, and its further developments are now a topic for Bioschemas community, particularly in relation to the Schema.org type MedicalSignOrSymptom. The PhenPath implementation provides a test for the efficacy and the completeness of the current Phenotype profile and will help the definition of the requirements for its improvement, following the community needs and suggestions.
