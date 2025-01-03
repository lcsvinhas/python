casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
ano = int(input('Quantos anos de fincanciamento? '))
prestacao = casa / (ano * 12)
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(casa, ano, prestacao))
if prestacao >= (salario * 0.30):
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')