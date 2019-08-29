# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
import time
import Connection
import Controller
from AddAgent import AddAgent
from AddDrone import AddDrone
from AddTask import AddTask
from AddTask import AddTaskVisitCPoint
from AddTask import NumAgentsUi
from CreateMap import CreateMapUi
from EnterControlPoint import AddControlPoint
from Mapper2 import Mapper2
from Message import Message
from Obstacle import ObstacleUi
from Show import ShowTasks
from Show import ShowVehicles

HTML = """<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n
<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n
p, li { white-space: pre-wrap; }\n"
</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">08:00&gt; asduıahdıauısda</p>\n
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">08:10&gt; kasjodoıjaosıdas</p>\n
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">08:20&gt; ajsdıoasjdıoasjıd</p>\n
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">08:30&gt; skdoaskdoaskd</p>\n
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">08:40&gt; asdknasdjasıd</p>\n
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">08:50&gt; asjdıasjdıajsıoda</p>\n
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">09:00&gt; aosdjpasojdpasjpd</p>\n
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">09:10&gt; apskdoaskdoaksod</p>\n
<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">09:20&gt; aosdjkoaskdoaksd</p></body></html>"""


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.droneRadioBtn = QtWidgets.QRadioButton(self.centralwidget)
        self.droneRadioBtn.setObjectName("droneRadioBtn")
        self.horizontalLayout_5.addWidget(self.droneRadioBtn)
        self.agentRadioBtn = QtWidgets.QRadioButton(self.centralwidget)
        self.agentRadioBtn.setChecked(False)
        self.agentRadioBtn.setObjectName("agentRadioBtn")
        self.horizontalLayout_5.addWidget(self.agentRadioBtn)
        self.mapRadioBtn = QtWidgets.QRadioButton(self.centralwidget)
        self.mapRadioBtn.setObjectName("mapRadioBtn")
        self.horizontalLayout_5.addWidget(self.mapRadioBtn)
        self.commCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.commCheckBox.setChecked(True)
        self.commCheckBox.setObjectName("commCheckBox")
        self.horizontalLayout_5.addWidget(self.commCheckBox)
        self.horizontalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        ##############################################################
        self.graphicsView = Mapper2(self.centralwidget)
        ##############################################################
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_2.addWidget(self.graphicsView)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 101))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 780, 99))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menuBar.setDefaultUp(False)
        self.menuBar.setObjectName("menuBar")
        self.menuMenu = QtWidgets.QMenu(self.menuBar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuMap = QtWidgets.QMenu(self.menuMenu)
        self.menuMap.setObjectName("menuMap")
        self.menuEdit_Map = QtWidgets.QMenu(self.menuMap)
        self.menuEdit_Map.setObjectName("menuEdit_Map")
        self.menuTask_Manager_System = QtWidgets.QMenu(self.menuMenu)
        self.menuTask_Manager_System.setObjectName("menuTask_Manager_System")
        self.menuAdd_Agent = QtWidgets.QMenu(self.menuTask_Manager_System)
        self.menuAdd_Agent.setObjectName("menuAdd_Agent")
        self.menuAdd_Task = QtWidgets.QMenu(self.menuTask_Manager_System)
        self.menuAdd_Task.setObjectName("menuAdd_Task")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        self.menuTools = QtWidgets.QMenu(self.menuBar)
        self.menuTools.setObjectName("menuTools")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionCommunication_Box = QtWidgets.QAction(MainWindow)
        self.actionCommunication_Box.setObjectName("actionCommunication_Box")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionShow_Map = QtWidgets.QAction(MainWindow)
        self.actionShow_Map.setObjectName("actionShow_Map")
        self.actionCreate_Map = QtWidgets.QAction(MainWindow)
        self.actionCreate_Map.setObjectName("actionCreate_Map")
        self.actionAdd_ControlPoint = QtWidgets.QAction(MainWindow)
        self.actionAdd_ControlPoint.setObjectName("actionAdd_ControlPoint")
        self.actionShow_Tasks = QtWidgets.QAction(MainWindow)
        self.actionShow_Tasks.setObjectName("actionShow_Tasks")
        self.actionShow_Vehicles = QtWidgets.QAction(MainWindow)
        self.actionShow_Vehicles.setObjectName("actionShow_Vehicles")
        self.actionAsphalt_Paver = QtWidgets.QAction(MainWindow)
        self.actionAsphalt_Paver.setObjectName("actionAsphalt_Paver")
        self.actionBulldozer = QtWidgets.QAction(MainWindow)
        self.actionBulldozer.setObjectName("actionBulldozer")
        self.actionCompactor = QtWidgets.QAction(MainWindow)
        self.actionCompactor.setObjectName("actionCompactor")
        self.actionDrone = QtWidgets.QAction(MainWindow)
        self.actionDrone.setObjectName("actionDrone")
        self.actionExcavator = QtWidgets.QAction(MainWindow)
        self.actionExcavator.setObjectName("actionExcavator")
        self.actionTruck = QtWidgets.QAction(MainWindow)
        self.actionTruck.setObjectName("actionTruck")
        self.actionAdd_Obstacle = QtWidgets.QAction(MainWindow)
        self.actionAdd_Obstacle.setObjectName("actionAdd_Obstacle")
        self.actionDelete_Obstacle = QtWidgets.QAction(MainWindow)
        self.actionDelete_Obstacle.setObjectName("actionDelete_Obstacle")
        self.actionAdd_Obstacle_2 = QtWidgets.QAction(MainWindow)
        self.actionAdd_Obstacle_2.setObjectName("actionAdd_Obstacle_2")
        self.actionDelete_Obstacle_2 = QtWidgets.QAction(MainWindow)
        self.actionDelete_Obstacle_2.setObjectName("actionDelete_Obstacle_2")
        self.actionShow_Vehicles_2 = QtWidgets.QAction(MainWindow)
        self.actionShow_Vehicles_2.setObjectName("actionShow_Vehicles_2")
        self.actionShow_Tasks_2 = QtWidgets.QAction(MainWindow)
        self.actionShow_Tasks_2.setObjectName("actionShow_Tasks_2")
        self.actionSettings_2 = QtWidgets.QAction(MainWindow)
        self.actionSettings_2.setObjectName("actionSettings_2")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionVisit_the_Control_Point = QtWidgets.QAction(MainWindow)
        self.actionVisit_the_Control_Point.setObjectName("actionVisit_the_Control_Point")
        self.actionExcavation = QtWidgets.QAction(MainWindow)
        self.actionExcavation.setObjectName("actionExcavation")
        self.actionPit_Filling = QtWidgets.QAction(MainWindow)
        self.actionPit_Filling.setObjectName("actionPit_Filling")
        self.actionPouring_Asphalt = QtWidgets.QAction(MainWindow)
        self.actionPouring_Asphalt.setObjectName("actionPouring_Asphalt")
        self.menuEdit_Map.addSeparator()
        self.menuEdit_Map.addAction(self.actionAdd_Obstacle)
        self.menuEdit_Map.addAction(self.actionDelete_Obstacle)
        self.menuMap.addAction(self.actionCreate_Map)
        self.menuMap.addAction(self.menuEdit_Map.menuAction())
        self.menuMap.addAction(self.actionShow_Map)
        self.menuAdd_Agent.addAction(self.actionAsphalt_Paver)
        self.menuAdd_Agent.addAction(self.actionBulldozer)
        self.menuAdd_Agent.addAction(self.actionCompactor)
        self.menuAdd_Agent.addSeparator()
        self.menuAdd_Agent.addAction(self.actionDrone)
        self.menuAdd_Agent.addSeparator()
        self.menuAdd_Agent.addAction(self.actionExcavator)
        self.menuAdd_Agent.addAction(self.actionTruck)
        self.menuAdd_Task.addAction(self.actionVisit_the_Control_Point)
        self.menuAdd_Task.addSeparator()
        self.menuAdd_Task.addAction(self.actionExcavation)
        self.menuAdd_Task.addAction(self.actionPit_Filling)
        self.menuAdd_Task.addAction(self.actionPouring_Asphalt)
        self.menuTask_Manager_System.addAction(self.actionAdd_ControlPoint)
        self.menuTask_Manager_System.addSeparator()
        self.menuTask_Manager_System.addAction(self.menuAdd_Agent.menuAction())
        self.menuTask_Manager_System.addAction(self.menuAdd_Task.menuAction())
        self.menuTask_Manager_System.addSeparator()
        self.menuTask_Manager_System.addAction(self.actionShow_Vehicles)
        self.menuTask_Manager_System.addAction(self.actionShow_Tasks)
        self.menuMenu.addAction(self.menuTask_Manager_System.menuAction())
        self.menuMenu.addAction(self.menuMap.menuAction())
        self.menuMenu.addAction(self.actionSettings)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionAdd_Obstacle_2)
        self.menuEdit.addAction(self.actionDelete_Obstacle_2)
        self.menuView.addAction(self.actionShow_Vehicles_2)
        self.menuView.addAction(self.actionShow_Tasks_2)
        self.menuTools.addAction(self.actionSettings_2)
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuMenu.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuTools.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.droneRadioBtn.setText(_translate("MainWindow", "Drone"))
        self.agentRadioBtn.setText(_translate("MainWindow", "Agent"))
        self.mapRadioBtn.setText(_translate("MainWindow", "Map"))
        self.commCheckBox.setText(_translate("MainWindow", "Communication Box"))
        self.textBrowser.setHtml(_translate("MainWindow", ""))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuMap.setTitle(_translate("MainWindow", "Map"))
        self.menuEdit_Map.setTitle(_translate("MainWindow", "Edit Map"))
        self.menuTask_Manager_System.setTitle(_translate("MainWindow", "Task Manager System"))
        self.menuAdd_Agent.setTitle(_translate("MainWindow", "Add Agent"))
        self.menuAdd_Task.setTitle(_translate("MainWindow", "Add Task"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionCommunication_Box.setText(_translate("MainWindow", "Communication Box"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionShow_Map.setText(_translate("MainWindow", "Show Map"))
        self.actionCreate_Map.setText(_translate("MainWindow", "Create Map"))
        self.actionAdd_ControlPoint.setText(_translate("MainWindow", "Add ControlPoint"))
        self.actionShow_Tasks.setText(_translate("MainWindow", "Show Tasks"))
        self.actionShow_Vehicles.setText(_translate("MainWindow", "Show Vehicles"))
        self.actionAsphalt_Paver.setText(_translate("MainWindow", "Asphalt Paver"))
        self.actionBulldozer.setText(_translate("MainWindow", "Bulldozer"))
        self.actionCompactor.setText(_translate("MainWindow", "Compactor"))
        self.actionDrone.setText(_translate("MainWindow", "Drone"))
        self.actionExcavator.setText(_translate("MainWindow", "Excavator"))
        self.actionTruck.setText(_translate("MainWindow", "Truck"))
        self.actionAdd_Obstacle.setText(_translate("MainWindow", "Add Obstacle"))
        self.actionDelete_Obstacle.setText(_translate("MainWindow", "Delete Obstacle"))
        self.actionAdd_Obstacle_2.setText(_translate("MainWindow", "Add Obstacle"))
        self.actionDelete_Obstacle_2.setText(_translate("MainWindow", "Delete Obstacle"))
        self.actionShow_Vehicles_2.setText(_translate("MainWindow", "Show Vehicles"))
        self.actionShow_Tasks_2.setText(_translate("MainWindow", "Show Tasks"))
        self.actionSettings_2.setText(_translate("MainWindow", "Settings"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionVisit_the_Control_Point.setText(_translate("MainWindow", "Visiting Control Point"))
        self.actionExcavation.setText(_translate("MainWindow", "Excavation"))
        self.actionPit_Filling.setText(_translate("MainWindow", "Pit Filling"))
        self.actionPouring_Asphalt.setText(_translate("MainWindow", "Pouring Asphalt"))
        ######################### After Here Let There Be Code ################################
        self.actionAdd_ControlPoint.triggered.connect(self.addControlPoint)
        self.actionCreate_Map.triggered.connect(self.createMap)
        self.actionAsphalt_Paver.triggered.connect(self.addAsphaltPver)
        self.actionBulldozer.triggered.connect(self.addBulldozer)
        self.actionCompactor.triggered.connect(self.addCompactor)
        self.actionDrone.triggered.connect(self.addDrone)
        self.actionExcavator.triggered.connect(self.addExcavator)
        self.actionTruck.triggered.connect(self.addTruck)
        self.actionAdd_Obstacle.triggered.connect(self.addObstacle)
        self.actionDelete_Obstacle.triggered.connect(self.delObstacle)
        self.actionAdd_Obstacle_2.triggered.connect(self.addObstacle)
        self.actionDelete_Obstacle_2.triggered.connect(self.delObstacle)
        self.actionVisit_the_Control_Point.triggered.connect(self.visitControlPoint)
        self.actionExcavation.triggered.connect(self.excavation)
        self.actionPit_Filling.triggered.connect(self.pitFilling)
        self.actionPouring_Asphalt.triggered.connect(self.pouringAsphalt)
        self.actionShow_Tasks.triggered.connect(self.showTasks)
        self.actionShow_Tasks_2.triggered.connect(self.showTasks)
        self.actionShow_Vehicles.triggered.connect(self.showVehicles)
        self.actionShow_Vehicles_2.triggered.connect(self.showVehicles)
        self.commCheckBox.clicked.connect(self.checkboxUpdate)
        self.actionExit.triggered.connect(sys.exit)
        self.actionAbout.triggered.connect(lambda: self.graphicsView.my_timer.start(500))
        self.pushButton.clicked.connect(self.start)

    def createMap(self):
        uiCMap = CreateMapUi()
        if dial(uiCMap) == 1:
            self.dummyMap = uiCMap.map
            self.graphicsView.addMap(self.dummyMap.toJSON())
            Controller.Map = self.dummyMap
            self.dummyMap.yaz()
            ##################################
            Controller.ControlPoints = set()
            Controller.Vehicles = set()
            Controller.Tasks = set()
            if hasattr(self, 'drone'):
                delattr(self, 'drone')
            # self.top=Topic()

    def addControlPoint(self):
        if not hasattr(self, 'dummyMap'):
            msg = Message("Warning", "First create a map.")
            msg.show()
            msg.exec()
            return
        # while True:
        #     uiAddcp = Ui_Dialog(self.dummyMap)
        #     uiAddcp.show()
        #     result = uiAddcp.exec_()
        #     if result == 0 and hasattr(uiAddcp, "error"):
        #         msg = Message("Warning", uiAddcp.error)
        #         msg.show()
        #         msg.exec()
        #     elif result == 0:
        #         break
        #     else:
        #         #look here after other jobs done.
        #         break
        dial(AddControlPoint(self.dummyMap))

    def addAsphaltPver(self):
        if not hasattr(self, 'dummyMap'):
            msg = Message("Warning", "First create a map.")
            msg.show()
            msg.exec()
            return
        dial(AddAgent("Asphalt Paver", self.dummyMap))

    def addBulldozer(self):
        if not hasattr(self, 'dummyMap'):
            msg = Message("Warning", "First create a map.")
            msg.show()
            msg.exec()
            return
        dial(AddAgent("Bulldozer", self.dummyMap))

    def addCompactor(self):
        if not hasattr(self, 'dummyMap'):
            msg = Message("Warning", "First create a map.")
            msg.show()
            msg.exec()
            return
        dial(AddAgent("Compactor", self.dummyMap))

    def addDrone(self):
        if not hasattr(self, 'dummyMap'):
            msg = Message("Warning", "First create a map.")
            msg.show()
            msg.exec()
            return
        if hasattr(self, 'drone'):
            msg = Message("Warning", "There is already a drone exists.")
            msg.show()
            msg.exec()
            return
        addDrnUi = AddDrone(self.dummyMap)
        if dial(addDrnUi) == 1:
            self.drone = addDrnUi.drone

    def addExcavator(self):
        if not hasattr(self, 'dummyMap'):
            msg = Message("Warning", "First create a map.")
            msg.show()
            msg.exec()
            return
        dial(AddAgent("Excavator", self.dummyMap))

    def addTruck(self):
        if not hasattr(self, 'dummyMap'):
            msg = Message("Warning", "First create a map.")
            msg.show()
            msg.exec()
            return
        dial(AddAgent("Truck", self.dummyMap))

    def addObstacle(self):
        if not hasattr(self, 'dummyMap'):
            msg = Message("Warning", "First create a map.")
            msg.show()
            msg.exec()
            return
        dial(ObstacleUi(self.dummyMap, "Add Obstacle"))
        self.graphicsView.addMap(self.dummyMap.toJSON())
        self.dummyMap.yaz()
        toSend = []
        map = []
        map.append(self.dummyMap.sizeX)
        map.append(self.dummyMap.sizeY)
        toSend.append(map)
        toSend.append(self.dummyMap.toJSON())
        # self.top.send("UI2Task", toSend)

    def delObstacle(self):
        if not hasattr(self, 'dummyMap'):
            msg = Message("Warning", "First create a map.")
            msg.show()
            msg.exec()
            return
        dial(ObstacleUi(self.dummyMap, "Delete Obstacle"))
        self.graphicsView.addMap(self.dummyMap.toJSON())

    # Deprecated code
    # def createTask(self):
    #     if not hasattr(self, 'dummyMap'):
    #         msg = Message("Warning", "First create a map.")
    #         msg.show()
    #         msg.exec()
    #         return
    #     if not hasattr(self, 'drone'):
    #         msg = Message("Warning", "First create a drone.")
    #         msg.show()
    #         msg.exec()
    #         return
    #     if Controller.ControlPoints == set():
    #         msg = Message("Warning", "First create a Control Point.")
    #         msg.show()
    #         msg.exec()
    #         return
    #     while True:
    #         tskChooser = TaskTypeChooser()
    #         tskChooser.show()
    #         result = tskChooser.exec_()
    #         if result == 1:
    #             #print(tskChooser.taskType)
    #             break
    #
    #     if tskChooser.taskType == "Visiting Control Point":
    #         uiAddTsk = AddTaskVisitCPoint(self.dummyMap)
    #     else:
    #         uiAddTsk = AddTask(self.dummyMap, tskChooser.taskType)
    #     dial(uiAddTsk)
    #
    #     #task added

    def visitControlPoint(self):
        if not hasattr(self, 'dummyMap'):
            msg = Message("Warning", "First create a map.")
            msg.show()
            msg.exec()
            return
        if not hasattr(self, 'drone'):
            msg = Message("Warning", "First create a drone.")
            msg.show()
            msg.exec()
            return
        if Controller.ControlPoints == set():
            msg = Message("Warning", "First create a Control Point.")
            msg.show()
            msg.exec()
            return
        addTskVisitCp = AddTaskVisitCPoint(self.dummyMap)
        if dial(addTskVisitCp) == 1:
            # Controller.addToTaskList(addTskVisitCp.task)
            print(addTskVisitCp.task.toJSON())

    def excavation(self):
        if not hasattr(self, 'dummyMap'):
            msg = Message("Warning", "First create a map.")
            msg.show()
            msg.exec()
            return
        if not hasattr(self, 'drone'):
            msg = Message("Warning", "First create a drone.")
            msg.show()
            msg.exec()
            return
        if Controller.ControlPoints == set():
            msg = Message("Warning", "First create a Control Point.")
            msg.show()
            msg.exec()
            return
        addTskUi = AddTask(self.dummyMap, "Excavation")
        if dial(addTskUi) == 1:
            dial(NumAgentsUi(addTskUi.task))

    def pitFilling(self):
        if not hasattr(self, 'dummyMap'):
            msg = Message("Warning", "First create a map.")
            msg.show()
            msg.exec()
            return
        if not hasattr(self, 'drone'):
            msg = Message("Warning", "First create a drone.")
            msg.show()
            msg.exec()
            return
        if Controller.ControlPoints == set():
            msg = Message("Warning", "First create a Control Point.")
            msg.show()
            msg.exec()
            return
        addTskUi = AddTask(self.dummyMap, "Pit Filling")
        if dial(addTskUi) == 1:
            dial(NumAgentsUi(addTskUi.task))

    def pouringAsphalt(self):
        if not hasattr(self, 'dummyMap'):
            msg = Message("Warning", "First create a map.")
            msg.show()
            msg.exec()
            return
        if not hasattr(self, 'drone'):
            msg = Message("Warning", "First create a drone.")
            msg.show()
            msg.exec()
            return
        if Controller.ControlPoints == set():
            msg = Message("Warning", "First create a Control Point.")
            msg.show()
            msg.exec()
            return
        addTskUi = AddTask(self.dummyMap, "Pouring Asphalt")
        if dial(addTskUi) == 1:
            dial(NumAgentsUi(addTskUi.task))

    def showTasks(self):
        dial(ShowTasks())

    def showVehicles(self):
        shwVec = ShowVehicles()
        dial(shwVec)
        if hasattr(shwVec, 'droneRemoved') and shwVec.droneRemoved == True:
            delattr(self, 'drone')

    def checkboxUpdate(self):
        self.scrollArea.setVisible(self.commCheckBox.isChecked())

    def start(self):
        try:
            conn = Connection.UI2Task()
            conn.register_as_publisher()
            conn.register_as_subscriber()
            conn.Publish(self.dummyMap, Controller.Vehicles, Controller.Tasks, Controller.ControlPoints)
            time.sleep(1)
            conn2 = Connection.UI2Drone()
            conn2.Publish(self.dummyMap, self.drone)
            time.sleep(1)
            conn3 = Connection.UI2MA()
            conn3.Publish(self.dummyMap)
            #After here data will be received
            self.com = Connection.Listener(self.textBrowser, self.graphicsView)
            self.com.start()
            # self.com = Connection.Task2UI(self.textBrowser)
            # self.com.start()
            # self.com2 = Connection.Drone2UI(self.scrollArea)
            # self.com2.start()
            # self.com3 = Connection.MA2UI(self.scrollArea)
            # self.com3.start()
        except Exception as e:
            print(e)



def dial(dialog):
    while True:
        dialog.show()
        result = dialog.exec_()
        if result == 0 and hasattr(dialog, "error"):
            msg = Message("Warning", dialog.error)
            msg.show()
            msg.exec()
            delattr(dialog, 'error')
        else:
            break
    return result


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
    ui.com.stop()
    sys.exit()
