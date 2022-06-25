
from re import I
import sqlite3
from sqlite3 import Error

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


def add_new_customer(conn, customer):

    sql = ''' INSERT INTO customer (first_name, last_name, phone, address, city, zip)
            VALUES (?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, customer)
    conn.commit()
    return cur.lastrowid

def create_new_project(conn, project):
    """
    Create a new project in the projects table
    """
    sql = ''' INSERT INTO projects(customer_id ,project_name, begin_date, end_date)
            VALUES(?,?,?,?) '''

    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid

def add_materials(conn, materials):
    """
    Add materials needed for each project on the materials table
    """

    sql = '''INSERT INTO materials(project_id, material_name, description, quantity, price, total)
            VALUES(?,?,?,?,?,?) '''

    cur = conn.cursor()
    cur.execute(sql, materials)
    conn.commit()

def add_new_task(conn, project_id):
    """ Create task for new project """

    sql = ''' INSERT INTO tasks (project_id)
                VALUES(?) '''

    cur = conn.cursor()
    cur.execute(sql, [project_id])
    conn.commit()
    return cur.lastrowid


def find_customer_id(conn, name):

    sql = '''SELECT id FROM customer
            WHERE first_name || " " || last_name = ?'''

    cur = conn.cursor()
    cur.execute(sql, [name])
    id = cur.fetchone()[0]
    return id


# def add_new_column(conn):

#     sql = ''' ALTER TABLE projects
#             ADD COLUMN status TEXT'''
    
#     cur = conn.cursor()
#     cur.execute(sql)
#     conn.commit()


# Returns dictionary with project_id and project_name 
def find_current_project(conn):

    sql = ''' SELECT id, project_name FROM projects
                WHERE status IS NULL'''
    
    cur = conn.cursor()
    cur.execute(sql)
    
    rows = cur.fetchall()
    
    projects_dict = {}
    for i in rows:
        projects_dict[i[0]] = i[1]
    return projects_dict
    

# def delete_projects(conn, id):
#     sql = 'DELETE FROM projects WHERE id = ?'

#     cur = conn.cursor()
#     cur.execute(sql, (id,))
#     conn.commit()

def delete_table(conn):
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS customer')
    conn.commit()

def mark_as_complete(conn, id):

    sql = ''' UPDATE projects
            SET status = 'Completed'
            WHERE id = ? '''
    cur = conn.cursor()
    cur.execute(sql, [id])
    conn.commit()

def get_full_customer_name(conn):
    
    sql = ''' SELECT id, first_name || " " || last_name FROM customer'''
    
    cur= conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    dict = {}
    for i in rows:
        dict[i[0]] = i[1]
    return dict

def get_customer_address(conn, id):

    sql = ''' SELECT address FROM customer
            WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, [id])
    address = cur.fetchone()[0]
    return address   


def get_project_customer_name(conn):

    sql = ''' SELECT projects.id, projects.customer_id, project_name, first_name || " " || last_name, status FROM projects
            INNER JOIN customer ON customer.id = projects.customer_id
            ORDER BY status ASC'''

    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    return rows

def get_dates(conn, project_id):

    sql = ''' SELECT begin_date, end_date FROM projects
                WHERE id = ?'''
    
    cur = conn.cursor()
    cur.execute(sql, [project_id])
    rows = cur.fetchone()
    return rows

def get_customer_data(conn, customer_id):

    sql = ''' SELECT first_name || " " || last_name, phone, address, city, zip FROM customer
                WHERE id = ?'''
    
    cur = conn.cursor()
    cur.execute(sql, [customer_id])
    row = cur.fetchone()
    return row


# def main():

#     database = r"app/data/database/customer_data.db"

#     conn = create_connection(database)

#     with conn:
#         delete_table(conn)

#     #     customer_id = find_customer_id(conn, "Grace Smith")
#     #     project = (customer_id, "1004 Mc Cue", "2022-03-07", "2022-04-10", "Bedroom, Bathroom", "$5,000", "$10,000")
#     #     project_id = create_new_project(conn, project)
#         #find_current_project(conn)
    



# if __name__== '__main__':
#     main()


