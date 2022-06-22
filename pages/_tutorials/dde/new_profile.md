---
layout: default
title: Create New Profile
nextTutorial:
  link: ./update_type
  title: Update a Type
---

# Create a New Profile
Profiles are constraints agreed by the community that capture (i) the information properties which are minimum (M), recommended (R), or optional (O), (ii) the cardinality of the property, i.e. whether it is expected to occur once or many times, and (iii) associated controlled vocabulary terms drawn from existing ontologies. These refine and optimise the use of ‘types’ by a specific community. Since communities may change, for example, the cardinality of a property after discussion, there is a need to have a simple mechanism to version and modify profiles. The process for creating a new profile is described below.

### Step 1 - Create your new specification in google sheets for ease of collaborative development
<details>
  <summary>We start with the google spreadsheet, as these are easy to use for collaboratively developing a schema and attaining community consensus.</summary>
  
 - Follow [steps 1-6](https://github.com/BioSchemas/bioschemas.github.io/blob/master/pages/_tutorials/howto/howto_create_new_profile.md) for creating a new profile/type as a google spreadsheet. This will serve as your reference for creating and registering the new type in the Data Discovery Engine.
 - If you are familiar with programming or are comfortable with json schema, you can look at existing json files for Bioschemas types (for example, the BioChemEntity json), use scripts to convert your spreadsheet to jsonld, and skip ahead to testing your schema.
  
</details>

### Step 2 - Search for the parent class of your new profile
{% include_relative search_the_schema_registry.md %}
