---
layout: use-case
name: DefinedTerm
group: data
active: true
redirect_from:
- "/useCases/DefinedTerm/"
- "/useCases/DefinedTerm"
---

The SchemaOrg type DefinedTerm is allowed in many places as property value.

In e.g. the life-sciences, there are a number of controlled vocabularies
and ontologies, which are often used as source of the `DefinedTerms`.
Many of them can be browsed and accessed through terminology and lookup services or portals.

For linked data applications it is sufficient for an entity
with `@type="DefinedTerm"` to link to an `@id` pointing to the IRI
of the referenced concept. In other cases, more information is needed to search and view defined term information
without having to lookup external resources. Those use cases are the target of this profile.
E.g., a domain-specific search engine
can create faceted search based on the `name` property, like e.g. done in TeSS.
Aforementioned terminology services also offer linking and query interfaces
beyond IRIs as parameters.

Another possible use of a conformant `DefinedTerm`
is to enable creating hyperlinks to other web ressources, e.g.
https://bio.tools/t?inputDataFormatID=%22format_3244%22
or provide tool-tips if the `description` is provided.

It is not intended to duplicate the content and expressivity
of powerful ontology representations and serialisations like OWL or RDF.
