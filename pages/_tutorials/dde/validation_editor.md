---
layout: default
title: Data Discovery Engine - Validation Editor
breadcrumb:
  link1: /tutorials/
  title1: Getting Started
  link2: /tutorials/dde/
  title2: "DDE"
---

## How to use the Validation Editor to apply constraints to your profile specification

The constraints for a profile specification are expressed as JSON Schema validation rules. JSON schema validation rules allow users of the **schema** to use [online validators](https://www.jsonschemavalidator.net/) to validate their json-formatted data against the schema.

The validation editor has the most commonly used JSON Schema validation rules for drag-and-drop use. It includes a custom validation **rule editor** for more complicated validation rules, and a definitions editor is available for even more complex custom validation rules. 

The validations rules apply only to the class in which they are being defined and do not apply outside the class. Using the validation rule editor and definition editor enables the user to flexibly customise the validation rules as needed within the DDE. Users comfortable with jsonschema, are welcome to customize the JSONLD file outside the DDE in their favourite text or json editor.

This guide details the use of the Validation Editor to express the constraints of a profile specification. JSON schema validation rules should not be applied to type specifications. If you are updating an existing profile, you should only need to add validation rules to properties that are new or being changed.

### Creating JSON schema validation rules for the most common expected types
<details>
  <summary>If the cardinality is ONE, you can usually just drag and drop the appropriate validation rule.</summary>

The most basic validation rule is expressing an expected type for a property. For example, each property should have an expected type of value (e.g. - the expected type for the `name` property is usually `schema:Text`.) The most common expected types are already available by default. They include:  
- "schema:Text" = `string` drag-and-drop option
- "schema:Integer" = `integer` drag-and-drop option
- "schema:Boolean" = `boolean` drag-and-drop option
- "schema:URL" = `url` drag-and-drop option
- "schema:Date" = `date` drag-and-drop option
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
    
     ```json
     {“oneOf”: [
       {“type”: “string”},
       {“type”: “array”,
        “items”: 
          {“type”: “string”}
       }
     ]}
     ```
 - We can use the validation rule editor (see the next section) to create a new rule which combines the two rules to be:
  
  ```json
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
  <summary>The Validation Rule Editor allows you to create reusable custom validation rules</summary>

 - Note this requires some familiarity with (or a willingness) to learn a bit of JSON schema
 - Click on the [(+) icon](https://docs.google.com/presentation/d/1yl_aTm-od5U729-nVZWsGnl33oTDTS3NNlLzou60phI/edit#slide=id.g12bfbc3a89b_3_126) following the available validation rules
 - Name your new validation rule and [click ‘ok’](https://docs.google.com/presentation/d/1yl_aTm-od5U729-nVZWsGnl33oTDTS3NNlLzou60phI/edit#slide=id.g12bfbc3a89b_3_201)
 - Now that it has been created, [click on it](https://docs.google.com/presentation/d/1yl_aTm-od5U729-nVZWsGnl33oTDTS3NNlLzou60phI/edit#slide=id.g12bfbc3a89b_3_210) to edit it in the [validation rule editor](https://docs.google.com/presentation/d/1yl_aTm-od5U729-nVZWsGnl33oTDTS3NNlLzou60phI/edit#slide=id.g12bfbc3a89b_3_220)
 - Edit it as needed and [click ‘save’](https://docs.google.com/presentation/d/1yl_aTm-od5U729-nVZWsGnl33oTDTS3NNlLzou60phI/edit#slide=id.g12bfbc3a89b_3_238). Once saved, you can drag-and-drop it to the appropriate property.
</details>
  

### Creating JSON schema validation rules for limiting the expected type
<details>
  <summary>Common expected types (Text, Date, etc.) are available for drag-and-drop by default</summary>

 It may be necessary to create custom validation rules for expected types not available by default including:
 <details>
   <summary>Other Jsonschema-acceptable expected types</summary>
 
 - There are a few expected types which can translate to Jsonschema-acceptable format; however, they are not common enough to clutter the user interface. Use the validation rule editor for these types
  - "schema:Datetime" = `{"type": "string", "format":"datetime"}`
  - "schema:Number" = `{"type": "number"}`
 </details>
 
 <details>
   <summary>All other expected types (from schema.org, bioschemas or any registered schema)</summary>
   
 Three examples of commonly-used example expected types have already been included:
  - object | Person (example of expected type = “schema:Person” treated as a simple drag-and-drop object)
  - DEF | citation (example of a citation defined in the validation only, and then referenced by the validation rule).
  - ontology (example of an object which references an external vocabulary) 
  
 </details> 
  
</details>



### Creating a new object definition for more complex constraints
<details>
  <summary>The Definition Editor allows you to define a new object:</summary>

Object definitions enable more efficient validation rule creation. For example, if multiple properties have a mix of non-default expected types, it is more efficient to define that expected type as an object, and then reference that definition for each property. When you create a new object definition, a corresponding drag-n-drop option will be created with it so that you can reference a single instance of the object (one), or an array of the object (many). To create a new object definition and its corresponding drag-n-drop options:
 - Click on the [(+) icon](https://docs.google.com/presentation/d/1yl_aTm-od5U729-nVZWsGnl33oTDTS3NNlLzou60phI/edit#slide=id.p48) under ‘Definition’
 - Name the new object definition and [click ‘OK’](https://docs.google.com/presentation/d/1yl_aTm-od5U729-nVZWsGnl33oTDTS3NNlLzou60phI/edit#slide=id.p49)
 - Click on the [edit icon](https://docs.google.com/presentation/d/1yl_aTm-od5U729-nVZWsGnl33oTDTS3NNlLzou60phI/edit#slide=id.p50) for the new object definition
 - If you don’t know how to write a new definition, click on [edit icon for the the citation definition](https://docs.google.com/presentation/d/1yl_aTm-od5U729-nVZWsGnl33oTDTS3NNlLzou60phI/edit#slide=id.p46)
 - Highlight the definition and copy it (ctrl+c)
 - Then go back to your [new object definition](https://docs.google.com/presentation/d/1yl_aTm-od5U729-nVZWsGnl33oTDTS3NNlLzou60phI/edit#slide=id.p52) and [paste](https://docs.google.com/presentation/d/1yl_aTm-od5U729-nVZWsGnl33oTDTS3NNlLzou60phI/edit#slide=id.p53)
 - Change the [description, ‘@type’, and properties](https://docs.google.com/presentation/d/1yl_aTm-od5U729-nVZWsGnl33oTDTS3NNlLzou60phI/edit#slide=id.p54) as needed and save your changes
 - Two new validation rules will be added to your validation drag-and-drop options for you to use:
  - `DEF | your definition name` ← allows singular instance of definition (one)
  - `DEF | your definition name(s)` ← allows multiple instance of your definition (many)
  
</details>
