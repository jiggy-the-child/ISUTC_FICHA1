list_numbers = [
    -23, 40, 53, 71, -93, 94, 38, 15, -18, -91, -61, -92, 90, -33, -92, 87, 93, -73, -30, 64, -54, -1, -51, -70, 23, -13, -38, 72, 38, 40, -63, -26, 40, -39, -98, 8, \
        96, -65, 93, 35, 92, -23, -90, -9, -51, 23, -88, -89, 84, 93
]
soma_positivos = 0
count_negativos = 0

for i in list_numbers:
    if (i > 0):
        soma_positivos += i
    else:
        count_negativos += 1

print(f'A soma dos números positivos é: {soma_positivos}')
print(f'A contagem dos números negativos é: {count_negativos}')