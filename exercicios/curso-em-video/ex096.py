def calcularArea(largura, comprimento):
    print(f'A área de um terreno de {largura:.2f}m x {comprimento:.2f}m é de {largura * comprimento:.2f}m².')
print('Controle de Terrenos')
print('-' * 20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
calcularArea(largura, comprimento)