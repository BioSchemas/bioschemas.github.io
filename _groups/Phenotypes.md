---
layout: group-details
identifier: phenotypes
name: Phenotypes
collection: groups
active: true
type: biological
description: Specification for phenotype profile
lead: [CarlosHorro]
issues: https://github.com/BioSchemas/bioschemas/labels/type%3A%20phenotypes
folder:

# Progress status
usecase:
crosswalk:
#spec-versions: [
#  [{"spec-num": "0.1", "spec-url": "https://docs.google.com/document/d/1kQE3lixvBjBiZ8X3I1Mi44c3dcdgf4SshoGdNX5-_TE"}]#,
  #[{"spec-num": "0.2", "spec-url": "https://docs.google.com/document/d/1fn-of4cxGJLYiw1G3-KepZsIE0Ptq4GSx-h3jPmvdvc"}]
#]
test: false
adoption: false
applications: false

# Page attributes
abstract: 'Information of phenotypes is scattered in multiple and disperse samples data repositories.
Not all the phenotype data repositories have a programmatic interface and the existing variety of programmatic interfaces are diverse and changeable.'
objectives:
  [
    'Relay on the metadata description defined by the ELIXIR plant use case',
    'Automate the ingestion of sample metadata from phenotype data repositories into registries via Bioschemas.',
    'Engage and help data providers to test and adopt the exposure of phenotype metadata with Schema.org via Bioschemas.',
    'Make registries like TransPlant compliant with Schema.org via Bioschemas.',
    'Focus on plant phenotypes but consider a general definition of phenotype taking into account different types of phenotypes. eg. biomedical phenotypes, mouse phenotypes, ...'
  ]

members:
    - PhilippeRocca-Serra
    - CarlosHorro
    - AndraWaagmeester
---
