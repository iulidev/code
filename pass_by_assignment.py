# Passing arguments to function by assignment
# 1/ Argumentele sunt variabile de tip immutable (str, int, float, bool) la assignment in interiorul functiei se creeaza o variabila locala
# Daca vrem sa modificam valoarea argumentelor, folosim return si assignment pentru a se reflecta modificarile in program
# 2/ Argumentele sunt mutable (schimbabile in-place, se pot rescrie items, de exp list) - la assignment in interiorul functiei se creeaza tot variabila locala
# 2.1/ Argumentele mutable se pot "modifica" daca le returnam si asignam noua valoare intoarsa, similar cu 1/
# 2.2/ Argumentele mutable, daca se modifica in-place (append, assignment pe baza de index, insert, etc), daca suprascriem un item sau inseram unul (operatii de mutare)
# se realizeaza "pass by assignment" in sensul ca modificarea va fi reflectata in program fara a se folosi return

# Pass by assignment inseamna ca argumentele se vor comporta diferit in functie de tipul lor
# Cand folosim argumente mutable si suprascriem elemente (schimbam/mutam argumentul in interiorul functiei) - schimbarea se reflecta dupa finalizarea functiei in program
# Mecanismul este similar cu "Pass by reference" din alte limbaje de programare
# Un al doilea mecanism de transmitere a argumentelor este "Pass by value" relativ similar cand realizam assignment in interiorul functiei (atat pt mutable cat si pt immutable data)
# Pass by assignment functioneaza pentru ca Python creeaza variabile ca referinte catre obiecte (=reprezentari concrete ale unor tipuri de date)
# Este esential daca acele obiecte sunt sau nu mutable pentru a determina daca modificarile (mutarile) se reflecta in afara functiei asupra argumentelor transmise

# Modificarile elementelor listelor, transmise ca argumente functiilor, se reflecta in afara functiei fara sa fie necesar return
# Modificarile oricarui tip de argumente transmise functiilor se pot reflecta prin return si assignment

x = 7
gl = ['old', 6, 20]

def double(number):
    """Dubleaza valoarea parametrului number"""
    number *=2 # se creeaza o variabila locala
    return number

def f(my_list):
    my_list = [3, 5] # se creeaza o variabila locala
    print(f'Lista din interiorul functiei f este {my_list}')
    return my_list

def g(lst):
    lst[0] = 'new'
    lst[1]+=1
    lst.append(77)
    print(f'Lista din interiorul functiei {lst}')


x = double(x)
print(f'Dublul lui x este {x}')

l = [6, 7]
print(f'Lista l inainte de executia functiei f: {l}')
l = f(l)
print(f'Lista l dupa executia functiei f: {l}')

print()
print(f'Lista gl inainte de executia functiei g: {gl}')
g(gl)
print(f'Lista gl dupa executia functiei g: {gl}')