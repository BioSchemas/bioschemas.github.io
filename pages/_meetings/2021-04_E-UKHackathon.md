---
layout: meeting
name: ELIXIR-UK Hackathon
title: ELIXIR-UK Hackathon
dates: 14-16 April 2021
start_date: 2021-04-14
end_date: 2021-04-16
venue: Virtual
meeting-name: ELIXIR-UK Hackathon
meeting-url: https://elixiruknode.org/uncategorized/second-elixir-uk-biohackathon/
agenda-doc: https://docs.google.com/document/d/1EkVy-zQH0zdHbkI8OzzRYjkFmgtup-0DKAVX2hvJf4M/
contact-people:
    - AlasdairGray
attendees:
    - AlasdairGray
    - AlanWilliams
    - ChrisChild
    - StianSoiland-Reyes
    - StuartOwen
---

__Aim:__
> We will work on collaborations around ELIXIR-UK services and projects. The event will be centered on collaborations across our existing services and projects such as Bioschemas, FAIRSharing, Galaxy, InterMine, ISAtools, Jalview, KnetMiner, RDMKit, TeSS, WorkflowHub and more.

The Bioschemas activities will centre around the projects detailed below. Notes from these projects can be found [here](https://docs.google.com/document/d/1BUmzzu5W1HUkMj8QsnIzZRfDIqchWHSf3FwShX6wiVM/edit#heading=h.qz4i2asiirvb).

### Bioschemas Live Deployments
__Project details:__ The Bioschemas [live deploys page](https://bioschemas.org/liveDeploys/) lists the deployments known to the Bioschemas community. Currently the data for the page is represented in YAML and is page type oriented rather than resource oriented. This means that there is a lot of repeated information, e.g. resource name, URL, node, and also that the count of the number of marked up resources is inaccurate.

This project would migrate the data to a JSON representation and update the webpages that display the content of the data. The data fields should be extended to include the resource sitemap, and possibly hints about the deployment technology (e.g. Single page application) that can make consuming the content easier. It should also provide a mechanism to allow for new deployments to be more easily registered.
The outcome should enable easier consumption of the list of live deploys by aggregators such as FAIRsharing.

### UK Bioschemas Knowledge Graph: Scrape markup deployment and make available for exploitation

__Project details:__ The promise of Bioschemas is that it makes consuming data from multiple resources more straightforward. This project would explore scraping some of the known Bioschemas deployments, aligning the page centric markup to concept oriented, and deploy these in a triplestore for further exploration.

As the project progresses, we can verify that the existing tutorials are sufficient to support developers to deploy their markup.

### Bioschemas infrastructure for profile development

__Project details:__ Bioschemas [profiles](https://bioschemas.org/profiles/) are community recommendations specifying the Schema.org properties to use for describing a particular type of resource. Profiles are currently developed in GSheets and then converted to YAML for display on the Bioschemas website using GoWeb. We’d like to move to a more machine readable format for the profiles, such as JSON-Schema or ShEx, with the canonical form of the profile being the GitHub version rather than the GSheet. Some initial requirements for the infrastructure have been identified, but two crucial elements are that the format should be machine processable and that it should be editable by non-technical users. We would also like to more closely align the profiles with their underlying Schema.org type. Some [initial work](https://github.com/BioSchemas/ProfileGenerator) has been done in this regard.

One possibility for the non-technical user interface could be [JSONschema.net](https://jsonschema.net/). We would need to see how this can be integrated with GitHub.

We would also like to explore the use of GitHub actions to verify the correctness of the markup within the profiles to provide a level of validation for deployment.

### Extending Bioschemas to Agri-food applications

__Project details:__ This is based on some draft [work that has already been done](https://github.com/Rothamsted/agri-schemas/tree/master/drafts/201904-dfw-hackathon) to use Bioschemas in the domain of plant biology, agriculture and food, and extend its types or profiles where necessary. Possible activities for the hackathon might be: reviewing the draft modelling that has already been done, considering new use cases (eg, BrAPI/MIAPPE, WheatIS, PHI-BASE), converting real datasets.

### RO-Crate, Bioschemas, WorkflowHub, Common Workflow Language (Stian Soiland-Reyes, Stuart Owen)

__Project details:__ [RO-Crate](https://www.researchobject.org/ro-crate/) is a community-led set of recommendations for packaging research output as Research Objects with rich metadata, based on schema.org. [WorkflowHub.eu](https://www.researchobject.org/ro-crate/) is a registry of computational workflow for life sciences, agnostic to workflow languages and platforms. It [uses RO-Crate](https://www.researchobject.org/ro-crate/) as packaging of workflows with their metadata, for import, export and publishing, and entry pages in the WorkflowHub is annotated with [Bioschemas](https://bioschemas.org/) markup, including the new [ComputationalWorkflow profile](https://bioschemas.org/profiles/ComputationalWorkflow/) now being aligned with the [ComputationalTool profile](https://bioschemas.org/profiles/ComputationalTool/). The WorkflowHub currently exposes the packaged RO-Crate as a single downloadable zip file.

Goals of the project:

1. Adding an RO-Crate preview page to the WorkflowHub,  which will include [Bioschemas Dataset](https://bioschemas.org/profiles/Dataset/) JSON-LD markup exposed for Google Dataset search. May use [GA4GH TRS API](https://about.workflowhub.eu/TRS/), already used for UseGalaxy.* integration.
1. The RO-Crate preview page and JSON-LD will be made available as separate Web resources, linked from the Workflow entry page
1. The RO-Crate preview page will also include and visual overview of the RO-Crate package, and the ability to browse and download individual components (e.g. using [makehtml](https://www.npmjs.com/package/ro-crate))
1. Test and improve prototype RO-Crate validator https://github.com/KockataEPich/CheckMyCrate of Workflow RO-Crate profile
  1. Implement more of Marc Portier’s [thoughts on RO-Crate profiles](https://bit.ly/ro-crate-profiles-brainstorm)
  1. See https://www.researchobject.org/ro-crate/profiles.html
