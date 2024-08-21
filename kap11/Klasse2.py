class Tier:
    eigentuemer = "Papa"
    def __init__(self,name,alter,typ):
        self.typ = typ
        self.name = name
        self.alter = alter

    def lautgeben(self):
        print("Mein Name ist ", self.name,", bin ein ", self.typ,
              " und ich bin ",  self.alter, " Jahre alt.", sep="")
        print("Miau")

obj = Tier("Herby", 5, "Kater")
print(obj.name, obj.alter, obj.typ)
obj.lautgeben()
print("Zugriff über das Objekt:", obj.eigentuemer)
print("Zugriff über die Klasse:", Tier.eigentuemer)
Tier.eigentuemer = "Felix"
print("Verkauft an", obj.eigentuemer)





