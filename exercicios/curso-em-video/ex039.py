from datetime import date
ano = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = ano - nasc
print('Quem nasceu em {} faz {} anos em {}.'.format(nasc, idade, ano))
if idade < 18:
    print('Ainda faltam {} anos para o alistamento.'.format((nasc + 18) - ano))
    print('Seu alistamento será em {}.'.format(nasc + 18))
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos.'.format(ano - (nasc + 18)))
    print('Seu alistamento foi em {}.'.format(nasc + 18))
else:
    print('Você tem que se alistar IMEDIATAMENTE!')