---
title: Marking up Rare diseases clinical entities
overviewTutorial:
  link: ./community_tutorials.html
  title: Return to community tutorials overview

  bioschemas:
    "@context": https://schema.org/
    "@type": LearningResource
    "http://purl.org/dc/terms/conformsTo":
    - "@type": CreativeWork
      "@id": "https://bioschemas.org/profiles/TrainingMaterial/0.9-DRAFT-2020_12_08/"
    about:
    - "@id": https://www.orpha.net
    audience:
    - "@type": Audience
      name: (Markup provider, Markup consumer) WebMaster
    name: "Bioschemas deploiement in the context of RD, based on Orphanet website"
    author:
    - "@type": Person
      name: "Marc Hanauer"
      "@id": https://orcid.org/0000-0002-6758-2506
      url: https://orcid.org/0000-0002-6758-2506
    contributor:
    - "@type": Person
      name: "Celine Rousselot"
      "@id": http://www.orphanet-france.fr/national/FR-FR/index/equipe/
      url: http://www.orphanet-france.fr/national/FR-FR/index/equipe/
    dateModified: 2021-12-22
    description: "This tutorial will show you how Orphanet rare diseases pages were annotated with Bioschemas."
    keywords: "schema, JSON-LD, bioschemas"
    license: CC-BY 4.0
    version: 1.3
---

## 1. Overview

This tutorial shows how Bioschemas markup was implemented in a community resource dedicated to Rare Diseases. It describes which Bioschemas type and properties were used in order to provide  comprehensive metadata about rare diseases as clinical entities, in several languages, to improve medical nomenclature interoperability.  These implementations will help successful consumption of Bioschemas markup aiding resource data findability and interoperability in the Rare disease field (RD).

## 2. Context

The [Orphanet website](https://www.orpha.net)  is a well known resource for the RD community for years. It provides information about Rare diseases (more than 6000 rare disorders entities, plus groups of diseases and subtypes). It also provides a directory of several resources (Experts centers, support groups, research projects, clinical trials, diagnostic tests, registries & biobanks) relevant for rare diseases in more than 40 countries. The website is available in 9 languages (and further extensions are ongoing). It’s heavily used (around 3 millions view pages by month).

We have started to draft the bioschemas implementation during the 2019 Elixir Biohackathon (Implementation of Bioschema for Orphanet and Orphadata) and made a first proposal for any clinical entity described in the Orphanet’s Knowledge base and displayed in the Orphanet’s website. We have described so far 10542 Clinical entities pages, in 9 languages, making 94878 pages with available information with markups including (when relevant): name, synonyms, identifiers (ORPHAcode), description, prevalence and nomenclatures mappings (ICD10, OMIM, UMLS, MeSH, GARD, MedDRA).

## Rare disease clinical entities markup

As described in specific Orphanet’s website pages a rare disease clinical entity is part of the Orphanet nomenclature and therefore has a unique identifier (OrphaCode):
https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=91
This will serve as an example of bioschemas implementation here.

The Orphanet Knowledge base provides information when available such as a label and synonyms, a definition of the concept, epidemiological information, mappings to other terminologies, inheritance mode, age of onset  and often structured textual information.

The main objective of the Bioschemas implementation was to leverage the findability of the disease information and the interoperability between different RD resources.

`"@type": "MedicalCondition"`:
Therefore, based on the [Disease profile](https://bioschemas.org/profiles/Disease/) we processed the information accordingly, using the MedicalCondition type.


`"@id"` & `"identifier"`:
As “unique id @id” we decided to use the permanent link to the concept in Orphanet website. (Instead, the IRI from the Orphanet Rare Diseases Ontology could be used, but in this particular concept we aim to improve the findability at the website level). Nevertheless, in the next version of the implementation we will probably set a “sameAs” (https://schema.org/sameAs) property to link directly to ORDO concepts.

The “identifier” is the OrphaCode of each specific RD clinical entity described on the page.

`"name"`,  `"@type": "PronounceableText", "inLanguage":, "textValue"`:
As the website framework will display the information in the language chosen by users, we had to describe the type of language used for each “name”. Therefore we used the `"@type": "PronounceableText" and "inLanguage"` to give language ISO 2 digit format and `"textValue"` as label instantiation.

`"alternateName"`:
We used [“alternateName”](http://schema.org/alternateName) for the list of synonyms (which differ in different languages). Several synonyms could be used, therefore the value set is an array.

`"epidemiology"`:
As the concept of “prevalence” is not defined in schema.org we decided to use “https://schema.org/epidemiology” which is applicable to “MedicalCondition”. Nevertheless the “epidemiology” definition in schema.org is not as accurate as a “prevalence” concept.

`"description"`:
The http://schema.org/description was used to give the definition of the concept. We have decided to limit the textual information available on the website page only to the definition section, which could be easily reusable on other resources. (In the Elixir Core resource Orphadata, provided by orphanet, definitions are part of the open data freely accessible in CCBY 4.0. Full text are available only under DTA - data transfer agreement- )

`"code", codeValue, codingSystem`:
The mapping to other terminologies is an important asset of the Orphanet nomenclature which leverages the interoperability between sources.

We decide not to use the “sameAs” property, mostly because often mappings are not “Exact match” (but BTNT NTBT) between terminologies. Also mappings could be 1 to many (from 1 Orphanet clinical entity to several in the considered terminology).
For the list of “code” we used https://schema.org/MedicalCode which is the most appropriate and “codeValue” and “codingSystem” properties for each mapping.

### JSON-LD
To ease the process of integration within the Orphanet website framework, we aim to implement directly in all disease page a JSON-LD script section returned in the HTML source constructed by the framework (`<script type="application/ld+json"> </script>`).
As example here is the code for the [Aromatase deficiency page](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=91).

{% highlight json linenos %}
{
  "@context": "http://schema.org/",
  "@type": "MedicalCondition",
  "@id": "http://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=91",
  "identifier": "91",
  "name": {
    "@type": "PronounceableText",
    "inLanguage": "EN",
    "textValue": "Aromatase deficiency"
  },
  "alternateName": [
    "Congenital estrogen deficiency"
  ],
  "epidemiology": "Prevalence : <1 / 1 000 000",
  "code": [
    {
      "@type": "MedicalCode",
      "codeValue": "ORPHA:91",
      "codingSystem": "ORPHAcode"
    },
    {
      "@type": "MedicalCode",
      "codeValue": "E25.8",
      "codingSystem": "ICD-10"
    },
    {
      "@type": "MedicalCode",
      "codeValue": "613546",
      "codingSystem": "OMIM"
    },
    {
      "@type": "MedicalCode",
      "codeValue": "C0853662",
      "codingSystem": "UMLS"
    },
    {
      "@type": "MedicalCode",
      "codeValue": "C0878680",
      "codingSystem": "UMLS"
    },
    {
      "@type": "MedicalCode",
      "codeValue": "C1960539",
      "codingSystem": "UMLS"
    },
    {
      "@type": "MedicalCode",
      "codeValue": "C537436",
      "codingSystem": "MeSH"
    },
    {
      "@type": "MedicalCode",
      "codeValue": "365",
      "codingSystem": "GARD"
    }
  ],
  "description": "A rare disorder that disrupts the synthesis of estradiol, resulting in hirsutism of mothers during gestation of an affected child; pseudohermaphroditism and virilization in women; and tall stature, osteoporosis and obesity in men."
}
{% endhighlight %}
