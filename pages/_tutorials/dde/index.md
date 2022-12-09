---
layout: default
title: Data Discovery Engine
---

# Data Discovery Engine
The [Data Discovery Engine (DDE)](https://discovery.biothings.io/) provides guidance for researchers on how to make their data discoverable and reusable, and bring the practical benefits of data sharing to researcher’s own research projects, as well as the research community as a whole. It was developed and is maintained by Dr. Chunlei Wu’s lab at the Scripps Research Institute and is supported by funding from the National Center for Data to Health (CD2H). The Data Discovery Engine has user-friendly tools which help with the extension and reusability of schemas. A general overview of the DDE Schema Playground can be found at: https://discovery.biothings.io/faq/dde#what-is-schema-playground

 - Note, a GitHub account is required to unlock most of the functionality of the DDE. You can sign up for GitHub for free at https://github.com

### How Bioschemas Specifications are stored in the DDE Schema Registry
Only the most recent drafts and releases of specifications should be saved to the registry. The DDE does not currently distinguish between profiles and types and instead treats all specifications as classes. The term **class** in the DDE is equivalent to the term **specification** in Bioschemas; hence, different kinds of specifications are saved to different namespaces in the DDE registry. These namespaces include:
 - [bioschemas](https://discovery.biothings.io/view/bioschemas): for released profiles
 - [bioschemasdrafts](https://discovery.biothings.io/view/bioschemasdrafts): for draft profiles
 - [bioschemastypes](https://discovery.biothings.io/view/bioschemastypes): for released types
 - [bioschemastypesdrafts](https://discovery.biothings.io/view/bioschemastypesdrafts): for draft types
 - [bioschemasdeprecated](https://discovery.biothings.io/view/bioschemasdeprecated): for deprecated specifications 

## How to use the DDE Schema Playground to:
- [Update a Profile](update_profile)
- [Create a Profile](new_profile)
- [Update a Type](update_type)
- [Create a Type](new_type)


## How to review a pull request on a specification JSON-LD file
Pull requests to the [Bioschemas specification repository](https://github.com/BioSchemas/specifications) will automatically trigger a notification in the bioschemas `#spec_repo_updates` slack channel. Community members are encouraged to help review these pull requests if they are:
- Familiar with or interested in learning about how to perform pull requests and merges on GitHub
- Familiar with or interested in learning about how JSON-LD formatting
- Familiar with or interested in learning about JSON-schema validation rules __(only for pull requests involving PROFILES)__

Interested? [Here's how to review a pull request on a specification](review_a_specification_pull_request)
