from asyncio import Task
import sys
import re
import sqlite3
import json
import os

from PySide6.QtCore import Qt, QSize, Signal, QObject
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlRelationalTableModel, QSqlQueryModel, QSqlQuery
from PySide6.QtWidgets import (QApplication, QDialogButtonBox, QWidget, QMainWindow, QDialog, QVBoxLayout, QLabel, QCheckBox,
 QListWidgetItem, QButtonGroup, QHeaderView, QTableWidgetItem)

from Ui_add_proj_new_version import Ui_Form as Ui_new_home
from Ui_task_list_widget import Ui_Form as Ui_task_widget
from ProjectEstimateWidget import ProjectEstimate
import insert_data_sql

db = QSqlDatabase("QSQLITE")
db.setDatabaseName("customer_data.db")
db.open()


# class MainWindowSignal(QObject):
#     EstimatePageSignal = Signal()


#Home Page widget
class HomeWidget(QWidget, Ui_new_home):
    
    EstimatePageSignal = Signal(int, int, int)

    def __init__(self, parent = None):
        super(HomeWidget, self).__init__(parent)
        self.setupUi(self)
        #self.main_window_connection = MainWindowSignal()
        
        ##################################
        ########### Initial Page #########

        database = r"customer_data.db" #Database path
        self.conn = insert_data_sql.create_connection(database) #Creates database connection 
        with self.conn:
            self.dict = insert_data_sql.find_current_project(self.conn) #Create dictionary to store ids and names of current projects

        self.comboBox.addItems(self.dict.values()) #Add current projects to homepage combo box
        self.comboBox.currentIndexChanged.connect(self.populate_table)

        self.model = QSqlQueryModel()
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #self.tableView.horizontalHeader().setStretchLastSection(True)

        #Populates inital materials table based on current project selected from combo box
        query = QSqlQuery("SELECT * FROM materials WHERE project_id = ?", db=db)
        current_id = self.get_key(self.dict, self.comboBox.currentText())
        query.bindValue(0, current_id)
        query.exec()
        self.model.setQuery(query)

        self.markCompleteButton.clicked.connect(self.mark_as_complete) #Connects "Mark as completed" button

        headers = ["Project ID", "Material", "Description", "Quantity", "Price ($)", "Total ($)"]
        for i in range(len(headers)):
            self.model.setHeaderData(i, Qt.Horizontal, headers[i])

        self.addNewProjectButton.clicked.connect(self.open_new_project_form) #Open new project form
        
        #####################################################
        ######## Customer Add Project Page #########
        
        self.newCustomerButton.clicked.connect(self.new_customer_project) #Open new project form for new customer
        self.existingCustomerButton.clicked.connect(self.existing_customer_project) #Open new project form for existing customer
        
        
        with self.conn:
            self.full_name_dict = insert_data_sql.get_full_customer_name(self.conn)
        self.customerNameComboBox.addItems(self.full_name_dict.values())

        self.addressCheckBox.stateChanged.connect(self.same_address_check)
        self.customerNameComboBox.currentIndexChanged.connect(self.same_address_check)
        self.addressLineEdit.textChanged.connect(self.same_address_check)

        # Contruction area check boxes
        
        self.tasks_button_grp = QButtonGroup(exclusive = False)
        self.tasks_button_grp.addButton(self.kitchenCheck)
        self.tasks_button_grp.addButton(self.bathroomCheck)
        self.tasks_button_grp.addButton(self.bedroomCheck)
        self.tasks_button_grp.addButton(self.multipleRoomCheck)
        self.tasks_button_grp.addButton(self.additionCheck)
        self.tasks_button_grp.addButton(self.otherCheck)

        self.constructionAreaStacked.setEnabled(False)
        self.constructionAreaStacked.setCurrentIndex(0)
        self.kitchenCheck.stateChanged.connect(self.new_task)
        self.bathroomCheck.stateChanged.connect(self.new_task)
        self.bedroomCheck.stateChanged.connect(self.new_task)
        self.multipleRoomCheck.stateChanged.connect(self.new_task)
        self.additionCheck.stateChanged.connect(self.new_task)
        self.otherCheck.stateChanged.connect(self.new_task)
        
        
        self.continueButton.clicked.connect(self.continue_add_material_page)
        self.cancelButton.clicked.connect(self.cancel_event)

        # Add new task keyword to task list 

        self.project_id = None
        self.task_id = None

        self.finishAddMaterialButton.clicked.connect(self.finish_save_project)

        ####### Add Materials section ##################

        self.backButton.clicked.connect(self.go_back)
        self.addMaterialPushButton.clicked.connect(self.add_material)

        
        # self.model_materials = QSqlTableModel(db=db)
        # self.model_materials.setTable('materials')
        # self.materialsTableView.setModel(self.model_materials)
        # for i in range(len(headers)):
        #     self.model_materials.setHeaderData(i, Qt.Horizontal, headers[i])
        # self.materialsTableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        
        self.materialsTableWidget.setColumnCount(5)
        self.materialsTableWidget.setHorizontalHeaderLabels(["Material", "Description", "Quantity", "Price ($)", "Total ($)"])
        self.materialsTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.materialsTableWidget.cellChanged.connect(self.cell_changed)



    
    def get_key(self, dict, val):
        """ Get id from dictionary of values """
        
        for key, value in dict.items():
            if val == value:
                return key
        return "key doesn't exist"

    def populate_table(self):
        """
        Set new query when current project on combo box is changed
        """
        id = self.get_key(self.dict, self.comboBox.currentText())

        query = QSqlQuery("SELECT * FROM materials WHERE project_id = ?", db=db)
        query.bindValue(0, id)
        query.exec()

        self.model.setQuery(query)
      
    def mark_as_complete(self):
        '''Mark a current project as complete'''
        
        id = self.get_key(self.dict, self.comboBox.currentText())
        with self.conn:
            insert_data_sql.mark_as_complete(self.conn, id)
        self.comboBox.removeItem(self.comboBox.currentIndex()) #Remove the completed project from the combo box
    
    
    
    def open_new_project_form(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def new_customer_project(self):
        
        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget_3.setCurrentIndex(1) #index 1 shows new customer page
        self.stackedWidget_3.setMaximumSize(QSize(16777215, 16777215))

    def existing_customer_project(self):

        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget_3.setCurrentIndex(0) #index 0 shows existing customer page
        self.stackedWidget_3.setMaximumSize(QSize(16777215, 55))

    def cancel_event(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def go_back(self):
        self.stackedWidget.setCurrentIndex(2)

            
            
    
    def new_task(self):
        ''' Populate tasks on list widget according to construction area'''

        with open("tasks_kw.json", "r") as f:
            tasks_data = json.load(f)

        checked_buttons = 0
        
        for button in self.tasks_button_grp.buttons():
            # First remove added widgets if they already exists. This will reload the widgets everytime a checkbox is checked or unchecked
            widget = self.findChild(TasksWidget, "{}_widget".format(button.text()))

            if button.isChecked():
                checked_buttons += 1
            
            if checked_buttons == 0:
                self.constructionAreaStacked.show()
            else:
                self.constructionAreaStacked.hide()
              
            if button.isChecked() and widget == None:

                self.new_widget = TasksWidget("{}_widget".format(button.text()))
                self.verticalLayout_6.addWidget(self.new_widget)
                self.new_widget.label.setText("{}".format(button.text()))
                self.new_widget.pushButton.clicked.connect(self.add_new_task_keyword)
                self.new_widget.pushButton_2.clicked.connect(self.add_new_task_keyword)
                self.new_widget.pushButton_3.clicked.connect(self.add_new_task_keyword)
                
                for key in tasks_data.keys():
                    if button.text() == key:
                        for value in tasks_data[key]["Demolition"]:
                            item = QListWidgetItem(value)
                            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
                            item.setCheckState(Qt.Unchecked)
                            self.new_widget.listWidget.addItem(item)
                        for value in tasks_data[key]["Rebuild"]:
                            item = QListWidgetItem(value)
                            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
                            item.setCheckState(Qt.Unchecked)
                            self.new_widget.listWidget_2.addItem(item)
                        for value in tasks_data[key]["Cosmetic"]:
                            item = QListWidgetItem(value)
                            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
                            item.setCheckState(Qt.Unchecked)
                            self.new_widget.listWidget_3.addItem(item)
 
            elif button.isChecked() == False and widget != None:
                self.verticalLayout_6.removeWidget(widget)
                widget.deleteLater()
        

                

                
    def add_new_task_keyword(self):
        '''Read data from json tasks, and add new keywords from user imput'''
        with open("tasks_kw.json", "r") as f:
            tasks_data = json.load(f)

            # for i in range(self.gridLayout_11.count()):
            #     widget = self.gridLayout_11.itemAt(i).widget()
            for button in self.tasks_button_grp.buttons():
                widget = self.findChild(TasksWidget, "{}_widget".format(button.text()))
            
                if button.isChecked() and widget !=None:
                    for key in tasks_data.keys():
                        if button.text() == key:
                            if widget.lineEdit.text():
                                tasks_data[key]["Demolition"].append(widget.lineEdit.text())
                                item = QListWidgetItem(widget.lineEdit.text())
                                item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
                                item.setCheckState(Qt.Unchecked)
                                widget.lineEdit.clear()
                                widget.listWidget.addItem(item)
                            elif widget.lineEdit_2.text():
                                tasks_data[key]["Rebuild"].append(widget.lineEdit_2.text())
                                item = QListWidgetItem(widget.lineEdit_2.text())
                                item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
                                item.setCheckState(Qt.Unchecked)
                                widget.lineEdit_2.clear()
                                widget.listWidget_2.addItem(item)
                            elif widget.lineEdit_3.text():
                                tasks_data[key]["Cosmetic"].append(widget.lineEdit_3.text())
                                item = QListWidgetItem(widget.lineEdit_3.text())
                                item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
                                item.setCheckState(Qt.Unchecked)
                                widget.lineEdit_3.clear()
                                widget.listWidget_3.addItem(item)
            
        with open("tasks_kw.json", "w") as new:
            json.dump(tasks_data, new)
        
    
    

    def checked_tasks(self):
        ''' Returns lists of checked items for construction tasks'''

        user_tasks = {}
        
        for button in self.tasks_button_grp.buttons():
            widget = self.findChild(TasksWidget, "{}_widget".format(button.text()))

            if widget != None:

                construction_area = button.text()

                demo_list = []
                for index in range(widget.listWidget.count()):
                    if widget.listWidget.item(index).checkState() == Qt.Checked:
                        demo_list.append(widget.listWidget.item(index).text())
                rebuild_list = []
                for index in range(widget.listWidget_2.count()):
                    if widget.listWidget_2.item(index).checkState() == Qt.Checked:
                        rebuild_list.append(widget.listWidget_2.item(index).text())
                cosmetic_list = []
                for index in range(widget.listWidget_3.count()):
                    if widget.listWidget_3.item(index).checkState() == Qt.Checked:
                        cosmetic_list.append(widget.listWidget_3.item(index).text())

                user_tasks[construction_area] = {"Demolition": demo_list, "Rebuild": rebuild_list, "Cosmetic": cosmetic_list}
        
        return user_tasks


    def same_address_check(self):
        ''' Input customer address as project name'''      
        
        id = self.get_key(self.full_name_dict, self.customerNameComboBox.currentText())

        address = insert_data_sql.get_customer_address(self.conn, id)

        if self.stackedWidget_3.currentIndex() == 0: #index 0 shows existing customer page
            if self.addressCheckBox.isChecked():
                self.projectNameLineEdit.setText(address)
                self.projectNameLineEdit.setEnabled(False)
            else:
                self.projectNameLineEdit.clear()
                self.projectNameLineEdit.setEnabled(True)
        elif self.stackedWidget_3.currentIndex() == 1: #index 1 shows new customer page
            if self.addressCheckBox.isChecked():
                self.projectNameLineEdit.setText(self.addressLineEdit.text())
                self.projectNameLineEdit.setEnabled(False)
            else:
                self.projectNameLineEdit.clear()
                self.projectNameLineEdit.setEnabled(True)
    
    
    def project_data(self):
        
               
        if self.stackedWidget_3.currentIndex() == 0: #index zero shows exisiting customer page

            customer_id = self.get_key(self.full_name_dict, self.customerNameComboBox.currentText())
            
            new_project = [
                        customer_id, self.projectNameLineEdit.text(),
                        self.begginingDateDateEdit.text(), self.endDateDateEdit.text()
            ]
              
            with self.conn:
                project_id = insert_data_sql.create_new_project(self.conn, new_project)
                task_id = insert_data_sql.add_new_task(self.conn, project_id)


        elif self.stackedWidget_3.currentIndex() == 1: #index 1 shows new customer page

            new_customer = [
                self.firstNamelineEdit.text(), self.lastNamelineEdit.text(), self.phoneLineEdit.text(),
                self.addressLineEdit.text(), self.cityLineEdit.text(), self.zipLineEdit.text()
            ]

            construction_area = []
            for i in range(self.gridLayout_11.count()):
                widget = self.gridLayout_11.itemAt(i).widget()
                if widget.isChecked():
                    construction_area.append(widget.text())

            new_project = [
                self.projectNameLineEdit.text(), self.begginingDateDateEdit.text(),
                self.endDateDateEdit.text()
            ]
            
            with self.conn:
                customer_id = insert_data_sql.add_new_customer(self.conn, new_customer)
                new_project = [customer_id] + new_project
                project_id = insert_data_sql.create_new_project(self.conn, new_project)
                task_id = insert_data_sql.add_new_task(self.conn, project_id)
            

        return customer_id, project_id, task_id 


    def continue_add_material_page(self):
        self.stackedWidget.setCurrentIndex(3)
    

    def save_user_json(self, task_id):

        checked_tasks = self.checked_tasks()

        user_tasks = {
                    "task_id": task_id,
                    "tasks": checked_tasks
                }

        if not os.path.exists("user_tasks.json"):
            with open("user_tasks.json", "w") as f:
                json.dump([user_tasks], f)
        else:
            with open("user_tasks.json", "r") as f:
                user_tasks_data = json.load(f)

            user_tasks_data.append(user_tasks)

            with open("user_tasks.json", "w") as new:
                json.dump(user_tasks_data, new)
    

    def add_material(self):
        '''Add new materials to QTableWidget'''

        material_name = self.materialLineEdit.text()
        material_description = self.materialDescLineEdit.text()
        material_qty = self.materialqtySpinBox.value()
        material_price = self.materialPriceSpinBox.value()
        product_total = material_qty * material_price

        new_material  = [material_name, material_description, material_qty, material_price, product_total]
          
        row = self.materialsTableWidget.rowCount()
        self.materialsTableWidget.setRowCount(row+1)
        col = 0 
        for item in new_material:
            cell = QTableWidgetItem()
            cell.setData(Qt.DisplayRole, item)
            self.materialsTableWidget.setItem(row, col, cell)
            col += 1
        
        self.materialLineEdit.clear()
        self.materialDescLineEdit.clear()
        self.materialqtySpinBox.clear()
        self.materialPriceSpinBox.clear()
        self.materialqtySpinBox.setValue(0)
        self.materialPriceSpinBox.setValue(0)

        # filter_str = 'project_id = {}'.format(self.project_id) #setFilter does not accept placeholders
        # self.model_materials.setFilter(filter_str)   
        # self.model_materials.select()
    
    def cell_changed(self, row, column):
        ''' Adusts total cost when user changes input'''

        if column == 2 and self.materialsTableWidget.item(row, 3) != None: 
            material_qty = self.materialsTableWidget.item(row, column).data(Qt.DisplayRole)
            material_price = self.materialsTableWidget.item(row, 3).data(Qt.DisplayRole)
            material_total = material_qty * material_price
            item = QTableWidgetItem()
            item.setData(Qt.DisplayRole, material_total)
            self.materialsTableWidget.setItem(row, 4, item)    
        elif column == 3 and self.materialsTableWidget.item(row, 2) != None:
            material_qty = self.materialsTableWidget.item(row, 2).data(Qt.DisplayRole)
            material_price = self.materialsTableWidget.item(row, column).data(Qt.DisplayRole)
            material_total = material_qty * material_price
            item = QTableWidgetItem()
            item.setData(Qt.DisplayRole, material_total)
            self.materialsTableWidget.setItem(row, 4, item)

        overall_total = 0
        for row in range(self.materialsTableWidget.rowCount()):
            if column == 4 and self.materialsTableWidget.item(row, 4) != None:
                value = self.materialsTableWidget.item(row, 4).data(Qt.DisplayRole)
                overall_total += value
                self.totalCostLabel.setText('${}'.format(overall_total))




    def retrieve_table_data(self, project_id):
        '''Retrieve data from QTableWidget for storage on database'''
        for row in range(self.materialsTableWidget.rowCount()):
            new_material = [project_id]
            for column in range(self.materialsTableWidget.columnCount()):
                item = self.materialsTableWidget.item(row, column)
                new_material.append(item.data(Qt.DisplayRole))
            with self.conn:
                insert_data_sql.add_materials(self.conn, new_material)

    def finish_save_project(self):

        customer_id, project_id, task_id = self.project_data()
        self.save_user_json(task_id)
        self.retrieve_table_data(project_id)
        #1st method
        #self.project_estimate = ProjectEstimate()
        #self.project_estimate.show()
        #2nd method
        #self.parent().setMyCentral(ProjectEstimate)
        #3rd method
        #self.main_window_connection.EstimatePageSignal.emit()
        self.EstimatePageSignal.emit(customer_id, project_id, task_id)
        



        

#Create dialog box to save new customer and project
class SaveDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        QBtn = QDialogButtonBox.Save | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Do you wish to save new changes?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

class TasksWidget(QWidget, Ui_task_widget):
    def __init__(self, name,  parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.setObjectName(name)
