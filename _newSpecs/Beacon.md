---
description: In this document we propose a simple way for a ELIXIR/GA4GH beacons to self-describe
  their genetic variant cardinality service for better integration with other beacons
  within the beacon-network. It builds upon the Beacon service API and uses existing
  schema.org entities and properties.
edit_url: https://github.com/BioSchemas/bioschemas.github.io/edit/master/_newSpecs/Beacon.md
extended_props:
  CreativeWork:
  - bsc_dec: provider
    cardinality: MANY
    controlled_vocab:
      ontologies: []
      terms: []
    expected_type:
    - Organization
    - Person
    marginality: Minimum
    name: provider
    sdo_desc: The service provider, service operator, or service performer; the goods
      producer. Another party (a seller) may offer those services or goods on behalf
      of the provider. A provider may also serve as the seller.
  - bsc_dec: version
    cardinality: ONE
    controlled_vocab:
      ontologies: []
      terms: []
    expected_type:
    - Number
    - Text
    marginality: Minimum
    name: version
    sdo_desc: The version of the CreativeWork embodied by a specified resource.
  DataCatalog:
  - bsc_dec: dataset
    cardinality: MANY
    controlled_vocab:
      ontologies: []
      terms: []
    expected_type:
    - Dataset
    marginality: Minimum
    name: dataset
    sdo_desc: A dataset contained in this catalog.
  Thing:
  - bsc_dec: identifier
    cardinality: MANY
    controlled_vocab:
      ontologies: []
      terms: []
    expected_type:
    - PropertyValue
    - Text
    - URL
    marginality: Recommended
    name: identifier
    sdo_desc: The identifier property represents any kind of identifier for any kind
      of <a class="localLink" href="http://schema.org/Thing">Thing</a>, such as ISBNs,
      GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing
      many of these, either as textual strings or as URL (URI) links. See <a href="/docs/datamodel.html#identifierBg">background
      notes</a> for more details.
  - bsc_dec: name
    cardinality: MANY
    controlled_vocab:
      ontologies: []
      terms: []
    expected_type:
    - Text
    marginality: Recommended
    name: name
    sdo_desc: The name of the item.
  - bsc_dec: sameAs
    cardinality: ONE
    controlled_vocab:
      ontologies: []
      terms: []
    expected_type:
    - URL
    marginality: Optional
    name: sameAs
    sdo_desc: URL of a reference Web page that unambiguously indicates the item's
      identity. E.g. the URL of the item's Wikipedia page, Wikidata entry, or official
      website.
  - bsc_dec: url
    cardinality: ONE
    controlled_vocab:
      ontologies: []
      terms: []
    expected_type:
    - URL
    marginality: Minimum
    name: url
    sdo_desc: URL of the item.
g_mapping_file: Beacon Mapping
gh_folder: https://github.com/BioSchemas/Beacon
gh_tasks: https://github.com/BioSchemas/bioschemas/labels/type%3A%20Beacon
hierarchy:
- DataCatalog
- CreativeWork
- Thing
layout: new_spec_detail
name: Beacon
new_props:
- bsc_dec: supportedRefs
  cardinality: MANY
  controlled_vocab:
    ontologies: []
    terms: []
  expected_type:
  - citation
  marginality: Recommended
  name: supportedReference
  sdo_desc: A citation or reference to another creative work, such as another publication,
    web page, scholarly article, etc.
parent_type: DataCatalog
spec_mapping_url: https://docs.google.com/spreadsheets/d/1WVVQ9UzEWz7hxreJwqf5SIyYO6YalZuASRX9njv7hYE/edit?usp=drivesdk
spec_type: Profile
status: revision
subtitle: 'A convention for beacon to self-describe. '
version: 0.0.1
---