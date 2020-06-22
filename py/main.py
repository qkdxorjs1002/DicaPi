import os
import sys
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import main_ui as ui
import picamera
import RPi.GPIO as GPIO
import json
import time

camera = picamera.PiCamera(framerate=30, led_pin=13, sensor_mode=2)
camera.rotation = 90
camera.resolution = (2592, 1944)
save_to_path = "/home/pi"


class WindowClass(QMainWindow, ui.Ui_MainWindow):
    latest_captured_img = ""
    isTimerOn = False
    isFlashOn = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint))
        self.setMaximumSize(480, 320)
        self.showMaximized()
        self.btnCameraAction.clicked.connect(self.capture)
        self.btnVideoAction.clicked.connect(self.record)
        self.btnFnConfig.clicked.connect(self.openConfigurator)
        self.btnFnFilter.clicked.connect(self.openFilter)
        self.btnFnDelay.clicked.connect(self.toggleTimer)
        self.btnFnFlash.clicked.connect(self.toggleFlash)
        self.lblCamInfo.mousePressEvent = self.latestImage
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(16, GPIO.FALLING, callback=self.switchPressed, bouncetime=300)
        self.loadConfig()
        self.showPreview()

    def capture(self):
        self.timerAction()
        timenow = time.localtime()
        capture_name = "%s/image-%04d%02d%02d-%02d%02d%02d.jpg" % (
            save_to_path, timenow.tm_year, timenow.tm_mon, timenow.tm_mday,
            timenow.tm_hour, timenow.tm_min, timenow.tm_sec)
        camera.resolution = (2592, 1944)
        self.flashAction(True)
        camera.capture(capture_name)
        self.flashAction(False)
        self.latest_captured_img = capture_name
        self.lblCamInfo.setPixmap(QPixmap(self.latest_captured_img).scaled(50, 50, QtCore.Qt.KeepAspectRatio))

    def record(self):
        self.btnCameraAction.setIconSize(QSize(0, 0))
        self.btnCameraAction.clicked.disconnect()
        self.timerAction()
        timenow = time.localtime()
        capture_name = "%s/video-%04d%02d%02d-%02d%02d%02d.mp4" % (
            save_to_path, timenow.tm_year, timenow.tm_mon, timenow.tm_mday,
            timenow.tm_hour, timenow.tm_min, timenow.tm_sec)
        camera.resolution = (1920, 1080)
        self.flashAction(True)
        camera.start_recording(capture_name, format='h264')
        self.scnLiveView.setStyleSheet("color: rgb(255, 0, 0);")
        self.scnLiveView.setText("Recording...")
        self.btnVideoAction.clicked.disconnect()
        self.btnVideoAction.clicked.connect(self.stop_record)
        self.btnVideoAction.setIcon(QIcon(QPixmap("./img/img_video_action_stop.png")))

    def stop_record(self):
        camera.stop_recording()
        self.btnCameraAction.setIconSize(QSize(40, 40))
        self.btnCameraAction.clicked.connect(self.capture)
        self.flashAction(False)
        camera.resolution = (2592, 1944)
        self.scnLiveView.setStyleSheet("color: rgb(255, 255, 255);")
        self.scnLiveView.setText("")
        self.btnVideoAction.clicked.disconnect()
        self.btnVideoAction.clicked.connect(self.record)
        self.btnVideoAction.setIcon(QIcon(QPixmap("./img/img_video_action.png")))

    def timerAction(self):
        if self.isTimerOn:
            os.system("python timer.py")

    def flashAction(self, on):
        if self.isFlashOn:
            GPIO.output(13, on)

    def toggleTimer(self):
        self.isTimerOn = not self.isTimerOn

        if self.isTimerOn:
            self.btnFnDelay.setIcon(QIcon(QPixmap("./img/img_fn_delay_on.png")))
        else:
            self.btnFnDelay.setIcon(QIcon(QPixmap("./img/img_fn_delay_off.png")))

    def toggleFlash(self):
        self.isFlashOn = not self.isFlashOn

        if self.isFlashOn:
            self.btnFnFlash.setIcon(QIcon(QPixmap("./img/img_fn_flash_on.png")))
        else:
            self.btnFnFlash.setIcon(QIcon(QPixmap("./img/img_fn_flash_off.png")))

    def showPreview(self):
        camera.start_preview(alpha=255, fullscreen=False, window=(60, 0, 330, 320))

    def loadConfig(self):
        try:
            f = open("./config.json", 'r')
            config_json = f.read()
            f.close()
            config = json.loads(config_json)
            camera.brightness = int(config["Brightness"])
            camera.contrast = int(config["Contrast"])
            camera.saturation = int(config["Saturation"])
            camera.shutter_speed = int(config["ShutterSpd"])
            camera.iso = int(config["ISO"])
            camera.sharpness = int(config["Sharpness"])
            camera.awb_mode = str(config["AWB"])
            camera.exposure_mode = str(config["ExposureMode"])
            camera.vflip = (config["Vflip"] == "True")
            camera.hflip = (config["Hflip"] == "True")
            camera.rotation = int(config["Rotation"])
        except FileNotFoundError:
            self.openConfigurator()

    def openConfigurator(self):
        camera.stop_preview()
        camera.start_preview(alpha=255, fullscreen=False, window=(15, 0, 60, 60))
        os.system("python configurator.py")
        camera.stop_preview()
        self.loadConfig()
        self.showPreview()

    def openFilter(self):
        camera.stop_preview()
        os.system("python filter.py")
        self.showPreview()

    def latestImage(self, event):
        if self.latest_captured_img:
            camera.stop_preview()
            os.system("nomacs %s" % self.latest_captured_img)
            self.showPreview()

    def switchPressed(self, channel):
        self.capture()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = WindowClass()

    myWindow.show()

    app.exec_()

    try:
        time.sleep(0.1)
    finally:
        GPIO.cleanup()
        camera.stop_preview()
