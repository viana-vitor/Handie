
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery

db = QSqlDatabase("QSQLITE")
db.setDatabaseName("customer_data.db")
db.open()

query = QSqlQuery(db=db)
query.prepare(
    """
    INSERT INTO customer (first_name, last_name, phone, address, city, zip)
    VALUES (:first_name, :last_name, :phone, :address, :city, :zip)
    """
)

data = [
    ("Ariana", "Davarpanah", 6507624416, "726 Serra St", "Stanford", 94305)]

for first_name, last_name, phone, address, city, zip in data:
    query.bindValue(":first_name", first_name)
    query.bindValue(":last_name", last_name)
    query.bindValue(":phone", phone)
    query.bindValue(":address", address)
    query.bindValue(":city", city)
    query.bindValue(":zip", zip)
    query.exec()