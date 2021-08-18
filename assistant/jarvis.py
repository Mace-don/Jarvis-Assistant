import speech_recognition as sr
from utils.utils import Utils
from intents.applications import Applications
from intents.music import Music
from intents.volume import Volume
import threading


class Jarvis(threading.Thread):
    def __init__(self,config,logger):
        threading.Thread.__init__(self)
        self.config = config
        self.logger = logger
        self.speech = sr.Recognizer()
        self.utils = Utils(logger)

    def read_voice_input(self,recognizer):
        try:
            with sr.Microphone() as source:
                self.logger.info("Listening.....")
                voice_input = recognizer.listen(source,timeout=5, phrase_time_limit=5)
                command = recognizer.recognize_google(voice_input).lower()
                return command
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            self.logger.info = "Network Error"
        except sr.WaitTimeoutError as e:
            pass

    def run(self):
        self.logger.info("Running Thread...")
        session = False
        while True:
            input = self.read_voice_input(self.speech)
            if input:
                self.logger.info('Voice Input: {}'.format(input))
                for key in self.config:
                    matched = self.utils.match_utterances(input,self.config[key]['utterances'])
                    if matched:
                        break
                self.logger.info('Executed intent '+key)

                if key == "intent_greeting":
                    response = Utils.choose(self.config[key]['responses'])
                    self.logger.info(response)
                    self.utils.playSound(response)
                    session = True
                if session:
                    if key == "intent_applications":
                        response = Utils.choose(self.config[key]['responses'])
                        try:
                            Applications(logger=self.logger,command=input,application=self.config[key]['applications']).launch_app()
                            self.logger.info(response)
                            self.utils.playSound(response)
                        except Exception as e:
                            self.utils.playSound("No application installed sir")
                    if key == "intent_music":
                        Music(logger=self.logger,command=input,utterances=self.config[key]['utterances']).start()
                        response = Utils.choose(self.config[key]['responses'])
                        self.utils.playSound(response)
                    if key == "intent_volume":
                        Volume(logger=self.logger,command=input,utterances=self.config[key]['utterances']).start()
                    if key == "intent_oops":
                        response = Utils.choose(self.config[key]['responses'])
                        self.utils.playSound(response)

