import sqlite3
import os.path

n = input("Eingabe Nachname\n")
v = input("Eingabe Vorname\n")
if os.path.exists('sqldb.db'):
    connection=sqlite3.connect('sqldb.db')
    cursor=connection.cursor()
    cursor.execute('''INSERT INTO personen VALUES(?,?)''',(n,v))
    print("Daten geschrieben")
    connection.commit()
    connection.close()
else:
    print("Datenbank nicht vorhanden")











