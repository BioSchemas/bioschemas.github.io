---
title: How to add markup to IDP resources
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
    - "@id": https://schema.org
    - "@id": http://edamontology.org/topic_0089
  audience:
  - "@type": Audience
    name: (Markup provider, Markup consumer) People interested in adding Bioschemas markup to their own Plant resource
  name: "How to add markup to Plant resources"
  author:
  - "@type": Person
    name: "Dan Faria"
  dateModified: 2022-01-24
  description: "In this how-to, we will guide you through the necessary steps in order to get a JSON-LD markup describing your own IPlantDP resource using a Bioschemas profile"
  keywords: "schemaorg, markup, structured data, bioschemas, ELIXIR Plant Community"
  license: CC-BY 4.0
  version: 1.0
---

<div class="col d-flex align-items-start rounded p-4 mb-4 mt-3 shadow">
  <img class="align-self-center me-3" src="{{ '/tutorials/images/exclamation_mark.png' | relative_url }}" alt="warning">
  <div>
      This tutorial complements the tutorials <a href="./howto_right_profile">how to select the right profile for your resource</a> and
      <a href="./howto_add_markup">how to mark up your own resource with Bioschemas</a> for resources from the plant sciences, so please
      check these tutorial first.
  </div>
</div> 


## 1. Philosophy for marking-up plant sciences resources with Bioschemas
The main goal of marking-up plant sciences resources with Bioschemas is to improve their Findability on the Web, in accordance with the goal of Bioschemas themselves.
Thus, while plant datasets themselves are expected to fully comply with applicable metadata standards, such as [MIAPPE](https://www.miappe.org/), the web pages
containing these datasets need only be marked-up with the metadata that are critical for Findability. For this end, and to ensure a consistent use of Bioschemas markup
across different types of plant datasets, the plant sciences community established a MIAPPE-Bioschemas mapping, spanning the MIAPPE fields deemed relevant for
Findability of plant datasets, namely those that describe the study and its biological material(s). Despite the domain of MIAPPE being plant phenotyping experiments,
the metadata fields encompassed by this mapping are generic, and can be used for plant genotyping or omics experiments.

## 2. Key Bioschemas profiles
- The [DataCatalog](https://schema.org/DataCatalog) profile can be used to markup data repositories or any listings of plant datasets.
- [Dataset](https://schema.org/Dataset) and [Study](https://bioschemas.org/Study) are the central profiles to markup web pages about plant phenotyping, genotyping or omics datasets, as per the MIAPPE-BioSchemas mapping provided below.
- [Taxon](https://bioschemas.org/Taxon) and [BioChemEntity](https://bioschemas.org/BioChemEntity) are critical for identifying the biological material(s) used in the dataset, with the former enabling taxonomic identification down to the variety level (if applicable) and the latter identifying a specific germplasm, seed lot or genotype.
- [Person](https://schema.org/Person) and [Place](https://schema.org/Place) should be used to identify the authors and locations of the dataset.
- Molecule-level profiles, such as [Gene](https://bioschemas.org/Gene), [RNA](https://bioschemas.org/RNA) or [Protein](https://bioschemas.org/Protein) should only be used to markup web pages that describe a specific molecular entity, such as in the case of plant genome portals.
- Likewise, [Sample](https://bioschemas.org/Sample) should only be used to markup pages that specifically describe a sample.

## 3. MIAPPE-Bioschemas mapping

The correspondence between Bioschemas profiles and MIAPPE sections is the following:

| Bioschemas profile | MIAPPE section      |
|:------------------:|:-------------------:|
| Dataset            | Investigation       |
| Study              | Study               |
| Person             | Person              |
| Place              | (Study) Location    |
| BioChemEntity      | Biological Material |
| Taxon              | Biological Material |

<br/>
The recommended fields within each profile and their correspondence to MIAPPE fields are the following.

### Dataset

| Dataset fields | MIAPPE fields             |
|:--------------:|:-------------------------:|
| identifier     | Investigation unique ID   |
| name	         | Investigation title       |
| dateCreated    | Submission date           |
| datePublished	 | Public release date       |
| description    | Investigation description |
| license        | License                   |
| hasPart        | *connect to Study*        |

### Study

| Study fields           | MIAPPE fields             |
|:----------------------:|:-------------------------:|
| identifier             | Study unique ID           |
| name                   | Study title               |
| description            | Study description         |
| startDate              | startDate                 |
| endDate                | endDate                   |
| studyDomain            | N/A                       |
| PPEO:hasGrowthFacility | Type of growth facility   |
| keywords               | Experimental factor type  |
| studyProcess           | Trait                     |
| author                 | *connect to Person*       |
| studyLocation          | *connect to Place*        |
| studySubject           | *connect to BioChemEntity |

<br/>
Note that keywords and studyProcess enable only a flat representation of experimental factors and traits, respectively, but this is enough for Findability.
For genotyping or omics datasets, studyProcess can be used accordingly to indicate the types of assays done.

### Person

| Person fields  | MIAPPE fields      |
|:--------------:|:------------------:|
| name	         | Person name        |
| email	         | Person email       |
| identifier     | Person ID          |
| jobTitle       | Person role        |
| affiliation    | Person affiliation |

### Place

| Place  fields  | MIAPPE fields                   |
|:--------------:|:-------------------------------:|
| addressCountry | Geographic location (country)   |
| name           | Experimental site name          |
| latitude       | Geographic location (latitude)  |
| longitude      | Geographic location (longitude) |

### BioChemEntity

| BioChemEntity fields   | MIAPPE fields        |
|:----------------------:|:--------------------:|
| identifier             | Material source ID   |
| url                    | Material source DOI  |
| name                   | N/A                  |
| taxonomicRange         | *connect to Taxon*   |

### Taxon

| Taxon fields   | MIAPPE fields        |
|:--------------:|:--------------------:|
| identifier     | Organism             |
| taxonRank      | N/A                  |
| scientificName | Species              |
| childTaxon     | Infraspecific name   |

<br/>
To enable a flat taxonomic characterization of the biological material, taxonRank should always be "species", with the "Infraspecific name" provided as a textual value for the childTaxon field.