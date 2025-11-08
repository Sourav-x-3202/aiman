import pyttsx3
import os

def text_to_speech(text, output_file="outputs/aiman_voice.mp3"):
    os.makedirs("outputs", exist_ok=True)
    engine = pyttsx3.init()
    
    # Set voice to male if available
    voices = engine.getProperty('voices')
    for voice in voices:
        if "David" in voice.name or "Male" in voice.name or "Guy" in voice.name:
            engine.setProperty('voice', voice.id)
            break

    # Deep and calm tone
    engine.setProperty('rate', 145)   # slower, calm
    engine.setProperty('volume', 1.0) # full volume
    engine.save_to_file(text, output_file)
    engine.runAndWait()
    
    return output_file
