velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h. Você deve pagar uma multa de R${:.2f}!'.format((velocidade - 80) * 7))
    print('Tenha um bom dia! Dirija com segurança!')