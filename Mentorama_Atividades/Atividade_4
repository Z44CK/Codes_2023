setx = {'apple', 'mango'}
sety = {'mango', 'orange'}
setz = {'mango'}

unindo = setx | sety | setz
print(unindo)

elemento_comun = setx & sety & setz
print(elemento_comun)

if setz.issubset(setx and sety):
    print(f'setz e subconjunto de setx e sety')
else:
    print('setz nao e subconjunto de setx e sety')

elemento_setx = setx - sety
print('Elementos presentes apenas no setx que nao tem no sety: ')
for elemento in elemento_setx:
    print(elemento)


# ----------------- exemplo com difference():

setx = {'apple', 'mango', 'orange'}
sety = {'mango', 'orange'}
elemento_setx = setx.difference(sety)
print('Elementos presentes apenas no setx que nao estao no sety: ')
for elemento in elemento_setx:
    print(elemento)
