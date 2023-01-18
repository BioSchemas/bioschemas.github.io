---
title: Review a pull request on a Bioschemas Specification
previousTutorial:
  link: ./dde/new_type
  title: Create New Type

  
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
    name: People familiar with GitHub, JSON-LD and JSON-schema representation
  name: "How to review a pull request for a Bioschemas Specification"
  author:
  - "@type": Person
    name: "Ginger Tsueng"
    "@id": https://bioschemas.org/people/GingerTsueng
    url: https://bioschemas.org/people/GingerTsueng
  - "@type": Person
    name: "Leyla Garcia"
    "@id": https://bioschemas.org/people/LeylaGarcia
    url: https://bioschemas.org/people/LeylaGarcia
  - "@type": Person
    name: "Nick Juty"
    "@id": https://bioschemas.org/people/NickJuty
    url: https://bioschemas.org/people/NickJuty
  - "@type": Person
    name: "Alasdair Gray"
    "@id": https://bioschemas.org/people/AlasdairGray
    url: https://bioschemas.org/people/AlasdairGray
  - "@type": Person
    name: "Sahar Frika"
    "@id": https://bioschemas.org/people/SaharFrikha
    url: https://bioschemas.org/people/SaharFrikha
  dateModified: 2022-11-02
  description: "In this how-to, we will provide recommendations for reviewing a pull request on a Bioschemas specification and triggering the automated scripts for pushing it onto the website"
  keywords: "schemaorg, markup, structured data, bioschemas"
  license: CC-BY 4.0
  version: 0.2

---

A community member has created or updated a Bioschemas specification JSON-LD file and created a pull request. Here’s how to help review and merge it, so that the website and the DDE will be updated. 

### Step 1 ensure you have access to the appropriate channels and repositories
* You will need access to the '#spec_repo_updates' channel on [slack](https://bioschemas.slack.com)
* You will need to be able to perform merges in the [Bioschemas specification repository](https://github.com/BioSchemas/specifications)
* You will need to be able to perform merges in the [Bioschemas website repository](https://github.com/BioSchemas/bioschemas.github.io)

### Step 2 Claim the pull request
* Reply to the slack notification on the pull request to inform others that you will be reviewing it
* Assign the pull request to yourself on GitHub

### Step 3 - Verify that the JSONLD schema file is working properly and that the config file is up-to-date
* Go to the branch or fork of the [Bioschemas specification repository](https://github.com/BioSchemas/specifications) that has the Bioschemas profile JSON-LD file that is the subject of the pull request
  * Does it load without error in the DDE?
  * Does it have the correct hierarchy (rdfs:subclassOf)?
  * Does the `@context` have the necessary iri’s?
  * __Only if it is a __profile__: Are the constraints properly expressed in the `$validation`?
* Verify that the configuration file in the bioschemas website repository is up-to-date
  * The configuration file needs to be updated __only for brand new specifications__, to update:
    * Create a new branch in the Bioschemas website repository with a suitable name to identify the intended outcome of the work, e.g. for a new 0.4 draft of the “example profile” we might have draft-example-0.4.
    * Find the [`_data/metadata_mapping.csv` file](https://github.com/BioSchemas/bioschemas.github.io/blob/profile-auto-generation/_data/metadata_mapping.csv). If it isn’t, add a row for the specification stating the specification name, working group name, and expected parent.
      * Note that the expected parent of a profile specification and type specification may be different:
        * For example: parent for FormalParameter profile is expected to be bioschemastypes:FormalParameter type, but the parent for FormalParameter type is expected to be schema:Intangible
    * Create a pull request from your branch to the parent branch.

### Step 4 - Merge the pull requests
* __IF you edited the metadata_mapping file in Step 3__: 
  * merge the pull request from your branch of the Bioschemas website to the parent branch. 
  * This will ensure that the automated script has the information needed to automatically generate html files once triggered.
* Merge the pull request for the new/updated JSON-LD file that you reviewed to the master branch of the specification repository
  * This will trigger the GitHub action for automatically generating the corresponding page in the Bioschemas website.
  * The GitHub action will create a new branch of the Bioschemas website with the required changes
    * The branch will be named based on the date and time of when the GitHub action was triggered
      * It will follow the format YYYY_MM_DD-HH_MM_SS
    * The GitHub action will also automatically generate a pull request to merge the branch into master
* Merge the pull request that was generated by the GitHub action

### Step 5 - Update the bioschemas specification in the DDE schema registry (to be automated and removed as a step)
* This step has been automated in a branch, but that branch has not been merged as it is dependant on the GitHub action in Step 4


### Links and Further Reading
* Documentation on the automated JSON-LD-to-webpage conversion: <https://hackmd.io/zGOAxx-BRfi4rDiaW9Rk4Q?both>
* Documentation on the automated DDE-updates: <https://github.com/bioschemas/bioschemas-dde>
* About JSON-LD: <https://json-ld.org/>
* About JSON-schema: <https://json-schema.org/>
* The FAQ for the Data Discovery Engine (DDE): <https://discovery.biothings.io/faq/dde>
