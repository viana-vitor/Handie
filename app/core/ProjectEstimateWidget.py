
import sys
import json
import sqlite3
import os

from PySide6.QtCore import Qt, QThreadPool, Signal
from PySide6.QtWidgets import (QWidget, QListWidgetItem, QButtonGroup, QHBoxLayout, QLabel, QPushButton, QHeaderView,
 QLineEdit, QSpinBox, QDoubleSpinBox, QVBoxLayout, QMessageBox, QTextEdit)
from PySide6.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery, QSqlTableModel
import app.data.database.insert_data_sql as insert_data_sql

from app.ui.Ui_customer_estimate import Ui_Form
from app.ui.Ui_construction_summary_wdg import Ui_Form as Ui_construction_tasks
from app.ui.Ui_tasks_writeup import Ui_Form as Ui_tasks_writeup
from app.core.EstimatePDFGenerator import Generator as Generator

db = QSqlDatabase("QSQLITE")
db.setDatabaseName("app/data/database/customer_data.db")
db.open()

class ProjectEstimate(QWidget, Ui_Form):

    HomeWidgetSignal = Signal() #Signal to go back to home page

    def __init__(self, customer_id, project_id, task_id, source):
        super().__init__()
        self.setupUi(self)
        self.show()

        #Database keys for current project
        self.customer_id = customer_id
        self.project_id = project_id
        self.task_id = task_id
        self.source = source

        self.threadpool = QThreadPool()
        
        #Total cost variables
        self.total_labor_cost = 0
        self.total_fee_amount = 0
        self.total_tax = 0
        self.total_cost = 0
        self.labor_list = []
        self.fee_list = []
        
        database = r"app/data/database/customer_data.db" #Database path
        self.conn = insert_data_sql.create_connection(database) #Creates database connection
        with self.conn:
            self.customer_data = insert_data_sql.get_customer_data(self.conn, self.customer_id) #Customer data
        
        self.customerDataLabel.setText(self.customer_data[0])
        self.phoneDataLabel.setText(str(self.customer_data[1]))
        self.addressDataLabel.setText(str(self.customer_data[2]))
        self.cityDataLabel.setText(self.customer_data[3])
        self.zipDataLabel.setText(str(self.customer_data[4]))
  
        self.construction_area_widgets()
        self.tasks_writeup()

        self.addFeepushButton.clicked.connect(self.add_fee)
        self.addLaborPushButton.clicked.connect(self.add_labor)
        self.addTaxPushButton.clicked.connect(self.add_tax)

        
        ## Set up table with construction materials
        self.materialsTableView.hide()

        headers = ["Project ID", "Material", "Description", "Quantity", "Price ($)", "Total ($)"]
        self.model_materials = QSqlTableModel(db=db)
        self.model_materials.setTable('materials')
        filter_str = 'project_id = {}'.format(self.project_id)
        self.model_materials.setFilter(filter_str)
        self.model_materials.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model_materials.select()
        self.materialsTableView.setModel(self.model_materials)
        for i in range(len(headers)):
            self.model_materials.setHeaderData(i, Qt.Horizontal, headers[i])
        self.materialsTableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.showMaterialButton.clicked.connect(self.show_hide_materials)
        self.addMaterialButton.clicked.connect(self.add_material)

        self.get_materials_total()
        self.get_fee_from_database(self.conn, self.project_id)
        self.get_labor_from_database(self.conn, self.project_id)
        self.get_total_cost()
        self.populate_client_version()

        self.estimateMaterialSpinBox.valueChanged.connect(self.estimate_version_changed)
        self.estimateLaborSpinBox.valueChanged.connect(self.estimate_version_changed)
        self.estimateFeeSpinBox.valueChanged.connect(self.estimate_version_changed)
        self.estimateTaxSpinBox.valueChanged.connect(self.estimate_version_changed)

        self.pdfPushButton.clicked.connect(self.generate_pdf)
        self.closePushButton.clicked.connect(self.close_estimate)

    
    def construction_area_widgets(self):
        ''' This function populates the construction area part of the estimate with all the tasks for the project'''
        
        with open("app/data/database/user_tasks.json", "r") as f:
            user_tasks = json.load(f)
        
        index = 7
        for dict in user_tasks[::-1]:
            if dict["task_id"] == self.task_id:
                for area in dict["tasks"].keys():
                    self.new_widget = TasksSummaryWidget("{}".format(area))
                    self.constructionTasksLayout = QVBoxLayout()
                    self.constructionTasksLayout.addWidget(self.new_widget)
                    self.verticalLayout_12.insertLayout(index, self.constructionTasksLayout)
                    index += 1
                    self.new_widget.label.setText(area)
                    for task in dict["tasks"][area]:
                        if task == "Demolition":
                            for value in dict['tasks'][area][task]:
                                item = QListWidgetItem(value)
                                self.new_widget.listWidget.addItem(item)
                        elif task == "Rebuild":
                            for value in dict['tasks'][area][task]:
                                item = QListWidgetItem(value)
                                self.new_widget.listWidget_2.addItem(item)
                        elif task == "Cosmetic":
                            for value in dict['tasks'][area][task]:
                                item = QListWidgetItem(value)
                                self.new_widget.listWidget_3.addItem(item)


    def add_labor(self):

        index = 0
        
        nbr_of_workers = self.nbrWorkersSpinBox.value()
        worker_rate = self.workerRateDoubleSpinBox.value()
        
        if self.durationComboBox.currentText() == 'Days':
            nbr_of_days = self.durationSpinBox.value()
        elif self.durationComboBox.currentText() == 'Months':
            nbr_of_months = self.durationSpinBox.value()
            nbr_of_days = 22 * nbr_of_months #Assuming a 5 day work week with 22 work days in a month
        
        self.labor_list.append((nbr_of_workers, worker_rate, nbr_of_days))

        self.laborHorizontalLayout = QHBoxLayout()
        self.nworkers_label = QLabel('{}'.format(nbr_of_workers))
        self.extra_label = QLabel('workers at')
        self.rate_label = QLabel('${}/hr'.format(worker_rate))
        self.duration_label = QLabel('for {} days'.format(nbr_of_days))
        self.laborHorizontalLayout.addWidget(self.nworkers_label)
        self.laborHorizontalLayout.addWidget(self.extra_label)
        self.laborHorizontalLayout.addWidget(self.rate_label)
        self.laborHorizontalLayout.addWidget(self.duration_label)
        self.verticalLayout_4.insertLayout(index, self.laborHorizontalLayout)


        self.get_labor_total(nbr_of_workers, worker_rate, nbr_of_days)
        self.get_total_cost()
        self.populate_client_version()

        self.nbrWorkersSpinBox.setValue(0)
        self.workerRateDoubleSpinBox.setValue(0)
        self.durationSpinBox.setValue(0)
    
    
    def get_labor_total(self, wkrs, rate, duration):

        hours = duration * 8 #Assuming an 8hr work day 
        total_labor = wkrs * rate * hours
        self.total_labor_cost += total_labor
        self.laborSpinBox.setValue(self.total_labor_cost)
    
    def get_labor_from_database(self, conn, project_id):

        sql = '''SELECT nbr_workers, rate, duration, labor_cost FROM labor
                    WHERE project_id = ?'''
        
        cur = conn.cursor()
        cur.execute(sql, [project_id])
        labor_data = cur.fetchall()

        index= 0
        total_labor = 0
        for labor in labor_data:
            total_labor += labor[3]
            self.laborHorizontalLayout = QHBoxLayout()
            self.nworkers_label = QLabel('{}'.format(labor[0]))
            self.extra_label = QLabel('workers at')
            self.rate_label = QLabel('${}/hr'.format(labor[1]))
            self.duration_label = QLabel('for {} days'.format(labor[2]))
            self.laborHorizontalLayout.addWidget(self.nworkers_label)
            self.laborHorizontalLayout.addWidget(self.extra_label)
            self.laborHorizontalLayout.addWidget(self.rate_label)
            self.laborHorizontalLayout.addWidget(self.duration_label)
            self.verticalLayout_4.insertLayout(index, self.laborHorizontalLayout)
        
        self.total_labor_cost += total_labor
        self.laborSpinBox.setValue(self.total_labor_cost)

    
    def add_fee(self):

        index = 0

        name = self.newFeeNameLineEdit.text()
        self.feeHorizontalLayout = QHBoxLayout()
        self.feeName = QLabel('{}:'.format(name))
        self.feeHorizontalLayout.addWidget(self.feeName)
    
        amount = self.addFeeSpinBox.value()
        self.amount = QLabel("${}".format(amount))
        self.feeHorizontalLayout.addWidget(self.amount)
        self.newFeeNameLineEdit.clear()
        self.addFeeSpinBox.setValue(0)
    
        self.delButton = QPushButton("-")
        self.delButton.setFlat(True)
        self.feeHorizontalLayout.addWidget(self.delButton)
        self.verticalLayout_6.insertLayout(index, self.feeHorizontalLayout)

        self.fee_list.append((name, amount))
        self.total_fee_amount += amount
        self.feeSpinBox.setValue(self.total_fee_amount)

        self.get_total_cost()
        self.populate_client_version()



    def get_fee_from_database(self, conn, project_id):

        sql = ''' SELECT fee_name, fee_amount FROM fees
                    WHERE project_id = ?'''
        
        cur = conn.cursor()
        cur.execute(sql, [project_id])
        fees = cur.fetchall()

        index = 0
        total = 0
        for fee in fees:
            total += fee[1]
            self.feeHorizontalLayout = QHBoxLayout()
            self.feeName = QLabel('{}:'.format(fee[0]))
            self.feeHorizontalLayout.addWidget(self.feeName)
            self.amount = QLabel("${}".format(fee[1]))
            self.feeHorizontalLayout.addWidget(self.amount)
            self.delButton = QPushButton("-")
            self.delButton.setFlat(True)
            self.feeHorizontalLayout.addWidget(self.delButton)
            self.verticalLayout_6.insertLayout(index, self.feeHorizontalLayout)

        self.total_fee_amount += total #Add total fee from database
        self.feeSpinBox.setValue(self.total_fee_amount)
        

    def add_tax(self):

        index = 0

        name = self.newTaxNameLineEdit.text()
        self.newTaxNameLineEdit.clear()
        self.taxHorinzontalLayout = QHBoxLayout()
        self.taxName = QLabel('{}:'.format(name))
        self.taxHorinzontalLayout.addWidget(self.taxName)
        
        rate = self.newTaxdoubleSpinBox.value()
        self.rate = QLabel('{}%'.format(rate))
        self.newTaxdoubleSpinBox.setValue(0)
        
        self.delTaxButton = QPushButton('-')
        self.delTaxButton.setFlat(True)
        
        self.taxHorinzontalLayout.addWidget(self.rate)
        self.taxHorinzontalLayout.addWidget(self.delTaxButton)
        self.verticalLayout_9.insertLayout(index, self.taxHorinzontalLayout)
        self.get_total_tax(rate)
        self.get_total_cost()
        self.populate_client_version()

    def get_total_tax(self, pctg):

        self.total_tax = pctg/100 * (self.total_labor_cost + self.overall_materials_cost)
        self.taxSpinBox.setValue(self.total_tax)


    def show_hide_materials(self):
        
        if self.showMaterialButton.isChecked():
            self.materialsTableView.show()
        else:
            self.materialsTableView.hide()
        
    
    def add_material(self):

        material_name = self.newMaterialLineEdit.text()
        material_description = self.descMaterialLineEdit.text()
        qty_material = self.qtyMaterialSpinBox.value()
        price_material = self.priceMaterialSpinBox.value()
        total = qty_material * price_material

        new_material = [self.project_id, material_name, material_description, qty_material, price_material, total]

        with self.conn:
            insert_data_sql.add_materials(self.conn, new_material)

        self.model_materials.select()
        self.get_materials_total()
        self.get_total_cost()
        self.populate_client_version()

        self.newMaterialLineEdit.clear()
        self.descMaterialLineEdit.clear()
        self.qtyMaterialSpinBox.setValue(0)
        self.priceMaterialSpinBox.setValue(0)

    def get_materials_total(self):

        sql = 'SELECT total FROM materials WHERE project_id = ?'

        with self.conn:
            cur = self.conn.cursor()
            cur.execute(sql, [self.project_id])
            rows = cur.fetchall()

            self.overall_materials_cost = 0
            for value in rows:
                self.overall_materials_cost += value[0]
            self.materialsSpinBox.setValue(self.overall_materials_cost)

    def get_total_cost(self):
        '''Add total cost value to spinbox'''
        self.total_cost = (self.overall_materials_cost + self.total_labor_cost + 
                self.total_fee_amount + self.total_tax)
        
        self.totalCostSpinBox.setValue(self.total_cost)

    
    def tasks_writeup(self):
        '''Add textEdit to the page for writing project tasks'''
         
        with open("app/data/database/user_tasks.json", "r") as f:
            user_tasks = json.load(f)
        
        index = 22
        for dict in user_tasks[::-1]:
            if dict["task_id"] == self.task_id:
                for area in dict["tasks"].keys():
                    self.task_text_widget = TasksWriteUp('{}_writeup'.format(area)) #Generate custom text edit according to project's construction area 
                    self.verticalLayout_12.insertWidget(index, self.task_text_widget)
                    index += 1
                    self.task_text_widget.label.setText(area + ":")

        if self.source == 'EstimateWidget': #Load previous entered text if coming from list of estimates on EstimateWidget
            with open("app/data/database/tasks_writeup.json", "r") as g:
                tasks_writeup = json.load(g)
            
            for dict in tasks_writeup[::-1]:
                if dict["task_id"] == self.task_id:
                    for task in dict['job_tasks'].items():
                        widget = self.findChild(TasksWriteUp, '{}_writeup'.format(task[0]))
                        widget.textEdit.setText(task[1])
                    self.generalCondTextEdit.setText(dict['general_conditions'])
        else:
            pass


    
    def get_tasks_writeup(self):
        '''Get text from tasks textEdits '''

        with open("app/data/database/user_tasks.json", "r") as f:
            user_tasks = json.load(f)

        tasks = {}
        for dict in user_tasks[::-1]:
            if dict['task_id'] == self.task_id:
                for area in dict['tasks'].keys():
                    widget = self.findChild(TasksWriteUp, '{}_writeup'.format(area))

                    tasks[area] = widget.textEdit.toPlainText()
        
        
        if self.source == 'HomeWidget':
            ##Save new data if coming from homewidget
            tasks_input = {
                "task_id": self.task_id,
                "job_tasks": tasks,
                "general_conditions": self.generalCondTextEdit.toPlainText()
            }
            
            if not os.path.exists("app/data/database/tasks_writeup.json"):
                with open("app/data/database/tasks_writeup.json", "w") as f:
                    tasks_writeup = json.dump([tasks_input], f)
            else:
                with open("app/data/database/tasks_writeup.json", "r") as f:
                    tasks_writeup = json.load(f)
                
                tasks_writeup.append(tasks_input)

                with open("app/data/database/tasks_writeup.json", "w") as new:
                    json.dump(tasks_writeup, new)
        else:
            ##Rewrite data if there is any changes
            with open("app/data/database/tasks_writeup.json", "r") as f: 
                tasks_writeup = json.load(f)
            
            for dict in tasks_writeup[::-1]:
                if dict["task_id"] == self.task_id:
                    for item in dict["job_tasks"].items():
                        if tasks[item[0]] != item[1]:
                            dict['job_tasks'][item[0]] = tasks[item[0]]
                    dict['general_conditions'] = self.generalCondTextEdit.toPlainText()
            
            with open("app/data/database/tasks_writeup.json", "w") as new:
                json.dump(tasks_writeup, new)
        

        return tasks
    
    
    def save_costs(self):

        for i in self.labor_list:
            nbr_of_workers = i[0]
            worker_rate = i[1]
            nbr_of_days = i[2]
            hours = nbr_of_days * 8 #Assuming an 8hr work shift
            labor_cost = nbr_of_workers * worker_rate * hours
            with self.conn:
                insert_data_sql.add_labor(self.conn, [self.project_id, nbr_of_workers, worker_rate, nbr_of_days, labor_cost])
        
        for i in self.fee_list:
            fee_name = i[0]
            fee_amount = i[1]
            with self.conn:
                insert_data_sql.add_fee(self.conn, [self.project_id, fee_name, fee_amount])
    
    def populate_client_version(self):
        
        if self.source == 'HomeWidget':
            self.estimateMaterialSpinBox.setValue(self.overall_materials_cost)
            self.estimateLaborSpinBox.setValue(self.total_labor_cost)
            self.estimateFeeSpinBox.setValue(self.total_fee_amount)
            self.estimateTaxSpinBox.setValue(self.total_tax)
            self.estimateTotalCostSpinBox.setValue(self.total_cost)
        else:
            sql = '''SELECT material_cost, labor_cost, fee_cost, tax_cost, total_cost FROM estimates
                    WHERE project_id = ?'''
            
            cur = self.conn.cursor()
            cur.execute(sql, [self.project_id])
            estimates = cur.fetchall()[0]

            self.estimateMaterialSpinBox.setValue(estimates[0])
            self.estimateLaborSpinBox.setValue(estimates[1])
            self.estimateFeeSpinBox.setValue(estimates[2])
            self.estimateTaxSpinBox.setValue(estimates[3])
            self.estimateTotalCostSpinBox.setValue(estimates[4])

    
    def estimate_version_changed(self):
        '''Update estimate total'''

        client_total = (self.estimateMaterialSpinBox.value() + self.estimateLaborSpinBox.value() + 
            self.estimateFeeSpinBox.value() + self.estimateTaxSpinBox.value())

        self.estimateTotalCostSpinBox.setValue(client_total)

    def save_client_version(self):
        '''Save values used to produce customer estimate report'''

        if self.source == 'HomeWidget':
            estimate = [self.project_id, self.estimateMaterialSpinBox.value(), self.estimateLaborSpinBox.value(),
                self.estimateFeeSpinBox.value(), self.estimateTaxSpinBox.value(), self.estimateTotalCostSpinBox.value()]

            with self.conn:
                insert_data_sql.add_client_estimate(self.conn, estimate)
        
        else:

            sql = ''' UPDATE estimates
                        SET material_cost = {material_cost}, 
                            labor_cost = {labor_cost},
                            fee_cost = {fee_cost},
                            total_cost = {total_cost}
                        WHERE project_id = ?'''.format(material_cost = self.estimateMaterialSpinBox.value(),
                                                        labor_cost = self.estimateLaborSpinBox.value(),
                                                        fee_cost = self.estimateFeeSpinBox.value(),
                                                        total_cost = self.estimateTotalCostSpinBox.value())

            cur = self.conn.cursor()
            cur.execute(sql, [self.project_id])
            self.conn.commit()
    
    
    def close_estimate(self):
        '''Leave the estimate page'''
        
        msgBox = QMessageBox()
        msgBox.setText("Do you wish to save changes?")
        msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Save)
        msgBox.setIcon(QMessageBox.Information)
        button = msgBox.exec()

        if self.source == 'HomeWidget': #if estimate page was open right after adding new project
            if button == QMessageBox.Save:
                self.save_costs()
                self.save_client_version()
                self.get_tasks_writeup()
                self.HomeWidgetSignal.emit()
            elif button == QMessageBox.Discard:
                self.HomeWidgetSignal.emit()
            else:
                #stay on page
                pass
        else: #if estimate page was opend directly from list of projects on estimate widget
            if button == QMessageBox.Save:
                self.save_costs()
                self.save_client_version()
                self.get_tasks_writeup()
                self.close()
            elif button == QMessageBox.Discard:
                self.close()
            else:
                #stay on page
                pass

    
    
    def generate_pdf(self):
        ''' Saves project info and start thread for pdf generation'''

        self.save_costs()
        self.save_client_version()
        tasks_writeup = self.get_tasks_writeup()

        self.pdfPushButton.setDisabled(True)
        #Data for pdf generation
        data = {
            "customer_name": self.customer_data[0],
            "phone": self.customer_data[1],
            "address": self.customer_data[2],
            "city":self.customer_data[3],
            'construction_tasks': tasks_writeup,
            'general_conditions': self.generalCondTextEdit.toPlainText(),
            'estimate_total': self.estimateTotalCostSpinBox.text()
        }

        g = Generator(data) #call worker thread passing the data
        g.signals.file_saved_as.connect(self.pdf_generated)
        g.signals.error.connect(print) #Print errors to the console
        self.threadpool.start(g)
    
    def pdf_generated(self, outfile):

        try:
            os.startfile(outfile)
        except Exception:
            # If startfile not available, show dialog.
            QMessageBox.information(self, "Finished", "PDF has been generated")
            if self.source == 'HomeWidget': #if from homewidget go back home
                self.HomeWidgetSignal.emit()
            else:
                self.close() #if from estimates close estimate


class TasksSummaryWidget(QWidget, Ui_construction_tasks):
    def __init__(self, name, parent = None):
        super().__init__(parent)
        self.setupUi(self)

        self.setObjectName(name)

class TasksWriteUp(QWidget, Ui_tasks_writeup):
    def __init__(self, name, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.setObjectName(name)