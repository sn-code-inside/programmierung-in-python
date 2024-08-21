class Person:
    def __init__(self,name,alter):
        self.name = name
        self.alter = alter

    def __del__(self):
        print("In der Regel nicht notwendig")

    def lautgeben(self):
        print("Mein Name ist",self.name,"und ich bin", self.alter, "Jahre alt.")

obj = Person("Herby", 5)
print(obj.name, obj.alter)
obj.lautgeben()
del obj
