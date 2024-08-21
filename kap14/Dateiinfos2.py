import shutil
import os.path

ori='Dateiinfos2.py'
kopie='Dateiinfos2.bak'

if os.path.exists(ori):
    print('Original existiert')
else:
    print('Original existiert nicht')
if os.path.exists(kopie):
    print('Kopie existiert')
else:
    print('Kopie existiert nicht')
try:
    shutil.copy(ori,kopie)
    print('copy-Methode ausgeführt')
except FileNotFoundError:
    print('Orginaldatei nicht gefunden')
except FileExistsError:
    print('Zieldatei schon vorhanden - es wird nicht kopiert')
except PermissionError:
    print('Zugriffsprobleme auf Zieldatei - es wird nicht kopiert')
if os.path.exists(kopie):
    print('Kopie vorhanden')
else:
    print('Kopie nicht vorhanden')







