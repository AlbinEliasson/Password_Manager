import sqlite3
from sqlite3 import Cursor, Connection

db_filename = 'password.db'


def get_db_connection() -> Connection:
    connection = None

    try:
        connection = sqlite3.connect(db_filename)
    except Exception as e:
        print(e)

    return connection


def get_cursor(connection) -> Cursor:
    return connection.cursor()


def create_table(connection, cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS passwords
    (appName TEXT PRIMARY KEY NOT NULL,
    password TEXT NOT NULL)
    ''')

    connection.commit()


def insert_app_name_password(connection, cursor, name, password):
    sql = 'INSERT INTO passwords (appName, password) VALUES (?, ?)'

    cursor.execute(sql, (name, password))
    connection.commit()


def update_password(connection, cursor, name, new_password):
    sql = 'UPDATE passwords SET password = ? WHERE appName = ?'

    cursor.execute(sql, (new_password, name))
    connection.commit()


def remove_app_name_password(connection, cursor, name):
    sql = 'DELETE FROM passwords WHERE appName = ?'

    cursor.execute(sql, (name,))
    connection.commit()


def drop_table(connection, cursor):
    sql = 'DROP TABLE passwords'

    cursor.execute(sql)
    connection.commit()


def show_table(cursor):
    for row in cursor.execute('SELECT * FROM passwords'):
        print(row)


def close_database(connection, cursor):
    cursor.close()
    connection.close()
