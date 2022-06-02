sum_pairs = 0
for i in range(85, 907):
    if (i % 2 == 0):
        print(f'Este número é par {i}')
        sum_pairs += i
print(sum_pairs)