import json

from PySide6.QtCore import Qt, Signal, QSize
from PySide6.QtWidgets import (QWidget, QLabel, QListWidgetItem, QHBoxLayout)

from app.ui.Ui_estimate_widget import Ui_Form as Ui_estimates
from app.core.ProjectEstimateWidget import ProjectEstimate
import app.data.database.insert_data_sql as insert_data_sql



class EstimateWidget(QWidget, Ui_estimates):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        database = r"app/data/database/customer_data.db" #Database path
        self.conn = insert_data_sql.create_connection(database)

        with self.conn:
            self.project_list = insert_data_sql.get_project_customer_name(self.conn)
        
        for project_id, customer_id, project_name, customer_name, status in self.project_list:
            myItemWidget = CustomListItem()
            myItemWidget.project_id(project_id)
            myItemWidget.customer_id(customer_id)
            task_id = insert_data_sql.get_task_id(self.conn, project_id)
            myItemWidget.task_id(task_id)
            myItemWidget.setProject(project_name)
            myItemWidget.setCustomer(customer_name)
            myItemWidget.setInfo('<br/>'.join("{}".format(i) for i in self.get_info(self.conn, customer_id)))
            myItemWidget.setJob('<br/>'.join("{}".format(i) for i in self.get_construction_area(task_id)))
            myItemWidget.setStatus(status)


            listWidgetItem = QListWidgetItem(self.listWidget)
            listWidgetItem.setSizeHint(QSize(30, 70))

            self.listWidget.addItem(listWidgetItem)
            self.listWidget.setItemWidget(listWidgetItem, myItemWidget)
        
        self.listWidget.itemClicked.connect(self.open_estimate)

        self.lineEdit.textChanged.connect(self.on_text_changed)


    def open_estimate(self, item):
        '''Retrieve primary keys, and send to it to estimate page. Open estimate page'''

        itemWidget = self.listWidget.itemWidget(item) # get custom widget from list item
        customer_id = itemWidget.customer_id
        project_id = itemWidget.project_id
        task_id = itemWidget.task_id

        self.project_estimate = ProjectEstimate(customer_id, project_id, task_id)
        self.project_estimate.show()

    def get_construction_area(self, task_id):

        with open("app/data/database/user_tasks.json", "r") as f:
            user_tasks = json.load(f)

        
        for dict in user_tasks[::-1]:
            if dict['task_id'] == task_id:
                area = dict['tasks'].keys()
        
        return area

    def get_info(self, conn, customer_id):

        sql = '''SELECT address, city, phone FROM customer
                WHERE id = ?'''
        
        cur = conn.cursor()
        cur.execute(sql, [customer_id])
        info = cur.fetchall()[0]
        return info


    def on_text_changed(self, text):
        '''Filter list using customer or project name'''
        for row in range(self.listWidget.count()):
            item = self.listWidget.item(row)
            widg = self.listWidget.itemWidget(item)
            if text.lower() in widg.customerText.text().lower():
                item.setHidden(False)
            elif text.lower() in widg.projectText.text().lower():
                item.setHidden(False)
            else:
                item.setHidden(True)


class CustomListItem(QWidget):
    def __init__(self):
        super().__init__()

        self.textLayout = QHBoxLayout()
        self.projectText = QLabel()
        self.projectText.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.projectText.setWordWrap(True)
        self.customerText = QLabel()
        self.customerText.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.customerText.setWordWrap(True)
        self.infoText = QLabel()
        self.infoText.setTextFormat(Qt.RichText)
        self.infoText.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.jobText = QLabel()
        self.jobText.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.jobText.setTextFormat(Qt.RichText)
        self.statusText = QLabel()
        self.statusText.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) 
        
        self.textLayout.addWidget(self.projectText)
        self.textLayout.addWidget(self.customerText)
        self.textLayout.addWidget(self.infoText)
        self.textLayout.addWidget(self.jobText)
        self.textLayout.addWidget(self.statusText)
        self.setLayout(self.textLayout)
    
    def project_id(self, project_id):
        self.project_id = project_id

    def customer_id(self, customer_id):
        self.customer_id = customer_id
    
    def task_id(self, task_id):
        self.task_id = task_id
    
    def setProject(self, text):
        self.projectText.setText(text)
    
    def setCustomer(self, text):
        self.customerText.setText(text)
    
    def setInfo(self, text):
        self.infoText.setText(text)
    
    def setJob(self, text):
        self.jobText.setText(text)
    
    def setStatus(self, text):
        self.statusText.setText(text)




