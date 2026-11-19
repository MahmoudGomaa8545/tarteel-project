import gradio as gr
from transformers import pipeline
import os

# قم بتعيين مسار ffmpeg هنا
os.environ["PATH"] += os.pathsep + r"C:\Users\user\AppData\Local\Programs\ffmpeg-8.0-full_build\bin"

# تحميل النموذج من Hugging Face
# هذا النموذج تم تدريبه خصيصاً على تلاوة القرآن
asr_model = pipeline(
    "automatic-speech-recognition", 
    "tarteel-ai/whisper-tiny-ar-quran",
    chunk_length_s=30,
    return_timestamps=False
)

def transcribe_quran(audio_file):
    """
    تقوم هذه الدالة بتحويل الصوت إلى نص باستخدام النموذج.
    """
    if audio_file is None:
        return "من فضلك قم بتسجيل أو رفع ملف صوتي."
        
    transcription = asr_model(audio_file)["text"]
    return transcription

# إنشاء واجهة المستخدم باستخدام Gradio
ui = gr.Interface(
    fn=transcribe_quran,
    inputs=gr.Audio(type="filepath"),
    outputs="text",
    title=" مرحب بقارئ القرآن   ",
    description="AI هذا تطبيق بسيط يستخدم نموذج ترتيل AI لتحويل تلاوتك من صوت إلى نص."
)

# تشغيل التطبيق
if __name__ == "__main__":
    ui.launch()