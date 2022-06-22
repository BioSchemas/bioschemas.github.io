<details>
  <summary>Click ‘extend’ (Icons on the right to ‘visualise’ (shows property details for that class) or ‘extend’)</summary>
  
  ([see 'extend' screenshot](https://docs.google.com/presentation/d/1yl_aTm-od5U729-nVZWsGnl33oTDTS3NNlLzou60phI/edit#slide=id.p8)), ([see 'visualize' screenshot](https://docs.google.com/presentation/d/1yl_aTm-od5U729-nVZWsGnl33oTDTS3NNlLzou60phI/edit#slide=id.g12bfbc3a89b_3_41)), (see [property details screenshot](https://docs.google.com/presentation/d/1yl_aTm-od5U729-nVZWsGnl33oTDTS3NNlLzou60phI/edit#slide=id.g12bfbc3a89b_3_49))
  
  <details>
    <summary>You will need to be logged in to continue</summary>
    
   - You can [login via your github account](https://docs.google.com/presentation/d/1yl_aTm-od5U729-nVZWsGnl33oTDTS3NNlLzou60phI/edit#slide=id.p10)
   - The DDE requires read access to find your repositories (so you can save to them) and write access in order for you to be able to export your work (specification in JSONLD format) to github
  </details>
  
  <details>
    <summary>Follow the prompts to create your new specification</summary>
    
   - Create a [temporary namespace](https://docs.google.com/presentation/d/1yl_aTm-od5U729-nVZWsGnl33oTDTS3NNlLzou60phI/edit#slide=id.p11) (it will get replaced later on). Note, This step may be subject to a timeout. **Please use PascalCase for your temporary namespace.**
    <details>
      <summary>Fill in the form to create the new specification including the name of your specification and a description.</summary>
      
      (see [screenshot of form](https://docs.google.com/presentation/d/1yl_aTm-od5U729-nVZWsGnl33oTDTS3NNlLzou60phI/edit#slide=id.p12))
      The description should include:
       - The description of the class as determined by the community
       - The version of the class
       - Any descriptions of changes between versions (this only applies to updating a class, not the creation of an entirely new class)
    </details>
    
  </details>
  <details>
    <summary>Select properties to inherit</summary>

  - The DDE will allow you to select properties from all parent classes to inherit.
    <details>
    <summary> Select the checkbox on pre-existing properties for reuse.</summary>
      
     - The [display shows](https://docs.google.com/presentation/d/1yl_aTm-od5U729-nVZWsGnl33oTDTS3NNlLzou60phI/edit#slide=id.p17) inheritable class properties ([blue bar](https://docs.google.com/presentation/d/1yl_aTm-od5U729-nVZWsGnl33oTDTS3NNlLzou60phI/edit#slide=id.g12bfbc3a89b_3_57)) , and class-specific properties ([yellow bar](https://docs.google.com/presentation/d/1yl_aTm-od5U729-nVZWsGnl33oTDTS3NNlLzou60phI/edit#slide=id.g12bfbc3a89b_3_65)). 
      Also shown is the inheritance ‘path’ of the class and its properties. The ‘...’ icon  on existing properties is an expandable view, listing existing properties from the class hierarchy.
     - Selecting a property will allow you to specify its marginality and to create constraints in the form of JSON Schema validation rules 
    </details>
  - If you are extending from a class with JSON schema validation rules (ie- a profile), the inheritable properties will be pre-loaded by default. **You will need to un-select any that you do NOT wish to keep**
  </details>
  <details>
  <summary> Special considerations for types</summary>
    
  - Since types are NOT subject to marginality and cardinality constraints, jsonschema validation rules do not apply, so you don’t need to select any properties as they will all be inherited by default
   
  </details>
 
 </details>
