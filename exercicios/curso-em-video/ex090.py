'''
Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
'''

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
