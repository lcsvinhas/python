# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

print('{:=^40}'.format(' PEDRA, PAPEL E TESOURA '))
print('Suas opções: \n[0] PEDRA \n[1] PAPEL \n[2] TESOURA')

opcoes = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
usuario = int(input('Qual é a sua jogada? '))

sleep(1)
print('PEDRA')
sleep(0.5)
print('PAPEL')
sleep(0.5)
print('E')
sleep(0.5)
print('TESOURA!')
sleep(1)
print('-=' * 11)
print('Jogador jogou {}'. format(opcoes[usuario]))
print('Computador jogou {}'. format(opcoes[computador]))
print('-=' * 11)

if computador == 0:
    if usuario == 0:
        print('EMPATE!')
    elif usuario == 1:
        print('JOGADOR VENCEU!')
    elif usuario == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')

if computador == 1:
    if usuario == 0:
        print('COMPUTADOR VENCEU!')
    elif usuario == 1:
        print('EMPATE!')
    elif usuario == 2:
        print('JOGADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')

if computador == 2:
    if usuario == 0:
        print('JOGADOR VENCEU!')
    elif usuario == 1:
        print('COMPUTADOR VENCEU!')
    elif usuario == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
