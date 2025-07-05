import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser
import pyjokes
import wikipedia

r = sr.Recognizer()
audio = None
engine = pyttsx3.init()
first_time = True

while True:
    with sr.Microphone() as source:
        if first_time:
            hello = "Please say something:"
            print(hello)
            engine.say(hello)
            engine.runAndWait()
            first_time = False
        r.adjust_for_ambient_noise(source, duration=1)

        audio = r.listen(source)
        print("Audio captured, processing...")

    try:
        #recognize the audio
        text = r.recognize_google(audio)
        print("You said:", text)

        command = text.lower()
        if "hello" in command:
            result = "hello, what can i help you with today?"
        elif "what is" in command or "calculate" in command or "how much is" in command:
            expression = command

            # Replace spoken words with math symbols
            expression = expression.replace("what is", "")
            expression = expression.replace("calculate", "")
            expression = expression.replace("how much is", "")
            expression = expression.replace("plus", "+")
            expression = expression.replace("minus", "-")
            expression = expression.replace("times", "*")
            expression = expression.replace("x", "*")
            expression = expression.replace("X", "*")
            expression = expression.replace("multiplied by", "*")
            expression = expression.replace("divided by", "/")

            try:
                result = eval(expression.strip())
                result = f"The answer is {result}"
            except:
                result = "Sorry, I couldn't calculate that."
        elif "time" in command:
            now = datetime.now()
            formatted_time = now.strftime("%H:%M")
            result = f"The time is {formatted_time}"
        elif "open" in command:
            newwords = command.split()

            try:
                index = newwords.index("open")
                next_word = newwords[index + 1]
                webbrowser.open(f"https://{next_word}.com")
                result = f"Opening {next_word}"
            except (ValueError, IndexError):
                print("No word found after 'open'")
        elif "joke" in command:
            result = pyjokes.get_joke()
        elif "wikipedia" in command:
            search_term = command.replace("wikipedia", "").strip()
            try:
                summary = wikipedia.summary(search_term, sentences=2)
                result = summary
            except Exception:
                result = "Sorry, I couldn't find anything on Wikipedia."
        elif "exit" in command or "stop" in command or "no" in command:
            result = "Goodbye!"
            exit()
        else:
            result = "Sorry, I don't understand that command."
        print(result)
        engine.say(result)
        engine.runAndWait()
        if "hello" not in command:
            engine.say("anything else?")
            print("Anything else?")
            engine.runAndWait()


    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
