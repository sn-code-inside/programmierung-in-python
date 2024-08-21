b = input("Geben Sie an, was Sie machen wollen:\nEnde:\t\tEnde\nSpeichern:\tSpeichern\nDrucken:\tDrucken\n").lower()
match b:
     case 'ende':
         print('Programm verlassen.')
     case 'speichern':
         print('Daten speichern.')
     case 'drucken':
         print('Drucken.')
     case other:
         print('Kein Treffer.')
