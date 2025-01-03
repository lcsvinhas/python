numero = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
convert = int(input('[1] converter para BINÁRIO \n[2] converter para OCTAL \n[3] converter para HEXADECIMAL \nSua opção: '))
if convert == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero, bin(numero)))
elif convert == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)))
elif convert == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)))
else:
    print('Opção inválida. Tente novamente.')