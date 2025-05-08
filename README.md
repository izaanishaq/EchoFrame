# 🎙️📸 *EchoFrame*: Conversational Insight from Images

## Introduction

What if your image could respond to your voice? **EchoFrame** turns that idea into an interactive experience. This experimental mini-application allows users to ask spoken questions about images and receive intelligent responses — both written and verbal.

Built on the convergence of voice recognition, visual understanding, and synthetic speech, EchoFrame demonstrates the capabilities of multimodal AI in a compact proof-of-concept.

In this guide, we unpack the **design blueprint**, **system components**, **technical considerations**, and **performance evaluation** that shaped the development of EchoFrame.

---

## 🧭 Concept Overview

**EchoFrame** offers a fluid interface for querying image content through speech. By leveraging tools such as **OpenAI Whisper**, **Salesforce BLIP-2**, and **Flan-T5-small**, the app orchestrates three core functionalities:

* Converts user voice input into text via automatic speech recognition (ASR).
* Analyzes images to extract contextual answers based on the transcribed question.
* Delivers responses through synthesized speech for a seamless conversational loop.

This interface is especially suited for assistive applications, educational tools, or any use case that benefits from auditory and visual interplay.

---

## 🗂️ Project Layout

```bash
EchoFrame/
│
├── main.py            # Central application controller
├── modules/
│   ├── voice_input.py     # ASR functionality via Whisper
│   ├── image_qa.py        # VQA engine using BLIP-2 + Flan-T5
│   └── voice_output.py    # Text-to-speech via pyttsx3
│
├── assets/            # Test images, audio clips, demonstration files
├── requirements.txt   # Python dependency list
└── README.md          # You're reading it now
```

---

## ✨ Key Capabilities

* 🔈 **Speech Input**: Supports voice recordings (≤ 10 seconds).
* 🖼️ **Image Support**: Compatible with `.jpg`, `.jpeg`, `.png`.
* 🧠 **Visual Understanding**: Contextual question answering using compact multimodal models.
* 🔊 **Audible Response**: Converts answers to natural speech output.
* 🧾 **Error Handling**: Handles rephrased or alternate question forms.

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/EchoFrame.git
cd EchoFrame
```

### 2. Prepare Your Python Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📋 Dependencies

```txt
torch
transformers
whisper
pyttsx3
streamlit
Pillow
sounddevice
soundfile
```

**Note**: `Whisper` depends on FFmpeg. Install it via:

```bash
sudo apt install ffmpeg
# or for macOS:
brew install ffmpeg
```

---

## ▶️ Running the Application

### Streamlit Interface (Recommended)

```bash
streamlit run main.py
```

Visit `http://localhost:8501` in your browser to interact with the app.

### Direct Module Testing

You may test individual modules independently:

#### ASR Test

```python
from modules.voice_input import transcribe
print(transcribe("assets/sample_question.wav"))
```

#### VQA Test

```python
from modules.image_qa import query_image
print(query_image("assets/sample_image.jpg", "What objects are visible?"))
```

#### TTS Test

```python
from modules.voice_output import speak
speak("Hello, this is a demonstration of text-to-speech output.")
```


## 🚧 Known Issues

* Speech-to-text quality degrades in noisy environments.
* Text-to-speech voice is synthetic and lacks expressiveness.
* The visual model may underperform on ambiguous or complex queries.

## 🙏 Acknowledgments

* [OpenAI Whisper](https://github.com/openai/whisper)
* [BLIP-2 via Hugging Face](https://huggingface.co/Salesforce/blip2-flan-t5-small)
* [Streamlit.io](https://streamlit.io/)
* [Pyttsx3 Documentation](https://pyttsx3.readthedocs.io/)
