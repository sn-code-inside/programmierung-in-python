def multiplizieren(a, b):
    print(a * b)
def multi(a, b):
    return a * b
def ausgabe():
    print("Ein Kratzer?! Ihr Arm ist ab!")
    print("Nein, das stimmt nicht.")
def rechnen(a, b, c):
    if c == "*":
        return multi(a, b)
    elif c == "+":
        return a + b
    elif c == "-":
        return a - b
    elif c == "/":
        return a / b
ausgabe()
multiplizieren(6,7)
print(rechnen(7,6,"*"))
print(rechnen(22,20,"+"))
