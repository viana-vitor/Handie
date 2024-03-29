import sys, os
import re
import sqlite3

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QActionGroup, QIcon
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlRelationalTableModel, QSqlQueryModel, QSqlQuery
from PySide6.QtWidgets import (QApplication, QDialogButtonBox, QLabel, QMainWindow, QLineEdit,
QPushButton, QStackedWidget, QToolBar, QToolButton, QVBoxLayout, QWidget, QDialog, QListWidgetItem, QHBoxLayout, QHeaderView)

from app.ui.Ui_customer_widget import Ui_Customers
from app.core.HomeWidget import HomeWidget
from app.core.ProjectWidget import ProjectWidget
from app.core.ProjectEstimateWidget import ProjectEstimate
from app.core.EstimateWidget import EstimateWidget
import app.data.database.create_tables as create_tables

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))

db = QSqlDatabase("QSQLITE")
db.setDatabaseName(os.path.join(ROOT_DIR, "app/data/database/customer_data.db"))
db.open()

#Create Main Window
class MainWindow(QMainWindow):
    def __init__(self, parent= None):
        super().__init__(parent)

        self.resize(1000, 700)

        create_tables.main(ROOT_DIR) #create database tables

        self.home_button_checked = True #start at home page
        
        toolbar = QToolBar()
        toolbar.setIconSize(QSize(30, 30))
        toolbar.setStyleSheet("QToolBar{spacing: 15px;}")
        toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.addToolBar(Qt.LeftToolBarArea, toolbar)

        self.button_home = QAction(QIcon(os.path.join(ROOT_DIR, "app/data/img/home.png")), "Home", self)
        self.button_home.setCheckable(True)
        self.button_home.triggered.connect(self.home_toggle)
        self.button_home.setChecked(self.home_button_checked)
        toolbar.addAction(self.button_home)
        
        self.button_customer = QAction(QIcon(os.path.join(ROOT_DIR, "app/data/img/contact.png")), "Customers", self)
        self.button_customer.setCheckable(True)
        self.button_customer.triggered.connect(self.customer_toggle)
        toolbar.addAction(self.button_customer)

        self.button_projects = QAction(QIcon(os.path.join(ROOT_DIR, "app/data/img/sketch.png")), "Projects", self)
        self.button_projects.setCheckable(True)
        self.button_projects.triggered.connect(self.projects_toggle)
        toolbar.addAction(self.button_projects)

        self.button_estimates = QAction(QIcon(os.path.join(ROOT_DIR, "app/data/img/budget.png")), "Estimates", self)
        self.button_estimates.setCheckable(True)
        self.button_estimates.triggered.connect(self.estimates_toggle)
        toolbar.addAction(self.button_estimates)

        action_group = QActionGroup(self)
        action_group.addAction(self.button_home)
        action_group.addAction(self.button_customer)
        action_group.addAction(self.button_projects)
        action_group.addAction(self.button_estimates)
        
        self.home_widget = HomeWidget(ROOT_DIR)
        self.setCentralWidget(self.home_widget)
        self.home_widget.EstimatePageSignal.connect(self.open_estimate)
    
    
    def home_toggle(self):
        self.home_widget = HomeWidget(ROOT_DIR)
        self.button_home.setChecked(True)
        self.home_widget.EstimatePageSignal.connect(self.open_estimate)
        self.setCentralWidget(self.home_widget)
    
    def customer_toggle(self):
        self.customer_widget = CustomerWidget()
        self.setCentralWidget(self.customer_widget)
    
    def projects_toggle(self):
        self.project_widget = ProjectWidget(ROOT_DIR)
        self.project_widget.CreateNewProject.connect(self.open_new_project_form)
        self.setCentralWidget(self.project_widget)
    
    def estimates_toggle(self):
        self.estimate_widget = EstimateWidget(ROOT_DIR)
        self.setCentralWidget(self.estimate_widget)

    def open_estimate(self, customer_id, project_id, task_id, source, basedir):
        self.project_estimate = ProjectEstimate(customer_id, project_id, task_id, source, basedir)
        self.button_estimates.setChecked(True)
        self.project_estimate.HomeWidgetSignal.connect(self.home_toggle)
        self.setCentralWidget(self.project_estimate)

    def open_new_project_form(self):
        self.home_widget = HomeWidget(ROOT_DIR)
        self.home_widget.stackedWidget.setCurrentIndex(1)
        self.home_widget.EstimatePageSignal.connect(self.open_estimate)
        self.setCentralWidget(self.home_widget)


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
            "email": "Email"
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



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()