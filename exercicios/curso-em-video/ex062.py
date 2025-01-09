print('Gerador de PA')
print('-=' * 10)
a = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = a
cont = 1
total = 0
extra = 10
while extra > 0:
    total += extra
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += r
        cont += 1
    print('PAUSA')
    extra = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))