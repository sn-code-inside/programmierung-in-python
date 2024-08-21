eingabe = input("Geben Sie Ihre Zugangskennung ein (Userid Password)\n")
zugangsdaten=eingabe.split()
# Pattern Matching
match zugangsdaten:
     case (['root','geheim']|['admin',"123"]): # Kombination von Oder und sequenzieller Datenstruktur - Datentypen beachten
         print('Hallo Meister.')
     case _:   
         print('Zugangsdaten falsch.')
