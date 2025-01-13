produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00,
            'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Caneta', 22.30, 'Livro', 34.90)
print('-' * 30)
print('{:^30}'.format('LISTAGEM DE PREÇOS'))
print('-' * 30)
for item in range(0, len(produtos)):
    if item % 2 == 0:
        print(f'{produtos[item]:.<21}', end='')
    else:
        print(f'R${produtos[item]:>7.2f}')
print('-' * 30)