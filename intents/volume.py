import threading
import os


class Volume(threading.Thread):
    def __init__(self, logger, command,utterances):
        threading.Thread.__init__(self)
        self.logger = logger
        self.command = command
        self.utterances = utterances

    def get_cmd_and_execute(self):
        if self.command == "mute":
            script = "osascript -e 'set volume output volume 0' ".strip()
        else:
            vol_level = (self.command[-3]+self.command[-2]+self.command[-1]).strip()
            print(vol_level)
            if vol_level != "volume":
                pass
            else:
                if self.command[0] == "full":
                    vol_level = 100
                elif self.command[0] == "zero":
                    vol_level = 0
            script = "osascript -e 'set volume output volume {}'".format(vol_level)
        self.logger.info("Script is : "+str(script))
        os.system(script)

    def run(self):
        self.get_cmd_and_execute()