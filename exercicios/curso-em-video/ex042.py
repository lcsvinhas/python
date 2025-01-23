'''
Exercício Python 042: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
'''

print('-=-' * 20)
print('\033[1;34;46mAnalisador de Triângulos\033[m')
print('-=-' * 20)

pseg = float(input('Primeiro segmento: '))
sseg = float(input('Segundo segmento: '))
tseg = float(input('Terceiro segmento: '))

if pseg < sseg + tseg and sseg < pseg + tseg and tseg < pseg + sseg:
    print(
        'Os segmentos acima \033[32mPODEM FORMAR\033[m um triângulo ', end='')
    if pseg == sseg == tseg:
        print('\033[32mEQUILÁTERO!\033[m')
    elif pseg != sseg != tseg != pseg:
        print('\033[32mESCALENO!\033[m')
    else:
        print('\033[32mISÓSCELES!\033[m')
else:
    print('Os segmentos acima \033[31mNÃO PODEM FORMAR\033[m um triângulo!')
