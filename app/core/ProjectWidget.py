import sys
import sqlite3

from PySide6.QtCore import Qt, QSize, Signal, QDate
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PySide6.QtWidgets import (QWidget, QLabel, QListWidgetItem, QHBoxLayout, QHeaderView)

from app.ui.Ui_project_widget import Ui_Projects
import app.data.database.insert_data_sql as insert_data_sql


db = QSqlDatabase("QSQLITE")
db.setDatabaseName("app/data/database/customer_data.db")
db.open()


class ProjectWidget(QWidget, Ui_Projects):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        database = r"app/data/database/customer_data.db" #Database path
        self.conn = insert_data_sql.create_connection(database)
        
        self.searchLineEdit.setPlaceholderText("Search...")
        self.searchLineEdit.textChanged.connect(self.on_text_changed)

        self.project_id = None
        self.customer_id = None

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

        self.projectLineEdit.editingFinished.connect(self.update_project_info)
        self.addressLineEdit.editingFinished.connect(self.update_customer_info)
        self.cityLineEdit.editingFinished.connect(self.update_customer_info)
        self.phoneLineEdit.editingFinished.connect(self.update_customer_info)
        self.emailLineEdit.editingFinished.connect(self.update_customer_info)
        self.begDateEdit.dateChanged.connect(self.beg_date_changed)
        self.endDateEdit.dateChanged.connect(self.end_date_changed)
    

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
        
        self.project_id = widget.id
        self.customer_id = widget.customer_id
        
        with self.conn:
            self.dates = insert_data_sql.get_dates(self.conn, self.project_id)
        

        self.begDateEdit.setDate(QDate.fromString(self.dates[0], 'M/d/yyyy'))
        self.endDateEdit.setDate(QDate.fromString(self.dates[1], 'M/d/yyyy'))

        with self.conn:
            info = insert_data_sql.get_customer_data(self.conn, self.customer_id)
        
        self.phoneLineEdit.setText(info[1])
        self.addressLineEdit.setText(info[2])
        self.cityLineEdit.setText(info[3])

        self.set_materials_table()
    
    def mark_completed(self):
        '''Mark project status as complete'''

        with self.conn:
            insert_data_sql.mark_as_complete(self.conn, self.project_id)
        
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

    
    def update_customer_info(self):
        '''Update customer info if it has been changed'''
        
        sql = '''UPDATE customer
                SET phone = '{phone}',
                    address = '{address}',
                    city = '{city}'
                WHERE id = ?'''.format(phone = self.phoneLineEdit.text(),
                                        address = self.addressLineEdit.text(),
                                        city = self.cityLineEdit.text()) #### DO NOT FORGET TO ADD EMAIL TO THIS    
        
        cur = self.conn.cursor()
        cur.execute(sql, [self.customer_id])
        self.conn.commit()

    def update_project_info(self):
        '''Save new project information'''
        sql = '''UPDATE projects
                    SET project_name = '{project}'
                     WHERE id = ?'''.format(project = self.projectLineEdit.text())
        
        cur = self.conn.cursor()
        cur.execute(sql, [self.project_id])
        self.conn.commit()


    
    def beg_date_changed(self):
        '''Save new beggining of project date'''
        if self.begDateEdit.text() != self.dates[0]:
            sql = '''UPDATE projects
                    SET begin_date = '{}'
                    WHERE id = ?'''.format(self.begDateEdit.text())
            cur = self.conn.cursor()
            cur.execute(sql, [self.project_id])
            self.conn.commit()
    
    
    def end_date_changed(self):
        '''Save new end of project date'''
        if self.endDateEdit.text() != self.dates[1]:
            sql = '''UPDATE projects
                    SET end_date = '{}'
                    WHERE id = ?'''.format(self.endDateEdit.text())
            cur = self.conn.cursor()
            cur.execute(sql, [self.project_id])
            self.conn.commit()

    

    def set_materials_table(self):

        self.model = QSqlQueryModel()
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        query = QSqlQuery(db=db)

        query.prepare(
            '''SELECT material_name, description, quantity, price, (quantity * price) AS total
                FROM materials
                WHERE project_id = ?'''
        )

        query.bindValue(0, self.project_id)
        query.exec()
        self.model.setQuery(query)

        headers = ["Material", "Description", "Quantity", "Price ($)", "Total ($)"]
        for i in range(len(headers)):
            self.model.setHeaderData(i, Qt.Horizontal, headers[i])




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