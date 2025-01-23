# Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input('Digite a medida em metros: '))

print('{} metros são {:.0f} centímetros e {:.0f} milímetros.'.format(
    medida, medida*100, medida*1000))
