from datetime import date
dados = {}
dados['Nome'] = input('Nome: ')
dados['Sexo'] = input('Sexo [M/F]: ').strip().lower()[0]
nasc = int(input('Ano de nascimento: '))
dados['Idade'] = date.today().year - nasc
dados['CTPS'] = int(input('Carteira de trabalho (digite "0" caso não tenha): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: '))
    if dados['Sexo'] == 'm':
        dados['Aposentadoria'] = dados['Contratação'] + 35 - nasc
    else:
        dados['Aposentadoria'] = dados['Contratação'] + 30 - nasc
print('-=' * 30)
for k, v in dados.items():
    print(f'- {k}: {v}')