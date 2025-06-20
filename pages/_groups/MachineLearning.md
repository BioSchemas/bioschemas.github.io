---
layout: group-details
identifier: machinelearning
name: Machine Learning
collection: groups
active: true
type: generic
description: Specification for digital objects commonly used in machine learning solutions.
lead: 
  - person: LeylaGarcia
  - person: FotisPsomopoulos
  - person: DanSKatz
email: enquiries@bioschemas.org
issues: https://github.com/BioSchemas/specifications/labels/group%3AMachineLearning
folder: https://drive.google.com/drive/folders/1NGiDfc6WSCJNDheGhYApfEVN3-X6Uj6z?usp=sharing

# Page attributes
abstract: 'Machine Learning combines data, software, models and workflows. There is a need to harmonize and connect those different elements to have a full picture of a Machine Learning approach from the metadata perspective.'
objectives:
  [
    'Describe training datasets including characterization of features and attributes that can be used for training (e.g., number of data points, classes, target variable).',
    'Describe software used for training purposes including elements related to the optimization process.',
    'Describe ML models together with their evaluation.',
    'Describe links among the different elements involved in ML approaches clearly and explicitly.'
  ]

specifications:
  [
    'Dataset', 'ComputationalTool'
  ]


members:
- AlbanGaignard
- DietrichRebholzSchuhmann
- IvanMicetic

breadcrumb:
  link1: /community/
  title1: Community
  link2: /groups/
  title2: Groups
---

<h2>Further Details</h2>

<p>Machine Learning (ML) is nowadays a common path in data-driven research due to the amount of available data and the resources needed to process it and make sense out of it. In addition to data, software also plays and important role in ML. Models produced by an ML training process also become a thing on their own, a thing that could be seen as similar to software (e.g., prediction model that can be executed with some input and produce a prediction as output) or to data (e.g., clusters emerged from a clustering approach). Furthermore, the training software has to be tuned and optimized while the model has to be evaluted, either intrinsic or extrinsically. Ideally, all of this information should be reported and represented as metadata of the ML process. However, this is not always the case. This group, a joint effort across <a href="https://www.rd-alliance.org/groups/fair-machine-learning-fair4ml-ig" target="_blank">Research Data Alliance FAIR4ML Interest Group</a>, <a href="https://elixir-europe.org/focus-groups/machine-learning" target="_blank">ELIXIR Machine Learning Focus Group</a> and <a href="https://www.nfdi4datascience.de/" target="_blank">NFDI4DataScience</a>, aims at providing a common ground for the metadata necessary to describe ML approaches. </p>

<p>To achieve its objectives, this group is using as a starting point <a href="https://research.google/pubs/pub48120/" target="_blank">Machine Learning Cards for models and datasets</a>. Other efforst will also be taken into account, e.g., <a href="https://www.nature.com/articles/s41592-021-01205-4" target="_blank">Data, Optimization, Model and Evaluation (DOME) recommendations</a>, <a href="https://doi.org/10.1038/s41592-021-01241-0" target="_blank">AIMe registry for artificial intelligence in biomedical research</a> and <a href="https://huggingface.co/" target="_blank">HuggingFace</a>.</p>
