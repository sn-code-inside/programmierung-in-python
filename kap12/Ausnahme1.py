try:
    n = input("Bitte eine Ganzzahl (integer) eingeben: ")
    print(int(n) * 4)
except ValueError:
    print("Das war keine Zahl! Bitte nochmals versuchen ...")

print("Programmende")
