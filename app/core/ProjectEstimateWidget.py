
import sys
import json
import sqlite3

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QListWidgetItem, QButtonGroup, QHBoxLayout, QLabel, QPushButton, QHeaderView, QLineEdit, QSpinBox, QDoubleSpinBox, QVBoxLayout
from PySide6.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery, QSqlTableModel
import app.data.database.insert_data_sql as insert_data_sql

from app.ui.Ui_customer_estimate import Ui_Form
from app.ui.Ui_construction_summary_wdg import Ui_Form as Ui_construction_tasks

db = QSqlDatabase("QSQLITE")
db.setDatabaseName("app/data/database/customer_data.db")
db.open()

class ProjectEstimate(QWidget, Ui_Form): 
    def __init__(self, customer_id, project_id, task_id):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.customer_id = customer_id
        self.project_id = project_id
        self.task_id = task_id
        
        self.total_labor_cost = 0
        self.total_fee_amount = 0
        self.total_tax = 0
        
        database = r"app/data/database/customer_data.db" #Database path
        self.conn = insert_data_sql.create_connection(database) #Creates database connection
        with self.conn:
            self.customer_data = insert_data_sql.get_customer_data(self.conn, self.customer_id)
        
        self.customerDataLabel.setText(self.customer_data[0])
        #self.emailDataLabel
        self.phoneDataLabel.setText(str(self.customer_data[1]))
        self.addressDataLabel.setText(str(self.customer_data[2]))
        self.cityDataLabel.setText(self.customer_data[3])
        self.zipDataLabel.setText(str(self.customer_data[4]))
  
        self.construction_area_widgets()


        # self.contractor_new_fee_group = QButtonGroup()
        # self.contractor_new_fee_group.addButton(self.pctgNewFeeRadioButton)
        # self.contractor_new_fee_group.addButton(self.amntNewFeeRadioButton)

        #self.pctgNewFeeRadioButton.setChecked(True)
        
        # self.newFeeLineEdit.hide()
        # self.newFeeDoubleSpinBox.show()

        # self.pctgNewFeeRadioButton.toggled.connect(self.show_new_fee)
        # self.amntNewFeeRadioButton.toggled.connect(self.show_new_fee)

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

        self.get_materials_total()
        self.get_total_cost()

        self.showMaterialButton.clicked.connect(self.show_hide_materials)
        self.addMaterialButton.clicked.connect(self.add_material)

        self.pushButton.clicked.connect(self.customer_info)

    def customer_info(self):
        print(self.customer_data)
    
    def construction_area_widgets(self):
        
        with open("app/data/database/user_tasks.json", "r") as f:
            user_tasks = json.load(f)
        
        index = 4
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
            nbr_of_days = 24 * nbr_of_months #Assuming 4 week month with 6 days work week

        self.laborHorizontalLayout = QHBoxLayout()
        self.nworkers_label = QLabel('{}'.format(nbr_of_workers))
        self.extra_label = QLabel('workers at')
        self.rate_label = QLabel('${}/hr'.format(worker_rate))
        self.duration_label = QLabel('{} days'.format(nbr_of_days))
        self.laborHorizontalLayout.addWidget(self.nworkers_label)
        self.laborHorizontalLayout.addWidget(self.extra_label)
        self.laborHorizontalLayout.addWidget(self.rate_label)
        self.laborHorizontalLayout.addWidget(self.duration_label)
        self.verticalLayout_4.insertLayout(index, self.laborHorizontalLayout)


        self.get_labor_total(nbr_of_workers, worker_rate, nbr_of_days)
        self.get_total_cost()

        self.nbrWorkersSpinBox.setValue(0)
        self.workerRateDoubleSpinBox.setValue(0)
        self.durationSpinBox.setValue(0)
    
    
    def get_labor_total(self, wkrs, rate, duration):

        hours = duration * 8 #Assuming an 8hr work day 
        total_labor = wkrs * rate * hours
        self.total_labor_cost += total_labor
        self.label_11.setText('${}'.format(self.total_labor_cost))

    
    # def show_new_fee(self):
        
    #     if self.pctgNewFeeRadioButton.isChecked():
    #         self.newFeeLineEdit.hide()
    #         self.newFeeDoubleSpinBox.show()
    #     elif self.amntNewFeeRadioButton.isChecked():
    #         self.newFeeDoubleSpinBox.hide()
    #         self.newFeeLineEdit.show()
 
    
    def add_fee(self):

        index = 0

        name = self.newFeeNameLineEdit.text()
        self.feeHorizontalLayout = QHBoxLayout()
        self.feeName = QLabel('{}:'.format(name))
        self.feeHorizontalLayout.addWidget(self.feeName)
    
        amount = int(self.newFeeLineEdit.text())
        self.amount = QLabel("${}".format(amount))
        self.feeHorizontalLayout.addWidget(self.amount)
        self.newFeeNameLineEdit.clear()
        self.newFeeLineEdit.clear()
    
        self.delButton = QPushButton("-")
        self.delButton.setFlat(True)
        self.feeHorizontalLayout.addWidget(self.delButton)
        self.verticalLayout_6.insertLayout(index, self.feeHorizontalLayout)
        self.get_total_fee(amount)
        self.get_total_cost()



    def get_total_fee(self, amount):

        self.total_fee_amount += amount
        self.label_16.setText('${}'.format(self.total_fee_amount))


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

    def get_total_tax(self, pctg):

        self.total_tax = pctg/100 * (self.total_labor_cost + self.overall_materials_cost)
        self.label_19.setText('${}'.format(self.total_tax))


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
            self.label_5.setText('${}'.format(self.overall_materials_cost))

    def get_total_cost(self):

        total_cost = (self.overall_materials_cost + self.total_labor_cost + 
                self.total_fee_amount + self.total_tax)
        
        self.label_20.setText('${}'.format(total_cost))



class TasksSummaryWidget(QWidget, Ui_construction_tasks):
    def __init__(self, name, parent = None):
        super().__init__(parent)
        self.setupUi(self)

        self.setObjectName(name)

