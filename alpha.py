import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import json
from test import ask_google
import googleSearch
import webbrowser
import time
import signal
import os

listener = sr.Recognizer()
engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.Alex')
engine.setProperty('rate',250)


class TimeoutException(Exception):   # Custom exception class
    pass


def break_after(seconds=2):
    def timeout_handler(signum, frame):   # Custom signal handler
        raise TimeoutException

    def function(function):
        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(seconds)
            try:
                res = function(*args, **kwargs)
                signal.alarm(0)      # Clear alarm
                return res
            except TimeoutException:
                print('Oops, timeout: %s sec reached.' % seconds, function.__name__, args, kwargs)
            return
        return wrapper
    return function


#@break_after(10)
def talk(text):
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    try:
        with sr.Microphone() as source:
            print("Listening.....")
            voices = listener.listen(source,timeout=5, phrase_time_limit=5)
            command = listener.recognize_google(voices).lower()
    except Exception as e:
        print(e)
    return command


def validate_input(input,commands):
    for cmd in commands:
        if cmd in input:
            return True


def launch(voice_command,launch_dict):
    for key,values in launch_dict.items():
        if key in voice_command:
            return values


def runAlexa():
    while True:
        command = takeCommand().strip().lower()
        print(command)
        quesWords = ['who', 'why']
        primeWords = ['minister', 'president']
        numerals = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']
        launch_cmd = ['open', 'launch', 'run']
        greeting_cmd = ['hello jarvis','hi jarvis','wake up jarvis']
        grateful_cmd = ['thank you jarvis','thanks jarvis','thank you very much jarvis','thanks','thank you']
        launch_dict = {'app store': '/Volumes/Omega/System/Applications/App\ Store.app', 'pycharm':'/Applications/PyCharm.app',
                       'downloads': '/Users/macedon/Downloads', 'library':'/Library','current directory':'.',
                       'youtube':"https://www.youtube.com",'clion':'/Applications/CLion.app'}

        if validate_input(command,greeting_cmd):
            talk("Hello Sir, how may I help you ?")
            continue
        elif validate_input(command,launch_cmd):
            path = launch(command,launch_dict)
            if os.uname().sysname == 'Darwin':
                cmd = 'open'
            else:
                cmd = 'explorer'
            cmd = cmd+" "+path
            talk("Opening Sir")
            os.system(cmd)
            continue
        elif validate_input(command,grateful_cmd):
            talk('It is my pleasure to serve you sir')
            continue
        elif 'play' in command:
            song = command.replace('play', '')
            talk('Playing ' + song)
            pywhatkit.playonyt(song)
            continue
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk("Current time is " + time)
            continue
        elif 'when' in command:
            answer = ask_google(command)
            talk(answer)
            continue
        elif not any(num in command for num in numerals):
            print('1')
            if any(word in command for word in primeWords):
                print('2')
                ind = command.index('the')
                s = command[0:ind + 4] + 'current ' + command[ind + 4:]
                answer = ask_google(s)
                talk(answer)
            elif any(word in command for word in quesWords):
                print('3')
                answer = ask_google(command)
                talk(answer)
                talk("Do you want additional information from web ?")
            else:
                print('4')
                answer = ask_google(command)
                talk(answer)
            continue
        elif any(num in command for num in numerals):
            print('5')
            if any(word in command for word in quesWords):
                print('6')
                if 'india' in command:
                    print('7')
                    answer = ask_google(command)
                    talk(answer)
                else:
                    print('8')
                    url = googleSearch.Search(command)
                    talk("Here is what I found on web ")
                    webbrowser.get().open(url)
            continue
        else:
            print("9")


runAlexa()