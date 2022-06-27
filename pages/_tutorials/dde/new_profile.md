---
layout: default
title: Create New Profile
nextTutorial:
  link: ./update_type
  title: Update a Type
---

# Create a New Profile
Profiles are constraints agreed by the community that capture (i) the information properties which are minimum (M), recommended (R), or optional (O), (ii) the cardinality of the property, i.e. whether it is expected to occur once or many times, and (iii) associated controlled vocabulary terms drawn from existing ontologies. These refine and optimise the use of ‘types’ by a specific community. Since communities may change, for example, the cardinality of a property after discussion, there is a need to have a simple mechanism to version and modify profiles. The process for creating a new profile is described below.

### Step 1 - Create your new profile specification in in your community's preferred collaborative environment (google spreadsheets, whiteboard, HackMd document, etc.)
{% include_relative create_google_sheet.md %}

### Step 2 - Search for the parent class of your new profile
{% include_relative search_the_schema_registry.md %}

### Step 3 - Extend from the parent class
{% include_relative extend_class.md %}

### Step 4 - Create new properties as needed
{% include_relative create_properties.md %}

### Step 5 - Add JSON validation rules to express property constraints
{% include_relative add_validation_rules.md %}

### Step 6 - Save your schema
{% include_relative save_your_schema.md %}

### optional - Edit your JSONLD (if external vocabulary used as properties)
{% include_relative edit_your_jsonld.md %}

### Step 7 - Verify that your JSONLD schema file is working properly
{% include_relative check_your_spec.md %}

### Step 8 - If you have not already, save your JSONLD to the bioschemas Specification repository
{% include_relative save_to_specs_repo.md %}

### Step 9 - Update the bioschemas specification in the DDE schema registry
{% include_relative push_updates_to_dde.md %}
