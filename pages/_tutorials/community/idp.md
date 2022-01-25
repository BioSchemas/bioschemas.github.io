---
layout: default
title: Tutorial for marking up IDP community resources

bioschemas:
  "@context": https://schema.org/
  "@type": LearningResource
  "http://purl.org/dc/terms/conformsTo":
  - "@type": CreativeWork
    "@id": "https://bioschemas.org/profiles/TrainingMaterial/0.9-DRAFT-2020_12_08/"
  about:
  - "@id": http://edamontology.org/topic_0089
  audience:
  - "@type": Audience
    name: (Markup provider, Markup consumer) WebMaster
  name: "How to check your Bioschemas deployment"
  author:
  - "@type": Person
    name: "Alasdair Gray"
    "@id": https://bioschemas.org/people/AlasdairGray
    url: https://bioschemas.org/people/AlasdairGray
  contributor:
  - "@type": Person
    name: "Ivan Mi&ccaron;eti&cacute;"
    "@id": https://bioschemas.org/people/IvanMicetic
    url: https://bioschemas.org/people/IvanMicetic
  dateModified: 2022-01-25
  description: "This tutorial will show you how to mark up IDP community resources using Bioschemas."
  keywords: "schemaorg, JSON-LD, bioschemas"
  license: CC-BY 4.0
  version: 1.1
---

# Tutorial for marking up IDP community resources

## Overview

This tutorial shows how to implement Bioschemas markup to a community resource. It describes Bioschemas profiles needed for a successful markup, their format and deployment on web pages. Adding a sitemap to a web site as well as registering persistent identifiers to resource data records completes the markup of a resource. These actions will ensure successful consumption of Bioschemas markup aiding resource data findability and interoperability.

## Bioschemas profiles for IDP resources

Main IDP resources are primary or aggregating databases describing aspects of intrinsically disordered proteins. As such, they are marked up with Bioschemas as a typical database using three profiles:
* `DataCatalog`: describes the site providing the data
* `Dataset`: describes the data releases from the site
* `Protein`: a profile describing data records, usually `Protein` in the IDP community; these can be supplemented with `SequenceAnnotation` and `SequenceRange` to denote annotations on the protein sequence

Every resource is described with a `DataCatalog` profile. That profile specifies the provider of the resource, it’s version, license, keywords, description, format and so on. The `DataCatalog` profile contains one or more `Dataset` profiles which have their own version, license, keywords and description. The difference between `DataCatalog` and `Datasets` can be explained with the [UniProt](https://www.uniprot.org/) resource as an example. UniProt is the `DataCatalog` that contains Swiss-Prot and TrEMBL `Dataset`s.

## Format and placement of Bioschemas profiles

Because Bioschemas is an extension of schema.org, it uses the same formats for embedding web pages: Microdata, RDFa and JSON-LD. Bioschemas community recommends JSON-LD format for embedding the markup. All implementations of Bioschemas in IDP resources also use the markup in JSON-LD format.

The three profiles must not be published on all web pages of a resource. Database resources should have `DataCatalog` and `Dataset`(s) markup on their home pages while entry pages (pages holding data records) should have only `Protein` records. All other pages (About, Help and others) should be void of markup. This implies that a mechanism must be in place that adds and removes dynamically schema profiles from web pages, especially in single page applications. Our suggestion is to place the markup as JSON-LD script in the document head with an id attribute (one for `DataCatalog` and `Dataset` schema and one for data record schema). In that way it will be relatively simple to toggle the visibility of the whole element containing the markup depending on the page that is being requested.

## Example profiles for IDP resources

### `DataCatalog`

```json
     1	{
     2	  "@context": "https://schema.org/",
     3	  "@type": "DataCatalog",
     4	  "@id": "https://disprot.org/#DataCatalog",
     5	  "http://purl.org/dc/terms/conformsTo": {
     6	    "@type": "CreativeWork",
     7	    "@id": "https://bioschemas.org/profiles/DataCatalog/0.3-RELEASE-2019_07_01"
     8	  },
     9	  "sameAs": "https://registry.identifiers.org/registry/disprot",
    10	  "url": "https://disprot.org/",
    11	  "identifier": "https://registry.identifiers.org/registry/disprot",
    12	  "name": "DisProt, The database of intrinsically disordered proteins",
    13	  "description": "DisProt is a database of…",
    14	  "datePublished": "2019-09",
    15	  "dateModified": "2021-08",
    16	  "citation": {
    17	    "@type": "ScholarlyArticle",
    18	    "@id": "https://doi.org/10.1093/nar/gkz975",
    19	    "name": "DisProt: intrinsic protein disorder annotation in 2020",
    20	    "url": "https://doi.org/10.1093/nar/gkz975",
    21	    "sameAs": [
    22	      "https://academic.oup.com/nar/advance-article/doi/10.1093/nar/gkz975/5622715",
    23	      "https://pubmed.ncbi.nlm.nih.gov/31713636/"
    24	    ]
    25	  },
    26	  "keywords": [
    27	    "IDP",
    28	    "IDPs",
    29	    … 
    30	  ],
    31	  "sourceOrganization": [
    32	    {
    33	      "@type": "Organization",
    34	      "@id": "https://biocomputingup.it/#Organization",
    35	      "http://purl.org/dc/terms/conformsTo": {
    36	        "@id": "https://bioschemas.org/profiles/Organization/0.2-DRAFT-2019_07_19",
    37	        "@type": "CreativeWork"
    38	      },
    39	      "description": "University of Padua, Department of …",
    40	      "name": "BioComputing UP, Department of …",
    41	      "legalName": "University of Padua",
    42	      "sameAs": "https://biocomputingup.it"
    43	    }
    44	  ],
    45	  "provider": [
    46	    {
    47	      "@type": "Person",
    48	      "givenName": "Silvio",
    49	      "familyName": "Tosatto",
    50	      "identifier": "https://orcid.org/0000-0003-4525-7793",
    51	      "name": "Silvio Tosatto",
    52	      "email": "user@domain.org",
    53	      "url": "https://biocomputingup.it/people/silvio"
    54	    }
    55	  ],
    56	  "encodingFormat": [
    57	    "text/html",
    58	    "application/json"
    59	  ],
    60	  "license": {
    61	    "@type": "CreativeWork",
    62	    "@id": "https://creativecommons.org/licenses/by/4.0/",
    63	    "name": "Creative Commons CC4 Attribution",
    64	    "url": "https://creativecommons.org/licenses/by/4.0/"
    65	  },
    66	  "dataset": {
    67	    "@type": "Dataset",
    68	    …
    69	  }
    70	}
```
### `Dataset`

```json
     1	{
     2	  "@type": "Dataset",
     3	  "@id": "https://disprot.org/#2021-08",
     4	  "http://purl.org/dc/terms/conformsTo": {
     5	    "@id": "https://bioschemas.org/profiles/Dataset/0.3-RELEASE-2019_06_14",
     6	    "@type": "CreativeWork"
     7	  },
     8	  "includedInDataCatalog": {
     9	    "@id": "https://disprot.org/#DataCatalog"
    10	  },
    11	  "url": "https://disprot.org/",
    12	  "dateModified": "2021-08",
    13	  "version": "8.3",
    14	  "name": "DisProt",
    15	  "description": "DisProt is …",
    16	  "identifier": "https://disprot.org/#2020-12",
    17	  "keywords": [
    18	    "IDP",
    19	    "IDPs",
    20	    …
    21	  ],
    22	  "creator": {
    23	    "@id": "https://biocomputingup.it/#Organization"
    24	  },
    25	  "license": {
    26	    "@type": "CreativeWork",
    27	    "@id": "https://creativecommons.org/licenses/by/4.0/",
    28	    "name": "Creative Commons CC4 Attribution",
    29	    "url": "https://creativecommons.org/licenses/by/4.0/"
    30	  }
    31	}
```

The whole `Dataset` profile can be included in the `DataCatalog` JSON object under the dataset key (`DataCatalog` lines 66-69).

### Data record profile: `Protein`

In case of data records describing a single protein entity, a Bioschemas Protein 0.11 profile can be used:
```json
     1	{
     2	  "@context": "https://schema.org",
     3	  "includedInDataset": "https://disprot.org/#2021-08",
     4	  "@type": "Protein",
     5	  "@id": "https://disprot.org/DP00003",
     6	  "http://purl.org/dc/terms/conformsTo": {
     7	    "@id": "https://bioschemas.org/profiles/Protein/0.11-RELEASE",
     8	    "@type": "CreativeWork"
     9	  },
    10	  "identifier": "https://identifiers.org/disprot:DP00003",
    11	  "sameAs": "http://purl.uniprot.org/uniprot/P03265",
    12	  "name": "DNA-binding protein",
    13	  "taxonomicRange": {
    14	    "@type": "DefinedTerm",
    15	    "termCode": "28285",
    16	    "url": "http://purl.bioontology.org/ontology/NCBITAXON/28285",
    17	    "sameAs": [
    18	      "http://purl.uniprot.org/taxonomy/28285",
    19	      "https://identifiers.org/taxonomy:28285",
    20	      "http://purl.obolibrary.org/obo/NCBITaxon_28285"
    21	    ],
    22	    "inDefinedTermSet": {
    23	      "@type": "DefinedTermSet",
    24	      "name": "NCBI taxon",
    25	      "url": "https://bioportal.bioontology.org/ontologies/NCBITAXON"
    26	    }
    27	  },
    28	  "hasBioPolymerSequence": "MASREEEQRET…",
    29	  "hasSequenceAnnotation": [
    30	    {
    31	      "@type": "SequenceAnnotation",
    32	      "@id": "https://disprot.org/DP00003#disorder-content",
    33	      "http://purl.org/dc/terms/conformsTo": {
    34	        "@id": "https://bioschemas.org/profiles/SequenceAnnotation/0.7-DRAFT",
    35	        "@type": "CreativeWork"
    36	      }
    37	      "sequenceLocation": {
    38	        "@type": "SequenceRange",
    39	        "rangeStart": 1,
    40	        "rangeEnd": 529
    41	      },
    42	      "additionalProperty": {
    43	        "@type": "PropertyValue",
    44	        "name": "Protein disorder content",
    45	        "propertyID": {
    46	          "@id": "https://disprot.org/assets/data/IDPO_v0.2.owl#IDPO:00499"
    47	        },
    48	        "value": 0.09829867674858223
    49	      }
    50	    },
    51	    {
    52	      "@type": "SequenceAnnotation",
    53	      "@id": "https://disprot.org/DP00003r002",
    54	      "http://purl.org/dc/terms/conformsTo": {
    55	        "@id": "https://bioschemas.org/profiles/SequenceAnnotation/0.7-DRAFT",
    56	        "@type": "CreativeWork"
    57	      }
    58	      "sequenceLocation": {
    59	        "@type": "SequenceRange",
    60	        "rangeStart": 294,
    61	        "rangeEnd": 334
    62	      },
    63	      "additionalProperty": [
    64	        {
    65	          "@type": "PropertyValue",
    66	          "name": "Term",
    67	          "value": {
    68	            "@type": "DefinedTerm",
    69	            "@id": "https://disprot.org/assets/data/IDPO_v0.2.owl#IDPO:00076",
    70	            "inDefinedTermSet": {
    71	              "@type": "DefinedTermSet",
    72	              "@id": "https://disprot.org/assets/data/IDPO_v0.2.owl",
    73	              "name": "IDP ontology"
    74	            },
    75	            "termCode": "IDPO:00076",
    76	            "name": "disorder"
    77	          }
    78	        }
    79	      ],
    80	      "subjectOf": {
    81	        "@type": "ScholarlyArticle",
    82	        "@id": "https://identifiers.org/pubmed:8632448"
    83	      }
    84	    }
    85	  ]
    86	}
```

Note the presence of two `SequenceAnnotation` profiles. The first one (lines 30-50) shows how to annotate a protein region (in this case the whole protein) to an ontology term which has a numerical value. The second one (lines 51-84) shows how to apply an ontology term to a part of a protein (defined by `SequenceRange`).

Several proteins or other biochemical entities may be represented in a single data record. In case of an ensemble, such a record can be encoded as a list of multiple `Protein` profiles:

```json
{
  "mainEntity": {
    "@type": "ItemList",
    "numberOfItems": 3,
    "itemListElement": [
      {
        "@type": "Protein",
        …
      },
    ]
  }
}
```

## Web resource site map

Web crawlers, validators, and scrapers must know what are the pages on a website in order to crawl it efficiently. A site map of a web resource is a list of all the pages that should be accessed by crawlers. Such a  site map can be produced by placing a sitemap file (named sitemap.xml) at the root of the domain. A simple XML sitemap example looks like this:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>http://www.example.net/</loc>
    <lastmod>2009-09-22</lastmod>
  </url>
  <url>
    <loc>http://www.example.net/help</loc>
    <lastmod>2009-09-22</lastmod>
  </url>
  <url>
    <loc>http://www.example.net/data/1</loc>
    <lastmod>2009-09-22</lastmod>
  </url>
</urlset>
```

Sitemaps are limited to 50,000 URLs. Resources with a larger number of web pages (data records) or dynamic, single page applications can use a sitemap index file. Such a file can include 50,000 individual sitemaps bringing the overall number of accessible pages to more than a billion URLs.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
   <sitemap>
      <loc>https://website.org/sitemap1.xml.gz</loc>
   </sitemap>
   <sitemap>
      <loc>https://website.org/sitemap2.xml.gz</loc>
   </sitemap>
</sitemapindex>
```

## Persistent identifiers for data records

Bioschemas promotes the use of persistent identifiers for data records in life sciences. Web resources such as databases (registries, repositories) are encouraged to register a unique URI to all data records within the resource. The registration can be done by requesting a namespace in [Identifiers.org](https://identifiers.org/). A namespace uniquely identifies the data collection while a namespace suffix identifies the data record within the collection. The whole Identifiers.org URI is used throughout Bioschemas markup whenever possible (e.g. line 10 and 19 in the data record profile example).
