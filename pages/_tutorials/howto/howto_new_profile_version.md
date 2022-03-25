---
title: How to update a profile
previousTutorial:
  link: ./howto/howto_create_new_profile
  title: How to create a new draft profile


bioschemas:
  "@context": https://schema.org/
  "@type": LearningResource
  "http://purl.org/dc/terms/conformsTo":
  - "@type": CreativeWork
    "@id": "https://bioschemas.org/profiles/TrainingMaterial/0.9-DRAFT-2020_12_08/"
  about:
    - "@id": https://schema.org
    - "@id": http://edamontology.org/topic_0089
  audience:
  - "@type": Audience
    name: (Specification developer) People interested in creating and publishing a new draft profile
  name: "How to update a profile"
  author:
  - "@type": Person
    name: "Leyla Garcia"
    "@id": https://bioschemas.org/people/LeylaGarcia
    url: https://bioschemas.org/people/LeylaGarcia
  contributor:
  - "@type": Person
    name: "Alban Gaignard"
    "@id": https://bioschemas.org/people/AlbanGaignard
    url: https://bioschemas.org/people/AlbanGaignard   
  - "@type": Person
    name: "Alasdair Gray"
    "@id": https://bioschemas.org/people/AlasdairGray
    url: https://bioschemas.org/people/AlasdairGray
  dateModified: 2021-10-13
  description: "In this how-to, we will guide you through the necessary steps for you to update a profile, i.e.,create and publish a new draft profile, you need some knowledge on spreadsheets, GitHub, git and Jekyll."
  keywords: "schema.org, markup, structured data, bioschemas profile"
  license: CC-BY 4.0
  version: 1.1
---

## 1. Prepare your working environment

To update a profile you need access to a couple of Bioschemas resources, here we list them all together with the main role they play in the whole process. We will explain how to use them and what to do with them in later steps.

* Bioschemas specifications [GDrive folder](https://drive.google.com/drive/folders/0B8yXU9SkT3ftaWJtTGYyTTJjck0): to create the spreadsheet corresponding to the new draft profile, you need editing rights
  * Note 1: a specification in Bioschemas defines either a type (existing in Schema.org or created by Bioschemas) or a profile (set of rules on how to use a type). A type specification corresponds to a set of relations, aka properties, between the described type and other types (for instance, the specification for the [type Protein](/types/Protein) includes a property ```associatedDisease``` describing how a relation between a protein and a disease). A profile specification selects the most useful properties for a given type and provides additional information on cardinality, marginality and controlled vocabularies (for instance, the specification for the [Protein profile](/profiles/Protein/) indicates that the property ```associatedDisease``` is recommended and has cardinality MANY)
  * Note 2: a GDrive, short for Google Drive, is a file storage and synchronization service developed by Google. Bioschemas uses a GDrive folder to host information related to, for instance, specifications
* [GOWeb repository](https://github.com/BioSchemas/bioschemas-goweb): to move from the spreadsheet to the website
* [Website repository](https://github.com/BioSchemas/bioschemas.github.io): to publish the new draft profile, you need editing rights
* [Specifications repository](https://github.com/BioSchemas/specifications): to add compliant examples regarding the new draft profile, you need editing rights

If you do not have the right permissions to edit the mentioned resources, send an email to the [mailing list](mailto:public-bioschemas@w3.org) explaining why you should have access and what Bioschemas group you belong to. Once your case has been validated, you will get an invitation to join the GDrive and the repositories.

From now on, we will use [ScholarlyArticle](/profiles/ScholarlyArticle) as an example to create and publish a new draft profile.

## 2. Create a new profile crosswalk

A profile crosswalk is the cornerstone of Bioschemas profile development. It is a spreadsheet with the Schema.org fields to be considered together with cardinality, marginality, suggested controlled vocabularies and examples. It is not a regular spreadsheet but one with a template and some predefined functionalities. It is then translated into structured data so that the Bioschemas web site is automatically updated.

A new profile is commonly based on the previous one so the easiest way to start is from the previous version.

* Go to the [GDrive](https://drive.google.com/drive/folders/0B8yXU9SkT3ftaWJtTGYyTTJjck0) and navigate to the folder [Specifications](https://drive.google.com/drive/folders/0Bw_p-HKWUjHoNThZOWNKbGhOODg)
* Locate and open the folder corresponding to the profile you want to update, in our example it is the [ScholarlyArticle folder](https://drive.google.com/drive/folders/1CgEyta4d7vFfYT7r7w9HtLZ4kAidDmJI)
* Create a copy of the latest ScholarlyArticle Mapping file. At the time of writing, it was the ScholarlyArticle Mapping 0.2-DRAFT
  * Note: a mapping file corresponds to a Google spreadsheet and it is the way that Bioschemas uses to do a crosswalk on a profile before adding it to the website. Bioschemas groups will work first on this crosswalk (mapping file, spreadsheet) and when it is ready to go (i.e., the involved people is happy with the content, it has been reviewed and approved), it can be published to the website
* Rename the copy so it reflects the new draft version, in this case it would be ScholarlyArticle Mapping 0.3-DRAFT

_Note that the properties `@id`, `@type`, `@context`, and `dct:conformsTo` are automatically added as minimal properties to all profiles and are not present in the GSheet._

We will now discuss the different tabs in the spreadsheet and how they are used in updating a profile.

### 2.1. The Specification Info tab

In this tab, you need to update the "Description" column. In most cases the actual description of the profile will remain the same but the "Summary of Changes" will change. List all the changes in this new draft profile, use a HTML list markup for that, below there is an example:

```

<h4>Summary of Changes</h4>
    Changes since previous draft 0.1 of the ScholarlyArticle profile:
    <ul>
      <li>Add examples</li>
      <li>Updates identifier property to MANY so multiple identifiers can be included</li>
      <li>Uses name for the title (as per Schema.org examples) and keeps headline (optional) for compatibility purposes</li>
      <li>Update ranges as per latest version of Schema.org</li>   
    </ul>

```

You will also need to update:
* the "version" column with the new version
* the "Full Example" column with the link pointing to examples for this new version, see more on the [Update examples](#6-update-examples) section

You should update the column "Official Type" if and only if you modified the main parent type from Schema.org. For instance, in previous versions the Bioschemas TrainingMaterial profile had CreativeWork as the main parent Schema.org type but it was changed to LearningResource from version 0.8

### 2.2. The Schema.org mapping tab

Here you will make the changes to the profile. There are a couple of possibilities here.
* You want to update a property that already exists (e.g., there is typo, description should be updated, a new controlled vocabulary will be added, a new example is necessary, expected Schema.org types have changed, etc.)
  * Go to the column you want to change and update it as needed, some examples include
    * Changing the marginality (column 'Marginality') or cardinality (column 'Cardinality') by selecting the new desired one from the provided drop-box list
    * Adding or modifying a tailor Bioschemas definition by directly entering the text in the corresponding column 'BSC Description'
    * Adding or modifying the mini example for a particular property by entering the text in the corresponding column 'Example', remember to use JSON-LD syntax for this
* You want to add a new property
  * If it is a property belonging to a parent type already recorded, see Figure 1 below. Our ScholarlyArticle example already extends ScholarlyArticle, Article, CreativeWork and Thing
    * Add a new column under the corresponding type. Let's suppose you want to add the property "wordCount" that comes from the type Article
    * Go to the parent type in Schema.org, in this case [Article](https://schema.org/Article) and copy the property name, the expected types and the description and paste them on the first three columns of the row you just created
    * Fill in the rest of the columns as needed (remember, columns "Type" and "Type URL" should be left empty)
  * If it is a property belonging to a new parent
    * Add a new row indicating what type is being extended
    * Follow the process as described for properties belonging to a parent already recorded

{% include image.html file="/tutorials/images/from_schema_to_spreadsheet.png" caption="Figure 1. From Schema.org to profile spreadsheet" alt="From Schema.org to profile spreadsheet" %}

## 3. Get the code for the new draft profile

Now you are ready to generate the machine-processable Bioschemas version of your new draft profile.

* Go to [GOWeb repository](https://github.com/BioSchemas/bioschemas-goweb) and get the executable version corresponding to your Operating System. If you need assistance with GOWeb send an email to the [mailing list](mailto:public-bioschemas@w3.org).
* Run GOWeb using the CSV file you created on the previous section [Publish the Bioschemas fields to the Web](#31-publish-the-bioschemas-fields-to-the-web)
* A YAML file will be created that is then used in the webpage for the new draft version

### 3.1 Publish the Bioschemas fields to the Web

Once you have finished with the changes on the spreadsheet, see previous section [Create a new profile crosswalk](#2-create-a-new-profile-crosswalk), go to the menu File/Publish to the web/, select "Bioschemas Fields" and "CSV", publish and copy the link, see Figure 2 below.

{% include image.html file="/tutorials/images/publish-to-web.png" caption="Figure 2. Publish Bioschemas fields to the web" alt="Publish Bioschemas fields to the web" %}

## 4. Update the website

You are now ready to publish the new draft version on the Bioschemas website.

### 4.1. Create a new version page

* If you have not done so yet, clone the [Bioschemas website repository](https://github.com/BioSchemas/bioschemas.github.io) so you have a local copy
* Open your local copy in your preferred editor
* Go to `pages/_profiles/<your profile>`, in this case `pages/_profiles/ScholarlyArticle`
* Create a copy of the latest profile, in our case it is 0.2-DRAFT-2020_12_03.html
* Rename the copy so it reflects the new draft version, in our case it would be 0.3-DRAFT.html (having the dates as part of the draft name is no longer needed/desired)

### 4.2. Update the redirects

Updating the redirects depends on the status of the previous version
* If the previous version is a draft profile then remove the `redirect_from` property
* If the previous version is a release then the `redirect_from` property should be updated to

```yaml
redirect_from:
- "/profiles/ScholarlyArticle/"
```

  and the new draft version should have the following `redirect_from` property:

```yaml
redirect_from:
- "devSpecs/ScholarlyArticle/specification"
- "devSpecs/ScholarlyArticle/specification/"
- "/devSpecs/ScholarlyArticle/"
- "/specifications/drafts/ScholarlyArticle"
```

### 4.3. Update the content

Now on the new draft version file
* Update the previous version, in our case it would be ```previous_version: 0.2-DRAFT-2020_12_03```
* Update the ```cross_walk_url``` to point to the spreadsheet on the GDrive
* If you changed the parent type (very rarely it happens), you need to update the section ```parent_type```

Now you are ready to update the part corresponding to the spreadsheet, go to the ```spec_info``` section, it start with the lines

```yaml
  # spec_info content generated using GOWeb
  # DO NOT MANUALLY EDIT THE CONTENT
```

* Keep the two first lines only, i.e., remove from the line ```spec_info``` all the way to a line with three dashes ```---```, which is at the end of the file
* Add all the lines coming from the YAML file that you got from GO Web
* Save the file!

### 4.4. Update the profile version

You are now ready to update the profile version
* Go to the folder `_data` and locate the file ```profile_versions.yaml```
* Find there the profile you are updating, in this case ScholarlyArticle, and update the version, in this case it would be version 0.3-DRAFT

```yaml
ScholarlyArticle:
    name: "ScholarlyArticle"
    latest_publication: "0.3-DRAFT"
    latest_release:
    status: "active"
```

## 5. Get an overview on your local copy

Now you are ready to run the website locally, open a terminal and run ```jekyll serve``` (how to get Jekyll running is out of the scope of this tutorial, you will find more information on the topic in the [corresponding GitHub Help pages](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll)).

Open the local URL and navigate the pages corresponding to the profile that you just changed to make sure everything is working well.

## 6. Update examples

Regardless whether it was a minor or major change, it is always a good idea to have full examples on the [Specifications repository](https://github.com/BioSchemas/specifications)

* You can choose adding the examples directly on GitHub or on a local version
* Navigate to the examples folder corresponding to your profile, in this case it would be ScholarlyArticle/examples
* Create a new folder corresponding to your new draft, 0.3-DRAFT in this case
* Add there the new examples in JSON-LD format using the extension file ```json```
* If the examples for the previous version are fully compatible with the new version, it is ok if you add a note pointing to the previous examples rather than adding new ones
* On the examples, always remember to add the ```dct:conformsTo``` property so it points to your profile version, for example  
_Note that you should use the full IRI for the DCTerms property_
```json
"http://purl.org/dc/terms/conformsTo": {
  "@id": "https://bioschemas.org/profiles/ScholarlyArticle/0.3-DRAFT",
  "@type": "CreativeWork"
}
```

## 7. Create a Pull Request

Congratulations, you have created a new draft profile and are now ready to create a Pull Request on the [Bioschemas website repository](https://github.com/BioSchemas/bioschemas.github.io). Always suggest at least one possible reviewer as your PR cannot be merged unless one reviewer has approved it.
