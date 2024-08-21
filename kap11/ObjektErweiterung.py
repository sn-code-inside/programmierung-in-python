class Tier():
    def __init__(self):
        self.alter = 5

obj1 = Tier()
print("Das Dictionary  __dict__:", obj1.__dict__,"\n")
obj1.name = "Herby"
print(obj1.alter)
print(obj1.name)
print("Das Dictionary  __dict__:", obj1.__dict__,"\n")
def lautgeben():
    print ("Miau")
obj1.lautgeben = lautgeben
obj1.lautgeben()
print("Das Dictionary  __dict__:", obj1.__dict__,"\n")
obj1.fressen = lambda x: print (x)
obj1.fressen("Mampf")
print("Das Dictionary  __dict__:", obj1.__dict__,"\n")


