total = mil = barato = cont = 0
nome = ''
print('-' * 30)
print('{:^30}'.format('LOJA SUPER BARATÃO'))
print('-' * 30)
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if preco > 1000:
        mil += 1
    if cont == 1 or preco < barato:
        barato = preco
        nome = produto
    if continuar != 's':
        break
print('{:-^30}'.format(' FIM DO PROGRAMA '))
print(f'O total de compra foi R${total:.2f}')
print(f'Temos {mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome} no valor de R${barato:.2f}')