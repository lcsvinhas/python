# Variável global
nome_global = "Lucas"

def funcao_local ():
    # Variável local
    nome_local = "Beth"
    print("Dentro da função local o nome é:", nome_local)

# Chamando a função
funcao_local ()

#Acesso a variável global
print("Fora da função local o nome é:", nome_global)