completo = []
pares = []
impares = []
while True:
    completo.append(int(input('Digite um valor: ')))
    continuar = input('Quer continuar? [S/N] ').strip().lower()[0]
    if continuar != 's':
        break
for i, valor in enumerate(completo):
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
print('-=' * 30)
print(f'A lista completa é {completo}')
print(f'A lista de pares é {pares}')
print(f'A lista completa de ímpares é {impares}')