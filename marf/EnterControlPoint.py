# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

import Controller


class AddControlPoint(QtWidgets.QDialog):
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
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 285, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.editX = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.editX.setObjectName("editX")
        self.gridLayout.addWidget(self.editX, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.editY = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.editY.setObjectName("editY")
        self.gridLayout.addWidget(self.editY, 3, 2, 1, 1)
        self.editName = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.editName.setObjectName("editName")
        self.gridLayout.addWidget(self.editName, 1, 1, 1, 2)
        self.enterBtn = QtWidgets.QPushButton(self)
        self.enterBtn.setGeometry(QtCore.QRect(110, 240, 75, 23))
        self.enterBtn.setObjectName("enterBtn")
        self.cancelBtn = QtWidgets.QPushButton(self)
        self.cancelBtn.setGeometry(QtCore.QRect(210, 240, 75, 23))
        self.cancelBtn.setObjectName("cancelBtn")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Enter Control Point"))
        self.label.setText(_translate("Dialog", "Unique Name:"))
        self.label_2.setText(_translate("Dialog", "Coordinates:"))
        self.enterBtn.setText(_translate("Dialog", "Enter"))
        self.cancelBtn.setText(_translate("Dialog", "Cancel"))
        #################################################################
        self.onlyInt = QtGui.QIntValidator(0, 100)
        self.editX.setValidator(self.onlyInt)
        self.editY.setValidator(self.onlyInt)
        #################################################################
        self.enterBtn.clicked.connect(self.onClickEnter)
        self.cancelBtn.clicked.connect(self.onClickCancel)

    def onClickEnter(self):
        try:
            self.controlPoint = Controller.ControlPoint(map=self.map, posX=int(self.editX.text()),
                                                        posY=int(self.editY.text()), name=self.editName.text())
            print(self.controlPoint.toJSON())
            self.accept()
        except ValueError as v:
            self.error = "Fill all the empty fields."
            self.reject()
        except Exception as e:
            self.error = e.__str__()
            self.reject()

    def onClickCancel(self):
        self.reject()
