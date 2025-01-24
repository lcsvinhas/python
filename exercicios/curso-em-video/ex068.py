'''
Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''

from random import randint

print('=-' * 20)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 20)

cont = 0

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = input('Par ou Ímpar? [P/I] ').strip().upper()[0]
    print('-' * 60)
    print(f'Você jogou {jogador} e o computador {
          computador}. Total de {total}. ', end='')
    print('DEU PAR!' if total % 2 == 0 else 'DEU ÍMPAR!')
    print('-' * 60)
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')

print(f'GAME OVER! Você venceu {cont} vezes.')
