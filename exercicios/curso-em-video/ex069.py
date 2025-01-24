'''
Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
'''

maioridade = homem = mulher20 = 0

while True:
    print('-' * 30)
    print('{:^30}'.format('CADASTRE UMA PESSOA'))
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().lower()[0]
    print('-' * 30)
    continuar = str(input('QUER CONTINUAR? [S/N] ')).strip().lower()[0]
    if idade >= 18:
        maioridade += 1
    if sexo == 'm':
        homem += 1
    if sexo == 'f' and idade < 20:
        mulher20 += 1
    if continuar != 's':
        break

print('-' * 30)
print(f'Total de pessoas com mais de 18 anos: {maioridade}')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos {mulher20} mulheres com menos de 20 anos.')
