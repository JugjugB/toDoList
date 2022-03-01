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

app = QtWidgets.QApplication([])
mw = MainWindow()
app.exec_()