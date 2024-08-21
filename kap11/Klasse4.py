class Tier:
    anzahl = 0
   
    def __init__(self):
        Tier.anzahl += 1
        
    @classmethod    
    def AnzahlTiere(cls):
        return cls.anzahl


print("Anzahl der Tiere: ", Tier.AnzahlTiere())
obj1 = Tier()
print("Anzahl der Tiere: ", Tier.AnzahlTiere())
obj2 = Tier()
obj3 = Tier()
print("Anzahl der Tiere (Abfrage für die Klasse): ", Tier.AnzahlTiere())
print("Anzahl der Tiere (Abfrage für eine Instanz): ", obj2.AnzahlTiere())
