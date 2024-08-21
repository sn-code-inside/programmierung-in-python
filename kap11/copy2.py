import copy
original_list = [1, 2, [3, 4]]
deep_copy = copy.deepcopy(original_list)
# Ändern des eingebetteten Elements in der Kopie
deep_copy[2][0] = 5
print(original_list, deep_copy) 
