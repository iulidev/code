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
removed_value = numbers.pop()
print('Lista numbers dupa stergerea valorii', removed_value, 'este:', numbers)
removed_from_index_2 = numbers.pop(2)
print('Lista numbers dupa extragerea item cu index 2', removed_from_index_2, 'este:', numbers)

del numbers[2]
print('Lista numbers dupa stergere item cu index 2', numbers)
# del numbers[:2]
# print('Lista numbers, dupa stergere cu del si slicing', numbers)
# del numbers
# print('Lista numbers', numbers)

# numbers.clear()
# print('Lista numbers dupa aplicarea clear:',numbers)
valoare_de_sters = 7
if valoare_de_sters in numbers:
    numbers.remove(valoare_de_sters)
    print('Lista numbers dupa stergere',valoare_de_sters,'este', numbers)
else:
    print(valoare_de_sters, 'nu este in numbers')
