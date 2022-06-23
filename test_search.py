
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QComboBox, QDialogButtonBox, QMainWindow, QLineEdit, QTableWidget, QTableWidgetItem, QWidget, QGridLayout
from PySide6.QtSql import QSqlDatabase, QSqlQueryModel, QSqlTableModel, QSqlQuery
import sqlite3

class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.edit = QLineEdit()
        self.combo = QComboBox()
        self.table = QTableWidget()

        grid = QGridLayout(self)
        grid.addWidget(self.edit, 0, 0)
        grid.addWidget(self.combo, 0, 1)
        grid.addWidget(self.table, 1, 0, 1, 2)

        self.connection = sqlite3.connect("customer_data.db")

        self.populate_table("SELECT * FROM customer")
        self.edit.textChanged.connect(self.filter_table)

    def populate_table(self, query, values=None):
        cursor = self.connection.cursor()
        if values is None:
            cursor.execute(query)
        else:
            cursor.execute(query, values)

        name_of_columns = [e[0] for e in cursor.description]
        self.table.setColumnCount(len(name_of_columns))
        self.table.setRowCount(0)
        self.table.setHorizontalHeaderLabels(name_of_columns)
        self.combo.clear()
        self.combo.addItems(name_of_columns)

        for i, row_data in enumerate(cursor.fetchall()):
            self.table.insertRow(self.table.rowCount())
            for j, value in enumerate(row_data):
                item = QTableWidgetItem()
                item.setData(Qt.DisplayRole, value)
                self.table.setItem(i, j, item)

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
    w = MyWidget()
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
