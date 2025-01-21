# Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

# COM MÓDULOS
from math import trunc

numero = float(input('Digite um número: '))

print('O númeor digitado foi {} e sua porção inteira é {}'.format(
    numero, trunc(numero)))

# SEM MÓDULOS
numero = float(input('Digite um número: '))

print('O númeor digitado foi {} e sua porção inteira é {}'.format(numero, int(numero)))
