# here too, just some basics...
number = int(input('Introduza um número: '))
multiply = 0
# we already saw range;
for i in range(13):
    multiply = number * (i+1)
    # and f strings.
    print(f'{number}x{(i+1)} = {multiply}')