class Tier:

    def __init__(self,alter):
        self.alter = alter

class Katze (Tier):

    def __init__(self,alter,name):
        Tier.__init__(self,alter)
        self.name = name

kater = Katze(5, "Herby")
print(kater.name,kater.alter)


