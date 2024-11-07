lista_numeros = [1, 2, 3, 4, 5]
lista_strings = ["a", "b", "c", "d"]
lista_mista = [10, "Oi", 3.14, True]
lista_vazia = []

print("Números:", lista_numeros)
print("Informações:", lista_strings)
print("Mista:", lista_mista)
print("Vazia:", lista_vazia)

tupla_1 = (1, 2, 3)
tupla_2 = "a", "b", "c"
tupla_mista = (10, "hello", 3.14)
tupla_vazia = ()

print("Tupla1:", tupla_1)
print("Tupla2:", tupla_2)
print("TuplaMista:", tupla_mista)
print("TuplaVazia:", tupla_vazia)

conjunto_1 = {1, 2, 3}
conjunto_2 = set([3, 4, 5])
conjunto_vazio = set()

print("Conjunto 1:", conjunto_1)
print("Conjunto 2:", conjunto_2)
print("Conjunto vazio:", conjunto_vazio)

pessoa = {
    "Nome": "Lucas",
    "Idade": 25,
    "Cidade": "Petrópolis"
}

print("Idade da pessoa:", pessoa["Idade"])