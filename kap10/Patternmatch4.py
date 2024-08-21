bestellung = input("Geben Sie Ihre Bestellung auf\n")
# Pattern Matching
match bestellung.split():
     case ['Bier']:
         print('Prost.')
     case ['Wein'|"Apfelwein"]: # Oder
         print('Wohl bekomm\'s.')
     case ['Limo'|"Saft"|"Wasser"]: # Oder
         print('Sie müssen wohl noch fahren?')
     case _:   
         print('Leider haben wir', bestellung, 'nicht vorrätig.')
