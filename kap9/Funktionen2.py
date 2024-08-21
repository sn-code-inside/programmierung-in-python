def rechnen(a,b = 8): # optionaler Parameter b
    print(a*b)
def multiplizieren(a, *b): # b ist eine Liste variabler länge
    erg = a
    for i in b:
        erg *=i
    print(erg)
rechnen(6)
rechnen(6,7)
multiplizieren(6)
multiplizieren(6, 1)
multiplizieren(6, 1, 1)


