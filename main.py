
import sys
import re
import sqlite3

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QActionGroup, QIcon
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlRelationalTableModel, QSqlQueryModel, QSqlQuery
from PySide6.QtWidgets import QApplication, QDialogButtonBox, QLabel, QMainWindow, QLineEdit, QPushButton, QStackedWidget, QToolBar, QToolButton, QVBoxLayout, QWidget

from Ui_home_widget import Ui_Home
from Ui_customer_widget import Ui_Customers
from add_customer_copy import addCustomerWindow
from Ui_add_project import Ui_MainWindow as addProjectWindow
from Ui_project_widget import Ui_Form
import insert_data_sql

db = QSqlDatabase("QSQLITE")
db.setDatabaseName("customer_data.db")
db.open()

#Create Main Window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(743, 653)

        self.home_button_checked = True
        
        toolbar = QToolBar()
        toolbar.setIconSize(QSize(30, 30))
        toolbar.setStyleSheet("QToolBar{spacing: 15px;}")
        toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.addToolBar(Qt.LeftToolBarArea, toolbar)

        self.button_home = QAction(QIcon("home (2).png"), "Home", self)
        self.button_home.setCheckable(True)
        self.button_home.triggered.connect(self.home_toggle)
        self.button_home.setChecked(self.home_button_checked)
        toolbar.addAction(self.button_home)
        
        self.button_customer = QAction(QIcon("contact.png"), "Customers", self)
        self.button_customer.setCheckable(True)
        self.button_customer.triggered.connect(self.customer_toggle)
        toolbar.addAction(self.button_customer)

        self.button_projects = QAction(QIcon("sketch (1).png"), "Projects", self)
        self.button_projects.setCheckable(True)
        self.button_projects.triggered.connect(self.projects_toggle)
        toolbar.addAction(self.button_projects)

        self.button_estimates = QAction(QIcon("budget.png"), "Estimates", self)
        self.button_estimates.setCheckable(True)
        toolbar.addAction(self.button_estimates)

        action_group = QActionGroup(self)
        action_group.addAction(self.button_home)
        action_group.addAction(self.button_customer)
        action_group.addAction(self.button_projects)
        action_group.addAction(self.button_estimates)      
        
        self.setCentralWidget(HomeWidget())
    
    def home_toggle(self):
        self.setCentralWidget(HomeWidget())
    
    def customer_toggle(self):
        self.setCentralWidget(CustomerWidget())
    
    def projects_toggle(self):
        self.setCentralWidget(ProjectWidget())


#Home Page widget
class HomeWidget(QWidget, Ui_Home):
    def __init__(self, parent = MainWindow):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.open_customer_add)

        self.quickAddProject = add_project()
        self.pushButton_2.clicked.connect(self.open_project_add)

        
        database = r"customer_data.db" #Database path
        conn = insert_data_sql.create_connection(database) #Creates database connection 
        with conn:
            self.dict = insert_data_sql.find_current_project(conn) #Create dictionary to store ids and names of current projects

        self.comboBox.addItems(self.dict.values()) #Add current projects to homepage combo box
        self.comboBox.activated.connect(self.populate_table)

        self.model = QSqlQueryModel()
        self.tableView.setModel(self.model)

        query = QSqlQuery("SELECT * FROM materials WHERE project_id = ?", db=db)
        current_id = self.get_key(self.comboBox.currentText())
        query.bindValue(0, current_id)
        query.exec()
       
        self.model.setQuery(query)

        headers = ["Project Id", "Material", "Description", "Quantity", "Price ($)", "Total ($)"]
        for i in range(len(headers)):
            self.model.setHeaderData(i, Qt.Horizontal, headers[i])

    
    def get_key(self, val):
        """ Get the project id from dictionary based on the project name value in combo box """
        
        for key, value in self.dict.items():
            if val == value:
                return key
        return "key doesn't exist"

    def populate_table(self):
        """
        Set new query when value of combo box is changed
        """
        id = self.get_key(self.comboBox.currentText())

        query = QSqlQuery("SELECT * FROM materials WHERE project_id = ?", db=db)
        query.bindValue(0, id)
        query.exec()

        self.model.setQuery(query)

        headers = ["Project Id", "Material", "Description", "Quantity", "Price ($)", "Total ($)"]
        for i in range(len(headers)):
            self.model.setHeaderData(i, Qt.Horizontal, headers[i])
        
    
    def open_customer_add(self):
        self.quickAddCustomer = addCustomerWindow()
        self.quickAddCustomer.show()

    def open_project_add(self):
        self.quickAddProject.show()
    

class CustomerWidget(QWidget, Ui_Customers):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.model = QSqlTableModel(db=db)
        self.tableView.setModel(self.model)

        self.model.setTable("Customer")
        column_titles = {
            "id": "Id",
            "first_name": "First Name",
            "last_name": "Last Name",
            "phone": "Phone #",
            "address": "Address",
            "city" : "City",
            "zip": "Zip Code",
        }
        for n, t in column_titles.items():
            idx = self.model.fieldIndex(n)
            self.model.setHeaderData(idx, Qt.Horizontal, t)
        
        self.model.select()

        self.lineEdit.setPlaceholderText("Search...")
        self.lineEdit.textChanged.connect(self.update_search) #filter customer table

    def update_search(self, s):
        s = re.sub("[\W_]+", "", s)
        filter_str = 'first_name LIKE "%{}%" OR last_name LIKE "%{}%" OR id LIKE "%{}%" OR phone LIKE "%{}%"'.format(s,s,s,s)
        self.model.setFilter(filter_str)


class ProjectWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.model_2 = QSqlTableModel(db=db)
        self.tableView_2.setModel(self.model_2)
        
        self.model_2.setTable("projects")
        self.model_2.select()

        self.addProject = add_project()
    
        self.pushButton_3.clicked.connect(self.open_project_add)
    def open_project_add(self):
        self.addProject.show()


class add_project(QMainWindow, addProjectWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)




app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()

