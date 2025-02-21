'''
Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
'''


def fatorial(n, show=False):
    '''
    -> Calcula o fatorial de um número.
    Parâmetro n: O número a ser calculado.
    Parêmetro show: (opcional) Mostrar ou não a conta.
    return: O valor do fatorial de um número n.
    '''
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


fat = int(input('Digite um número para ver seu fatorial: '))

print(fatorial(fat, show=True))
help(fatorial)
