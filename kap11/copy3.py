original_list = [1, 2, [3, 4]]
assignment_copy = original_list  # Kopieren durch Zuweisung
# Ändern des eingebetteten Elements in der Kopie
assignment_copy[2][0] = 5
print(original_list, assignment_copy)  

