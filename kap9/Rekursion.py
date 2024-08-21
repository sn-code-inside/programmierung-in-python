i = 0
def fkt():
    global i
    i += 1
    if i < 10:
        fkt()
fkt()
print(i)







