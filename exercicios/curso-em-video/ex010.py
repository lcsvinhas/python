# Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

# Cotações de 31/12/2024. Voltar no futuro e ver se melhoramos a situação!
real = float(input('Quanto dinheiro você tem? R$'))
dolar = real / 6.18
euro = real / 6.40

print('Com R${:.2f} você pode comprar US${:.2f} e €{:.2f}'.format(
    real, dolar, euro))
