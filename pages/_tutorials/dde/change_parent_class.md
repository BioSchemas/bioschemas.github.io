<details>
  <summary>How to change the parent class for your specification</summary>

  <p>The DDE treats every new specification as a child class of the class that it was extended from. </p>
  <ul>
    <li>To change the parent class, search for the line containing <code>rdfs:subclassOf</code></li>
    <li>Replace the content after the <code>&quot;@id&quot;:</code> of the <code>rdfs:subclassOf</code> value. For
      example:
      <pre><code>  <span class="hljs-string">"rdfs:subClassOf"</span>: {
        <span class="hljs-string">"@id"</span>: <span class="hljs-string">"bioschemasdrafts:CourseInstance"</span>
      },
  </code></pre>can be changed to:
      <pre><code>  <span class="hljs-string">"rdfs:subClassOf"</span>: {
        <span class="hljs-string">"@id"</span>: <span class="hljs-string">"schema:CourseInstance"</span>
      },
  </code></pre>
    </li>
  </ul>

</details>