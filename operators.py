# Arithmetic operators (Operatorii matematici)
print('4 * 3 = ', 4 * 3)
numar_minute_intro_zi = 24 * 60
print('Numarul de minute dintr-o zi este = ', numar_minute_intro_zi)
# Operatorul modulo %
print('Impartind 7 la 2 obtinem restul ', 7 % 2) # rezultatul ar trebui sa fie 1 (restul impartirii lui 7 la 2)
# Operatorul // - impartire cu rezultat intreg (rotunjire la intreg)
print('Rezultatul impartirii lui 7 la 2 ', 7 / 2)
print('Rezultatul impartirii intregi ', 7 // 2)
print('2 la puterea 3 este ', 2 ** 3)

# Assignment operators
x = 7
# x = x + 3
x += 3
print('Noua valoare a lui x este ', x)
numar_zile_lucratoare = 5
numar_ore_programare_zilnic = 1
total_ore_saptamanal = numar_ore_programare_zilnic * numar_zile_lucratoare
print('Scriem cod ', total_ore_saptamanal, 'ore saptamanal')
# numar_ore_programare_zilnic = numar_ore_programare_zilnic * 2
numar_ore_programare_zilnic *= 2
total_ore_saptamanal = numar_ore_programare_zilnic * numar_zile_lucratoare
print('Daca dublam numarul de ore in care programam zilnic, scriem cod', total_ore_saptamanal,' ore saptamanal')

# Comparison operators
x = 7
print('x >= 7', x >= 7)
print('x > 3', x > 3)
alfa = 3
print('Verificam daca alfa este diferit de 3', alfa!=3)
print('Verificam daca 4 este divizor al lui 12', 12 % 4 == 0)
print('Verificam daca x > alfa', x > alfa)

nr_zile = 12
print('Verificam daca nr_zile este diferit de x', nr_zile!=x) # 12!=7

# Logical operators
print()
print('Verificam daca alfa >1 si alfa <10', alfa >1 and alfa <10)
print('Verificam daca x > 2 sau x este divizibil cu 3', x > 2 or x % 3 == 0)
raining = True
print('Ploia s-a oprit, afirmatia "afara ploua" este', not raining)

# Bitwise operators
x = 7 # 0b111 
y = 4 # 0b100 
# x | y 0b111 = 7
print('x | y este ', x | y, '= ', bin(x | y))
print('x >>2 este ', x >>2, '=', bin(x>>2)) # => 0b1 = 1
print('y <<1 este ', y<<1, '= ',bin(y<<1)) # => 0b1000 = 8

# Identity operators
an = 2021
print(type(an) is int)
gas = 4.55
print(type(gas) is not float)
result = None
print(result is None)

# Membership operators
print()
curs = 'Python developer'
print("py" in curs) # False
print("Py" in curs) # True