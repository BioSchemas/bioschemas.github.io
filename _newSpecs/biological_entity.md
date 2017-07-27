---
layout: new_spec_detail
name: Biological Entity
version: 0.0.1
description: The BiologicalEntity aims to encompasses as much as possible biological types such as  "samples”,  "protein”,  "protein annotation”,  "protein structure”,  "phenotype” and so on. Most of the properties here will be optional as the specific profiles, i.e., a tailored usage of BiologicalEntitty, will provide stronger requirements whenever needed.
bsc_desc:
spec_doc: https://drive.google.com/open?id=1XASuESIHU3bi1aXMxQS5-rCOQX0ugjMNkh68VF4co4Q
spec_mapping: https://drive.google.com/open?id=1h0-fgqnRe25-tVCmu2yWNQjthLzgkW4a1TVNMpCABlc
new_bsc:
    - name: associatedDisease
      expected_type: MedicalCondition OR URL
      sdo_desc: Disease associated to this protein feature
      bsc_dec: 
      marginality: Optional
      cardinality: MANY
      controlled_vocab: 
      domain: BiologicalEntity
      domain_case: new_bsc
    - name: biocoordinates
      expected_type: QuantitativeValue
      sdo_desc: Coordinates in a 1 or 2D space, for instance length/coordinates in a sequence.  Usage  example  Use a QuantitativeValue with properties minValue and maxValue for a region or value for a site in a Protein. Use it only with value for a protein length.
      bsc_dec: 
      marginality: Optional
      cardinality: MANY
      controlled_vocab: 
      domain: BiologicalEntity
      domain_case: new_bsc
    - name: biologicalType
      expected_type: Text
      sdo_desc: List with types preferably supported by BioSchemas-> enumeration list of values maintained on a wikipage (cf accessibilityAPI in schema.org for implementation). If the value is not on the list then the data will still be parsed but only generic properties will be validated. {population,individual,tissue,cell,molecule,protein,nucleic acid}
      bsc_dec: 
      marginality: Minimum
      cardinality: MANY
      controlled_vocab: 
      domain: BiologicalEntity
      domain_case: new_bsc
    - name: crossReference
      expected_type: Thing
      sdo_desc: A pointer to another, somehow related entity. Usage  Whenever isBasedOn/isBasisFor, isPartOf/hasPart, citation or any other more specific does not work.
      bsc_dec: 
      marginality: Optional
      cardinality: MANY
      controlled_vocab: 
      domain: BiologicalEntity
      domain_case: new_bsc
    - name: isBasisFor
      expected_type: CreativeWork or   URL or BiologicalEntity
      sdo_desc: A resource for which this resource has been used for the creation of the former.  Inverse property  isBasedOn
      bsc_dec: 
      marginality: Optional
      cardinality: MANY
      controlled_vocab: 
      domain: BiologicalEntity
      domain_case: new_bsc
    - name: phenotype
      expected_type: Text, Url, PropertyValue
      sdo_desc: To associate a biological entity to phenotypic information, whether the entity presents the phenotype or causes it.
      bsc_dec: 
      marginality: Optional
      cardinality: MANY
      controlled_vocab: 
      domain: BiologicalEntity
      domain_case: new_bsc
    - name: representation
      expected_type: Text or URL or PropertyValue
      sdo_desc: Representation of this entity. For instance, chemical structure or sequence
      bsc_dec: 
      marginality: Optional
      cardinality: MANY
      controlled_vocab: 
      domain: BiologicalEntity
      domain_case: new_bsc
    - name: sample
      expected_type: BiologicalEntity or URL
      sdo_desc:   Clarify usage... 
      bsc_dec: 
      marginality: Optional
      cardinality: MANY
      controlled_vocab: 
      domain: BiologicalEntity
      domain_case: new_bsc
    - name: taxon
      expected_type: URL 
      sdo_desc:   A url pointing to NCBI Taxonomy or a taxonomic resource 
      bsc_dec: 
      marginality: Optional
      cardinality: MANY
      controlled_vocab: Yes
      domain: BiologicalEntity
      domain_case: new_bsc
new_sdo:
    - name: isMentionedIn
      expected_type: Thing
      sdo_desc: CretiveWork, Dataset, collection mentioning this entity  Inverse of  mentions
      bsc_dec: Additional Description for BioSchemas
      marginality: Recommended
      cardinality: ONE
      controlled_vocab: list of types or list of ontologies
      domain: Thing
reu_bsc:
    - name: citation
      expected_type: CreativeWork or URL
      sdo_desc: A citation or reference to a creative work, such as a publication, web page, scholarly article, etc.
      bsc_dec: 
      marginality: Recommended
      cardinality: MANY
      controlled_vocab: 
      domain: BiologicalEntity
      domain_case: reu_bsc
    - name: dateCreated
      expected_type: Date or DateTime
      sdo_desc: The date on which the BiologicalEntity was created or the item was added to a DataFeed.
      bsc_dec: 
      marginality: Optional
      cardinality: ONE
      controlled_vocab: 
      domain: BiologicalEntity
      domain_case: reu_bsc
    - name: dateModified
      expected_type: Date or   DateTime
      sdo_desc: The date on which the BiologicalEntity was most recently modified or when the item's entry was modified within a DataFeed.
      bsc_dec: 
      marginality: Optional
      cardinality: ONE
      controlled_vocab: 
      domain: BiologicalEntity
      domain_case: reu_bsc
    - name: datePublished
      expected_type: Date
      sdo_desc: Date of first broadcast/publication.
      bsc_dec: 
      marginality: Optional
      cardinality: ONE
      controlled_vocab: 
      domain: BiologicalEntity
      domain_case: reu_bsc
    - name: distribution
      expected_type: DataDownload
      sdo_desc: "A downloadable form of this entity, at a specific location, in a specific format"
      bsc_dec: 
      marginality: Optional
      cardinality: MANY
      controlled_vocab: 
      domain: BiologicalEntity
      domain_case: reu_bsc
    - name: hasPart
      expected_type: BiologicalEntity
      sdo_desc: "Indicates a BiologicalEntity that is (in some sense) a part of this BiologicalEntity. Inverse property: isPartOf."
      bsc_dec: 
      marginality: Optional
      cardinality: MANY
      controlled_vocab: 
      domain: BiologicalEntity
      domain_case: reu_bsc
    - name: isBasedOn
      expected_type: CreativeWork or URL or BiologicalEntity
      sdo_desc: "A resource that was used in the creation of this resource. This term can be repeated for multiple sources. For example, http://example.com/great-multiplication-intro.html. Supersedes isBasedOnUrl."
      bsc_dec: 
      marginality: Optional
      cardinality: MANY
      controlled_vocab: 
      domain: BiologicalEntity
      domain_case: reu_bsc
    - name: isPartOf
      expected_type: BiologicalEntity
      sdo_desc: "Indicates a BiologicalEntity that this BiologicalEntity is (in some sense) part of.  Inverse property: hasPart."
      bsc_dec: 
      marginality: Optional
      cardinality: MANY
      controlled_vocab: 
      domain: BiologicalEntity
      domain_case: reu_bsc
    - name: location
      expected_type: Place
      sdo_desc:  "Position where this entity is located or originates from (e.g. an entity from Polynesia islands or an Anatomical location. If multiple locations with multiple purposes (collection, storage) should be modelled, please use the additionalProperty from Place to specify this."
      bsc_dec: 
      marginality: Optional
      cardinality: MANY
      controlled_vocab: 
      domain: BiologicalEntity
      domain_case: reu_bsc
    - name: measurementTechnique
      expected_type: Text, url, PropertyValue
      sdo_desc: "To describe the process used to obtain a biological entity or which is associated with that entity (i.e procedure to obtain it or measure/characterise it)"
      bsc_dec: 
      marginality: Optional
      cardinality: MANY
      controlled_vocab: 
      domain: BiologicalEntity
      domain_case: reu_bsc
reu_sdo:
    - name: additionalProperty
      expected_type: PropertyValue
      sdo_desc: "A property-value pair representing an additional characteristics of the entitity, e.g. a product feature or another characteristic for which there is no matching property in schema.org."
      bsc_dec: 
      marginality: Optional
      cardinality: MANY
      controlled_vocab: 
      domain: Thing
      domain_case: reu_sdo
    - name: alternateName
      expected_type: Text
      sdo_desc: An alias for the item.
      bsc_dec: 
      marginality: Recommended
      cardinality: MANY
      controlled_vocab: 
      domain: Thing
      domain_case: reu_sdo
    - name: description
      expected_type: Text
      sdo_desc: A description of the item.
      bsc_dec: 
      marginality: Recommended
      cardinality: ONE
      controlled_vocab: 
      domain: Thing
      domain_case: reu_sdo
    - name: identifier
      expected_type: PropertyValue or   Text or   URL
      sdo_desc: "The identifier property represents any kind of identifier for any kind of Thing, such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See background notes for more details. Recommendation: identifiers.org whenever possible"
      bsc_dec: 
      marginality: Minimum
      cardinality: ONE
      controlled_vocab: 
      domain: Thing
      domain_case: reu_sdo
    - name: image
      expected_type: ImageObject or   URL
      sdo_desc: An image of the item. This can be a URL or a fully described ImageObject.
      bsc_dec: 
      marginality: Optional
      cardinality: MANY
      controlled_vocab: 
      domain: Thing
      domain_case: reu_sdo
    - name: name
      expected_type: Text
      sdo_desc: The name of the item.
      bsc_dec: 
      marginality: Recommended
      cardinality: ONE
      controlled_vocab: 
      domain: Thing
      domain_case: reu_sdo
    - name: sameAs
      expected_type: URL
      sdo_desc: "URL of a reference Web page that unambiguously indicates the item's identity. E.g. the URL of the item's Wikipedia page, Wikidata entry, or official website."
      bsc_dec: 
      marginality: Optional
      cardinality: MANY
      controlled_vocab: 
      domain: Thing
      domain_case: reu_sdo
    - name: url
      expected_type: URL
      sdo_desc: "URL of the item."
      bsc_dec: 
      marginality: Optional
      cardinality: ONE
      controlled_vocab: 
      domain: Thing
      domain_case: reu_sdo
---
