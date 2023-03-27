---
title: Create New Type
previousTutorial:
  link: ./dde/update_type
  title: Type Update
nextTutorial:
  link: ./dde/review_a_specification_pull_request
  title: Review a pull request on a Bioschemas Specification
  
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
    name: People interested in creating a new Bioschemas type
  name: "How to create a new Bioschemas Type with the Data Discovery Engine (DDE) Schema Playground"
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
  description: "In this how-to, we will guide you through the necessary steps in order to create a new Bioschemas type"
  keywords: "schemaorg, markup, structured data, bioschemas"
  license: CC-BY 4.0
  version: 0.2

---

You have come to a community consensus on creating a new type. Congratulations! Now you have to add the new type on the Bioschemas website.
 Note, if you are comfortable with JSON schema and JSON-LD, you are welcome to copy, paste, and edit the JSON-LD files in the Bioschemas Specifications repository

### Step 1 - Log in
{% include_relative login_to_dde.md %}

### Step 2 - Creating the type
#### 2.1 Find the parent type/class of the new type in the Registry
* DDE classes are commonly known as ‘types’ in schema.org and ‘specifications’ in Bioschemas
* If the parent type/class is from schema.org, search for it in the search bar in the ‘Search By Class Name’ tab 
* If the parent type/class is from bioschemas:
  * On the Registry page, select “Browse By Namespace”
  * Select ‘bioschemastypes’ or ‘bioschemastypesdraft’ depending on whether the parent class is a released or draft type.


{% include image.html file="/tutorials/dde/images/select-namespace-type.png" alt="Browse types in the DDE by namespace" width="80%" %}

* Search for the name of the parent class (ie- the parent type) using the search box
* Click ‘extend’ (icon on the right at the end of the row corresponding to the parent class)

{% include image.html file="/tutorials/dde/images/extend_bioschemas_parent.png" alt="Selecting a bioschemas type to extend" width="80%" %}

#### 2.2 Follow the prompts to create your new type
* Create a temporary namespace that will help us identify your working space  
* Fill in the form to create the new type including the name of the type and a description. The description should include:
  * The description of the type as determined by the community
  * The version of the type
  * The name of the person who prepared the type
  
  __You will not be able to change this information on the next steps so make sure it is correct before moving on.__

{% include image.html file="/tutorials/dde/images/fill-out-spec-form.png" alt="Complete the web form for the type" width="80%" %}

#### 2.3 Create any new properties needed for your type
* All properties from all parent classes (note: classes are commonly known as ‘types’ in schema.org and Bioschemas) are automatically inherited. Each parent class is displayed in a blue box.
* To __create an entirely new property__
  * Any schema.org properties that are not available in a parent class will need to be created.
  * Click on the (+) icon 
  * Enter the name and description of your property into the form (see screenshot of property creation form)
  * The Domain will automatically be populated from the class
* __Specifying the expected (range) input type__
  * Enter/search for the expected type of your property into the (range) input type(s) of the form. (see screenshot of setting an expected range type or input)
  * Clicking on a class will usually be sufficient to add it as an expected type; HOWEVER, for schema:URL or schema:Text, you will need to click on the Add button.
  * To specify a __bioschemas type as the expected (range) input type__
    * __Enter it manually__ into the __expected (range) input type box__ as “namespace:class”
      * Eg- bioschemastypes:BioSample
      * Eg2- bioschemastypesdrafts:Phenotype
* __Saving, restoring and submitting work on a property__
  * Save your work locally regularly (it will be saved to your browser's data so clearing your browser's data may cause your files to be lost)
    * Click on "save/load progress" on the top dark gray bar
    * Use the "Select Action" drop down menu to ‘save’ your work
{% include image.html file="/tutorials/dde/images/save-progress-1.png" alt="Save your progress" width="40%" %}{% include image.html file="/tutorials/dde/images/save-progress-2.png" alt="Save your progress" width="40%" %}

#### 2.4 Download / Save your JSON-LD schema
* Downloading your DDE-generated schema
  * Click the download button 
{% include image.html file="/tutorials/dde/images/download_schema.png" alt="Download schema" width="80%" %}
  * Name your DDE-generated file, and click download
  * Your JSON-LD file should follow the appropriate naming convention
  ```
  (Type Name)_v(version)-(DRAFT|RELEASE).(json|jsonld)
  ```
    * example 1 - LabProtocol_v0.3-DRAFT.json
    * example 2 - Gene_v0.3-RELEASE.json (note, you cannot create a new type RELEASE without approval from the Steering Council)
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
