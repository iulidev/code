curs = "Python developer"
for character in curs:
    print(character)
print('Lungimea este : ', len(curs))
if 'Dev' in curs:
    print('Stringul Dev este in ', curs)
else:
    print('Stringul Dev nu este in ', curs)

# array = o secventa de valori de acelasi tip, ordonata si schimbabila
# list = colectie ordonata (indexata) de elemente
# Listele spre deosebire de arrays pot avea elemente de tip diferit
# Sintaxa de declararea/crearea unei liste este nume_lista = [elemente_separate_prin_virgula]
numbers = [7, 21, 4, 3, 21, 20] # lista de valori int
cars = ["Sandero 1.4", "VW Golf 6", "Duster 4x4"] # lista de strings
prices = [4.56, 5.32, 6.01, 6.14] # lista de valori float
my_empty_list = [] #empty list
new_numbers = list([7, 33, 999, 12, 0])
lst = list() # empty list
# index = pozitia in lista, porneste de la 0
# element = item (valoare din lista)
print('Element de la index 0:', numbers[0])
print('Item de la index 3', numbers[3]) #3
print('Pretul cu index 2', prices[2]) # 6.01
# print('Pretul cu index 10', prices[10])
diff_list = [3, "three", 4.55, True]
print('Lista cu valori de tip diferit', diff_list)

# list si str au in comun indexing (accesare element pe baza index), len() = determina lungimea
# list si str sunt iterables (iterabile, pot fi parcurse elementele, unul cate unul, intr-un for)
print('Lungimea listei numbers este:', len(numbers))
print('Caracterul avand index 4:', curs[4])

for n in numbers:
    print(n)

# negative indexes - elementele de la sfarsitul listei cand nu ii stim lungimea
print('Primul element, afisat folosind index negativ', numbers[-6])
print('Primul element, afisat folosind index negativ', numbers[-len(numbers)])
print('Ultimul element din lista este, afisat cu index negativ -1', numbers[-1])
print('Ultimul caracter al stringului curs', curs[-1])

# slicing - accesarea unei felii din lista (o sublista respectiv substring)
# sintaxa nume_lista[start:stop:step]
for value in range(2, 7, 2):
    print(value)
print('Sublista din numbers intre 2 si 5 este: ', numbers[2:5]) # exclusiv stop (de la start pana la stop-1)
print('Primele 3 caractere din stringul curs: ', curs[:3])
print('Valorile din numbers, incepand cu pozitia 4', numbers[4:])
# ultimele n elemente folosim lista[len(lista)-n:]
print('Ultimele 4 caractere din curs sunt:', curs[len(curs)-4:])
my_substring = curs[2:4]
print('Slice from 2 to 4', my_substring)
new_list = numbers[3:5:2]
print('O felie din numbers:', new_list)
numbers_2 = numbers[:]
print('Copia listei numbers', numbers_2)
