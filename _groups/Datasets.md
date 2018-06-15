---
layout: group-details
identifier: data
name: Datasets
path: datasets.html
collection: groups
active: true
type: generic
description: Specification for Dataset
lead: [SusannaSansone]
issues: https://github.com/BioSchemas/bioschemas/labels/type%3A%20data
folder: https://drive.google.com/open?id=0B2tKthYRS0f5aEhkU1Q4aEE5TEU

# Progress status
usecase: https://docs.google.com/document/d/1klUdYkCK-7YmbfKv2FNvBIOXZ1Pq9EhxvjceO7gWzfQ/edit#heading=h.ngffjf4and1x
crosswalk: https://docs.google.com/spreadsheets/d/1XzrZxFIuG3TS9RU8vACoUjAvaADLmI_FrIk7O3BEkxY/edit#gid=0
spec-versions: [
  [{"spec-num": "0.1", "spec-url": "https://docs.google.com/document/d/1klUdYkCK-7YmbfKv2FNvBIOXZ1Pq9EhxvjceO7gWzfQ"}]#,
  #[{"spec-num": "0.2", "spec-url": "https://docs.google.com/document/d/1fn-of4cxGJLYiw1G3-KepZsIE0Ptq4GSx-h3jPmvdvc"}]
]
test: false
adoption: false
applications: false

# Page attributes
abstract: 'Most dataset repositories and registries of dataset do not provide structured data easily crawlable by search engines.
Registries like DataMed, OMICsDI and BioSamples do automated ingestion of content mainly through APIs but not all the data repositories have a programmatic interface and the existing variety of programmatic interfaces are subject to changes which break integration workflows.'
objectives:
  [
    'Facilitate the ingestion of datasets metadata from data repositories (databases) into search engines and dataset registries like OMICsDI and DataMed via Bioschemas',
    'Automate the linking of datasets metadata to samples in dataset registries like Biosamples, and identify cases where samples are missing or metadata is absent.',
    'Engage and help data providers to test and adopt the exposure of dataset metadata Bioschemas',
    'Contribute to increase the number of indexed data repositories via Bioschemas.',
    'Make dataset registries compliant with Bioschemas.'
  ]

specifications:
  [
    'Dataset', 'DataRecord'
  ]

members:
  - NiallBeard
  - PhilippeRocca-Serra
  - SusheelVarma
  - LizWilliams
  - SusannaSansone
  - AnilWipat
  - PeterMcQuilton
  - GianluigiZanetti
  - EthyCannon
  - VickySchneider
  - AndraWaagmeester
  - HeimoMüller
  - JustinClark-Casey
  - MorrisSwertz
  - saqibmir
  - AnkitKumarLohani
  - DanTimmons
  - AlejandraGonzalez-Beltran
  - GuillermoCalderonMantilla
  - AlasdairGray
  - JeffreyGrethe
  - KaisaSilander
  - CaroleGoble
  - PetrHolub
  - GosMicklem
  - MichelDumontier
  - NicolasLeNovère
  - anyango
  - HaydeeArtaza
  - DavidvanEnckevort


---
