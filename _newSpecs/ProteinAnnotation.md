---
description: In this document we propose a simple way for a beacons to self-describe
  their genetic variant cardinality service for better integration with other beacons
  within the beacon-network. It builds upon the Beacon service API and uses existing
  schema.org entities and properties.
g_mapping_file: ProteinAnnotation Mapping
github_url: https://github.com/BioSchemas/Proteins
layout: new_spec_detail
name: ProteinAnnotation
new_bsc:
- bsc_dec: ''
  cardinality: ONE
  controlled_vocab: ''
  domain: invalid domain type
  domain_case: new_bsc
  expected_type:
  - Thing
  marginality: Recommended
  name: isMentionedIn
  sdo_desc: CretiveWork, Dataset, collection mentioning this entity  Inverse of:mentions
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab: ''
  domain: invalid domain type
  domain_case: new_bsc
  expected_type:
  - Text
  marginality: Recommended
  name: alternateName
  sdo_desc: An alias for the item.
- bsc_dec: ''
  cardinality: ONE
  controlled_vocab: ''
  domain: invalid domain type
  domain_case: new_bsc
  expected_type:
  - Text
  marginality: Recommended
  name: description
  sdo_desc: A description of the item.
- bsc_dec: ''
  cardinality: ONE
  controlled_vocab: ''
  domain: invalid domain type
  domain_case: new_bsc
  expected_type:
  - PropertyValue
  - Text
  - URL
  marginality: Minimum
  name: identifier
  sdo_desc: 'The identifier property represents any kind of identifier for any kind
    of Thing, such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated
    properties for representing many of these, either as textual strings or as URL
    (URI) links. See background notes for more details. Recommendation: identifiers.org
    whenever possible'
- bsc_dec: ''
  cardinality: ONE
  controlled_vocab: ''
  domain: invalid domain type
  domain_case: new_bsc
  expected_type:
  - Text
  marginality: Recommended
  name: name
  sdo_desc: The name of the item.
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab: ''
  domain: invalid domain type
  domain_case: new_bsc
  expected_type:
  - URL
  marginality: Optional
  name: sameAs
  sdo_desc: URL of a reference Web page that unambiguously indicates the item's identity.
    E.g. the URL of the item's Wikipedia page, Wikidata entry, or official website.
- bsc_dec: ''
  cardinality: ONE
  controlled_vocab: ''
  domain: invalid domain type
  domain_case: new_bsc
  expected_type:
  - URL
  marginality: Optional
  name: url
  sdo_desc: URL of the item.
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab: ''
  domain: invalid domain type
  domain_case: new_bsc
  expected_type:
  - QuantitativeValue
  marginality: Optional
  name: biocoordinates
  sdo_desc: 'Coordinates in a 1 or 2D space, for instance length/coordinates in a
    sequence.  Usage (example): Use a QuantitativeValue with properties minValue and
    maxValue for a region or value for a site in a Protein. Use it only with value
    for a protein length.'
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab: ''
  domain: invalid domain type
  domain_case: new_bsc
  expected_type:
  - Text
  marginality: Minimum
  name: biologicalType
  sdo_desc: List with types preferably supported by BioSchemas-> enumeration list
    of values maintained on a wikipage (cf accessibilityAPI in schema.org for implementation).
    If the value is not on the list then the data will still be parsed but only generic
    properties will be validated. {population,individual,tissue,cell,molecule,protein,nucleic
    acid}
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab: ''
  domain: invalid domain type
  domain_case: new_bsc
  expected_type:
  - Thing
  marginality: Optional
  name: crossReference
  sdo_desc: 'A pointer to another, somehow related entity. Usage: Whenever isBasedOn/isBasisFor,
    isPartOf/hasPart, citation or any other more specific does not work.'
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab: ''
  domain: invalid domain type
  domain_case: new_bsc
  expected_type:
  - CreativeWork
  - URL
  - BiologicalEntity
  marginality: Optional
  name: isBasisFor
  sdo_desc: 'A resource for which this resource has been used for the creation of
    the former.  Inverse property: isBasedOn'
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab: ''
  domain: invalid domain type
  domain_case: new_bsc
  expected_type:
  - Text
  - URL
  - PropertyValue
  marginality: Optional
  name: representation
  sdo_desc: Representation of this entity. For instance, chemical structure or sequence
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab: 'Yes'
  domain: invalid domain type
  domain_case: new_bsc
  expected_type:
  - URL
  marginality: Optional
  name: taxon
  sdo_desc: A url pointing to NCBI Taxonomy or a taxonomic resource
new_sdo: []
reu_bsc: []
reu_sdo:
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab: ''
  domain: CreativeWork
  domain_case: reu_sdo
  expected_type:
  - CreativeWork
  - URL
  marginality: Recommended
  name: citation
  sdo_desc: A citation or reference to a creative work, such as a publication, web
    page, scholarly article, etc.
- bsc_dec: ''
  cardinality: ONE
  controlled_vocab: ''
  domain: CreativeWork
  domain_case: reu_sdo
  expected_type:
  - Date
  - DateTime
  marginality: Optional
  name: dateCreated
  sdo_desc: The date on which the CreativeWork/BiologicalEntity was created or the
    item was added to a DataFeed/Dataset/DataRepository.
- bsc_dec: ''
  cardinality: ONE
  controlled_vocab: ''
  domain: CreativeWork
  domain_case: reu_sdo
  expected_type:
  - Date
  - DateTime
  marginality: Optional
  name: dateModified
  sdo_desc: The date on which the CreativeWork/BiologicalEntity was most recently
    modified or when the item's entry was modified within a DataFeed/Dataset/DataRepository
- bsc_dec: ''
  cardinality: ONE
  controlled_vocab: ''
  domain: CreativeWork
  domain_case: reu_sdo
  expected_type:
  - Date
  marginality: Optional
  name: datePublished
  sdo_desc: Date of first broadcast/publication.
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab: ''
  domain: CreativeWork
  domain_case: reu_sdo
  expected_type:
  - DataDownload
  marginality: Optional
  name: distribution
  sdo_desc: A downloadable form of this entity, at a specific location, in a specific
    format
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab: ''
  domain: CreativeWork
  domain_case: reu_sdo
  expected_type:
  - CreativeWork
  - URL
  - BiologicalEntity
  marginality: Optional
  name: isBasedOn
  sdo_desc: A resource that was used in the creation of this resource. This term can
    be repeated for multiple sources. For example, http://example.com/great-multiplication-intro.html.
    Supersedes isBasedOnUrl.
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab: ''
  domain: CreativeWork
  domain_case: reu_sdo
  expected_type:
  - BiologicalEntity
  marginality: Optional
  name: isPartOf
  sdo_desc: 'Indicates a BiologicalEntity that this BiologicalEntity is (in some sense)
    part of.  Inverse property: hasPart.'
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab: ''
  domain: CreativeWork
  domain_case: reu_sdo
  expected_type:
  - Text, url, PropertyValue
  marginality: Optional
  name: measurementTechnique
  sdo_desc: To describe the process used to obtain a biological entity or which is
    associated with that entity (i.e procedure to obtain it or measure/characterise
    it)
spec_mapping_url: https://docs.google.com/spreadsheets/d/1KNVv3xedOpckk3ZcILnPmlys2DTzpk8KnkRwVFR2SL0/edit?usp=drivesdk
status: revision
stereotype: BiologicalEntity
subtitle: 'A convention for beacon to self-describe. '
version: 0.0.1
---