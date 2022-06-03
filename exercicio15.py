number = int(input('Introduza um número: '))
multiply = 0
for i in range(13):
    multiply = number * (i+1)
    print(f'{number}x{(i+1)} = {multiply}')