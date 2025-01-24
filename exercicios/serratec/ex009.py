def calcular_soma(a, b):
    resultado = a + b
    return resultado


def minha_funcao():
    variavel_local = 10
    print(variavel_local)


variavel_global = 20


def minha_funcao():
    print(variavel_global)


minha_funcao()
print(variavel_global)
