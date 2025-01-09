resposta = 's'
cont = soma = maior = menor = 0
while resposta == "s":
    numero = int(input('Digite um número: '))
    resposta = str(input('Quer continuar [S/N]: ')).strip().lower()[0]
    cont += 1
    soma += numero
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
print('Você digitou um total de {} números e a média foi {:.2f}'.format(cont, soma / cont))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))