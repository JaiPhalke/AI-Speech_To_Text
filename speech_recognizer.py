import speech_recognition as sr

def recognize_from_mic():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("🎙️ Listening... Speak clearly!")
        audio = recognizer.listen(source, timeout=15)

    try:
        print("🧠 Transcribing...")
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "🤷 Sorry, I couldn't understand what you said."
    except sr.RequestError:
        return "🔌 API unavailable. Please check your internet connection."
