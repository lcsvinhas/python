'''
Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
'''


def jogador(nome='<desconhecido>', gol=0):
    return f'O jogador {nome} fez {gol} gol(s) no campeonato.'


nome = input('Nome do jogador: ')
gol = input('Número de gols: ')

if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    print(jogador(gol=0))
else:
    print(jogador(nome, gol))
