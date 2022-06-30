---
layout: default
title: New Type
---

# Create a New Type
JSON Schema validation rules are automatically created and used by the DDE to apply the constraints found in profiles. Types do not have these constraints, so this process will skip and ignore any step that involves setting JSON Schema validation rules. The DDE refers to all specifications (profiles and types) as classes, and may use the term 'type' interchangeably with 'class'.

To create a new type, you will need to determine which existing type you would derive your new type from. For instance, it may just be a basic schema.org type, such as ‘Thing’.

### Step 1 - Create your new type specification in your community's preferred collaborative environment (google spreadsheets, whiteboard, HackMd document, etc.)
{% include_relative create_google_sheet.md %}

### Step 2 - Search for the parent class of your new type
{% include_relative search_the_schema_registry.md %}

### Step 3 - Extend from the parent class
{% include_relative extend_class.md %}

### Step 4 - Create new properties as needed
{% include_relative create_properties.md %}

### Step 6 - Remove the default JSON Schema validation rules
{% include_relative edit_your_jsonld.md %}

### Step 5 - Save your schema
{% include_relative save_your_schema.md %}

### Step 7 - Verify that your JSONLD schema file is working properly
{% include_relative check_your_spec.md %}

### Step 8 - If you have not already, save your JSONLD to the bioschemas Specification repository
{% include_relative save_to_specs_repo.md %}

### Step 9 - Update the bioschemas specification in the DDE schema registry
{% include_relative push_updates_to_dde.md %}
