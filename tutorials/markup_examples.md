---
layout: tutorial
title: Schema.org markup examples
previousTutorial:
  link: ./what_why_schema
  title: What and why schema.org
nextTutorial:
  link: ./what_why_bioschemas
  title: What and why Bioschemas

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
    name: People interested in Schema.org markup examples
  name: "Schema.org markup examples"
  author:
  - "@type": Person
    name: "Azerty Proxy"
  contributor:
  - "@type": Person
    name: "Leyla Garcia"
    "@id": https://bioschemas.org/people/LeylaGarcia
    url: https://bioschemas.org/people/LeylaGarcia
  dateModified: 2021-02-17
  description: "With these examples you will get a better understanding of benefits brought by structure data, i.e., schema.org markup"
  keywords: "schemaorg, markup, structured data, example"
  license: CC-BY 4.0
  version: 2.0
---

## 1. Google cupcake microdata

By performing a simple search of cupcake recipes on Google, see Figure 1, we will have as a result a preview of the information shown on the website even before going to the actual website; information such as the recipe name, rating, cooking time, calories and a description.

{% include image.html file="/tutorials/images/google_search.png" caption="Figure 1: Cupcake recipe search in Google" alt="Cupcake recipe search in Google" %}

Displayed on the website you can find the same rating details shown on the Google card, see Figure 2.

{% include image.html file="/tutorials/images/google_detail.png" caption="Figure 2: Cupcake recipe card" alt="Cupcake recipe card" %}

And behind the scenes this metadata, used by Google on its search result cards, its marked schema.org, see Figure 3.

{% include image.html file="/tutorials/images/google_html.png" caption="Figure 3: Cupcake recipe HTML" alt="Cupcake recipe HTML" %}

The type used on the markup `itemprop="aggregateRating"` is referencing the property on https://schema.org/Recipe website, see Figure 4.

{% include image.html file="/tutorials/images/google_recipe.png" caption="Figure 4: Cupcake recipe HTML" alt="Cupcake recipe HTML" %}

## 2. DuckDuckGo cupcake jsonld

DuckDuckGo take advantage of schema.org in a similar way Google does, see a search on Figure 5.

{% include image.html file="/tutorials/images/duckduck_search.png" caption="Figure 5: Cupcake recipe search in DuckDuckGo" alt="Cupcake recipe search in DuckDuckGo" %}

The author of the recipe could be found on the search result card and the actual website as seen below, Figure 6.

{% include image.html file="/tutorials/images/duckduck_detail.png" caption="Figure 6: Cupcake recipe card in DuckDuckGo" alt="Cupcake recipe card in DuckDuckGo" %}

and behind the scenes, Figure 7, we will find the `json-ld` tag with the Recipe information

{% include image.html file="/tutorials/images/duckduck_html.png" caption="Figure 7: Cupcake recipe JSON-LD in DuckDuckGo" alt="Cupcake recipe JSON-LD in DuckDuckGo" %}

The author property, for instance, holds the name we are seeing displayed on DuckDuckGo result search cards, Figure 8.

{% include image.html file="/tutorials/images/duckduck_jsonld.png" caption="Figure 8: Author information" alt="Author information" %}

As expected from the documentation on schema.org, see Figure 9.

{% include image.html file="/tutorials/images/duckduck_author.png" caption="Figure 9: Author property in schema.org" alt="Author property in schema.org" %}
