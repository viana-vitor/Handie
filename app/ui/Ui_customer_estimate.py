# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customerEstimate.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QAbstractSpinBox, QApplication, QComboBox,
    QDoubleSpinBox, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QPlainTextEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QStackedWidget, QTableView,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(872, 719)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_2 = QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(self.page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 809, 1549))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(22)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label)

        self.label_27 = QLabel(self.scrollAreaWidgetContents)
        self.label_27.setObjectName(u"label_27")
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.label_27.setFont(font1)

        self.verticalLayout_12.addWidget(self.label_27)

        self.label_19 = QLabel(self.scrollAreaWidgetContents)
        self.label_19.setObjectName(u"label_19")
        font2 = QFont()
        font2.setPointSize(11)
        self.label_19.setFont(font2)

        self.verticalLayout_12.addWidget(self.label_19)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_12.addItem(self.horizontalSpacer_12)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.customerDataLabel = QLabel(self.scrollAreaWidgetContents)
        self.customerDataLabel.setObjectName(u"customerDataLabel")

        self.gridLayout.addWidget(self.customerDataLabel, 0, 1, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.emailDataLabel = QLabel(self.scrollAreaWidgetContents)
        self.emailDataLabel.setObjectName(u"emailDataLabel")

        self.gridLayout.addWidget(self.emailDataLabel, 0, 3, 1, 1)

        self.cityDataLabel = QLabel(self.scrollAreaWidgetContents)
        self.cityDataLabel.setObjectName(u"cityDataLabel")

        self.gridLayout.addWidget(self.cityDataLabel, 1, 1, 1, 1)

        self.addressDataLabel = QLabel(self.scrollAreaWidgetContents)
        self.addressDataLabel.setObjectName(u"addressDataLabel")

        self.gridLayout.addWidget(self.addressDataLabel, 1, 3, 1, 1)

        self.zipDataLabel = QLabel(self.scrollAreaWidgetContents)
        self.zipDataLabel.setObjectName(u"zipDataLabel")

        self.gridLayout.addWidget(self.zipDataLabel, 1, 5, 1, 1)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 0, 4, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setWordWrap(False)
        self.label_2.setMargin(0)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_32 = QLabel(self.scrollAreaWidgetContents)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout.addWidget(self.label_32, 1, 4, 1, 1)

        self.phoneDataLabel = QLabel(self.scrollAreaWidgetContents)
        self.phoneDataLabel.setObjectName(u"phoneDataLabel")

        self.gridLayout.addWidget(self.phoneDataLabel, 0, 5, 1, 1)


        self.verticalLayout_12.addLayout(self.gridLayout)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_12.addWidget(self.line)

        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")
        font3 = QFont()
        font3.setPointSize(14)
        self.label_12.setFont(font3)

        self.verticalLayout_12.addWidget(self.label_12)

        self.verticalSpacer = QSpacerItem(17, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer)

        self.line_2 = QFrame(self.scrollAreaWidgetContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_12.addWidget(self.line_2)

        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font3)

        self.verticalLayout_12.addWidget(self.label_13)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_2.addWidget(self.label_14)

        self.line_7 = QFrame(self.scrollAreaWidgetContents)
        self.line_7.setObjectName(u"line_7")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line_7.sizePolicy().hasHeightForWidth())
        self.line_7.setSizePolicy(sizePolicy1)
        self.line_7.setFrameShadow(QFrame.Plain)
        self.line_7.setMidLineWidth(3)
        self.line_7.setFrameShape(QFrame.HLine)

        self.horizontalLayout_2.addWidget(self.line_7)

        self.materialsSpinBox = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.materialsSpinBox.setObjectName(u"materialsSpinBox")
        self.materialsSpinBox.setAutoFillBackground(False)
        self.materialsSpinBox.setWrapping(False)
        self.materialsSpinBox.setFrame(False)
        self.materialsSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.materialsSpinBox.setReadOnly(True)
        self.materialsSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.materialsSpinBox.setProperty("showGroupSeparator", True)
        self.materialsSpinBox.setMaximum(100000000.000000000000000)

        self.horizontalLayout_2.addWidget(self.materialsSpinBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.materialsWidget = QWidget(self.scrollAreaWidgetContents)
        self.materialsWidget.setObjectName(u"materialsWidget")
        self.horizontalLayout_21 = QHBoxLayout(self.materialsWidget)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_7)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_21 = QLabel(self.materialsWidget)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_8.addWidget(self.label_21)

        self.newMaterialLineEdit = QLineEdit(self.materialsWidget)
        self.newMaterialLineEdit.setObjectName(u"newMaterialLineEdit")

        self.horizontalLayout_8.addWidget(self.newMaterialLineEdit)


        self.verticalLayout_10.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_23 = QLabel(self.materialsWidget)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_19.addWidget(self.label_23)

        self.qtyMaterialSpinBox = QSpinBox(self.materialsWidget)
        self.qtyMaterialSpinBox.setObjectName(u"qtyMaterialSpinBox")
        self.qtyMaterialSpinBox.setMaximum(10000)

        self.horizontalLayout_19.addWidget(self.qtyMaterialSpinBox)


        self.verticalLayout_10.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_24 = QLabel(self.materialsWidget)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_20.addWidget(self.label_24)

        self.priceMaterialSpinBox = QDoubleSpinBox(self.materialsWidget)
        self.priceMaterialSpinBox.setObjectName(u"priceMaterialSpinBox")
        self.priceMaterialSpinBox.setMaximum(100000.000000000000000)

        self.horizontalLayout_20.addWidget(self.priceMaterialSpinBox)


        self.verticalLayout_10.addLayout(self.horizontalLayout_20)


        self.horizontalLayout_21.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_22 = QLabel(self.materialsWidget)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_11.addWidget(self.label_22)

        self.descTextEdit = QPlainTextEdit(self.materialsWidget)
        self.descTextEdit.setObjectName(u"descTextEdit")

        self.verticalLayout_11.addWidget(self.descTextEdit)


        self.horizontalLayout_21.addLayout(self.verticalLayout_11)

        self.addMaterialButton = QPushButton(self.materialsWidget)
        self.addMaterialButton.setObjectName(u"addMaterialButton")

        self.horizontalLayout_21.addWidget(self.addMaterialButton)

        self.horizontalSpacer_6 = QSpacerItem(38, 38, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addWidget(self.materialsWidget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.showMaterialButton = QPushButton(self.scrollAreaWidgetContents)
        self.showMaterialButton.setObjectName(u"showMaterialButton")
        self.showMaterialButton.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.showMaterialButton)

        self.editMaterialBtn = QPushButton(self.scrollAreaWidgetContents)
        self.editMaterialBtn.setObjectName(u"editMaterialBtn")

        self.horizontalLayout_3.addWidget(self.editMaterialBtn)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_16)

        self.label_20 = QLabel(self.scrollAreaWidgetContents)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_3.addWidget(self.label_20)

        self.searchHDBtn = QPushButton(self.scrollAreaWidgetContents)
        self.searchHDBtn.setObjectName(u"searchHDBtn")

        self.horizontalLayout_3.addWidget(self.searchHDBtn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.materialsTableView = QTableView(self.scrollAreaWidgetContents)
        self.materialsTableView.setObjectName(u"materialsTableView")
        self.materialsTableView.setMinimumSize(QSize(0, 250))

        self.horizontalLayout_6.addWidget(self.materialsTableView)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)


        self.verticalLayout_12.addLayout(self.verticalLayout_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_15 = QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_7.addWidget(self.label_15)

        self.line_6 = QFrame(self.scrollAreaWidgetContents)
        self.line_6.setObjectName(u"line_6")
        sizePolicy1.setHeightForWidth(self.line_6.sizePolicy().hasHeightForWidth())
        self.line_6.setSizePolicy(sizePolicy1)
        self.line_6.setFrameShadow(QFrame.Plain)
        self.line_6.setMidLineWidth(4)
        self.line_6.setFrameShape(QFrame.HLine)

        self.horizontalLayout_7.addWidget(self.line_6)

        self.laborSpinBox = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.laborSpinBox.setObjectName(u"laborSpinBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.laborSpinBox.sizePolicy().hasHeightForWidth())
        self.laborSpinBox.setSizePolicy(sizePolicy2)
        self.laborSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.laborSpinBox.setReadOnly(True)
        self.laborSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.laborSpinBox.setProperty("showGroupSeparator", True)
        self.laborSpinBox.setMaximum(100000000.000000000000000)

        self.horizontalLayout_7.addWidget(self.laborSpinBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, -1, -1)
        self.nbrWorkersSpinBox = QSpinBox(self.scrollAreaWidgetContents)
        self.nbrWorkersSpinBox.setObjectName(u"nbrWorkersSpinBox")
        self.nbrWorkersSpinBox.setMaximum(1000)

        self.horizontalLayout_4.addWidget(self.nbrWorkersSpinBox)

        self.label_17 = QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_4.addWidget(self.label_17)

        self.workerRateDoubleSpinBox = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.workerRateDoubleSpinBox.setObjectName(u"workerRateDoubleSpinBox")
        self.workerRateDoubleSpinBox.setMaximum(1000.000000000000000)

        self.horizontalLayout_4.addWidget(self.workerRateDoubleSpinBox)

        self.label_18 = QLabel(self.scrollAreaWidgetContents)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_4.addWidget(self.label_18)

        self.durationSpinBox = QSpinBox(self.scrollAreaWidgetContents)
        self.durationSpinBox.setObjectName(u"durationSpinBox")
        self.durationSpinBox.setMaximum(1000)

        self.horizontalLayout_4.addWidget(self.durationSpinBox)

        self.durationComboBox = QComboBox(self.scrollAreaWidgetContents)
        self.durationComboBox.addItem("")
        self.durationComboBox.addItem("")
        self.durationComboBox.setObjectName(u"durationComboBox")

        self.horizontalLayout_4.addWidget(self.durationComboBox)

        self.addLaborPushButton = QPushButton(self.scrollAreaWidgetContents)
        self.addLaborPushButton.setObjectName(u"addLaborPushButton")

        self.horizontalLayout_4.addWidget(self.addLaborPushButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setMargin(0)

        self.verticalLayout_4.addWidget(self.label_5)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)


        self.verticalLayout_12.addLayout(self.verticalLayout_5)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_25 = QLabel(self.scrollAreaWidgetContents)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_12.addWidget(self.label_25)

        self.line_5 = QFrame(self.scrollAreaWidgetContents)
        self.line_5.setObjectName(u"line_5")
        sizePolicy1.setHeightForWidth(self.line_5.sizePolicy().hasHeightForWidth())
        self.line_5.setSizePolicy(sizePolicy1)
        self.line_5.setFrameShadow(QFrame.Plain)
        self.line_5.setLineWidth(1)
        self.line_5.setMidLineWidth(4)
        self.line_5.setFrameShape(QFrame.HLine)

        self.horizontalLayout_12.addWidget(self.line_5)

        self.feeSpinBox = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.feeSpinBox.setObjectName(u"feeSpinBox")
        self.feeSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.feeSpinBox.setReadOnly(True)
        self.feeSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.feeSpinBox.setProperty("showGroupSeparator", True)
        self.feeSpinBox.setMaximum(100000000.000000000000000)

        self.horizontalLayout_12.addWidget(self.feeSpinBox)


        self.verticalLayout_7.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_15)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_10.addWidget(self.label_4)

        self.newFeeNameLineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.newFeeNameLineEdit.setObjectName(u"newFeeNameLineEdit")

        self.horizontalLayout_10.addWidget(self.newFeeNameLineEdit)

        self.label_26 = QLabel(self.scrollAreaWidgetContents)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_10.addWidget(self.label_26)

        self.addFeeSpinBox = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.addFeeSpinBox.setObjectName(u"addFeeSpinBox")
        self.addFeeSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.addFeeSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.addFeeSpinBox.setProperty("showGroupSeparator", True)
        self.addFeeSpinBox.setMaximum(100000000.000000000000000)

        self.horizontalLayout_10.addWidget(self.addFeeSpinBox)

        self.addFeepushButton = QPushButton(self.scrollAreaWidgetContents)
        self.addFeepushButton.setObjectName(u"addFeepushButton")
        self.addFeepushButton.setFlat(False)

        self.horizontalLayout_10.addWidget(self.addFeepushButton)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_11.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_14)


        self.verticalLayout_7.addLayout(self.horizontalLayout_11)


        self.verticalLayout_12.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_28 = QLabel(self.scrollAreaWidgetContents)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_13.addWidget(self.label_28)

        self.line_4 = QFrame(self.scrollAreaWidgetContents)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setWindowModality(Qt.NonModal)
        self.line_4.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.line_4.sizePolicy().hasHeightForWidth())
        self.line_4.setSizePolicy(sizePolicy1)
        font4 = QFont()
        font4.setBold(False)
        self.line_4.setFont(font4)
        self.line_4.setStyleSheet(u"")
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setMidLineWidth(4)
        self.line_4.setFrameShape(QFrame.HLine)

        self.horizontalLayout_13.addWidget(self.line_4)

        self.taxSpinBox = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.taxSpinBox.setObjectName(u"taxSpinBox")
        self.taxSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.taxSpinBox.setReadOnly(True)
        self.taxSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.taxSpinBox.setProperty("showGroupSeparator", True)
        self.taxSpinBox.setMaximum(100000000.000000000000000)

        self.horizontalLayout_13.addWidget(self.taxSpinBox)


        self.verticalLayout_8.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_17)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_16.addWidget(self.label_8)

        self.newTaxNameLineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.newTaxNameLineEdit.setObjectName(u"newTaxNameLineEdit")

        self.horizontalLayout_16.addWidget(self.newTaxNameLineEdit)

        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_16.addWidget(self.label_9)

        self.newTaxdoubleSpinBox = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.newTaxdoubleSpinBox.setObjectName(u"newTaxdoubleSpinBox")
        self.newTaxdoubleSpinBox.setAutoFillBackground(False)
        self.newTaxdoubleSpinBox.setFrame(True)

        self.horizontalLayout_16.addWidget(self.newTaxdoubleSpinBox)

        self.addTaxPushButton = QPushButton(self.scrollAreaWidgetContents)
        self.addTaxPushButton.setObjectName(u"addTaxPushButton")

        self.horizontalLayout_16.addWidget(self.addTaxPushButton)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_19)


        self.verticalLayout_9.addLayout(self.horizontalLayout_16)


        self.horizontalLayout_14.addLayout(self.verticalLayout_9)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_20)


        self.verticalLayout_8.addLayout(self.horizontalLayout_14)


        self.verticalLayout_12.addLayout(self.verticalLayout_8)

        self.line_3 = QFrame(self.scrollAreaWidgetContents)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setLineWidth(1)
        self.line_3.setFrameShape(QFrame.HLine)

        self.verticalLayout_12.addWidget(self.line_3)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_21)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_31 = QLabel(self.scrollAreaWidgetContents)
        self.label_31.setObjectName(u"label_31")
        font5 = QFont()
        font5.setPointSize(16)
        self.label_31.setFont(font5)

        self.horizontalLayout_17.addWidget(self.label_31)

        self.totalCostSpinBox = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.totalCostSpinBox.setObjectName(u"totalCostSpinBox")
        self.totalCostSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.totalCostSpinBox.setReadOnly(True)
        self.totalCostSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.totalCostSpinBox.setProperty("showGroupSeparator", True)
        self.totalCostSpinBox.setMaximum(100000000.000000000000000)

        self.horizontalLayout_17.addWidget(self.totalCostSpinBox)


        self.horizontalLayout_18.addLayout(self.horizontalLayout_17)


        self.verticalLayout_12.addLayout(self.horizontalLayout_18)

        self.line_8 = QFrame(self.scrollAreaWidgetContents)
        self.line_8.setObjectName(u"line_8")
        sizePolicy2.setHeightForWidth(self.line_8.sizePolicy().hasHeightForWidth())
        self.line_8.setSizePolicy(sizePolicy2)
        self.line_8.setMinimumSize(QSize(0, 7))
        self.line_8.setFrameShadow(QFrame.Plain)
        self.line_8.setLineWidth(6)
        self.line_8.setFrameShape(QFrame.HLine)

        self.verticalLayout_12.addWidget(self.line_8)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_12.addItem(self.horizontalSpacer_11)

        self.label_16 = QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.verticalLayout_12.addWidget(self.label_16)

        self.label_29 = QLabel(self.scrollAreaWidgetContents)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font2)

        self.verticalLayout_12.addWidget(self.label_29)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_12.addItem(self.horizontalSpacer_13)

        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")
        font6 = QFont()
        font6.setPointSize(17)
        self.label_11.setFont(font6)

        self.verticalLayout_12.addWidget(self.label_11)

        self.generalCondTextEdit = QTextEdit(self.scrollAreaWidgetContents)
        self.generalCondTextEdit.setObjectName(u"generalCondTextEdit")
        self.generalCondTextEdit.setMinimumSize(QSize(0, 150))

        self.verticalLayout_12.addWidget(self.generalCondTextEdit)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_30 = QLabel(self.scrollAreaWidgetContents)
        self.label_30.setObjectName(u"label_30")
        font7 = QFont()
        font7.setPointSize(13)
        self.label_30.setFont(font7)

        self.horizontalLayout_9.addWidget(self.label_30)

        self.line_9 = QFrame(self.scrollAreaWidgetContents)
        self.line_9.setObjectName(u"line_9")
        sizePolicy1.setHeightForWidth(self.line_9.sizePolicy().hasHeightForWidth())
        self.line_9.setSizePolicy(sizePolicy1)
        self.line_9.setMaximumSize(QSize(16777215, 16777215))
        self.line_9.setFrameShadow(QFrame.Plain)
        self.line_9.setLineWidth(1)
        self.line_9.setMidLineWidth(1)
        self.line_9.setFrameShape(QFrame.HLine)

        self.horizontalLayout_9.addWidget(self.line_9)

        self.label_33 = QLabel(self.scrollAreaWidgetContents)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font7)

        self.horizontalLayout_9.addWidget(self.label_33)

        self.estimateMaterialSpinBox = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.estimateMaterialSpinBox.setObjectName(u"estimateMaterialSpinBox")
        self.estimateMaterialSpinBox.setFont(font7)
        self.estimateMaterialSpinBox.setWrapping(False)
        self.estimateMaterialSpinBox.setFrame(True)
        self.estimateMaterialSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.estimateMaterialSpinBox.setReadOnly(False)
        self.estimateMaterialSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.estimateMaterialSpinBox.setAccelerated(False)
        self.estimateMaterialSpinBox.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.estimateMaterialSpinBox.setProperty("showGroupSeparator", True)
        self.estimateMaterialSpinBox.setMinimum(0.000000000000000)
        self.estimateMaterialSpinBox.setMaximum(100000000.000000000000000)

        self.horizontalLayout_9.addWidget(self.estimateMaterialSpinBox)


        self.verticalLayout_12.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_34 = QLabel(self.scrollAreaWidgetContents)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font7)

        self.horizontalLayout_15.addWidget(self.label_34)

        self.line_10 = QFrame(self.scrollAreaWidgetContents)
        self.line_10.setObjectName(u"line_10")
        sizePolicy1.setHeightForWidth(self.line_10.sizePolicy().hasHeightForWidth())
        self.line_10.setSizePolicy(sizePolicy1)
        self.line_10.setFrameShadow(QFrame.Plain)
        self.line_10.setMidLineWidth(1)
        self.line_10.setFrameShape(QFrame.HLine)

        self.horizontalLayout_15.addWidget(self.line_10)

        self.label_35 = QLabel(self.scrollAreaWidgetContents)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font7)

        self.horizontalLayout_15.addWidget(self.label_35)

        self.estimateLaborSpinBox = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.estimateLaborSpinBox.setObjectName(u"estimateLaborSpinBox")
        self.estimateLaborSpinBox.setFont(font7)
        self.estimateLaborSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.estimateLaborSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.estimateLaborSpinBox.setProperty("showGroupSeparator", True)
        self.estimateLaborSpinBox.setMaximum(100000000.000000000000000)

        self.horizontalLayout_15.addWidget(self.estimateLaborSpinBox)


        self.verticalLayout_12.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_36 = QLabel(self.scrollAreaWidgetContents)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font7)

        self.horizontalLayout_22.addWidget(self.label_36)

        self.line_11 = QFrame(self.scrollAreaWidgetContents)
        self.line_11.setObjectName(u"line_11")
        sizePolicy1.setHeightForWidth(self.line_11.sizePolicy().hasHeightForWidth())
        self.line_11.setSizePolicy(sizePolicy1)
        self.line_11.setFrameShadow(QFrame.Plain)
        self.line_11.setFrameShape(QFrame.HLine)

        self.horizontalLayout_22.addWidget(self.line_11)

        self.label_37 = QLabel(self.scrollAreaWidgetContents)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font7)

        self.horizontalLayout_22.addWidget(self.label_37)

        self.estimateFeeSpinBox = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.estimateFeeSpinBox.setObjectName(u"estimateFeeSpinBox")
        sizePolicy2.setHeightForWidth(self.estimateFeeSpinBox.sizePolicy().hasHeightForWidth())
        self.estimateFeeSpinBox.setSizePolicy(sizePolicy2)
        self.estimateFeeSpinBox.setFont(font7)
        self.estimateFeeSpinBox.setAutoFillBackground(False)
        self.estimateFeeSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.estimateFeeSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.estimateFeeSpinBox.setProperty("showGroupSeparator", True)
        self.estimateFeeSpinBox.setMaximum(100000000.000000000000000)

        self.horizontalLayout_22.addWidget(self.estimateFeeSpinBox)


        self.verticalLayout_12.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_38 = QLabel(self.scrollAreaWidgetContents)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font7)

        self.horizontalLayout_23.addWidget(self.label_38)

        self.line_12 = QFrame(self.scrollAreaWidgetContents)
        self.line_12.setObjectName(u"line_12")
        sizePolicy1.setHeightForWidth(self.line_12.sizePolicy().hasHeightForWidth())
        self.line_12.setSizePolicy(sizePolicy1)
        self.line_12.setFrameShadow(QFrame.Plain)
        self.line_12.setMidLineWidth(1)
        self.line_12.setFrameShape(QFrame.HLine)

        self.horizontalLayout_23.addWidget(self.line_12)

        self.label_39 = QLabel(self.scrollAreaWidgetContents)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font7)

        self.horizontalLayout_23.addWidget(self.label_39)

        self.estimateTaxSpinBox = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.estimateTaxSpinBox.setObjectName(u"estimateTaxSpinBox")
        self.estimateTaxSpinBox.setFont(font7)
        self.estimateTaxSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.estimateTaxSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.estimateTaxSpinBox.setProperty("showGroupSeparator", True)
        self.estimateTaxSpinBox.setMaximum(100000000.000000000000000)

        self.horizontalLayout_23.addWidget(self.estimateTaxSpinBox)


        self.verticalLayout_12.addLayout(self.horizontalLayout_23)

        self.line_13 = QFrame(self.scrollAreaWidgetContents)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShadow(QFrame.Plain)
        self.line_13.setLineWidth(2)
        self.line_13.setFrameShape(QFrame.HLine)

        self.verticalLayout_12.addWidget(self.line_13)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_8)

        self.label_41 = QLabel(self.scrollAreaWidgetContents)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font5)

        self.horizontalLayout_24.addWidget(self.label_41)

        self.estimateTotalCostSpinBox = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.estimateTotalCostSpinBox.setObjectName(u"estimateTotalCostSpinBox")
        self.estimateTotalCostSpinBox.setFont(font5)
        self.estimateTotalCostSpinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.estimateTotalCostSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.estimateTotalCostSpinBox.setProperty("showGroupSeparator", True)
        self.estimateTotalCostSpinBox.setMaximum(100000000.000000000000000)

        self.horizontalLayout_24.addWidget(self.estimateTotalCostSpinBox)


        self.verticalLayout_12.addLayout(self.horizontalLayout_24)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.closePushButton = QPushButton(self.page)
        self.closePushButton.setObjectName(u"closePushButton")

        self.horizontalLayout.addWidget(self.closePushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pdfPushButton = QPushButton(self.page)
        self.pdfPushButton.setObjectName(u"pdfPushButton")

        self.horizontalLayout.addWidget(self.pdfPushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(Form)

        self.addFeepushButton.setDefault(False)
        self.pdfPushButton.setDefault(True)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Estimate", None))
        self.label.setText(QCoreApplication.translate("Form", u"Estimate", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"Contractor:", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"This section is for contractor view only.", None))
        self.customerDataLabel.setText("")
        self.label_6.setText(QCoreApplication.translate("Form", u"Email:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"City:", None))
        self.emailDataLabel.setText("")
        self.cityDataLabel.setText("")
        self.addressDataLabel.setText("")
        self.zipDataLabel.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"Address:", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Phone #:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Customer:", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"Zip", None))
        self.phoneDataLabel.setText("")
        self.label_12.setText(QCoreApplication.translate("Form", u"Construction Area:", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Estimate:", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Materials", None))
        self.materialsSpinBox.setPrefix(QCoreApplication.translate("Form", u"$", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"Material Name:", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"Quantity:", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"Price:", None))
        self.priceMaterialSpinBox.setPrefix(QCoreApplication.translate("Form", u"$", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"Description:", None))
        self.addMaterialButton.setText(QCoreApplication.translate("Form", u"Add", None))
        self.showMaterialButton.setText(QCoreApplication.translate("Form", u"Show/Hide Materials", None))
        self.editMaterialBtn.setText(QCoreApplication.translate("Form", u"Edit Materials", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"Search Home Depot", None))
        self.searchHDBtn.setText(QCoreApplication.translate("Form", u"Search", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Labor", None))
        self.laborSpinBox.setPrefix(QCoreApplication.translate("Form", u"$", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"workers at ", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"/hr for", None))
        self.durationComboBox.setItemText(0, QCoreApplication.translate("Form", u"Months", None))
        self.durationComboBox.setItemText(1, QCoreApplication.translate("Form", u"Days", None))

        self.addLaborPushButton.setText(QCoreApplication.translate("Form", u"Add", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"*Assumes a 5 day work week with 22 work days.", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"Fees", None))
        self.feeSpinBox.setPrefix(QCoreApplication.translate("Form", u"$", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Fee (Name):", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"Amount ($):", None))
        self.addFeeSpinBox.setPrefix("")
        self.addFeepushButton.setText(QCoreApplication.translate("Form", u"Add", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"Taxes", None))
        self.taxSpinBox.setPrefix(QCoreApplication.translate("Form", u"$", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Tax (Name):", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Rate:", None))
        self.newTaxdoubleSpinBox.setPrefix("")
        self.newTaxdoubleSpinBox.setSuffix(QCoreApplication.translate("Form", u"%", None))
        self.addTaxPushButton.setText(QCoreApplication.translate("Form", u"Add", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"Total:", None))
        self.totalCostSpinBox.setPrefix(QCoreApplication.translate("Form", u"$", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Customer:", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"This section will be used to create the customer estimate pdf document.", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"General Conditions:", None))
        self.generalCondTextEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Add general conditions.", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"Materials:", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"Total Cost:", None))
        self.estimateMaterialSpinBox.setPrefix(QCoreApplication.translate("Form", u"$", None))
        self.label_34.setText(QCoreApplication.translate("Form", u"Labor:", None))
        self.label_35.setText(QCoreApplication.translate("Form", u"Total Cost:", None))
        self.estimateLaborSpinBox.setPrefix(QCoreApplication.translate("Form", u"$", None))
        self.label_36.setText(QCoreApplication.translate("Form", u"Fees:", None))
        self.label_37.setText(QCoreApplication.translate("Form", u"Total Cost:", None))
        self.estimateFeeSpinBox.setPrefix(QCoreApplication.translate("Form", u"$", None))
        self.label_38.setText(QCoreApplication.translate("Form", u"Tax:", None))
        self.label_39.setText(QCoreApplication.translate("Form", u"Total Cost:", None))
        self.estimateTaxSpinBox.setPrefix(QCoreApplication.translate("Form", u"$", None))
        self.label_41.setText(QCoreApplication.translate("Form", u"Customer Total:", None))
        self.estimateTotalCostSpinBox.setPrefix(QCoreApplication.translate("Form", u"$", None))
        self.closePushButton.setText(QCoreApplication.translate("Form", u"Close", None))
        self.pdfPushButton.setText(QCoreApplication.translate("Form", u"Generate PDF", None))
    # retranslateUi

