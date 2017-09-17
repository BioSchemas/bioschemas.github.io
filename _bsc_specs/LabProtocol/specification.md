# Bioschemas specification describing a LabProtocol in Life Sciences

LabProtocol specification 0.0.2

[Thing](http://schema.org/Thing) > [CreativeWork](http://schema.org/CreativeWork) > LabProtocol

## Description

An experimental protocol is a sequence of tasks and operations executed to perform experimental research in biological and biomedical areas.

Experimental protocols are fundamental information structures that support the description of the processes by means of which results are generated in experimental research [1]. Experimental protocols describe how the data were produced, the steps undertaken and conditions under which these steps were carried out.

[1]  Giraldo, O., Garcia, A., Corcho, O.: SMART Protocols: SeMAntic RepresenTation for Experimental Protocols, Riva del Garda, Trentino, Italy (2014). 4th Workshop on Linked Science 2014- Making Sense Out of Data (LISC2014)

# Properties

<table>
  <tr>
    <td>Properties from [LabProtocol]</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Property</td>
    <td>Expected Type</td>
    <td>Description</td>
    <td>CN</td>
    <td>MG</td>
    <td>CV</td>
  </tr>
  <tr>
    <td>duration</td>
    <td>Duration</td>
    <td>The time it takes to actually carry on the protocol, in ISO 8601 duration format.</td>
    <td>one</td>
    <td>R</td>
    <td></td>
  </tr>
  <tr>
    <td>instrument</td>
    <td>Thing, Text or URL</td>
    <td>The object that helped the agent perform the action. e.g. John wrote a book with a pen.

Bioschema usage.
For LabProtocols it would be a laboratory equipment use by a person to follow one or more steps described in this LabProtocol.</td>
    <td>many</td>
    <td>M</td>
    <td></td>
  </tr>
  <tr>
    <td>purpose</td>
    <td>Text</td>
    <td>A goal towards an action is taken. Can be concrete or abstract.</td>
    <td>one</td>
    <td>M</td>
    <td></td>
  </tr>
  <tr>
    <td>reagent</td>
    <td>PhysicalEntity, Text or URL</td>
    <td>Reagents used in the protocol. ChEBI and PubChem entities can be used whenever available. Commercial names are also acceptable (URL if possible)</td>
    <td>many</td>
    <td>M</td>
    <td>ChEBI, Pubchem
</td>
  </tr>
  <tr>
    <td>sample</td>
    <td>PhysicalEntity, Text or URL</td>
    <td>Sample used in the protocol. It could be a record in a Dataset describing the sample or a physical object corresponding to the sample or a URL pointing to the type of sample used.</td>
    <td>many</td>
    <td>M</td>
    <td></td>
  </tr>
  <tr>
    <td>software</td>
    <td>SoftwareApplication</td>
    <td>An application that can complete the request.</td>
    <td>many</td>
    <td>R</td>
    <td></td>
  </tr>
</table>


<table>
  <tr>
    <td>Properties from [CreativeWork]</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Property</td>
    <td>Expected Type</td>
    <td>Description</td>
    <td>CN</td>
    <td>MG</td>
    <td>CV</td>
  </tr>
  <tr>
    <td>citation</td>
    <td>CreativeWork or URL</td>
    <td>A citation or reference to a creative work, such as a publication, web page, scholarly article, etc.</td>
    <td>many</td>
    <td>R</td>
    <td></td>
  </tr>
  <tr>
    <td>license</td>
    <td>CreativeWork or URL</td>
    <td>A license document that applies to this content, typically indicated by URL.</td>
    <td>one</td>
    <td>R</td>
    <td></td>
  </tr>
  <tr>
    <td>isBasedOn</td>
    <td>CreativeWork or
URL</td>
    <td>A resource that was used in the creation of this resource. This term can be repeated for multiple sources. For example, http://example.com/great-multiplication-intro.html. Supersedes isBasedOnUrl.</td>
    <td>many</td>
    <td>O</td>
    <td></td>
  </tr>
  <tr>
    <td>isPartOf</td>
    <td>CreativeWork</td>
    <td>Indicates a CreativeWork that this CreativeWork is (in some sense) part of.</td>
    <td>many</td>
    <td>O</td>
    <td></td>
  </tr>
  <tr>
    <td>keywords</td>
    <td>Text</td>
    <td>Keywords or tags used to describe this content. Multiple entries in a keywords list are typically delimited by commas.</td>
    <td>many</td>
    <td>R</td>
    <td></td>
  </tr>
  <tr>
    <td>structuralElement</td>
    <td>Creative Work</td>
    <td>A structural element refers to qualified text in a CreativeWork. It should be used when plain text is not enough, for instance, to distinguish abstract, sections or paragraphs. Qualification is achieved by using the additionaType property which should point to an ontological term describing the element referred to by this property. The text itself can be added using the property text.

Bioschemas usage.

A particular case in Bioschemas is LabProtocol where structural elements are used to described advantages (situations the Protocol has been successfully employed), limitations (situations the Protocol would be unreliable or otherwise unsuccessful), applications (Applications of the protocol list the full diversity of the applications of the method and support if is possible to extend the range of applications of the protocol. e.g. northern blot assays, sequencing, etc.), and outcomes (outcome or expected result by a protocol execution).

Bioschemas usage.
For LabProtocol, in the applicationType, please use http://purl.org/net/SMARTprotocol#AdvantageOfTheProtocol for advantages, http://purl.org/net/SMARTprotocol#LimitationOfTheProtocol for limitations, http://purl.org/net/SMARTprotocol#ApplicationOfTheProtocol for applicability, and http://purl.org/net/SMARTprotocol#OutcomeOfTheProtocol for outcomes.</td>
    <td>many</td>
    <td>R</td>
    <td>SMARTProtocols (https://bioportal.bioontology.org/ontologies/SP)</td>
  </tr>
</table>


<table>
  <tr>
    <td>Properties from  [Thing]</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Property</td>
    <td>Expected Type</td>
    <td>Description</td>
    <td>CN</td>
    <td>MG</td>
    <td>CV</td>
  </tr>
  <tr>
    <td>additionalType</td>
    <td></td>
    <td>An additional type for the item, typically used for adding more specific types from external vocabularies in microdata syntax. This is a relationship between something and a class that the thing is in. In RDFa syntax, it is better to use the native RDFa syntax - the 'typeof' attribute - for multiple types. Schema.org tools may have only weaker understanding of extra types, in particular those defined externally.

Bioschemas usage.
If used, the recommended URL is experimental protocol as defined by SmartProtocols (http://purl.org/net/SMARTprotocol#ExperimentalProtocol)</td>
    <td>one</td>
    <td>O</td>
    <td>SMARTProtocols (https://bioportal.bioontology.org/ontologies/SP)</td>
  </tr>
  <tr>
    <td>description</td>
    <td>Text</td>
    <td>A description of the item.

Bioschemas usage.
Use in LabProtocol to include the step byt step process folowed in this protocol.</td>
    <td>one</td>
    <td>R</td>
    <td></td>
  </tr>
  <tr>
    <td>identifier</td>
    <td>PropertyValue, Text, URL</td>
    <td>The identifier property represents any kind of identifier for any kind of Thing, such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See background notes for more details.</td>
    <td>one</td>
    <td>R</td>
    <td></td>
  </tr>
</table>


**Legend:		***CN: Cardinality (one, many)*

*MG: Marginality (**M: minimum**; **R: recommended**; **O: optional**)*

*CV: Suggested controlled vocabularies (yes, no)*

# Examples
Schema.org[ suggests](http://schema.org/docs/gs.html) implementing metadata using JSON-LD, RDFa or Microdata. JSON-LD is the recommended format by Google, but any of these formats can be used for embedding information about tools in a web page or other online resource.

<table>
  <tr>
    <td>Example 1 - [format: JSON-LD].  [Example description. Using minimum fields]</td>
  </tr>
  <tr>
    <td>{
  "@type": "LabProtocol",
  "additionalType", "http://purl.org/net/SMARTprotocol#ExperimentalProtocol",
  "reagent": {
    "@type": "PhysicalEntity",
    "additionalType": "http://purl.obolibrary.org/obo/CHEBI_30879",
    "name": "Alcohol"
  },
  "purpose": "This protocol describes the steps involved in the whole mount   
    processing of mouse eyes for visualization of the retinal vasculature.",
  "instrument": [
    "http://www.bio-thing.com/p6286",
    "microscope",
    {
      "@type": "Thing",
      "additionalType": 
        "http://purl.bioontology.org/ontology/SNOMEDCT/29319002",
      "name": "forceps"
    }
  ],
  "sample": {
    "@type": "PhysicalEntity",
    "additonalType": "http://purl.bioontology.org/ontology/NCBITAXON/10090",
    "name": "mus musculus (mouse)"
  }
}</td>
  </tr>
</table>


<table>
  <tr>
    <td>Example 1 - [format: JSON-LD].  [Example description. Incomplete example using structuralElement]</td>
  </tr>
  <tr>
    <td>{
  "@type": "LabProtocol",
  "additionalType", "http://purl.org/net/SMARTprotocol#ExperimentalProtocol",
  "structuralElement": {
    "@type": "CreativeWork",
    "additionalType":       
      "http://purl.org/net/SMARTprotocol#LimitationOfTheProtocol",
    "text": "A major problem faced both in this and other safflower
      transformation studies is the hyperhydration of transgenic   
      shoots which result in the loss of a large proportion of 
      transgenic shoots.",
    "isPartOf":   "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3115923/"
  }
}</td>
  </tr>
</table>

