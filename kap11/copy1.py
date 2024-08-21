import copy
original_list = [1, 2, [3, 4]]
shallow_copy = copy.deepcopy(original_list)
# Ändern des eingebetteten Elements in der Kopie
shallow_copy[2][0] = 5
print(original_list, shallow_copy) 
