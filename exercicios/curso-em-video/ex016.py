# COM MÓDULOS

from math import trunc
numero = float(input('Digite um número: '))
print('O númeor digitado foi {} e sua porção inteira é {}'.format(numero, trunc(numero)))

# SEM MÓDULOS

numero = float(input('Digite um número: '))
print('O númeor digitado foi {} e sua porção inteira é {}'.format(numero, int(numero)))