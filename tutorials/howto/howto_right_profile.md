---
layout: tutorial
title: How to select the right profile for your resource
previousTutorial:
  link: ./what_why_bioschemas
  title: What and why bioschemas
nextTutorial:
  link: ./howto/howto_create_new_profile
  title: How to create a new draft profile

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
    name: People interested in selecting a Bioschemas profile to markup their own data
  name: "How to select the right profile for your resource"
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
  - "@type": Person
    name: "Franck Michel"
    "@id": https://bioschemas.org/people/FranckMichel
    url: https://bioschemas.org/people/FranckMichel/    
  dateModified: 2021-05-05
  description: "In this how-to, we will guide you through the necessary steps for you to select a Bioschemas profile that will be later used to add mark up to your own resources"
  keywords: "schemaorg, markup, structured data, bioschemas profile"
  license: CC-BY 4.0
  version: 2.0
---

## Your first encounter with Bioschemas profiles

You can find the availabe Bioschemas profiles at [http://bioschemas.org/specifications](http://bioschemas.org/specifications). There, you will be presented with a list of all the current and stable profiles, as illustrated on Figure 1. You can hover on the profile name to see a quick description. Should you need a more detailed information, just click on the profile name.

As seen on Figure 1,  each profile will show you details such as current version, release date, use cases, crosswalk, tasks and issues, usage examples and current live deploys.

| ![Figure 1. List of some Bioschemas profiles](/tutorials/images/specifications.png) |
| __Figure 1. List of some Bioschemas profiles__ |

<table>
  <tbody>
    <tr>
      <td align="center">
        <img src="/tutorials/images/information_mark.png" alt="info">
      </td>
      <td>
      <ul>
        <li>Use cases: Used as a basis for the profile</li>
        <li>Crosswalk: Documentation on the brainstorming and process followed by a group in order to come up with a profile specification</li>
        <li>Tasks & issues: Link to a GitHub space where you can report issues with a profile, see the assignees, and participate of the discussion</li>
        <li>Example: Usage examples for the profile</li>
        <li>Live deploys: Link to live deploys for the profile</li>
      </ul>
      </td>
    </tr>
  </tbody>
</table>

## Pick up a profile

Which profile is the right one for you will depend on your resource. Go through the list above, and try to figure out which one most closely matches your use case.
If you cannot find any relevant profile, then check out the "Drafts" tab where some new profiles or new profile releases are being discussed.

If you still cannot find any profile suited for your needs, do not hesite to engage with the community by submitting an issue on [Github](https://github.com/BioSchemas/specifications/issues).

In the next section, we will present some hints on those profiles that have been more broadly used so far, i.e., mainly customizing generic types rather corresponding to specific Life Science entities.

## A guided tour to some selected Bioschemas profiles

### DataCatalog

Also known as data repository, a data catalog commonly aggregates more than one dataset. If your resource supports only one dataset, you still could decide to markup your resource, in this case, as [DataCatalog](/specifications/DataCatalog) and also [Dataset](/specifications/Dataset) (this would make it easier if you are thinking of adding more datasets. However, whenever more than one dataset is provided, it totally makes sense to markup your resource as a [DataCatalog](/specifications/DataCatalog).

### Dataset

If your resource provides data and you can easily identify a common entity type for all the data contained in it, you should probably go for a [Dataset](/specifications/Dataset) profile. Let's clarify what we mean by "common type". Let's suppose you have chemical compounds including drugs, proteins and cells. If you see them all as the same thing, chemical compound, you have one [Dataset](/specifications/Dataset), and you have found the right profile for you. However, if you actually distinguish drugs from proteins from cells and so, and (maybe even) tailor the information provided for each case, you have a data catalog and multiple datasets, you should use both, one DataCatalog and multiple [Datasets](/specifications/Dataset).
