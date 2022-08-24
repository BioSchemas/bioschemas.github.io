---
title: How Bioschemas uses the training profiles with GitHub pages and Jekyll
overviewTutorial:
  link: ./community/
  title: Return to community tutorials overview


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
    name: (Markup provider, Markup consumer) People interested in adding Bioschemas markup to their own training resource when hosted via GitHub pages
  name: "How Bioschemas uses the training profiles with GitHub pages and Jekyll"
  author:
  - "@type": Person
    name: "Leyla Garcia"
    "@id": https://bioschemas.org/people/LeylaGarcia
    url: https://bioschemas.org/people/LeylaGarcia
  dateModified: 2022-08-24
  description: "In this how-to, we will show you how Bioschemas uses Jekyll layouts to include training profiles on their markup"
  keywords: "schemaorg, markup, structured data, Bioschemas, Bioschemas Training Group"
  license: CC-BY 4.0
  version: 1.0
---

## 1. Overview

This tutorial will show you how Bioschemas uses the Jekyll layouts to add markup to its pages. In particular, we will focus on Training profiles. If you are interested in a more comprenhensive tutorial (more a hands-on that a demo like this one) on how to add Bioschemas markup to GitHub pages, you should visit our tutorial ["Adding markup to GitHub pages"](/tutorials/howto/howto_add_github).

## 2. Bioschemas profiles for training resources

Main training related resources will include pages describing tutorials or courses. As such, they are marked up with Bioschemas using the follwoing three profiles:
* `TrainingMaterial`, a profile describing training materials in life sciences, it can be used on its own (as it happens with the Bioschemas tutorials) or in combination with a `CourseInstance`.
* `Course`, a profile describing a course from a generic point of view, i.e., a course that might have or not instances associated to a particular edition of that course.
* `CourseInstance`, a profile describing a particular instance of a course, i.e., an edition of a course that is scheduled for specific dates and happening in a specific location (that of course can be online or on-site, virtual or real). This profile is used in tandem with `Course`, i.e., a `CourseInstance` does not exist without a `Course`.

More information on how to select the right profile and how to combine them is provided on the tutorial ["Choosing a profile"](/tutorials/howto/howto_right_profile).

## 3. How Bioschemas adds markup to its web pages

Bioschemas takes advantage of the Jekyll layouts. Our Bioschemas deafult layout includes a `HTML` that will be added to the `HEAD` element of any page

```
{% raw %}
<!DOCTYPE html>
<html lang="en">
<html>
  {% include head.html %}
  <body>
    {% include header.html %}
    {% include navbar.html %}
    <div class="container min-vh-100">
      <main id="main" class="my-5">
        {{ content }}
      </main>
    </div>
    {% include footer.html %}
  </body>
</html>
{% endraw %}
```

The `head.html` will look for a `YAML` element named `bioschemas` and will display it as `JSON`

```
{% raw %}
<script type="application/ld+json">
  {{ page.bioschemas | jsonify }}
</script>
{% endraw %}
```

## 3. Example profiles for Bioschemas resources

Note: We are using examples that correspond to pages as they were displayed on the date that this tutorial was created (2022.08.24). If you explore those pages, some changes in the Bioschemas markup could have been introduced in upates after that date.

### `TrainingMaterial`

The `bioschemas` `YAML` element on the tutorial about ["Adding markup to GitHub pages"](/tutorials/howto/howto_add_github) looks like

```
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
    name: (Markup provider, Markup consumer) WebMaster, people deploying GitHub pages
  name: "Adding Schema.org to a GitHub Pages site"
  author:
  - "@type": Person
    name: "Niall Beard"
    "@id": https://bioschemas.org/people/NiallBeard
    url: https://bioschemas.org/people/NiallBeard
  contributor:
  - "@type": Person
    name: "Alasdair Gray"
    "@id": https://bioschemas.org/people/AlasdairGray
    url: https://bioschemas.org/people/AlasdairGray
  dateModified: 2021-07-22
  description: "This guide will show you how to do add Schema.org markup to a GitHub Pages site."
  keywords: "schemaorg, TeSS, GitHub pages"
  license: CC-BY 4.0
  version: 2.0
``` 

And it is rendered as JSON-LD on the website like

{% highlight json linenos %}
{
  "@context":"https://schema.org/",
  "@type":"LearningResource",
  "http://purl.org/dc/terms/conformsTo":{
    "@type":"CreativeWork",
    "@id":"https://bioschemas.org/profiles/TrainingMaterial/1.0-RELEASE"
  },
  "about":[{"@id":"https://schema.org"},{"@id":"http://edamontology.org/topic_0089"}],
  "audience":[
    {
      "@type":"Audience",
      "name":"(Markup provider, Markup consumer) WebMaster, people deploying GitHub pages"
    }
  ],
  "name":"Adding Schema.org to a GitHub Pages site",
  "author":[
    {
      "@type":"Person",
      "name":"Niall Beard",
      "@id":"https://bioschemas.org/people/NiallBeard",
      "url":"https://bioschemas.org/people/NiallBeard"
    }
  ],
  "contributor":[
    {
      "@type":"Person",
      "name":"Alasdair Gray",
      "@id":"https://bioschemas.org/people/AlasdairGray",
      "url":"https://bioschemas.org/people/AlasdairGray"
    }
  ],
  "dateModified":"2021-07-22",
  "description":"This guide will show you how to do add Schema.org markup to a GitHub Pages site.",
  "keywords":"schemaorg, TeSS, GitHub pages",
  "license":"CC-BY 4.0",
    "version":2.0
  }
{% endhighlight %}

### `Course` and `CourseInstance`

The `bioschemas` `YAML` element on the [course ofered at the conference SWAT4HCLS 2022](/meetings/2022-01_SWAT4HCLS_leiden) (i.e., we have here a `Course` with a specific `CourseInstance`, the one corresponding to its edition for the SWAT4HCLS 2022 conference) looks like 

```
bioschemas:
  "@context": https://schema.org/
  "@type": Course
  "http://purl.org/dc/terms/conformsTo":
  - "@type": CreativeWork
    "@id": "https://bioschemas.org/profiles/Course/0.9-DRAFT-2020_12_08"
  description: "Bioschemas Tutorial at SWAT4HCLS Leiden"
  keywords: "Bioschemas, SWAT4HCLS, Schema validation, Harvesting markup, Deploying markup"
  name: "Bioschemas - Deploying and Harvesting Markup"
  hasPart:
    - "@type": LearningResource
      "@id": "https://dx.doi.org/10.4126/FRL01-006432243"
      "http://purl.org/dc/terms/conformsTo":
        - "@type": CreativeWork
          "@id": "https://bioschemas.org/profiles/TrainingMaterial/1.0-RELEASE"
      description: "Bioschemas Tutorial at SWAT4HCLS Leiden"
      keywords: "Bioschemas, SWAT4HCLS, Schema validation, Harvesting markup, Deploying markup"
      name: "Bioschemas - Deploying and Harvesting Markup"
  hasCourseInstance:
    - "@type": CourseInstance
      "http://purl.org/dc/terms/conformsTo":
        - "@type": CreativeWork
          "@id": "https://bioschemas.org/profiles/CourseInstance/0.8-DRAFT-2020_10_06"
      courseMode: "online"
      location: "Virtual, and Fletcher Wellness-Hotel, Leiden, The Netherlands"
      startDate: "2022-01-10"
      endDate: "2022-01-10"
      inLanguage: en
      url: "https://www.swat4ls.org/workshops/leiden2022/"
      instructor:
        - "@type": Person
          name: "Alban Gaignard"
          "@id": https://bioschemas.org/people/AlbanGaignard
          url: https://bioschemas.org/people/AlbanGaignard
        - "@type": Person
          name: "Leyla Jael Castro"
          "@id": https://bioschemas.org/people/LeylaGarcia
          url: https://bioschemas.org/people/LeylaGarcia  
        - "@type": Person
          name: "Alasdair Gray"
          "@id": https://bioschemas.org/people/AlasdairGray
          url: https://bioschemas.org/people/AlasdairGray 
```

And it is rendered as JSON-LD on the website like

{% highlight json linenos %}
{
  "@context":"https://schema.org/",
  "@type":"Course",
  "http://purl.org/dc/terms/conformsTo":{
    "@type":"CreativeWork",
    "@id":"https://bioschemas.org/profiles/Course/0.9-DRAFT-2020_12_08"
  },
  "description":"Bioschemas Tutorial at SWAT4HCLS Leiden",
  "keywords":"Bioschemas, SWAT4HCLS, Schema validation, Harvesting markup, Deploying markup",
  "name":"Bioschemas - Deploying and Harvesting Markup",
  "hasPart":[
    {"@type":"LearningResource",
    "@id":"https://dx.doi.org/10.4126/FRL01-006432243",
    "http://purl.org/dc/terms/conformsTo":{
      "@type":"CreativeWork",
      "@id":"https://bioschemas.org/profiles/TrainingMaterial/1.0-RELEASE"
    },
    "description":"Bioschemas Tutorial at SWAT4HCLS Leiden",
    "keywords":"Bioschemas, SWAT4HCLS, Schema validation, Harvesting markup, Deploying markup",
    "name":"Bioschemas - Deploying and Harvesting Markup"
    }
  ],
  "hasCourseInstance":[
    {
      "@type":"CourseInstance",
      "http://purl.org/dc/terms/conformsTo":{
        "@type":"CreativeWork",
        "@id":"https://bioschemas.org/profiles/CourseInstance/0.8-DRAFT-2020_10_06"
      },
      "courseMode":"online",
      "location":"Virtual, and Fletcher Wellness-Hotel, Leiden, The Netherlands",
      "startDate":"2022-01-10",
      "endDate":"2022-01-10",
      "inLanguage":"en",
      "url":"https://www.swat4ls.org/workshops/leiden2022/",
      "instructor":[
        {
          "@type":"Person",
          "name":"Alban Gaignard",
          "@id":"https://bioschemas.org/people/AlbanGaignard",
          "url":"https://bioschemas.org/people/AlbanGaignard"
        },{
          "@type":"Person",
          "name":"Leyla Jael Castro",
          "@id":"https://bioschemas.org/people/LeylaGarcia",
          "url":"https://bioschemas.org/people/LeylaGarcia"
        },{
          "@type":"Person",
          "name":"Alasdair Gray",
          "@id":"https://bioschemas.org/people/AlasdairGray",
          "url":"https://bioschemas.org/people/AlasdairGray"
        }
      ]
    }
  ]
}
{% endhighlight %}

Note that the [same page](meetings/2022-01_SWAT4HCLS_leiden) includes markup for three profiles `Course` and `CourseInstance` which both in tandem correspond to the actual page for the [Bioschemas course at SWAT4HCLS 2022](/meetings/2022-01_SWAT4HCLS_leiden) while the `TrainingMaterial` element points to an external location with its own `@id` corresponding to the [DOI:FRL01-006432243](https://dx.doi.org/10.4126/FRL01-006432243)
