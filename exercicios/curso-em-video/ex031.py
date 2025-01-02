dist = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.2f}Km.'.format(dist))
if dist <= 200:
    print('O preço da sua passagem será de R${:.2f}'.format(dist * 0.50))
else:
    print('O preço da sua passagem será de R${:.2f}'.format(dist * 0.45))