nome = input('Introduza o nome do candidato: ')
pt = abs(float(input('Introduza a nota de Português do candidato: ')))
mt = abs(float(input('Introduza a nota de Matemática do candidato: ')))
cg = abs(float(input('Introduza a nota de Conhecimentos Gerais do candidato: ')))
media = (pt + mt + cg) / 3

print(f'Nome: {nome};\nPortuguês: {pt};\nMatemática: {mt};\nConhecimentos Gerais: {cg}.')
print(f'A média do candidato é: {media}')

if (media > 7) and (pt >= 5) and (mt >= 5) and (cg >= 5):
    print('O candidato foi aprovado!')
else:
    print('O candidato foi reprovado!')