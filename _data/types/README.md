# Process for Getting JSON representaiton from Schema.org

1. In your browser, go to the page where you have been developing the type and its properties, i.e. the test site that comes with the schemaorg development environment.
1. View the page source
1. Find the json-ld embedded within the source
1. Copy the json-ld into a file
1. Remove all `@` signs from keys, i.e.
  `@id` --> `id`
  `@value` --> `value`
1. Remove all namespaces from keys, e.g. `http://www.w3.org/2002/07/owl#equivalentProperty` --> `equivalentProperty`

# Dealing with Type Versions

Versioning of types is not straightforward since a change can happen on the parent type which is a consequence of wanting a change in the child, e.g. when adding `hasSequenceAnnotation` to `Protein` this was actually a change to the `BioChemEntity` type since this property also applies to Genes.

First idea was to have typed files for each part of the type hierarchy, but perhaps we need to first simplify what we have captured about each type.

There is redundancy in the type definitions that are grabbable from Schema.org and this is likely to lead to inconsistencies in the future.
