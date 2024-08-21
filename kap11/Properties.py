class Katze:
    def __init__(self,alter):
        self.__alter = alter

    def __getAlter(self):
        return self.__alter

    def __setAlter(self, alter):
        self.__x = alter

    alter = property(__getAlter, __setAlter)
obj = Katze(1)
print(obj.alter)
obj.alter = 5;
print(obj.alter)


