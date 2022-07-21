import sys
import sqlite3

from PySide6.QtCore import Qt, QSize, Signal
from PySide6.QtSql import QSqlDatabase
from PySide6.QtWidgets import (QWidget, QLabel, QListWidgetItem, QHBoxLayout)

from app.ui.Ui_project_widget import Ui_Projects
import app.data.database.insert_data_sql as insert_data_sql


class ProjectWidget(QWidget, Ui_Projects):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        database = r"app/data/database/customer_data.db" #Database path
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