---
layout: default
title: Profile Update
nextTutorial:
  link: ./new_profile
  title: Create a New Profile
---
# Update a Profile

You have come to a community consensus on changes needed to a profile that already exists. Congratulations! Now you have to update the new profile version on the Bioschemas website. Note, if you are comfortable with JSON schema and JSON-LD, you are welcome to copy, paste, and edit the JSON-LD files in the Bioschemas Specifications repository

### Step 1 - Log in
{% include_relative login_to_dde.md %}

### Step 2 - Prepare the profile for update
#### 2.1 Find the profile in the Registry
* On the Registry page, select “Browse By Namespace”
* Select ‘bioschemas’ or ‘bioschemasdraft’ depending on whether you are updating a release or draft profile. In this tutorial we will use examples corresponding to updating a draft profile.
<br><img src="{{/images/select-namespace.png | relative_url }}" width="80%"></img>
* Search for the name of the profile to be updated
* Click ‘extend’ (icon on the right at the end of the row corresponding to the profile name)
<br><img src="/pages/_tutorials/dde/images/extend-specification.png" width="80%"></img>

#### 2.2 Follow the prompts to update your profile
* Create a temporary namespace that will help us identify your working space.
* Fill in the form to create the updated profile version including the name of the profile and a description. The description should include:
  * The description of the profile as determined by the community
  * The version of the profile
  * Any descriptions of changes between versions
  * The name of the person who prepared the changes
* **You will not be able to change this information on the next steps so make sure it is correct before moving on**
<br><img src="/pages/_tutorials/dde/images/fill-out-spec-form.png" width="80%"></img>

#### 2.3 Select minimum, recommended and optional properties of your profile
* You can select properties from all parent classes. Each parent class will be displayed on a blue box. 
* The  minimum (aka requested/mandatory), recommended, and optional properties are automatically shown from the latest available profile you selected in 2.1.
<br><img src="/pages/_tutorials/dde/images/inherit-properties.png" width="80%"></img>
* You can select additional properties or unselect those that are no longer needed for the updated version.
* To **update properties for a particular parent class**, click on the “...” icon on the right of that parent class. This will open up a list of all availables properties for this class. 
  * If a property **should be** included in the profile:
    * select it with the checkbox icon
    * define its marginality (red star for minimum, yellow circle for recommended, turquoise square for optional)
  * If a property **should NOT** be part of the profile:
    * deselect it with the checkbox icon - i.e., checkbox icon should be gray
  * Change the selection checkbox icon and marginality buttons as needed for each available property
* Special property: conformsTo
  * "Uncheck" conformsTo as it will be added automatically via a script

#### 2.4 Modify cardinality and description of properties selected for your profile
* You can modify the cardinality of those properties that you have selected for your profile. To activate the cardinality selection, please look for the “Validation Editor” option on the top of your profile and enable it
<br><img src="/pages/_tutorials/dde/images/validation_toggle.jpg" width="15%"></img>
* On the Validation View, make sure that “Cardinality” is enabled, you will find this option on the top left
<br><img src="/pages/_tutorials/dde/images/cardinality_toggle.jpg" width="30%"></img>
* You will have to select the cardinality for each property 
<br><img src="/pages/_tutorials/dde/images/cardinality_selection.jpg" width="15%"></img>
* You can also modify the description. We suggest doing so only when you need to add a note on how the property should be used for the Bioschemas use case, otherwise leave it as it comes from schema.org. Remember to always copy the portion corresponding to the original text in schema.org and then, separated by an empty line, add the usage note for Bioschemas. The usage note should include any recommendation on existing controlled vocabularies for the property.
<br><img src="/pages/_tutorials/dde/images/edit_description.jpg" width="30%"></img>
* Remember to save your work. The DDE editor will tell you if there is any property that still need validation rules
<br><img src="/pages/_tutorials/dde/images/validation_warning.jpg" width="20%"></img>
* Add or modify existing validation rules as needed via the drag-and-drop interface in the DDE validation editor

#### 2.5 Download / Save your JSON-LD schema
* Downloading your DDE-generated schema
  * Click the download button 
  * Name your DDE-generated file, and click download
* Saving your DDE-generated schema to GitHub
  * Click the GitHub icon to save your JSON-LD to a GitHub repository
  * Click "get repos" to see repositories for which you have access
  * Select a repository for which you have access
  * To save a new file, slide the "Update file" toggle to the off position
  * Enter a name for your file and a github commit comment (if you wish) and click "save"
* Interpreting the validation warnings
  * The DDE will automatically check your schema for JSON validation rules and give warnings if they are missing
  * Revisit the DDE validation editor and add JSON Schema validation rules to the properties that lack them

#### 2.6 Test your JSON-LD schema
* Click on "Register Schema"
* Copy the url to your JSONLD schema in GitHub from the address bar of your browser and paste it into the schema playground (Use the link convert option if it pops up)
* Click on "Let’s go" to test the compatibility of your schema with the DDE
  * If it works well, you will see no errors
  * If there are some minor issues, you will receive a warning but can and should select the option to continue
  * If there are major issues, you will be blocked from continuing until those issues are addressed. If you don't think you can address them yourself, copy them into a temporary text file so you can paste them in your pull request later

#### 3.0 Save your JSON-LD to the Bioschemas Specification Repository and create a pull request
* Go to the [Bioschemas Specification repository](https://github.com/BioSchemas/specifications) and find your specification
* In your fork or branch, add your JSON-LD to the `jsonld` directory for your specification
* Create a pull request for your fork or branch
  * Include any issues you encountered from your test that you were unable to address


