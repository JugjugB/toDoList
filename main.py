from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QVBoxLayout, QHBoxLayout 
from uiDesigns.design import Ui_MainWindow as mainui
from uiDesigns.logodesign import Ui_MainWindow as logoui
from uiDesigns.createaccountdesign import Ui_MainWindow as createui
import sqlite3
import sys

# Connect to SQLite3 Database
conn = sqlite3.connect('databases/todoitems.db') # database for list items
c = conn.cursor()

c.execute("""CREATE TABLE if not exists items (
        item text
        )""")

conn.commit()
conn.close()

conn2 = sqlite3.connect('databases/accountdetails.db') # database for account usernames/passwords
c2 = conn2.cursor()

c2.execute("""CREATE TABLE if not exists accounts (
        username text,
        password text
        )""")

conn2.commit()
conn2.close()

# Create MainWindow (UI comes from design.py file)
class MainWindow(QtWidgets.QMainWindow, mainui):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("To-Do List")
        self.w = None

        # Set layouts (for window scaling)
        mainlayout = QVBoxLayout()
        mainlayout.addWidget(self.input)
        buttonslayout = QHBoxLayout()
        buttonslayout.addWidget(self.deleteItem)
        buttonslayout.addWidget(self.addItem)
        buttonslayout.addWidget(self.clear)
        buttonslayout.addWidget(self.save)
        mainlayout.addLayout(buttonslayout)
        mainlayout.addWidget(self.list)
        self.centralwidget.setLayout(mainlayout)

        # Attach functions to buttons
        self.addItem.clicked.connect(self.add_it)
        self.deleteItem.clicked.connect(self.delete_it)
        self.clear.clicked.connect(self.clear_list)
        self.save.clicked.connect(self.save_list)

        # Load items from database
        conn = sqlite3.connect('databases/todoitems.db')
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
        conn = sqlite3.connect('databases/todoitems.db')
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
        if item != "" and item.isspace() != True:
            self.list.addItem(item)
            self.input.setText("")
    
    # Deletes selected row
    def delete_it(self):
        current = self.list.currentRow()
        self.list.takeItem(current)

    # Clears list
    def clear_list(self):
        self.list.clear()

# Window for creating new accounts
class CreateWindow(QtWidgets.QMainWindow, createui):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle('Create an Account')
        self.createButton.clicked.connect(self.submitAccount)
        self.returnButton.clicked.connect(self.returnLogin)
        self.show()

    # submits new account to database
    def submitAccount(self):
        self.usernameErrorLabel.setText("")
        self.passwordErrorLabel.setText("")
        username = None
        password = None

        if self.usernameInput.text() != "" and self.usernameInput.text().isspace() != True:
            username = self.usernameInput.text()
        else: 
            self.usernameErrorLabel.setText("Invalid username")
            self.usernameInput.setText("")

        if self.passwordInput.text() != "" and self.passwordInput.text().isspace() != True:
            password = self.passwordInput.text()
        else: 
            self.passwordErrorLabel.setText("Invalid password")
            self.passwordInput.setText("")

        if username != None and password != None:
            conn2 = sqlite3.connect('databases/accountdetails.db')
            c2 = conn2.cursor()  
            c2.execute("INSERT INTO accounts VALUES (?,?)", (username, password))
            conn2.commit()
            conn2.close()

            msg = QMessageBox()
            msg.setWindowTitle("Account Created!")
            msg.setText("Account created successfully!") 
            x = msg.exec()
        
        self.usernameInput.setText("")
        self.passwordInput.setText("")

    # returns user to login window
    def returnLogin(self):
        self.lw = LoginWindow()
        self.lw.show()
        self.close()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            self.submitAccount()

# Add a login window at startup
class LoginWindow(QtWidgets.QMainWindow, logoui):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle('Login')
        self.mw = None
        self.loginButton.clicked.connect(self.verifyAccount)
        self.createaccountButton.clicked.connect(self.createAccount)
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.show()

    # validates username/password
    def verifyAccount(self):
        conn2 = sqlite3.connect('databases/accountdetails.db')
        c2 = conn2.cursor()  
        c2.execute("SELECT * FROM accounts")
        accounts = c2.fetchall()
        conn2.commit()
        conn2.close()

        username = str(self.usernameInput.text())
        password = str(self.passwordInput.text())

        valid = False

        for i in accounts:
            if username == i[0] and password == i[1]:
                self.showMain() # show main window if account is validated
                valid = True
            
        if valid is False: 
            msg = QMessageBox()
            msg.setWindowTitle('Login failed')
            msg.setText('Login failed.  Invalid username/password.')
            msg.exec()
            self.usernameInput.setText("")
            self.passwordInput.setText("")

    # creates CreateWindow for new accounts
    def createAccount(self):
        self.cw = CreateWindow()
        self.cw.show()
        self.close()

    # shows main window
    def showMain(self):
        self.mw = MainWindow()
        self.mw.show()
        self.close()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            self.verifyAccount()

app = QtWidgets.QApplication(sys.argv)
w = LoginWindow()
w.show()
app.exec()