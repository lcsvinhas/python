from random import randint
computador = randint(0, 10)
print('Sou seu computador... \nAcabei de pensar em um número entre 0 e 10. \nSerá que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = float(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        else:
            print('Menos... Tente mais uma vez.')
print('Você acertou com {} tentativas. Parabéns!'.format(palpites))