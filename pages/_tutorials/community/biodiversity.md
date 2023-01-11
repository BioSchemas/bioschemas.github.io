---
title: How to markup biodiversity-related resources
overviewTutorial:
  link: ./community/
  title: Return to community tutorials overview

bioschemas:
  "@context": https://schema.org/
  "@type": LearningResource
  "http://purl.org/dc/terms/conformsTo":
  - "@type": CreativeWork
    "@id": "https://bioschemas.org/profiles/TrainingMaterial/1.0-RELEASE"
  about:
    - "@id": https://schema.org
  audience:
  - "@type": Audience
    name: (Markup provider, Markup consumer) People interested in adding Bioschemas markup to their own biodiversity-related resources
  name: "How to markup biodiversity-related resources"
  author:
  - "@type": Person
    name: "Franck Michel"
  dateModified: 2023-01-09
  keywords: "schemaorg, markup, structured data, bioschemas, biodiversity"
  license: CC-BY 4.0
  version: 1.0
---

<div class="col d-flex align-items-start rounded p-4 mb-4 mt-3 shadow">
  <img class="align-self-center me-3" src="{{ '/tutorials/images/exclamation_mark.png' | relative_url }}" alt="warning">
  <div>
      This tutorial complements the tutorials <a href="../howto/howto_right_profile">how to select the right profile for your resource</a> and <a href="../howto/howto_add_markup">how to mark up your own resource with Bioschemas</a>. Please check these tutorials first.

      Depending on your use case, you may also want to check this related tutorial: <a href="plant">How to add markup to Plant resources</a>.
  </div>
</div> 


## Overview

This How-To will guide you through the steps necessary to markup resources dealing with biodiversity in a broad sense, using Bioschemas' [Taxon](../../profiles/Taxon) and [TaxonName](../../profiles/TaxonName) profiles.

The resources may span a large spectrum of domains, ranging from academic biodiversity databases such as taxonommic registries, species check lists and scientific literature repositories, to private companies concerned with regulations and directives related to endangered species, to associations of citizens praticing birdwatching or sea fishing.

The main goal of marking up these resources is to improve their Findability on the Web, in accordance with the goals of Bioschemas themselves, while connecting them together thus helping to weave a broad biodiversity web.


## The Taxon and TaxonName profiles

These two profiles can be used together or separately depending on the use case.


### Taxon

A [taxon](https://en.wikipedia.org/wiki/Taxon) is a group of organisms with common characteristics, identified by taxonomists to form a certain unit. 
If your resources deal with groups of biological organisms like animals, plants, fungi or bacteria, then you may want to use the [**Taxon**](../../profiles/Taxon) profile. 
The least you would need to know to describe a Taxon is: 
- its full **[scientific name](https://en.wikipedia.org/wiki/Binomial_nomenclature)** including authorship and date (property `schema:name`), also called _accepted name_ in botanics or _valid name_ in zoology, 
- its **[taxonomimc rank](https://en.wikipedia.org/wiki/Taxonomic_rank)** (property `schema:taxonRank`) such as species, genus, family etc.

Additional names can be provided:
- **synonyms** of the accepted/valid scientific name (property `schema:alternateName`) keep track of the taxonomic changes and thus reflect the way biologists think of a given taxon, that is, its circumscription.
- **vernacular names** can also be provided using a property borrowed from Darwin Core terms: `dwc:vernacularName`

For instance, the taxon representing the Beluga species has a valid scientific name which is _Delphinapterus leucas (Pallas, 1776)_, a synonym name is _Balaena albicans Muller, 1776_ (note that typographic elements such as parentheses, comma, the use of uppercase vs. lowercase letters etc., are normalized by the [Codes of nomenclature](https://en.wikipedia.org/wiki/Nomenclature_codes)), and its rank is _species_.
This is illustrated by the simple example below:

{% highlight json %}
{
    "@context": [
        "http://schema.org",
        {   "dwc": "http://rs.tdwg.org/dwc/terms/",
            "dwc:vernacularName": { "@container": "@language" }
        }
    ],

    "@type" : "Taxon",
    "@id": "http://taxref.mnhn.fr/lod/taxon/60932",
    "mainEntityOfPage": "https://inpn.mnhn.fr/espece/cd_nom/60932?lg=en",
    "name": "Delphinapterus leucas (Pallas, 1776)",
    "alternateName": "Balaena albicans Muller, 1776",
    "dwc:vernacularName": { "@language": "en", "@value": "Beluga Whale" },
    "taxonRank": [ "http://www.wikidata.org/entity/Q7432", "species" ],
}
{% endhighlight %}

Other recommended or optional information can be added to the description. In particualr, it is recommended to link a Taxon to its **parent taxon** by means of the `schema:parentTaxon` property, and optionally to its **child taxa** with `schema:childTaxon`.
The `schema:isBasedOn` property can be used to refer to an article that described the taxon.

Furthermore, a good pratice is to link a Taxon to its counterparts in third-party taxonomic registers like the [NBCI taxonomy](https://www.ncbi.nlm.nih.gov/taxonomy), or data agregators like [GBIF](https://www.gbif.org/) or [Catalog of Life](https://www.catalogueoflife.org/), using the `schema:sameAs` property and/or `schema:identifier` property with a `schema:PropertyValue` as an object, such that people would know exactly what taxon you refer to.


### TaxonName

Some databases (e.g. [Zoobank](https://zoobank.org/), [IPNI](https://www.ipni.org/) and [Mycobank](https://www.mycobank.org/)) describe specifically _scientific names_ but do not keep track of how names are assigned to taxa, such that they would be poorly supported by the use of the Taxon profile. 
In such cases, the [**TaxonName**](../../profiles/TaxonName) profile is more relevant to markup the resources of these taxonomic names registries.

A TaxonName essentially consists of the scientific name (`schema:name`) without authorship nor date that are specified separately (`schema:author`).
It is also recommended that a TaxonName be assigned a [taxonomic rank](https://en.wikipedia.org/wiki/Taxonomic_rank) (property `schema:taxonRank`).

Similarly to the description of a Taxon, a good pratice is to link a TaxonName to its counterpart in third-party projects like [Zoobank](https://zoobank.org/) or [IPNI](https://www.ipni.org/) using the `schema:sameAs` property and/or `schema:identifier` property with a `schema:PropertyValue` object.

Furthermore, the TaxonName profile may be used jointly with the Taxon profile when one wants to describe a taxon while giving details about the scientific names. To do so, properties `schema:scientificName` and `schema:alternateScientificName` are the counterparts of `schema:name` and `schema:alternateName`, but they take a TaxonName object.

A simple example would look like this:

{% highlight json %}
{
    "@context": "http://schema.org",

    "@type" : "TaxonName",
    "name": "Delphinapterus leucas",
    "author": "(Pallas, 1776)",
    "taxonRank": [ "http://www.wikidata.org/entity/Q7432", "species" ],
}
{% endhighlight %}

Additional information could be provided, in particular the article that proposed the name (`schema:isBasedOn`).


## How to decide whether to use Taxon or TaxonName?

If you are unsure whether your resources deal with taxa or taxon names, just follow this simple rule:
- When your resources are primarily about biology in the broad sense, organisms, biological features, life traits, phenotypes etc., then most likely you should use the Taxon profile.
- When your resources relate to the publication and typification of scientific names, specifically when this pertains to the application of a Code of nomenclature, then you should use the TaxonName profile.


## How to denote taxonomic ranks?

In both Taxon and TaxonName profiles, a taxonomic rank is given with property `schema:taxonRank` that may take either a string or a URI.
A simple string would typically be "species, "genus" or family". This is easy to read but leaves room for multiple wordings with respect, for instance, to the case or the use of singluar or plural etc. 
By contrast, a URI from a controlled vocabulary is well defined but multiple choices exist and consumers of the markup data may not know about them all. Some candidates are Wikidata, TDWG TaxonRank ontology, NCBI taxonomy.

Therefore, a recommended practice is to provide at least one string and one URI to denote the rank, as illustrated below:

{% highlight json %}
    "taxonRank": [ "http://www.wikidata.org/entity/Q7432", "species" ],
{% endhighlight %}


## Cross-references to other databases

So that people understand exactly what taxon or taxon name your resource describes, it is a good practice to link the descriptions to their counterparts in third-party databases.

A simple way to do that is to link to a web page that describes the same entity with property `schema:sameAs`.
For instance, a Taxon could link to the GBIF page for taxon _Delphinapterus leucas (Pallas, 1776)_ in this way:

{% highlight json %}
    "@type" : "Taxon",
    "name": "Delphinapterus leucas (Pallas, 1776)",
    "sameAs": [ "https://www.gbif.org/species/5220003" ],
{% endhighlight %}

An even better option is to provide the identifier of the entity within other databases using property `schema:identifier` and an object of type `schema:PropertyValue` where `schema:propertyID` is the URI of a property and `schema:value` is the value of the identifier.
Continuing on the same example, the GBIF identifier could be provided this way:

{% highlight json %}
    "identifier": [
        {   "@type": "PropertyValue",
            "name": "GBIF id",
            "propertyID": "https://www.wikidata.org/entity/P846",
            "value": "5220003"
        }
    ]
{% endhighlight %}

The interest of this approach is that a consumer of the Taxon markup data could, later on, use this identifier to query GBIF's API and retrieve additional information.


## Examples

### Single TaxonName

{% highlight json %}
{
    "@context": "http://schema.org",
    "http://purl.org/dc/terms/conformsTo": {
        "@id": "https://bioschemas.org/profiles/TaxonName/0.1-DRAFT"
    },

    "@type" : "TaxonName",
    "name": "Delphinapterus",
    "author": "Lacépède, 1804",
    "taxonRank": [ "http://www.wikidata.org/entity/Q34740", "genus" ],
    "identifier": [
        {   "@type": "PropertyValue",
            "name": "Zoobank id",
            "propertyID": "https://www.wikidata.org/entity/P1746",
            "value": "urn:lsid:zoobank.org:act:D78127F0-143A-4B05-8124-5BA73C10B5F0"
        }
    ],
    "sameAs": [
        "https://zoobank.org/NomenclaturalActs/d78127f0-143a-4b05-8124-5ba73c10b5f0",
        "https://doi.org/10.1080/01639374.2012.682254"
    ],

    "isBasedOn": {
        "@type": "ScholarlyArticle",
        "@id": "https://doi.org/10.1080/01639374.2012.682254",
        "name": "Histoire naturelle des cétacées",
        "author": [ "Lacépède, Bernard Germain Étienne de" ],
        "datePublished": "1804"
    }
}
{% endhighlight %}


### Joint use of Taxon and TaxonName

{% highlight json %}
{
    "@context": [
        "http://schema.org",
        {   "dwc": "http://rs.tdwg.org/dwc/terms/",
            "dwc:vernacularName": { "@container": "@language" }
        }
    ],
    "http://purl.org/dc/terms/conformsTo": {
        "@id": "https://bioschemas.org/profiles/Taxon/0.7-DRAFT"
    },

    "@type" : "Taxon",
    "@id": "http://taxref.mnhn.fr/lod/taxon/60932",
    "additionalType": [ "dwc:Taxon", "http://rs.tdwg.org/ontology/voc/TaxonConcept#TaxonConcept" ],
    "identifier": [
        {   "@type": "PropertyValue",
            "name": "TAXREF id",
            "propertyID": "https://www.wikidata.org/entity/P3186",
            "value": "60932"
        },
        {   "@type": "PropertyValue",
            "name": "WoRMS id",
            "propertyID": "https://www.wikidata.org/entity/P850",
            "value": "137115"
        },
        {   "@type": "PropertyValue",
            "name": "GBIF id",
            "propertyID": "https://www.wikidata.org/entity/P846",
            "value": "5220003"
        }
    ],
    "mainEntityOfPage": "https://inpn.mnhn.fr/espece/cd_nom/60932?lg=en",
    
    "name": "Delphinapterus leucas (Pallas, 1776)",
    "scientificName": {
        "@type" : "TaxonName",
        "name": "Delphinapterus leucas",
        "author": "(Pallas, 1776)",
        "taxonRank": "species"
    },
    "alternateName": [ "Balaena albicans Muller, 1776", "Beluga catodon Gray, 1846" ],
    "alternateScientificName": [
        {   "@type" : "TaxonName",
            "name": "Balaena albicans",
            "author": "Muller, 1776",
            "taxonRank": "species"
        },
        {   "@type" : "TaxonName",
            "name": "Beluga catodon",
            "author": "Gray, 1846",
            "taxonRank": "species"
        }
    ],
    "dwc:vernacularName": [
        { "@language": "en", "@value": "Beluga Whale" },
        { "@language": "fr", "@value": "Bélouga" }
    ],

    "taxonRank": [
        "species",
        "http://rs.tdwg.org/ontology/voc/TaxonRank#Species",
        "http://www.wikidata.org/entity/Q7432"
    ],

    "parentTaxon": { 
        "@type": "Taxon",
        "name": "Delphinapterus Lacépède, 1804",
        "identifier": "191588",
        "mainEntityOfPage": "https://inpn.mnhn.fr/espece/cd_nom/191588?lg=en",
        "taxonRank" : [ 
            "genus",
            "http://rs.tdwg.org/ontology/voc/TaxonRank#Genus", 
            "http://www.wikidata.org/entity/Q34740"
        ]
    },
    
    "image": "https://inpn.mnhn.fr/photos/uploads/webtofs/inpn/3/181473.jpg",
    "sameAs": [
        "http://www.marinespecies.org/aphia.php?p=taxdetails&id=137115",
        "http://www.iucnredlist.org/details/6335",
        "https://www.gbif.org/species/5220003"
    ]
}
{% endhighlight %}