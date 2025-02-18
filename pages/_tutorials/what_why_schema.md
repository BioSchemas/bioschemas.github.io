---
title: 'Introduction to Schema.org: What and Why?'
previousTutorial:
  link: ./
  title: Overview of Bioschemas Tutorials
nextTutorial:
  link: ./markup_examples
  title: Schema.org markup examples

bioschemas:
  "@context": https://schema.org/
  "@type": LearningResource
  "http://purl.org/dc/terms/conformsTo":
  - "@type": CreativeWork
    "@id": "https://bioschemas.org/profiles/TrainingMaterial/1.0-RELEASE"
  about:
    - "@id": https://schema.org
    - "@id": http://edamontology.org/topic_0089
  audience:
  - "@type": Audience
    name: (General interest) People interested in introductory information to Schema.org
  name: "Introduction to Schema.org, what and why?"
  author:
  - "@type": Person
    name: "Ricardo Arcila"
    "@id": https://bioschemas.org/people/RicardoArcila
    url: https://bioschemas.org/people/RicardoArcila
  contributor:
  - "@type": Person
    name: "Leyla Garcia"
    "@id": https://bioschemas.org/people/LeylaGarcia
    url: https://bioschemas.org/people/LeylaGarcia
  - "@type": Person
    name: "Victoria Dominguez del Angel"
    "@id": https://bioschemas.org/people/VictoriaDominguezDelAngel
    url: https://bioschemas.org/people/VictoriaDominguezDelAngel/
  - "@type": Person
    name: "Alasdair Gray"
    "@id": https://bioschemas.org/people/AlasdairGray
    "url": https://bioschemas.org/people/AlasdairGray
  dateModified: 2021-04-23
  description: "In this tutorial you will get an idea on what Schema.org is and how it is useful"
  keywords: "schemaorg, markup, structured data"
  license: CC-BY 4.0
  version: 2.1
---

## 1. What is Schema.org?
[Schema.org](https://schema.org/) is a collaborative, community activity with a mission to create, maintain, and promote schemas for structured data on the Internet, on web pages, in email messages, and beyond.
Structured data can be used to mark up all kinds of items from products to events to recipes.

Most sites and organizations will not have a reason to extend Schema.org. However, Schema.org offers the ability to specify additional properties or sub-types to existing types.

The Schema.org vocabulary can be used with many different encodings, including RDFa, Microdata and JSON-LD. These vocabularies cover entities, relationships between entities and actions, and can easily be extended through a well-documented extension model. Over 10 million sites use Schema.org to markup their web pages and email messages. Many applications from Google, Microsoft, Pinterest, Yandex and others already use these vocabularies to power rich, extensible experiences.

## 2. Why use Schema.org?

As with any site nowadays; you’re competing in a crowded market-place. Ranking higher on search result pages or being included in 3rd party registries that receive more web-traffic can raise the exposure of your work to be seen by larger audiences. This is all achievable by following best practices and applying Schema.org to your site.

* Communicate with all the search engines
* Enhance findability from search engine results
* Provide context to an ambigous webpage
* Metadata Interoperability and Standardization across all website using Schema.org

## 3. Schema.org Formats

Schema.org markup can be embedded in your web page using [Microdata](http://en.wikipedia.org/wiki/Microdata_(HTML)), [RDFa](http://en.wikipedia.org/wiki/RDFa), or [JSON-LD](http://en.wikipedia.org/wiki/JSON-LD). In Bioschemas we favor the use of JSON-LD, as do most of the search engines.

### 3.1. Format examples

* JSON-LD

```json
<script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "SportsTeam",
    "name": "San Francisco 49ers",
    "member": {
      "@type": "OrganizationRole",
      "member": {
        "@type": "Person",
        "name": "Joe Montana"
      },
      "startDate": "1979",
      "endDate": "1992",
      "roleName": "Quarterback"
    }
  }
</script>
```

* Microdata

```html
<div itemscope itemtype="http://schema.org/SportsTeam">
  <span itemprop="name">San Francisco 49ers</span>
  <div itemprop="member" itemscope
       itemtype="http://schema.org/OrganizationRole">
    <div itemprop="member" itemscope
         itemtype="http://schema.org/Person">
      <span itemprop="name">Joe Montana</span>
    </div>
    <span itemprop="startDate">1979</span>
    <span itemprop="endDate">1992</span>
    <span itemprop="roleName">Quarterback</span>
  </div>
</div>
```

* RDFa

```html
<div vocab="http://schema.org/" typeof="SportsTeam">
  <span property="name">San Francisco 49ers</span>
  <div property="member" typeof="OrganizationRole">
    <div property="member" typeof="http://schema.org/Person">
      <span property="name">Joe Montana</span>
    </div>
    <span property="startDate">1979</span>
    <span property="endDate">1992</span>
    <span property="roleName">Quarterback</span>
  </div>
</div>
```
