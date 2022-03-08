---
title: How to add markup to IDP resources
overviewTutorial:
  link: ./community/
  title: Return to community tutorials overview


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

<div class="col d-flex align-items-start rounded p-4 mb-4 mt-3 shadow">
  <img class="align-self-center me-3" src="{{ '/tutorials/images/information_mark.png' | relative_url }}" alt="information">
  <div>
      More information about the <a href="https://elixir-europe.org/communities/intrinsically-disordered-proteins" target="_blank">ELIXIR IDP community</a>
  </div>
</div> 

## 1. Overview

This tutorial will introduce you to the necessary steps for a successful implementation of Bioschemas markup to an Intrinsically Disordered Protein (IDP) Community resource, providing a detailed description of Bioschemas profiles, their format and deployment on web pages. Adding a sitemap to a web site as well as registering persistent identifiers to resource data records complete the markup of a resource.

Following the instructions below you will learn how to implement Bioschemas markup, aiding resource data findability and interoperability.

IDP resources with Bioschemas markup will benefit from being included in the [IDPcentral registry](https://idpcentral.org/registry) which will act as a domain search engine covering all community resources.

## 2. Bioschemas profiles for IDP resources

Main IDP resources are primary or aggregating databases describing aspects of IDPs. As such, they are marked up with Bioschemas as a typical database using three profiles:
* `DataCatalog`, a profile informing on the site providing the data
* `Dataset`, a profile describing the data releases from the site
* `Protein`, a profile describing data records, which can be supplemented among others with:
    * `SequenceAnnotation` and `SequenceRange` to denote annotations on the protein sequence
    * `ScholarlyArticle` to denote publications describing protein annotations

Every resource is primarily described with a `DataCatalog` profile, specifying the provider of the resource, its version, license, keywords, description, format and so on.
In the `DataCatalogue` profile you will find one or more `Dataset` profiles with their own version, license, keywords and description.

For example, in the resource [UniProt](https://www.uniprot.org/), the `DataCatalog` is the UniProt knowledgebase, while the `Dataset`s are Swiss-Prot and TrEMBL.

## 3. Format and placement of Bioschemas profiles

### Format

Bioschemas is an extension of schema.org, therefore it uses the same formats for embedding web pages: Microdata, RDFa and JSON-LD. The Bioschemas community mainly uses the JSON-LD markup format, thus you are also recommended to use this format.

### Placement

When placing profiles in your resource, you must remember the following best practice:
* `DataCatalog` and `Dataset`(s) profiles must be included on the resource home page exclusively
* `Protein` profile must be included on entry pages, i.e. pages holding data records, only
* all other pages (About, Help and others) should be void of markup.

While developing your resource, find a way to add and remove profiles from individual web pages, especially in single page applications. Within a page, you should place the markup as JSON-LD script in the document head with an id attribute (one for `DataCatalog` and `Dataset` schema and one for data record schema). By including id attributes, it will be relatively simple for you to toggle the visibility of the element containing the markup depending on the web page.

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

You can include the whole `Dataset` profile in the `DataCatalog` JSON object under the dataset key (`DataCatalog` lines 66-69).

A deployed `DataCatalog` and `Dataset` markup can be seen in [MobiDB](https://mobidb.org/), [DisProt](https://disprot.org/) and [PED](https://proteinensemble.org/)
resource landing pages.

### Data record profile: `Protein`

When data records describe a single protein entity, you can use a Bioschemas Protein 0.11 profile, as in the following example:
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

Note the presence of two `SequenceAnnotation` profiles.
* the first one (lines 30-50) shows how to annotate a protein region (in this case the whole protein) to an ontology term which has a numerical value
* the second one (lines 51-84) shows how to apply an ontology term to a part of a protein (defined by `SequenceRange`).

All data records (like the `Protein` record) must link back to one `dataset` profile with the use of `includedInDataset` property as shown in line 3. This will ensure the correct assignment of data records to one or more datasets.

When data records describe protein complexes, ensembles or other biochemical entities, you can use a list of multiple `Protein` profiles as in the following example:
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
You are encouraged to credit a publication for all protein annotations described in data records by using a `ScholarlyArticle` schema.org type. An example can be seen in `Protein` profile, lines 80-83.

## 5. Web resource site map

For each of your resources, you are required to generate a **sitemap file**, a site map of your web resource listing all the pages accessible to crawlers, validators, or scrapers. This file will enable them to crawl your resource efficiently.

To create your sitemap file, place a file named `sitemap.xml` at the root of the domain. A simple XML sitemap example looks like this:

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

Sitemaps are limited to 50,000 URLs. If your resource has a higher number of web pages or data records, you should use a sitemap index file, which can include 50,000 individual sitemap. A sitemap index file example looks like this:

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

Bioschemas promotes the use of persistent identifiers for data records in life sciences. You are encouraged to register a unique URI to all data records within your resources.
You can register your persistent identifiers by requesting a namespace in [Identifiers.org](https://identifiers.org/).

Each persistent identifier has
* a namespace which uniquely identifies the data collection
* a namespace suffix, identifying the data record within the collection.

Persistent identifiers are used throughout Bioschemas markup whenever possible (e.g. line 10 and 19 in the data record profile example).