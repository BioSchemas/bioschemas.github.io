---
layout: default
title: Type Update
nextTutorial:
  link: ./new_type
  title: Create a New Type
---

# Update a Type

Jsonschema validation rules are automatically created and used by the DDE to apply the constraints found in profiles. Types do not have these constraints, so this process will skip and ignore any step that involves setting jsonschema validation rules. Since this is an UPDATE of an existing type, and NOT the creation of a new type, the parent class may need to be updated. Note, if you are comfortable with JSON schema and JSON-LD, you are welcome to copy, paste, and edit the JSON-LD files in the Bioschemas Specifications repository (and skip directly to step 7 below).

To create a new type, you will need to determine which existing type you would derive your new type from. For instance, it may just be a basic schema.org type, such as ‘Thing’.

### Step 1 - Obtain community consensus on the proposed changes to be made

### Step 2 - Search for the bioschemas type to be updated in the DDE
{% include_relative search_the_registry.md %}

### Step 3 - Extend from the bioschemas type to be updated in the DDE
{% include_relative extend_class.md %}

### Step 4 - Create new properties as needed
{% include_relative create_properties.md %}

### Step 5 - Remove the default JSON Schema validation rules
{% include_relative remove_validation.md %}

### Step 6 - Save your schema
{% include_relative save_your_schema.md %}

### Step 7 - Fix the parent class
{% include_relative edit_your_jsonld.md %}

### Step 8 - Verify that your JSONLD schema file is working properly
{% include_relative check_your_spec.md %}

### Step 9 - If you have not already, save your JSONLD to the bioschemas Specification repository
{% include_relative save_to_specs_repo.md %}

### Step 10 - Update the bioschemas specification in the DDE schema registry
{% include_relative push_updates_to_dde.md %}
