import speech_recognition as sr
import pyttsx3

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language="en-US")  # choose language
        print("📝 You said:", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print("⚠️ API error:", e)
        return ""

def text_to_speech(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    # Pick male voice if available
    for v in voices:
        if "male" in v.name.lower():
            engine.setProperty('voice', v.id)
            break

    # Speak out loud
    engine.say(text)
    engine.runAndWait()
    print(f"✅ Voice output done, and saved as {filename}")


if __name__ == "__main__":
    while True:
        print(speech_to_text())
