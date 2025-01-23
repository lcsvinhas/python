'''
Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

from datetime import date

ano = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = ano - nasc

print('Quem nasceu em {} faz {} anos em {}.'.format(nasc, idade, ano))

if idade < 18:
    print('Ainda faltam {} anos para o alistamento.'.format((nasc + 18) - ano))
    print('Seu alistamento será em {}.'.format(nasc + 18))
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos.'.format(ano - (nasc + 18)))
    print('Seu alistamento foi em {}.'.format(nasc + 18))
else:
    print('Você tem que se alistar IMEDIATAMENTE!')
