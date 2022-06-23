# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addProject.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(481, 413)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.nameLineEdit = QLineEdit(self.centralwidget)
        self.nameLineEdit.setObjectName(u"nameLineEdit")

        self.gridLayout.addWidget(self.nameLineEdit, 0, 1, 1, 1)

        self.begginingDateLabel = QLabel(self.centralwidget)
        self.begginingDateLabel.setObjectName(u"begginingDateLabel")

        self.gridLayout.addWidget(self.begginingDateLabel, 2, 0, 1, 1)

        self.nameLabel = QLabel(self.centralwidget)
        self.nameLabel.setObjectName(u"nameLabel")

        self.gridLayout.addWidget(self.nameLabel, 0, 0, 1, 1)

        self.endDateDateEdit = QDateEdit(self.centralwidget)
        self.endDateDateEdit.setObjectName(u"endDateDateEdit")

        self.gridLayout.addWidget(self.endDateDateEdit, 3, 1, 1, 1)

        self.endDateLabel = QLabel(self.centralwidget)
        self.endDateLabel.setObjectName(u"endDateLabel")

        self.gridLayout.addWidget(self.endDateLabel, 3, 0, 1, 1)

        self.begginingDateDateEdit = QDateEdit(self.centralwidget)
        self.begginingDateDateEdit.setObjectName(u"begginingDateDateEdit")

        self.gridLayout.addWidget(self.begginingDateDateEdit, 2, 1, 1, 1)

        self.customerLabel = QLabel(self.centralwidget)
        self.customerLabel.setObjectName(u"customerLabel")

        self.gridLayout.addWidget(self.customerLabel, 1, 0, 1, 1)

        self.customerLineEdit = QLineEdit(self.centralwidget)
        self.customerLineEdit.setObjectName(u"customerLineEdit")

        self.gridLayout.addWidget(self.customerLineEdit, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox_3 = QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout_2.addWidget(self.checkBox_3, 0, 2, 1, 1)

        self.checkBox_5 = QCheckBox(self.centralwidget)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.gridLayout_2.addWidget(self.checkBox_5, 1, 0, 1, 1)

        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.checkBox_6 = QCheckBox(self.centralwidget)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.gridLayout_2.addWidget(self.checkBox_6, 0, 4, 1, 1)

        self.checkBox_4 = QCheckBox(self.centralwidget)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout_2.addWidget(self.checkBox_4, 0, 1, 1, 1)

        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout_2.addWidget(self.checkBox_2, 0, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAutoFillBackground(False)

        self.verticalLayout.addWidget(self.label_2)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout.addWidget(self.comboBox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cancelButton = QPushButton(self.centralwidget)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)

        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout.addWidget(self.saveButton)

        self.saveAddMaterialButton = QPushButton(self.centralwidget)
        self.saveAddMaterialButton.setObjectName(u"saveAddMaterialButton")
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(68, 137, 246, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(238, 244, 249, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(111, 117, 122, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(148, 156, 162, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        brush6 = QBrush(QColor(222, 234, 243, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush7 = QBrush(QColor(255, 255, 220, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush8 = QBrush(QColor(0, 0, 0, 216))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        brush9 = QBrush(QColor(236, 236, 236, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        brush10 = QBrush(QColor(245, 245, 245, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush10)
        brush11 = QBrush(QColor(191, 191, 191, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush11)
        brush12 = QBrush(QColor(169, 169, 169, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush12)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        self.saveAddMaterialButton.setPalette(palette)
        self.saveAddMaterialButton.setTabletTracking(False)
        self.saveAddMaterialButton.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.saveAddMaterialButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 481, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.saveAddMaterialButton.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Add New Project", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Project:", None))
        self.begginingDateLabel.setText(QCoreApplication.translate("MainWindow", u"Beggining Date", None))
        self.nameLabel.setText(QCoreApplication.translate("MainWindow", u"Project Name", None))
        self.endDateLabel.setText(QCoreApplication.translate("MainWindow", u"End Date", None))
        self.customerLabel.setText(QCoreApplication.translate("MainWindow", u"Customer", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Construction Area:", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Bedroom ", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Other", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Kitchen", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"Addition", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Multiple Room", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Bathroom", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Tasks:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Demolition", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Painting", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"New Item", None))

        self.cancelButton.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.saveAddMaterialButton.setText(QCoreApplication.translate("MainWindow", u"Save and Add Materials ", None))
    # retranslateUi

