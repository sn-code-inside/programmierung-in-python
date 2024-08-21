i = 0

class MeineAusnahme(Exception):
    pass
def werfen():
    global i
    i+=1
    if i > 3: raise (MeineAusnahme())

while True:
    try:
        werfen()
        print(i)
    except MeineAusnahme:
        print ("Ausnahme")
        break
    
print("Und nun ist das Programm zu Ende")
