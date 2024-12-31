try:
    numero_texto = "123"
    numero = 456
    soma = numero_texto + numero
except TypeError as e:
    print(f"Erro: {e}")

try:
    numero_inicial = 5
    resultado = 10 / numero_inicial
except ValueError as value_error:
    print(f"Erro de Valor: {value_error}")
except ZeroDivisionError as zero_division_error:
    print(f"Erro de Divisão por Zero: {zero_division_error}")
except Exception as exception:
    print(f"Erro genérico: {exception}")
else:
    print(f"Resultado: {resultado}")

try:
    nome = "Lucas Vinhas"
    for caractere in nome:
        if "0" <= caractere <= "9":
            raise ValueError("O nome não pode conter números")
    print(f"Nome digitado: {nome}")
except ValueError as e:
    print(f"Erro: {e}")
finally:
    print("Exemplo completo de utilização do tratamento de exceções")