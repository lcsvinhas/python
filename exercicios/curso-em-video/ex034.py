salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, salario + (salario * 0.15)))
else:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, salario + (salario * 0.10)))