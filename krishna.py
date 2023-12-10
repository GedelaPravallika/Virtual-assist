import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
listener = sr.Recognizer()
machine = pyttsx3.init()
def talk(text):
    machine.say(text)
    machine.runAndWait()
def input_instruction():
    global instruction
    try:
        with sr.Microphone() as origin:
            print("listening...")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "Krishna" in instruction:
                instruction = instruction.replace('Krishna', '')
                print(instruction)
    except sr.UnknownValueError:
        pass
    return instruction
def play_Krishna():
    instruction = input_instruction()
    print(instruction)
    if "play" in instruction:
        song = instruction.replace("play", "")
        talk("playing " + song)
        pywhatkit.playonyt(song)
    elif 'time' in instruction:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + current_time)
    elif 'date' in instruction:
        current_date = datetime.datetime.now().strftime('%d/%m/%Y')
        talk("Today's date is " + current_date)
    elif 'how are you' in instruction:
        talk('I am fine, how about you')
    elif 'what is your name' in instruction:
        talk('My name is Krishna, how can I help you?')
    elif 'what is' in instruction:
        query = instruction.replace('what is', '')
        info = wikipedia.summary(query, 1)
        print(info)
        talk(info)
    else:
        talk('Please repeat again')
play_Krishna()