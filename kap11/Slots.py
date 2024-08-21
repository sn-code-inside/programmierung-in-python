class Tier():
    __slots__ = ['alter']
    def __init__(self):
        self.alter = 5

obj1 = Tier()
print(obj1.alter)
obj1.name = "Herb"
