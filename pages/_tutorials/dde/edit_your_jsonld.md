<details>
  <summary>You may need to edit your JSONLD depending on what you're trying to do with a specification</summary>
  
  <details>
    <summary> How to edit your JSON LD</summary>
    
  <details>
    <summary>  If your JSONLD has been saved locally</summary>
      
  - If you downloaded your json, open it in a simple text editor like notepad
  - text editors like Sublime, Brackets, will also work and provide a nicer editing experience
  </details>
  
  <details>
    <summary> If your JSONLD has been saved to GitHub</summary>
  
  - Navigate to the file in your repo on github and click on it
  - Click on the `edit` icon in github  
  </details>
  
  </details>  
  
  <details>
    <summary> What to edit in your JSONLD</summary>
    
  <details>
    <summary> Edits needed when creating a new type specification</summary>
  
  - Since types do not have marginality/cardinality constraints, you'll need to delete the entire `$validation`
    - {% include_relative remove_validation.md  %} 
  </details>
  
  <details>
    <summary> Edits needed when updating an existing type specification</summary>
    
  - Since types do not have marginality/cardinality constraints, you'll need to delete the entire `$validation`
    - {% include_relative remove_validation.md  %}
  - Since this JSONLD schema is meant to REPLACE a previous version rather than be a child of the previous version, you'll need to update the parent class
    - {% include_relative change_parent_class.md %} 
  </details>  
  
  <details>
    <summary> Edits needed when creating a new profile specification</summary>
  
  - The DDE was originally designed for deriving profile-like specifications from schema.org; hence, editing the JSONLD for a new profile specification is usually not necessary with some exceptions (see other common manual edits)
  </details>
  
  <details>
    <summary> Edits needed when updating an existing profile specification</summary>
    
  - Since this JSONLD schema is meant to REPLACE a previous version rather than be a child of the previous version, you'll need to update the parent class
    - {% include_relative change_parent_class.md %} 
  </details>   
  
  
  <details>
    <summary> Other common manual edits</summary>
    
  - Using external vocabularies as properties (not property values)
    - When using external vocabularies as properties, you will need to include the url for the vocabulary in the `@context`, and to fix the namespace in the property definition
    - For example, I create a property (for a new class called `test`) in the DDE called `dateCopyrighted`, but I really want it to just use `dateCopyrighted` from an external vocabulary, the Dublin Core Initiative Term. The DDE-generated property definition would look like this:
    
          {
            "@id": "test:dct:dateCopyrighted",
            "@type": "rdf:Property",
            "rdfs:comment": "Date of copyright of the resource.",
            "rdfs:label": "dct:dateCopyrighted",
            "schema:domainIncludes": {
              "@id": "test:MyTest"
            },
            "schema:rangeIncludes": [
              {
                "@id": "schema:Date"
              }
            ]
          }
    
    and would need to be adjusted to:
    
          {
            "@id": "dct:dateCopyrighted",
            "@type": "rdf:Property",
            "rdfs:comment": "Date of copyright of the resource.",
            "rdfs:label": "dateCopyrighted",
            "schema:domainIncludes": {
              "@id": "test:MyTest"
            },
            "schema:rangeIncludes": [
              {
                "@id": "schema:Date"
              }
            ]
          }
    
    and the DDE-generated `@context` content:
    
         "@context": {
          "schema": "http://schema.org/",
          "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
          "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
          "test": "https://discovery.biothings.io/view/test/",
          "bioschemas": "https://discovery.biothings.io/view/bioschemas/"
        }
    
    would need to be adjusted to include dct:
    
          "@context": {
          "schema": "http://schema.org/",
          "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
          "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
          "test": "https://discovery.biothings.io/view/test/",
          "bioschemas": "https://discovery.biothings.io/view/bioschemas/",
          "dct": "http://purl.org/dc/terms/"
        }   
  </details>   
    
  </details>
</details>
  
