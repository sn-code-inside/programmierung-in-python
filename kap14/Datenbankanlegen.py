import sqlite3
import os.path

if not os.path.exists('sqldb.db'):
    connection=sqlite3.connect('sqldb.db')
    cursor=connection.cursor()
    cursor.execute('''CREATE TABLE personen(name TEXT, vorname TEXT)''')
    print("Datenbank erstellt")
    connection.close()
else:
    print("Datenbank schon vorhanden")










