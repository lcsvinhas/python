'''
Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
'''

import moeda

p = float(input('Digite o preço: R$'))

print(f'A metade de R${moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de R${moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentado 10%, temos R${moeda.aumentar(p, 10, True)}')
print(f'Diminuindo 13%, temos R${moeda.aumentar(p, 13, True)}')
