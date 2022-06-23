import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PySide6.QtWidgets import ( QDialogButtonBox, QFormLayout, QGridLayout, QHBoxLayout, QLabel,
QLineEdit, QMainWindow, QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout, QWidget,
QPushButton, QDialog, QDialogButtonBox
)

db = QSqlDatabase("QSQLITE")
db.setDatabaseName("customer_data.db")
db.open()

class addCustomerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(358, 375)
        
        layout = QVBoxLayout()

        grid = QGridLayout()
        

        #Add line edit and label to grid layout
        self.firstName = QLineEdit()
        grid.addWidget(self.firstName, 0, 1, 1, 1)
        self.label = QLabel("First Name:")
        grid.addWidget(self.label, 0, 0, 1, 1)
        
        self.lastName = QLineEdit()
        grid.addWidget(self.lastName, 1, 1, 1, 1)
        self.label_2 = QLabel("Last Name:")
        grid.addWidget(self.label_2, 1, 0, 1, 1)

        self.phoneNumber = QLineEdit()
        grid.addWidget(self.phoneNumber, 2, 1, 1, 1)
        self.label_3 = QLabel("Phone #:")
        grid.addWidget(self.label_3, 2, 0, 1, 1)

        self.address = QLineEdit()
        grid.addWidget(self.address, 3, 1, 1, 1)
        self.label_4 = QLabel("Address:")
        grid.addWidget(self.label_4, 3, 0, 1, 1)

        self.city = QLineEdit()
        grid.addWidget(self.city, 4, 1, 1, 1)
        self.label_5 = QLabel("City:")
        grid.addWidget(self.label_5, 4, 0, 1, 1)

        self.zipCode = QLineEdit()
        grid.addWidget(self.zipCode, 5, 1, 1, 1)
        self.label_6 = QLabel("Zip Code:")
        grid.addWidget(self.label_6, 5, 0, 1, 1)

        layout.addLayout(grid)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(self.verticalSpacer)


        #Creates the query
        self.query = QSqlQuery(db=db)
        self.query.prepare(
            "INSERT INTO customer (first_name, last_name, phone, address, city, zip) " 
            "VALUES (:first_name, :last_name, :phone, :address, :city, :zip)")
        

        self.setMinimumSize(QSize(200, 200))

        controls = QHBoxLayout()

        save_rec = QPushButton("Save")
        save_rec.clicked.connect(self.update_query) #Connects button to update query function

        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.close)


        controls.addWidget(cancel_btn)
        controls.addWidget(save_rec)


        layout.addLayout(controls)

        #widget = QWidget()
        #widget.setLayout(layout)
        #self.setCentralWidget(widget)
        self.setLayout(layout)

    def update_query(self):

        dlg = CustomDialog()

        if dlg.exec(): # Execute the query when pressed to save
            self.query.bindValue(":first_name", self.firstName.text())
            self.query.bindValue(":last_name", self.lastName.text())
            self.query.bindValue(":phone", self.phoneNumber.text())
            self.query.bindValue(":address", self.address.text())
            self.query.bindValue(":city", self.city.text())
            self.query.bindValue(":zip", self.zipCode.text())
            self.query.exec()
            self.close()

        else:
            print('cancel')

#Create dialog box to save new customer
class CustomDialog(QDialog):
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


# app = QApplication(sys.argv)
# window = addCustomerWindow()
# window.show()
# app.exec()
