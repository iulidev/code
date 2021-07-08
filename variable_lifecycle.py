# Variable lifecycle = timpul cat variabila este "in viata" 
#  = timpul cat variabila este in memorie si poate fi accesata
# Variabile locale = variable lifecycle este limitat la timpul de executie al functiei in care sunt declarate
# O variabila locala este o variabila declarata in interiorul unei functii
# Variabilele locale sunt sterse din memorie la finalul executiei functiei in interiorul careia sunt declarate
# Variabila globala = o variabila creata in afara functiilor, in program (accesibila sau vizibila de oriunde)
# Prin assignment (inclusiv compus +=, *=, etc) in interiorul functiei, declaram variabile locale (se sterg la finalizarea executiei functiei)
# nu afecteaza variabilele globale cu acelasi nume
# Variable scope = domeniul de vizibilitate al unei variabile (zona din program unde este vizibila si accesibila)
# Variabilele locale sunt de scop local. Variabilele globale sunt de scop global

curs = "Python developer" # variabila globala
student = "Marius Sima" # variabila globala (global scope variable)
x = 7 # variabila globala

def show_language(nume_curs):
    """Afiseaza limbajul de programare asociat cursului dat ca parametru"""
    curs = 'Java developer' # variabila curs este declarata in interiorul functiei, este locala
    words = nume_curs.split() # imparte in substringuri folosind space ca separator
    language = words[0] # local (scope) variable
    print(f'Language for course {nume_curs} is {language}')
    print(f'Afisam variabila locala student din functia show_language {student}') # student - variabila globala
    print(f'{curs}')

def add(): # modificam o variabila globala din interiorul functiei
    global x # x este globala in functia add
    x  += 7
    # x = 3
    # print(f'Variabila x in interiorul functiei add: {x}') #3, x este local variable

show_language(nume_curs=curs)
# print(f'Limbajul este: {language}') # NameError - language este variabila locala
print(f'Curs afisat din afara functiei, dupa apelare {curs}')

# Pentru a modifica o variabila globala in interiorul functiei folosim 'global'
# Sintaxa: global nume_variabila_globala
print(f'Variabila x inainte de executia functiei add: {x}') # 7
add()
print(f'Variabila x dupa executia functiei add: {x}') # x este 14