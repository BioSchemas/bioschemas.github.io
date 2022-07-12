<details>
  <summary>Update your changes to the DDE schema registry</summary>

  <details>
    <summary>Fork the Bioschemas_DDE repo</summary>
    <ul>
      <li>The repository that hosts the actual JSONLD files that are updated into the DDE is: <a
          href="https://github.com/BioSchemas/bioschemas-dde">https://github.com/BioSchemas/bioschemas-dde</a></li>
      <li>The repository also includes a GitHub actions script to automatically merge JSONLD files from the
        specifications repo as long as they’re included in the table of classes for import</li>
    </ul>
  </details>

  <details>
    <summary>Update the appropriate file in <strong>your fork of Bioschemas_DDE repository</strong></summary>
    <ul>
      <li>In YOUR fork of the Bioschemas_DDE repository, edit the appropriate list file:<ul>
          <li>If this new specification is a draft type, add a record of it to the <code>draft_type_list.txt</code> (ie.
            the file equivalent to this in YOUR repo)</li>
          <li>If this new specification is a draft profile, add a record of it to the
            <code>draft_profile_list.txt</code>
          </li>
          <li>If you are updating an existing draft specification to a new version, find the record in the appropriate
            file and update it</li>
          <li>Note, these files are all tab-delimited text files</li>
        </ul>
      </li>
    </ul>
    <details>
      <summary>About released specifications</summary>

      <ul>
        <li>You should NOT be unilaterally updating any of the release files (as there is an additional approval
          process);
          however, if the approval process has been completed, the appropriate files are:</li>
        <li><code>type_list.txt</code> for <strong>released</strong> type specifications</li>
        <li><code>profile_list.txt</code> for <strong>released</strong> profile specifications</li>
      </ul>
    </details>
  </details>

  <details>
    <summary>Test your fork of the Bioschemas_DDE repository</summary>

    <ul>
      <li>Save/push your changes to your fork of the Bioschemas_DDE repo this will trigger a GitHub action script to
        update
        the appropriate merged JSONLD file (which gets ingested into the DDE)<ul>
          <li>Once the GitHub actions completes, wait 2-3 minutes for GitHub’s internal cache to update</li>
          <li>Test the GitHub actions generated json in DDE</li>
          <li>Using the url for the corresponding JSONLD file in YOUR fork of the repo, load your JSONLD into the DDE
            Schema
            playground viewer</li>
        </ul>
      </li>
    </ul>

  </details>

  <details>
    <summary>Push your changes from your fork to the Bioschemas_DDE repository</summary>

    <ul>
      <li>If it works well, push your changes from your fork to the Bioschemas_DDE repo<ul>
          <li>Note that you may need to force the push, or to re-follow the previous steps in the main repo in order to
            make the
            changes</li>
          <li>This will trigger the GitHub actions in the Bioschemas_DDE repo causing an update</li>
          <li>The changes in the JSONLD files in the Bioschemas_DDE repo are automatically updated to the DDE on a
            <strong>scheduled
              basis</strong>, so you might not see the change in the DDE immediately. However, you can (and should have
            already)
            previewed how it is expected to look in the DDE.</li>
        </ul>
      </li>
    </ul>

  </details>

</details>