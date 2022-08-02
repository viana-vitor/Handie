# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addProjectVersion3.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QDoubleSpinBox, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QTableView, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(986, 746)
        font = QFont()
        font.setPointSize(13)
        Form.setFont(font)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_7 = QVBoxLayout(self.page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_37 = QLabel(self.page)
        self.label_37.setObjectName(u"label_37")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.label_37.setFont(font1)
        self.label_37.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_37, 0, Qt.AlignHCenter)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.addNewProjectButton = QPushButton(self.page)
        self.addNewProjectButton.setObjectName(u"addNewProjectButton")

        self.horizontalLayout_8.addWidget(self.addNewProjectButton)

        self.pushButton_3 = QPushButton(self.page)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_8.addWidget(self.pushButton_3)


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)

        self.line_4 = QFrame(self.page)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line_4)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_38 = QLabel(self.page)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_9.addWidget(self.label_38)

        self.comboBox = QComboBox(self.page)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_9.addWidget(self.comboBox)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)

        self.label_39 = QLabel(self.page)
        self.label_39.setObjectName(u"label_39")

        self.verticalLayout_7.addWidget(self.label_39)

        self.tableView = QTableView(self.page)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_7.addWidget(self.tableView)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.markCompleteButton = QPushButton(self.page)
        self.markCompleteButton.setObjectName(u"markCompleteButton")

        self.horizontalLayout_10.addWidget(self.markCompleteButton)

        self.goProjectButton = QPushButton(self.page)
        self.goProjectButton.setObjectName(u"goProjectButton")

        self.horizontalLayout_10.addWidget(self.goProjectButton)


        self.verticalLayout_7.addLayout(self.horizontalLayout_10)

        self.stackedWidget.addWidget(self.page)
        self.page_initial = QWidget()
        self.page_initial.setObjectName(u"page_initial")
        self.verticalLayout_3 = QVBoxLayout(self.page_initial)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.newCustomerButton = QPushButton(self.page_initial)
        self.newCustomerButton.setObjectName(u"newCustomerButton")
        self.newCustomerButton.setFocusPolicy(Qt.TabFocus)

        self.verticalLayout_3.addWidget(self.newCustomerButton)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.existingCustomerButton = QPushButton(self.page_initial)
        self.existingCustomerButton.setObjectName(u"existingCustomerButton")

        self.verticalLayout_3.addWidget(self.existingCustomerButton)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.stackedWidget.addWidget(self.page_initial)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_12 = QVBoxLayout(self.page_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.scrollArea = QScrollArea(self.page_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 923, 745))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.stackedWidget_3 = QStackedWidget(self.scrollAreaWidgetContents)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget_3.sizePolicy().hasHeightForWidth())
        self.stackedWidget_3.setSizePolicy(sizePolicy)
        self.stackedWidget_3.setMaximumSize(QSize(16777215, 16777215))
        self.stackedWidget_3.setLayoutDirection(Qt.LeftToRight)
        self.stackedWidget_3.setAutoFillBackground(False)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.verticalLayout_14 = QVBoxLayout(self.page_8)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_36 = QLabel(self.page_8)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setScaledContents(False)
        self.label_36.setWordWrap(False)
        self.label_36.setIndent(-1)

        self.horizontalLayout_7.addWidget(self.label_36)

        self.customerNameComboBox = QComboBox(self.page_8)
        self.customerNameComboBox.setObjectName(u"customerNameComboBox")

        self.horizontalLayout_7.addWidget(self.customerNameComboBox)


        self.verticalLayout_14.addLayout(self.horizontalLayout_7)

        self.stackedWidget_3.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.gridLayout = QGridLayout(self.page_9)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_7 = QGridLayout()
#ifndef Q_OS_MAC
        self.gridLayout_7.setSpacing(-1)
#endif
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_7.setContentsMargins(0, 0, -1, -1)
        self.lastNamelineEdit = QLineEdit(self.page_9)
        self.lastNamelineEdit.setObjectName(u"lastNamelineEdit")

        self.gridLayout_7.addWidget(self.lastNamelineEdit, 0, 3, 1, 1)

        self.label_21 = QLabel(self.page_9)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_7.addWidget(self.label_21, 1, 0, 1, 1)

        self.zipLineEdit = QLineEdit(self.page_9)
        self.zipLineEdit.setObjectName(u"zipLineEdit")

        self.gridLayout_7.addWidget(self.zipLineEdit, 2, 3, 1, 1)

        self.label_22 = QLabel(self.page_9)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_7.addWidget(self.label_22, 2, 0, 1, 1)

        self.firstNamelineEdit = QLineEdit(self.page_9)
        self.firstNamelineEdit.setObjectName(u"firstNamelineEdit")

        self.gridLayout_7.addWidget(self.firstNamelineEdit, 0, 1, 1, 1)

        self.phoneLineEdit = QLineEdit(self.page_9)
        self.phoneLineEdit.setObjectName(u"phoneLineEdit")

        self.gridLayout_7.addWidget(self.phoneLineEdit, 1, 1, 1, 1)

        self.label_23 = QLabel(self.page_9)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_7.addWidget(self.label_23, 1, 2, 1, 1)

        self.label_24 = QLabel(self.page_9)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_7.addWidget(self.label_24, 2, 2, 1, 1)

        self.cityLineEdit = QLineEdit(self.page_9)
        self.cityLineEdit.setObjectName(u"cityLineEdit")

        self.gridLayout_7.addWidget(self.cityLineEdit, 2, 1, 1, 1)

        self.label_25 = QLabel(self.page_9)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_7.addWidget(self.label_25, 0, 2, 1, 1)

        self.addressLineEdit = QLineEdit(self.page_9)
        self.addressLineEdit.setObjectName(u"addressLineEdit")

        self.gridLayout_7.addWidget(self.addressLineEdit, 1, 3, 1, 1)

        self.label_26 = QLabel(self.page_9)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_7.addWidget(self.label_26, 0, 0, 1, 1)

        self.label_27 = QLabel(self.page_9)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_7.addWidget(self.label_27, 3, 0, 1, 1)

        self.label_28 = QLabel(self.page_9)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_7.addWidget(self.label_28, 3, 2, 1, 1)

        self.emailLineEdit = QLineEdit(self.page_9)
        self.emailLineEdit.setObjectName(u"emailLineEdit")

        self.gridLayout_7.addWidget(self.emailLineEdit, 3, 1, 1, 1)

        self.companyLineEdit = QLineEdit(self.page_9)
        self.companyLineEdit.setObjectName(u"companyLineEdit")

        self.gridLayout_7.addWidget(self.companyLineEdit, 3, 3, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_7, 0, 0, 1, 1)

        self.stackedWidget_3.addWidget(self.page_9)

        self.verticalLayout_6.addWidget(self.stackedWidget_3)

        self.line_3 = QFrame(self.scrollAreaWidgetContents)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_3)

        self.label_33 = QLabel(self.scrollAreaWidgetContents)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setAcceptDrops(False)

        self.verticalLayout_6.addWidget(self.label_33)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.begginingDateDateEdit = QDateEdit(self.scrollAreaWidgetContents)
        self.begginingDateDateEdit.setObjectName(u"begginingDateDateEdit")
        self.begginingDateDateEdit.setDateTime(QDateTime(QDate(2000, 9, 14), QTime(0, 0, 0)))
        self.begginingDateDateEdit.setMinimumDate(QDate(2000, 1, 1))
        self.begginingDateDateEdit.setCalendarPopup(True)

        self.gridLayout_10.addWidget(self.begginingDateDateEdit, 2, 1, 1, 1)

        self.endDateDateEdit = QDateEdit(self.scrollAreaWidgetContents)
        self.endDateDateEdit.setObjectName(u"endDateDateEdit")
        self.endDateDateEdit.setMinimumDate(QDate(2000, 1, 1))
        self.endDateDateEdit.setCalendarPopup(True)

        self.gridLayout_10.addWidget(self.endDateDateEdit, 3, 1, 1, 1)

        self.nameLabel_4 = QLabel(self.scrollAreaWidgetContents)
        self.nameLabel_4.setObjectName(u"nameLabel_4")

        self.gridLayout_10.addWidget(self.nameLabel_4, 0, 0, 1, 1)

        self.begginingDateLabel = QLabel(self.scrollAreaWidgetContents)
        self.begginingDateLabel.setObjectName(u"begginingDateLabel")

        self.gridLayout_10.addWidget(self.begginingDateLabel, 2, 0, 1, 1)

        self.projectNameLineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.projectNameLineEdit.setObjectName(u"projectNameLineEdit")

        self.gridLayout_10.addWidget(self.projectNameLineEdit, 0, 1, 1, 1)

        self.endDateLabel = QLabel(self.scrollAreaWidgetContents)
        self.endDateLabel.setObjectName(u"endDateLabel")

        self.gridLayout_10.addWidget(self.endDateLabel, 3, 0, 1, 1)

        self.addressCheckBox = QCheckBox(self.scrollAreaWidgetContents)
        self.addressCheckBox.setObjectName(u"addressCheckBox")

        self.gridLayout_10.addWidget(self.addressCheckBox, 1, 1, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_10)

        self.label_34 = QLabel(self.scrollAreaWidgetContents)
        self.label_34.setObjectName(u"label_34")

        self.verticalLayout_6.addWidget(self.label_34)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.kitchenCheck = QCheckBox(self.scrollAreaWidgetContents)
        self.kitchenCheck.setObjectName(u"kitchenCheck")

        self.gridLayout_11.addWidget(self.kitchenCheck, 1, 0, 1, 1)

        self.otherCheck = QCheckBox(self.scrollAreaWidgetContents)
        self.otherCheck.setObjectName(u"otherCheck")

        self.gridLayout_11.addWidget(self.otherCheck, 4, 0, 1, 1)

        self.multipleRoomCheck = QCheckBox(self.scrollAreaWidgetContents)
        self.multipleRoomCheck.setObjectName(u"multipleRoomCheck")

        self.gridLayout_11.addWidget(self.multipleRoomCheck, 1, 3, 1, 1)

        self.bathroomCheck = QCheckBox(self.scrollAreaWidgetContents)
        self.bathroomCheck.setObjectName(u"bathroomCheck")

        self.gridLayout_11.addWidget(self.bathroomCheck, 1, 1, 1, 1)

        self.additionCheck = QCheckBox(self.scrollAreaWidgetContents)
        self.additionCheck.setObjectName(u"additionCheck")

        self.gridLayout_11.addWidget(self.additionCheck, 1, 6, 1, 1)

        self.bedroomCheck = QCheckBox(self.scrollAreaWidgetContents)
        self.bedroomCheck.setObjectName(u"bedroomCheck")

        self.gridLayout_11.addWidget(self.bedroomCheck, 1, 2, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_11)

        self.line_6 = QFrame(self.scrollAreaWidgetContents)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line_6)

        self.constructionAreaStacked = QStackedWidget(self.scrollAreaWidgetContents)
        self.constructionAreaStacked.setObjectName(u"constructionAreaStacked")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.constructionAreaStacked.sizePolicy().hasHeightForWidth())
        self.constructionAreaStacked.setSizePolicy(sizePolicy1)
        self.constructionAreaStacked.setMinimumSize(QSize(0, 300))
        self.constructionAreaStacked.setFrameShape(QFrame.NoFrame)
        self.constructionAreaStacked.setFrameShadow(QFrame.Plain)
        self.constructionAreaStacked.setLineWidth(0)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_4 = QVBoxLayout(self.page_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.page_4)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_4.addWidget(self.label_5)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.constructionAreaStacked.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_15 = QVBoxLayout(self.page_5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setSizeConstraint(QLayout.SetNoConstraint)

        self.verticalLayout_15.addLayout(self.verticalLayout_13)

        self.constructionAreaStacked.addWidget(self.page_5)

        self.verticalLayout_6.addWidget(self.constructionAreaStacked)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_12.addWidget(self.scrollArea)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.cancelButton = QPushButton(self.page_2)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout_6.addWidget(self.cancelButton)

        self.continueButton = QPushButton(self.page_2)
        self.continueButton.setObjectName(u"continueButton")
        self.continueButton.setAutoDefault(False)

        self.horizontalLayout_6.addWidget(self.continueButton)


        self.verticalLayout_12.addLayout(self.horizontalLayout_6)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_5 = QVBoxLayout(self.page_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.page_3)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(False)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.label)

        self.widget = QWidget(self.page_3)
        self.widget.setObjectName(u"widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy2)
        self.widget.setMaximumSize(QSize(16777215, 191))
        self.verticalLayout_10 = QVBoxLayout(self.widget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.materialLineEdit = QLineEdit(self.widget)
        self.materialLineEdit.setObjectName(u"materialLineEdit")

        self.gridLayout_2.addWidget(self.materialLineEdit, 0, 1, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.materialqtySpinBox = QSpinBox(self.widget)
        self.materialqtySpinBox.setObjectName(u"materialqtySpinBox")
        self.materialqtySpinBox.setPrefix(u"")
        self.materialqtySpinBox.setMaximum(10000)

        self.gridLayout_2.addWidget(self.materialqtySpinBox, 1, 1, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        self.materialPriceSpinBox = QDoubleSpinBox(self.widget)
        self.materialPriceSpinBox.setObjectName(u"materialPriceSpinBox")
        self.materialPriceSpinBox.setMaximum(999999.989999999990687)
        self.materialPriceSpinBox.setValue(0.000000000000000)

        self.gridLayout_2.addWidget(self.materialPriceSpinBox, 2, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_2.addWidget(self.label_9)

        self.materialDescLineEdit = QLineEdit(self.widget)
        self.materialDescLineEdit.setObjectName(u"materialDescLineEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.materialDescLineEdit.sizePolicy().hasHeightForWidth())
        self.materialDescLineEdit.setSizePolicy(sizePolicy3)
        self.materialDescLineEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.materialDescLineEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_10.addLayout(self.horizontalLayout)

        self.line_7 = QFrame(self.widget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_10.addWidget(self.line_7)

        self.addMaterialPushButton = QPushButton(self.widget)
        self.addMaterialPushButton.setObjectName(u"addMaterialPushButton")
        self.addMaterialPushButton.setFlat(False)

        self.verticalLayout_10.addWidget(self.addMaterialPushButton)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_2.addWidget(self.label_10)

        self.searchHDPushButton = QPushButton(self.widget)
        self.searchHDPushButton.setObjectName(u"searchHDPushButton")

        self.horizontalLayout_2.addWidget(self.searchHDPushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_10.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addWidget(self.widget)

        self.line = QFrame(self.page_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line)

        self.label_12 = QLabel(self.page_3)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_5.addWidget(self.label_12)

        self.materialsTableWidget = QTableWidget(self.page_3)
        self.materialsTableWidget.setObjectName(u"materialsTableWidget")

        self.verticalLayout_5.addWidget(self.materialsTableWidget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label_11 = QLabel(self.page_3)
        self.label_11.setObjectName(u"label_11")
        font3 = QFont()
        font3.setPointSize(14)
        self.label_11.setFont(font3)

        self.horizontalLayout_3.addWidget(self.label_11)

        self.totalCostLabel = QLabel(self.page_3)
        self.totalCostLabel.setObjectName(u"totalCostLabel")
        self.totalCostLabel.setFont(font3)

        self.horizontalLayout_3.addWidget(self.totalCostLabel)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.backButton = QPushButton(self.page_3)
        self.backButton.setObjectName(u"backButton")

        self.horizontalLayout_13.addWidget(self.backButton)

        self.finishAddMaterialButton = QPushButton(self.page_3)
        self.finishAddMaterialButton.setObjectName(u"finishAddMaterialButton")

        self.horizontalLayout_13.addWidget(self.finishAddMaterialButton)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)
        self.constructionAreaStacked.setCurrentIndex(0)
        self.continueButton.setDefault(True)
        self.addMaterialPushButton.setDefault(False)
        self.finishAddMaterialButton.setDefault(True)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Add New Project", None))
        self.label_37.setText(QCoreApplication.translate("Form", u"Handie \u00ae", None))
        self.addNewProjectButton.setText(QCoreApplication.translate("Form", u"Add New Project", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Quick Estimate", None))
        self.label_38.setText(QCoreApplication.translate("Form", u"Current Projects:", None))
        self.label_39.setText(QCoreApplication.translate("Form", u"Materials:", None))
        self.markCompleteButton.setText(QCoreApplication.translate("Form", u"Mark as complete", None))
        self.goProjectButton.setText(QCoreApplication.translate("Form", u"Go to project", None))
        self.newCustomerButton.setText(QCoreApplication.translate("Form", u"New Customer", None))
        self.existingCustomerButton.setText(QCoreApplication.translate("Form", u"Existing Customer", None))
        self.label_36.setText(QCoreApplication.translate("Form", u"Customer:", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"Phone #", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"City", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"Address", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"Zip Code", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"Last Name*", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"First Name*", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"Email", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"Company", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"Project:", None))
        self.begginingDateDateEdit.setDisplayFormat(QCoreApplication.translate("Form", u"M/d/yyyy", None))
        self.endDateDateEdit.setDisplayFormat(QCoreApplication.translate("Form", u"M/d/yyyy", None))
        self.nameLabel_4.setText(QCoreApplication.translate("Form", u"Project Name*", None))
        self.begginingDateLabel.setText(QCoreApplication.translate("Form", u"Beggining Date", None))
        self.endDateLabel.setText(QCoreApplication.translate("Form", u"End Date", None))
        self.addressCheckBox.setText(QCoreApplication.translate("Form", u"Same as customer address", None))
        self.label_34.setText(QCoreApplication.translate("Form", u"Construction Area:", None))
        self.kitchenCheck.setText(QCoreApplication.translate("Form", u"Kitchen", None))
        self.otherCheck.setText(QCoreApplication.translate("Form", u"Other", None))
        self.multipleRoomCheck.setText(QCoreApplication.translate("Form", u"Multiple Room", None))
        self.bathroomCheck.setText(QCoreApplication.translate("Form", u"Bathroom", None))
        self.additionCheck.setText(QCoreApplication.translate("Form", u"Addition", None))
        self.bedroomCheck.setText(QCoreApplication.translate("Form", u"Bedroom", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"No construction area selected", None))
        self.cancelButton.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.continueButton.setText(QCoreApplication.translate("Form", u"Continue", None))
        self.label.setText(QCoreApplication.translate("Form", u"New Material:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Name:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Quantity:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Price:", None))
        self.materialPriceSpinBox.setPrefix(QCoreApplication.translate("Form", u"$", None))
        self.materialPriceSpinBox.setSuffix("")
        self.label_9.setText(QCoreApplication.translate("Form", u"Description:", None))
        self.addMaterialPushButton.setText(QCoreApplication.translate("Form", u"Add Material", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Search The Home Depot?", None))
        self.searchHDPushButton.setText(QCoreApplication.translate("Form", u"Search", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Added Materials:", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Total:", None))
        self.totalCostLabel.setText("")
        self.backButton.setText(QCoreApplication.translate("Form", u"Back ", None))
        self.finishAddMaterialButton.setText(QCoreApplication.translate("Form", u"Finish", None))
    # retranslateUi

