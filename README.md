Edge TTS Web UI
===============

A simple, self-hosted web interface to generate speech using Microsoft's high-quality Edge Text-to-Speech (TTS) service. This tool allows you to generate audio files directly from your browser without needing to use the command line.

Features
--------

*   ✅ **Simple & Clean Interface:** An easy-to-use web form for generating audio.
    
*   🎤 **Customizable Output:** Control the text, voice, and output filename.
    
*   🎧 **No CLI Needed:** Generate and download audio without touching the terminal.
    
*   📥 **Direct Downloads:** Get a download link for your MP3 file right after generation.
    
*   🏠 **Runs Locally:** Everything runs on your own machine. No cloud deployment or external services required.
    

Tech Stack
----------

*   **Backend**: Python 3 with Flask
    
*   **TTS Engine**: The edge-tts Python library
    
*   **Frontend**: Plain HTML, CSS, and JavaScript (no frameworks)
    

Installation
------------

Follow these steps to get the project running on your local machine.

**1\. Clone the Repository**
```pyhton
git clone [https://github.com/your-username/edge-tts-webui.git](https://github.com/your-username/edge-tts-webui.git)  cd edge-tts-webui
```
Or simply download the ZIP file and extract it.

### 2\. Create the Output Directory

You need to create a folder where the generated MP3 files will be stored.

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   mkdir output   `

### 3\. Install Dependencies

This project requires a few Python libraries. Install them using pip:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pip install Flask Flask-Cors edge-tts   `

Usage
-----

Once everything is installed, you can start the application.

### 1\. Run the Python Server

Open your terminal, navigate to the project directory, and run:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python server.py   `

You should see a message indicating that the server is running on [http://localhost:5050](http://localhost:5050). Keep this terminal window open.

### 2\. Open the UI

Navigate to the project folder in your file explorer and double-click the index.html file to open it in your default web browser.

### 3\. Generate Audio

*   Fill in the text you want to convert.
    
*   Specify the voice model (e.g., id-ID-ArdiNeural).
    
*   Enter your desired output filename.
    
*   Click the **"Generate Audio"** button.
    

The generated MP3 file will be saved in the output directory, and a download link will appear on the page.

License
-------

This project is licensed under the MIT License.
