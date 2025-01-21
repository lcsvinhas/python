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
