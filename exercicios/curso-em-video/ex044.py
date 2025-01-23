'''
Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
'''

print('{:=^40}'.format('SUPERMERCADO'))

preco = float(input('Preço das compras: R$'))

print(
    'FORMAS DE PAGAMENTO \n[1] à vista no dinheiro/pix \n[2] à vista no cartão \n[3] 2x no cartão \n[4] 3x ou mais no cartão')

opcao = int(input('Qual é a opção? '))

if opcao == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no total.'.format(
        preco, preco * 0.90))
elif opcao == 2:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no total.'.format(
        preco, preco * 0.95))
elif opcao == 3:
    print('Sua compra de R${:.2f} será parcelada em 2x de R${:.2f} SEM JUROS.'.format(
        preco, preco / 2))
elif opcao == 4:
    vezes = int(input('Quantas parcelas? '))
    print('Sua compra de R${:.2f} será parcelada em {:.0f}x de R${:.2f} COM JUROS e custará R${:.2f} no total.'.format(
        preco, vezes, preco * 1.20 / vezes, preco * 1.20))
else:
    print('Opcão inválida')
