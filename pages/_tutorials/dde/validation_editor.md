## How to use the Validation Editor to apply constraints to your schema

The constraints for a profile specification are expressed as JSON Schema validation rules.
The validation editor has the most commonly used JSON Schema validation rules for drag-and-drop use. It includes a custom validation **rule editor** for more complicated validation rules, and a definitions editor is available for even more complex custom validation rules. 

The validations rules apply only to the class in which they are being defined and do not apply outside the class. 

This guide details the use of the Validation Editor to express the constraints of a profile.

### Addressing the most common expected types
<details>
  <summary>If the cardinality is ONE, you can just drag and drop the appropriate validation rule.</summary>
  
The most common expected types include:  
- "schema:Text" = “string” drag-and-drop option
- "schema:Integer" = “integer” drag-and-drop option
- "schema:Boolean" = “boolean” drag-and-drop option
- "schema:URL" = “url” drag-and-drop option
- "schema:Date" = “date” drag-and-drop option
</details>

### Addressing cardinality rules (one vs many)
<details>
  <summary>By default, the validation editor has only 3 options which allow for ‘many’ options:</summary>

  - string(s), which allows a property to have `many` inputs as long as the expected type is “schema:Text”
  - keyword(s), same as string(s)
  - Enumeration, which allows the user to set a fixed list of string options
</details>
<details>
  <summary>Alternative options may be created by combining the rules in the validation rule editor</summary>

  - For example, we can see that the [validation rule for url](https://docs.google.com/presentation/d/1yl_aTm-od5U729-nVZWsGnl33oTDTS3NNlLzou60phI/edit#slide=id.g12bfbc3a89b_3_178) is: 
      
     `{“type”: “string”, “format”: “uri”}`
  - And we can see that the [validation rule for string(s)](https://docs.google.com/presentation/d/1yl_aTm-od5U729-nVZWsGnl33oTDTS3NNlLzou60phI/edit#slide=id.g12bfbc3a89b_3_191) is:
    
     ```
     {“oneOf”: [
       {“type”: “string”},
       {“type”: “array”,
        “items”: 
          {“type”: “string”}
       }
     ]}
     ```
 - We can use the validation rule editor (see the next section) to create a new rule which combines the two rules to be:
  
  ```
     {“oneOf”: [
       {“type”: “string”, “format”: “uri”},
       {“type”: “array”,
        “items”: 
          {“type”: “string”, “format”: “uri”}
       }
     ]}
  ```

</details>

### Using the Validation Rule Editor
<details>
  <summary></summary>
  
</details>
  

### Addressing expected types not available in the DDE
<details>
  <summary></summary>
  
</details>



### Creating a new object definition for more complex constraints
<details>
  <summary></summary>
  
</details>
