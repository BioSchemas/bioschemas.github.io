## Check a pull request for a new or updated specification:

### Step 1 - Verify the parent class is correct. If not, edit the JSONLD to fix it
{% include_relative edit_your_jsonld.md %}

### Step 2 - Verify that the JSONLD schema file is working properly
{% include_relative check_your_spec.md %}

### Step 3 - Edit the configuration files in the bioschemas website repository
Detailed instructions [here](https://hackmd.io/zGOAxx-BRfi4rDiaW9Rk4Q?both)

### Step 4 - Pull the JSONLD to the bioschemas Specification repository
{% include_relative save_to_specs_repo.md %}

### Step 5 - Update the bioschemas specification in the DDE schema registry
{% include_relative push_updates_to_dde.md %}
