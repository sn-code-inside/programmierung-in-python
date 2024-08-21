try:
    fp = open("dat.txt","r")
    print(fp.read())
    fp.close()
except IOError:
    print("Fehler beim Zugriff auf die Datei")





