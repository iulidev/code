# Lists comprehensions - metoda de a genera o lista noua pe baza unei liste vechi, dupa un criteriu de selectie/generare
# Sintaxa lista_noua = [expresie for value in old_list]
# Sintaxa lista_noua = [expresie for value in iterable]
numbers = [4, 7, 2, 11, 0, 55, 7]
# Cream o lista in care stocam valori duble, pe baza listei numbers
doubles = []
for val in numbers:
    doubles.append(2*val)
print('Lista numbers:', numbers)
print('Lista valorilor dublate:', doubles)

doubles_c = [2*val for val in numbers]
print('Lista dubluri folosind lists comprehensions:', doubles_c)


# Cream o lista care sa contina lungimile stringurilor din alta lista 
names = ['Alex', 'Ion', 'Alexandru']
lengths = []
for name in names:
    lengths.append(len(name))
print('Lista cu dimensiunea stringurilor:', lengths)

lengths_c = [len(name) for name in names]
print('Lista lungimilor cu lists comprehensions', lengths_c)

# Generam o lista de caractere pe baza unui string
curs = 'Python developer'
chars = [char for char in curs]
print('Lista caracterelor:', chars)

chars_without_e = [c for c in curs if c != 'e']
# Sintaxa extinsa: [expresie for value in iterable if conditie_filtrare]
print('Lista caracterelor, excluzand e:', chars_without_e)

evens = [x for x in numbers if x % 2 == 0 ]
print('Lista valorilor pare generata cu lists comprehensions', evens)
# Generam o lista cu patratele valorilor impare din numbers
square_odds = [value**2 for value in numbers if value % 2 == 1]
print('Lista patratelor valorilor impare:', square_odds)

# ternary if-else operator
price = 20
price_over_limit = True if price > 100 else False
# price_over_limit = 1 if price > 100 else 0
print('Price limit check:', price_over_limit)

# Sintaxa extinsa (if else operator): lista_noua = [expresie_if_else for value in iterable]
# Generam o lista care sa contina valorile din numbers daca valoare este para, altfel stocheaza 0
evens_list = [value if value % 2 == 0 else 0 for value in numbers]
print('Lista noua cu valori pare si zero pe pozitiile valorilor impare:', evens_list)

numbers2 = [x + 2 if x > 6 and x <=20 else x - 10 for x in numbers]
print('Lista obtinuta prin comprehension cu o expresie mai complexa:', numbers2)