---
description: A PhysicalEntity is any object that exists in the physical world and
  cannot be better represented with any other type exisitein in schema.org. In order
  to specify the nature of this physical entity, additionalProperty must be used to
  specify the nature/type of this physical entity. For instance, http://semanticscience.org/resource/SIO_010043
  can be used.
edit_url: https://github.com/BioSchemas/bioschemas.github.io/edit/master/_newSpecs/PhysicalEntity.md
extended_props:
  Thing:
  - bsc_dec: ''
    cardinality: MANY
    controlled_vocab:
      ontologies: []
      terms: []
    expected_type:
    - Text
    marginality: Recommended
    name: alternateName
    sdo_desc: An alias for the item.
  - bsc_dec: ''
    cardinality: ONE
    controlled_vocab:
      ontologies: []
      terms: []
    expected_type:
    - Text
    marginality: Recommended
    name: description
    sdo_desc: A description of the item.
  - bsc_dec: ''
    cardinality: ONE
    controlled_vocab:
      ontologies: []
      terms: []
    expected_type:
    - PropertyValue
    - Text
    - URL
    marginality: Minimum
    name: identifier
    sdo_desc: The identifier property represents any kind of identifier for any kind
      of <a class="localLink" href="http://schema.org/Thing">Thing</a>, such as ISBNs,
      GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing
      many of these, either as textual strings or as URL (URI) links. See <a href="/docs/datamodel.html#identifierBg">background
      notes</a> for more details.
  - bsc_dec: ''
    cardinality: MANY
    controlled_vocab:
      ontologies: []
      terms: []
    expected_type:
    - ImageObject
    - URL
    marginality: Optional
    name: image
    sdo_desc: An image of the item. This can be a <a class="localLink" href="http://schema.org/URL">URL</a>
      or a fully described <a class="localLink" href="http://schema.org/ImageObject">ImageObject</a>.
  - bsc_dec: ''
    cardinality: ONE
    controlled_vocab:
      ontologies: []
      terms: []
    expected_type:
    - Text
    marginality: Recommended
    name: name
    sdo_desc: The name of the item.
  - bsc_dec: ''
    cardinality: MANY
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
  - bsc_dec: ''
    cardinality: ONE
    controlled_vocab:
      ontologies: []
      terms: []
    expected_type:
    - URL
    marginality: Optional
    name: url
    sdo_desc: URL of the item.
  - bsc_dec: ''
    cardinality: MANY
    controlled_vocab:
      ontologies: []
      terms: []
    expected_type:
    - URL
    marginality: Recommended
    name: additionalType
    sdo_desc: An additional type for the item, typically used for adding more specific
      types from external vocabularies in microdata syntax. This is a relationship
      between something and a class that the thing is in. In RDFa syntax, it is better
      to use the native RDFa syntax - the 'typeof' attribute - for multiple types.
      Schema.org tools may have only weaker understanding of extra types, in particular
      those defined externally.
g_mapping_file: PhysicalEntity Mapping
gh_folder: https://github.com/BioSchemas/PhysicalEntity
gh_tasks: https://github.com/BioSchemas/bioschemas/labels/type%3A%20PhysicalEntity
hierarchy:
- Thing
layout: new_spec_detail
name: PhysicalEntity
new_props:
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab:
    ontologies: []
    terms: []
  expected_type:
  - StructuredValue
  marginality: Optional
  name: additionalProperty
  sdo_desc: Any addional property required by this record that is not covered by any
    other explicit property. The property additionalType from Thing should be used
    to point to an ontological term describing the nature of this property.
parent_type: Thing
spec_mapping_url: https://docs.google.com/spreadsheets/d/1e_8LUQ4GYxar0-gotOXsbAUVUQkvF6GNuBdr54hbcdc/edit?usp=drivesdk
spec_type: Type
status: revision
subtitle: Bioschemas specification describing a physical entity.
version: 0.0.1
---