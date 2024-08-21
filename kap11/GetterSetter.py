class Katze:
    def __init__(self,alter):
        self.__alter = alter

    def getAlter(self):
        return self.__alter

    def setAlter(self, alter):
        self.__alter = alter

obj = Katze(1)
print(obj.getAlter())
obj.setAlter(5);
print(obj.getAlter())


