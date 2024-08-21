t1 = "Ein Kratzer?! Ihr Arm ist ab!"
t2 = "Es ist lustig, nicht wahr? Wie Ihr bester Freund einfach so explodieren kann?" 
t3 = "Dieser Papagei ist nicht mehr."
t4 = "Und jetzt zu etwas vollkommen anderem."
t5 = "42"
print(t1.upper())
print(t1.lower())
print( "nein, das stimmt nicht.".capitalize() )
print("Die Länge von t2.",
      "Hier einmal keine String-Methode, sondern eine String-Funktion:):",
      len(t2))
print("Stehen in t5 nur Zahlen?", t5.isdigit())
print(t3.index("ist"))
print(t2.count("e"))
print(t4.replace("e","i"))
print(t4.split(" "))
