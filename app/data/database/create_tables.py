import sqlite3
from sqlite3 import Error
import os


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main(basedir):

    database = os.path.join(basedir, "app/data/database/customer_data.db")

    sql_create_customer_table = """ CREATE TABLE IF NOT EXISTS customer (
                                        id integer PRIMARY KEY,
                                        first_name nvarchar(30) NOT NULL,
                                        last_name nvarchar(30) NOT NULL,
                                        phone nvarchar(24),
                                        address nvarchar(35),
                                        city nvarchar(35),
                                        zip nvarchar(10),
                                        email nvarchar(40)
                                    ); """
    
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        customer_id integer NOT NULL,
                                        project_name text NOT NULL,
                                        begin_date text,
                                        end_date text,
                                        status text,
                                        FOREIGN KEY (customer_id) REFERENCES customer (id)
                                    );"""
    
    sql_create_materials_table = """ CREATE TABLE IF NOT EXISTS materials (
                                        project_id integer,
                                        material_name text NOT NULL,
                                        description text,
                                        quantity integer NOT NULL,
                                        price integer NOT NULL, 
                                        total integer NOT NULL,
                                        FOREIGN KEY (project_id) REFERENCES projects (id)
                                    );"""

    sql_create_task_table = """ CREATE TABLE IF NOT EXISTS tasks (
                                    task_id integer PRIMARY KEY,
                                    project_id integer NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                );"""
    
    sql_create_labor_table = """ CREATE TABLE IF NOT EXISTS labor(
                                    project_id integer,
                                    nbr_workers integer,
                                    rate real, 
                                    duration real,
                                    labor_cost real,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                    );"""

    sql_create_fees_table = """ CREATE TABLE IF NOT EXISTS fees(
                                    project_id integer,
                                    fee_name text, 
                                    fee_amount real,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                    );"""    
    
    sql_create_client_costs_table = """ CREATE TABLE IF NOT EXISTS estimates (
                                            project_id integer,
                                            material_cost real,
                                            labor_cost real,
                                            fee_cost real,
                                            tax_cost real,
                                            total_cost real,
                                            FOREIGN KEY (project_id) REFERENCES projects (id)
                                            );"""

    
    # create database connection
    conn = create_connection(database)

    #create tables
    if conn is not None:
        create_table(conn, sql_create_customer_table)
        create_table(conn, sql_create_projects_table)
        create_table(conn, sql_create_materials_table)
        create_table(conn, sql_create_task_table)
        create_table(conn, sql_create_labor_table)
        create_table(conn, sql_create_fees_table)
        create_table(conn, sql_create_client_costs_table)

    else:
        print("Error! cannot create the database connection")

# if __name__ == '__main__':
#     main()