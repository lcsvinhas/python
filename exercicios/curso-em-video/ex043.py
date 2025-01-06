peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / altura**2
print('Seu IMC é {:.2f}.'.format(imc))
if imc <= 18.5:
    print('Classificação: Baixo Peso')
elif imc <= 24.9:
    print('Classificação: Peso Normal')
elif imc <= 29.9:
    print('Classificação: Sobrepeso')
elif imc <= 34.9:
    print('Classificação: Obesidade Grau I')
elif imc <= 39.9:
    print('Classificação: Obesidade Grau II')
else:
    print('Classificação: Obesidade Grau III')