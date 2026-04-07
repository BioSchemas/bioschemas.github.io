---
layout: post
title: "BH25DE report: On the path to machine-actionable training materials"
tags:
- BH25DE
- Preprint
- BioHackrXiv
---

The [4th BioHackathon Germany](https://www.denbi.de/de-nbi-events/1840-4th-biohackathon-germany) took place from 1-5 December 2025 in Walsrode, Germany, organised by de.NBI and ELIXIR Germany. Life scientists, data managers, software developers and project leaders attended the hybrid event to work together on open source code, standards and infrastructure to advance research data practices and tools.

![Colourful umbrellas mounted the ceiling as art.](/images/umbrellas.jpg)
<small>BioHackathon Germany was hosted at the ANDERS Hotel Walsrode.</small>

## Making FAIRer access to training registries and learning paths across domains

The hackathon project titled [On the path to machine-actionable training materials](https://osf.io/preprints/biohackrxiv/un6cd_v1) was led by Nick Juty (University of Manchester) and Petra Steiner (Technical University of Darmstadt). The lead author of the project report was Phil Reed (University of Manchester).

The project operated across three interrelated streams: metadata interoperability, material analysis, and the definition and representation of learning paths in a machine readable manner.

- Content federation was demonstrated via the [mTeSS-X](https://elixirtess.github.io/mTeSS-X/) platform, enabling cross-instance exchange and preparing for future integration with the EOSC federation. To enhance interoperability, relevant ontologies and crosswalks were curated between established metadata models, specifically MoDALIA and Schema.org/Bioschemas. These mappings were implemented within the open-source OERbservatory Python package, providing a facility for exchanging data between platforms such as DALIA and TeSS.
- For material analysis, Large Language Models (LLMs) were utilised and vectorisation techniques were explored to calculate similarity, allowing for the identification of related materials and the potential for future deduplication of records across registries.
- To address the lack of machine-actionable trajectories across related or sequential materials, new Bioschemas profiles were proposed, specifically for learning paths. This model was validated using SPARQL queries on knowledge graphs derived from real-world examples like the Galaxy Training Network.

Such advancements provide a foundation for automated path generation and improved discoverability within training catalogues, and serves as a use case and strategy with broader applicability beyond those materials.

* [Read more in the project report in BioHackrXiv (doi:10.37044/osf.io/un6cd_v1)](https://doi.org/10.37044/osf.io/un6cd_v1)
