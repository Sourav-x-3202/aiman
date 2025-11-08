<!-- 🔥 Project Banner -->
<p align="center">
  <img src="https://via.placeholder.com/1200x350.png?text=AIMAN+-+Cinematic+Motivational+AI" />
</p>

<h1 align="center">🧠 AIMAN — Cinematic Motivational AI</h1>
<h3 align="center">_"Type your pain, receive motivation."_</h3>

<p align="center">
  <a href="https://github.com/<your-username>/aiman/stargazers">
    <img src="https://img.shields.io/github/stars/<your-username>/aiman?style=flat-square&logo=github" />
  </a>
  <a href="https://github.com/<your-username>/aiman/issues">
    <img src="https://img.shields.io/github/issues/<your-username>/aiman?style=flat-square" />
  </a>
  <img src="https://img.shields.io/badge/Made%20with-Streamlit-FF4B4B?logo=streamlit&style=flat-square" />
  <img src="https://img.shields.io/badge/AI-Offline%20&%20Private-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" />
</p>

---

## 🎥 Demo

| AI Generated Image + Quote | AI Voice Output |
|----------------------------|----------------|
| <img src="outputs/sample.png" width="450"> | 🔊 `aiman_voice.wav` |

> Your message → AIMAN’s motivation → Cinematic image → Spoken in voice.

---

## ✨ What AIMAN Does

| Feature | Description |
|---------|-------------|
| 💬 Understands your emotions | Converts your message into motivational text using `phi3:mini` via **Ollama** |
| 🎨 Generates art | Creates cinematic portraits with **Stable Diffusion** |
| 🗣️ Speaks to you | Deep voice using `pyttsx3` (offline) |
| 🧠 100% Local | No internet. No API keys. Privacy-first. |
| 🌐 Beautiful UI | Built in **Streamlit**, just click and use. |

---

## 🧠 Tech Stack

| Area | Tech |
|------|------|
| Web UI | Streamlit |
| LLM Text Generation | Ollama (`phi3:mini`) |
| Image Generation | Hugging Face Diffusers + Stable Diffusion |
| Voice / Speech | pyttsx3 (Offline TTS) |
| Utility | Pillow, Requests, Accelerate |

---

## 🚀 Getting Started

### ✅ Clone Repo

```bash
git clone https://github.com/<your-username>/aiman.git
cd aiman


### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# or
source venv/bin/activate  # Mac/Linux
```

### 3. Install requirements

```bash
pip install -r requirements.txt
```

### 4. Start Ollama (Local LLM)

```bash
ollama serve
ollama pull phi3:mini
```

### 5. Run the app

```bash
streamlit run app.py
```


## Project Structure

```bash
aiman/
│
├── app.py                   # Streamlit UI
├── generate_text.py         # AI motivational message generation
├── motivational_image.py    # Stable Diffusion cinematic image generation
├── text_to_speech.py        # Voice synthesis
├── requirements.txt         
├── README.md
├── assets/
│   └── fonts/               # Dancing Script font for overlay text
└── outputs/                 # Generated images + voice (auto-created)

```

## Example Code (AI Motivation Generation)

```bash
from generate_text import generate_motivation

text = "I feel lost and tired of failing."
print(generate_motivation(text))

```


## Author

Developed by Sourav Sharma
If you like this project, please ⭐ star the repo — it motivates the developer 😉
👉 https://github.com/Sourav-x-3202/aiman



## License

MIT License — Free to use, modify, and distribute.


> "Pain is input. Growth is output. AIMAN is the bridge."







