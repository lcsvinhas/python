'''
Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
'''

import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de R${moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de R${moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentado 10%, temos R${moeda.moeda(moeda.aumentar(p, 10))}')
