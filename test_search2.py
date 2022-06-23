
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QComboBox, QDialogButtonBox,
QGridLayout, QMainWindow, QLineEdit, QTableView, QTableWidget, QTableWidgetItem, QWidget, QTableView, QGridLayout)
from PySide6.QtSql import QSqlDatabase, QSqlQueryModel, QSqlTableModel, QSqlQuery
import sqlite3


class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.edit = QLineEdit()
        self.combo = QComboBox()
        self.table = QTableView()
        self.model = QSqlQueryModel()
        self.table.setModel(self.model)

        grid = QGridLayout(self)
        grid.addWidget(self.edit, 0, 0)
        grid.addWidget(self.combo, 0, 1)
        grid.addWidget(self.table, 1, 0, 1, 2)

        self.populate_table("SELECT * FROM customer")
        self.edit.textChanged.connect(self.filter_table)

        for i in range(self.model.columnCount()):
            self.combo.addItem(self.model.headerData(i, Qt.Horizontal))

    def populate_table(self, query, values=None):
        q = QSqlQuery(query)
        if values is not None:
            for value in values:
                q.addBindValue(value)
                #print(value)
        if not q.exec():
            print(q.lastError().text())
        self.model.setQuery(q)

    def filter_table(self, text):
        if text:
            self.populate_table(
                "SELECT * FROM customer WHERE {} LIKE ?".format(
                    self.combo.currentText()
                ),
                ["%{}%".format(text)],
            )
        else:
            self.populate_table("SELECT * FROM customer")


def main():
    import sys

    app = QApplication(sys.argv)

    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("customer_data.db")
    if not db.open():
        sys.exit(-1)

    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()