class Tier:
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






