import threading
import sys
from PyQt5.QtWidgets import QWidget,QLabel,QGraphicsDropShadowEffect, QApplication
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QTimer,QTime,Qt


class GUI(threading.Thread,QWidget):
    def __init__(self):
        QWidget.__init__(self)
        threading.Thread.__init__(self)
        self.setFixedSize(498,400)
        self.setStyleSheet('background-color:#000000')
        self.label_animation = QLabel(self)
        self.movie = QMovie('jarvis.gif')
        self.label_animation.setMovie(self.movie)
        self.time = QLabel(self)
        self.time.setAlignment(Qt.AlignCenter)
        self.time.resize(350,150)
        self.time.setStyleSheet("color:#00BFFF;background-color:transparent;font:80px;font-weight:bold")
        self.time.move(70,280)
        self.shadow_effect = QGraphicsDropShadowEffect()
        self.shadow_effect.setColor(QColor("#ffffff"))
        self.shadow_effect.setOffset(1,1)
        self.time.setGraphicsEffect(self.shadow_effect)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_time)
        self.timer.start(1000)
        self.movie.start()
        self.show()

    def run(self):
        self.show_time()

    def show_time(self):
        current_time = QTime.currentTime()
        current_time = current_time.toString("hh:mm:ss")
        self.time.setText(current_time)



