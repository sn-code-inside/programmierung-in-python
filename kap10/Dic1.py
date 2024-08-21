person = ("Meier","Otto")
print(person[0])
person2 = {"vorname":"Otto","nachname":"Meier"}
print(type(person2))
print(person2)
print(person2["vorname"])
for v in person2.values():
    print(v)
print(person2.keys())
numindex = {1:0,2:True}
boolindex={True:False,False:True}
print(boolindex[True])
tupelindex={(1,2):True,(1,2,3):False}
print(tupelindex[(1,2,3)])
#warumgehtdasnicht = {[1,2]:True,[1,2,3]:False}





