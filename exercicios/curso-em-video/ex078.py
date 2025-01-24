'''
Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''

numeros = []

for numero in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a posição {numero}: ')))

print('=-' * 30)
print(f'Você digitou os valores {numeros}')
print(f'O maior valor digitado foi {max(numeros)} nas posições ', end='')

for i, v in enumerate(numeros):
    if v == max(numeros):
        print(f'{i}... ', end='')

print(f'\nO maior valor digitado foi {min(numeros)} nas posições ', end='')

for i, v in enumerate(numeros):
    if v == min(numeros):
        print(f'{i}... ', end='')
