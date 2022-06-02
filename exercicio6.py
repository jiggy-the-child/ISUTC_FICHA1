# I guess you won't have any trouble understanding this exercise!
a = float(input("Introduza o valor de a: "))
b = float(input("Introduza o valor de b: "))

if (a % b == 0) or (b % a == 0):
    print(f'Os números {a} e {b} são múltiplos!')
else:
    print(f'Os números {a} e {b} não são múltiplos!')