import os.path
import time

p='Dateiinfos1.py'
if os.path.exists(p):
    print('Die Datei ist vorhanden.')
    if os.path.isfile(p):
        print('Ist eine Datei und kein Verzeichnis')
        print('Größe:',os.path.getsize(p))
        print('Änderungsdatum:', time.ctime(os.path.getmtime(p)))






