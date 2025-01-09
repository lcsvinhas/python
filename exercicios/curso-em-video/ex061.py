print('Gerador de PA')
print('-=' * 10)
a = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = a
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += r
    cont += 1
print('FIM')