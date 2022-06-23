<details>
  <summary>You may need to edit your JSONLD depending on what you're trying to do with a specification</summary>
  
  <details>
    <summary> If your JSONLD has been saved locally</summary>
      
  - If you downloaded your json, open it in a simple text editor like notepad
  - text editors like Sublime, Brackets, will also work and provide a nicer editing experience
  </details>
  
  <details>
    <summary> If your JSONLD has been saved to GitHub</summary>
  
  - Navigate to the file in your repo on github and click on it
  - Click on the `edit` icon in github  
  </details>
  
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
    - 
  </details>   
    
</details>
  
