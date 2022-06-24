import sys
import re
import sqlite3

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QActionGroup, QIcon
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlRelationalTableModel, QSqlQueryModel, QSqlQuery
from PySide6.QtWidgets import (QApplication, QDialogButtonBox, QLabel, QMainWindow, QLineEdit,
QPushButton, QStackedWidget, QToolBar, QToolButton, QVBoxLayout, QWidget, QDialog, QListWidgetItem, QHBoxLayout, QHeaderView)

from app.ui.Ui_customer_widget import Ui_Customers
from app.ui.Ui_project_widget import Ui_Projects
from HomeWidget import HomeWidget
from ProjectEstimateWidget import ProjectEstimate
import insert_data_sql

db = QSqlDatabase("QSQLITE")
db.setDatabaseName("customer_data.db")
db.open()

#Create Main Window
class MainWindow(QMainWindow):
    def __init__(self, parent= None):
        super().__init__(parent)

        self.resize(900, 700)

        self.home_button_checked = True
        
        toolbar = QToolBar()
        toolbar.setIconSize(QSize(30, 30))
        toolbar.setStyleSheet("QToolBar{spacing: 15px;}")
        toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.addToolBar(Qt.LeftToolBarArea, toolbar)

        self.button_home = QAction(QIcon("app/data/img/home.png"), "Home", self)
        self.button_home.setCheckable(True)
        self.button_home.triggered.connect(self.home_toggle)
        self.button_home.setChecked(self.home_button_checked)
        toolbar.addAction(self.button_home)
        
        self.button_customer = QAction(QIcon("app/data/img/contact.png"), "Customers", self)
        self.button_customer.setCheckable(True)
        self.button_customer.triggered.connect(self.customer_toggle)
        toolbar.addAction(self.button_customer)

        self.button_projects = QAction(QIcon("app/data/img/sketch.png"), "Projects", self)
        self.button_projects.setCheckable(True)
        self.button_projects.triggered.connect(self.projects_toggle)
        toolbar.addAction(self.button_projects)

        self.button_estimates = QAction(QIcon("app/data/img/budget.png"), "Estimates", self)
        self.button_estimates.setCheckable(True)
        toolbar.addAction(self.button_estimates)

        action_group = QActionGroup(self)
        action_group.addAction(self.button_home)
        action_group.addAction(self.button_customer)
        action_group.addAction(self.button_projects)
        action_group.addAction(self.button_estimates)
        
        self.home_widget = HomeWidget()
        self.customer_widget = CustomerWidget()
        self.project_widget = ProjectWidget()
        
        self.setCentralWidget(self.home_widget)

        #self.home_widget.main_window_connection.EstimatePageSignal.connect(self.custom_slot)

        self.home_widget.EstimatePageSignal.connect(self.open_estimate)
        #self.setCentralWidget(self.home_widget)
    
    
    
    def home_toggle(self):
        self.home_widget = HomeWidget()
        self.home_widget.EstimatePageSignal.connect(self.open_estimate)
        self.setCentralWidget(self.home_widget)
    
    def customer_toggle(self):
        self.customer_widget = CustomerWidget()
        self.setCentralWidget(self.customer_widget)
    
    def projects_toggle(self):
        self.project_widget = ProjectWidget()
        self.setCentralWidget(self.project_widget)
    
    def setMyCentral(self, widgetClass):
        myWidget = widgetClass()
        self.setCentralWidget(myWidget)

    def open_estimate(self, customer_id, project_id, task_id):
        self.project_estimate = ProjectEstimate(customer_id, project_id, task_id)
        self.setCentralWidget(self.project_estimate)


class CustomerWidget(QWidget, Ui_Customers):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.model = QSqlTableModel(db=db)
        self.tableView.setModel(self.model)

        self.model.setTable("Customer")
        column_titles = {
            "id": "ID",
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
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.lineEdit.setPlaceholderText("Search...")
        self.lineEdit.textChanged.connect(self.update_search) #filter customer table

    def update_search(self, s):
        s = re.sub("[\W_]+", "", s)
        filter_str = 'first_name LIKE "%{}%" OR last_name LIKE "%{}%" OR id LIKE "%{}%" OR phone LIKE "%{}%"'.format(s,s,s,s)
        self.model.setFilter(filter_str)


class ProjectWidget(QWidget, Ui_Projects):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        database = r"customer_data.db" #Database path
        self.conn = insert_data_sql.create_connection(database)
        
        self.searchLineEdit.setPlaceholderText("Search...")
        self.searchLineEdit.textChanged.connect(self.on_text_changed)

        with self.conn:
            self.projects = insert_data_sql.get_project_customer_name(self.conn)
        for id, customer_id, project, customer, status in self.projects:
            myListWidget = customListItem()
            myListWidget.id(id)
            myListWidget.customer_id(customer_id)
            myListWidget.setProject(project)
            myListWidget.setCustomer(customer)
            myListWidget.setStatus(status)
            listWidgetItem = QListWidgetItem(self.listWidget)
            listWidgetItem.setSizeHint(QSize(15, 40))
            self.listWidget.addItem(listWidgetItem)
            self.listWidget.setItemWidget(listWidgetItem, myListWidget)

            self.listWidget.itemClicked.connect(self.populate_fields)
        
    def on_text_changed(self, text):
        for row in range(self.listWidget.count()):
            item = self.listWidget.item(row)
            widg = self.listWidget.itemWidget(item)
            if text:
                item.setHidden(not self.filter(text.lower(), widg.customerText.text().lower()))
            else:
                item.setHidden(False)
    
    def filter(self, text, customer):
        return text in customer

    def populate_fields(self, item):
        
        widget = self.listWidget.itemWidget(item)
        project = widget.projectText.text()
        customer = widget.customerText.text()
        self.projectLabel.setText(project)
        self.customerLabel.setText(customer)
        project_id = widget.id
        customer_id = widget.customer_id
        
        with self.conn:
            dates = insert_data_sql.get_dates(self.conn, project_id)
        
        self.begDateLabel.setText(dates[0])
        self.endDateLabel.setText(dates[1])




class customListItem(QWidget):
    def __init__(self, parent=None):
        super(customListItem, self).__init__(parent)
        self.textLayout = QHBoxLayout()
        self.projectText = QLabel()
        self.customerText = QLabel()
        self.statusText = QLabel()
        self.textLayout.addWidget(self.projectText)
        self.textLayout.addWidget(self.customerText)
        self.textLayout.addWidget(self.statusText)
        self.setLayout(self.textLayout)
    
    def id(self, id):
        self.id = id
    
    def customer_id(self, customer_id):
        self.customer_id = customer_id

    def setProject(self, text):
        self.projectText.setText(text)
    
    def setCustomer(self, text):
        self.customerText.setText(text)
    
    def setStatus(self, text):
        self.statusText.setText(text)




app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()