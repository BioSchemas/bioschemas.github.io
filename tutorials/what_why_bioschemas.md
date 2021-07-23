---
layout: tutorial
title: Bioschemas, what and why?
previousTutorial:
  link: ./markup_examples
  title: Schema.org markup examples
nextTutorial:
  link: ./howto/howto_right_profile
  title: How to select the right profile

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
    name: People interested in introductory information to Bioschemas
  name: "Bioschemas, what and why?"
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
  description: "In this tutorial you will learn what Bioschemas is, what the added value to schema.org.is and what the main elements in Bioschemas are"
  keywords: "schemaorg, markup, structured data, bioschemas"
  license: CC-BY 4.0
  version: 2.0
---

## 1. What is Bioschemas?

Bioschemas is a community project built on top of schema.org, aiming to improve interoperability in Life Sciences so resources can better communicate and work together by using a common markup on their websites.

Using schema.org markup on web pages enables the generation of 'info box' summaries in typical web search results pages, as exemplified by google search results. Bioschemas aims to make it possible to get similar summaries, but focused on Life Science resources such as Proteins, Samples, Beacons, Tools, Training, Life science events and so on.

Imagine an insulin summary appearing within search results, but rather than pointing to Wikipedia, that summary would direct one to specialized resources such as Orphanet or CATH as seen in Figure 1. In this way you would get a quick overview while also being provided links to relevant resources, all in one search.

{% include image.html file="/tutorials/images/ilustration_life_sciences_event.png" caption="Figure 1. Insulin summary on a search engine" alt="Insulin summary on a search engine" %}


## 2. What are the benefits of Bioschemas?

Bioschemas inherits the benefits from schema.org, i.e., enabling machines to understand what your metadata is in advance, making it easier to find, integrate, and re-use your data. It also brings some benefits tailored to the Life Sciences community. In Figure 2, you can find a graphical summary of such benefits, which are explained in more detail in the paragraphs below.

{% include image.html file="/tutorials/images/ilustration_life_sciences_event.png" caption="Figure 2: Event profile provided by Bioschemas for the Event type in schema.org" alt="Event profile provided by Bioschemas for the Event type in schema.org" %}

<table>
  <tbody>
    <tr>
      <td align="center">
        <img src="/tutorials/images/exclamation_mark.png" alt="warning">
      </td>
      <td>
        Schema.org provides only 'types', while Bioschemas provides 'types' and 'profiles'. A profile is a customisation of type, including important guidelines on how to use it within the Life Sciences domain. A profile can be used to define the semantics of a particular property, the valid value(s) and ranges that may be attributed to that property, and the cardinality with which that property may appear. <br/>Disclaimer: Initially, Bioschemas types were developed with the aim to eventually mature those types and have them integrated for direct use in schema.org. While this remains desirable, it is not essential; community tools and resources are being developed to directly harvest this markup, and there are activities in progress to migrate Bioschemas markup from individual resources to the EOSC (European Open Science Cloud). 
      </td>
    </tr>
  </tbody>
</table>


* Bioschemas focuses on key properties prioritised as Minimum, Recommended and Optional  based on community agreements and common practices

<table>
  <tbody>
    <tr>
      <td align="center">
        <img src="/tutorials/images/information_mark.png" alt="info">
      </td>
      <td>
        <ul><li>Minimum properties should be provided</li><li>Recommended properties should be provided whenever possible and available</li><li>Optional properties could be omitted unless important or relevant for your resource</li></ul>
        <br/>
        e.g., For the Event case shown on Figure 2, endDate and location are minimum while organizer is recommended.
        <br/>
        Reminder: a property helps you describe your resource
      </td>
    </tr>
  </tbody>
</table>

* Bioschemas provides additional recommendations regarding properties cardinality

<table>
  <tbody>
    <tr>
      <td align="center">
        <img src="/tutorials/images/information_mark.png" alt="info">
      </td>
      <td>
        A property expects ONE or MANY elements
        <br/>
e.g., For the Event case, endDate should be ONE while organizer could be MANY
      </td>
    </tr>
  </tbody>
</table>

* Bioschemas customises schema.org types (see previous tutorial) to better supports needs on the life sciences community

<table>
  <tbody>
    <tr>
      <td align="center">
        <img src="/tutorials/images/information_mark.png" alt="info">
      </td>
      <td>
        Event already exists in schema.org. However, Bioschemas has added some new properties, for instance, "prerrequisite" is commonly used in Life Sciences to define a list of required skills to be able to attend an appropriate event.
      </td>
    </tr>
  </tbody>
</table>

* Bioschemas reuses terms from well-known ontologies, thus avoiding reinventing the wheel

<table>
  <tbody>
    <tr>
      <td align="center">
        <img src="/tutorials/images/information_mark.png" alt="info">
      </td>
      <td>
        Tools, a SoftwareApplication profile, recommends using terms from the <a href="http://bioportal.bioontology.org/ontologies/EDAM">EDAM</a> ontology in order to specify, for instance, the input and output expected.
        <br/>
        Protein, a BioChemEntity profile, includes some properties that come from well-known ontologies. For instance associatedWith comes from from the <a href="https://www.ebi.ac.uk/ols/ontologies/so">Sequence Ontology</a>. By reusing terms, Bioschemas aims to avoid reinventing the wheel.
      </td>
    </tr>
  </tbody>
</table>
