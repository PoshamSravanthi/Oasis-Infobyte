import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture voice input from the user."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand that. Please repeat.")
        return ""
    except sr.RequestError:
        speak("There seems to be an issue with the speech recognition service.")
        return ""

def respond(command):
    """Respond to voice commands."""
    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "time" in command:
        time_now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time_now}")
    elif "date" in command:
        date_today = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today is {date_today}")
    elif "search" in command:
        query = command.replace("search", "").strip()
        if query:
            speak(f"Searching for {query}")
            pywhatkit.search(query)
        else:
            speak("Please tell me what you want to search for.")
    else:
        speak("I can only handle basic commands right now.")

# Main function to run the assistant
def run_voice_assistant():
    speak("Voice Assistant activated. Say something!")
    while True:
        command = listen()
        if "exit" in command or "quit" in command:
            speak("Goodbye!")
            break
        respond(command)

# Run the assistant
if __name__ == "__main__":
    run_voice_assistant()
