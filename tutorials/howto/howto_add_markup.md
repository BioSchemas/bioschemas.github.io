---
layout: tutorial
title: How to mark up your own resource with Bioschemas
previousTutorial:
  link: ./howto/howto_right_profile
  title: How to select the right profile
nextTutorial:
  link: ./howto/howto_add_github
  title: How to add markup to GitHub pages

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
    name: (Markup provider, Markup consumer) WebMaster, people interested in adding Bioschemas markup to their website
  name: "How to mark up your own resource with Bioschemas"
  author:
  - "@type": Person
    name: "Leyla Garcia"
    "@id": https://bioschemas.org/people/LeylaGarcia
    url: https://bioschemas.org/people/LeylaGarcia
  contributor:
  - "@type": Person
    name: "Ricardo Arcila"
    "@id": https://bioschemas.org/people/RicardoArcila
    url: https://bioschemas.org/people/RicardoArcila
  - "@type": Person
    name: "Victoria Dominguez del Angel"
    "@id": https://bioschemas.org/people/VictoriaDominguezDelAngel
    url: https://bioschemas.org/people/VictoriaDominguezDelAngel/
  dateModified: 2021-07-22
  description: "In this how-to, we will guide you through the necessary steps in order to get a JSON-LD markup describing your own resource using a Bioschemas profile"
  keywords: "schemaorg, markup, structured data, bioschemas"
  license: CC-BY 4.0
  version: 2.0
---

<table>
  <tbody>
    <tr>
      <td align="center">
        <img src="/tutorials/images/exclamation_mark.png" alt="warning">
      </td>
      <td>
        If have not read yet our <a href="./howto_right_profile">how to select the right profile for your resource</a>, please give it a try before this one.
      </td>
    </tr>
  </tbody>
</table>

## 1. A pre-markup brainstorming activity

If you are eager to markup your resource, get your hands "coding" and quickly see some structured data rather that free text, you can skip this section and jump to the next one. However, if you want to go step by step and then smoothly move forward and get some JSON-LD for your resource, please stay here, you are on the right place.

## 2. Define your strategy

If your resource involves more than one profile, you first need to define the strategy that suits best to your case. You can link a profile, let's say DataCatalog, to other related ones, let's day Dataset, via properties. Sometimes those properties are bidirectional, so you can go from DataCatalog to Dataset or the other way around. Which direction suits best to you?

<table>
  <tbody>
    <tr>
      <td align="center">
        <img src="/tutorials/images/information_mark.png" alt="info">
      </td>
      <td>
        Link from DataCatalog to Dataset if you have some few datasets and you introduce them all on your catalog landing page. Example: UniProt
        <br/>
        Link from Dataset to DataCatalog if you have that many datasets than rather than list them all, you provide a search and retrieval mechanism to find them. Example: identifiers.org
      </td>
    </tr>
  </tbody>
</table>

## 3. Map elements to properties

Now, focus on a particular profile, have at hand the [corresponding specification page on Bioschemas](/specifications/) as well as your resource, i.e., your web pages. Do a manual exercise mapping elements to properties. This will help you have a clearer idea on what you want to achieve once you go and use gimme-my-jsonld (see next section). You might need more than one iteration here as you can face multiple option at the beginning, choose that one that gives more benefits. Keep in mind your goal by adding this mark up to your resource.

## 4. Add markup to your page

Now that you have identified those elements on your web page that you want to mark up, it is time to add the markup to your page. Yo will need to decide what format to use, how to add the markup and where to add it.

### 4.1. Formats

As disccused on the introduction to schema.org, there are [multiple formats](https://bioschemas.org/tutorials/what_why_schema#3-schemaorg-formats) that can be used to add structured markup to web pages. Bioschemas mainly supports JSON-LD so this is the format used for examples and so.

### 4.2. How add the markup

Here we have two possibilities: manually or automatically adding the markup. 

Depending on how the data is rendered on your website, there might be a production pipeline behind your web pages. If this is the case, web developers will decide the best way to programmatically add the Bioschemas markup. This is commonly the case for registries/repositories or data/knowledge bases. For instace, the [Ensembl Genome Browser](https://www.ensembl.org) provides information on genomes and has integrated the Bioschemas markup to their production pipeline. Thus, whenever you visit an Ensembl gene page you get not only the HTML but also the JSON-LD. 

For websites without a production pipeline behind, those where you manually edit the HTML yourself, you will have to add the markup by hand. For instance, if you organize a half-day workshop with less than 10 accepted papers, you could add the corresponding markup by hand. This is the case for the [Research Objects Management for Linked Open Science Workshop](https://zbmed.github.io/damalos) which includes bibliographic markup for the [submissions on 2020](https://zbmed.github.io/damalos/docs/2020.html). The workshop web page is based on GitHub pages and the markup for the publications was manually added at the [end of the corresponding MarkDown document](https://github.com/zbmed/damalos/blob/master/docs/2020.md). 

### 4.3. Where to add the markup

You can put the JSON-LD corresponding to your markup anywhere within the HTML where a ```<script>``` element is allowed. You can choose between having multiple ```<script type="application/ld+json">``` elements or only one. 

If you choose to have multiple ```<script type="application/ld+json">``` elements, most likely you want them close to the corresponding HTML. For instance, if you visit the gene page [BRCA2](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139618;r=13:32315086-32400268) at Ensembl, you will observe the following gene summary.

![Figure 1: BRCA2 gene summary](/tutorials/images/brca_gene_summary.png)

**Figure 1**: BRCA2 gene summary

<br/>

This summary corresponds to a two-colum ```<div>``` used to show the name, CCDS, UniProtKB and so. In Figure 2, we show the respective HTML code where the two-column ```<div>``` is highlithed in blue and the row corresponding to the Ensembl version has been expanded. Below this ```div>``` appears the JSON-LD with the corresponding markup.

![Figure 2: Code corresonding to the BRCA2 gene summary](/tutorials/images/brca_gene_html.png)


**Figure 2**: Code corresonding to the BRCA2 gene summary

<br/>

If you want to include only one ```<script type="application/ld+json">``` with all the markup relevant to your page, a common option is adding the JSON-LD at the end of the HTML code so it will not interfere with the rendering of the page.

If your page is not too big, you can also choose to have the JSON-Ld at the beginning of the HTML code as part of the ```<head>```. This is the way used for Bioschemas how-to pages as shown in Figure 3 where the JSON-LD is highlithed in blue. 

![Figure 3: JSON-LD as part of the head](/tutorials/images/code_on_head.PNG)

**Figure 3**: JSON-LD as part of the head





