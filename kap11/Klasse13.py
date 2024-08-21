class Tier(object):
    def __init__(self):
        self.alter = 5

    def getAlter(self):
        return self.alter

class Katze(Tier):
    def getAlter(self):
        return super(Katze, self).getAlter() + 1

obj1 = Tier()
obj2 = Katze()
print(obj1.getAlter())
print(obj2.getAlter())



