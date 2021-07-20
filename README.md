# Bioschemas Website
This repo contains the files for the Bioschemas website. The website is deployed on [GitHub](https://github.com/) using [Jekyll](https://jekyllrb.com/).

## Getting Started

If you already have Ruby installed on your machine, then the following files will allow you to get started by installing the relevant dependencies:

- Install Jekyll and Dependencies: ```gem install jekyll bundler jekyll-redirect-from``` and ```gem install jekyll-sitemap```
- Clone the repository: ```git clone https://github.com/Bioschemas/bioschemas.github.io.git```
- Run the website: ```jekyll serve```

If you need more help with installing Jekyll, then see their [installation instructions](https://jekyllrb.com/docs/installation/) for full details.

Note, if you use the GitHub pages documentation, then you will need a `Gemfile` with the following contents

```ruby
source 'https://rubygems.org'
gem 'github-pages', group: :jekyll_plugins
```
