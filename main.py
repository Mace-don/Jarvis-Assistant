import json
from assistant.jarvis import Jarvis
import logging
from PyQt5.QtWidgets import QApplication
from assistant.gui import GUI
import sys
import time

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)s:%(message)s',
                        datefmt='%Y-%m-%d %H-%M-%S')

    with open('config/config.json') as file:
        config = json.load(file)
    logging.info("Jarvis is initialising...")
    app = QApplication(sys.argv)
    obj = Jarvis(config=config, logger=logging)
    gui = GUI()
    obj.start()
    gui.start()
    app.exit(app.exec_())
