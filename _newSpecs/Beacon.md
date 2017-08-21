---
description: In this document we propose a simple way for a beacons to self-describe
  their genetic variant cardinality service for better integration with other beacons
  within the beacon-network. It builds upon the Beacon service API and uses existing
  schema.org entities and properties.
g_mapping_file: Beacon Mapping
github_url: None
layout: new_spec_detail
name: Beacon
new_bsc:
- bsc_dec: supportedRefs
  cardinality: MANY
  controlled_vocab: 'YES'
  domain: invalid domain type
  domain_case: new_bsc
  expected_type:
  - citation
  marginality: Recommended
  name: supportedReference
  sdo_desc: A citation or reference to another creative work, such as another publication,
    web page, scholarly article, etc.
new_sdo: []
reu_bsc: []
reu_sdo:
- bsc_dec: dataset
  cardinality: MANY
  controlled_vocab: 'NO'
  domain: DataCatalog
  domain_case: reu_sdo
  expected_type:
  - Dataset
  marginality: Minimum
  name: dataset
  sdo_desc: 'A dataset contained in this catalog. Inverse property: includedInDataCatalog.'
- bsc_dec: provider
  cardinality: MANY
  controlled_vocab: 'NO'
  domain: DataCatalog
  domain_case: reu_sdo
  expected_type:
  - Organization
  - Person
  marginality: Minimum
  name: provider
  sdo_desc: The service provider, service operator, or service performer; the goods
    producer. Another party (a seller) may offer those services or goods on behalf
    of the provider. A provider may also serve as the seller. Supersedes carrier.
- bsc_dec: version
  cardinality: ONE
  controlled_vocab: 'NO'
  domain: DataCatalog
  domain_case: reu_sdo
  expected_type:
  - Number
  - Text
  marginality: Minimum
  name: version
  sdo_desc: The version of the CreativeWork embodied by a specified resource.
- bsc_dec: identifier
  cardinality: MANY
  controlled_vocab: 'NO'
  domain: Thing
  domain_case: reu_sdo
  expected_type:
  - PropertyValue
  - Text
  - URL
  marginality: Recommended
  name: identifier
  sdo_desc: The identifier property represents any kind of identifier for any kind
    of Thing, such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated
    properties for representing many of these, either as textual strings or as URL
    (URI) links. See background notes for more details.
- bsc_dec: name
  cardinality: MANY
  controlled_vocab: 'NO'
  domain: Thing
  domain_case: reu_sdo
  expected_type:
  - Text
  marginality: Recommended
  name: name
  sdo_desc: The name of the item.
- bsc_dec: sameAs
  cardinality: ONE
  controlled_vocab: 'NO'
  domain: Thing
  domain_case: reu_sdo
  expected_type:
  - URL
  marginality: Optional
  name: sameAs
  sdo_desc: URL of a reference Web page that unambiguously indicates the item's identity.
    E.g. the URL of the item's Wikipedia page, Wikidata entry, or official website.
- bsc_dec: url
  cardinality: ONE
  controlled_vocab: 'NO'
  domain: Thing
  domain_case: reu_sdo
  expected_type:
  - URL
  marginality: Minimum
  name: url
  sdo_desc: URL of the item.
spec_mapping_url: https://docs.google.com/spreadsheets/d/1WVVQ9UzEWz7hxreJwqf5SIyYO6YalZuASRX9njv7hYE/edit?usp=drivesdk
status: revision
stereotype: None
subtitle: 'A convention for beacon to self-describe. '
version: 0.0.1
---