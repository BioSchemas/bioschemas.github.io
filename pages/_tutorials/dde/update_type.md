---
layout: default
title: Type Update
nextTutorial:
  link: ./new_type
  title: Create a New Type
---

# Update a Type

You have come to a community consensus on changes needed to a type that already exists. Congratulations! Now you have to update the new type version on the Bioschemas website. Note, if you are comfortable with JSON schema and JSON-LD, you are welcome to copy, paste, and edit the JSON-LD files in the Bioschemas Specifications repository

### Step 1 - Log in
{% include_relative login_to_dde.md %}

### Step 2 - Prepare the type for update
#### 2.1 Find the type in the Registry
* On the Registry page, select “Browse By Namespace”
* Select ‘bioschemastypes’ or ‘bioschemastypesdraft’ depending on whether you are updating a release or draft profile. In this tutorial we will use examples corresponding to updating a draft type.
<!--<br><img src="/pages/_tutorials/dde/images/select-namespace.png" width="80%"></img>-->
* Search for the name of the type to be updated
* Click ‘extend’ (icon on the right at the end of the row corresponding to the type name)
<!--<br><img src="/pages/_tutorials/dde/images/extend-specification.png" width="80%"></img>-->

#### 2.2 Follow the prompts to update your type
* Create a temporary namespace that will help us identify your working space.
* Fill in the form to create the updated type version including the name of the type and a description. The description should include:
  * The description of the type as determined by the community
  * The version of the type
  * Any descriptions of changes between versions
  * The name of the person who prepared the changes
* **You will not be able to change this information on the next steps so make sure it is correct before moving on**
<!--<br><img src="/pages/_tutorials/dde/images/fill-out-spec-form.png" width="80%"></img>-->

#### 2.3 Select properties for this type that you would like to keep
* Similar to Schema.org, properties from the parent class will be inherited, so you can ignore those
* Select any unchanged properties that you would like to keep. If a property has changed expected types:
  * unselect the property and create it again following step 2.4

#### 2.4 Create new properties as needed
* Any schema.org properties that are not available in a parent class will need to be created
* To create a new property:
  * Click on the (+) icon 
  * Enter the name and description of your property into the form (see screenshot of property creation form)
    * The Domain will automatically be populated from the class
  * Specify the expected (range) input type
  * Enter/search for the expected type of your property into the (range) input type(s) of the form. (see screenshot of setting an expected range type or input)
    * Clicking on a class will usually be sufficient to add it as an expected type; HOWEVER, for schema:URL or schema:Text, you will need to click on the Add button.
    * To specify a bioschemas type as the expected (range) input type
      * Enter it manually into the expected (range) input type box as “namespace:class”
        * Eg- bioschemastypesdrafts:Phenotype
  * Special property: conformsTo
    * "Uncheck" conformsTo as it will be added automatically via a script

 #### 2.4 Remove the default JSON Schema validation rules
 * Click on the `remove validation` toggle

### Step 3 - Save your schema
{% include_relative save_your_schema.md %}

### Step 4 - Fix the parent class
{% include_relative edit_your_jsonld.md %}

### Step 5 - Verify that your JSONLD schema file is working properly
{% include_relative check_your_spec.md %}

### Step 6 - If you have not already, save your JSONLD to the bioschemas Specification repository
{% include_relative save_to_specs_repo.md %}

### Step 7 - Update the bioschemas specification in the DDE schema registry
{% include_relative push_updates_to_dde.md %}
