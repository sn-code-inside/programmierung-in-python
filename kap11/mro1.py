class A: 
    i = 42
class B:
    i = 1
class C(A,B):
    def __init__(self):
        print(super().i)
C()