class A:
    def reden(self):
        print("A")
class B(A):
    def reden(self):
        print("B")
class C(A):
    def reden(self):
        print("C")
class D(B, C):
    pass
d = D()
d.reden()
