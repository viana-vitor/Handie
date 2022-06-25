
import sys
import re

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QDialogButtonBox, QMainWindow, QLineEdit, QPushButton, QToolBar, QWidget
from PySide6.QtSql import QSqlDatabase, QSqlQueryModel, QSqlTableModel, QSqlQuery

from Ui_MainWindow import Ui_MainWindow
from CustomerProject import Ui_MainWindow as CustomerWindow

class MainWindowOne(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.hide)

        toolbar = QToolBar()
        toolbar.setIconSize(QSize(30, 30))
        toolbar.setStyleSheet("QToolBar{spacing: 15px;}")
        toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.addToolBar(Qt.LeftToolBarArea, toolbar)

        self.button_home = QAction(QIcon("home (2).png"), "Home", self)
        #button_home.setStatusTip("Home")
        self.button_home.setCheckable(True)
        toolbar.addAction(self.button_home)

        self.button_customer = QAction(QIcon("contact.png"), "Customers", self)
        self.button_customer.setCheckable(True)
        #button_customer.triggered.connect(self.CustomerTable)
        toolbar.addAction(self.button_customer)

        self.button_customer.triggered.connect(self.hide)




class MainWindowTwo(QMainWindow, CustomerWindow ):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.hide)

        toolbar = QToolBar()
        toolbar.setIconSize(QSize(30, 30))
        toolbar.setStyleSheet("QToolBar{spacing: 15px;}")
        toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.addToolBar(Qt.LeftToolBarArea, toolbar)

        self.button_home = QAction(QIcon("home (2).png"), "Home", self)
        #button_home.setStatusTip("Home")
        self.button_home.setCheckable(True)
        toolbar.addAction(self.button_home)

        self.button_home.triggered.connect(self.hide)

        self.button_customer = QAction(QIcon("contact.png"), "Customers", self)
        self.button_customer.setCheckable(True)
        #button_customer.triggered.connect(self.CustomerTable)
        toolbar.addAction(self.button_customer)





class Manager:
    def __init__(self):
        self.first = MainWindowOne()
        self.second = MainWindowTwo()

        self.first.pushButton.clicked.connect(self.second.show)
        self.second.pushButton_2.clicked.connect(self.first.show)

        #self.first.button_home.triggered.connect(self.first.show)
        self.second.button_home.triggered.connect(self.first.show)
        self.first.button_customer.triggered.connect(self.second.show)

        self.first.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    manager = Manager()
    sys.exit(app.exec())
