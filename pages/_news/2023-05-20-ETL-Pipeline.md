---
layout: post
title: "BioHackathon 2022 preprint ETL for Knowledge Graph"
tags:
- Knowledge Graph
- JSON-LD
- SPARQL
- Community
---
We are pleased to announce, belatedly, that our preprint from [BioHackathon 2022](https://2022.biohackathon-europe.org/) is available [here](https://doi.org/10.37044/osf.io/7f95d)

Abstract:

Schema.org and Bioschemas are lightweight vocabularies that aim at making the contents of web pages machine-readable so that software agents can consume that content and understand it in an actionable way. Due to the time needed to process each page, extracting markup by visiting each page of a site is not practical for huge sites. This approach imposes processing requirements on the publisher and the consumer. The Schema.org community proposed a method for exchanging markup from various pages as a DataFeed published at a recognized address in February 2022. This would ease publisher and customer processing requirements and accelerate data collection. In this work, we report on the implementation of a JSON-LD consumer ETL (Extract-Transform-Load) pipeline that enables data dumps to be ingested into knowledge graphs (KG). The pipeline loads scraped JSON-LD from the three sources, converts it to RDF, applies SPARQL construct queries to map the source RDF to a unified Bioschemas-based model and stores the resulting KG as a turtle file. This work was conducted during the one-week Biohackathion Europe 2022 in Paris France, under Project 23 titled, “Publishing and Consuming Schema.org DataFeeds.”









