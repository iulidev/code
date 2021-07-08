# Lists concatenation - lipirea de liste (Merge)
list1 = [4, 6, 2, 0, -1, 22, 4, 2, 33]
list2 = [7, 9, 22, 33, 1, 0]

# Concatenare cu operatorul +
list3 = list1 + list2
print('Rezultatul concatenarii cu operatorul +', list3)
# print('Lista obtinuta prin multiplicare *', list1*3)

# Concatenare cu append si for
# for element in list2:
#     if element > 10:
#         list1.append(element)
# print('Lista 1 dupa concatenarea folosind for si append', list1)

# Concatenare folosind metoda extend()
# Sintaxa lista.extend(lista_de_lipit)

list1.extend(list2)
print('Lista 1 dupa aplicare extend', list1)

# copy - realizeaza un duplicat
list4 = list1.copy()
print('Lista obtinuta prin duplicare', list4)
nested_list = [
    [3, 4, 5, 6],
    [4, 6, 4, 0],
    [3, 5, 3, 0]
]
print(nested_list)