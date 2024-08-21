# Text, den wir in binäre Daten umwandeln wollen
text = "Guten Tag"
# Text in eine binäre Datenfolge (Bytes) mit der UTF-8 Zeichencodierung umwandeln
binary_data = text.encode('utf-8')
# Datei öffnen und die binären Daten schreiben
with open('binäre_datei.bin', 'wb') as file:
    file.write(binary_data)
print(f'Die binären Daten wurden in die Datei "binäre_datei.bin" geschrieben.')
