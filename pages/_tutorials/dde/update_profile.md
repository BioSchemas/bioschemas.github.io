---
layout: default
title: Profile Update
nextTutorial:
  link: ./new_profile
  title: Create a New Profile
---
# Update a Profile

Profiles are constraints agreed by the community that capture (i) the information properties which are minimum (M), recommended (R), or optional (O), (ii) the cardinality of the property, i.e. whether it is expected to occur once or many times, and (iii) associated controlled vocabulary terms drawn from existing ontologies. These refine and optimise the use of ‘types’ by a specific community. Since communities may change, for example, the cardinality of a property after discussion, there is a need to have a simple mechanism to version and modify profiles. The process for updating a profile is described below. Note, if you are comfortable with JSON schema and JSON-LD, you are welcome to copy, paste, and edit the JSON-LD files in the Bioschemas Specifications repository (and skip directly to step 8 below)

### Step 1 - Obtain community consensus on the proposed changes to be made
{% include_relative create_google_sheet.md %}

### Step 2 - Search for the profile you are trying to update in the DDE
{% include_relative search_the_registry.md %}

### Step 3 - Extend from the profile you are trying to update
{% include_relative extend_class.md %}

### Step 4 - Create new properties as needed
{% include_relative create_properties.md %}

### Step 5 - Add JSON validation rules to express property constraints
{% include_relative add_validation_rules.md %}

### Step 6 - Save your schema
{% include_relative save_your_schema.md %}

### Step 7 - Edit your JSONLD to fix the parent class
{% include_relative edit_your_jsonld.md %}

### Step 8 - Verify that your JSONLD schema file is working properly
{% include_relative check_your_spec.md %}

### Step 9 - If you have not already, save your JSONLD to the bioschemas Specification repository
{% include_relative save_to_specs_repo.md %}

### Step 10 - Update the bioschemas specification in the DDE schema registry
{% include_relative push_updates_to_dde.md %}
