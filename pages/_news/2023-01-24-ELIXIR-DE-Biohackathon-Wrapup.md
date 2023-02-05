---
layout: post
title: "ELIXIR-DE BioHackathon Wrapup"
tags:
- Community
---
In December the first BioHackathon Germany was organised by the team of the German ELIXIR node. Leyla Jael Garcia-Castro (ZBMed and NFDI4Microbiota) and Steffen Neumann (IPB Halle and NFDI4Chem) used the opportunity and successfully submitted a proposal on (Bio)Schemas4NFDI.

Aim of the workshop was to bring together metadata experts from Bioschemas and several NFDI consortia (see here for [all consortia](https://www.nfdi.de/consortia/?lang=en) in NFDI) to adopt and adapt Bioschemas to NFDI use cases. We had participants from, e.g., NFDI4DataScience, GHGA, NFDI4Microbiota, and seven participants from NFDI4Chem.

Actual Hacking was divided into the *Data Provider Department*, where we were improving the number of supporting ressources, and the coverage of schema metadata provided. There were also discussions on a [LinkML](https://linkml.io/) representation for Bioschemas, with a crosswalk spreadsheet between GHGA’s metadata, Bioschemas and corresponding LinkML yaml schemas with “exact_mapping” elements. People also developed [prototype LinkML code](https://github.com/deNBI/biohackathon-2022/tree/main/projects/bioschemas4nfdi/linkml-crosswalk) for the translation from YAML to JSON-LD. In the *New & Improved Schemas Department* we worked on improving the analytical DataSet, and the new chemical reaction type. The *Querying / Harvesting / Exploitation Department* had participants from IPB and TIB, and were actually working to make all that metadata useful for you. We were successful in fetching data from BioSchema providers (MassBank) via the OAI-PMH prototype [oai4schemas](https://github.com/NFDI4Chem/oai4schemas) and gathering them into the [NFDI4Chem Search service](https://search.nfdi4chem.de/). The presentation by Denitsa Eckweiler (TU Braunschweig) showed how PubPharm currently collects information useful in pharmaceutical chemistry, and we discussed how metadata on chemical data could be included in the future.

Other projects in the Hackathon which touched Bioschemas were
working towards FAIR Computational Metabolomics Workflows and improving provenance collection through provenance libraries in R Script [rdtLite](https://cran.r-project.org/package=rdtLite) and Python Script [provenance](https://provenance.readthedocs.io/) to export “inner” provenance of scripts. The plant community worked to improve markup in the [e!Dal](https://edal.ipk-gatersleben.de/) repository.

Finally, you are currently reading the output from the *Dissemination & Outreach Department*, with more to come. We will contribute our experience to the NFDI Section Metadata, and if things work out, you’ll see more in 2023 maybe at NFDI’s own metadata hackathon or the [Conference on Research Data Infrastructure CoRDI 2023](https://www.nfdi.de/cordi-2023/?lang=en) in September in Karlsruhe.

There are also some [Tweets about the Hackathon](https://twitter.com/hashtag/BHG_2022?src=hashtag_click) by de.NBI team including some pictures.
