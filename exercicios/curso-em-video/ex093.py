'''
Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''

jogador = {}
gols = []
jogador['nome'] = input('Nome do jogador: ')
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for p in range(1, partidas + 1):
    gol = gols.append(int(input(f'      Quantos gols na partida {p}? ')))

jogador['gols'] = gols[:]
jogador['total'] = sum(gols)

print('-=' * 30)
print(jogador)
print('-=' * 30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')

for i, v in enumerate(jogador['gols']):
    print(f'        => Na partida {i + 1}, fez {v} gols.')

print(f'Foi um total de {jogador["total"]} gols.')
