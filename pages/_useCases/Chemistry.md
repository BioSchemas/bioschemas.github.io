---
layout: use-case
name: Chemistry Data
group: chemicals
active: true
---

Finding information about chemicals is an open challenge. There are plenty of databases that have been collecting properties in central places, but at the same time there is a long list of databases and smaller and larger website with essential information about these chemicals, their properties, their use cases, that are not currently systematically aggregated. Bioschemas is the door to the long tail of chemical information, opening niche databases and overviews of chemical information found on websites. The `MolecularEntity` and `ChemicalSubstance` profiles will allow us to recognize chemical information.

The `MolecularEntity` profile should support data discovery using standard features such as its name, both informal and IUPAC standardised name, formula, and structure using representations such as InChI, InChIKey, and SMILES. When distinguishing between search results, it is helpful to have information such as the molecuar weight and any known connections to reacation, diseases, and roles played for example as a drug.

The `ChemicalSubstance` profile should support data discovery using standard features such as its name and chemical composition.

For both profiles, when distinguishing between search results, it is helpful to have additional information returned such as the molecuar weight for `MolecularEntity`, known associations with diseases, e.g. known to be used in a drug for specific conditions, and any known roles when processed in the body.

A typical search question would be:

> Alice is looking for data about ‘3-(2-aminoethyl)-1H-indol-5-ol, 5-Hydroxytryptamine’. She would like to search either by name or InChI/SMILES. In the response, she would like data about diseases for which the compound is used.

### Adoption

The `ChemicalSubstance` profile, for example, is starting to be adopted by projects from the NanoSafety Cluster (NSC) and associated with the ELIXIR Toxicology Community being established. Using website scraping, information about nanomaterials will be collected and made available in the NSC databases.
