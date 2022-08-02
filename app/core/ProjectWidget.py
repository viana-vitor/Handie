import sys
import sqlite3

from PySide6.QtCore import Qt, QSize, Signal, QDate
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

        self.create_list()

        # with self.conn:
        #     self.projects = insert_data_sql.get_project_customer_name(self.conn)
        # for id, customer_id, project, customer, status in self.projects:
        #     myListWidget = customListItem()
        #     myListWidget.id(id)
        #     myListWidget.customer_id(customer_id)
        #     myListWidget.setProject(project)
        #     myListWidget.setCustomer(customer)
        #     myListWidget.setStatus(status)

        #     listWidgetItem = QListWidgetItem(self.listWidget)
        #     listWidgetItem.setSizeHint(QSize(30, 45))
        #     self.listWidget.addItem(listWidgetItem)
        #     self.listWidget.setItemWidget(listWidgetItem, myListWidget)

        self.listWidget.itemClicked.connect(self.populate_fields)

        self.markCompletedButton.clicked.connect(self.mark_completed)

        self.projectLineEdit.textEdited.connect(self.info_data_changed)
        self.customerLineEdit.textEdited.connect(self.info_data_changed)
        self.addressLineEdit.textEdited.connect(self.info_data_changed)
        self.cityLineEdit.textEdited.connect(self.info_data_changed)
        self.phoneLineEdit.textEdited.connect(self.info_data_changed)
        self.emailLineEdit.textEdited.connect(self.info_data_changed)
    

    def create_list(self):
        '''Create list of projects'''

        self.listWidget.clear()
        self.markCompletedButton.setEnabled(True)
        
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
            listWidgetItem.setSizeHint(QSize(30, 45))
            self.listWidget.addItem(listWidgetItem)
            self.listWidget.setItemWidget(listWidgetItem, myListWidget)


    def on_text_changed(self, text):
        '''Filter project list based on project or customer name'''
        for row in range(self.listWidget.count()):
            item = self.listWidget.item(row)
            widg = self.listWidget.itemWidget(item)
            if text.lower() in widg.customerText.text().lower():
                item.setHidden(False)
            elif text.lower() in widg.projectText.text().lower():
                item.setHidden(False)
            else:
                item.setHidden(True)
    

    def populate_fields(self, item):
        '''Populate customer info section with data'''
        
        widget = self.listWidget.itemWidget(item)
        project = widget.projectText.text()
        customer = widget.customerText.text()
        self.projectLineEdit.setText(project)
        self.customerLineEdit.setText(customer)
        project_id = widget.id
        customer_id = widget.customer_id
        
        with self.conn:
            dates = insert_data_sql.get_dates(self.conn, project_id)
        

        self.begDateEdit.setDate(QDate.fromString(dates[0], 'M/d/yyyy'))
        self.endDateEdit.setDate(QDate.fromString(dates[1], 'M/d/yyyy'))

        with self.conn:
            info = insert_data_sql.get_customer_data(self.conn, customer_id)
        
        self.phoneLineEdit.setText(info[1])
        self.addressLineEdit.setText(info[2])
        self.cityLineEdit.setText(info[3])
    
    def mark_completed(self):
        '''Mark project status as complete'''
        
        item = self.listWidget.currentItem()
        widg = self.listWidget.itemWidget(item)
        project_id = widg.id

        with self.conn:
            insert_data_sql.mark_as_complete(self.conn, project_id)
        
        self.markCompletedButton.setEnabled(False)
        self.create_list()
        self.projectLineEdit.clear()
        self.customerLineEdit.clear()
        self.endDateEdit.clear()
        self.begDateEdit.clear()
        self.addressLineEdit.clear()
        self.phoneLineEdit.clear()
        self.cityLineEdit.clear()
        self.emailLineEdit.clear()

    
    def info_data_changed(self):
        '''Update info if it has been changed'''

        item = self.listWidget.currentItem()
        widg = self.listWidget.itemWidget(item)
        project_id = widg.id
        customer_id = widg.customer_id
        
        sql = '''UPDATE customer
                SET phone = {phone},
                    address = {address},
                    city = {city},
                    email = {email}
                WHERE id = ?'''.format(phone = self.phoneLineEdit.text(),
                                        address = self.addressLineEdit.text(),
                                        city = self.cityLineEdit.text(),
                                        email = self.emailLineEdit.text())
        
        sql2 = '''UPDATE projects
                SET project_name = {project},
                    begin_date = {beg_date},
                    end_date = {end_date}
                WHERE id = ?'''.format(project = self.projectLineEdit.text(), 
                                        beg_date = self.begDateEdit.text(),
                                        end_date = self.endDateEdit.text())
        
        cur = self.conn.cursor()
        cur.execute(sql, [customer_id])
        cur.execute(sql2, [project_id])
        self.conn.commit()
        




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