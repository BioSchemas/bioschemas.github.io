<details>
  <summary>Click ‘extend’ (Icons on the right to ‘visualise’ (shows property details for that class) or ‘extend’)
  </summary>

  <p>(<a href="https://docs.google.com/presentation/d/1yl_aTm-od5U729-nVZWsGnl33oTDTS3NNlLzou60phI/edit#slide=id.p8">see
      &#39;extend&#39; screenshot</a>), (<a
      href="https://docs.google.com/presentation/d/1yl_aTm-od5U729-nVZWsGnl33oTDTS3NNlLzou60phI/edit#slide=id.g12bfbc3a89b_3_41">see
      &#39;visualize&#39; screenshot</a>), (see <a
      href="https://docs.google.com/presentation/d/1yl_aTm-od5U729-nVZWsGnl33oTDTS3NNlLzou60phI/edit#slide=id.g12bfbc3a89b_3_49">property
      details screenshot</a>)</p>


  <details>
    <summary>You will need to be logged in to continue</summary>
    <ul>
      <li>You can <a
          href="https://docs.google.com/presentation/d/1yl_aTm-od5U729-nVZWsGnl33oTDTS3NNlLzou60phI/edit#slide=id.p10">login
          via your GitHub account</a></li>
      <li>The DDE requires read access to find your repositories (so you can save to them) and write access in order for
        you to be able to export your work (specification in JSONLD format) to github</li>
    </ul>

  </details>

  <details>
    <summary>Follow the prompts to create your new specification</summary>
    <ul>
      <li>
        <p>Create a <a
            href="https://docs.google.com/presentation/d/1yl_aTm-od5U729-nVZWsGnl33oTDTS3NNlLzou60phI/edit#slide=id.p11">temporary
            namespace</a> (it will get replaced later on). Note, This step may be subject to a timeout. <strong>Please
            use PascalCase for your temporary namespace.</strong>
        <details>
          </p>
          <summary>Fill in the form to create the new specification including the name of your specification and a
            description.</summary>

          <p> (see <a
              href="https://docs.google.com/presentation/d/1yl_aTm-od5U729-nVZWsGnl33oTDTS3NNlLzou60phI/edit#slide=id.p12">screenshot
              of form</a>)
            The description should include:</p>
          <ul>
            <li>The description of the class as determined by the community</li>
            <li>The version of the class</li>
            <li>Any descriptions of changes between versions (this only applies to updating a class, not the creation of
              an entirely new class)</li>
          </ul>
      </li>
    </ul>

  </details>

</details>
<details>
  <summary>Select properties to inherit</summary>

  <ul>
    <li>The DDE will allow you to select properties from all parent classes to inherit.</li>
  </ul>

  <details>
    <summary> Select the checkbox on pre-existing properties for reuse.</summary>
    <p>(see <a
        href="https://docs.google.com/presentation/d/1yl_aTm-od5U729-nVZWsGnl33oTDTS3NNlLzou60phI/edit#slide=id.p40">screenshot
        of checkboxes for pre-existing properties</a>) </p>
    <ul>
      <li>The <a
          href="https://docs.google.com/presentation/d/1yl_aTm-od5U729-nVZWsGnl33oTDTS3NNlLzou60phI/edit#slide=id.p17">display
          shows</a> inheritable class properties (<a
          href="https://docs.google.com/presentation/d/1yl_aTm-od5U729-nVZWsGnl33oTDTS3NNlLzou60phI/edit#slide=id.g12bfbc3a89b_3_57">blue
          bar</a>) , and class-specific properties (<a
          href="https://docs.google.com/presentation/d/1yl_aTm-od5U729-nVZWsGnl33oTDTS3NNlLzou60phI/edit#slide=id.g12bfbc3a89b_3_65">yellow
          bar</a>).
        Also shown is the inheritance ‘path’ of the class and its properties. The ‘...’ icon on existing properties is
        an expandable view, listing existing properties from the class hierarchy.<ul>
          <li>Selecting a property will allow you to specify its marginality and to create constraints in the form of
            JSON Schema validation rules<ul>
              <li><a
                  href="https://docs.google.com/presentation/d/1yl_aTm-od5U729-nVZWsGnl33oTDTS3NNlLzou60phI/edit#slide=id.g12bfbc3a89b_3_105">Red
                  star</a> to mark it mandatory.</li>
              <li><a
                  href="https://docs.google.com/presentation/d/1yl_aTm-od5U729-nVZWsGnl33oTDTS3NNlLzou60phI/edit#slide=id.g12bfbc3a89b_3_112">Yellow
                  circle</a> to mark it recommended.</li>
              <li><a
                  href="https://docs.google.com/presentation/d/1yl_aTm-od5U729-nVZWsGnl33oTDTS3NNlLzou60phI/edit#slide=id.g12bfbc3a89b_3_119">Turquoise
                  square</a> to mark it optional. </li>
            </ul>
          </li>
        </ul>
      </li>
    </ul>
  </details>
  <ul>
    <li>If you are extending from a class with JSON schema validation rules (ie- a profile), the inheritable properties
      will be pre-loaded by default. <strong>You will need to un-select any that you do NOT wish to keep</strong></li>
    <li>Special exception: <code>conformsTo</code>
      <ul>
        <li>If you are extending from a bioschemas type specification, do NOT select <code>conformsTo</code> as that
          will be added via external script</li>
        <li>If you are extending from a bioschemas profile specification, you may need to &quot;uncheck&quot;
          <code>conformsTo</code>
        </li>
      </ul>
    </li>
  </ul>

</details>
<details>
  <summary> Special considerations for types</summary>

  <ul>
    <li>Since types are NOT subject to marginality and cardinality constraints, jsonschema validation rules do not
      apply, so
      you don’t need to select any properties as they will all be inherited by default</li>
  </ul>


</details>
<details>
  <summary> Saving and restoring your work</summary>
  <ul>
    <li>You can and should save your work locally.</li>
    <li>Click on &quot;save/load progress&quot;</li>
    <li>Use the &quot;Select Action&quot; drop down manu to:</li>
    <li>&#39;save&#39; your work</li>
    <li>&#39;load&#39; previous work</li>
    <li>&#39;delete&#39; save files that you no longer need</li>
  </ul>

</details>

</details>