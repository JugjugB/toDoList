from PyQt5 import QtCore, QtGui, QtWidgets
from design import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.addItem.clicked.connect(self.add_it)
        self.deleteItem.clicked.connect(self.delete_it)
        self.clear.clicked.connect(self.clear_list)

        self.show()
    
    def add_it(self):
        item = self.input.text()
        if item != "":
            self.list.addItem(item)
            self.input.setText("")

    def delete_it(self):
        current = self.list.currentRow()
        self.list.takeItem(current)

    def clear_list(self):
        self.list.clear()

app = QtWidgets.QApplication([])
mw = MainWindow()
app.exec_()