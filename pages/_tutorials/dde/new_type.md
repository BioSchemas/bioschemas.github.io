---
layout: default
title: New Type
---

# Create a New Type
JSON Schema validation rules are automatically created and used by the DDE to apply the constraints found in profiles. Types do not have these constraints, so this process will skip and ignore any step that involves setting JSON Schema validation rules. The DDE refers to all specifications (profiles and types) as classes, and may use the term 'type' interchangeably with 'class'.

To create a new type, you will need to determine which existing type you would derive your new type from. For instance, it may just be a basic schema.org type, such as ‘Thing’.

### Step 1 - Create your new type specification in google sheets for ease of collaborative development
{% include_relative create_google_sheet.md %}

### Step 2 - Search for the parent class of your new type
{% include_relative search_the_schema_registry.md %}

### Step 3 - Extend from the parent class
{% include_relative extend_class.md %}
