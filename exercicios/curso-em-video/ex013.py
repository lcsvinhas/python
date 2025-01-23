# Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual é o salário do funcionário? R$'))
aumento = float(input('Quantos por cento de aumento? '))

print('Um funcionário que ganhava R${}, com {}% de aumento, passa a receber R${:.2f}.'.format(
    salario, aumento, salario + (salario*aumento/100)))
