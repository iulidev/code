# Nested lists (liste imbricate) - liste avand elemente de tip lista
numbers = [3, 5, 6, 7]
dif_list = [True, 'Alfa', 5, 2.22, 3, 4.444]
nested_list = [[3, 5, 4], [8, 9, 22, 33, 11], [3,5], [6]]
print(nested_list, len(nested_list))
for l in nested_list:
    print(len(l))
    print(l)
print('Ultimul element din lista', nested_list[-1]) # [6]
print('Al doilea element al listei de la index 0', nested_list[0][1]) # 5

# multidimensional arrays (matrice) - elementele listei sunt liste cu aceeasi lungime
matrix = [[1, 2, 5, 6], [4, 7, 8, 1]]
print('Matrice 2x4',matrix)
# afisare elemente de tip lista, 
for l in matrix:
    print(l)
# afisare elemente din interiorul listelor din lista
for l in matrix:
    for element in l:
        print(element)
if [3, 5] in nested_list:
    print('Am gasit [3,5]')
nested_list[1][1] = 999
print('Lista dupa suprascriere', nested_list)
matrix[1][2] = 777
print('Matrix dupa suprascriere valoare', matrix)
matrix[1].append(4444)
matrix[0].append(0)
print('Matrix dupa append', matrix)
matrix2 = [
    [3, 2, 1, 5],
    [4, 5, 44, 1],
    [3, 2, 11, 22]
] # matrix 3x3
print('A doua matrice', matrix2)
for row in matrix2:
    print(row)

