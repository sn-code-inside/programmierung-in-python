gz = (1234,5678,87654,12333, 4711)
anzahlVersuche = 0
while anzahlVersuche < 3:
    e = int(input("Geben Sie Ihre Geheimzahl ein:\n"))
    if e in gz:
        print("Die Geheimzahl ist korrekt. Geld auszahlen")
        break
    print("Die Geheimzahl war leider nicht korrekt.\n")
    anzahlVersuche += 1
    if anzahlVersuche < 3:
        w = input("Abbruch (A)?\n")
        if w == "A": break
if anzahlVersuche >= 3:
    print("Sie haben zu viele Versuche benötigt.\nDie Karte wird eingezogen.")


