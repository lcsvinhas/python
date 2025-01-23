'''
Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''

soma = 0
cont = 0

for c in range(1, 7):
    numero = int(input('Digite o {}º valor: '.format(c)))
    if numero % 2 == 0:
        soma += numero
        cont += 1

print('Você informou {} números PARES e a soma foi {}.'.format(cont, soma))
