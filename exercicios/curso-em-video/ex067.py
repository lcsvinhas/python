'''
Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
'''

while True:
    tab = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 36)
    if tab < 0:
        break
    for cont in range(1, 11):
        print(f'{tab} x {cont} = {tab * cont}')
    print('-' * 36)

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
