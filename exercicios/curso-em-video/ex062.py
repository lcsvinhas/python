'''
Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
'''

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
