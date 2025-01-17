from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        numeros.append(n)
        print(n, end=' ', flush=True)
        sleep(0.1)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos valores pares da lista é {soma}.')


numeros = []
sorteia(numeros)
somaPar(numeros)