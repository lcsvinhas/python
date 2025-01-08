numero = int(input('Digite um número para calcular seu fatorial: '))
cont = numero
fat = 1
print('Calculando {}! = '.format(numero), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fat *= cont
    cont -= 1
print('{}'.format(fat))