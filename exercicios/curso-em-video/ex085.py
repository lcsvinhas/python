completo = [[], []]
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        completo[0].append(valor)
    else:
        completo[1].append(valor)
print('-=' * 30)
completo[0].sort()
completo[1].sort()
print(f'Os valores pares digitados foram: {completo[0]}')
print(f'Os valores ímpares digitados foram: {completo[1]}')