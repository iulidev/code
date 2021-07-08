# Splitting and joining strings (Divizare si imbinare stringuri)
text = 'Learning Python is fun'

# Generam lista de caractere din string
list_of_chars = [x for x in text]
print('Lista de caractere este:', list_of_chars)

# Splitting (divizare) a unui string in substringuri pe baza unui separator
# implicit separatorul = space
# sintaxa este lista_substringuri = string.split(string_separare)
lista_substrings = text.split()
print('Lista de subsiruri este:', lista_substrings)
lista2 = text.split(' is ')
print('Lista de substringuri folosing split cu separatorul " is ":',lista2)

# Joining (imbinare) a unor stringuri intr-un string
# sintaxa este string_de_imbinare.join(lista_stringuri)
names = ["Maria", "Ion", "Alex"]
all_names = " ".join(names)
print('Stringul obtinut prin join este', all_names) 
all_names_and_used = " and ".join(names)
print('Joining strings cu " and " va genera', all_names_and_used)

# Transformarea unei liste de caractere (array of chars) intr-un string
lista_c = ['a', 'l', 'e','x']
s = ''.join(lista_c)
print('Stringul obtinut prin join aplica listei de caractere:', s)