# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'projectWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableView, QVBoxLayout, QWidget)

class Ui_Projects(object):
    def setupUi(self, Projects):
        if not Projects.objectName():
            Projects.setObjectName(u"Projects")
        Projects.resize(967, 687)
        self.verticalLayout_3 = QVBoxLayout(Projects)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget = QStackedWidget(Projects)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(736, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_5 = QPushButton(self.page)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout.addWidget(self.pushButton_5)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.searchLineEdit = QLineEdit(self.page)
        self.searchLineEdit.setObjectName(u"searchLineEdit")

        self.verticalLayout.addWidget(self.searchLineEdit)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(self.page)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_4.addWidget(self.label_7)

        self.label_8 = QLabel(self.page)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_4.addWidget(self.label_8)

        self.label_9 = QLabel(self.page)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_4.addWidget(self.label_9)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.listWidget = QListWidget(self.page)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setStyleSheet(u"QListWidget {\n"
"    show-decoration-selected: 1; /* make the selection span the entire width of the view */\n"
"}\n"
"\n"
"QListWidget::item:alternate {\n"
"    background: #EEEEEE;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    border: 1px solid #6a6ea9;\n"
"}\n"
"\n"
"QListWidget::item:selected:!active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #ABAFE5, stop: 1 #8588B2);\n"
"}\n"
"\n"
"QListWidget::item:selected:active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #6a6ea9, stop: 1 #888dd9);\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #FAFBFE, stop: 1 #DCDEF1);\n"
"}")

        self.verticalLayout.addWidget(self.listWidget)


        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 2, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.page)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 1, 3, 1, 1)

        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_5 = QLabel(self.page)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.projectLabel = QLabel(self.page)
        self.projectLabel.setObjectName(u"projectLabel")
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        font.setBold(False)
        self.projectLabel.setFont(font)
        self.projectLabel.setFrameShape(QFrame.NoFrame)
        self.projectLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.projectLabel, 0, 1, 1, 1)

        self.customerLabel = QLabel(self.page)
        self.customerLabel.setObjectName(u"customerLabel")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(14)
        self.customerLabel.setFont(font1)
        self.customerLabel.setFrameShape(QFrame.NoFrame)
        self.customerLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.customerLabel, 0, 3, 1, 1)

        self.begDateLabel = QLabel(self.page)
        self.begDateLabel.setObjectName(u"begDateLabel")
        self.begDateLabel.setFont(font1)
        self.begDateLabel.setFrameShape(QFrame.NoFrame)
        self.begDateLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.begDateLabel, 1, 1, 1, 1)

        self.endDateLabel = QLabel(self.page)
        self.endDateLabel.setObjectName(u"endDateLabel")
        self.endDateLabel.setFont(font1)
        self.endDateLabel.setFrameShape(QFrame.NoFrame)
        self.endDateLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.endDateLabel, 2, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_6 = QLabel(self.page)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_4.addWidget(self.label_6)

        self.listWidget_2 = QListWidget(self.page)
        self.listWidget_2.setObjectName(u"listWidget_2")

        self.verticalLayout_4.addWidget(self.listWidget_2)


        self.gridLayout_2.addLayout(self.verticalLayout_4, 2, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_2 = QPushButton(self.page)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.tableView = QTableView(self.page)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_2.addWidget(self.tableView)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 4, 0, 1, 2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButton_3 = QPushButton(self.page)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 5, 1, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.retranslateUi(Projects)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Projects)
    # setupUi

    def retranslateUi(self, Projects):
        Projects.setWindowTitle(QCoreApplication.translate("Projects", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Projects", u"Add Project", None))
        self.pushButton_5.setText(QCoreApplication.translate("Projects", u"Edit Project", None))
        self.label_7.setText(QCoreApplication.translate("Projects", u"Project", None))
        self.label_8.setText(QCoreApplication.translate("Projects", u"Customer", None))
        self.label_9.setText(QCoreApplication.translate("Projects", u"Status", None))
        self.label_2.setText(QCoreApplication.translate("Projects", u"Project Name:", None))
        self.label_3.setText(QCoreApplication.translate("Projects", u"Customer:", None))
        self.pushButton_4.setText(QCoreApplication.translate("Projects", u"See customer info", None))
        self.label_4.setText(QCoreApplication.translate("Projects", u"Beggining Date:", None))
        self.label_5.setText(QCoreApplication.translate("Projects", u"End Date:", None))
        self.projectLabel.setText("")
        self.customerLabel.setText("")
        self.begDateLabel.setText("")
        self.endDateLabel.setText("")
        self.label_6.setText(QCoreApplication.translate("Projects", u"Tasks:", None))
        self.pushButton_2.setText(QCoreApplication.translate("Projects", u"Add Materials", None))
        self.label.setText(QCoreApplication.translate("Projects", u"Materials:", None))
        self.pushButton_3.setText(QCoreApplication.translate("Projects", u"Go to estimates", None))
    # retranslateUi

