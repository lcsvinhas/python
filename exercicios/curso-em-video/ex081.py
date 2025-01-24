'''
Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

numeros = []

while True:
    valor = numeros.append(int(input('Digite um valor: ')))
    continuar = input('Quer continuar? [S/N] ').strip().lower()[0]
    if continuar != 's':
        break

print('-=' * 30)
print(f'Você digitou {len(numeros)} elementos.')

numeros.sort(reverse=True)

print(f'Os valores em ordem decrescente são {numeros}')

if 5 in numeros:
    print('O valor 5 foi encontrado na lista.')
else:
    print('O valor 5 não foi encontrado na lista!')
