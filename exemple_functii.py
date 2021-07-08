# Exemple functii
# Regula ordine parametri 
# def nume_functie(pos1, pos2, *args, keyw1, keyw2)
# def nume_functie(pos1, pos2, keyw1, keyw2)

# variadic functions (functii cu numar variabil de parametri *args)
# Pentru a apela o functie doar cu argumente named (keyword) indicam ca 
# functia are zero parametri pozitionali prin def nume_functie(*, keyw1, keyw2, keyw3)


start = 10
# 2*start_value + suma(nr_variabil_de_valori)


def double_start_and_add(start_value, *args): # start_value este required
    """
    Calculeaza dublul lui start_value si aduna la valoarea obtinuta 
    parametrii transmisi in lista cu numar variabil de parametri
    """
    sum = 2 * start_value
    for value in args:
        sum += value # sum = sum + value
    return sum

def double_end_and_add(*args, end_value): # end_value este required keyword-only only
    """
    Calculeaza dublul lui end_value si aduna la valoarea obtinuta 
    parametrii transmisi in lista cu numar variabil de parametri
    """
    sum = 2* end_value
    for value in args:
        sum += value
    return sum

def ridicare_la_putere(*, baza, exponent): # fortam apelarea functiei cu keyword arguments
    """Returneaza baza la puterea exponent"""

    return baza**exponent


print(f'Suma este: {double_start_and_add(start, 4, 6, 8, 9)}')

print(f'Suma este: {double_start_and_add(start, 4, 6, 8, 9)}')
print(f'Suma este: {double_start_and_add(start, 4, 9)}')
print(f'Suma este: {double_start_and_add(start)}')
# print(f'Suma cand nu transmitem nici un argument: {double_start_and_add()}')
print(f'Suma dubland valoarea de la sfarsit: {double_end_and_add(4,5, end_value=6)}')
print(f'Ridicam {5} la puterea {2}: {ridicare_la_putere(baza=5, exponent=2)}')
print(ridicare_la_putere(baza=5, exponent=6))

# 1. o functie my_max(*args) cu numar variabil de parametri care calculeaza maximul valorilor transmise (prin *args)
# 2. o functie care schimba intre ele valorile celor doi parametri si le returneaza pentru a fi asignate variabilelor
# x, y = switch(x, y) => a, b = b, a sau cu o valoare intermediara
# 3. o functie care "curata" un string (elimina spatii de la inceput si sfarsit si schimba prima litera sa fie upper case si restul lower case)

