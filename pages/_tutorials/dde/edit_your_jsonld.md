<details>
  <summary> How to edit your JSON LD</summary>

  <details>
    <summary> If your JSONLD has been saved locally</summary>
    <ul>
      <li>If you downloaded your json, open it in a simple text editor like notepad<ul>
          <li>text editors like Sublime, Brackets, will also work and provide a nicer editing experience</li>
        </ul>
      </li>
    </ul>

  </details>

  <details>
    <summary> If your JSONLD has been saved to GitHub</summary>

    <ul>
      <li>Navigate to the file in your repo on github and click on it<ul>
          <li>Click on the <code>edit</code> icon in github </li>
        </ul>
      </li>
    </ul>

  </details>

</details>

<details>
  <summary> What to edit in your JSONLD</summary>

  <details>
    <summary> Edits needed when updating an existing type specification</summary>

    <ul>
      <li>Since this JSONLD schema is meant to REPLACE a previous version rather than be a child of the previous
        version, you&#39;ll need to update the parent class<ul>
          <li>{% include_relative change_parent_class.md %} </li>
        </ul>
      </li>
    </ul>

  </details>

  <details>
    <summary> Edits needed when updating an existing profile specification</summary>

    <ul>
      <li>Since this JSONLD schema is meant to REPLACE a previous version rather than be a child of the previous
        version, you&#39;ll need to update the parent class<ul>
          <li>{% include_relative change_parent_class.md %} </li>
        </ul>
      </li>
    </ul>

  </details>


  <details>
    <summary> Other common manual edits</summary>

    <ul>
      <li>Using external vocabularies as properties (not property values)<ul>
          <li>When using external vocabularies as properties, you will need to include the url for the vocabulary in the
            <code>@context</code>, and to fix the namespace in the property definition</li>
          <li>For example, I create a property (for a new class called <code>test</code>) in the DDE called
            <code>dateCopyrighted</code>, but I really want it to just use <code>dateCopyrighted</code> from an external
            vocabulary, the Dublin Core Initiative Term. The DDE-generated property definition would look like this:
            <pre><code class="lang-json">    {
            <span class="hljs-attr">"@id"</span>: <span class="hljs-string">"test:dct:dateCopyrighted"</span>,
            <span class="hljs-attr">"@type"</span>: <span class="hljs-string">"rdf:Property"</span>,
            <span class="hljs-attr">"rdfs:comment"</span>: <span class="hljs-string">"Date of copyright of the resource."</span>,
            <span class="hljs-attr">"rdfs:label"</span>: <span class="hljs-string">"dct:dateCopyrighted"</span>,
            <span class="hljs-attr">"schema:domainIncludes"</span>: {
              <span class="hljs-attr">"@id"</span>: <span class="hljs-string">"test:MyTest"</span>
            },
            <span class="hljs-attr">"schema:rangeIncludes"</span>: [
              {
                <span class="hljs-attr">"@id"</span>: <span class="hljs-string">"schema:Date"</span>
              }
            ]
          }
      </code></pre>
            and would need to be adjusted to:
            <pre><code class="lang-json">      {
              <span class="hljs-attr">"@id"</span>: <span class="hljs-string">"dct:dateCopyrighted"</span>,
              <span class="hljs-attr">"@type"</span>: <span class="hljs-string">"rdf:Property"</span>,
              <span class="hljs-attr">"rdfs:comment"</span>: <span class="hljs-string">"Date of copyright of the resource."</span>,
              <span class="hljs-attr">"rdfs:label"</span>: <span class="hljs-string">"dateCopyrighted"</span>,
              <span class="hljs-attr">"schema:domainIncludes"</span>: {
                <span class="hljs-attr">"@id"</span>: <span class="hljs-string">"test:MyTest"</span>
              },
              <span class="hljs-attr">"schema:rangeIncludes"</span>: [
                {
                  <span class="hljs-attr">"@id"</span>: <span class="hljs-string">"schema:Date"</span>
                }
              ]
            }
      </code></pre>
            and the DDE-generated <code>@context</code> content:
            <pre><code class="lang-json">     <span class="hljs-string">"@context"</span>: {
            <span class="hljs-string">"schema"</span>: <span class="hljs-string">"http://schema.org/"</span>,
            <span class="hljs-string">"rdf"</span>: <span class="hljs-string">"http://www.w3.org/1999/02/22-rdf-syntax-ns#"</span>,
            <span class="hljs-string">"rdfs"</span>: <span class="hljs-string">"http://www.w3.org/2000/01/rdf-schema#"</span>,
            <span class="hljs-string">"test"</span>: <span class="hljs-string">"https://discovery.biothings.io/view/test/"</span>,
            <span class="hljs-string">"bioschemas"</span>: <span class="hljs-string">"https://discovery.biothings.io/view/bioschemas/"</span>
          }
      </code></pre>
            would need to be adjusted to include dct:
            <pre><code class="lang-json">      <span class="hljs-string">"@context"</span>: {
            <span class="hljs-string">"schema"</span>: <span class="hljs-string">"http://schema.org/"</span>,
            <span class="hljs-string">"rdf"</span>: <span class="hljs-string">"http://www.w3.org/1999/02/22-rdf-syntax-ns#"</span>,
            <span class="hljs-string">"rdfs"</span>: <span class="hljs-string">"http://www.w3.org/2000/01/rdf-schema#"</span>,
            <span class="hljs-string">"test"</span>: <span class="hljs-string">"https://discovery.biothings.io/view/test/"</span>,
            <span class="hljs-string">"bioschemas"</span>: <span class="hljs-string">"https://discovery.biothings.io/view/bioschemas/"</span>,
            <span class="hljs-string">"dct"</span>: <span class="hljs-string">"http://purl.org/dc/terms/"</span>
          }
      </code></pre>
          </li>
        </ul>
      </li>
    </ul>

  </details>

</details>