---
layout: community_tutorial
title: How to add markup to IDP resources
nextTutorial:
  link: ./community/plant
  title: How to add markup to Plant resources

bioschemas:
  "@context": https://schema.org/
  "@type": LearningResource
  "http://purl.org/dc/terms/conformsTo":
  - "@type": CreativeWork
    "@id": "https://bioschemas.org/profiles/TrainingMaterial/0.9-DRAFT-2020_12_08/"
  about:
    - "@id": https://schema.org
    - "@id": http://edamontology.org/topic_0089
  audience:
  - "@type": Audience
    name: (Markup provider, Markup consumer) People interested in adding Bioschemas markup to their own IDP resource
  name: "How to add markup to IDP resources"
  author:
  - "@type": Person
    name: "Ivan Mi&ccaron;eti&cacute;"
    "@id": https://bioschemas.org/people/IvanMicetic
    url: https://bioschemas.org/people/IvanMicetic
  dateModified: 2022-01-25
  description: "In this how-to, we will guide you through the necessary steps in order to get a JSON-LD markup describing your own IDP resource using a Bioschemas profile"
  keywords: "schemaorg, markup, structured data, bioschemas, ELIXIR IDP Community"
  license: CC-BY 4.0
  version: 1.0
---

## 1. Overview

This tutorial shows how to implement Bioschemas markup to a community resource. It describes Bioschemas profiles needed for a successful markup, their format and deployment on web pages. Adding a sitemap to a web site as well as registering persistent identifiers to resource data records completes the markup of a resource. These actions will ensure successful consumption of Bioschemas markup aiding resource data findability and interoperability.

## 2. Bioschemas profiles for IDP resources

Main IDP resources are primary or aggregating databases describing aspects of intrinsically disordered proteins. As such, they are marked up with Bioschemas as a typical database using three profiles:
* `DataCatalog`: describes the site providing the data
* `Dataset`: describes the data releases from the site
* `Protein`: a profile describing data records, usually `Protein` in the IDP community; these can be supplemented with `SequenceAnnotation` and `SequenceRange` to denote annotations on the protein sequence

Every resource is described with a `DataCatalog` profile. That profile specifies the provider of the resource, it’s version, license, keywords, description, format and so on. The `DataCatalog` profile contains one or more `Dataset` profiles which have their own version, license, keywords and description. The difference between `DataCatalog` and `Datasets` can be explained with the [UniProt](https://www.uniprot.org/) resource as an example. UniProt is the `DataCatalog` that contains Swiss-Prot and TrEMBL `Dataset`s.

## 3. Format and placement of Bioschemas profiles

Because Bioschemas is an extension of schema.org, it uses the same formats for embedding web pages: Microdata, RDFa and JSON-LD. Bioschemas community recommends JSON-LD format for embedding the markup. All implementations of Bioschemas in IDP resources also use the markup in JSON-LD format.

The three profiles must not be published on all web pages of a resource. Database resources should have `DataCatalog` and `Dataset`(s) markup on their home pages while entry pages (pages holding data records) should have only `Protein` records. All other pages (About, Help and others) should be void of markup. This implies that a mechanism must be in place that adds and removes dynamically schema profiles from web pages, especially in single page applications. Our suggestion is to place the markup as JSON-LD script in the document head with an id attribute (one for `DataCatalog` and `Dataset` schema and one for data record schema). In that way it will be relatively simple to toggle the visibility of the whole element containing the markup depending on the page that is being requested.

## 4. Example profiles for IDP resources

### `DataCatalog`

{% highlight json linenos %}
{
  "@context": "https://schema.org/",
  "@type": "DataCatalog",
  "@id": "https://disprot.org/#DataCatalog",
  "http://purl.org/dc/terms/conformsTo": {
    "@type": "CreativeWork",
    "@id": "https://bioschemas.org/profiles/DataCatalog/0.3-RELEASE-2019_07_01"
  },
  "sameAs": "https://registry.identifiers.org/registry/disprot",
  "url": "https://disprot.org/",
  "identifier": "https://registry.identifiers.org/registry/disprot",
  "name": "DisProt, The database of intrinsically disordered proteins",
  "description": "DisProt is a database of…",
  "datePublished": "2019-09",
  "dateModified": "2021-08",
  "citation": {
    "@type": "ScholarlyArticle",
    "@id": "https://doi.org/10.1093/nar/gkz975",
    "name": "DisProt: intrinsic protein disorder annotation in 2020",
    "url": "https://doi.org/10.1093/nar/gkz975",
    "sameAs": [
      "https://academic.oup.com/nar/advance-article/doi/10.1093/nar/gkz975/5622715",
      "https://pubmed.ncbi.nlm.nih.gov/31713636/"
    ]
  },
  "keywords": [
    "IDP",
    "IDPs",
    … 
  ],
  "sourceOrganization": [
    {
      "@type": "Organization",
      "@id": "https://biocomputingup.it/#Organization",
      "http://purl.org/dc/terms/conformsTo": {
        "@id": "https://bioschemas.org/profiles/Organization/0.2-DRAFT-2019_07_19",
        "@type": "CreativeWork"
      },
      "description": "University of Padua, Department of …",
      "name": "BioComputing UP, Department of …",
      "legalName": "University of Padua",
      "sameAs": "https://biocomputingup.it"
    }
  ],
  "provider": [
    {
      "@type": "Person",
      "givenName": "Silvio",
      "familyName": "Tosatto",
      "identifier": "https://orcid.org/0000-0003-4525-7793",
      "name": "Silvio Tosatto",
      "email": "user@domain.org",
      "url": "https://biocomputingup.it/people/silvio"
    }
  ],
  "encodingFormat": [
    "text/html",
    "application/json"
  ],
  "license": {
    "@type": "CreativeWork",
    "@id": "https://creativecommons.org/licenses/by/4.0/",
    "name": "Creative Commons CC4 Attribution",
    "url": "https://creativecommons.org/licenses/by/4.0/"
  },
  "dataset": {
    "@type": "Dataset",
    …
  }
}
{% endhighlight %}
### `Dataset`

{% highlight json linenos %}
{
  "@type": "Dataset",
  "@id": "https://disprot.org/#2021-08",
  "http://purl.org/dc/terms/conformsTo": {
    "@id": "https://bioschemas.org/profiles/Dataset/0.3-RELEASE-2019_06_14",
    "@type": "CreativeWork"
  },
  "includedInDataCatalog": {
    "@id": "https://disprot.org/#DataCatalog"
  },
  "url": "https://disprot.org/",
  "dateModified": "2021-08",
  "version": "8.3",
  "name": "DisProt",
  "description": "DisProt is …",
  "identifier": "https://disprot.org/#2020-12",
  "keywords": [
    "IDP",
    "IDPs",
    …
  ],
  "creator": {
    "@id": "https://biocomputingup.it/#Organization"
  },
  "license": {
    "@type": "CreativeWork",
    "@id": "https://creativecommons.org/licenses/by/4.0/",
    "name": "Creative Commons CC4 Attribution",
    "url": "https://creativecommons.org/licenses/by/4.0/"
  }
}
{% endhighlight %}

The whole `Dataset` profile can be included in the `DataCatalog` JSON object under the dataset key (`DataCatalog` lines 66-69).

### Data record profile: `Protein`

In case of data records describing a single protein entity, a Bioschemas Protein 0.11 profile can be used:
{% highlight json linenos %}
{
  "@context": "https://schema.org",
  "includedInDataset": "https://disprot.org/#2021-08",
  "@type": "Protein",
  "@id": "https://disprot.org/DP00003",
  "http://purl.org/dc/terms/conformsTo": {
    "@id": "https://bioschemas.org/profiles/Protein/0.11-RELEASE",
    "@type": "CreativeWork"
  },
  "identifier": "https://identifiers.org/disprot:DP00003",
  "sameAs": "http://purl.uniprot.org/uniprot/P03265",
  "name": "DNA-binding protein",
  "taxonomicRange": {
    "@type": "DefinedTerm",
    "termCode": "28285",
    "url": "http://purl.bioontology.org/ontology/NCBITAXON/28285",
    "sameAs": [
      "http://purl.uniprot.org/taxonomy/28285",
      "https://identifiers.org/taxonomy:28285",
      "http://purl.obolibrary.org/obo/NCBITaxon_28285"
    ],
    "inDefinedTermSet": {
      "@type": "DefinedTermSet",
      "name": "NCBI taxon",
      "url": "https://bioportal.bioontology.org/ontologies/NCBITAXON"
    }
  },
  "hasBioPolymerSequence": "MASREEEQRET…",
  "hasSequenceAnnotation": [
    {
      "@type": "SequenceAnnotation",
      "@id": "https://disprot.org/DP00003#disorder-content",
      "http://purl.org/dc/terms/conformsTo": {
        "@id": "https://bioschemas.org/profiles/SequenceAnnotation/0.7-DRAFT",
        "@type": "CreativeWork"
      }
      "sequenceLocation": {
        "@type": "SequenceRange",
        "rangeStart": 1,
        "rangeEnd": 529
      },
      "additionalProperty": {
        "@type": "PropertyValue",
        "name": "Protein disorder content",
        "propertyID": {
          "@id": "https://disprot.org/assets/data/IDPO_v0.2.owl#IDPO:00499"
        },
        "value": 0.09829867674858223
      }
    },
    {
      "@type": "SequenceAnnotation",
      "@id": "https://disprot.org/DP00003r002",
      "http://purl.org/dc/terms/conformsTo": {
        "@id": "https://bioschemas.org/profiles/SequenceAnnotation/0.7-DRAFT",
        "@type": "CreativeWork"
      }
      "sequenceLocation": {
        "@type": "SequenceRange",
        "rangeStart": 294,
        "rangeEnd": 334
      },
      "additionalProperty": [
        {
          "@type": "PropertyValue",
          "name": "Term",
          "value": {
            "@type": "DefinedTerm",
            "@id": "https://disprot.org/assets/data/IDPO_v0.2.owl#IDPO:00076",
            "inDefinedTermSet": {
              "@type": "DefinedTermSet",
              "@id": "https://disprot.org/assets/data/IDPO_v0.2.owl",
              "name": "IDP ontology"
            },
            "termCode": "IDPO:00076",
            "name": "disorder"
          }
        }
      ],
      "subjectOf": {
        "@type": "ScholarlyArticle",
        "@id": "https://identifiers.org/pubmed:8632448"
      }
    }
  ]
}
{% endhighlight %}

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

## 5. Web resource site map

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

## 6. Persistent identifiers for data records

Bioschemas promotes the use of persistent identifiers for data records in life sciences. Web resources such as databases (registries, repositories) are encouraged to register a unique URI to all data records within the resource. The registration can be done by requesting a namespace in [Identifiers.org](https://identifiers.org/). A namespace uniquely identifies the data collection while a namespace suffix identifies the data record within the collection. The whole Identifiers.org URI is used throughout Bioschemas markup whenever possible (e.g. line 10 and 19 in the data record profile example).
