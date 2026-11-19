from fastapi import FastAPI, File, UploadFile
from transformers import pipeline
import uvicorn
import shutil


asr_model = pipeline(
    "automatic-speech-recognition", 
    "tarteel-ai/whisper-tiny-ar-quran",
    chunk_length_s=30,
    return_timestamps=False
)

app = FastAPI()

@app.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    
    temp_file_path = f"temp_{file.filename}"
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    
    try:
        transcription = asr_model(temp_file_path)["text"]
    except Exception as e:
        
        os.remove(temp_file_path)
        return {"error": str(e)}

   
    os.remove(temp_file_path)

    return {"transcription": transcription}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)