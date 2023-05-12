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
- person: 
email: enquiries@bioschemas.org
issues: 'https://github.com/Bioschemas/bioschemas/issues?q=is%3Aopen+label:"type:%20Datase","type:%20tool"'
folder: 

# Page attributes
abstract: 'Machine Learning combines data, software, models and possibly workflows. There is a need to harmonize and connect those different elements to have a full picture of a Machine Learning approach.'
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

---

<h2>Further Details</h2>

<p>Machine Learning (ML) are nowadays a common path in data-driven research due to the amount of available data and the resources needed to process it and make sense out of it. In addition to data, software also plays and important role in ML. Models produced by an ML training process also become a thing on their own, a thing that could be seen as similar to software (e.g., prediction model that can be executed with some input and produce a prediction as output) or to data (e.g., clusters emerged from a clustering approach). Furthermore, the training software has to be tuned and optimized while the model has to be evaluted, either intrinsic or extrinsic. Ideally, all of this information should be reported and represented as metadata of the ML process. However, this is not always the case. This group, a joint effort across Research Data Alliance FAIR4ML Interest Group, ELIXIR Machine Learning Focus Group and NFDI4DataScience,aims at providing a common ground for the metadata necessary to describe ML approaches. </p>

<p>To achieve its objectives, this group is using as a starting point the <a href="https://www.nature.com/articles/s41592-021-01205-4" target="_blank">Data, Optimization, Model and Evaluation (DOME) recommendations to report supervised machine learning in biology</a>. Other efforts related to metadata for ML will also taken into account, e.g. <a href="https://doi.org/10.1038/s41592-021-01241-0" target="_blank">AIMe registry for artificial intelligence in biomedical research</a>.</p>
