# Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input('Qual é o seu nome completo? ')

print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
