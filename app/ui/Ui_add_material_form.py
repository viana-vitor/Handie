# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addMaterialForm.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(387, 498)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.materialNameLineEdit = QLineEdit(Form)
        self.materialNameLineEdit.setObjectName(u"materialNameLineEdit")

        self.verticalLayout.addWidget(self.materialNameLineEdit)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.descTextEdit = QPlainTextEdit(Form)
        self.descTextEdit.setObjectName(u"descTextEdit")

        self.verticalLayout.addWidget(self.descTextEdit)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.qtySpinBox = QSpinBox(Form)
        self.qtySpinBox.setObjectName(u"qtySpinBox")
        self.qtySpinBox.setProperty("showGroupSeparator", True)
        self.qtySpinBox.setMaximum(1000000)

        self.verticalLayout.addWidget(self.qtySpinBox)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.priceSpinBox = QDoubleSpinBox(Form)
        self.priceSpinBox.setObjectName(u"priceSpinBox")
        self.priceSpinBox.setProperty("showGroupSeparator", True)
        self.priceSpinBox.setMaximum(1000000.000000000000000)

        self.verticalLayout.addWidget(self.priceSpinBox)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.searchHDBtn = QPushButton(Form)
        self.searchHDBtn.setObjectName(u"searchHDBtn")

        self.horizontalLayout.addWidget(self.searchHDBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.cancelBtn = QPushButton(Form)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.verticalLayout.addWidget(self.cancelBtn)

        self.addBtn = QPushButton(Form)
        self.addBtn.setObjectName(u"addBtn")

        self.verticalLayout.addWidget(self.addBtn)


        self.retranslateUi(Form)

        self.addBtn.setDefault(True)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Add Material", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Material Name:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Description:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Quantity:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Price:", None))
        self.priceSpinBox.setPrefix(QCoreApplication.translate("Form", u"$", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Search Home Depot", None))
        self.searchHDBtn.setText(QCoreApplication.translate("Form", u"Search", None))
        self.cancelBtn.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.addBtn.setText(QCoreApplication.translate("Form", u"Add", None))
    # retranslateUi

