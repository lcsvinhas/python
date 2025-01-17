from time import sleep
def maior(*num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(valor, end=' ', flush=True)
        sleep(0.1)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

maior(2, 2, 4, 100, 204, 190, 5)
maior(5, 2, 9)
maior(9, 3)
maior(6)
maior()