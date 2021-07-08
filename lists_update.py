curs = "Python developer"
# array = o secventa de valori de acelasi tip, ordonata si schimbabila
# list = colectie ordonata (indexata) de elemente
# Listele spre deosebire de arrays pot avea elemente de tip diferit
# Sintaxa de declararea/crearea unei liste este nume_lista = [elemente_separate_prin_virgula]
numbers = [7, 21, 4, 3, 21, 20] # lista de valori int
cars = ["Sandero 1.4", "VW Golf 6", "Duster 4x4"] # lista de strings
prices = [4.56, 5.32, 6.01, 6.14] # lista de valori float
my_empty_list = [] #empty list
new_numbers = list([7, 33, 999, 12, 0])
# index = pozitia in lista, porneste de la 0
# element = item (valoare din lista)

# list si str au in comun indexing (accesare element pe baza index), len() = determina lungimea
# list si str sunt iterables (iterabile, pot fi parcurse elementele, unul cate unul, intr-un for)
# list - mutable (schimbabile, putem suprascrie valorile items), strings - immutable
# negative indexes - elementele de la sfarsitul listei cand nu ii stim lungimea
# slicing - accesarea unei felii din lista (o sublista respectiv substring)
# sintaxa nume_lista[start:stop:step]
# ultimele n elemente folosim lista[len(lista)-n:]
# Update list (suprascriere elemente) - [], [:], append - la sfarsit, insert - la un index
print('Lista numbers', numbers)
numbers[2] = 77
print('Lista numbers, dupa suprascriere item cu index 2', numbers)
# curs[2] ='j' String - immutable (nu se pot suprascrie caractere)
# print('Update string curs ',curs)
# curs = 'Python learning'
# print(curs)
numbers[2:4]=[0, -3]
print('Lista numbers dupa update aplicand slicing operator ', numbers)

numbers.append(121)
print('Lista dupa append', numbers)
numbers.insert(2, 3233)
print('Lista numbers dupa insert in pozitia 2', numbers)