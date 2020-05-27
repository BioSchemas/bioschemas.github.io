---
layout: meeting
name: ELIXIR All Hands 2020
title: ELIXIR All Hands 2020
dates: 8-11 June 2020
start_date: 2020-06-08
end_date: 2020-06-11
venue: Virtual (<del>Eye Filmmuseum, IJpromenade 1, Amsterdam, 1031 KT, Netherlands</del>)
meeting-name: ELIXIR All Hands 2020
meeting-url: https://elixir-europe.org/events/elixir-all-hands-2020
agenda-doc: https://docs.google.com/document/d/1VxdgDAmvT4Gffx_h1DwU4YzR_X8Z4MXTVgdvlJPjIxU/edit#
contact-people:
    - AlasdairGray
attendees:
    - AlasdairGray
---

We have had two abstracts accepted for presentation at the ELIXIR All Hands Meeting 2020. The full abstracts are included below.

- [Exploiting Bioschemas Markup to Support ELIXIR Communities](#exploiting-bioschemas-markup-to-support-elixir-communities)
- [Discovering Biodiversity Resources on the Web](#discovering-biodiversity-resources-on-the-web)


## Exploiting Bioschemas Markup to Support ELIXIR Communities

_Alasdair Gray and the Bioschemas Community_

Bioschemas aims to make life sciences resources more discoverable by exploiting widely deployed web search optimisation approaches. Specifically, the Bioschemas approach is to embed machine-readable markup using the Schema.org vocabulary within the web page about the resource. To achieve this, Bioschemas has focused on extending the Schema.org vocabulary to include life sciences types, such as Gene and Protein, and providing usage profiles that state how to markup a resource of a particular type; focusing on recommending a small number of properties that are most useful for search purposes. These types and profiles have been developed in conjunction with deployments of these on web sites where more than 11 million pages have been marked up by over 70 sites (November 2019).

In January 2020, the Bioschemas Strategic Implementation Study started with the goal of exploiting Bioschemas markup to the benefit of ELIXIR communities. This is being demonstrated in 3 communities: Rare Diseases, Plants, and Intrinsically Disordered Proteins (IDP). In each of these communities, we are enhancing the content of a community focused portal by automating the aggregation of data content from a large number of community resources. The approach lowers the bar for resources getting their content into the community portal as Bioschemas markup can easily be embedded in existing web pages without the need to deploy a complex web service implementing a community API. For example, in the Plants community the FAIDARE portal aggregates data from a small number of web services that implement the BrAPI standard. However, this means that the large number of resources which are available on the web, e.g. WheatIS or ORBITRAP, are not discoverable through FAIDARE. By adding Bioschemas markup into these sites, we are able to extend the content available through FAIDARE meaning that the community can more easily discover resources of interest.

To aggregate content from a large number of web resources, the community portals need to be able to extract the Bisochemas markup. This markup has been embedded on web sites that are deployed using a wide variety of frameworks and alternative markup formats (i.e. JSON-LD and RDFa). Increasingly websites are being deployed as single page applications where the HTML is rendered dynamically on the client’s machine based on the interaction of the user. This makes extracting markup a non-trivial task. B-MUSE has been developed to extract Bioschemas markup from web pages and deliver the structured content to the community portals. B-MUSE pulls content from a known list of web pages, rather than being a general web crawler. This enables the portal developers to focus on supporting their communities search for content within their portal.

## Discovering Biodiversity Resources on the Web

_Alasdair Gray, Franck Michel, Quentin Groom, and the Bioschemas Community_

There is an ever increasing quantity of data being published on the web. Within the area of Biodiversity there are large sequencing projects, e.g. Tree of Life, Barcode of Life, i5K, that are making vast quantities of data available. This makes discovering data and deciding its relevance increasingly challenging.

Bioschemas is an approach to make life sciences resources more discoverable by exploiting widely deployed web search optimisation approaches. Specifically, the Bioschemas approach is to embed machine-readable markup using the Schema.org vocabulary within the web page about the resource. To achieve this, Bioschemas has focused on extending the Schema.org vocabulary to include life sciences types and providing usage profiles that state how to markup a resource of a particular type; focusing on recommending a small number of properties that are most useful for search purposes. These types and profiles have been developed in conjunction with deployments of these on web sites where more than 11 million pages have been marked up by over 70 sites (November 2019). Deploying Bioschemas markup does not require special frameworks or to provide a Web API. The markup is embedded in existing web pages; making the human readable content of the pages understandable to machines.

The Bioschemas community now has proposals for 17 types that extend the Schema.org vocabulary to enable it to be used by the life sciences community. These include types such as Taxon, BioSample, and Phenotype, that are directly relevant to the Biodiversity community. There are deployments of these at the National Museum of Natural History of Paris and the Botanical Collections at the Meise Botanic Garden, Belgium.

To enable ELIXIR communities to exploit Bioschemas markup to populate community search portals, we have developed the B-MUSE directed crawler. B-MUSE will extract Bioschemas markup from a given set of pages or identifier pattern and make the structured content available for search. This approach has been demonstrated using the ELIXIR TeSS training portal, and is in active development in other ELIXIR communities, viz Rare Diseases, Plants, and Intrinsically Disordered Proteins.
