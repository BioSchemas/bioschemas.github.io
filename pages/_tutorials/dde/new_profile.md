---
title: Create a New Profile in the DDE
previousTutorial:
  link: ./dde/update_profile
  title: How to create a new draft profile
nextTutorial:
  link: ./dde/update_type
  title: Update a Type
  
bioschemas:
  "@context": https://schema.org/
  "@type": LearningResource
  "http://purl.org/dc/terms/conformsTo":
  - "@type": CreativeWork
    "@id": "https://bioschemas.org/profiles/TrainingMaterial/1.0-RELEASE"
  about:
    - "@id": https://schema.org
    - "@id": http://edamontology.org/topic_0089
  audience:
  - "@type": Audience
    name: People interested in creating a new Bioschemas profile
  name: "How to create a new Bioschemas Profile with the Data Discovery Engine (DDE) Schema Playground"
  author:
  - "@type": Person
    name: "Ginger Tsueng"
    "@id": https://bioschemas.org/people/GingerTsueng
    url: https://bioschemas.org/people/GingerTsueng
  - "@type": Person
    name: "Leyla Garcia"
    "@id": https://bioschemas.org/people/LeylaGarcia
    url: https://bioschemas.org/people/LeylaGarcia
  - "@type": Person
    name: "Nick Juty"
    "@id": https://bioschemas.org/people/NickJuty
    url: https://bioschemas.org/people/NickJuty
  - "@type": Person
    name: "Alasdair Gray"
    "@id": https://bioschemas.org/people/AlasdairGray
    url: https://bioschemas.org/people/AlasdairGray
  dateModified: 2022-10-25
  description: "In this how-to, we will guide you through the necessary steps in order to create a new Bioschemas profile"
  keywords: "schemaorg, markup, structured data, bioschemas"
  license: CC-BY 4.0
  version: 0.2

---

You have come to a community consensus on changes needed to a profile that already exists. Congratulations! Now you have to update the new profile version on the Bioschemas website. Note, if you are comfortable with JSON schema and JSON-LD, you are welcome to copy, paste, and edit the JSON-LD files in the Bioschemas Specifications repository

### Step 1 - Log in
{% include_relative login_to_dde.md %}

### Step 2 - Create the new profile
#### 2.1 Find the parent type/class of the new profile in the Registry
* DDE classes are commonly known as ‘types’ in schema.org and ‘specifications’ in Bioschemas
* If the parent type/class __is from schema.org__, search for it in the search bar in the ‘Search By Class Name’ tab
* If the parent type/class is from bioschemas:
  * On the Registry page, select “Browse By Namespace”
    * Select ‘bioschemastypes’ if the parent type/class is a released Bioschemas type
    * Select ‘bioschemastypesdraft’ if the parent type/class is a draft Bioschemas type
{% include image.html file="/tutorials/dde/images/select-namespace-type.png" alt="Browse types in the DDE by namespace" width="80%" %}

* Search for the name of the parent class for your new profile
* Click ‘extend’ (icon on the right at the end of the row corresponding to the parent class/type)

{% include image.html file="/tutorials/dde/images/extend_bioschemas_parent.png" alt="Selecting a bioschemas type to extend" width="80%" %}

#### 2.2 Follow the prompts to create your new profile
* Create a temporary namespace that will help us identify your working space.
* Fill in the form to create the new profile including the name of the profile and a description. The description should include:
  * The description of the profile as determined by the community
  * The version of the profile
  * Any descriptions of changes between versions
  * The name of the person who prepared the changes
  
  __You will not be able to change this information on the next steps so make sure it is correct before moving on.__

{% include image.html file="/tutorials/dde/images/fill-out-spec-form.png" alt="Complete the web form for the profile" width="80%" %}

#### 2.3 Select minimum, recommended and optional properties of your profile
* You can select properties from all parent classes. Each parent class will be displayed on a blue box. 
* The  minimum (aka requested/mandatory), recommended, and optional properties are automatically shown from the latest available profile you selected in 2.1.
* You can select additional properties or unselect those that are no longer needed for the updated version.
* To **update properties for a particular parent class**, click on the "..." icon on the right of that parent class. This will open up a list of all availables properties for this class. 
  * If a property **should be** included in the profile:
    * select it with the checkbox icon
    * define its marginality (red star for minimum, yellow circle for recommended, turquoise square for optional)
  * If a property **should NOT** be part of the profile:
    * deselect it with the checkbox icon - i.e., checkbox icon should be gray
  * Change the selection checkbox icon and marginality buttons as needed for each available property
* Special property: conformsTo
  * "Uncheck" conformsTo as it will be added automatically via a script
 {% include image.html file="tutorials/dde/images/inherit-properties.png" alt="inherit properties" width="80%" %}

#### 2.4 Modify cardinality and description of properties selected for your profile
* You can modify the cardinality of those properties that you have selected for your profile. To activate the cardinality selection, please look for the “Validation Editor” option on the top of your profile and enable it
* On the Validation View, make sure that “Cardinality” is enabled, you will find this option on the top left

{% include image.html file="/tutorials/dde/images/cardinality_toggle.jpg" alt="Enabling cardinality" width="30%" %}

* You will have to select the cardinality for each property 

{% include image.html file="/tutorials/dde/images/cardinality_selection.jpg" alt="Select cardinality for a property%" width="15%" %}

* You can also modify the description. We suggest doing so only when you need to add a note on how the property should be used for the Bioschemas use case, otherwise leave it as it comes from schema.org. Remember to always copy the portion corresponding to the original text in schema.org and then, separated by an empty line, add the usage note for Bioschemas. The usage note should include any recommendation on existing controlled vocabularies for the property.

{% include image.html file="/tutorials/dde/images/edit_description.jpg" alt="Editing the description of a property" width="30%" %}

* __Saving, restoring and submitting work on a property__
  * Save your work locally regularly (it will be saved to your browser's data so clearing your browser's data may cause your files to be lost)
    * Click on "save/load progress" on the top dark gray bar
    * Use the "Select Action" drop down menu to ‘save’ your work
{% include image.html file="/tutorials/dde/images/save-progress-1.png" alt="Save your progress" width="40%" %}{% include image.html file="/tutorials/dde/images/save-progress-2.png" alt="Save your progress" width="40%" %}
* The DDE editor will tell you if there is any property that still need validation rules

{% include image.html file="/tutorials/dde/images/validation_warning.jpg" alt="Validation warning" width="20%" %}

* Add validation rules as needed via the drag-and-drop interface in the DDE validation editor

#### 2.5 Download / Save your JSON-LD schema
* Downloading your DDE-generated schema
  * Click the download button 
{% include image.html file="/tutorials/dde/images/download_schema.png" alt="Download schema" width="80%" %}
  * Name your DDE-generated file, and click download
  * Your JSON-LD file should follow the appropriate naming convention
  ```
  (Profile Name)_v(version)-(DRAFT|RELEASE).(json|jsonld)
  ```
    * example 1 - LabProtocol_v0.6-DRAFT.json
    * example 2 - Gene_v1.0-RELEASE.json
* Interpreting the validation warnings
  * The DDE will automatically check your schema for JSON validation rules and give warnings if they are missing
  * Revisit the DDE validation editor and add JSON Schema validation rules to the properties that lack them

### Step 3 - Save your JSON-LD to the Bioschemas Specification Repository and create a pull request
* Go to the [Bioschemas Specification repository](https://github.com/BioSchemas/specifications) 
* Create a [new branch](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-branches-in-your-repository/viewing-branches-in-your-repository) or [fork the repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
* In your branch or fork, and find your specification
* Add your JSON-LD to the `jsonld` directory for your specification
* Create a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) for your fork or branch
  * Include any issues you encountered from your test that you were unable to address


