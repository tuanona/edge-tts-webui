# Edge TTS Web UI

A simple, self-hosted web interface to generate speech using Microsoft's high-quality Edge Text-to-Speech (TTS) service. This tool allows you to generate audio files directly from your browser without needing to use the command line.

---

## Features

-   ✅ **Simple & Clean Interface:** An easy-to-use web form for generating audio.
-   🎤 **Customizable Output:** Control the text, voice, and output filename.
-   🎧 **No CLI Needed:** Generate and download audio without touching the terminal.
-   📥 **Direct Downloads:** Get a download link for your MP3 file right after generation.
-   🏠 **Runs Locally:** Everything runs on your own machine. No cloud deployment or external services required.

---

## Tech Stack

-   **Backend**: Python 3 with Flask
-   **TTS Engine**: The `edge-tts` Python library
-   **Frontend**: Plain HTML, CSS, and JavaScript (no frameworks)

---

## Installation

Follow these steps to get the project running on your local machine.

**1. Clone the Repository**
```bash
git clone [https://github.com/your-username/edge-tts-webui.git](https://github.com/your-username/edge-tts-webui.git)
cd edge-tts-webui
