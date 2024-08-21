menge1 = set()
i = 1
while i < 10:
    menge1.add(i * 3)
    i += 1
print(menge1)
menge2 = {"a","b","c", "d"}
print(menge2)
i = 0
while i < 5:
    menge2.add(menge1.pop())
    i += 1
print(menge2)
print(menge1)







