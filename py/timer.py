import json
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore
from PyQt5.QtCore import QTimer

form_class = uic.loadUiType("timer.ui")[0]


class TestWindow(QMainWindow, form_class):
    timer = QTimer()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint))
        self.setGeometry(0, 0, 50, 50)
        self.loadConfig()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.timerTick)
        self.timerLabel.setText("%ds" % self.count)
        self.timer.start()

    def timerTick(self):
        self.count -= 1
        self.timerLabel.setText("%ds" % self.count)
        if self.count < 1:
            self.timer.stop()
            self.close()

    def loadConfig(self):
        try:
            f = open("./config.json", 'r')
            config_json = f.read()
            f.close()
            config = json.loads(config_json)
            self.count = int(config["TimerDelay"])

        except FileNotFoundError:
            self.count = 5


if __name__ == "__main__":
    app = QApplication(sys.argv)
    testWindow = TestWindow()
    testWindow.show()
    app.exec_()
