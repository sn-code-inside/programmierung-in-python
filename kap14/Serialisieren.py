import pickle
import random

zahlen = []
# Zufallsgenerator initialisieren
random.seed()
i = 0
while i < 10:
    i+=1
    # Zufallszahl zwischen 1 und 1000 ermitteln
    x = random.randint(1,1000)
    zahlen.append(x)
print(zahlen)
output = open('data.pkl', 'wb')
pickle.dump(zahlen,output)
output.close()








