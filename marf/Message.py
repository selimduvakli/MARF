# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets


class Message(QtWidgets.QDialog):

    def __init__(self, title, msg):
        super().__init__()
        self.setupUi(title, msg)

    def setupUi(self, title, msg):
        self.setObjectName("Dialog")
        self.setFixedSize(291, 197)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.btnOk = QtWidgets.QPushButton(self)
        self.btnOk.setObjectName("btnOk")
        self.verticalLayout.addWidget(self.btnOk, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(title, msg)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, title, msg):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", title))
        self.label.setText(_translate("Dialog", msg))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.btnOk.setText(_translate("Dialog", "OK"))
        self.btnOk.clicked.connect(self.accept)
