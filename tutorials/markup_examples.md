---
layout: tutorial
title: Schema.org markup examples
previousTutorial:
  link: ./what_why_schema
  title: What and why schema.org
nextTutorial:
  link: ./what_why_bioschemas
  title: What and why Bioschemas

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
    name: (General interest, Markup provider, Markup consumer) People interested in Schema.org markup examples
  name: "Schema.org markup examples"
  author:
  - "@type": Person
    name: "Azerty Proxy"
  - "@type": Person
    name: "Alan Williams"
  contributor:
  - "@type": Person
    name: "Leyla Garcia"
    "@id": https://bioschemas.org/people/LeylaGarcia
    url: https://bioschemas.org/people/LeylaGarcia
  dateModified: 2021-07-26
  description: "With these examples you will get a better understanding of benefits brought by structure data, i.e., schema.org markup"
  keywords: "schemaorg, markup, structured data, example"
  license: CC-BY 4.0
  version: 3.0
---

## 1. Searching for a biology event in Google

By performing a simple search of biology events on Google, see Figure 1, we will have as a result a preview of the information about events even before going to the actual websites; information such as the date, title and description

| ![Figure 1: Biology event search in Google](/tutorials/images/google-biology-event-search.png) |
| __Figure 1: Biology event search in Google__ |

Displayed on the website you can find the same (and more) information for the event, see Figure 2.

| ![Figure 2: Event detail](/tutorials/images/google-event-detail.png) |
| __Figure 2: Biology event detail__ |

## 2. Schema.org behind the scenes

Behind the scenes metadata is used by Google to understand search resultts. In particular, it uses schema.org markup, see Figure 3.

	 {
	    "@context":"http://schema.org",
	    "@type":"Event",
	    "name":"Synthetic Biology Congress",
	    "url":"https://10times.com/synthetic-biology-congress",
	    "startDate":"2021-11-04",
	    "endDate":"2021-11-05",
	    "eventStatus":"EventScheduled",
	    "eventAttendanceMode":"https://schema.org/OfflineEventAttendanceMode",
	    "location":{
	       "@type":"Place",
	       "name":"Novotel London West Hotel",
	       "address":{
	          "@type":"PostalAddress",
	          "streetAddress":"Hammersmith International Ctre, 1 Shortlands, London W6 8DR",
	          "addressLocality":"London",
	          "addressRegion":"England",
	          "addressCountry":"UK"
	       },
	       "geo":{
	          "@type":"GeoCoordinates",
	          "latitude":"51.491966",
	          "longitude":"-0.220088"
	       }
	    },
	    "organizer":{
	       "@type":"Organization",
	       "name":"Oxford Global Conferences Ltd",
	       "url":"https://10times.com/company/oxford-global-conferences"
	    },
	    "image":[
	       "https://c1.10times.com/industry/53.jpg",
	       "https://c1.10times.com/map/venue/4966.png"
	    ],
	    "description":"The Synthetic Biology Congress brings together over 600 senior-level delegates representing internationally renowned research &amp; academic institutions, clinical research institutions and pharmaceutical companies and it features over 20 case studies and presentations demonstrating the latest synthetic biology tools and their therapeutic applications."
	 }

| __Figure 3: Biology event HTML__ |

The markup `"eventStatus":"EventScheduled"` is referencing the property described on https://schema.org/Event and 'EventScheduled' is one of the options for an EventStatusType - https://schema.org/EventStatusType, see Figures 4 and 5.

| ![Figure 4: Event markup definition](/tutorials/images/event-type.png) |
| __Figure 4: Event markup definition__ |

| ![Figure 5: Event status definition](/tutorials/images/event-status-type.png) |
| __Figure 5: Event status definition__ |

