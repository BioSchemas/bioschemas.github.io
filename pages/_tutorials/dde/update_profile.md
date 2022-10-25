---
title: Profile Update
nextTutorial:
  link: ./new_profile
  title: Create a New Profile
  
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
    name: People interested in updating a Bioschemas profile
  name: "How to update a Bioschemas Profile with the Data Discovery Engine (DDE) Schema Playground"
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
  dateModified: 2022-10-24
  description: "In this how-to, we will guide you through the necessary steps in order to update an existing Bioschemas profile"
  keywords: "schemaorg, markup, structured data, bioschemas"
  license: CC-BY 4.0
  version: 0.1

---
# Update a Profile

You have come to a community consensus on changes needed to a profile that already exists. Congratulations! Now you have to update the new profile version on the Bioschemas website. Note, if you are comfortable with JSON schema and JSON-LD, you are welcome to copy, paste, and edit the JSON-LD files in the Bioschemas Specifications repository

### Step 1 - Log in
{% include_relative login_to_dde.md %}

