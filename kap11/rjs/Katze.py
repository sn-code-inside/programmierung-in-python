from rjs.Tier import *

class Katze (Tier):
    def __init__(self,alter,name):
        Tier.__init__(self,alter)
        self.name = name

