# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

import Controller


class AddAgent(QtWidgets.QDialog):
    def __init__(self, title, map):
        super().__init__()
        self.setupUi(title)
        self.title = title
        self.map = map

    def setupUi(self, title):
        self.setObjectName("Dialog")
        self.setFixedSize(400, 300)
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(50, 50, 291, 171))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, 0, 291, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBoxFuel = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBoxFuel.setObjectName("comboBoxFuel")
        self.comboBoxFuel.addItem("")
        self.comboBoxFuel.addItem("")
        self.comboBoxFuel.addItem("")
        self.comboBoxFuel.addItem("")
        self.gridLayout.addWidget(self.comboBoxFuel, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.editName = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.editName.setObjectName("editName")
        self.gridLayout.addWidget(self.editName, 0, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.editX = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.editX.setObjectName("editX")
        self.gridLayout.addWidget(self.editX, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.editY = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.editY.setObjectName("editY")
        self.gridLayout.addWidget(self.editY, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.spinBoxSpeed = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBoxSpeed.setMinimum(1)
        self.spinBoxSpeed.setMaximum(5)
        self.spinBoxSpeed.setObjectName("spinBoxSpeed")
        self.gridLayout.addWidget(self.spinBoxSpeed, 3, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioWeak = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioWeak.setChecked(True)
        self.radioWeak.setObjectName("radioWeak")
        self.horizontalLayout.addWidget(self.radioWeak)
        self.radioMedium = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioMedium.setObjectName("radioMedium")
        self.horizontalLayout.addWidget(self.radioMedium)
        self.radioStrong = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioStrong.setObjectName("radioStrong")
        self.horizontalLayout.addWidget(self.radioStrong)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 1, 1, 2)
        self.enterBtn = QtWidgets.QPushButton(self)
        self.enterBtn.setGeometry(QtCore.QRect(110, 240, 75, 23))
        self.enterBtn.setObjectName("enterBtn")
        self.cancelBtn = QtWidgets.QPushButton(self)
        self.cancelBtn.setGeometry(QtCore.QRect(210, 240, 75, 23))
        self.cancelBtn.setObjectName("cancelBtn")

        self.retranslateUi(title)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, title):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Add " + title))
        self.comboBoxFuel.setItemText(0, _translate("Dialog", "25%"))
        self.comboBoxFuel.setItemText(1, _translate("Dialog", "50%"))
        self.comboBoxFuel.setItemText(2, _translate("Dialog", "75%"))
        self.comboBoxFuel.setItemText(3, _translate("Dialog", "100%"))
        self.label.setText(_translate("Dialog", " Unique Name:"))
        self.label_3.setText(_translate("Dialog", " Fuel Percentage:"))
        self.label_5.setText(_translate("Dialog", " Power Capacity:"))
        self.label_4.setText(_translate("Dialog", " Speed:"))
        self.label_2.setText(_translate("Dialog", " Starting Point:"))
        self.radioWeak.setText(_translate("Dialog", "Weak"))
        self.radioMedium.setText(_translate("Dialog", "Medium"))
        self.radioStrong.setText(_translate("Dialog", "Strong"))
        self.enterBtn.setText(_translate("Dialog", "Enter"))
        self.cancelBtn.setText(_translate("Dialog", "Cancel"))
        ###############################################################
        self.onlyInt = QtGui.QIntValidator(0, 100)
        self.editX.setValidator(self.onlyInt)
        self.editY.setValidator(self.onlyInt)
        self.enterBtn.clicked.connect(self.onClickEntr)
        self.cancelBtn.clicked.connect(self.onClickCncl)

    def onClickCncl(self):
        self.reject()

    def onClickEntr(self):
        try:
            name = self.editName.text()
            startPoint = Controller.Point(self.map, int(self.editX.text()), int(self.editY.text()))
            type = self.title
            fuel = self.comboBoxFuel.currentIndex() * 25 + 25
            speed = self.spinBoxSpeed.value()
            if self.radioWeak.isChecked():
                power = 'Weak'
            elif self.radioMedium.isChecked():
                power = 'Medium'
            elif self.radioStrong.isChecked():
                power = 'Strong'
            vehicle = Controller.Vehicle(self.map, name, type, startPoint, fuel, speed, power)
            print(vehicle.toJSON())
            self.accept()
        except ValueError as v:
            self.error = "Fill all the empty fields."
            self.reject()
        except Exception as e:
            self.error = e.__str__()
            self.reject()
