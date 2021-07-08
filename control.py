# Controlul executiei prin structuri de control
a = 4
b = 6
if a > b:
    print('Maximul este', a)
else:
    print('Maximul este', b)
x = -3
if x > 0:
    print('Numarul este pozitiv')
elif x == 0:
    print('Numarul este zero')
else:
    print('Numarul este negativ')
raining = True
if raining == True:
    print('Afara ploua')

# for element in secventa:
#    bloc_instructiuni
for element in range(2, 7, 2):
    print(element)
curs = 'Python'
for char in curs:
    print(char)

# while conditie:
#   bloc_instructiuni

i = 0
while i < 6:
    print(i)
    i += 1

for i in range(6):
    print(i)

#afisam numerele impare de la zero la 7
j=0
while j < 8:
    j+=1
    if j%2 ==0:
        continue
    print(j)

while True:
    string = input('Enter x pentru a termina:')
    if string == 'x':
        break