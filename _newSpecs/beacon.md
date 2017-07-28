---
layout: new_spec_detail
name: Beacon
description: In this document we propose a simple way for a beacons to self-describe their genetic variant cardinality service for better integration with other beacons within the beacon-network. It builds upon the Beacon service API and uses existing schema.org entities and properties.
bsc_desc:
mapping: link
version: 0.0.1
spec_doc: https://drive.google.com/open?id=1kQE3lixvBjBiZ8X3I1Mi44c3dcdgf4SshoGdNX5-_TE
spec_mapping: https://drive.google.com/open?id=1wLJa4LkCM8oIvBPTFS1IBcygRGBpSrAgNfRSEadVICo
new_bsc:
    - name: supportedReference
      expected_type: citation
      sdo_desc:  "A citation or reference to another creative work, such as another publication, web page, scholarly article, etc."
      bsc_dec:  supportedRefs
      marginality: Recommended 
      cardinality:  MANY 
      controlled_vocab:  YES 
      domain:  Beacon
      domain_case:  new_bsc
reu_sdo:
    - name:  dataset
      expected_type:  Dataset 
      sdo_desc:  "A dataset contained in this catalog. Inverse property: includedInDataCatalog."
      bsc_dec:  dataset 
      marginality:  Minimum 
      cardinality:  MANY 
      controlled_vocab:  NO 
      domain:  DataCatalog 
      domain_case:  reu_sdo 
    - name:  provider 
      expected_type:  Organization or  Person 
      sdo_desc:  "The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller. Supersedes carrier." 
      bsc_dec:  provider 
      marginality:  Minimum 
      cardinality:  MANY 
      controlled_vocab:  NO 
      domain:  CreativeWork 
      domain_case:  reu_sdo 
    - name:  version 
      expected_type:  Number or  Text 
      sdo_desc:  "The version of the CreativeWork embodied by a specified resource."
      bsc_dec:  version 
      marginality:  Minimum 
      cardinality:  ONE 
      controlled_vocab:  NO 
      domain:  CreativeWork 
      domain_case:  reu_sdo 
    - name:  identifier 
      expected_type:  PropertyValue or  Text or  URL 
      sdo_desc: "The identifier property represents any kind of identifier for any kind of Thing, such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See background notes for more details." 
      bsc_dec:  identifier 
      marginality:  Recommended 
      cardinality:  MANY 
      controlled_vocab:  NO 
      domain:  Thing 
      domain_case:  reu_sdo 
    - name:  name 
      expected_type:  Text 
      sdo_desc:  "The name of the item." 
      bsc_dec:  name 
      marginality:  Recommended 
      cardinality:  MANY 
      controlled_vocab:  NO 
      domain:  Thing 
      domain_case:  reu_sdo 
    - name:  sameAs 
      expected_type:  URL 
      sdo_desc:  "URL of a reference Web page that unambiguously indicates the item's identity. E.g. the URL of the item's Wikipedia page, Wikidata entry, or official website."
      bsc_dec:  sameAs 
      marginality:  Optional 
      cardinality:  ONE 
      controlled_vocab:  NO 
      domain:  Thing 
      domain_case:  reu_sdo 
    - name:  url 
      expected_type:  URL 
      sdo_desc:  "URL of the item."
      bsc_dec:  url 
      marginality:  Minimum 
      cardinality:  ONE 
      controlled_vocab:  NO 
      domain:  Thing 
      domain_case:  reu_sdo 
---







