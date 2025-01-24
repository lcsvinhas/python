'''
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''

galera = []
pessoas = []
maior = menor = 0

while True:
    pessoas.append(input('Nome: '))
    pessoas.append(float(input('Peso: ')))
    if len(galera) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
    galera.append(pessoas[:])
    pessoas.clear()
    continuar = input('Quer continuar? [S/N] ').strip().lower()[0]
    if continuar != 's':
        break

print('-=' * 30)
print(f'Ao todo, você cadastrou {len(galera)} pessoas.')
print(f'O maior peso doi de {maior}Kg. Peso de ', end='')

for c in galera:
    if c[1] == maior:
        print(f'[{c[0]}] ', end='')

print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')

for c in galera:
    if c[1] == menor:
        print(f'[{c[0]}] ', end='')

print()
