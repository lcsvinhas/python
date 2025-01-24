'''
Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

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

print('Você digitou um total de {} números e a média foi {:.2f}'.format(
    cont, soma / cont))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
