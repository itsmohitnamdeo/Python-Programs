print ('>> Mohit Namdeo')
print ('>> Program to Remove Duplicate Element From a List')

print ('Using set()')

list_1 = [1, 2, 1, 4, 6]

print(list(set(list_1)))

print ('Remove the items that are duplicated in two lists')
list_1 = [1, 2, 1, 4, 6]
list_2 = [7, 8, 2, 1]

print(list(set(list_1) ^ set(list_2)))