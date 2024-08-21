# Datei öffnen und binäre Daten aus der Datei lesen
with open('binäre_datei.bin', 'rb') as file:
    binary_data = file.read()
# Binäre Daten in Text mit UTF-8 Zeichencodierung umwandeln
text = binary_data.decode('utf-8')
# Den Text ausgeben
print(f'Gelesener Text aus der binären Datei: {text}')
