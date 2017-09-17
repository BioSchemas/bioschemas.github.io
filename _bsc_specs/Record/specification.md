# Record specification 0.0.1

Thing > CreativeWork > Dataset > Record

Bioschemas specification describing a Record in Life Sciences

## Description

A Record acts itself as a dataset although it refers to what could be seen as the minimum compact, complete and auto-descriptive unit in a dataset, i.e., a record.

**Bioschemas usage**

In Life Sciences, records will represent a PhysicalEntity. A link to the represented physical entity should be done via "represents" property. 

## Properties

<table>
  <tr>
    <td>Properties from [Record]</td>
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
    <td>additionalProperty</td>
    <td>PropertyValue</td>
    <td>A property-value pair representing an additional characteristics of the entitity, e.g. a product feature or another characteristic for which there is no matching property in schema.org.

Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. http://schema.org/width, http://schema.org/color, http://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.

Bioschemas usage.
Additional to the use of name and description to describe this property in a human-readable way, in Bioschemas additionalType is used to specify the nature of the property/relation. For instance, if the property refers to a disease association, you could use http://semanticscience.org/resource/SIO_000983.</td>
    <td>many</td>
    <td>O</td>
    <td>Yes, as better suits to describe this additional property</td>
  </tr>
  <tr>
    <td>seeAlso</td>
    <td>Thing or URL</td>
    <td>A pointer to any somehow related thing. To be used whenever you are not so sure about the nature of the relation. Otherwise, use additionalProperty.

Bioschemas usage.
URL is preferred than Thing</td>
    <td>many</td>
    <td>O</td>
    <td></td>
  </tr>
  <tr>
    <td>represents</td>
    <td>PhysicalEntity</td>
    <td>The entity represented by this record</td>
    <td>one</td>
    <td>O</td>
    <td></td>
  </tr>
</table>


<table>
  <tr>
    <td>Properties from [Dataset]</td>
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
    <td>distribution</td>
    <td>DataDownload</td>
    <td>A downloadable form of this dataset, at a specific location, in a specific format.</td>
    <td>many</td>
    <td>O</td>
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
    <td>O</td>
    <td></td>
  </tr>
  <tr>
    <td>dateCreated</td>
    <td>Date  or 
DateTime </td>
    <td>The date on which the CreativeWork was created or the item was added to a DataFeed.</td>
    <td>one</td>
    <td>R</td>
    <td></td>
  </tr>
  <tr>
    <td>dateModified</td>
    <td>Date  or 
DateTime </td>
    <td>The date on which the CreativeWork was most recently modified or when the item's entry was modified within a DataFeed.</td>
    <td>one</td>
    <td>R</td>
    <td></td>
  </tr>
  <tr>
    <td>datePublished</td>
    <td>Date  or 
DateTime </td>
    <td>Date of first broadcast/publication.</td>
    <td>one</td>
    <td>R</td>
    <td></td>
  </tr>
  <tr>
    <td>hasPart</td>
    <td>CreativeWork</td>
    <td>Indicates a CreativeWork that is (in some sense) a part of this CreativeWork.
Inverse property: isPartOf.
</td>
    <td>many</td>
    <td>O</td>
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
    <td>isBasisFor</td>
    <td>CreativeWork or
URL</td>
    <td>A resource for which this resource is used in its creation
InverseProperty: isBasedOn</td>
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
    <td>URL</td>
    <td>An additional type for the item, typically used for adding more specific types from external vocabularies in microdata syntax. This is a relationship between something and a class that the thing is in. In RDFa syntax, it is better to use the native RDFa syntax - the 'typeof' attribute - for multiple types. Schema.org tools may have only weaker understanding of extra types, in particular those defined externally.

Bioschemas usage.
A link to the type of record represented by this resource. For instance, you can use http://purl.uniprot.org/core/Protein if your record is about a UniProt protein</td>
    <td>one</td>
    <td>O</td>
    <td>Yes, as it better suits to describe the nature of this record</td>
  </tr>
  <tr>
    <td>identifier</td>
    <td>PropertyValue, Text, URL</td>
    <td>The identifier property represents any kind of identifier for any kind of Thing, such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See background notes for more details.</td>
    <td>one</td>
    <td>M</td>
    <td></td>
  </tr>
  <tr>
    <td>sameAs</td>
    <td>URL</td>
    <td>URL of a reference Web page that unambiguously indicates the item's identity. E.g. the URL of the item's Wikipedia page, Wikidata entry, or official website.</td>
    <td>many</td>
    <td>O</td>
    <td></td>
  </tr>
  <tr>
    <td>url</td>
    <td>URL </td>
    <td>URL of the item.</td>
    <td>many</td>
    <td>O</td>
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
    <td>Example 1 - [format: JSON-LD].  [Example description. Simple but comprehensive example]</td>
  </tr>
  <tr>
    <td>{
  "@type": "Record",
  "@id": "http://www.identifiers.org/uniprot/P00519",
  "additionalType": "http://purl.uniprot.org/core/Protein",
  "citation": [
    {
      "@id": "http://www.identifiers.org/pubmed/10194451",
      "@type": "ScholarlyArticle",
      "name": {
        "@language": "en",
        "@value": "A novel SH2-containing ..."
      },
      "sameAs": [
        "https://www.ncbi.nlm.nih.gov/pubmed/10194451",
        "http://europepmc.org/abstract/MED/10194451",
        "http://purl.uniprot.org/citations/10194451"
      ]
    },
    {
      "@id": "http://www.identifiers.org/pubmed/9037071",
      "@type": "ScholarlyArticle",
      "name": {
        "@language": "en",
        "@value": "Regulation of DNA ..."
      },
      "sameAs": [
        "https://www.ncbi.nlm.nih.gov/pubmed/9037071",
        "http://europepmc.org/abstract/MED/9037071",
        "http://purl.uniprot.org/citations/10194451"
      ]
    }
 ],
  "dateCreated": "1986-07-21",
  "dateModified": "2017-03-15",
  "distribution": "http://www.uniprot.org/uniprot/P05067.fasta",
  "isPartOf": {
    "@type": "Dataset",
    "@id": "http://www.uniprot.org/news/2017/03/15/release"
  },
  "represents": {
    "@type": "PhysicalEntity",
    "additionalType": "http://semanticscience.org/resource/SIO_010043",
    "identifier": "P00519",
    "name": "Tyrosine-protein kinase ABL1",
    "hasRepresentation": "http://purl.uniprot.org/uniprot/P00519"    
  },
  "sameAs": "http://purl.uniprot.org/uniprot/P00519",
  "seeAlso": "http://www.ebi.ac.uk/ena/data/view/AK312326",
  "url": "http://www.uniprot.org/uniprot/P00519"
}</td>
  </tr>
</table>

