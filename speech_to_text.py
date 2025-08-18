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
    async def say(text):
    communicate = edge_tts.Communicate(text, "en-IN-PrabhatNeural")
    await communicate.save("output.mp3")

 asyncio.run(say(text))
 playsound('output.mp3')



if __name__ == "__main__":
    while True:
        print(speech_to_text())
