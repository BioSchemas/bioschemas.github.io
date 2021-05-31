---
layout: tutorial
title: How to mark up your own resource with Bioschemas
previousTutorial:
  link: ./howto/howto_create_new_profile
  title: How to create a new draft profile
nextTutorial:
  link: ./howto/howto_add_github
  title: How to add markup to GitHub pages

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
    name: WebMaster, people interested in adding Bioschemas markup to their website
  name: "How to mark up your own resource with Bioschemas"
  author:
  - "@type": Person
    name: "Leyla Garcia"
    "@id": https://bioschemas.org/people/LeylaGarcia
    url: https://bioschemas.org/people/LeylaGarcia
  contributor:
  - "@type": Person
    name: "Ricardo Arcila"
    "@id": https://bioschemas.org/people/RicardoArcila
    url: https://bioschemas.org/people/RicardoArcila
  - "@type": Person
    name: "Victoria Dominguez del Angel"
    "@id": https://bioschemas.org/people/VictoriaDominguezDelAngel
    url: https://bioschemas.org/people/VictoriaDominguezDelAngel/
  dateModified: 2021-02-17
  description: "In this how-to, we will guide you through the necessary steps in order to get a JSON-LD markup describing your own resource using a Bioschemas profile"
  keywords: "schemaorg, markup, structured data, bioschemas"
  license: CC-BY 4.0
  version: 2.0
---

<table>
  <tbody>
    <tr>
      <td align="center">
        <img src="/tutorials/images/exclamation_mark.png" alt="warning">
      </td>
      <td>
        If have not read yet our <a href="./howto_right_profile">how to select the right profile for your resource</a>, please give it a try before this one.
      </td>
    </tr>
  </tbody>
</table>

## A pre-markup brainstorming activity

If you are eager to markup your resource, get your hands "coding" and quickly see some structured data rather that free text, you can skip this section and jump to the next one. However, if you want to go step by step and then smoothly move forward and get some JSON-LD for your resource, please stay here, you are on the right place.

### Define your strategy

If your resource involves more than one profile, you first need to define the strategy that suits best to your case. You can link a profile, let's say DataCatalog, to other related ones, let's day Dataset, via properties. Sometimes those properties are bidirectional, so you can go from DataCatalog to Dataset or the other way around. Which direction suits best to you?

<table>
  <tbody>
    <tr>
      <td align="center">
        <img src="/tutorials/images/information_mark.png" alt="info">
      </td>
      <td>
        Link from DataCatalog to Dataset if you have some few datasets and you introduce them all on your catalog landing page. Example: UniProt
        <br/>
        Link from Dataset to DataCatalog if you have that many datasets than rather than list them all, you provide a search and retrieval mechanism to find them. Example: identifiers.org
      </td>
    </tr>
  </tbody>
</table>

### Map elements to properties

Now, focus on a particular profile, have at hand the [corresponding specification page on Bioschemas](/specifications/) as well as your resource, i.e., your web pages. Do a manual exercise mapping elements to properties. This will help you have a clearer idea on what you want to achieve once you go and use gimme-my-jsonld (see next section). You might need more than one iteration here as you can face multiple option at the beginning, choose that one that gives more benefits. Keep in mind your goal by adding this mark up to your resource.

