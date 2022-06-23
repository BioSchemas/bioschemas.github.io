<details>
  <summary>How to change the parent class for your specification</summary>
  
The DDE treats every new specification as a child class of the class that it was extended from. 
- To change the parent class, search for the line containing `rdfs:subclassOf`
- Replace the content after the `"@id":` of the `rdfs:subclassOf` value. For example:
   ```
    "rdfs:subClassOf": {
        "@id": "bioschemasdrafts:CourseInstance"
      },
   ```
  can be changed to:
   ```
    "rdfs:subClassOf": {
        "@id": "schema:CourseInstance"
      },
   ```  
</details>
