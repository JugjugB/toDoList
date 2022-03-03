from PyQt5 import QtCore, QtGui, QtWidgets
from design import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("To-Do List")
        self.addItem.clicked.connect(self.add_it)
        self.deleteItem.clicked.connect(self.delete_it)
        self.clear.clicked.connect(self.clear_list)
        self.save.clicked.connect(self.save_list)
        self.show()
    
    def keyPressEvent(self, event):
       if event.key() == QtCore.Qt.Key_Return:
           self.add_it()

    def save_list(self):
        items = []
        for i in range(self.list.count()):
            items.append(self.list.item(i))

        for item in items:
            print(item.text())

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