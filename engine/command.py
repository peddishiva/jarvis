import pyttsx3

def speak(text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) 
    engine.setProperty('rate', 174) 
    print(voices)
    engine.say(text)
    engine.runAndWait()

speak("Hello, I am jarvis and I am your personal assistant. How can I help you?")