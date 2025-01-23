# Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Qual é o preço do produto? R$'))
desconto = float(input('Quantos por cento de desconto? '))

print('O produto que custava R${}, com desconto de {:.0f}% vai custar R${:.2f}.'.format(
    preco, desconto, preco - (preco*desconto/100)))
