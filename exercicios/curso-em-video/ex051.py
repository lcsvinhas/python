'''
Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
'''

print('=' * 22)
print(' 10 TERMOS DE UMA PA')
print('=' * 22)

num = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = num + (10 - 1) * razao

for c in range(num, decimo, razao):
    print(c, end=' -> ')

print('ACABOU')
