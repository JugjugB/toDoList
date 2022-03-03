from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from design import Ui_MainWindow
import sqlite3

# Connect to SQLite3 Database
conn = sqlite3.connect('todoitems.db')
c = conn.cursor()

c.execute("""CREATE TABLE if not exists items (
        item text
        )""")

conn.commit()
conn.close()

# Create MainWindow (UI comes from design.py file)
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("To-Do List")
        self.addItem.clicked.connect(self.add_it)
        self.deleteItem.clicked.connect(self.delete_it)
        self.clear.clicked.connect(self.clear_list)
        self.save.clicked.connect(self.save_list)

        # Load items from database
        conn = sqlite3.connect('todoitems.db')
        c = conn.cursor()  

        c.execute("SELECT * FROM items")
        items = c.fetchall()
        for i in items:
            self.list.addItem(str(i[0]))
        
        conn.commit()
        conn.close()

        self.show()
    
    # Adds item when enter/return is pressed
    def keyPressEvent(self, event):
       if event.key() == QtCore.Qt.Key_Return:
           self.add_it()

    # Saves list to database
    def save_list(self):
        conn = sqlite3.connect('todoitems.db')
        c = conn.cursor() 
        c.execute("DELETE FROM items;")

        items = []
        for i in range(self.list.count()):
            items.append(self.list.item(i))
            c.execute("INSERT INTO items VALUES (:item)", 
            {
                'item': self.list.item(i).text()
            })

        conn.commit()
        conn.close()       

        # Creates pop-up message when items are saved
        msg = QMessageBox()
        msg.setWindowTitle("Saved to Database!")
        msg.setText("Your To-Do List Has Been Saved!") 
        x = msg.exec()
    
    # Function to add item in input box
    def add_it(self):
        item = self.input.text()
        if item != "":
            self.list.addItem(item)
            self.input.setText("")
    
    # Deletes selected row
    def delete_it(self):
        current = self.list.currentRow()
        self.list.takeItem(current)

    # Clears list
    def clear_list(self):
        self.list.clear()




app = QtWidgets.QApplication([])
mw = MainWindow()
app.exec_()
conn.close()