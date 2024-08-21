import Tier

class Katze (Tier.Tier):

    def __init__(self,alter,name):
        Tier.Tier.__init__(self,alter)
        self.name = name
