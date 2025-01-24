'''
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''

from time import sleep

pvalor = float(input('Primeiro valor: '))
svalor = float(input('Segundo valor: '))
opcao = 0

while opcao != 5:
    print('[1] somar \n[2] multiplicar \n[3] maior \n[4] novos números \n[5] sair do programa')
    opcao = int(input('Qual a sua opção? '))
    if opcao == 1:
        print('A soma de {} + {} é {}'.format(pvalor, svalor, pvalor + svalor))
    elif opcao == 2:
        print('O produto de {} x {} é {}'.format(
            pvalor, svalor, pvalor * svalor))
    elif opcao == 3:
        if pvalor > svalor:
            print('Entre {} e {}, o maior número é {}'.format(
                pvalor, svalor, pvalor))
        elif pvalor == svalor:
            print('Os valores são iguais')
        else:
            print('Entre {} e {}, o maior número é {}'.format(
                pvalor, svalor, svalor))
    elif opcao == 4:
        pvalor = float(input('Primeiro valor: '))
        svalor = float(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 15)
    sleep(2)

print('Fim do programa! Volte sempre!')
