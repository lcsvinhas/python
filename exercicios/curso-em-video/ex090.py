dados = {}
dados['Nome'] = input('Nome: ')
dados['Média'] = float(input(f'Média de {dados['Nome']}: '))
print('-=' * 30)
if dados['Média'] >= 7:
    dados['Situação'] = 'aprovado'
elif dados['Média'] < 5:
    dados['Situação'] = 'reprovado'
else:
    dados['Situação'] = 'recuperação'
for k, v in dados.items():
    print(f'- {k} é igual a {v}')
print(dados)