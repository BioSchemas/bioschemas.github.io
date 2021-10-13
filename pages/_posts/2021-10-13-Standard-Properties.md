---
layout: post
title: "Standard Properties"
tags:
- Community
- Profile
---
A standard set of properties have been added to all Bioschemas [profiles](/profiles/). These properties allow consumers of markup to more easily understand the markup, and to validate it against the relevant profile. Essentially the properties form a boilerplate for any markup, see following code snippet for an example protein taken from [DisProt](https://disprot.org/).

```JSON
{
  "@context": "https://schema.org/",
  "@type": "Protein",
  "@id": "https://disprot.org/DP00003",
  "http://purl.org/dc/terms/conformsTo": {
    "@id": "https://bioschemas.org/profiles/Protein/0.11-RELEASE",
    "@type": "CreativeWork"
  },
  ...
}
```

Note that while the properties are stated in the JSON-LD form, there are equivalents for RDFa.
