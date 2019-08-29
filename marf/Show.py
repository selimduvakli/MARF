# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

import Controller


class MyQListWidgetItem(QtWidgets.QListWidgetItem):
    def __init__(self, item, QlistW):
        super().__init__(item.name, QlistW)
        self.item = item


class ShowTasks(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Dialog")
        self.setFixedSize(400, 300)
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(50, 50, 291, 171))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 291, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        # item = QtWidgets.QListWidgetItem()
        # self.listWidget.addItem(item)
        # item = QtWidgets.QListWidgetItem()
        # self.listWidget.addItem(item)
        # item = QtWidgets.QListWidgetItem()
        # self.listWidget.addItem(item)
        # item = QtWidgets.QListWidgetItem()
        # self.listWidget.addItem(item)
        # item = QtWidgets.QListWidgetItem()
        # self.listWidget.addItem(item)
        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 1)
        self.killBtn = QtWidgets.QPushButton(self)
        self.killBtn.setGeometry(QtCore.QRect(110, 240, 75, 23))
        self.killBtn.setObjectName("killBtn")
        self.closeBtn = QtWidgets.QPushButton(self)
        self.closeBtn.setGeometry(QtCore.QRect(210, 240, 75, 23))
        self.closeBtn.setObjectName("closeBtn")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Tasks"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        # item = self.listWidget.item(0)
        # item.setText(_translate("Dialog", "Task 1"))
        # item = self.listWidget.item(1)
        # item.setText(_translate("Dialog", "Task 2"))
        # item = self.listWidget.item(2)
        # item.setText(_translate("Dialog", "Task 3"))
        # item = self.listWidget.item(3)
        # item.setText(_translate("Dialog", "Task 4"))
        # item = self.listWidget.item(4)
        # item.setText(_translate("Dialog", "Task 5"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.killBtn.setText(_translate("Dialog", "Kill"))
        self.closeBtn.setText(_translate("Dialog", "Close"))
        ############################################################
        for t in Controller.Tasks:
            item = MyQListWidgetItem(t, self.listWidget)
            if not t.isRemoveable():
                item.setBackground(QtGui.QBrush(QtCore.Qt.red, QtCore.Qt.SolidPattern))
            self.listWidget.addItem(item)
        self.killBtn.clicked.connect(self.onClickEntr)
        self.closeBtn.clicked.connect(self.onClickCancel)

    def onClickEntr(self):
        try:
            for i in self.listWidget.selectedItems():
                task = i.item
                if task.isRemoveable():
                    self.listWidget.takeItem(self.listWidget.row(i))
                    Controller.remFromTaskList(task)
                else:
                    raise Exception("This task cannot be killed.")
        except Exception as e:
            self.error = e.__str__()
            self.reject()

    def onClickCancel(self):
        if hasattr(self, 'error'):
            delattr(self, 'error')
        self.reject()


class ShowVehicles(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Dialog2")
        self.setFixedSize(400, 300)
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(50, 50, 291, 171))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 291, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        # item = QtWidgets.QListWidgetItem()
        # self.listWidget.addItem(item)
        # item = QtWidgets.QListWidgetItem()
        # self.listWidget.addItem(item)
        # item = QtWidgets.QListWidgetItem()
        # self.listWidget.addItem(item)
        # item = QtWidgets.QListWidgetItem()
        # self.listWidget.addItem(item)
        # item = QtWidgets.QListWidgetItem()
        # self.listWidget.addItem(item)
        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 1)
        self.deleteBtn = QtWidgets.QPushButton(self)
        self.deleteBtn.setGeometry(QtCore.QRect(110, 240, 75, 23))
        self.deleteBtn.setObjectName("deleteBtn")
        self.closeBtn = QtWidgets.QPushButton(self)
        self.closeBtn.setGeometry(QtCore.QRect(210, 240, 75, 23))
        self.closeBtn.setObjectName("closeBtn")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Vehicles"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        # item = self.listWidget.item(0)
        # item.setText(_translate("Dialog", "Vehicle 1"))
        # item = self.listWidget.item(1)
        # item.setText(_translate("Dialog", "Vehicle 2"))
        # item = self.listWidget.item(2)
        # item.setText(_translate("Dialog", "Vehicle 3"))
        # item = self.listWidget.item(3)
        # item.setText(_translate("Dialog", "Vehicle 4"))
        # item = self.listWidget.item(4)
        # item.setText(_translate("Dialog", "Vehicle 5"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.deleteBtn.setText(_translate("Dialog", "Delete"))
        self.closeBtn.setText(_translate("Dialog", "Close"))
        ############################################################
        self.deleteBtn.clicked.connect(self.onClickEntr)
        self.closeBtn.clicked.connect(self.onClickCancel)
        # try:
        for v in Controller.Vehicles:
            item = MyQListWidgetItem(v, self.listWidget)
            if not v.isRemoveable():
                item.setBackground(QtGui.QBrush(QtCore.Qt.red, QtCore.Qt.SolidPattern))
            self.listWidget.addItem(item)
        # except Exception as e:
        #     print(e)

    def onClickEntr(self):
        try:
            for i in self.listWidget.selectedItems():
                vehicle = i.item
                if vehicle.isRemoveable():
                    self.listWidget.takeItem(self.listWidget.row(i))
                    Controller.remFromVehicleList(vehicle)
                    if isinstance(vehicle, Controller.Drone):
                        self.droneRemoved = True
                else:
                    raise Exception("This vehicle cannot be removed.")
        except Exception as e:
            self.error = e.__str__()
            self.reject()

    def onClickCancel(self):
        if hasattr(self, 'error'):
            delattr(self, 'error')
        self.reject()
