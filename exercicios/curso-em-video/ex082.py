'''
Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''

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
