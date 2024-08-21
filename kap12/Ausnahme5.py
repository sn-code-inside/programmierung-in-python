while True:
    try:
        x = float(input("Bitte eine Zahl eingeben:"))
        if(x==0):
            print ("Keine 0 eingeben,")
            break
        inverse = 1.0 / x
        print(inverse)
        if(input("Ende mit q - weiter mit jeder anderen Taste: ")=="q"): break

    except (ValueError):
        print ("Entweder einen int oder einen float eingeben.")
        if(input("Ende mit q - weiter mit jeder anderen Taste: ")=="q"): break
    finally:
        print("Das ist das Finale - trotz break.")
    print ("Auf zum nächsten Schleifendurchlauf")

print("Und nun ist das Programm zu Ende")




