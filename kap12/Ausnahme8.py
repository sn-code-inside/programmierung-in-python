i = 0
def werfen():
    global i
    i+=1
    if i > 3: raise
while True:
    try:
        werfen()
        print(i)
    except :
        print ("Ausnahme")
        break
    
print("Und nun ist das Programm zu Ende")
