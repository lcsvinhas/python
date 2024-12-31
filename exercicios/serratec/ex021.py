import pandas as pd
import matplotlib as plt

# LER O ARQUIVO CSV E CRIAR UM DATAFRAME
dados_vendas = pd.read_csv("dados_vendas.csv")

# IMPRIMIR AS PRIMEIRAS 5 LINHAS DO DATAFRAME
print(dados_vendas.head())

# CALCULAR A MÉDIA DO VALOR TOTAL DAS VENDAS
media_vendas = dados_vendas["Valor Total"].mean()
print("media do valor total das vendas: R$", media_vendas)

# CALCULAR O TOTAL DE VENDAS
total_vendas = dados_vendas["Valor Total"].sum()
print("Total de vendas: R$", total_vendas)

# CALCULAR A QUANTIDADE TOTAL DE VENDAS
quantidade_vendas = dados_vendas.shape[0]
print("Quantidade total de vendas:", quantidade_vendas)

# CRIAR UM GRÁFICO DE BARRAS COM O TOTAL DE VENDAS POR PRODUTO
dados_vendas_por_produto = dados_vendas.groupby("Produto")["Valor Total"].sum()
dados_vendas_por_produto.plot(kind="bar", figsize=(10, 6))
plt.xlabel("Produto")
plt.ylabel("Valor total")
plt.title("Total de vendas por produto")
plt.show()