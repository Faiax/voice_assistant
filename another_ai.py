import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import wikipedia
import random
import calendar
# -----------------------------------------------

# Ignore any warning messages
warnings.filterwarnings('ignore')


# record audio adn return it as a string
def recordAudio():
    # record the audio
    r = sr.Recognizer() # creating a recognizer object
    # Open the microphone and start recording
    with sr.Microphone as source:
        print('say something')
        audio = r.listen(source)

    # use google speech recognition
    data = ''
    try:
        data = r.recognize_google(audio)
        print('You said: ' + data)
    except sr.UnknownValueError: # Check for unknow errors
        print("Google speech recognition could not understand the audio, unknown error")
    except sr.RequestError as e:
        print('Request result from Google speech recognition service error' + e)
