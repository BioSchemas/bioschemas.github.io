---
layout: default
title: Profile Update
nextTutorial:
  link: ./new_profile
  title: Create a New Profile
---
# Update a Profile

You have come to a community consensus on changes needed to a profile that already exists. Congratulations! Now you have to update the Bioschemas website. Note, if you are comfortable with JSON schema and JSON-LD, you are welcome to copy, paste, and edit the JSON-LD files in the Bioschemas Specifications repository (and skip directly to step 6 below)

### Step 1 - Log in
{% include_relative login_to_dde.md %}

### Step 2 - Prepare the profile for update
2.1 Find the profile in the Registry
* On the Registry page, select “Browse By Namespace”
<br><img src="/pages/_tutorials/dde/images/namespace-search-1.png" width="80%"></img>
* Select ‘bioschemas’ or ‘bioschemasdraft’ depending on whether you are updating a release or draft profile
<br><img src="/pages/_tutorials/dde/images/select-profiles.png" width="80%"></img>
* Search for the name of the profile to be updated
<br><img src="/pages/_tutorials/dde/images/extend-specification.png" width="80%"></img>
* Click ‘extend’ (icon on the right at the end of the row corresponding to the profile name)

2.2 Follow the prompts to update your profile
* Create a temporary namespace (it will get replaced later on). Please use PascalCase for your temporary namespace. This step might timeout.
<br><img src="/pages/_tutorials/dde/images/create-temp-namespace.png" width="80%"></img>
* Fill in the form to create the updated profile version including the name of the profile and a description. The description should include:
  * The description of the class as determined by the community
  * The version of the class
  * Any descriptions of changes between versions
  * The name of the person who prepared the changes
* Click submit when you are done
<br><img src="/pages/_tutorials/dde/images/fill-out-spec-form.png" width="80%"></img>

2.3 Select minimum, recommended and optional properties of your profile
* You can select properties from all parent classes. Each parent class will be displayed on a blue box. 
* The  minimum (aka requested/mandatory), recommended, and optional properties are automatically shown from the latest available profile you selected in 2.1.
* You can select additional properties or unselect those that are no longer needed for the updated version.
* To update properties for a particular parent class, click on the “...” icon on the right of that parent class. This will open up a list of all availables properties for this class. 
  * If a property should be included in the profile, you should (i) select it with the checkbox icon, and (ii) define its marginality (red star for minimum, yellow circle for recommended, turquoise square for optional)
  * If a property should NOT be part of the profile, make sure it is NOT selected (i.e., checkbox icon should be grey)
  * Change the selection checkbox icon and marginality buttons as needed for each available property
*  Special property: conformsTo
  * "Uncheck" conformsTo as it will be added automatically via a script

### Step 3 - Add JSON validation rules to express property constraints
{% include_relative add_validation_rules.md %}

### Step 4 - Save your schema
{% include_relative save_your_schema.md %}

### Step 5 - Submit a pull request
{% include_relative save_to_specs_repo.md %}
