# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customerWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLineEdit, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)

class Ui_Customers(object):
    def setupUi(self, Customers):
        if not Customers.objectName():
            Customers.setObjectName(u"Customers")
        Customers.resize(722, 574)
        self.verticalLayout = QVBoxLayout(Customers)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(Customers)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.tableView = QTableView(Customers)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)


        self.retranslateUi(Customers)

        QMetaObject.connectSlotsByName(Customers)
    # setupUi

    def retranslateUi(self, Customers):
        Customers.setWindowTitle(QCoreApplication.translate("Customers", u"Form", None))
    # retranslateUi

