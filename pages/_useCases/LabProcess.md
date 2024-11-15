---
layout: use-case
name: Laboratory Processes
group: labprotocols
active: true
redirect_from: 
- "/useCases/LabProcesses/"
- "/useCases/LabProcesses"
- "/useCases/LabProcess/"
- "/useCases/LabProcess"
---

### Findability

#### Findability for comparative analysis
A user is seeking experimental data for the purpose of conducting a comparative
analysis. Their primary interest lies in identifying and comparing experiments with
specific factors. In individual experiments, these factors are not the primary focus of
the studies; instead, they serve as fixed parameters within the experimental
processes. These seemingly "uninteresting" parameters need to be easily accessible
for their research. The user aims to search for various parameters, factors, and
characteristics within the specific context of different parts of the experimental setup.
For example, consider an experiment comprising two distinct processes: one for
growth and another for measurement under heat stress, both involving the
parameter "temperature." However, for their comparative analysis, they are
interested in a specific instance of this parameter, and they need the capability to
search for it. Consequently, this parameter must be structured and accessible within
the schema markup of the original experiment. In the event that all this information is
associated with a dataset object, manual creation of the markup becomes
necessary, as it demands a semantic understanding of formal parameters. The ISA's
straightforward process graph model excels in capturing these nuances. Therefore,
we recommend integrating the LabProcess object type into Bioschemas, as this will
facilitate the structured markup of the formal parameters associated with experiment
steps.

#### Findability for fine-grained data acquisition
Improve the findability for datasets providing (raw) files which can be used for
bioinformaticians to get data that was created using a dedicated facility or
instrument. Imagine a bioinformatician developing a new image analysis algorithm to
calculate plant growth based on drone images. Now he wants to improve the
underlying calculation and need more drone images which have a minimal resolution
or were generated with a certain camera sensor, he is not interested in the original
experimental design, just looking for data based on any equipment.

#### Findability for Input-based dataset search
In a plant phenomic dataset that includes both direct measures and computed data
elaborated to characterize the plant varieties, the LabProcess type will allow to
document the relationship between datafiles. Hence, a user, through a search
engine, would be able to identify reproducible datasets that include both raw and
derived data. Also, a search engine would be able to point to raw data that have
been used to extract specific traits. For instance, a raw images dataset from which a
trait disease dataset has been derived could be easily found thanks to LabProcess,
hence identifying potential training dataset for challenges such as the global wheat
challenge.

### Overview
Overview of LabProcess and how it relates to other specifications in Bioschemas, for instance LabProtcol and Sample.

![Overview](/images/labProcessOverview.png)