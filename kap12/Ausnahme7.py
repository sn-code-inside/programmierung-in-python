while True:
    try:
        x = float(input("Bitte eine Zahl eingeben:"))
        inverse = 1.0 / x
        print(inverse)
        if input("Ende mit q - weiter mit jeder anderen Taste: ")=="q":
            break
    except (ValueError,ZeroDivisionError)  as e:
        print(e.args[0])

        if input("Ende mit q - weiter mit jeder anderen Taste: ")=="q":
            break

print("Und nun ist das Programm zu Ende")





