# Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = int(input('Digite um número: '))

print('O dobro de {} é {}.'.format(numero, (numero*2)))
print('O triplo de {} é {}. \nA raiz quadrada de {} é {:.2f}.'.format(
    numero, (numero*3), numero, pow(numero, 0.5)))
