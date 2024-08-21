while True:
    try:
        x = float(input("Bitte eine Zahl eingeben:"))
        if x==0:
            print ("Keine 0 eingeben.")
            continue
        inverse = 1.0 / x
        print(inverse)
    except (ValueError):
        print ("Entweder einen int oder einen float eingeben.")
    finally:
        print("Finale.")
        if input("Ende mit q - weiter mit jeder anderen Taste: ")=="q":
            break

print("Ende")



