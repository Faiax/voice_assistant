import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
# This is for the quality of the voice
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[2].id)
# This is for the speed of speaking
engine.setProperty('rate', 170)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            listener.energy_threshold = 5000
            listener.adjust_for_ambient_noise(source, 1.2)
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk("playing" + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%p')
        print(time)
        talk('current time is' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'what is' and 'tell me about' in command:
        data = command.replace('what is', '')
        info = wikipedia.summary(data, 3)
        print(info)
        talk(info)
    elif 'who are you' in command:
        talk("HI!, I am a Personal assistant type Programme, created by Faiaz ")

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'what are you doing' in command:
        talk("I am doing nothing in particular.")

    elif 'stop' in command:
        talk('Okay, Quitting this program')
        quit()

    elif 'quit' in command:
        talk('Okay, Quitting this program')
        quit()

    elif 'hello' in command:
        talk('Hi! What can i do for you?')

    elif 'hi' in command:
        talk('Hi! What can i do for you?')

    elif 'how are you' in command:
        talk('I am feeling Amazing. Thanks for asking!')

    elif 'why were you created' in command:
        talk('I was created by Faiaz for particularly nothing. Thanks for asking!')

    elif 'who created you' in command:
        talk('I was created by Faiaz for particularly nothing. Thanks for asking!')

    elif 'where are you' in command:
        talk('I am stuck in this computer')

    elif 'are you alive' in command:
        talk('I am not a living being, I am just a program created by Faiaz.')

    elif 'are you stupid' in command:
        talk(' It depends on how you define intelligence. You should not expect any intelligence from a program')

    elif 'other language' in command:
        talk("Right now this program doesn't support any language other than English. ")

    elif 'do you know me' in command:
        talk(' If you are talking to me then there is a high chance that you are Faiaz.'
             ' If you are not Faiaz then you should not be here! ')

    elif 'what can you do' in command:
        talk('Hi! I am a voice assistant program and I can do different task. For example I can play a youtube video')

    else:
        talk('Sorry! Please say the command again.')


while True:
    run_alexa()