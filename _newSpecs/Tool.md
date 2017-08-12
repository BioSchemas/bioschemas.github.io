---
description: Some description.
name: Tool
new_bsc:
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab: ''
  domain: invalid domain type
  domain_case: new_bsc
  expected_type:
  - Text
  - URL
  marginality: Minimum
  name: featureList
  sdo_desc: Features or modules provided by this application (and possibly required
    by other applications).
- bsc_dec: softwareHelp:url, softwareHelp:genre, softwareHelp:description/review
  cardinality: MANY
  controlled_vocab: ''
  domain: invalid domain type
  domain_case: new_bsc
  expected_type:
  - CreativeWork
  marginality: Minimum
  name: softwareHelp
  sdo_desc: Software application help.
- bsc_dec: contact/email, contact/url, contact/name, contact/tel, contact/type
  cardinality: MANY
  controlled_vocab: ''
  domain: invalid domain type
  domain_case: new_bsc
  expected_type:
  - Text
  - URL
  marginality: Minimum
  name: softwareRequirements
  sdo_desc: 'Component dependency requirements for application. This includes runtime
    environments and shared libraries that are not included in the application distribution
    package, but required to run the application (Examples: DirectX, Java or .NET
    runtime). Supersedes requirements.'
- bsc_dec: ''
  cardinality: ONE
  controlled_vocab: ''
  domain: invalid domain type
  domain_case: new_bsc
  expected_type:
  - DataFeed
  marginality: Minimum
  name: supportingData
  sdo_desc: Supporting data for a SoftwareApplication.
- bsc_dec: ''
  cardinality: ONE
  controlled_vocab: ''
  domain: invalid domain type
  domain_case: new_bsc
  expected_type:
  - Person
  marginality: Minimum
  name: accountablePerson
  sdo_desc: Specifies the Person that is legally accountable for the CreativeWork.
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab: ''
  domain: invalid domain type
  domain_case: new_bsc
  expected_type:
  - CreativeWork
  - Text
  marginality: Minimum
  name: citation
  sdo_desc: A citation or reference to another creative work, such as another publication,
    web page, scholarly article, etc.
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab: ''
  domain: invalid domain type
  domain_case: new_bsc
  expected_type:
  - Text
  marginality: Minimum
  name: description
  sdo_desc: A description of the item.
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab: ''
  domain: invalid domain type
  domain_case: new_bsc
  expected_type:
  - Text
  marginality: Optional
  name: name
  sdo_desc: The name of the item.
- bsc_dec: publication, publication/doi
  cardinality: MANY
  controlled_vocab: ''
  domain: invalid domain type
  domain_case: new_bsc
  expected_type:
  - ''
  marginality: Recommended
  name: ''
  sdo_desc: ''
new_sdo: []
reu_bsc: []
reu_sdo: []
version: 0.0.1
---