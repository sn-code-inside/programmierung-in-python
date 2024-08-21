class Tier:
    eigentuemer = "Papa"
    def __init__(self,name,alter,typ):
        self.typ = typ
        self.name = name
        self.alter = alter

obj1 = Tier("Herby", 5, "Kater")
obj2 = Tier("Hägar", 2, "Kanarienvogel")
obj3 = Tier("Helga", 4, "Kanarienvogel")

print(obj1.name, "gehört", obj1.eigentuemer)
print(obj2.name, "gehört", obj2.eigentuemer)
print(obj3.name, "gehört", obj3.eigentuemer)
print("Alle Tiere gehören", Tier.eigentuemer, "\n")

obj1.eigentuemer = "Florian"

print(obj1.name, "gehört jetzt", obj1.eigentuemer)
print(obj2.name, "gehört jetzt", obj2.eigentuemer)
print(obj3.name, "gehört jetzt", obj3.eigentuemer)
print("Alle Tiere gehören jetzt", Tier.eigentuemer, "\n")

Tier.eigentuemer = "Felix"

print(obj1.name, "gehört jetzt", obj1.eigentuemer)
print(obj2.name, "gehört jetzt", obj2.eigentuemer)
print(obj3.name, "gehört jetzt", obj3.eigentuemer)
print("Alle Tiere gehören jetzt", Tier.eigentuemer)



