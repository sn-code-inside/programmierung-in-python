b = input("Geben Sie an, was Sie machen wollen\nx:\t Ende\ns:\tSpeichern\nd:\tDrucken\n").lower()
match b:
     case 'x':
         print('Programm verlassen.')
     case 's':
         print('Daten speichern.')
     case 'd':
         print('Drucken.')
     case _:
         print('Kein Treffer.')
