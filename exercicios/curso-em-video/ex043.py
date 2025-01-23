'''
Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
'''

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
