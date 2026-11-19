# Tarteel - Quran Recitation Transcription

A Gradio web app that transcribes Quran recitation audio to text using the [tarteel-ai/whisper-tiny-ar-quran](https://huggingface.co/tarteel-ai/whisper-tiny-ar-quran) speech recognition model.

## Live Demo

https://huggingface.co/spaces/MahmoudGomaa8545/Tasmee3_Mutqin

## Tech Stack

- Python, Gradio
- Hugging Face Transformers (Whisper fine-tuned for Quranic Arabic)
- Docker

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Or with Docker:

```bash
docker build -t tarteel .
docker run -p 7860:7860 tarteel
```
