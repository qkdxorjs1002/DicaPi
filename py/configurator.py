import json
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import configurator_ui as ui

default_config = {
    "Brightness": 50, # 0~100, default 50 / step : 10
    "Contrast": 0, # -100~100, default 0 / step : 10
    "Saturation": 0, # -100~100, default 0 / step : 10
    "ShutterSpd": 0, # 0, 50~1000, default 0 / step : 50
    "ISO": 0, # 0, 100, 200, 320, 400, 500, 640, 800, default 0
    "Sharpness": 0, # -100~100, default 0 / step : 10
    "AWB": 'auto', # 'off', 'auto', 'sunlight', 'cloudy', 'shade', 'tungsten', 'fluorescent', 'incandescent', 'flash', 'horizon', default 1
    "ExposureMode": 'auto', # 'off', 'auto', 'night', 'nightpreview', 'backlight', 'spotlight', 'sports', 'snow', 'beach', 'verylong', 'fixedfps', 'antishake', 'fireworks', default 1
    "Vflip": 'False', # False, True, default False
    "Hflip": 'False', # False, True, default False
    "Rotation": 90, # 0, 90, 180, 270, default 90
    "TimerDelay": 5, # 1~10, default 5 / step : 1
}

iso_table = [0, 100, 200, 320, 400, 500, 640, 800]
awb_table = ['off', 'auto', 'sunlight', 'cloudy', 'shade', 'tungsten', 'fluorescent', 'incandescent', 'flash', 'horizon']
exposure_table = ['off', 'auto', 'night', 'nightpreview', 'backlight', 'spotlight', 'sports', 'snow', 'beach', 'verylong', 'fixedfps', 'antishake', 'fireworks']
rotation_table = [0, 90, 180, 270]


class WindowClass(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint))
        self.setMaximumSize(480, 320)
        self.showMaximized()

        ### Save Exit ###
        self.btnSaveExit.clicked.connect(self.saveExit)

        ### Load Default ###
        self.btnDefault.clicked.connect(self.loadDefault)

        ### Brightness ###
        self.btnBrightness_down.clicked.connect(lambda: self.decreaseValue(self.btnBrightness_down.objectName()))
        self.btnBrightness_up.clicked.connect(lambda: self.increaseValue(self.btnBrightness_up.objectName()))

        ### Contrast ###
        self.btnContrast_down.clicked.connect(lambda: self.decreaseValue(self.btnContrast_down.objectName()))
        self.btnContrast_up.clicked.connect(lambda: self.increaseValue(self.btnContrast_up.objectName()))

        ### Saturation ###
        self.btnSaturation_down.clicked.connect(lambda: self.decreaseValue(self.btnSaturation_down.objectName()))
        self.btnSaturation_up.clicked.connect(lambda: self.increaseValue(self.btnSaturation_up.objectName()))

        ### Shutter Speed ###
        self.btnShutterSpd_down.clicked.connect(lambda: self.decreaseValue(self.btnShutterSpd_down.objectName()))
        self.btnShutterSpd_up.clicked.connect(lambda: self.increaseValue(self.btnShutterSpd_up.objectName()))

        ### ISO ###
        self.btnISO_down.clicked.connect(lambda: self.decreaseValue(self.btnISO_down.objectName()))
        self.btnISO_up.clicked.connect(lambda: self.increaseValue(self.btnISO_up.objectName()))

        ### Sharpness ###
        self.btnSharpness_down.clicked.connect(lambda: self.decreaseValue(self.btnSharpness_down.objectName()))
        self.btnSharpness_up.clicked.connect(lambda: self.increaseValue(self.btnSharpness_up.objectName()))

        ### AWB ###
        self.btnAWB_toggle.clicked.connect(lambda: self.toggleValue(self.btnAWB_toggle.objectName()))

        ### Exposure ###
        self.btnExposure_toggle.clicked.connect(lambda: self.toggleValue(self.btnExposure_toggle.objectName()))

        ### Vflip ###
        self.btnVflip_toggle.clicked.connect(lambda: self.toggleValue(self.btnVflip_toggle.objectName()))

        ### Hflip ###
        self.btnHflip_toggle.clicked.connect(lambda: self.toggleValue(self.btnHflip_toggle.objectName()))

        ### Rotation ###
        self.btnRotation_down.clicked.connect(lambda: self.decreaseValue(self.btnRotation_down.objectName()))
        self.btnRotation_up.clicked.connect(lambda: self.increaseValue(self.btnRotation_up.objectName()))

        ### Timer Delay ###
        self.btnTimerDelay_down.clicked.connect(lambda: self.decreaseValue(self.btnTimerDelay_down.objectName()))
        self.btnTimerDelay_up.clicked.connect(lambda: self.increaseValue(self.btnTimerDelay_up.objectName()))

        ### Load Config from config.json ###
        self.loadConfig()

    def loadConfig(self):
        try:
            f = open("./config.json", 'r')
            config_json = f.read()
            f.close()
            config = json.loads(config_json)
        except FileNotFoundError:
            config = default_config

        self.lblBrightness_value.setText(str(config["Brightness"]))
        self.lblContrast_value.setText(str(config["Contrast"]))
        self.lblSaturation_value.setText(str(config["Saturation"]))
        self.lblShutterSpd_value.setText(str(config["ShutterSpd"]))
        self.lblISO_value.setText(str(config["ISO"]))
        self.lblSharpness_value.setText(str(config["Sharpness"]))
        self.lblAWB_value.setText(str(config["AWB"]))
        self.lblExposure_value.setText(str(config["ExposureMode"]))
        self.lblVflip_value.setText(str(config["Vflip"]))
        self.lblHflip_value.setText(str(config["Hflip"]))
        self.lblRotation_value.setText(str(config["Rotation"]))
        self.lblTimerDelay_value.setText(str(config["TimerDelay"]))
        self.saveConfig()

    def saveConfig(self):
        config = {
            "Brightness": int(self.lblBrightness_value.text()),
            "Contrast": int(self.lblContrast_value.text()),
            "Saturation": int(self.lblSaturation_value.text()),
            "ShutterSpd": int(self.lblShutterSpd_value.text()),
            "ISO": int(self.lblISO_value.text()),
            "Sharpness": int(self.lblSharpness_value.text()),
            "AWB": self.lblAWB_value.text(),
            "ExposureMode": self.lblExposure_value.text(),
            "Vflip": str(self.lblVflip_value.text()),
            "Hflip": str(self.lblHflip_value.text()),
            "Rotation": int(self.lblRotation_value.text()),
            "TimerDelay": int(self.lblTimerDelay_value.text()),
        }
        config_json = json.dumps(config)
        if config_json:
            f = open("./config.json", 'w')
            f.write(config_json)
            f.close()
        else:
            QMessageBox.about(self, "Error", "Invalid Config")

    def loadDefault(self):
        config = default_config
        self.lblBrightness_value.setText(str(config["Brightness"]))
        self.lblContrast_value.setText(str(config["Contrast"]))
        self.lblSaturation_value.setText(str(config["Saturation"]))
        self.lblShutterSpd_value.setText(str(config["ShutterSpd"]))
        self.lblISO_value.setText(str(config["ISO"]))
        self.lblSharpness_value.setText(str(config["Sharpness"]))
        self.lblAWB_value.setText(str(config["AWB"]))
        self.lblExposure_value.setText(str(config["ExposureMode"]))
        self.lblVflip_value.setText(str(config["Vflip"]))
        self.lblHflip_value.setText(str(config["Hflip"]))
        self.lblRotation_value.setText(str(config["Rotation"]))
        self.lblTimerDelay_value.setText(str(config["TimerDelay"]))
        QMessageBox.about(self, "Alert", "Default Config")

    def saveExit(self):
        self.saveConfig()
        self.close()

    def increaseValue(self, objectName: str):
        if objectName == "btnBrightness_up":
            next_value = (int(self.lblBrightness_value.text()) + 10) % 110
            self.lblBrightness_value.setText(str(next_value))
        elif objectName == "btnContrast_up":
            next_value = (int(self.lblContrast_value.text()) + 10) % 110
            self.lblContrast_value.setText(str(next_value))
        elif objectName == "btnSaturation_up":
            next_value = (int(self.lblSaturation_value.text()) + 10) % 110
            self.lblSaturation_value.setText(str(next_value))
        elif objectName == "btnShutterSpd_up":
            next_value = int(self.lblShutterSpd_value.text()) + 50
            if next_value == 1050:
                next_value = 0
            self.lblShutterSpd_value.setText(str(next_value))
        elif objectName == "btnISO_up":
            next_idx = (iso_table.index(int(self.lblISO_value.text())) + 1) % 8
            self.lblISO_value.setText(str(iso_table[next_idx]))
        elif objectName == "btnSharpness_up":
            next_value = (int(self.lblSharpness_value.text()) + 10) % 110
            self.lblSharpness_value.setText(str(next_value))
        elif objectName == "btnRotation_up":
            next_idx = (rotation_table.index(int(self.lblRotation_value.text())) + 1) % 4
            self.lblRotation_value.setText(str(rotation_table[next_idx]))
        elif objectName == "btnTimerDelay_up":
            next_value = (int(self.lblTimerDelay_value.text()) % 10) + 1
            self.lblTimerDelay_value.setText(str(next_value))

    def decreaseValue(self, objectName: str):
        if objectName == "btnBrightness_down":
            next_value = int(self.lblBrightness_value.text()) - 10
            if next_value == -10:
                next_value = 100
            self.lblBrightness_value.setText(str(next_value))
        elif objectName == "btnContrast_down":
            next_value = int(self.lblContrast_value.text()) - 10
            if next_value == -110:
                next_value = 100
            self.lblContrast_value.setText(str(next_value))
        elif objectName == "btnSaturation_down":
            next_value = int(self.lblSaturation_value.text()) - 10
            if next_value == -110:
                next_value = 100
            self.lblSaturation_value.setText(str(next_value))
        elif objectName == "btnShutterSpd_down":
            next_value = int(self.lblShutterSpd_value.text()) - 50
            if next_value == -50:
                next_value = 1000
            self.lblShutterSpd_value.setText(str(next_value))
        elif objectName == "btnISO_down":
            next_idx = iso_table.index(int(self.lblISO_value.text())) - 1
            if next_idx == -1:
                next_idx = 7
            self.lblISO_value.setText(str(iso_table[next_idx]))
        elif objectName == "btnSharpness_down":
            next_value = int(self.lblSharpness_value.text()) - 10
            if next_value == -110:
                next_value = 100
            self.lblSharpness_value.setText(str(next_value))
        elif objectName == "btnRotation_down":
            next_idx = rotation_table.index(int(self.lblRotation_value.text())) - 1
            if next_idx == -1:
                next_idx = 3
            self.lblRotation_value.setText(str(rotation_table[next_idx]))
        elif objectName == "btnTimerDelay_down":
            next_value = int(self.lblTimerDelay_value.text()) - 1
            if next_value == 0:
                next_value = 10
            self.lblTimerDelay_value.setText(str(next_value))

    def toggleValue(self, objectName: str):
        if objectName == "btnAWB_toggle":
            next_idx = (awb_table.index(self.lblAWB_value.text()) + 1) % 10
            self.lblAWB_value.setText(awb_table[next_idx])
        elif objectName == "btnExposure_toggle":
            next_idx = (exposure_table.index(self.lblExposure_value.text()) + 1) % 13
            self.lblExposure_value.setText(exposure_table[next_idx])
        elif objectName == "btnVflip_toggle":
            self.lblVflip_value.setText(str(not (self.lblVflip_value.text() == "True")))
        elif objectName == "btnHflip_toggle":
            self.lblHflip_value.setText(str(not (self.lblHflip_value.text() == "True")))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = WindowClass()

    myWindow.show()

    app.exec_()
