# PhysicalEntity specification 0.0.1

Thing > PhysicalEntity

Bioschemas specification describing a PhysicalEntity in Life Sciences

## Description

A PhysicalEntity is any object that exists in the physical world and cannot be better represented with any other existing type in schema.org. In order to specify the nature of this physical entity, additionalProperty must be used to specify the nature/type of this physical entity. For instance, http://semanticscience.org/resource/SIO_010043 can be used to refer to a protein. 

**Bioschemas usage**

A PhysicalEntity is a flexible and extensible wrapper for Life Sciences entities. Representations of physical entities in Life Sciences are usually recorded in datasets; the link to a dataset should be done via properties. A particular Life Sciences entity, refer to as a profile in Bioschemas, will customize PhysicalEntity by modifying the marginality, cardinality and ontologies used. For instance, a protein profile would recommend pointing to an organism a part of the minimum information, but not necessarily to a sample or disease. 

# Properties

<table>
  <tr>
    <td>Properties from [PhysicalEntity]</td>
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
    <td>isContainedIn</td>
    <td>PhysicalEntity</td>
    <td>Indicates a PhysicalEntity that this PhysicalEntity is (in some sense) part of.</td>
    <td>many</td>
    <td>O</td>
    <td></td>
  </tr>
  <tr>
    <td>contains</td>
    <td>PhysicalEntity</td>
    <td>
Indicates a PhysicalEntity that is (in some sense) a part of this PhysicalEntity.
Inverse property: isPartOf.</td>
    <td>many</td>
    <td>O</td>
    <td></td>
  </tr>
  <tr>
    <td>location</td>
    <td>Place,
PostalAddress,
PropertyValue,
Text or URL</td>
    <td>The location of for example where the event is happening, an organization is located, or where an action takes place.

Bioschemas usage.
In Bioschemas location can be refer to a position in a chromosome or sequence or to a physical place where, for instance, a sample is stored. Using additionalType is advised to make the distinction. For instance, FALDO can be used for sequence coordinates.</td>
    <td>many</td>
    <td>O</td>
    <td>Yes, as it better suits to describe the location. </td>
  </tr>
  <tr>
    <td>hasRepresentation</td>
    <td>Record, PropertyValue, Text or URL</td>
    <td>Any representation of this entity. For instance, a record in a dataset or a web page about it.

If the representation is an image, it is advisable to use the property image from Thing</td>
    <td>many</td>
    <td>O</td>
    <td>Yes, as it better suits to describe the nature of the representation</td>
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
    <td>SmartProtocols (https://bioportal.bioontology.org/ontologies/SP)</td>
  </tr>
  <tr>
    <td>alternateName</td>
    <td>Text</td>
    <td>An alias for the item</td>
    <td>many</td>
    <td>O</td>
    <td></td>
  </tr>
  <tr>
    <td>description</td>
    <td>Text</td>
    <td>A description of the item.

Bioschemas usage.
Use in LabProtocol to include the step byt step process folowed in this protocol.</td>
    <td>one</td>
    <td>O</td>
    <td></td>
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
    <td>image</td>
    <td>ImageObject  or 
URL </td>
    <td>An image of the item. This can be a URL or a fully described ImageObject.</td>
    <td>many</td>
    <td>O</td>
    <td></td>
  </tr>
  <tr>
    <td>name</td>
    <td>Text</td>
    <td>The name of the item</td>
    <td>one</td>
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
  "@type": "PhysicalEntity",
  "additionalType": "http://semanticscience.org/resource/SIO_010043",
  "alternateName": [
    {
    "@language": "en",
    "@value": "EGFR_HUMAN"
    },
    {
    "@language": "en",
    "@value": "EGFR"
    }
  ],
  "description": {
    "@language": "en",
    "@value": "Receptor tyrosine kinase binding ligands of the EGF..."
  },
  "identifier": "P00533",
  "name": "Epidermal growth factor receptor",
  "contains": {
    "@type": "PhysicalEntity",
    "additionalType": "http://semanticscience.org/resource/SIO_010041",
    "description": "Proton acceptor"   
  },
  "location": {
    "@type": "PropertyValue",
    "additionalType": "http://biohackathon.org/resource/faldo#ExactPosition",
    "name": "Position",
    "value": 837 
  },
  "hasRepresentation": "http://purl.uniprot.org/uniprot/P00533"    
}</td>
  </tr>
</table>

