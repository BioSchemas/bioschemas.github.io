---
layout: default
title: Schema.org, what and why?
---

# Schema.org, what and why?

***
&#9664; Previous tutorial: [Getting started](./index) | Next tutorial: [Markup examples](markup_examples) &#9654; 

***

## What is schema.org?
[Schema.org](https://schema.org/) is a collaborative, community activity with a mission to create, maintain, and promote schemas for structured data on the Internet, on web pages, in email messages, and beyond.
Structured data can be used to mark up all kinds of items from products to events to recipes.

Most sites and organizations will not have a reason to extend schema.org. However, schema.org offers the ability to specify additional properties or sub-types to existing types.

"Schema.org" vocabulary can be used with many different encodings, including RDFa, Microdata and JSON-LD. These vocabularies cover entities, relationships between entities and actions, and can easily be extended through a well-documented extension model. Over 10 million sites use Schema.org to markup their web pages and email messages. Many applications from Google, Microsoft, Pinterest, Yandex and others already use these vocabularies to power rich, extensible experiences.

## Why to use schema.org?

As with any site nowadays; you’re competing in a crowded market-place. Ranking higher on search result pages or being included in 3rd party registries that receive more web-traffic can raise the exposure of your work to be seen by larger audiences. This is all achievable by following best practices and applying schema.org to your site.

* Communicate with all the search engine
* Enhance findability from search engine results
* Provide context to an ambigous webpage
* Metadata Interoperability and Standardization across all website using schema.org

## Schema.org formats

You can use the schema.org vocabulary along with Microdata, RDFa, or JSON-LD format to add markup to your web pages.

You can use the schema.org vocabulary along with [Microdata](http://en.wikipedia.org/wiki/Microdata_(HTML)), [RDFa](http://en.wikipedia.org/wiki/RDFa), or [JSON-LD](http://en.wikipedia.org/wiki/JSON-LD) format to add markup to your web pages. In Bioschemas we favor the use of JSON-LD.

### Format examples

* JSON-LD

```json
    <script type="application/ld+json">
    {
      "@context": "http://schema.org",
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
```

***
&#9664; Previous tutorial: [Getting started](./index) | Next tutorial: [Markup examples](markup_examples) &#9654; 

***