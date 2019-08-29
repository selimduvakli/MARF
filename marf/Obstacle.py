# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

import Controller


class ObstacleUi(QtWidgets.QDialog):
    def __init__(self, map, title):
        super().__init__()
        self.title = title
        self.map = map
        self.setupUi(title)

    def setupUi(self, title):
        self.setObjectName("Dialog")
        self.setFixedSize(291, 213)
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 291, 171))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 291, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.editSizeX = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.editSizeX.setObjectName("editSizeX")
        self.horizontalLayout.addWidget(self.editSizeX)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.editSizeY = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.editSizeY.setObjectName("editSizeY")
        self.horizontalLayout.addWidget(self.editSizeY)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.enterBtn = QtWidgets.QPushButton(self)
        self.enterBtn.setGeometry(QtCore.QRect(60, 180, 75, 23))
        self.enterBtn.setObjectName("enterBtn")
        self.cancelBtn = QtWidgets.QPushButton(self)
        self.cancelBtn.setGeometry(QtCore.QRect(160, 180, 75, 23))
        self.cancelBtn.setObjectName("cancelBtn")

        self.retranslateUi(title)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, title):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", title))
        self.label.setText(_translate("Dialog", "Please Enter Coordinates of Obstacle:"))
        self.label_2.setText(_translate("Dialog", " X "))
        self.enterBtn.setText(_translate("Dialog", "Enter"))
        self.cancelBtn.setText(_translate("Dialog", "Cancel"))
        ####################################################################
        self.onlyInt = QtGui.QIntValidator(0, 100)
        self.editSizeX.setValidator(self.onlyInt)
        self.editSizeY.setValidator(self.onlyInt)
        self.enterBtn.clicked.connect(self.onClickEntr)
        self.cancelBtn.clicked.connect(self.onClickCncel)

    def onClickEntr(self):
        try:
            posX = int(self.editSizeX.text())
            posY = int(self.editSizeY.text())
            point = Controller.Point(self.map, posX, posY)
            if self.title == "Add Obstacle":
                self.map.addObstacle(point)
            elif self.title == "Delete Obstacle":
                self.map.deleteObstacle(point)
            print(self.map.yaz())
            self.accept()
        except Exception as e:
            self.error = e.__str__()
            self.reject()

    def onClickCncel(self):
        if hasattr(self, 'error'):
            delattr(self, 'error')
        self.reject()
