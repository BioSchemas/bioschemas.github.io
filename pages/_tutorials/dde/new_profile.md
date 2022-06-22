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
{% include_relative create_google_sheet.md %}

### Step 2 - Search for the parent class of your new profile
{% include_relative search_the_schema_registry.md %}
