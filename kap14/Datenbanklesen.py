import sqlite3
import os.path

if os.path.exists('sqldb.db'):
    connection=sqlite3.connect('sqldb.db')
    cursor=connection.cursor()
    cursor.execute('''SELECT * FROM personen''')
    rows=cursor.fetchall()
    for row in rows:
        print(row[0], row[1])
    print("Alle Daten ausgelesen")
    connection.close()
else:
    print("Datenbank nicht vorhanden")












