erg = int(input("Geben Sie eine Zahl zwischen 1 und 10 ein:\n"))
print(f"Sie haben {erg} eingeben! ")
if erg == 1:
    print("The Lumberjack-Song")
    print("Holzfäller-Lied")
elif erg == 2:
    print("The Funniest Joke in the World")
    print("Der tödlichste Witz der Welt")
elif erg == 3:
    print("Dirty Hungarian Phrasebook")
    print("Versautes ungarisch-englisches Wörterbuch")
    print("(English As She Is Spoke)")
elif erg > 3 and erg <= 10:
    print("*** Gerade in Arbeit ***")    
else:
    print("Dazu hat Monty Python nichts zu sagen")


