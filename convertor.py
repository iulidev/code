# Realizeaza conversia unor sume in dolari si euro la cursul zilei
sume = ['100$', '20E', '33$', '44.20E']
rata_conversie_dolar_leu = 4.1
rata_conversie_euro_leu = 4.9
sume_lei = [float(x[:-1])*rata_conversie_dolar_leu if x[-1]=='$' else float(x[:-1])*rata_conversie_euro_leu for x in sume]
print(f'Sumele initiale: {sume}')
print(f'Sumele in lei: {sume_lei}')
# for suma in sume_lei:
#     print(f'Suma este {suma:.2f}')
print('Sumele in lei: ', end='')
[print(f'{suma:10.2f}', end = ' ') for suma in sume_lei]
print()
