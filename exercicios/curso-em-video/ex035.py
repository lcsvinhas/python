'''
Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''

print('-=-' * 20)
print('\033[1;34;46mAnalisador de Triângulos\033[m')
print('-=-' * 20)

pseg = float(input('Primeiro segmento: '))
sseg = float(input('Segundo segmento: '))
tseg = float(input('Terceiro segmento: '))

if pseg < sseg + tseg and sseg < pseg + tseg and tseg < pseg + sseg:
    print('Os segmentos acima \033[32mPODEM FORMAR\033[m um triângulo!')
else:
    print('Os segmentos acima \033[31mNÃO PODEM FORMAR\033[m um triângulo!')
