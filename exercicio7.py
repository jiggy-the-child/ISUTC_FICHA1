# I guess you won't have any trouble understanding this exercise!
nome1, peso1, altura1 = '', 0, 0
nome2, peso2, altura2 = '', 0, 0
for i in range(2):
    if i == 0:
        nome1 = str(input(f'Introduza o nome da {i+1}ª pessoa: '))
        altura1 = float(input(f'Introduza a altura da {i+1}ª pessoa: '))
        peso1 = float(input(f'Introduza o peso da {i+1}ª pessoa: '))
    else:
        nome2 = str(input(f'Introduza o nome da {i+1}ª pessoa: '))
        altura2 = float(input(f'Introduza a altura da {i+1}ª pessoa: '))
        peso2 = float(input(f'Introduza o peso da {i+1}ª pessoa: '))
    print('______________________________________________________')

if peso1 > peso2:
    print('Mais pesada!')
    print(f'Nome: {nome1};\nPeso: {peso1}')
elif peso2 > peso1:
    print('Mais pesada!')
    print(f'Nome: {nome2};\nPeso: {peso2}')
else:
    print('As duas pessoas têm o mesmo peso.')

if altura1 > altura2:
    print('Mais alta!')
    print(f'Nome: {nome1};\nPeso: {altura1}')
elif altura2 > altura1:
    print('Mais alta!')
    print(f'Nome: {nome2};\nPeso: {altura2}')
else:
    print('As duas pessoas têm a mesma altura.')

