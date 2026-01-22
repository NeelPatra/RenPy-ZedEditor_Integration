<h1 id="renpy-zed-editor-integration">Ren'Py Zed Editor Integration</h1>
<p>A lightweight Python script to enable <a href="https://zed.dev/">Zed Editor</a> support in the Ren'Py Visual Novel Engine.</p>
<h2 id="features">Features</h2>
<ul>
<li>Opens Ren'Py scripts directly in Zed.</li>
<li>Supports &quot;Jump to Line&quot; functionality for errors and script editing.</li>
<li>Groups multiple file requests into a single Zed transaction.</li>
</ul>
<h2 id="installation">Installation</h2>
<ol style="list-style-type: decimal">
<li>Download <code>Zed.edit.py</code> https://www.github.com/NeelPatra/RenPy-ZedEditor_Integration/releases/download/v1.0/Zed.edit.py</code> from this repository.</li>
<li>Locate your Ren'Py SDK folder (e.g., <code>renpy-8.5.2-sdk/</code>). https://www.renpy.org/dl/8.5.2/renpy-8.5.2-sdk.zip</li>
<li>Move <code>Zed.edit.py</code> into the <code>launcher/</code> directory: <code>renpy-8.5.2-sdk/launcher/Zed.edit.py</code></li>
<li>Restart the Ren'Py Launcher.</li>
<li>Go to <strong>Preferences &gt; Editor</strong> and select <strong>Zed</strong>.</li>
</ol>
<h2 id="requirements">Requirements</h2>
<ul>
<li><strong>Zed CLI</strong>: You must have the <code>zed</code> command in your system PATH.</li>
<li><em>macOS</em>: Open Zed and select <code>Zed &gt; Install CLI</code>.</li>
<li><em>Linux/Windows</em>: Ensure <code>zed</code> is accessible from your terminal.</li>
<li><strong>Ren'Py</strong>: Tested on version 8.5.2.</li>
</ul>
<h2 id="license">License</h2>
<p>This project is licensed under the MIT License - see the <a href="LICENSE" class="uri">LICENSE</a> file for details.</p>
