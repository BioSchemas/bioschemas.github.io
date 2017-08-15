---
description: 'An experimental protocol is a sequence of tasks and operations executed
  to perform experimental research in biological and biomedical areas.

  Experimental protocols are fundamental information structures that support the description
  of the processes by means of which results are generated in experimental research
  [1]. Experimental protocols describe how the data were produced, the steps undertaken
  and conditions under which these steps were carried out.

  [1]  Giraldo, O., Garcia, A., Corcho, O.: SMART Protocols: SeMAntic RepresenTation
  for Experimental Protocols, Riva del Garda, Trentino, Italy (2014). 4th Workshop
  on Linked Science 2014- Making Sense Out of Data (LISC2014)

  '
layout: new_spec_detail
name: LabProtocol
new_bsc:
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab: ''
  domain: LabProtocol
  domain_case: new_bsc
  expected_type:
  - Text
  marginality: Recommended
  name: advantage
  sdo_desc: It should be made clear in which situations the Protocol has been successfully
    employed.
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab: ''
  domain: LabProtocol
  domain_case: new_bsc
  expected_type:
  - Text
  marginality: Recommended
  name: limitation
  sdo_desc: It should be made clear in which situations the Protocol would be unreliable
    or otherwise unsuccessful.
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab: ''
  domain: LabProtocol
  domain_case: new_bsc
  expected_type:
  - Text
  marginality: Recommended
  name: applicability
  sdo_desc: Applications of the protocol list the full diversity of the applications
    of the method and support if is possible to extend the range of applications of
    the protocol. e.g. northern blot assays, sequencing, etc.
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab: ''
  domain: LabProtocol
  domain_case: new_bsc
  expected_type:
  - BiologicalEntity (chemicals)
  - URL
  marginality: Minimum
  name: reagent
  sdo_desc: Reagents participating in the list. ChEBI and PubChem entities can be
    used whenever available. Commercial names are also acceptable (URL if possible)
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab: ''
  domain: invalid domain type
  domain_case: new_bsc
  expected_type:
  - Thing
  marginality: Recommended
  name: isMentionedIn
  sdo_desc: CretiveWork, Dataset, collection mentioning this entity  Inverse of:mentions
new_sdo: []
reu_bsc:
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab: ''
  domain: Product/Service
  domain_case: reu_bsc
  expected_type:
  - Text
  marginality: Recommended
  name: category
  sdo_desc: A category for the item. Greater signs or slashes can be used to informally
    indicate a category hierarchy.
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab: ''
  domain: BiologicalEntity
  domain_case: reu_bsc
  expected_type:
  - BiologicalEntity
  - URL
  marginality: Minimum
  name: sample
  sdo_desc: Samples used in the protocol
reu_sdo:
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab: ''
  domain: MedicalDevice
  domain_case: reu_sdo
  expected_type:
  - Text
  marginality: Minimum
  name: purpose
  sdo_desc: A goal towards an action is taken. Can be concrete or abstract.
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab: ''
  domain: MedicalStudy
  domain_case: reu_sdo
  expected_type:
  - Text
  marginality: Recommended
  name: outcome
  sdo_desc: outcome or expected result by a protocol execution.
- bsc_dec: ''
  cardinality: ONE
  controlled_vocab: ''
  domain: CreativeWork
  domain_case: reu_sdo
  expected_type:
  - PropertyValue, Text, URL
  marginality: Minimum
  name: identifier
  sdo_desc: The identifier property represents any kind of identifier for any kind
    of Thing, such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated
    properties for representing many of these, either as textual strings or as URL
    (URI) links. See background notes for more details.
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
  - CreativeWork
  - URL
  marginality: Minimum
  name: license
  sdo_desc: A license document that applies to this content, typically indicated by
    URL.
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab: ''
  domain: CreativeWork
  domain_case: reu_sdo
  expected_type:
  - CreativeWork
  - URL
  marginality: Recommended
  name: isBasedOn
  sdo_desc: A resource that was used in the creation of this resource. This term can
    be repeated for multiple sources. For example, http://example.com/great-multiplication-intro.html.
    Supersedes isBasedOnUrl.
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab: ''
  domain: SoftwareApplication
  domain_case: reu_sdo
  expected_type:
  - Text
  - URL
  marginality: Minimum
  name: device
  sdo_desc: Device required to run the application. Used in cases where a specific
    make/model is required to run the application.  For LabProtocols it would be a
    laboratory equipment.
- bsc_dec: ''
  cardinality: MANY
  controlled_vocab: ''
  domain: EntryPoint
  domain_case: reu_sdo
  expected_type:
  - SoftwareApplication
  marginality: Recommended
  name: actionApplication
  sdo_desc: An application that can complete the request.
- bsc_dec: ''
  cardinality: ONE
  controlled_vocab: ''
  domain: Event
  domain_case: reu_sdo
  expected_type:
  - Duration
  marginality: Recommended
  name: duration
  sdo_desc: The time it takes to actually carry on the protocol, in ISO 8601 duration
    format.
version: 0.0.1
---