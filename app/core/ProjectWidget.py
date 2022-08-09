from __future__ import with_statement
from asyncio import Task, tasks
from curses import keyname
import sys
import sqlite3
import json

from PySide6.QtCore import Qt, QSize, Signal, QDate
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel, QSqlTableModel
from PySide6.QtWidgets import (QWidget, QLabel, QListWidgetItem, QHBoxLayout, QHeaderView, QDataWidgetMapper, QButtonGroup)

from app.ui.Ui_project_widget import Ui_Projects
from app.ui.Ui_edit_material_form import Ui_Form as UiEditMaterial
from app.ui.Ui_task_list_widget import Ui_Form as Ui_task_widget
from app.ui.Ui_add_material_form import Ui_Form as UiAddMaterial
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

        self.listWidget.itemClicked.connect(self.populate_fields)

        self.markCompletedButton.clicked.connect(self.mark_completed)

        self.projectLineEdit.editingFinished.connect(self.update_project_info)
        self.addressLineEdit.editingFinished.connect(self.update_customer_info)
        self.cityLineEdit.editingFinished.connect(self.update_customer_info)
        self.phoneLineEdit.editingFinished.connect(self.update_customer_info)
        self.emailLineEdit.editingFinished.connect(self.update_customer_info)
        self.begDateEdit.dateChanged.connect(self.beg_date_changed)
        self.endDateEdit.dateChanged.connect(self.end_date_changed)

        self.tasks_button_grp = QButtonGroup(exclusive = False)
        self.tasks_button_grp.addButton(self.kitchenCheck)
        self.tasks_button_grp.addButton(self.bathroomCheck)
        self.tasks_button_grp.addButton(self.bedroomCheck)
        self.tasks_button_grp.addButton(self.multipleroomCheck)
        self.tasks_button_grp.addButton(self.additionCheck)
        self.tasks_button_grp.addButton(self.livingroomCheck)
        self.tasks_button_grp.addButton(self.exteriorCheck)
        self.tasks_button_grp.addButton(self.landscapeCheck)

        # self.kitchenCheck.stateChanged.connect(self.set_construction_tasks)
        # self.bathroomCheck.stateChanged.connect(self.set_construction_tasks)
        #self.bedroomCheck.stateChanged.connect(self.delete_tasks_widget)


        self.editMaterialBtn.clicked.connect(self.open_edit_form)
        self.addMaterialbtn.clicked.connect(self.open_add_form)
        
    

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
        self.task_id = insert_data_sql.get_task_id(self.conn, self.project_id)
        
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
        self.check_tasks()
    
    def mark_completed(self):
        '''Mark project status as complete'''

        with self.conn:
            insert_data_sql.mark_as_complete(self.conn, self.project_id)
        
        self.markCompletedButton.setEnabled(False)
        self.create_list()
        self.model.clear()
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

        idx = self.listWidget.currentIndex()
        self.create_list()
        self.listWidget.setCurrentIndex(idx)


    def update_project_info(self):
        '''Save new project information'''
        sql = '''UPDATE projects
                    SET project_name = '{project}'
                     WHERE id = ?'''.format(project = self.projectLineEdit.text())
        
        cur = self.conn.cursor()
        cur.execute(sql, [self.project_id])
        self.conn.commit()

        idx = self.listWidget.currentIndex()
        self.create_list()
        self.listWidget.setCurrentIndex(idx)

    
    def beg_date_changed(self):
        '''Save new beggining of project date'''
        if self.begDateEdit.text() != self.dates[0]:
            sql = '''UPDATE projects
                    SET begin_date = '{}'
                    WHERE id = ?'''.format(self.begDateEdit.text())
            cur = self.conn.cursor()
            cur.execute(sql, [self.project_id])
            self.conn.commit()
        else:
            pass
    
    
    def end_date_changed(self):
        '''Save new end of project date'''
        if self.endDateEdit.text() != self.dates[1]:
            sql = '''UPDATE projects
                    SET end_date = '{}'
                    WHERE id = ?'''.format(self.endDateEdit.text())
            cur = self.conn.cursor()
            cur.execute(sql, [self.project_id])
            self.conn.commit()
        else:
            pass
        
    
    def uncheck_tasks(self):
        '''Uncheck previously checked tasks when changing between projects'''
    
        for button in self.tasks_button_grp.buttons():
            button.setChecked(False)
    
    def check_tasks(self):
        '''Retrieve checked tasks from json'''
        self.uncheck_tasks() ### First uncheck all checkboxes 

        with open("app/data/database/user_tasks.json", "r") as f:
            user_checked_tasks = json.load(f)
        
        for button in self.tasks_button_grp.buttons():
            for dict in user_checked_tasks[::-1]:
                if dict['task_id'] == self.task_id:
                    for key in dict['tasks'].keys():
                        if button.text() == key:
                            button.setChecked(True)
        
        self.set_construction_tasks()

    
    def set_construction_tasks(self):
        '''This function takes care of creating and destroying tasks widgets, as well as populating it with tasks and checking then if
            they were previously checked when creating the project'''

        
        with open("app/data/database/user_tasks.json", "r") as f:
            user_checked_tasks = json.load(f)
        
        with open("app/data/database/tasks_kw.json", "r") as n:
            tasks_keywords = json.load(n)

        
        idx = 6
        for button in self.tasks_button_grp.buttons():
            widget = self.findChild(TaskList, '{}_widget'.format(button.text()))
        
            for dict in user_checked_tasks[::-1]:
                if dict['task_id'] == self.task_id:
            
                    if button.isChecked() and widget == None: ## if the widget has not been created before -> create and populate a new one
                
                        self.new_widget = TaskList('{}_widget'.format(button.text()))
                        self.verticalLayout_2.insertWidget(idx, self.new_widget)
                        self.new_widget.label.setText("{}".format(button.text()))
                        idx += 1
                        for value in tasks_keywords[button.text()]['Demolition']:
                            item = QListWidgetItem(value)
                            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
                            if value in dict['tasks'][button.text()]['Demolition']:
                                item.setCheckState(Qt.Checked)
                            else:
                                item.setCheckState(Qt.Unchecked)
                            self.new_widget.listWidget.addItem(item)
                        for value in tasks_keywords[button.text()]['Rebuild']:
                            item = QListWidgetItem(value)
                            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
                            if value in dict['tasks'][button.text()]['Rebuild']:
                                item.setCheckState(Qt.Checked)
                            else:
                                item.setCheckState(Qt.Unchecked)
                            self.new_widget.listWidget_2.addItem(item)
                        for value in tasks_keywords[button.text()]['Cosmetic']:
                            item = QListWidgetItem(value)
                            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
                            if value in dict['tasks'][button.text()]['Cosmetic']:
                                item.setCheckState(Qt.Checked)
                            else:
                                item.setCheckState(Qt.Unchecked)
                            self.new_widget.listWidget_3.addItem(item)

                    elif button.isChecked() and widget != None: ### if the widget has been previously created -> reload it with tasks from new project
                        
                        widget.listWidget.clear()
                        widget.listWidget_2.clear()
                        widget.listWidget_3.clear()
                        for value in tasks_keywords[button.text()]['Demolition']:
                            item = QListWidgetItem(value)
                            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
                            if value in dict['tasks'][button.text()]['Demolition']:
                                item.setCheckState(Qt.Checked)
                            else:
                                item.setCheckState(Qt.Unchecked)
                            widget.listWidget.addItem(item)
                        for value in tasks_keywords[button.text()]['Rebuild']:
                            item = QListWidgetItem(value)
                            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
                            if value in dict['tasks'][button.text()]['Rebuild']:
                                item.setCheckState(Qt.Checked)
                            else:
                                item.setCheckState(Qt.Unchecked)
                            widget.listWidget_2.addItem(item)
                        for value in tasks_keywords[button.text()]['Cosmetic']:
                            item = QListWidgetItem(value)
                            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
                            if value in dict['tasks'][button.text()]['Cosmetic']:
                                item.setCheckState(Qt.Checked)
                            else:
                                item.setCheckState(Qt.Unchecked)
                            widget.listWidget_3.addItem(item)
                    
                    elif button.isChecked() == False and widget != None: ## Delete tasks widgets that do not belong to the selected project
                        self.verticalLayout_2.removeWidget(widget)
                        widget.deleteLater()

    
    #def tasks_state_changed(self):
    
    
    
    
    
    
    
    
    
    
    
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
    

    def open_edit_form(self):

        self.editForm = EditForm(self.project_id)
        self.editForm.show()
        self.editForm.FormClosed.connect(self.set_materials_table)
    
    def open_add_form(self):
        self.addForm = AddForm(self.conn, self.project_id)
        self.addForm.show()
        self.addForm.FormClosed.connect(self.set_materials_table)



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


class EditForm(QWidget, UiEditMaterial):
    
    FormClosed = Signal()

    def __init__(self, project_id):
        super().__init__()
        self.setupUi(self)

        self.model = QSqlTableModel(db=db)

        self.mapper = QDataWidgetMapper()
        self.mapper.setModel(self.model)

        self.mapper.addMapping(self.idSpinBox, 0)
        self.mapper.addMapping(self.materialNameEdit, 1)
        self.mapper.addMapping(self.descTextEdit, 2)
        self.mapper.addMapping(self.qtySpinBox, 3)
        self.mapper.addMapping(self.priceSpinBox, 4)

        self.model.setTable('materials')
        filter_str = 'project_id = {}'.format(project_id)
        self.model.setFilter(filter_str)
        self.model.select()

        self.mapper.toFirst()

        self.previousBtn.clicked.connect(self.mapper.toPrevious)
        self.nextBtn.clicked.connect(self.mapper.toNext)
        self.saveBtn.clicked.connect(self.on_submit)
    
    def on_submit(self):
        self.mapper.submit()
        self.close()
        self.FormClosed.emit()
    

class AddForm(QWidget, UiAddMaterial):
    
    FormClosed = Signal()

    def __init__(self, conn, project_id):
        super().__init__()
        self.setupUi(self)

        self.conn = conn
        self.project_id = project_id

        self.cancelBtn.clicked.connect(self.on_cancel)
        self.addBtn.clicked.connect(self.on_add)

    def on_cancel(self):
        self.close()
    
    def on_add(self):
        
        total = self.qtySpinBox.value() * self.priceSpinBox.value()
        new_material = [self.project_id, self.materialNameLineEdit.text(), self.descTextEdit.toPlainText(), 
                            self.qtySpinBox.value(), self.priceSpinBox.value(), total]
        
        with self.conn:
            insert_data_sql.add_materials(self.conn, new_material)
        
        self.close()
        self.FormClosed.emit()
    



class TaskList(QWidget, Ui_task_widget):
    def __init__(self, name, parent=None):
        super().__init__()
        self.setupUi(self)

        self.setObjectName(name)

