class Tier:
    __anzahl = 0
   
    def __init__(self):
        Tier.__anzahl += 1
        
    @classmethod    
    def AnzahlTiere(cls):
        return cls.__anzahl


print("Anzahl der Tiere: ", Tier.AnzahlTiere())
obj1 = Tier()
print("Anzahl der Tiere: ", Tier.AnzahlTiere())
obj2 = Tier()
print("Anzahl der Tiere: ", Tier.__anzahl)
