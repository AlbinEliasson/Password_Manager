import sqlite3

db_filename = 'password.db'

connection = sqlite3.connect(db_filename)

# Create a cursor object to execute SQL commands
cursor = connection.cursor()


def create_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS passwords
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    app TEXT NOT NULL,
    password TEXT NOT NULL)         
    ''')


def close_database():
    cursor.close()
    connection.close()


close_database()
