def multiplizieren(*b, a): # b ist eine Liste variabler länge
    erg = a
    for i in b:
        erg *=i
    print(erg)
multiplizieren(6)
multiplizieren(6, 1)
multiplizieren(6, 1, 1)


