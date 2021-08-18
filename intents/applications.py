import os


class Applications:

    def __init__(self,logger,application,command):
        self.command = command
        self.logger = logger
        self.application = application

    def get_path(self):
        key = self.command.strip().split(' ')[1]
        for app,path in self.application.items():
            if app in key:
                return path

    def launch_app(self):
        self.logger.info('Return path: '+self.get_path())
        os.system('open {}'.format(self.get_path()))
