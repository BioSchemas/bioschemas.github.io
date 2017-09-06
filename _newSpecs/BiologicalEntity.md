---
description: "The BiologicalEntity aims to encompasses as much as possible biological\
  \ types such as \u201Csamples\u201D, \u201Cprotein\u201D, \u201Cprotein annotation\u201D\
  , \u201Cprotein structure\u201D, \u201Cphenotype\u201D and so on. Most of the properties\
  \ here will be optional as the specific profiles, i.e., a tailored usage of BiologicalEntitty,\
  \ will provide stronger requirements whenever needed.\nMost of the new properties\
  \ belong to BiologicalEntity but some required changes at a different level in schema.org.\
  \ That is why we also have some new properties for CreativeWork and Thing."
edit_url: https://github.com/BioSchemas/bioschemas.github.io/edit/master/_newSpecs/BiologicalEntity.md
extended_props:
  CreativeWork:
  - bsc_dec: ''
    cardinality: MANY
    controlled_vocab:
      ontologies: []
      terms: []
    expected_type:
    - CreativeWork
    - URL
    marginality: Recommended
    name: citation
    sdo_desc: A citation or reference to another creative work, such as another publication,
      web page, scholarly article, etc.
  - bsc_dec: ''
    cardinality: ONE
    controlled_vocab:
      ontologies: []
      terms: []
    expected_type:
    - Date
    - DateTime
    marginality: Optional
    name: dateCreated
    sdo_desc: The date on which the CreativeWork was created or the item was added
      to a DataFeed.
  - bsc_dec: ''
    cardinality: ONE
    controlled_vocab:
      ontologies: []
      terms: []
    expected_type:
    - Date
    - DateTime
    marginality: Optional
    name: dateModified
    sdo_desc: The date on which the CreativeWork was most recently modified or when
      the item's entry was modified within a DataFeed.
  - bsc_dec: ''
    cardinality: ONE
    controlled_vocab:
      ontologies: []
      terms: []
    expected_type:
    - Date
    marginality: Optional
    name: datePublished
    sdo_desc: Date of first broadcast/publication.
  - bsc_dec: ''
    cardinality: MANY
    controlled_vocab:
      ontologies: []
      terms: []
    expected_type:
    - BiologicalEntity
    marginality: Optional
    name: hasPart
    sdo_desc: Indicates a CreativeWork that is (in some sense) a part of this CreativeWork.
  - bsc_dec: ''
    cardinality: MANY
    controlled_vocab:
      ontologies: []
      terms: []
    expected_type:
    - CreativeWork
    - URL
    - BiologicalEntity
    marginality: Optional
    name: isBasedOn
    sdo_desc: A resource that was used in the creation of this resource. This term
      can be repeated for multiple sources. For example, http://example.com/great-multiplication-intro.html.
  - bsc_dec: ''
    cardinality: MANY
    controlled_vocab:
      ontologies: []
      terms: []
    expected_type:
    - BiologicalEntity
    marginality: Optional
    name: isPartOf
    sdo_desc: Indicates a CreativeWork that this CreativeWork is (in some sense) part
      of.
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
g_mapping_file: BiologicalEntity Mapping
gh_folder: https://github.com/BioSchemas/BiologicalEntity
gh_tasks: https://github.com/BioSchemas/bioschemas/labels/type%3A%20BiologicalEntity
hierarchy:
- CreativeWork
- Thing
layout: new_spec_detail
name: BiologicalEntity
new_props:
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab:
    ontologies: []
    terms: []
  expected_type:
  - MedicalCondition
  - URL
  marginality: Optional
  name: associatedDisease
  sdo_desc: Disease associated to this protein feature
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab:
    ontologies: []
    terms: []
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
  controlled_vocab:
    ontologies: []
    terms: []
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
  controlled_vocab:
    ontologies: []
    terms: []
  expected_type:
  - Thing
  marginality: Optional
  name: crossReference
  sdo_desc: 'A pointer to another, somehow related entity. Usage: Whenever isBasedOn/isBasisFor,
    isPartOf/hasPart, citation or any other more specific does not work.'
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab:
    ontologies: []
    terms: []
  expected_type:
  - Text
  - Url
  - PropertyValue
  marginality: Optional
  name: phenotype
  sdo_desc: To associate a biological entity to phenotypic information , whether the
    entity presents the phenotype or causes it.
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab:
    ontologies: []
    terms: []
  expected_type:
  - Text
  - URL
  - PropertyValue
  marginality: Optional
  name: representation
  sdo_desc: Representation of this entity. For instance, chemical structure or sequence
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab:
    ontologies: []
    terms: []
  expected_type:
  - BiologicalEntity
  - URL
  marginality: Optional
  name: sample
  sdo_desc: Clarify usage...
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab:
    ontologies:
    - name: ncbitaxon
      url: http://purl.bioontology.org/ontology/NCBITAXON/
    - name: uniprottaxon
      url: http://purl.uniprot.org/taxonomy/
    terms: []
  expected_type:
  - URL
  marginality: Optional
  name: taxon
  sdo_desc: A url pointing to NCBI Taxonomy or a taxonomic resource
- bsc_dec: ''
  cardinality: ONE
  controlled_vocab:
    ontologies: []
    terms: []
  expected_type:
  - Thing
  marginality: Recommended
  name: isMentionedIn
  sdo_desc: CretiveWork, Dataset, collection mentioning this entity  Inverse of:mentions
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab:
    ontologies: []
    terms: []
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
  controlled_vocab:
    ontologies: []
    terms: []
  expected_type:
  - PropertyValue
  marginality: Optional
  name: additionalProperty
  sdo_desc: A property-value pair representing an additional characteristics of the
    entitity, e.g. a product feature or another characteristic for which there is
    no matching property in schema.org.
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab:
    ontologies: []
    terms: []
  expected_type:
  - DataDownload
  marginality: Optional
  name: distribution
  sdo_desc: A downloadable form of this entity, at a specific location, in a specific
    format
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab:
    ontologies: []
    terms: []
  expected_type:
  - Place
  marginality: Optional
  name: location
  sdo_desc: Position where this entity is located or originates from (e.g. an entity
    from Polynesia islands or an Anatomical location. If multiple locations with multiple
    purposes (collection, storage) should be modelled, please use the additionalProperty
    from Place to specify this.
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab:
    ontologies: []
    terms: []
  expected_type:
  - Text
  - URL
  - PropertyValue
  marginality: Optional
  name: measurementTechnique
  sdo_desc: To describe the process used to obtain a biological entity or which is
    associated with that entity (i.e procedure to obtain it or measure/characterise
    it)
parent_type: CreativeWork
spec_mapping_url: https://docs.google.com/spreadsheets/d/1h0-fgqnRe25-tVCmu2yWNQjthLzgkW4a1TVNMpCABlc/edit?usp=drivesdk
spec_type: Type
status: revision
subtitle: Bioschemas specification describing BiologicalEntity in the life-science
version: 0.0.1
---