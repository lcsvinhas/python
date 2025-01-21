'''
Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''

from math import sin, cos, tan, radians

angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O ângulo de {} tem o SENO de {:.2f} \nO ângulo de {} tem o COSSENO de {:.2f} \nO ângulo de {} tem a tangente de {:.2f}'.format(
    angulo, seno, angulo, cosseno, angulo, tangente))
