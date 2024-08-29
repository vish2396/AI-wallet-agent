from gtts import gTTS
import os
import uuid

def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    filename = f"temp/{uuid.uuid4()}.mp3"
    tts.save(filename)

    return filename