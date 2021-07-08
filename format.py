# Code formatting and linting
# Scopul = asigurarea calitatii codului, readability, preventia erorilor
# Linting - analiza codului sursa din punct de vedere stilistic si sintacti
#           evidentiind posibile probleme
# Linter (lint) = tool (software) care analizeaza codul sursa (stil si sintaxa)
# flake8 - Python linter
# Standardul de calitate = PEP8 (Python Enhancement Proposal 8)
# PEP8 = Style guide pentru limbajul Python
# autopep8 - formatter pentru Python code (standardul PEP8)
# instalare formatter autopep8 -
# in windows click dreapta document - Format document - click pe Yes
#           in popup unde se propune instalarea autopep8
# Alternativa, in linux, in terminal:   pip install pep8
#                                       pip install --upgrade autopep8
# Windows - adaugare folder in PATH, in Command Prompt
# set PATH=%PATH%;C:\Users\Iulian\AppData\Roaming\Python\Python38\Scripts
# In Linux comanda este export pt a adauga folder in path
# export PATH="folder:$PATH" unde folder = /usr/bin

number = 77


def max_value(*args):
    """
    Primeste un numar arbitrar de valori
    Returneaza valoarea maxima
    """
    max = args[0]
    for value in args[1:]:
        if value > max:
            max = value
    return max


def double(v=7):
    return 2*v


print(f'Valoarea maxima este: {max(4, 7, 20, 3, 1, 5, 0, 30, 5, 2)}')
print(f'Valoarea maxima: {max(5, number)}')

curs = 'Python developer'
a, b = 5, 7
double(4)
print(f'Double apelat fara argumente: {double()}')
print(f'Double cu argument: {double(v=2)}')
