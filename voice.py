import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:", query)
    except sr.UnknownValueError:
        print("Could not understand audio")
        speak("I didn't understand")
        return "None"
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        speak("Sorry, I couldn't access the internet to process your request")
        return "None"
    return query.lower()

if __name__ == '__main__':
    speak("Amigo assistance activated")
    speak("How can I help you")
    
    while True:
        query = take_command()
        
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", '').strip()
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("Multiple results found. Please specify.")
            except wikipedia.exceptions.PageError as e:
                speak("Sorry, I couldn't find any relevant information.")
        elif 'are you' in query:
            speak("I am Amigo developed Challa Pooja")
        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
        elif 'open github' in query:
            speak("Opening GitHub")
            webbrowser.open("https://www.github.com")
        elif 'open stackoverflow' in query:
            speak("Opening Stack Overflow")
            webbrowser.open("https://www.stackoverflow.com")
        elif 'open spotify' in query:
            speak("Opening Spotify")
            webbrowser.open("https://www.spotify.com")
        elif 'open whatsapp' in query:
            speak("Opening WhatsApp")
            loc = "C:\\Users\\jaspr\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(loc)
        elif 'play music' in query:
            speak("Opening music on Spotify")
            webbrowser.open("https://www.spotify.com")
        elif 'local disk d' in query:
            speak("Opening Local Disk D")
            webbrowser.open("file://D:/")
        elif 'local disk c' in query:
            speak("Opening Local Disk C")
            webbrowser.open("file://C:/")
        elif 'local disk e' in query:
            speak("Opening Local Disk E")
            webbrowser.open("file://E:/")
        elif 'sleep' in query:
            speak("Goodbye!")
            break
