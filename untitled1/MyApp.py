from __future__ import division
import sys
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QApplication
from PyQt5.uic.properties import QtWidgets
import Ui_MainWindow

Form, Window = uic.loadUiType("tax_calc.ui")


class MyApp(object):


    def setupUi(self, MainWindow):
        MainWindow.resize(764, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.price_box = QtWidgets.QTextEdit(self.centralwidget)
        self.price_box.setGeometry(QtCore.QRect(220, 140, 104, 64))
        self.price_box.setObjectName("price_box")
        self.Taxbox = QtWidgets.QLabel(self.centralwidget)
        self.Taxbox.setGeometry(QtCore.QRect(100, 170, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Taxbox.setFont(font)
        self.Taxbox.setObjectName("Taxbox")
        self.tax_rate = QtWidgets.QSpinBox(self.centralwidget)
        self.tax_rate.setGeometry(QtCore.QRect(240, 260, 61, 31))
        self.tax_rate.setProperty("value", 20)
        self.tax_rate.setObjectName("tax_rate")
        self.calc_tax_button = QtWidgets.QPushButton(self.centralwidget)
        self.calc_tax_button.setGeometry(QtCore.QRect(160, 350, 131, 41))
        self.calc_tax_button.setObjectName("calc_tax_button")
        self.TaxRate = QtWidgets.QLabel(self.centralwidget)
        self.TaxRate.setGeometry(QtCore.QRect(100, 270, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TaxRate.setFont(font)
        self.TaxRate.setObjectName("TaxRate")
        self.results_window = QtWidgets.QTextEdit(self.centralwidget)
        self.results_window.setGeometry(QtCore.QRect(170, 430, 104, 64))
        self.results_window.setObjectName("results_window")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 50, 361, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setLineWidth(5)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 764, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Taxbox.setText(_translate("MainWindow", "Price"))
        self.calc_tax_button.setText(_translate("MainWindow", "Calculate Tax"))
        self.TaxRate.setText(_translate("MainWindow", "Tax Rate"))
        self.label.setText(_translate("MainWindow", "Sales Tax Calculator"))

    def __init__(self):

        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.calc_tax_button.clicked.connect(self.CalculateTax)

    def CalculateTax(self):
        price = int(self.price_box.toPlainText())
        tax = (self.tax_rate.value())
        total_price = price + ((tax / 100) * price)
        total_price_string = "The total price with tax is: " + str(total_price)
        self.results_window.setText(total_price_string)


if __name__ == "__main__":
    app =QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())