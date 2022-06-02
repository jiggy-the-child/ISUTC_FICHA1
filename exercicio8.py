# I guess you won't have any trouble understanding this exercise!
number = int(input('Introduza um número: '))

if (abs(number) % 2 == 0):
    print(f'O número {number}, é par!')
    if (number < 0):
        print('E é negativo!')
    else:
        print('E é positivo!')
else:
    print(f'O número {number}, é ímpar!')
    if (number < 0):
        print('E é negativo!')
    else:
        print('E é positivo!')