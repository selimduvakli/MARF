# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

import Controller


class TaskTypeChooser(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("tchooser")
        self.setFixedSize(292, 213)
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.comboBoxType = QtWidgets.QComboBox(self)
        self.comboBoxType.setObjectName("comboBoxType")
        self.comboBoxType.addItem("")
        self.comboBoxType.addItem("")
        self.comboBoxType.addItem("")
        self.comboBoxType.addItem("")
        self.gridLayout.addWidget(self.comboBoxType, 3, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 2)
        self.enterBtn = QtWidgets.QPushButton(self)
        self.enterBtn.setObjectName("enterBtn")
        self.gridLayout_2.addWidget(self.enterBtn, 2, 0, 1, 1)
        self.cancelBtn = QtWidgets.QPushButton(self)
        self.cancelBtn.setObjectName("cancelBtn")
        self.gridLayout_2.addWidget(self.cancelBtn, 2, 1, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Task Type"))
        self.label.setText(_translate("Dialog", "Please Choose a Task Type:"))
        self.comboBoxType.setItemText(0, _translate("Dialog", "Visiting the Control Point"))
        self.comboBoxType.setItemText(1, _translate("Dialog", "Excavation"))
        self.comboBoxType.setItemText(2, _translate("Dialog", "Pouring Asphalt"))
        self.comboBoxType.setItemText(3, _translate("Dialog", "Pit Filling"))
        self.enterBtn.setText(_translate("Dialog", "Enter"))
        self.cancelBtn.setText(_translate("Dialog", "Cancel"))
        ############################################################
        self.enterBtn.clicked.connect(self.onClickEntr)
        self.cancelBtn.clicked.connect(self.reject)

    def onClickEntr(self):
        if self.comboBoxType.currentIndex() == 0:
            self.taskType = "Visiting Control Point"
        elif self.comboBoxType.currentIndex() == 1:
            self.taskType = "Excavation"
        elif self.comboBoxType.currentIndex() == 2:
            self.taskType = "Pouring Asphalt"
        elif self.comboBoxType.currentIndex() == 3:
            self.taskType = "Pit Filling"
        self.accept()


class AddTask(QtWidgets.QDialog):
    def __init__(self, map, taskType):
        super().__init__()
        self.map = map
        self.taskType = taskType
        self.setupUi()

    def setupUi(self):
        self.setObjectName("tskcreator")
        self.setFixedSize(400, 300)
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(50, 50, 291, 171))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 292, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.editX = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.editX.setObjectName("editX")
        self.gridLayout.addWidget(self.editX, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.editY = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.editY.setObjectName("editY")
        self.gridLayout.addWidget(self.editY, 2, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioLow = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioLow.setChecked(True)
        self.radioLow.setObjectName("radioLow")
        self.horizontalLayout.addWidget(self.radioLow)
        self.radioMedium = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioMedium.setObjectName("radioMedium")
        self.horizontalLayout.addWidget(self.radioMedium)
        self.radioHigh = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioHigh.setObjectName("radioHigh")
        self.horizontalLayout.addWidget(self.radioHigh)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 2)
        self.editControlPoint = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.editControlPoint.setObjectName("editControlPoint")
        self.gridLayout.addWidget(self.editControlPoint, 3, 1, 1, 1)
        self.timeEditStart = QtWidgets.QTimeEdit(self.gridLayoutWidget)
        self.timeEditStart.setMaximumDate(QtCore.QDate(2040, 1, 1))
        self.timeEditStart.setMinimumDate(QtCore.QDate(2019, 1, 1))
        self.timeEditStart.setObjectName("timeEditStart")
        self.gridLayout.addWidget(self.timeEditStart, 4, 1, 1, 1)
        self.timeEditFinish = QtWidgets.QTimeEdit(self.gridLayoutWidget)
        self.timeEditFinish.setObjectName("timeEditFinish")
        self.gridLayout.addWidget(self.timeEditFinish, 4, 2, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.dateEdit.setMinimumDate(QtCore.QDate(2019, 1, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 5, 1, 1, 1)
        self.editName = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.editName.setObjectName("editName")
        self.gridLayout.addWidget(self.editName, 0, 1, 1, 2)
        self.checkBoxRept = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBoxRept.setText("")
        self.checkBoxRept.setChecked(True)
        self.checkBoxRept.setObjectName("checkBoxRept")
        self.gridLayout.addWidget(self.checkBoxRept, 6, 1, 1, 1)
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
        self.setWindowTitle(_translate("Dialog", "Add Task"))
        self.label_2.setText(_translate("Dialog", " Priority:"))
        self.label_3.setText(_translate("Dialog", " Target Point:"))
        self.label.setText(_translate("Dialog", " Task Name:"))
        self.label_5.setText(_translate("Dialog", " Time Period:"))
        self.label_4.setText(_translate("Dialog", " Control Point:"))
        self.label_6.setText(_translate("Dialog", " Deadline:"))
        self.label_7.setText(_translate("Dialog", " Is Repeatable:"))
        self.radioLow.setText(_translate("Dialog", "Low"))
        self.radioMedium.setText(_translate("Dialog", "Medium"))
        self.radioHigh.setText(_translate("Dialog", "High"))
        self.enterBtn.setText(_translate("Dialog", "Enter"))
        self.cancelBtn.setText(_translate("Dialog", "Cancel"))
        ###############################################################
        self.onlyInt = QtGui.QIntValidator(0, 100)
        self.editX.setValidator(self.onlyInt)
        self.editY.setValidator(self.onlyInt)
        self.enterBtn.clicked.connect(self.onClickEntr)
        self.cancelBtn.clicked.connect(self.onClickCancel)
        self.checkBoxRept.clicked.connect(lambda: self.dateEdit.setEnabled(self.checkBoxRept.isChecked()))

    def onClickEntr(self):
        try:
            name = self.editName.text()
            for t in Controller.Tasks:
                if name == t.name:
                    raise Exception("This task name already given to another task.")
            if self.radioLow.isChecked():
                priority = 'Low'
            elif self.radioMedium.isChecked():
                priority = 'Medium'
            elif self.radioHigh.isChecked():
                priority = 'High'
            targetPoint = Controller.Point(self.map, int(self.editX.text()), int(self.editY.text()))
            for obs in self.map.Obstacles:
                if obs.positionX == targetPoint.positionX and obs.positionY == targetPoint.positionY:
                    raise Exception("There is a obstacle in target point")
            controlPoint = Controller.returnPointByName(self.editControlPoint.text())
            startTime = self.timeEditStart.time().toPyTime()
            finishTime = self.timeEditFinish.time().toPyTime()
            if startTime.__str__() == finishTime.__str__():
                raise Exception("Starting and Ending times can not be same.")
            # elif (startTime.hour * 60 + startTime.minute) > (finishTime.hour * 60 + startTime.minute):
            elif startTime > finishTime:
                raise Exception("Ending time can't come before Starting time.")
            if self.checkBoxRept.isChecked():
                deadline = self.dateEdit.date().toPyDate()
                self.task = Controller.RepeatableTask(name, self.taskType, priority, targetPoint, controlPoint,
                                                      startTime, finishTime, deadline)
            else:
                self.task = Controller.NonRepeatableTask(name, self.taskType, priority, targetPoint, controlPoint,
                                                         startTime, finishTime)
            self.accept()
        except Exception as e:
            self.error = e.__str__()
            print(e)
            self.reject()

    def onClickCancel(self):
        if hasattr(self, 'error'):
            delattr(self, 'error')
        self.reject()


class AddTaskVisitCPoint(QtWidgets.QDialog):
    def __init__(self, map):
        super().__init__()
        self.map = map
        self.setupUi()

    def setupUi(self):
        self.setObjectName("tskcreator2")
        self.setFixedSize(400, 300)
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(50, 50, 291, 171))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 292, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioLow = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioLow.setChecked(True)
        self.radioLow.setObjectName("radioLow")
        self.horizontalLayout.addWidget(self.radioLow)
        self.radioMedium = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioMedium.setObjectName("radioMedium")
        self.horizontalLayout.addWidget(self.radioMedium)
        self.radioHigh = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioHigh.setObjectName("radioHigh")
        self.horizontalLayout.addWidget(self.radioHigh)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.editName = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.editName.setObjectName("editName")
        self.gridLayout.addWidget(self.editName, 0, 1, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.editControlPoint = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.editControlPoint.setObjectName("editControlPoint")
        self.gridLayout.addWidget(self.editControlPoint, 2, 1, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.dateEdit.setMinimumDate(QtCore.QDate(2019, 1, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 4, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.timeEditStart = QtWidgets.QTimeEdit(self.gridLayoutWidget)
        self.timeEditStart.setObjectName("timeEditStart")
        self.horizontalLayout_2.addWidget(self.timeEditStart)
        self.timeEditFinish = QtWidgets.QTimeEdit(self.gridLayoutWidget)
        self.timeEditFinish.setMaximumDate(QtCore.QDate(2040, 1, 1))
        self.timeEditFinish.setMinimumDate(QtCore.QDate(2019, 1, 1))
        self.timeEditFinish.setObjectName("timeEditFinish")
        self.horizontalLayout_2.addWidget(self.timeEditFinish)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 1, 1, 1)
        self.checkBoxRept = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBoxRept.setText("")
        self.checkBoxRept.setChecked(True)
        self.checkBoxRept.setObjectName("checkBoxRept")
        self.gridLayout.addWidget(self.checkBoxRept, 5, 1, 1, 1)
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
        self.setWindowTitle(_translate("Dialog", "Add Task"))
        self.label_2.setText(_translate("Dialog", " Priority:"))
        self.radioLow.setText(_translate("Dialog", "Low"))
        self.radioMedium.setText(_translate("Dialog", "Medium"))
        self.radioHigh.setText(_translate("Dialog", "High"))
        self.label.setText(_translate("Dialog", " Task Name:"))
        self.label_5.setText(_translate("Dialog", " Time Period:"))
        self.label_4.setText(_translate("Dialog", " Control Point:"))
        self.label_6.setText(_translate("Dialog", " Deadline:"))
        self.label_7.setText(_translate("Dialog", " Is Repeatable:"))
        self.enterBtn.setText(_translate("Dialog", "Enter"))
        self.cancelBtn.setText(_translate("Dialog", "Cancel"))
        ###############################################################
        self.enterBtn.clicked.connect(self.onClickEntr)
        self.cancelBtn.clicked.connect(self.onClickCancel)
        self.checkBoxRept.clicked.connect(lambda: self.dateEdit.setEnabled(self.checkBoxRept.isChecked()))

    def onClickEntr(self):
        try:
            name = self.editName.text()
            for t in Controller.Tasks:
                if name == t.name:
                    raise Exception("This task name already given to another task.")
            if self.radioLow.isChecked():
                priority = 'Low'
            elif self.radioMedium.isChecked():
                priority = 'Medium'
            elif self.radioHigh.isChecked():
                priority = 'High'
            controlPoint = Controller.returnPointByName(self.editControlPoint.text())
            startTime = self.timeEditStart.time().toPyTime()
            finishTime = self.timeEditFinish.time().toPyTime()
            if startTime.__str__() == finishTime.__str__():
                raise Exception("Starting and Ending times can not be same.")
            # todo cont from here
            # elif (startTime.hour * 60 + startTime.minute) > (finishTime.hour * 60 + startTime.minute) :
            elif startTime > finishTime:
                raise Exception("Ending time can't come before Starting time.")
            if self.checkBoxRept.isChecked():
                deadline = self.dateEdit.date().toPyDate()
                self.task = Controller.RepeatableTaskVisitCP(name, priority, controlPoint, startTime, finishTime,
                                                             deadline)
            else:
                self.task = Controller.NonRepeatableTaskVisitCP(name, priority, controlPoint, startTime, finishTime)
            vehicles = {
                "Asphalt Paver": 0,
                "Bulldozer": 0,
                "Compactor": 0,
                "Excavator": 0,
                "Truck": 0,
                "Drone": 1
            }
            self.task.addVehiclesToTask(vehicles)
            Controller.addToTaskList(self.task)
            self.accept()
        except Exception as e:
            self.error = e.__str__()
            self.reject()

    def onClickCancel(self):
        if hasattr(self, 'error'):
            delattr(self, 'error')
        self.reject()


class NumAgentsUi(QtWidgets.QDialog):
    def __init__(self, task):
        super().__init__()
        self.task = task
        self.setupUi()

    def setupUi(self):
        self.setObjectName("numagnt")
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
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.spinBoxAsphaltPaver = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBoxAsphaltPaver.setMaximum(10)
        self.spinBoxAsphaltPaver.setObjectName("spinBoxAsphaltPaver")
        self.gridLayout.addWidget(self.spinBoxAsphaltPaver, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.spinBoxBulldozer = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBoxBulldozer.setMaximum(10)
        self.spinBoxBulldozer.setObjectName("spinBoxBulldozer")
        self.gridLayout.addWidget(self.spinBoxBulldozer, 1, 1, 1, 1)
        self.spinBoxCompactor = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBoxCompactor.setMaximum(10)
        self.spinBoxCompactor.setObjectName("spinBoxCompactor")
        self.gridLayout.addWidget(self.spinBoxCompactor, 2, 1, 1, 1)
        self.spinBoxExcavator = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBoxExcavator.setMaximum(10)
        self.spinBoxExcavator.setObjectName("spinBoxExcavator")
        self.gridLayout.addWidget(self.spinBoxExcavator, 3, 1, 1, 1)
        self.spinBoxTruck = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBoxTruck.setMaximum(10)
        self.spinBoxTruck.setObjectName("spinBoxTruck")
        self.gridLayout.addWidget(self.spinBoxTruck, 4, 1, 1, 1)
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
        self.setWindowTitle(_translate("Dialog", "Number of Agents"))
        self.label.setText(_translate("Dialog", " Asphalt Paver:"))
        self.label_5.setText(_translate("Dialog", " Truck:"))
        self.label_4.setText(_translate("Dialog", " Excavator:"))
        self.label_3.setText(_translate("Dialog", " Compactor:"))
        self.label_2.setText(_translate("Dialog", " Bulldozer:"))
        self.enterBtn.setText(_translate("Dialog", "Enter"))
        self.cancelBtn.setText(_translate("Dialog", "Cancel"))
        #############################################################
        self.spinBoxAsphaltPaver.setEnabled(False)
        self.spinBoxBulldozer.setEnabled(False)
        self.spinBoxCompactor.setEnabled(False)
        self.spinBoxExcavator.setEnabled(False)
        self.spinBoxExcavator.setEnabled(False)
        self.spinBoxTruck.setEnabled(False)
        if self.task.type == "Excavation":
            self.spinBoxExcavator.setEnabled(True)
        elif self.task.type == "Pit Filling":
            self.spinBoxBulldozer.setEnabled(True)
            self.spinBoxTruck.setEnabled(True)
        elif self.task.type == "Pouring Asphalt":
            self.spinBoxAsphaltPaver.setEnabled(True)
            self.spinBoxCompactor.setEnabled(True)
        self.spinBoxAsphaltPaver.setMaximum(Controller.NumberOfAsphaltPaver())
        self.spinBoxBulldozer.setMaximum(Controller.NumberOfBulldozer())
        self.spinBoxCompactor.setMaximum(Controller.NumberOfCompactor())
        self.spinBoxExcavator.setMaximum(Controller.NumberOfExcavator())
        self.spinBoxTruck.setMaximum(Controller.NumberOfTruck())
        self.enterBtn.clicked.connect(self.onClickEntr)
        self.cancelBtn.clicked.connect(self.onClickCancel)

    def onClickEntr(self):
        if self.task.type == "Excavation" and self.spinBoxExcavator.value() == 0:
            self.error = "Not enough vehicle allocated to the task"
            self.reject()
        elif self.task.type == "Pit Filling" and (self.spinBoxBulldozer.value() <= 0 or self.spinBoxTruck.value() <= 0):
            self.error = "Not enough vehicle allocated to the task"
            self.reject()
        elif self.task.type == "Pouring Asphalt" and (
                self.spinBoxAsphaltPaver.value() <= 0 or self.spinBoxCompactor.value() <= 0):
            self.error = "Not enough vehicle allocated to the task"
            self.reject()
        else:
            vehicles = {
                "Asphalt Paver": self.spinBoxAsphaltPaver.value(),
                "Bulldozer": self.spinBoxBulldozer.value(),
                "Compactor": self.spinBoxCompactor.value(),
                "Excavator": self.spinBoxExcavator.value(),
                "Truck": self.spinBoxTruck.value()
            }
            self.task.addVehiclesToTask(vehicles)
            Controller.addToTaskList(self.task)
            print(self.task.toJSON())
            # print(self.task.vehicles.__str__())
            self.accept()

    def onClickCancel(self):
        if hasattr(self, 'error'):
            delattr(self, 'error')
        self.reject()
