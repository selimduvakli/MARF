# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

import Controller


class AddDrone(QtWidgets.QDialog):
    def __init__(self, map):
        super().__init__()
        self.setupUi()
        self.map = map

    def setupUi(self):
        self.setObjectName("Dialog")
        self.setFixedSize(400, 300)
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(50, 50, 291, 171))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 291, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)
        self.editName = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.editName.setObjectName("editName")
        self.gridLayout.addWidget(self.editName, 0, 2, 1, 2)
        self.editX = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.editX.setObjectName("editX")
        self.gridLayout.addWidget(self.editX, 1, 2, 1, 1)
        self.comboBoxAlg = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBoxAlg.setObjectName("comboBoxAlg")
        self.comboBoxAlg.addItem("")
        self.comboBoxAlg.addItem("")
        self.gridLayout.addWidget(self.comboBoxAlg, 3, 2, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.editY = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.editY.setObjectName("editY")
        self.gridLayout.addWidget(self.editY, 1, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.spinBoxRntmCap = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBoxRntmCap.setMinimum(1)
        self.spinBoxRntmCap.setMaximum(100)
        self.spinBoxRntmCap.setObjectName("spinBoxRntmCap")
        self.gridLayout.addWidget(self.spinBoxRntmCap, 2, 2, 1, 2)
        self.enterBtn = QtWidgets.QPushButton(self)
        self.enterBtn.setGeometry(QtCore.QRect(110, 240, 75, 23))
        self.enterBtn.setObjectName("enterBtn")
        self.cancelBtn = QtWidgets.QPushButton(self)
        self.cancelBtn.setGeometry(QtCore.QRect(210, 240, 75, 23))
        self.cancelBtn.setObjectName("cancelBtn")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Add Drone"))
        self.label_3.setText(_translate("Dialog", " Runtime Capacity:"))
        self.label_4.setText(_translate("Dialog", " Algorithm:"))
        self.comboBoxAlg.setItemText(0, _translate("Dialog", "A* Algorithm"))
        self.comboBoxAlg.setItemText(1, _translate("Dialog", "Genetic Algorithm"))
        self.label_2.setText(_translate("Dialog", " Starting Point:"))
        self.label.setText(_translate("Dialog", " Unique Name:"))
        self.enterBtn.setText(_translate("Dialog", "Enter"))
        self.cancelBtn.setText(_translate("Dialog", "Cancel"))
        ######################################################################
        self.onlyInt = QtGui.QIntValidator(0, 100)
        self.editX.setValidator(self.onlyInt)
        self.editY.setValidator(self.onlyInt)
        self.enterBtn.clicked.connect(self.onClickEntr)
        self.cancelBtn.clicked.connect(self.reject)

    def onClickEntr(self):
        try:
            name = self.editName.text()
            startPoint = Controller.Point(self.map, int(self.editX.text()), int(self.editY.text()))
            runtmCap = self.spinBoxRntmCap.value()
            if self.comboBoxAlg.currentIndex() == 0:
                alg = "A*"
            elif self.comboBoxAlg.currentIndex() == 1:
                alg = "Genetic"
            self.drone = Controller.Drone(self.map, name, startPoint, runtmCap, alg)
            print(self.drone.toJSON())
            self.accept()
        except ValueError as v:
            self.error = "Fill all the empty fields."
            self.reject()
        except Exception as e:
            self.error = e.__str__()
            self.reject()
