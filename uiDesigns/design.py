# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(525, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.deleteItem = QtWidgets.QPushButton(self.centralwidget)
        self.deleteItem.setGeometry(QtCore.QRect(120, 47, 110, 25))
        self.deleteItem.setObjectName("deleteItem")
        self.addItem = QtWidgets.QPushButton(self.centralwidget)
        self.addItem.setGeometry(QtCore.QRect(10, 47, 110, 25))
        self.addItem.setObjectName("addItem")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(230, 47, 110, 25))
        self.clear.setObjectName("clear")
        self.input = QtWidgets.QLineEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(10, 10, 505, 31))
        self.input.setText("")
        self.input.setObjectName("input")
        self.list = QtWidgets.QListWidget(self.centralwidget)
        self.list.setGeometry(QtCore.QRect(10, 80, 505, 391))
        self.list.setObjectName("list")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(340, 47, 90, 24))
        self.save.setObjectName("save")
        self.returnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.returnLogin.setGeometry(QtCore.QRect(430, 47, 85, 24))
        self.returnLogin.setObjectName("returnLogin")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.deleteItem.setText(_translate("MainWindow", "Delete Item"))
        self.addItem.setText(_translate("MainWindow", "Add Item"))
        self.clear.setText(_translate("MainWindow", "Clear List"))
        self.save.setText(_translate("MainWindow", "Save List"))
        self.returnLogin.setText(_translate("MainWindow", "Logout"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
