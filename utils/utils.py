import pyttsx3
import re
import random
import os
import nest_asyncio


class Utils:

    def __init__(self,logger):
        self.logger = logger
        self.engine = pyttsx3.init()

    def playSound(self,text):
        self.engine.setProperty('voice', 'com.apple.speech.synthesis.voice.Alex')
        self.engine.setProperty('rate',250)
        os.system('say -v Alex "{}" -r 200'.format(text))

        #self.engine.say(text)
        #self.engine.runAndWait()

    @staticmethod
    def normalize_utterances(utterances):
        normalized = ''
        for i in utterances:
            normalized += i.lower() + '|'
        return normalized[:-1]

    def match_utterances(self,voice_input,utterances):
        self.logger.info("Normalizing utterances...")
        normalized = Utils.normalize_utterances(utterances)
        pattern = re.compile(normalized)
        value = pattern.search(voice_input)
        return value

    @staticmethod
    def choose(responses):
        return random.choice(responses)

