import threading
import os
import pywhatkit


class Music(threading.Thread):

    def __init__(self,logger,command,utterances):
        threading.Thread.__init__(self)
        self.logger = logger
        self.command = command
        self.utterances = utterances

    def get_cmd_word(self):
        cmd_word = self.command
        for i in self.utterances:
            if i in cmd_word:
                return cmd_word

    def run(self):
        self.logger.info(self.command)
        self.what_to_play()

    def runScript(self):
        cmd_word = self.get_cmd_word()
        if cmd_word in ["next","previous"]:
            cmd_word = cmd_word + " track"
        cmd = '''osascript -e 'tell app "Music" to {}' '''.format(cmd_word).strip()
        os.system(cmd)

    @staticmethod
    def is_music_open():
        script = '''osascript {}'''.format("isMusicRunning.scpt")
        music = os.system(script)
        if music:
            return True
        else:
            return False

    def what_to_play(self):
        if self.is_music_open():
            self.runScript()
        else:
            song = self.command.replace('play', '')
            pywhatkit.playonyt(song)

