# website
Files for the Bioschemas website.

The website is deployed using [Jekyll](https://jekyllrb.com/). 

## Geting Started

See [installation instructions](https://jekyllrb.com/docs/installation/) for full details of installing Jekyll. Below are a quick set of commands that should hopefully get you going:

- Install Jekyll and Dependencies: ```gem install jekyll bundler jekyll-redirect-from```
- Clone the repository: ```git clone https://github.com/BioSchemas/bioschemas.github.io.git```
- Run the website: ```jekyll serve```

## Specifications subtree update
1. ```git subtree pull --prefix=_bsc_specs/ --squash subtree_specs master -m "[commit message]"```
2. ```git push origin master```


## Specifications subtree creation

1. Reference to specifications repository using as local alias **subtree_specs** ```git remote add subtree_specs https://github.com/BioSchemas/specifications.git```
2. Subtree creation, the subtree is stored in the dir **_bsc_specs**, represented in the subtree command by the prefix value. ```subtree add --prefix=_bsc_specs/ subtree_specs master```
3. ```git push origin master```



