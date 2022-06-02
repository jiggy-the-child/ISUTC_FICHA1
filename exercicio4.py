# I guess you won't have any trouble understanding this exercise!
a = float(input("Introduza o valor de 'a': "))
b = float(input("Introduza o valor de 'b': "))
c = float(input("Introduza o valor de 'c': "))

sum_a_b = a + b

if (sum_a_b < c):
    print('A soma de (a + b) é menor que c.')
else:
    print('A soma de (a + b) é maior ou igual a c.')