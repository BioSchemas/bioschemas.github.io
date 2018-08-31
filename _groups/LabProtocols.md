---
layout: group-details
identifier: labprotocols
name: Laboratory Protocols
collection: groups
active: true
type: generic
description: Specification for biological laboratory protocol Type
lead:
    - OlgaXimenaGiraldo
    - AlexanderGarcia
issues: https://github.com/BioSchemas/bioschemas/labels/type%3A%20labprotocols
folder: https://drive.google.com/drive/folders/0B0fE3oOZIq44TzFwejFEbE9WdXM

# Progress status
usecase: https://docs.google.com/document/d/1EZ_U2u2aJH_ERsoecaJRAJkWVHYGU2SK8HYSjvhEaMM/
crosswalk: https://docs.google.com/spreadsheets/d/1julB0P6kjXK_mL2dU8EDU9zMxIMah0_dYYeGt2Spllo/
spec-versions: [
  [{"spec-num": "0.1", "spec-url": "https://docs.google.com/document/d/1y3UQgdixhuVlZZ5hN0xwhqgOI-2HdDOkRzRkmQ7Hkxo/"}]#,
  #[{"spec-num": "0.2", "spec-url": "https://docs.google.com/document/d/1fn-of4cxGJLYiw1G3-KepZsIE0Ptq4GSx-h3jPmvdvc"}]
]
test: false
adoption: false
applications: false

# Page attributes
abstract: 'In schema.org we cannot find life science types (eg. protein, gene, biological pathway) except those types that overlap with healthcare and medicine domains defined by the health schema.org extension (eg. drug, artery). These life science types share many elements which can be captured in a common biological entity type.'
objectives:
  [
    'Describe biological laboratory protocols using Bioschemas compliant markup so protocols can be more easily indexed by search engines and registries.',
    'Evaluating the issues and benefits about how to work with laboratory protocols in schema.org and Bioschemas'
  ]

types:
    [
      'LabProtocol'
    ]

members:
    - OlgaXimenaGiraldo
    - AlexanderGarcia
    - FedericoLópezGómez
    - LeylaGarcia
    - GianluigiZanetti
    - AndraWaagmeester
    - HeimoMüller
    - MorrisSwertz
    - KaisaSilander
    - PetrHolub
    - DavidvanEnckevort
---
