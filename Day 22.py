'''
import pyttsx3

engine = pyttsx3.init()

def voice_text(text):
    engine.say(text)
    engine.runAndWait()

voice_text("Good morning") 

import pyttsx3

engine = pyttsx3.init()

song = ("Twinkle twinkle little star...How i wonder what you are")

engine.say(song)
engine.runAndWait()  


import pyttsx3

engine = pyttsx3.init()

def voice_speak(text):
    engine.say(text)
voice_speak("Hello, iam sangeetha")
voice_speak("What's your plan today")
engine.runAndWait()           

import pyttsx3
engine = pyttsx3.init()
def speak_text(text):
    engine.say(text)
user_text = input("enter your message : ").lower( )
name = "user"
if "my name is " in user_text:
    name = user_text.split("my name is ")[-1].strip( )
elif "name is " in user_text:
    name = user_text.split("name is ")[-1].strip( )

if user_text in["hi","hello","hey"]:
    response = "Hello ! How can i help u?"
elif "name" in user_text:
    response = f" Hello (Sangeetha),how can i help u?"
else :
    response = "sorry ,i didnt understand that"
print(response)
speak_text(response)
engine.runAndWait( ) '''

import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)   # 0 = male, 1 = female

engine.say("This is female voice")
engine.runAndWait()



    





