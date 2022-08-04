# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editMaterialForm.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDoubleSpinBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(449, 498)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.idSpinBox = QSpinBox(Form)
        self.idSpinBox.setObjectName(u"idSpinBox")
        self.idSpinBox.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.idSpinBox.sizePolicy().hasHeightForWidth())
        self.idSpinBox.setSizePolicy(sizePolicy)
        self.idSpinBox.setMinimum(1)
        self.idSpinBox.setMaximum(1000000)

        self.verticalLayout.addWidget(self.idSpinBox)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.materialNameEdit = QLineEdit(Form)
        self.materialNameEdit.setObjectName(u"materialNameEdit")

        self.verticalLayout.addWidget(self.materialNameEdit)

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
        sizePolicy.setHeightForWidth(self.qtySpinBox.sizePolicy().hasHeightForWidth())
        self.qtySpinBox.setSizePolicy(sizePolicy)
        self.qtySpinBox.setMaximum(100000)

        self.verticalLayout.addWidget(self.qtySpinBox)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.priceSpinBox = QDoubleSpinBox(Form)
        self.priceSpinBox.setObjectName(u"priceSpinBox")
        sizePolicy.setHeightForWidth(self.priceSpinBox.sizePolicy().hasHeightForWidth())
        self.priceSpinBox.setSizePolicy(sizePolicy)
        self.priceSpinBox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.priceSpinBox.setProperty("showGroupSeparator", True)
        self.priceSpinBox.setMaximum(1000000.000000000000000)

        self.verticalLayout.addWidget(self.priceSpinBox)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout.addWidget(self.pushButton_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.previousBtn = QPushButton(Form)
        self.previousBtn.setObjectName(u"previousBtn")

        self.verticalLayout.addWidget(self.previousBtn)

        self.nextBtn = QPushButton(Form)
        self.nextBtn.setObjectName(u"nextBtn")

        self.verticalLayout.addWidget(self.nextBtn)

        self.saveBtn = QPushButton(Form)
        self.saveBtn.setObjectName(u"saveBtn")

        self.verticalLayout.addWidget(self.saveBtn)


        self.retranslateUi(Form)

        self.saveBtn.setDefault(True)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Edit Materials", None))
        self.label.setText(QCoreApplication.translate("Form", u"Project ID:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Material name:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Description:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Quantity:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Price:", None))
        self.priceSpinBox.setPrefix(QCoreApplication.translate("Form", u"$", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Search Home Depot", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Search", None))
        self.previousBtn.setText(QCoreApplication.translate("Form", u"Previous", None))
        self.nextBtn.setText(QCoreApplication.translate("Form", u"Next", None))
        self.saveBtn.setText(QCoreApplication.translate("Form", u"Save Changes", None))
    # retranslateUi

