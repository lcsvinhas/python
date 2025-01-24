'''
Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
'''

from time import sleep

boletim = []

while True:
    nome = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    boletim.append([nome, [n1, n2], media])
    resp = input('Quer continuar? [S/N] ').strip().lower()[0]
    if resp != 's':
        break

print('-=' * 30)
print(f'{'Nº':<4}{'NOME':<10}{'MÉDIA':>8}')
print('-' * 25)

for i, a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

print('-' * 25)

while True:
    mostrar = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
    if mostrar <= len(boletim) - 1:
        print(f'Notas de {boletim[mostrar][0]} são {boletim[mostrar][1]}')
    if mostrar == 999:
        print('FINALIZANDO...')
        break

sleep(1)
print('<<< VOLTE SEMPRE >>>')
