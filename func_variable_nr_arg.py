# Functions with a variable number of arguments
# Functii cu numar variabil de argumente/parametri
"""
Sintaxa: 
def nume_functie(*args):
    instructiuni
"""
# args - este precedat de asterix (*) pt a indica o functie cu nr variabil de argumente
# args este un iterable (putem folosi for, len, indexing...)

x = 300
def add(*args):
    """Returneaza suma valorilor date ca parametri"""
    # for index in range(len(args)):
    #     print(f'Index: {index} Valoare: {args[index]}')
    sum = 0
    for value in args:
        sum += value
    return sum

def concat_strings(*values):
    """Concateneaza stringuri date ca parametri"""
    rezultat = ''
    for value in values:
        rezultat = rezultat + value
    return rezultat

print(add(3, 5, 6))
print(add())
print(add(4, 7 , 6, 20, 40, 50))
print(add(x, 200))

# print(concat_strings(5, 6, 4, 3))
print(concat_strings('Alex','Marius','Roma'))