'''
Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. 
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''

numero = int(input('Digite um número para calcular seu fatorial: '))
cont = numero
fat = 1

print('Calculando {}! = '.format(numero), end='')

while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fat *= cont
    cont -= 1

print('{}'.format(fat))
