# Passing arguments
"""
1/ Argumente pozitionale (Positional arguments) - valorile parametrilor sunt transmise pe baza pozitiei
2/ Argumente numite (Named sau keyword arguments) - valoarile transmise functiei sunt identificate pe baza numelui
Avantajul argumentelor numite (keyword) - nu ne mai intereseaza ordinea
3/ Argumente cu valori implicite (Default arguments)
Regula: Argumentele pozitionale sunt mentionate inaintea celor keyword (numite) la apelul functiei
"""

def suma(x, y):
    s = x + y
    print('y este', y)
    return s

def f(a, b=10): # default value for b - b este optional
    print('a + 2*b = ', a+2*b)

print(suma(3, 5)) # positional arguments
num = 20
val = 10
print(suma(val, num)) # positional arguments
print(suma(3, y=20)) # positional primii, keyword dupa argumentele pozitionale
# print(suma(y=20, 4)) Syntax error
print(suma(x=3, y=5)) # keyword arguments 
print(suma(y=55, x =22)) # keyword arguments

f(4, 6) # positional arguments
f(b=8, a =1) # keyword arguments
f(3)

# insert
numbers = [2, 5, 6, 51]
numbers.insert(20, 3)

# print
print ('Un text', end=' .')
print('Alt text', end = ' =')
