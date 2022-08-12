# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'projectWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QDateEdit,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableView, QVBoxLayout,
    QWidget)

class Ui_Projects(object):
    def setupUi(self, Projects):
        if not Projects.objectName():
            Projects.setObjectName(u"Projects")
        Projects.resize(1068, 810)
        self.verticalLayout_7 = QVBoxLayout(Projects)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(12, -1, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addNewProjectBtn = QPushButton(Projects)
        self.addNewProjectBtn.setObjectName(u"addNewProjectBtn")

        self.horizontalLayout.addWidget(self.addNewProjectBtn)

        self.horizontalSpacer = QSpacerItem(736, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.searchLineEdit = QLineEdit(Projects)
        self.searchLineEdit.setObjectName(u"searchLineEdit")
        font = QFont()
        font.setPointSize(14)
        self.searchLineEdit.setFont(font)
        self.searchLineEdit.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.searchLineEdit)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(Projects)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_7)

        self.label_8 = QLabel(Projects)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_8)

        self.label_9 = QLabel(Projects)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_9)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.listWidget = QListWidget(Projects)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QSize(0, 150))
        self.listWidget.setMaximumSize(QSize(16777215, 16777215))
        self.listWidget.setStyleSheet(u"QListWidget {\n"
"    show-decoration-selected: 1; /* make the selection span the entire width of the view */\n"
"}\n"
"\n"
"QListWidget::item {\n"
"	border-bottom: 1px dashed black;\n"
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


        self.verticalLayout_7.addLayout(self.verticalLayout)

        self.stackedWidget = QStackedWidget(Projects)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_6 = QVBoxLayout(self.page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.page)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setMinimumSize(QSize(0, 400))
        self.scrollArea.setFrameShape(QFrame.Box)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -236, 1025, 712))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.label_14.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_14)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(False)
        self.label_2.setFont(font2)

        self.horizontalLayout_6.addWidget(self.label_2)

        self.projectLineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.projectLineEdit.setObjectName(u"projectLineEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.projectLineEdit.sizePolicy().hasHeightForWidth())
        self.projectLineEdit.setSizePolicy(sizePolicy3)
        self.projectLineEdit.setMinimumSize(QSize(200, 0))
        self.projectLineEdit.setFont(font)

        self.horizontalLayout_6.addWidget(self.projectLineEdit)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setFont(font2)

        self.horizontalLayout_7.addWidget(self.label_4)

        self.begDateEdit = QDateEdit(self.scrollAreaWidgetContents)
        self.begDateEdit.setObjectName(u"begDateEdit")
        self.begDateEdit.setFrame(False)
        self.begDateEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.begDateEdit.setReadOnly(False)
        self.begDateEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.begDateEdit.setMinimumDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 0)))
        self.begDateEdit.setMinimumDate(QDate(2000, 1, 1))
        self.begDateEdit.setCalendarPopup(True)

        self.horizontalLayout_7.addWidget(self.begDateEdit)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setFont(font2)

        self.horizontalLayout_7.addWidget(self.label_5)

        self.endDateEdit = QDateEdit(self.scrollAreaWidgetContents)
        self.endDateEdit.setObjectName(u"endDateEdit")
        self.endDateEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.endDateEdit.setProperty("showGroupSeparator", False)
        self.endDateEdit.setMinimumDate(QDate(2000, 1, 1))
        self.endDateEdit.setCalendarPopup(True)
        self.endDateEdit.setCurrentSectionIndex(0)

        self.horizontalLayout_7.addWidget(self.endDateEdit)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_8.addLayout(self.verticalLayout_4)

        self.line_3 = QFrame(self.scrollAreaWidgetContents)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setFont(font2)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.customerLineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.customerLineEdit.setObjectName(u"customerLineEdit")
        sizePolicy3.setHeightForWidth(self.customerLineEdit.sizePolicy().hasHeightForWidth())
        self.customerLineEdit.setSizePolicy(sizePolicy3)
        self.customerLineEdit.setMinimumSize(QSize(200, 0))
        self.customerLineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.customerLineEdit.setFont(font)
        self.customerLineEdit.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.customerLineEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label_11)

        self.phoneLineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.phoneLineEdit.setObjectName(u"phoneLineEdit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.phoneLineEdit.sizePolicy().hasHeightForWidth())
        self.phoneLineEdit.setSizePolicy(sizePolicy4)

        self.horizontalLayout_3.addWidget(self.phoneLineEdit)

        self.label_15 = QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName(u"label_15")
        sizePolicy2.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy2)
        self.label_15.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label_15)

        self.emailLineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.emailLineEdit.setObjectName(u"emailLineEdit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.emailLineEdit.sizePolicy().hasHeightForWidth())
        self.emailLineEdit.setSizePolicy(sizePolicy5)

        self.horizontalLayout_3.addWidget(self.emailLineEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)
        self.label_12.setFont(font2)

        self.horizontalLayout_5.addWidget(self.label_12)

        self.addressLineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.addressLineEdit.setObjectName(u"addressLineEdit")
        sizePolicy5.setHeightForWidth(self.addressLineEdit.sizePolicy().hasHeightForWidth())
        self.addressLineEdit.setSizePolicy(sizePolicy5)

        self.horizontalLayout_5.addWidget(self.addressLineEdit)

        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)
        self.label_13.setFont(font2)

        self.horizontalLayout_5.addWidget(self.label_13)

        self.cityLineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.cityLineEdit.setObjectName(u"cityLineEdit")
        sizePolicy5.setHeightForWidth(self.cityLineEdit.sizePolicy().hasHeightForWidth())
        self.cityLineEdit.setSizePolicy(sizePolicy5)

        self.horizontalLayout_5.addWidget(self.cityLineEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_8.addLayout(self.verticalLayout_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy6)
        self.label.setFont(font)

        self.verticalLayout_5.addWidget(self.label)

        self.markCompletedButton = QPushButton(self.scrollAreaWidgetContents)
        self.markCompletedButton.setObjectName(u"markCompletedButton")
        self.markCompletedButton.setAutoDefault(False)

        self.verticalLayout_5.addWidget(self.markCompletedButton)


        self.verticalLayout_2.addLayout(self.verticalLayout_5)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        font3 = QFont()
        font3.setPointSize(15)
        self.label_6.setFont(font3)

        self.verticalLayout_2.addWidget(self.label_6)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.livingroomCheck = QCheckBox(self.scrollAreaWidgetContents)
        self.livingroomCheck.setObjectName(u"livingroomCheck")

        self.gridLayout.addWidget(self.livingroomCheck, 0, 3, 1, 1)

        self.additionCheck = QCheckBox(self.scrollAreaWidgetContents)
        self.additionCheck.setObjectName(u"additionCheck")

        self.gridLayout.addWidget(self.additionCheck, 1, 1, 1, 1)

        self.bathroomCheck = QCheckBox(self.scrollAreaWidgetContents)
        self.bathroomCheck.setObjectName(u"bathroomCheck")

        self.gridLayout.addWidget(self.bathroomCheck, 0, 1, 1, 1)

        self.kitchenCheck = QCheckBox(self.scrollAreaWidgetContents)
        self.kitchenCheck.setObjectName(u"kitchenCheck")

        self.gridLayout.addWidget(self.kitchenCheck, 0, 0, 1, 1)

        self.bedroomCheck = QCheckBox(self.scrollAreaWidgetContents)
        self.bedroomCheck.setObjectName(u"bedroomCheck")

        self.gridLayout.addWidget(self.bedroomCheck, 0, 2, 1, 1)

        self.landscapeCheck = QCheckBox(self.scrollAreaWidgetContents)
        self.landscapeCheck.setObjectName(u"landscapeCheck")

        self.gridLayout.addWidget(self.landscapeCheck, 1, 2, 1, 1)

        self.exteriorCheck = QCheckBox(self.scrollAreaWidgetContents)
        self.exteriorCheck.setObjectName(u"exteriorCheck")

        self.gridLayout.addWidget(self.exteriorCheck, 1, 0, 1, 1)

        self.multipleroomCheck = QCheckBox(self.scrollAreaWidgetContents)
        self.multipleroomCheck.setObjectName(u"multipleroomCheck")

        self.gridLayout.addWidget(self.multipleroomCheck, 0, 4, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.line_2 = QFrame(self.scrollAreaWidgetContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)

        self.verticalLayout_2.addWidget(self.label_10)

        self.tableView = QTableView(self.scrollAreaWidgetContents)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setMinimumSize(QSize(0, 300))

        self.verticalLayout_2.addWidget(self.tableView)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.editMaterialBtn = QPushButton(self.scrollAreaWidgetContents)
        self.editMaterialBtn.setObjectName(u"editMaterialBtn")
        sizePolicy3.setHeightForWidth(self.editMaterialBtn.sizePolicy().hasHeightForWidth())
        self.editMaterialBtn.setSizePolicy(sizePolicy3)

        self.horizontalLayout_9.addWidget(self.editMaterialBtn)

        self.addMaterialbtn = QPushButton(self.scrollAreaWidgetContents)
        self.addMaterialbtn.setObjectName(u"addMaterialbtn")
        sizePolicy3.setHeightForWidth(self.addMaterialbtn.sizePolicy().hasHeightForWidth())
        self.addMaterialbtn.setSizePolicy(sizePolicy3)

        self.horizontalLayout_9.addWidget(self.addMaterialbtn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_6.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_8 = QVBoxLayout(self.page_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_16 = QLabel(self.page_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setEnabled(False)
        self.label_16.setFont(font3)

        self.verticalLayout_8.addWidget(self.label_16)

        self.verticalSpacer = QSpacerItem(20, 427, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_7.addWidget(self.stackedWidget)


        self.retranslateUi(Projects)

        self.stackedWidget.setCurrentIndex(1)
        self.markCompletedButton.setDefault(True)


        QMetaObject.connectSlotsByName(Projects)
    # setupUi

    def retranslateUi(self, Projects):
        Projects.setWindowTitle(QCoreApplication.translate("Projects", u"Form", None))
        self.addNewProjectBtn.setText(QCoreApplication.translate("Projects", u"Add new project", None))
        self.searchLineEdit.setPlaceholderText(QCoreApplication.translate("Projects", u"Search project...", None))
        self.label_7.setText(QCoreApplication.translate("Projects", u"Project", None))
        self.label_8.setText(QCoreApplication.translate("Projects", u"Customer", None))
        self.label_9.setText(QCoreApplication.translate("Projects", u"Status", None))
        self.label_14.setText(QCoreApplication.translate("Projects", u"Information:", None))
        self.label_2.setText(QCoreApplication.translate("Projects", u"Project Name:", None))
        self.label_4.setText(QCoreApplication.translate("Projects", u"Beggining Date:", None))
        self.begDateEdit.setDisplayFormat(QCoreApplication.translate("Projects", u"M/d/yyyy", None))
        self.label_5.setText(QCoreApplication.translate("Projects", u"End Date:", None))
        self.endDateEdit.setDisplayFormat(QCoreApplication.translate("Projects", u"M/d/yyyy", None))
        self.label_3.setText(QCoreApplication.translate("Projects", u"Customer:", None))
        self.label_11.setText(QCoreApplication.translate("Projects", u"Phone#:", None))
        self.label_15.setText(QCoreApplication.translate("Projects", u"Email:", None))
        self.label_12.setText(QCoreApplication.translate("Projects", u"Address:", None))
        self.label_13.setText(QCoreApplication.translate("Projects", u"City:", None))
        self.label.setText(QCoreApplication.translate("Projects", u"Mark project as completed:", None))
        self.markCompletedButton.setText(QCoreApplication.translate("Projects", u"Completed", None))
        self.label_6.setText(QCoreApplication.translate("Projects", u"Construction Area:", None))
        self.livingroomCheck.setText(QCoreApplication.translate("Projects", u"Living Room", None))
        self.additionCheck.setText(QCoreApplication.translate("Projects", u"Addition", None))
        self.bathroomCheck.setText(QCoreApplication.translate("Projects", u"Bathroom", None))
        self.kitchenCheck.setText(QCoreApplication.translate("Projects", u"Kitchen", None))
        self.bedroomCheck.setText(QCoreApplication.translate("Projects", u"Bedroom", None))
        self.landscapeCheck.setText(QCoreApplication.translate("Projects", u"Landscape", None))
        self.exteriorCheck.setText(QCoreApplication.translate("Projects", u"Exterior", None))
        self.multipleroomCheck.setText(QCoreApplication.translate("Projects", u"Multiple Room", None))
        self.label_10.setText(QCoreApplication.translate("Projects", u"Materials:", None))
        self.editMaterialBtn.setText(QCoreApplication.translate("Projects", u"Edit", None))
        self.addMaterialbtn.setText(QCoreApplication.translate("Projects", u"Add", None))
        self.label_16.setText(QCoreApplication.translate("Projects", u"Select a project...", None))
    # retranslateUi

