---
layout: use-case
name: Samples
group: samples
active: true
redirect_from: 
- "/useCases/Samples/"
- "/useCases/Samples"
---


### Use Cases

1.  Rare diseases biobanks should be able to crawl the BioSamples database to identify all the published (and searchable) datasets derived from samples they have provided.
2.  Public archives should be able to crawl rare disease Biobank websites, in order to identify samples that are known to have public accessions in the BioSamples database AND that are publically available, and thereby link public samples to a provider (“where can I get more of this sample?”).
3.  Public archives should be able to crawl rare disease Biobank websites, in order to identify sample metadata description.
4.  BioSamples database should be able to crawl manually curated high quality sample metadata available in repositories linked to BioSamples, like the MarRef database, and use that information to curate BioSamples

## Assumptions

1.  Each sample provided by a biobank has an identifier that is assigned by the biobank to identify a specific sample.
2.  Each sample reported in a public archive or used to generate a public dataset has a public, BioSamples database accession.
3.  Each sample provided in an external highly curated repository could have an identifier assigned by the repository itself.

Given these use cases and assumptions, we will use Bioschemas to describe sample links and retrieve curated information from different sources. The main challenge is therefore the identification of links between samples exposed in different repositories (Biobank, Curated repository and BioSamples) based on repository identifier. This is not always possible without considerable additional curation effort, but of the 5 million samples in the BioSamples database, over 4 million declare either a ‘synonym’, ‘sample source name’ or ‘source name’ attribute, frequently used to encode the original biobank sample name. Exposing these in a structured manner through the BioSamples database would allow Biobanks to crawl and analyse this content, marrying sample that are recognised with their own identifiers.

In those cases where a single sample entity is not exposable, like the BioBank Directory use case defined during the sample hackathon (meeting notes [here](https://docs.google.com/document/d/1xKFFLXcc6Db5wSuifOETpQSIFd73GLL2__2BNK9d4tk/edit#heading=h.aqwqtawny32k)), you should probably use a different Bioschemas profile/entity, like the DataCatalog or the DataRecord. You can find more examples on how BBMRI-ERIC directory used Bioschemas for their need in this [DataCatalog](https://github.com/Bioschemas/specifications/blob/master/DataCatalog/examples/bbmri-eric-ID-CZ_MMCI_jsonld.json) and [DataRecord](https://github.com/Bioschemas/specifications/blob/master/DataRecord/examples/bbmri-eric-ID-CZ_MMCI-collection-LTS_jsonld.json) examples.