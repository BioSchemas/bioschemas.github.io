---
title: RevisedLifeScienceEventSpecification
layout: post
author: roberto.preste
permalink: /copy_revised-life-science-event-specification/
source-id: 1XGfPXTouKwQE_HvQRZwN5Y4JxpfF40VdrwV1ow9FnOk
published: true
---
Life Science Event Specification 0.1

A specification for describing life sciences events

<table>
  <tr>
    <td>Note: the new properties proposed in this document have been posted to the Schema.org issues.</td>
  </tr>
</table>


# Recommendation [DAY] [MONTH] 2016

This version: [github link]

Latest published version: [github link]

Previous version: [github link]

Editors: [Names]

Authors: [Names]

Contributors: [Names]

# Abstract

The Life Science Events specification provides a way to describe bioscience events on the World Wide Web. It defines a set of metadata and vocabularies, built on top of existing technologies and standards, that can be used to represent events in Web pages and applications. The goal of the specification is to make it easier to discover, exchange and integrate life science event information across the Internet. 

# Status of this Document

This specification is under development. It is being written by a multi-institutional team from [ELIXIR](https://www.elixir-europe.org), [Pistoia Alliance](http://www.pistoiaalliance.org), [GOBLET](http://mygoblet.org), [TeSS](https://tess.elixir-uk.org), [BioSharing](https://biosharing.org) and [BBMRI](http://bbmri-eric.eu/). You can find more about the project and similar projects on the [bioschemas GitHub pages](https://github.com/BioSchemas). If you are interested in helping with this or any other of the listed projects, please visit the [Event Group](https://github.com/BioSchemas/bioschemas/wiki/Event-Group) page.

The document will be reviewed by the [Event Group](https://github.com/BioSchemas/bioschemas/wiki/Event-Group), following the [Standard Specifications Process](https://docs.google.com/document/d/1eDHBfw6frl9xAjIduLYRwcqUY3jehfzJ-xSKCc1nSsc/edit?usp=sharing) defined by the community BioSchemas group.

The work proposed in this document builds on top of previous meetings and discussions involving the organisations mentioned above plus [ISCB](http://www.iscb.org) and [SIB](https://www.isb-sib.ch). The research behind these new properties has been compiled into a [Google sheet](https://docs.google.com/spreadsheets/d/1RE2JBaFz_i1uo_nRA7swDBNZG5BodmcbXo5V_jScsTo/edit#gid=0). It uses terms agreed during these meetings, and builds on existing standards outlined at [Schema.org](https://schema.org).

# Table of Contents

[[TOC]]

# Introduction

## Problem statement

Conferences, workshops, meetings and events in general play a very important role in knowledge sharing and acquisition of new skills. Though there are several technological solutions for event sharing, events in life sciences are still not described in a consistent manner that would make them easy to discover, exchange or compare.

Because there is no single standard to follow, the dissemination, discovery and aggregation of events is not effective. As a result, the advertisement of an event in third party websites normally requires manual curation to shape the content to each provider's requirements.

## Proposed solution

### Rationale

In the development of the Life Science Events standard we have considered the following design goals.

#### *Consensus*

Many organisations and repositories providing events already exist. It is important this standard takes into account their experience and contribution. 

#### *Adoption*

Many organisations already have a website or system providing information about events. They will not be willing to change their methods unless there is a clear benefit and a low barrier for adoption. 

#### *Reuse*

There are existing formats and technologies suitable to represent at least some information about events. This specification will avoid reinvention and seek to extend existing standards.

### Goals

The Life Science Events specification aims to support the description, discoverability, exchange and aggregation of the event information in the life sciences. It will do this by working with the community to reach consensus on how to identify, describe and classify life science events. Components will include: 

* a data model, 

* a minimum information guideline, 

* controlled vocabularies, and

* tools.

The specification is designed to be unintrusive to event providers, minimising changes to the methods organisations currently use to advertise events. It aims to facilitate adoption by extending existing standards. The definition and classification of fields in the data model use standard specifications from Schema.org, and the dissemination of information is facilitated by making use of standards like Microdata, JSON-LD and RDFa. Fields that require controlled vocabularies will specify existing ontologies where possible.

### Scope

The document is intended for:

* **software developers** who are working on projects that need to advertise or aggregate events, and

* **users** who want to understand how event data can be described and discovered using this standard.

# Data model

The data model is based on the standards set out in Schema.org. [Schema.org](http://schema.org/) is a collaborative, community-driven project with a mission to create, maintain and promote schemas (types) for structured data on the Internet. These types (like Event, Person, Book) provide a standard for creating semantic markup in web pages and applications. 

Schema.org markup covers entities, relationships between entities and actions, and can easily be extended through a well-defined extension model. Over 10 million sites already use Schema.org to code their web pages, email messages, etc. Many applications from Google, Microsoft, Pinterest, Yandex and others also use Schema.org types.

The data model proposed involves: 

1. **Adopting the Schema.org Event type, and extending it with additional properties**. Schema.org already has a way of describing events, through its [Event type](https://schema.org/Event). In this document we suggest using this type to describe life science events, but we also suggest new properties for this type, so that event descriptions can be more accurate and useful in life sciences. If the community agrees, these additional properties will be put forward for adoption to Schema.org.

2. **Adopting a standard way of using the Schema.org Event type.**** **Many properties in the Schema.org Event type are loosely defined, and we propose guidelines on how to use them so that they are more specific and consistent.** **These guidelines include concepts not supported by Schema.org, such as cardinality, controlled vocabularies and content guidelines (minimum, optional and recommended fields). For example, we suggest the use of a controlled vocabulary based on the EDAM ontology for the 'topics' property. These recommendations will not be part of the Schema.org Event type, but are proposed as best practices in using that type in life science. 

In the table below, the existing Schema.org properties for the Event type are listed first, and the suggested new properties are listed afterwards (highlighted in blue). The research behind these new properties has been compiled into a [Google sheet](https://docs.google.com/spreadsheets/d/1RE2JBaFz_i1uo_nRA7swDBNZG5BodmcbXo5V_jScsTo/edit#gid=0).

## Event type definition

### Data fields

**Legend:**

*CN: Cardinality (one, many)*

*CG: Content Guideline (**M: minimum**; **R: recommended**; O: optional)*

*CV: Controlled Vocabulary*

<table>
  <tr>
    <td>Property</td>
    <td>Expected Type</td>
    <td>Description</td>
    <td>CN</td>
    <td>CG</td>
    <td>CV</td>
  </tr>
  <tr>
    <td>Existing properties in schema.org/Event</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>aggregateRating</td>
    <td>AggregateRating </td>
    <td>The overall rating, based on a collection of reviews or ratings, of the item.</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>attendee</td>
    <td>Organization  or Person</td>
    <td>A person or organization attending the event. Supersedes attendees.</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>doorTime</td>
    <td>DateTime </td>
    <td>The time admission will commence.</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>duration</td>
    <td>Duration </td>
    <td>The duration of the item (movie, audio recording, event, etc.) in ISO 8601 date format.</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>endDate</td>
    <td>Date </td>
    <td>The end date and time of the item (in ISO 8601 date format).</td>
    <td>One</td>
    <td>M</td>
    <td>    </td>
  </tr>
  <tr>
    <td>eventStatus</td>
    <td>EventStatusType </td>
    <td>An eventStatus of an event represents its status; particularly useful when an event is cancelled or rescheduled.</td>
    <td></td>
    <td></td>
    <td>x</td>
  </tr>
  <tr>
    <td>inLanguage</td>
    <td>Language  or Text</td>
    <td>The language of the content or performance or used in an action. Please use one of the language codes from the IETF BCP 47 standard. Supersedes language.</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>location</td>
    <td>Place or PostalAddress</td>
    <td>The location of the event, organization or action.</td>
    <td>One</td>
    <td>M</td>
    <td></td>
  </tr>
  <tr>
    <td>offers</td>
    <td>Offer </td>
    <td>An offer to provide this item—for example, an offer to sell a product, rent the DVD of a movie, or give away tickets to an event. Can use eligibleCustomerType and eligibleDuration properties to express any special offers.</td>
    <td>One</td>
    <td>O</td>
    <td></td>
  </tr>
  <tr>
    <td>organizer</td>
    <td>Organization  or Person</td>
    <td>An organizer of an Event.</td>
    <td>Many</td>
    <td>R</td>
    <td></td>
  </tr>
  <tr>
    <td>performer</td>
    <td>Organization  or Person</td>
    <td>A performer at the event—for example, a presenter, musician, musical group or actor. Supersedesperformers.</td>
    <td>Many</td>
    <td>O</td>
    <td></td>
  </tr>
  <tr>
    <td>previousStartDate</td>
    <td>Date </td>
    <td>Used in conjunction with eventStatus for rescheduled or cancelled events. This property contains the previously scheduled start date. For rescheduled events, the startDate property should be used for the newly scheduled start date. In the (rare) case of an event that has been postponed and rescheduled multiple times, this field may be repeated.</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>recordedIn</td>
    <td>CreativeWork </td>
    <td>The CreativeWork that captured all or part of this Event. Inverse property: recordedAt.</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>review</td>
    <td>Review </td>
    <td>A review of the item. Supersedes reviews.</td>
    <td>Many</td>
    <td>O</td>
    <td></td>
  </tr>
  <tr>
    <td>startDate</td>
    <td>Date </td>
    <td>The start date and time of the item (in ISO 8601 date format).</td>
    <td>One</td>
    <td>M</td>
    <td></td>
  </tr>
  <tr>
    <td>subEvent</td>
    <td>Event </td>
    <td>An Event that is part of this event. For example, a conference event includes many presentations, each of which is a subEvent of the conference. Supersedes subEvents.</td>
    <td>Many</td>
    <td>O</td>
    <td></td>
  </tr>
  <tr>
    <td>superEvent</td>
    <td>Event </td>
    <td>An event that this event is a part of. For example, a collection of individual music performances might each have a music festival as their superEvent.</td>
    <td>One</td>
    <td>O</td>
    <td></td>
  </tr>
  <tr>
    <td>typicalAgeRange</td>
    <td>Text </td>
    <td>The typical expected age range, e.g. '7-9', '11-'.</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>workFeatured</td>
    <td>CreativeWork </td>
    <td>Can be used to reference training materials.

</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Proposed new properties for the Event type</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>eventId</td>
    <td>Text </td>
    <td>Unique Id for the event.</td>
    <td>One</td>
    <td>O</td>
    <td></td>
  </tr>
  <tr>
    <td>prerequisite</td>
    <td>Text </td>
    <td>A list of prerequisites to be able to attend the event.</td>
    <td>Many</td>
    <td>R</td>
    <td></td>
  </tr>
  <tr>
    <td>fee</td>
    <td>Offer </td>
    <td>An offer to provide this item—for example, an offer to sell a product, rent the DVD of a movie, or give away tickets to an event.</td>
    <td>Many</td>
    <td>O</td>
    <td></td>
  </tr>
  <tr>
    <td>accreditation</td>
    <td>Organization  or Text </td>
    <td>Type of accreditation or organisation that accredits the event.</td>
    <td>One</td>
    <td>R</td>
    <td></td>
  </tr>
  <tr>
    <td>eligibility</td>
    <td>Text </td>
    <td>Defines the type of eligibility to attend this event e.g first come first served.</td>
    <td>Many</td>
    <td>R</td>
    <td>x</td>
  </tr>
  <tr>
    <td>capacity</td>
    <td>Integer</td>
    <td>Available number of spaces</td>
    <td>One</td>
    <td>R</td>
    <td></td>
  </tr>
  <tr>
    <td>contact</td>
    <td>Organization  or Person</td>
    <td>Main point of contact that can be contacted for general queries. This would be an event organiser or an administrator.</td>
    <td>Many</td>
    <td>M</td>
    <td></td>
  </tr>
  <tr>
    <td>attachment</td>
    <td>URL </td>
    <td>Any files or related websites which give more information about this event. e.g. flyers, third party sites handling tickets. </td>
    <td>Many</td>
    <td>O</td>
    <td></td>
  </tr>
  <tr>
    <td>socialMedia</td>
    <td>URL </td>
    <td>Link to social media websites like twitter or facebook.</td>
    <td>Many</td>
    <td>O</td>
    <td></td>
  </tr>
  <tr>
    <td>lastUpdate</td>
    <td>Date </td>
    <td>Date when the event was last modified.</td>
    <td>?</td>
    <td>O</td>
    <td></td>
  </tr>
  <tr>
    <td>deadline</td>
    <td>Text</td>
    <td>Deadlines dates for this event e.g. application deadline, poster submission, paper submission, early registration. </td>
    <td>Many</td>
    <td>R</td>
    <td></td>
  </tr>
  <tr>
    <td>acceptanceNotificationDate</td>
    <td>Date </td>
    <td>Date for the host to confirm acceptance to applicants.</td>
    <td>Many</td>
    <td>R</td>
    <td></td>
  </tr>
  <tr>
    <td>eventType</td>
    <td>Text</td>
    <td>Enumeration value for a type of event following one of the categories defined by SASI.</td>
    <td>Many</td>
    <td>M</td>
    <td>x</td>
  </tr>
  <tr>
    <td>topic</td>
    <td>Text</td>
    <td>In the context of Life Science, the scientific topics that describe the content of the event (e.g. statistics). Please use one of the scientific ontology terms for class 'Topic' from EDAM ontology. </td>
    <td>Many</td>
    <td>M</td>
    <td>x</td>
  </tr>
  <tr>
    <td>keywords</td>
    <td>CV and/or Text </td>
    <td>Keywords to describe the event. In Life Science, use terms that are not available in "topic" or “targetAudience”. Use text keywords or ontology terms from other ontologies that could complement EDAM topics.</td>
    <td>Many</td>
    <td>R</td>
    <td></td>
  </tr>
  <tr>
    <td>targetAudience</td>
    <td>Audience</td>
    <td>In Life Science, use Scientific topics that describe the research field of audience members (e.g. computer scientists). Please use one of the scientific ontology terms for class ‘Topic’ from EDAM ontology.</td>
    <td>Many</td>
    <td>R</td>
    <td>x</td>
  </tr>
  <tr>
    <td>spotlight</td>
    <td>boolean</td>
    <td>Event highlighted by the event provider.

Whether or not the event provider wishes to highlight this event as very important/significant.</td>
    <td>One</td>
    <td>R</td>
    <td></td>
  </tr>
  <tr>
    <td>programme</td>
    <td>Text or URL</td>
    <td>A plan or schedule of activities or procedures to be followed.</td>
    <td>One</td>
    <td>R</td>
    <td></td>
  </tr>
  <tr>
    <td>submitter</td>
    <td>Organization  or Person</td>
    <td>The person or organization who submits an event to a repository or registry of events (such as iAnn, ISCB ). </td>
    <td>Many</td>
    <td>O</td>
    <td></td>
  </tr>
  <tr>
    <td>hostInstitution</td>
    <td>Organization</td>
    <td>The organization or institution responsible for hosting the event (not necessarily responsible for organizing). </td>
    <td>Many</td>
    <td>M</td>
    <td></td>
  </tr>
  <tr>
    <td>sponsor</td>
    <td>Organization</td>
    <td>The organization or institutions providing sponsorship for the event. </td>
    <td>Many</td>
    <td>O</td>
    <td></td>
  </tr>
  <tr>
    <td>registrationStatus</td>
    <td>Registration Status</td>
    <td>Enumerative type displaying the status of registration for an event. See the notes below.</td>
    <td>One</td>
    <td>O</td>
    <td>x</td>
  </tr>
</table>


<table>
  <tr>
    <td>Properties inherited from schema.org/Thing</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>additionalType</td>
    <td>URL </td>
    <td>An additional type for the item, typically used for adding more specific types from external vocabularies in microdata syntax. This is a relationship between something and a class that the thing is in. In RDFa syntax, it is better to use the native RDFa syntax - the 'typeof' attribute - for multiple types. Schema.org tools may have only weaker understanding of extra types, in particular those defined externally.</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>alternateName</td>
    <td>Text </td>
    <td>An alias for the item. Can be used for the subtitle of the event.</td>
    <td>One</td>
    <td>R</td>
    <td></td>
  </tr>
  <tr>
    <td>description</td>
    <td>Text </td>
    <td>A short description of the item.</td>
    <td>One</td>
    <td>M</td>
    <td></td>
  </tr>
  <tr>
    <td>image</td>
    <td>ImageObject  or URL</td>
    <td>An image of the item. This can be a URL or a fully described ImageObject.Inverse property: mainEntity.</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>mainEntityOfPage</td>
    <td>CreativeWork  or URL</td>
    <td>Indicates a page (or other CreativeWork) for which this thing is the main entity being described. See background notes for details. Inverse property: mainEntity.</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>name</td>
    <td>Text </td>
    <td>The name of the item.</td>
    <td>One</td>
    <td>M</td>
    <td></td>
  </tr>
  <tr>
    <td>potentialAction</td>
    <td>Action </td>
    <td>Indicates a potential Action, which describes an idealized action in which this thing would play an 'object' role.</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>sameAs</td>
    <td>URL </td>
    <td>URL of a reference Web page that unambiguously indicates the item's identity. E.g. the URL of the item's Wikipedia page, Freebase page, or official website.</td>
    <td>One</td>
    <td>O</td>
    <td></td>
  </tr>
  <tr>
    <td>url</td>
    <td>URL </td>
    <td>URL of the item.This property can be used on a page listing many events, to indicate each individual event's page.</td>
    <td>Many</td>
    <td>R</td>
    <td></td>
  </tr>
</table>


Here is an example snippet showing the attributes you can use on an Event. For complete examples see the "Further examples" section at the end of this document.

<table>
  <tr>
    <td>Example 1. Attributes/properties of an Event</td>
  </tr>
  <tr>
    <td><div itemscope itemtype="http://schema.org/Event">
	<div itemprop="name">Epigenomics of Common Diseases</div>
	<div itemprop="description">This conference will bring together leading scientists from the fields of epigenomics, genetics and bioinformatics. </div>
	<div><meta itemprop="startDate" content="2015-04-15T">Wednesday 14 April 2015</div>
...
</div></td>
  </tr>
</table>


### Controlled Vocabularies (CV)

Some data fields suggest the use of controlled vocabularies or enumerations. We will rely on existing vocabularies and ontologies wherever possible but define new collections of terms for very specific purposes as required.

This section contains a list of fields that require a controlled vocabulary, enumeration or an ontology term, and specifies what is acceptable for each. The fields involved are:

* **event****Type**

*Must be* one of:

<table>
  <tr>
    <td>Value</td>
    <td>Description</td>
  </tr>
  <tr>
    <td>Workshops and courses</td>
    <td>A workshop or a course event</td>
  </tr>
  <tr>
    <td>Meetings and conferences</td>
    <td>A meeting or a conference event</td>
  </tr>
  <tr>
    <td>Receptions and networking</td>
    <td>A reception or a networking event</td>
  </tr>
  <tr>
    <td>Awards and prizegivings</td>
    <td>An award or a prize giving event</td>
  </tr>
</table>


		

* **topic**

*Must be* one of the [EDAM Topic](http://edamontology.org/topic_0003) class values.

* **targetAudience**

*Should be* blank or one of the [EDAM Topic](http://edamontology.org/topic_0003) class values.

* **e****ligibility**

*Should be* blank or one (possibly two) of:

<table>
  <tr>
    <td>Value</td>
    <td>Description</td>
  </tr>
  <tr>
    <td>First come first served </td>
    <td>Registrations will be accepted in the order received</td>
  </tr>
  <tr>
    <td>Registration of interest</td>
    <td>The organisers will select successful registrants from a list of interested parties</td>
  </tr>
  <tr>
    <td>By invitation</td>
    <td>Only invited parties may register (this option may be used on its own or in conjunction with either of the others by specifying both values, e.g. for an event where people are individually invited but only the first X will be able to register)</td>
  </tr>
</table>


* **registrationStatus**

*Should be* blank or one of:

<table>
  <tr>
    <td>Value</td>
    <td>Description</td>
  </tr>
  <tr>
    <td>Proposed</td>
    <td>Currently being planned, not yet confirmed</td>
  </tr>
  <tr>
    <td>Pre-open</td>
    <td>Confirmed but not yet open for registration</td>
  </tr>
  <tr>
    <td>Open</td>
    <td>Open for registration</td>
  </tr>
  <tr>
    <td>Cancelled</td>
    <td>Cancelled</td>
  </tr>
  <tr>
    <td>Full</td>
    <td>Fully booked</td>
  </tr>
</table>


* **eventS****tatus**

*Should be* blank or one of:

<table>
  <tr>
    <td>Value</td>
    <td>Description</td>
  </tr>
  <tr>
    <td>EventCancelled</td>
    <td>Event cancelled</td>
  </tr>
  <tr>
    <td>EventPostponed</td>
    <td>Event postponed</td>
  </tr>
  <tr>
    <td>EventRescheduled</td>
    <td>Event rescheduled</td>
  </tr>
  <tr>
    <td>EventScheduled</td>
    <td>Event happening</td>
  </tr>
</table>


Topic and targetAudience work together to specify what the event is about and who should attend. For example if the event is a statistics training session for biologists, then topic would be statistics and targetAudience would be biology. If it is an event for geneticists about genetics then both topic and targetAudience would be genetics.

### Content Guidelines (CG)

To make it as easy as possible to implement a basic Event model, we suggest a very small set of minimum (M) fields to include. For optimal discovery and integration we suggest some additional recommended (R) fields. All other fields are optional (O), but if included will enhance the user experience.

Fields that *must be* present (M) in order to comply with the specification are:

* name

* description

* eventType

* topic

* hostInstitution

* [startDate](https://schema.org/startDate)

* [endDate](https://schema.org/endDate)

* location

* fee

* contact

### Cardinality

The Schema.org specification permits any field to be included any number of times. Whether this is desirable depends on the context and intended use of the data. This specification includes suggestions as to the cardinality of selected fields, as indicated in the data model table above.

The table notates cardinalities in the following way:

<table>
  <tr>
    <td>Notation</td>
    <td>Definition</td>
  </tr>
  <tr>
    <td>One</td>
    <td>There may only be a maximum of one instance of this property type. For example, an event may only have a maximum of one start date. </td>
  </tr>
  <tr>
    <td>Many</td>
    <td>There can be multiple instances of this property type. For example, there may be more than one sponsor of an event.</td>
  </tr>
</table>


<table>
  <tr>
    <td>Example 2. Cardinality in Event properties as microdata within HTML</td>
  </tr>
  <tr>
    <td><div itemscope itemtype="http://schema.org/Event">
...
<div>Type: 
    <span itemprop="eventType">Workshop</span>, 
    <span itemprop="eventType">Meeting</span>
</div>
<div>Start: <meta itemprop="startDate" content="2015-04-15T">Wednesday 14 April 2015</div>
...
</div></td>
  </tr>
</table>


*An example of a property type with multiple cardinality (eventType) and single cardinality (startDate).*

### Identifiers

TBD

## Implementation Guidelines

Schema.org [suggests](http://schema.org/docs/gs.html) implementing metadata, including the Event specification, using Microdata, RDFa, or JSON-LD. Depending on the context, any of these can be used for embedding compliant event data in an event provider's web pages or other online resources and services.

### Microdata

Microdata can be used for embedding properties from the specification directly into existing web pages and HTML tags to enrich event descriptions. This microdata can be extracted and further processed by search engines and other applications, but does not affect the 'look and feel' of the web page it is embedded in. Using microdata is the easiest method of implementing the specification, as it requires minimal intervention on event providers’ part. Example below depicts the use of microdata within HTML tags. 

<table>
  <tr>
    <td>Example 3. Embedding Event properties as microdata within HTML</td>
  </tr>
  <tr>
    <td><div itemscope itemtype="http://schema.org/Event">
<div itemprop="name">Epigenomics of Common Diseases</div>
<div itemprop="description">This conference will bring together leading scientists from the  fields of epigenomics, genetics and bioinformatics. </div>
<div>Event type: <span itemprop="eventType">Workshops and courses</span></div>
<div>Date: <meta itemprop="startDate" content="2015-04-15T">Wednesday 14 April 2015</div>
   ...
</div></td>
  </tr>
</table>


For more information, please refer to the [Microdata Guide on Schema.org](https://schema.org/docs/gs.html).

### RDFa

[RDFa](https://en.wikipedia.org/wiki/RDFa) (or[ Resource Description Framework](https://en.wikipedia.org/wiki/Resource_Description_Framework) in Attributes[[1]](https://en.wikipedia.org/wiki/RDFa#cite_note-n-1)) is a[ W3C](https://en.wikipedia.org/wiki/W3C) Recommendation that adds a set of attribute-level extensions to[ HTML](https://en.wikipedia.org/wiki/HTML),[ XHTML](https://en.wikipedia.org/wiki/XHTML) and various XML-based document types for embedding rich[ metadata](https://en.wikipedia.org/wiki/Metadata) within web documents. Example below explains the use of RDFa within HTML tags. 

<table>
  <tr>
    <td>Example 4. Embedding Event properties as RDFa within HTML</td>
  </tr>
  <tr>
    <td><div vocab="http://schema.org/" typeof="Event">
<div property="name">Epigenomics of Common Diseases</div>
<div property="description">This conference will bring together leading scientists from the fields of epigenomics, genetics and bioinformatics. </div>
<div>Event type: <span property="eventType">Workshops and courses</span></div>
<div>Date: <meta property="startDate" content="2015-04-15T">Wednesday 14 April 2015</div>
   ...
</div> </td>
  </tr>
</table>


 

For more information, please refer to the [RDFa wiki](http://rdfa.info/).

### JSON-LD

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD) (JavaScript Object Notation for Linked Data), is a method of transporting[ Linked Data](https://en.wikipedia.org/wiki/Linked_Data) using[ JSON](https://en.wikipedia.org/wiki/JSON). Example below represents an Event described in JSON-LD format. 

<table>
  <tr>
    <td>Example 5. Representing an Event in JSON-LD format</td>
  </tr>
  <tr>
    <td><script type="application/ld+json">
{
"@context": "http://schema.org/",
"@type": "Event",
"name": "Epigenomics of Common Diseases",
"description": "This conference will bring together leading scientists from the fields of epigenomics, genetics and bioinformatics.",
"eventType": "Workshops and courses",
"startDate": "2015-04-15T",
  ...
}
</script></td>
  </tr>
</table>


For more information, please refer to the [JSON-LD specification](http://www.w3.org/TR/json-ld/).

# Glossary

<table>
  <tr>
    <td>Term</td>
    <td>Definition</td>
  </tr>
  <tr>
    <td>Ontology/Controlled vocabulary</td>
    <td>For the purposes of this document the terms ontology and controlled vocabulary are interchangeable. Wikipedia defines ontologies as: 
"In computer science and information science, an ontology is a formal naming and definition of the types, properties, and interrelationships of the entities that really or fundamentally exist for a particular domain of discourse. It is thus a practical application of philosophical ontology, with a taxonomy."</td>
  </tr>
  <tr>
    <td>EDAM ontology</td>
    <td>EDAM ontology is one of the ontologies available in the life sciences domain, for classifying and describing bioinformatics operations, types of data, formats, and scientific topics.</td>
  </tr>
  <tr>
    <td>EDAM ontology topic</td>
    <td>EDAM ontology topics describe general bioinformatics subjects or categories, such as a field of study, data, processing, analysis or technology - starting from very general terms such as “biology” and “bioinformatics” to more specific ones such as "sequence analysis", "alignment", "sequencing", "microarrays", etc.</td>
  </tr>
</table>


# Further examples

<table>
  <tr>
    <td>Example 6. Event containing all the minimum (M) fields</td>
  </tr>
  <tr>
    <td>Microdata:
<div itemscope itemtype="http://schema.org/Event">
<meta itemprop="eventId" content="id6593990">
<div itemprop="name">Epigenomics of Common Diseases</div>
<div itemprop="description">This conference will bring together leading scientists from the fields of epigenomics, genetics and bioinformatics. </div>
<div>Event type: <span itemprop="eventType">Workshops and courses</span></div>
<div>Date: <meta itemprop="startDate" content="2015-04-15T">Wednesday 14 April 2015</div>
<div itemprop="location" itemscope itemtype="http://schema.org/Place">
Location:
<span itemprop="name">Greensands Conference Centre</span>
<div itemprop="address" itemscope itemtype="http://schema.org/PostalAddress">
<span itemprop="streetAddress">6 Burridge Road</span><br>
<span itemprop="addressLocality">Manchester</span><br>
<span itemprop="postalCode">M15 3RT</span><br>
<span itemprop="addressCountry">UK</span>
</div> 
</div>
<div itemprop="offers" itemscope itemtype="http://schema.org/Offer">
Price:
<span itemprop="priceCurrency" content="GBP">£</span><span
itemprop="price" content="100.00">100.00</span>
</div>
<div itemprop="contact">
<div itemscope itemtype="http://schema.org/Person">
Contact:
<span itemprop="name">Jane Doe</span> 
(<a href="mailto:jane-doe@nwu.ac.uk" itemprop="email">
    jane-doe@nwu.ac.uk</a>)
</div>
</div>
<div itemprop="hostInstitution">
Host institution: 
<div itemscope itemtype="http://schema.org/Organization">
<span itemprop="name">North West University</span>
</div> 
</div>
<div>Link: <a itemprop="url" href="http://www.nwu.ac.uk/event-url">North West University website</a></div>
<div>Topics:<span itemprop="topic">Biomedical science</span>, <span itemprop="topic">Human disease</span>
</div>
</div>

RDFa:
<div vocab="http://schema.org/" typeof="Event">
<meta property="eventId" content="id6593990">
<div property="name">Epigenomics of Common Diseases</div>
<div property="description">This conference will bring together leading scientists from the fields of epigenomics, genetics and bioinformatics. </div>
<div>Event type: <span property="eventType">Workshops and courses</span></div>
<div><meta property="startDate" content="2015-04-15T">Wednesday 14 April 2015</div>
<div property="location" typeof="Place">
Location:
<span property="name">Greensands Conference Centre</span>
<div property="address" typeof="postalAddress">
<span property="streetAddress">6 Burridge Road</span><br>
<span property="addressLocality">Manchester</span><br>
<span property="postalCode">M15 3RT</span><br>
<span property="addressCountry">UK</span>
</div> 
</div>
<div property="offers" typeof="Offer">
Price:
<span property="priceCurrency" content="GBP">£</span><span
property="price" content="100.00">100.00</span>
</div>
<div property="contact">
<div typeof="Person">
Contact:
<span property="name">Jane Doe</span> 
(<a href="mailto:jane-doe@nwu.ac.uk" property="email">
    jane-doe@nwu.ac.uk</a>)
</div>
</div>
<div property="hostInstitution">
Host institution: 
<div typeof="Organization">
<span property="name">North West University</span>
</div> 
</div>
<div>Link: <a property="url" href="http://www.nwu.ac.uk/event-url">North West University website</a></div>
<div>Topics:<span property="topic">Biomedical science</span>, <span property="topic">Human disease</span>
</div>
</div> 

JSON-LD:
<script type="application/ld+json">
{
"@context": "http://schema.org",
"@type": "Event",
"eventId": "id6593990",
"name": "Epigenomics of Common Diseases",
"description": "This conference will bring together leading scientists from the fields of epigenomics, genetics and bioinformatics.",
"type": "Workshops and courses",
"startDate": "2015-04-15T",
"location": {
"name": "Greensands Conference Centre",
"@type": "Place",
"address": {
			"@type": "PostalAddress",
			"streetAddress": "6 Burridge Road",
			"addressLocality": "Manchester",
			"postalCode": "M15 3RT",
			"addressCountry": "UK"
}
},
"contact": {
"@type": "Person",
"name": "Jane Doe",
"email": "jane.doe@nwu.ac.uk"
},
"offers": {
"@type": "Offer",
"price": "100.00",
"priceCurrency": "GBP"
},
"hostInstitution": {
"@type": "Organization",
"name": "North West University"
},
"url": "http://www.nwu.ac.uk/event-url",
"topic": "Biomedical science",
"topic": "Human disease"
}
</script></td>
  </tr>
</table>


<table>
  <tr>
    <td>Example 7. Using the url property as the event organiser and as a third party event advertiser</td>
  </tr>
  <tr>
    <td>As the event organiser
You can include a hidden link to an external event advertiser on your site by using the "same as" property:

<div itemscope itemtype="http://schema.org/Event">
...
<div>Link: 
<a itemprop="url" href="http://www.nwu.ac.uk/event-url">Epigenomics of Common Diseases</a>
<link itemprop="sameAs" href="http://externaladvertiser.com/nwu-event"/>
</div>
   ...
</div>

As an external event advertiser
It is recommended that you add a link on your site to the source of the information about the event:

<div itemscope itemtype="http://schema.org/Event">
...
<div>Link: 
<a itemprop="url" href="http://www.externaladvertiser.com/nwu-event">Epigenomics of Common Diseases</a>
<link itemprop="sameAs" href="http://www.nwu.ac.uk/event-url"/>
</div>
   ...
</div>
</td>
  </tr>
</table>


<table>
  <tr>
    <td>Example 8. Using the proposed new ontologyTerm type</td>
  </tr>
  <tr>
    <td>Example of a keyword field using terms from different ontologies. In this case a term from EDAM, a term from MeSH and a custom term.

<div itemscope itemtype="http://schema.org/Event">
…
Keywords:
<div itemscope itemtype="http://schema.org/ontologyTerm">
<link itemprop="ontologyName" href="http://purl.bioontology.org/ontology/EDAM">
<meta itemprop="termId" content="data_0006">
<span itemprop="termName">Metagenomics</span>
<div>,
<div itemscope itemtype="http://schema.org/ontologyTerm">
<link itemprop="ontologyName" href="https://www.nlm.nih.gov/mesh/">
<meta itemprop="termId" content="D056186">
<span itemprop="termName">Metagenomics</span>
<div>
<div itemscope itemtype="https://schema.org/CreativeWork">
<meta itemprop="keywords" content="disease, bioinformatics">
<span>Disease, Bioinformatics</span>
<div>
   ...
</div>

</td>
  </tr>
</table>


