class Tier:

    def __init__(self,alter):
        self.alter = alter

class Eigentuemer:

    def __init__(self,wohnort):
        self.wohnort = wohnort
    
class Katze (Tier,Eigentuemer):

    def __init__(self,alter,name, wohnort):
        Tier.__init__(self,alter)
        Eigentuemer.__init__(self,wohnort)
        self.name = name

kater = Katze(5, "Herby","Bodenheim")
print(kater.name,kater.alter,kater.wohnort)


