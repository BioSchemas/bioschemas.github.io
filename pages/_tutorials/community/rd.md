---
title: Marking up clinical entities in the Rare Diseases community
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
  name: "Adding Bioschemas to the Orphanet website"
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
  - "@type": Person
    name: "Alasdair Gray"
    "@id": https://bioschemas.org/people/AlasdairGray
    url: https://bioschemas.org/people/AlasdairGray
  dateCreated: 2021-12-22
  dateModified: 2022-02-11
  description: "This tutorial will show you how Orphanet rare disease pages were annotated with Bioschemas."
  keywords: "Disease, Rare Disease, Schema.org, JSON-LD, Bioschemas"
  license: CC-BY 4.0
  version: 1.4
---

## 1. Overview

This tutorial shows how Bioschemas markup was implemented in a Rare Diseases community resource. It describes which Bioschemas types and properties were used to provide metadata about rare diseases as clinical entities in several languages in order to improve medical nomenclature interoperability.  The resulting markup is machine processable enabling others to consume and exploit the data.

The main objective of the Bioschemas implementation was to leverage the Findability of the disease information and the interoperability between different Rare Diseases resources.

## 2. Context

[Orphanet website](https://www.orpha.net) is a well known resource for the Rare Diseases community. It provides information about Rare Diseases (more than 6,000 rare disorder entities, plus groups of diseases and subtypes). It also provides a directory of several resources (expert centers, support groups, research projects, clinical trials, diagnostic tests, and registries & biobanks) relevant for rare diseases in more than 40 countries. The website is available in 9 languages (and further extensions are ongoing). It’s heavily used with around 3 million page views each month.

During the [2019 ELIXIR BioHackathon](https://2019.biohackathon-europe.org/), we drafted the implementation of Bioschemas markup within Orphanet and Orphadata. This resulted in a new Bioschemas profile for capturing clinical entities as a [Disease](https://bioschemas.org/profiles/Disease/). We have embedded the markup in over ten thousand clinical entity pages, in 9 languages. The properties include: name, synonyms, identifiers (ORPHAcode), description, prevalence and mappings to common nomenclatures (e.g. ICD10, OMIM, UMLS, MeSH, GARD, MedDRA).

## Rare disease clinical entities markup

The Orphanet website includes pages for rare disease clinical entities. Each page includes data from the Orphanet nomenclature, which has a unique OrphaCode as its identifier. In this tutorial we will be looking at [orpha:91](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=91), the Orphanet page about 'Aromatase deficiency'.

Each page provides information about a disease including its preferred label and known synonyms, a definition of the concept, epidemiological information, mappings to other terminologies, inheritance mode, age of onset, and often structured textual information.

- `"@type": "MedicalCondition"`:
  A clinical entity on Orpahnet corresponds to the Bioschemas [Disease profile](https://bioschemas.org/profiles/Disease/) which is defined over the Schema.org [MedicalCondition](https://schema.org/MedicalCondition) type.

- `"@id"` & `"identifier"`:
  For the JSON-LD `@id` value, the permanent URL of each page is used to identify the concept within the Orphanet website. This will increase the findability of the resource. The OrphaCode is declared using the [schema:identifier](https://schema.org/identifier) property.  
  In the next iteration, we plan to use [schema:sameAs](https://schema.org/sameAs)to link with ORDO concepts.

- `"name"`,  `"@type": "PronounceableText", "inLanguage":, "textValue"`:
  As the website displays the information in the language chosen by the user, we had declare the language used within the page rendering. Each instance of the `name` property was declared with it language tag as per the following snippet
  {% highlight json linenos %}
    'name': {
      '@type': 'PronounceableText',
      'inLanguage': 'en',
      'textValue': 'Aromatase deficiency'
    }
  {% endhighlight %}

- `"alternateName"`:
  The property [“schema:alternateName”](https://schema.org/alternateName) is used for the list of synonyms (which differ in different languages). Several synonyms could be used, therefore the value set is an array.

- `"epidemiology"`:
  As the concept of “prevalence” is not defined in Schema.org we decided to use [schema:epidemiology](https://schema.org/epidemiology) which is applicable to the MedicalCondition type. We note that the “epidemiology” definition in Schema.org is not as accurate as a “prevalence” concept.

- `"description"`:
  The [schema:description](https://schema.org/description) property was used to give the definition of the concept. We have decided to limit the textual information available on the website page only to the definition section, which could be easily reusable on other resources. (In the ELIXIR Core Data Resource Orphadata, provided by Orphanet, definitions are part of the open data freely accessible in CC-BY 4.0. Full text are available only under data transfer agreements.

- `"code", codeValue, codingSystem`:
  The mapping to other terminologies is an important asset of the Orphanet nomenclature which leverages the interoperability between sources.

  We decide not to use the [schema:sameAs](https://schema.org/sameAs) property, mostly because often mappings are not an exact match between terminologies. Also mappings could be 1 to many (from 1 Orphanet clinical entity to several in the considered terminology).

  For the list of [schema:code](https://schema.org/code) we used [schema:MedicalCode](https://schema.org/MedicalCode) which is the most appropriate and [schema:codeValue](https://schema.org/codeValue) and [schema:codingSystem](https://schema.org/codingSystem) properties for each mapping.

### Complete Example as JSON-LD
To ease the process of embedding the markup within each disease page on the Orphanet website, the framework that generates the HTML page content was extended to add the markup within a JSON-LD script tag.
As an example here is the JSON-LD for the [Aromatase deficiency page](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=91).

{% highlight json linenos %}
<script type="application/ld+json">
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
</script>
{% endhighlight %}

## Conclusion

In this tutorial we have shown how a web page containing information about a disease can include Bioschemas markup to capture the main features of the disease that may be used for search.
