from random import randint
from time import sleep
lista = []
jogos = []
cont = 0
print('-' * 45)
print(f'{'JOGA NA MEGA SENA':^45}')
print('-' * 45)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'-=-=-=-=-=-=- SORTEANDO {quant} JOGOS -=-=-=-=-=-=-')
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(0.5)
print(f'-=-=-=-=-=-=-=- < BOA SORTE! > -=-=-=-=-=-=-=-')