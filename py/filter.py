import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap

form_class = uic.loadUiType("filter.ui")[0]
select_effect = 0


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint))
        self.setMaximumSize(480, 320)
        self.showMaximized()

        self.btn_1.clicked.connect(self.btn1print)
        self.btn_2.clicked.connect(self.btn2print)
        self.btn_3.clicked.connect(self.btn3print)

        self.slider.valueChanged.connect(self.sliderEv)

        self.btn_f.clicked.connect(self.btnfprint)
        self.btnExit.clicked.connect(self.exit)

    def sliderEv(self):
        if select_effect == 1:
            self.slider.valueChanged.connect(self.btn1print)
        else:
            self.slider.valueChanged.disconnect()

    def btn1print(self):
        global select_effect
        if select_effect > 0:
            # fname = QFileDialog.getOpenFileName(self, 'Open file', './')
            # with open(fname[0], encoding='UTF8') as f:
            # data = f.read()
            select_effect = 1
            image = cv2.imread(fname[0])

            size = self.slider.value()

            motion_blur = np.zeros((size, size))
            motion_blur[int((size - 1) / 2), :] = np.ones(size)
            motion_blur = motion_blur / size

            mv = cv2.filter2D(image, -1, motion_blur)

            height, width, channel = mv.shape

            qImg = QtGui.QImage(mv.data, width, height, QtGui.QImage.Format_RGB888).rgbSwapped()
            self.label.setPixmap(QPixmap.fromImage(qImg))

    def btn2print(self):
        global select_effect
        if select_effect > 0:
            select_effect = 2
            # 소벨
            image = cv2.imread(fname[0])
            # cv2.imread('C:/pc/dog.jpg')

            sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
            sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
            sobel_x = cv2.convertScaleAbs(sobel_x)
            sobel_y = cv2.convertScaleAbs(sobel_y)
            img_sobel = cv2.addWeighted(sobel_x, 1, sobel_y, 1, 0)

            height, width, channel = img_sobel.shape

            qImg = QtGui.QImage(img_sobel.data, width, height, QtGui.QImage.Format_RGB888).rgbSwapped()
            self.label.setPixmap(QPixmap.fromImage(qImg))

    def btn3print(self):
        global select_effect
        if select_effect > 0:
            select_effect = 3
            image = cv2.imread(fname[0])

            # embossing = np.array([[1, 0, 0], [0, 0, 0], [0, 0, -1]])

            # gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            #  image_em = cv2.filter2D(gray_image, -1, embossing) + 128

            # 1) Edges
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            gray = cv2.medianBlur(gray, 5)
            edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

            # 2) Color
            color = cv2.bilateralFilter(image, 9, 300, 300)

            # 3) Cartoon
            cartoon = cv2.bitwise_and(color, color, mask=edges)

            height, width, channel = cartoon.shape

            qImg = QtGui.QImage(cartoon.data, width, height, QtGui.QImage.Format_RGB888).rgbSwapped()
            self.label.setPixmap(QPixmap.fromImage(qImg))

    def btnfprint(self):
        global fname, select_effect
        fileDialog = QFileDialog(self, 'Open file', '../', "JPEG (*.jpg *.jpeg);; PNG (*.png);; All files (*.*)")
        fileDialog.setMaximumSize(480, 320)
        fileDialog.showMaximized()
        fileDialog.exec()
        fname = fileDialog.selectedFiles()

        if fname[0]:
            QMessageBox.about(self, "Alert", "Loaded. Select Filter")
            select_effect = 1
        else:
            QMessageBox.about(self, "Alert", "Open image first")

    def exit(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myFilterWindow = WindowClass()
    myFilterWindow.show()
    app.exec_()
