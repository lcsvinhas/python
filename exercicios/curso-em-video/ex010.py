real = float(input('Quanto dinheiro você tem? R$'))
dolar = real / 6.18 # Cotação em 31/12/2024. Voltar no futuro e ver se melhoramos a situação!
euro = real / 6.40 # Cotação em 31/12/2024. Voltar no futuro e ver se melhoramos a situação!
print('Com R${:.2f} você pode comprar US${:.2f} e €{:.2f}'.format(real, dolar, euro))