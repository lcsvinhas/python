'''
Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''


def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if 70 > idade >= 18:
        return f'Com {idade} anos, o voto é OBRIGATÓRIO.'
    elif idade < 16:
        return f'Com {idade} anos, ainda NÃO PODE VOTAR.'
    else:
        return f'Com {idade} anos, o voto é FACULTATIVO.'


nasc = int(input('Em que ano você nasceu: '))

print(voto(nasc))
