largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
print('Sua parede tem a dimensão de {}x{} e sua área é {:.2f}m². Para pintá-la, você precisará de {:.2f}l de tinta.'.format(largura, altura, area, area/2))