numeros = []
while True:
    opcao = int(input('Digite um valor: '))
    if opcao not in numeros:
        numeros.append(opcao)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado, não vou adicionar.')
    continuar = input('Quer continuar? [S/N] ').strip().lower()[0]
    if continuar != 's':
        break
print('-=' * 30)
print(f'Você digitou os valores {sorted(numeros)}')