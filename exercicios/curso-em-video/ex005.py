# Exercício Python 005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

numero = int(input('Digite um número: '))

print('O antecessor do número {} é {} e o sucessor é {}.'.format(
    numero, (numero-1), (numero+1)))
