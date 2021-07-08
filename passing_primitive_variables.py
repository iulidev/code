# Passing primitive variables to functions as parameters
# Primitive variables = variabile de tipurile de baza (int, float, str, boolean)
# Basic data types variables (variabilele cu date de baza, primitive : int, str, float, boolean) - sunt immutable
# O functie poate modifica o variabila avand tip immutable doar daca o intoarce prin return
# Prin return putem intoarce mai multe variabile


number = 4
v1 = 7
v2 = 2

def square(x):
    """Ridica x la patrat"""
    x = x**2 # x = x*x - x local variable
    print(f'x in interiorul functiei {x}')
    return x

def cat_rest(a, b):
    """
    Calculeaza catul si restul impartirii celor doi parametri intregi
    Returneaza catul si restul
    """
    cat = a // b
    rest = a % b
    return cat, rest

def create_name(nume, prenume):
    nume = nume + ' '+ prenume # full_name = ' '.join(nume, prenume)
    return nume

number = square(number) # transmitem ca argument un int functiei square
print(f'Valoarea lui number la patrat {number}')

c, r = cat_rest(v1, v2) # putem prelua prin enumerare rezultatele multiple ale unei functii
print(f'Catul este {c} si restul este {r}')
nume, prenume, g = "Sima", "Marian", 789
print(f'Nume = {nume} si prenume = {prenume}')
print(g)

new_name = create_name("Alex", "Dobre")
print(f'Nume intreg = {new_name}')