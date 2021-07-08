# String formatting syntax ( f-Strings)
names = ['Alex', 'Mihai', 'Maria']
print('Lista numelor:', names)
print('Lungimea listei este', len(names))
print('Ultimul element al listei este', names[-1], 'si are lungimea', len(names[-1]))

# f-Strings - formatted strings literals - permit includerea de expresii in stringuri
# sintaxa:  f'string1{expresie2}string2{expresie2}'
print(f'Lungimea listei este {len(names)}')
print(f'Ultimul element al listei este {names[-1]} si are lungimea {len(names[-1])}')

value = 5
name = 'Python'
print(f'Valoarea este {value} iar numele este {name}. Iar inmultind {2} cu {2} obtinem {2*2}')
print(f'Dublul lui {value} este {2*value}')

# Multiline strings
string1 = 'Curs de programare intr-un \
limbaj avansat, simplu, concis, orientat pe obiecte,\
interpretat si usor de invatat'
string2 = """ curs de programare
    in Python
    versiunea 3"""
print(string1)
print(string2)