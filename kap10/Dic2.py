teilnehmer = {}
op = ""
while op != "A":
    name = input("Name\n")
    firma = input("Firma\n")
    teilnehmer.update({name:firma})
    print(teilnehmer)
    op = input("(A)bbruch oder weiteren Wert aktualisieren/hinzufügen?\n")






