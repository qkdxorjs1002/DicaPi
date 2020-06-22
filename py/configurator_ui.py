from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.btnDefault = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDefault.sizePolicy().hasHeightForWidth())
        self.btnDefault.setSizePolicy(sizePolicy)
        self.btnDefault.setMaximumSize(QtCore.QSize(70, 16777215))
        self.btnDefault.setObjectName("btnDefault")
        self.verticalLayout_2.addWidget(self.btnDefault)
        self.btnSaveExit = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSaveExit.sizePolicy().hasHeightForWidth())
        self.btnSaveExit.setSizePolicy(sizePolicy)
        self.btnSaveExit.setMaximumSize(QtCore.QSize(70, 16777215))
        self.btnSaveExit.setObjectName("btnSaveExit")
        self.verticalLayout_2.addWidget(self.btnSaveExit)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnBrightness_down = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBrightness_down.sizePolicy().hasHeightForWidth())
        self.btnBrightness_down.setSizePolicy(sizePolicy)
        self.btnBrightness_down.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnBrightness_down.setObjectName("btnBrightness_down")
        self.horizontalLayout_2.addWidget(self.btnBrightness_down)
        self.lblBrightness_value = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblBrightness_value.sizePolicy().hasHeightForWidth())
        self.lblBrightness_value.setSizePolicy(sizePolicy)
        self.lblBrightness_value.setMinimumSize(QtCore.QSize(0, 0))
        self.lblBrightness_value.setAlignment(QtCore.Qt.AlignCenter)
        self.lblBrightness_value.setObjectName("lblBrightness_value")
        self.horizontalLayout_2.addWidget(self.lblBrightness_value)
        self.btnBrightness_up = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBrightness_up.sizePolicy().hasHeightForWidth())
        self.btnBrightness_up.setSizePolicy(sizePolicy)
        self.btnBrightness_up.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnBrightness_up.setObjectName("btnBrightness_up")
        self.horizontalLayout_2.addWidget(self.btnBrightness_up)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnContrast_down = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnContrast_down.sizePolicy().hasHeightForWidth())
        self.btnContrast_down.setSizePolicy(sizePolicy)
        self.btnContrast_down.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnContrast_down.setObjectName("btnContrast_down")
        self.horizontalLayout_3.addWidget(self.btnContrast_down)
        self.lblContrast_value = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblContrast_value.sizePolicy().hasHeightForWidth())
        self.lblContrast_value.setSizePolicy(sizePolicy)
        self.lblContrast_value.setMinimumSize(QtCore.QSize(0, 0))
        self.lblContrast_value.setAlignment(QtCore.Qt.AlignCenter)
        self.lblContrast_value.setObjectName("lblContrast_value")
        self.horizontalLayout_3.addWidget(self.lblContrast_value)
        self.btnContrast_up = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnContrast_up.sizePolicy().hasHeightForWidth())
        self.btnContrast_up.setSizePolicy(sizePolicy)
        self.btnContrast_up.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnContrast_up.setObjectName("btnContrast_up")
        self.horizontalLayout_3.addWidget(self.btnContrast_up)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btnSaturation_down = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSaturation_down.sizePolicy().hasHeightForWidth())
        self.btnSaturation_down.setSizePolicy(sizePolicy)
        self.btnSaturation_down.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnSaturation_down.setObjectName("btnSaturation_down")
        self.horizontalLayout_7.addWidget(self.btnSaturation_down)
        self.lblSaturation_value = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblSaturation_value.sizePolicy().hasHeightForWidth())
        self.lblSaturation_value.setSizePolicy(sizePolicy)
        self.lblSaturation_value.setMinimumSize(QtCore.QSize(0, 0))
        self.lblSaturation_value.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSaturation_value.setObjectName("lblSaturation_value")
        self.horizontalLayout_7.addWidget(self.lblSaturation_value)
        self.btnSaturation_up = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSaturation_up.sizePolicy().hasHeightForWidth())
        self.btnSaturation_up.setSizePolicy(sizePolicy)
        self.btnSaturation_up.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnSaturation_up.setObjectName("btnSaturation_up")
        self.horizontalLayout_7.addWidget(self.btnSaturation_up)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setObjectName("label_17")
        self.verticalLayout.addWidget(self.label_17)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.btnShutterSpd_down = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnShutterSpd_down.sizePolicy().hasHeightForWidth())
        self.btnShutterSpd_down.setSizePolicy(sizePolicy)
        self.btnShutterSpd_down.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnShutterSpd_down.setObjectName("btnShutterSpd_down")
        self.horizontalLayout_11.addWidget(self.btnShutterSpd_down)
        self.lblShutterSpd_value = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblShutterSpd_value.sizePolicy().hasHeightForWidth())
        self.lblShutterSpd_value.setSizePolicy(sizePolicy)
        self.lblShutterSpd_value.setMinimumSize(QtCore.QSize(0, 0))
        self.lblShutterSpd_value.setAlignment(QtCore.Qt.AlignCenter)
        self.lblShutterSpd_value.setObjectName("lblShutterSpd_value")
        self.horizontalLayout_11.addWidget(self.lblShutterSpd_value)
        self.btnShutterSpd_up = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnShutterSpd_up.sizePolicy().hasHeightForWidth())
        self.btnShutterSpd_up.setSizePolicy(sizePolicy)
        self.btnShutterSpd_up.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnShutterSpd_up.setObjectName("btnShutterSpd_up")
        self.horizontalLayout_11.addWidget(self.btnShutterSpd_up)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.btnISO_down = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnISO_down.sizePolicy().hasHeightForWidth())
        self.btnISO_down.setSizePolicy(sizePolicy)
        self.btnISO_down.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnISO_down.setObjectName("btnISO_down")
        self.horizontalLayout_10.addWidget(self.btnISO_down)
        self.lblISO_value = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblISO_value.sizePolicy().hasHeightForWidth())
        self.lblISO_value.setSizePolicy(sizePolicy)
        self.lblISO_value.setMinimumSize(QtCore.QSize(0, 0))
        self.lblISO_value.setAlignment(QtCore.Qt.AlignCenter)
        self.lblISO_value.setObjectName("lblISO_value")
        self.horizontalLayout_10.addWidget(self.lblISO_value)
        self.btnISO_up = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnISO_up.sizePolicy().hasHeightForWidth())
        self.btnISO_up.setSizePolicy(sizePolicy)
        self.btnISO_up.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnISO_up.setObjectName("btnISO_up")
        self.horizontalLayout_10.addWidget(self.btnISO_up)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btnSharpness_down = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSharpness_down.sizePolicy().hasHeightForWidth())
        self.btnSharpness_down.setSizePolicy(sizePolicy)
        self.btnSharpness_down.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnSharpness_down.setObjectName("btnSharpness_down")
        self.horizontalLayout_6.addWidget(self.btnSharpness_down)
        self.lblSharpness_value = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblSharpness_value.sizePolicy().hasHeightForWidth())
        self.lblSharpness_value.setSizePolicy(sizePolicy)
        self.lblSharpness_value.setMinimumSize(QtCore.QSize(0, 0))
        self.lblSharpness_value.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSharpness_value.setObjectName("lblSharpness_value")
        self.horizontalLayout_6.addWidget(self.lblSharpness_value)
        self.btnSharpness_up = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSharpness_up.sizePolicy().hasHeightForWidth())
        self.btnSharpness_up.setSizePolicy(sizePolicy)
        self.btnSharpness_up.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnSharpness_up.setObjectName("btnSharpness_up")
        self.horizontalLayout_6.addWidget(self.btnSharpness_up)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lblAWB_value = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblAWB_value.sizePolicy().hasHeightForWidth())
        self.lblAWB_value.setSizePolicy(sizePolicy)
        self.lblAWB_value.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAWB_value.setObjectName("lblAWB_value")
        self.horizontalLayout_9.addWidget(self.lblAWB_value)
        self.btnAWB_toggle = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAWB_toggle.sizePolicy().hasHeightForWidth())
        self.btnAWB_toggle.setSizePolicy(sizePolicy)
        self.btnAWB_toggle.setObjectName("btnAWB_toggle")
        self.horizontalLayout_9.addWidget(self.btnAWB_toggle)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_3.addWidget(self.label_23)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.lblExposure_value = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblExposure_value.sizePolicy().hasHeightForWidth())
        self.lblExposure_value.setSizePolicy(sizePolicy)
        self.lblExposure_value.setAlignment(QtCore.Qt.AlignCenter)
        self.lblExposure_value.setObjectName("lblExposure_value")
        self.horizontalLayout_14.addWidget(self.lblExposure_value)
        self.btnExposure_toggle = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnExposure_toggle.sizePolicy().hasHeightForWidth())
        self.btnExposure_toggle.setSizePolicy(sizePolicy)
        self.btnExposure_toggle.setObjectName("btnExposure_toggle")
        self.horizontalLayout_14.addWidget(self.btnExposure_toggle)
        self.verticalLayout_3.addLayout(self.horizontalLayout_14)
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_3.addWidget(self.label_19)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.lblVflip_value = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblVflip_value.sizePolicy().hasHeightForWidth())
        self.lblVflip_value.setSizePolicy(sizePolicy)
        self.lblVflip_value.setAlignment(QtCore.Qt.AlignCenter)
        self.lblVflip_value.setObjectName("lblVflip_value")
        self.horizontalLayout_12.addWidget(self.lblVflip_value)
        self.btnVflip_toggle = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnVflip_toggle.sizePolicy().hasHeightForWidth())
        self.btnVflip_toggle.setSizePolicy(sizePolicy)
        self.btnVflip_toggle.setObjectName("btnVflip_toggle")
        self.horizontalLayout_12.addWidget(self.btnVflip_toggle)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_3.addWidget(self.label_21)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.lblHflip_value = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblHflip_value.sizePolicy().hasHeightForWidth())
        self.lblHflip_value.setSizePolicy(sizePolicy)
        self.lblHflip_value.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHflip_value.setObjectName("lblHflip_value")
        self.horizontalLayout_13.addWidget(self.lblHflip_value)
        self.btnHflip_toggle = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnHflip_toggle.sizePolicy().hasHeightForWidth())
        self.btnHflip_toggle.setSizePolicy(sizePolicy)
        self.btnHflip_toggle.setObjectName("btnHflip_toggle")
        self.horizontalLayout_13.addWidget(self.btnHflip_toggle)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_3.addWidget(self.label_25)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.btnRotation_down = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRotation_down.sizePolicy().hasHeightForWidth())
        self.btnRotation_down.setSizePolicy(sizePolicy)
        self.btnRotation_down.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnRotation_down.setObjectName("btnRotation_down")
        self.horizontalLayout_15.addWidget(self.btnRotation_down)
        self.lblRotation_value = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblRotation_value.sizePolicy().hasHeightForWidth())
        self.lblRotation_value.setSizePolicy(sizePolicy)
        self.lblRotation_value.setMinimumSize(QtCore.QSize(0, 0))
        self.lblRotation_value.setAlignment(QtCore.Qt.AlignCenter)
        self.lblRotation_value.setObjectName("lblRotation_value")
        self.horizontalLayout_15.addWidget(self.lblRotation_value)
        self.btnRotation_up = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRotation_up.sizePolicy().hasHeightForWidth())
        self.btnRotation_up.setSizePolicy(sizePolicy)
        self.btnRotation_up.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnRotation_up.setObjectName("btnRotation_up")
        self.horizontalLayout_15.addWidget(self.btnRotation_up)
        self.verticalLayout_3.addLayout(self.horizontalLayout_15)
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_3.addWidget(self.label_29)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.btnTimerDelay_down = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnTimerDelay_down.sizePolicy().hasHeightForWidth())
        self.btnTimerDelay_down.setSizePolicy(sizePolicy)
        self.btnTimerDelay_down.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnTimerDelay_down.setObjectName("btnTimerDelay_down")
        self.horizontalLayout_17.addWidget(self.btnTimerDelay_down)
        self.lblTimerDelay_value = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTimerDelay_value.sizePolicy().hasHeightForWidth())
        self.lblTimerDelay_value.setSizePolicy(sizePolicy)
        self.lblTimerDelay_value.setMinimumSize(QtCore.QSize(0, 0))
        self.lblTimerDelay_value.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTimerDelay_value.setObjectName("lblTimerDelay_value")
        self.horizontalLayout_17.addWidget(self.lblTimerDelay_value)
        self.btnTimerDelay_up = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnTimerDelay_up.sizePolicy().hasHeightForWidth())
        self.btnTimerDelay_up.setSizePolicy(sizePolicy)
        self.btnTimerDelay_up.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnTimerDelay_up.setObjectName("btnTimerDelay_up")
        self.horizontalLayout_17.addWidget(self.btnTimerDelay_up)
        self.verticalLayout_3.addLayout(self.horizontalLayout_17)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnDefault.setText(_translate("MainWindow", "Default"))
        self.btnSaveExit.setText(_translate("MainWindow", "Exit"))
        self.label_2.setText(_translate("MainWindow", "Brightness"))
        self.btnBrightness_down.setText(_translate("MainWindow", "<"))
        self.lblBrightness_value.setText(_translate("MainWindow", "0"))
        self.btnBrightness_up.setText(_translate("MainWindow", ">"))
        self.label_4.setText(_translate("MainWindow", "Contrast"))
        self.btnContrast_down.setText(_translate("MainWindow", "<"))
        self.lblContrast_value.setText(_translate("MainWindow", "0"))
        self.btnContrast_up.setText(_translate("MainWindow", ">"))
        self.label_10.setText(_translate("MainWindow", "Saturation"))
        self.btnSaturation_down.setText(_translate("MainWindow", "<"))
        self.lblSaturation_value.setText(_translate("MainWindow", "0"))
        self.btnSaturation_up.setText(_translate("MainWindow", ">"))
        self.label_17.setText(_translate("MainWindow", "Shutter Speed"))
        self.btnShutterSpd_down.setText(_translate("MainWindow", "<"))
        self.lblShutterSpd_value.setText(_translate("MainWindow", "0"))
        self.btnShutterSpd_up.setText(_translate("MainWindow", ">"))
        self.label_15.setText(_translate("MainWindow", "ISO"))
        self.btnISO_down.setText(_translate("MainWindow", "<"))
        self.lblISO_value.setText(_translate("MainWindow", "0"))
        self.btnISO_up.setText(_translate("MainWindow", ">"))
        self.label_7.setText(_translate("MainWindow", "Sharpness"))
        self.btnSharpness_down.setText(_translate("MainWindow", "<"))
        self.lblSharpness_value.setText(_translate("MainWindow", "0"))
        self.btnSharpness_up.setText(_translate("MainWindow", ">"))
        self.label_12.setText(_translate("MainWindow", "AWB"))
        self.lblAWB_value.setText(_translate("MainWindow", "0"))
        self.btnAWB_toggle.setText(_translate("MainWindow", "Toggle"))
        self.label_23.setText(_translate("MainWindow", "Exposure Mode"))
        self.lblExposure_value.setText(_translate("MainWindow", "0"))
        self.btnExposure_toggle.setText(_translate("MainWindow", "Toggle"))
        self.label_19.setText(_translate("MainWindow", "Vertical Flip"))
        self.lblVflip_value.setText(_translate("MainWindow", "0"))
        self.btnVflip_toggle.setText(_translate("MainWindow", "Toggle"))
        self.label_21.setText(_translate("MainWindow", "Horizontal Flip"))
        self.lblHflip_value.setText(_translate("MainWindow", "0"))
        self.btnHflip_toggle.setText(_translate("MainWindow", "Toggle"))
        self.label_25.setText(_translate("MainWindow", "Rotation"))
        self.btnRotation_down.setText(_translate("MainWindow", "<"))
        self.lblRotation_value.setText(_translate("MainWindow", "0"))
        self.btnRotation_up.setText(_translate("MainWindow", ">"))
        self.label_29.setText(_translate("MainWindow", "Timer Delay"))
        self.btnTimerDelay_down.setText(_translate("MainWindow", "<"))
        self.lblTimerDelay_value.setText(_translate("MainWindow", "0"))
        self.btnTimerDelay_up.setText(_translate("MainWindow", ">"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
