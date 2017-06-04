---
layout: group-details
id: data
name: Data
path: data.html
collection: groups
active: true
type: generic
description: Specification for data
lead: [SusannaSansone]
issues: https://github.com/BioSchemas/bioschemas/labels/type%3A%20data
folder:

# Progress status
usecase:
crosswalk: https://docs.google.com/spreadsheets/d/1XzrZxFIuG3TS9RU8vACoUjAvaADLmI_FrIk7O3BEkxY/edit#gid=0
spec-num: 0.1
spec-url: https://docs.google.com/document/d/1klUdYkCK-7YmbfKv2FNvBIOXZ1Pq9EhxvjceO7gWzfQ/edit#heading=h.esim87b96w1t
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
---
