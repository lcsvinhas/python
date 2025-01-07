from datetime import date
maior = 0
menor = 0
for pessoa in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(pessoa)))
    if date.today().year - ano >= 18:
        maior += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(maior))
print('E também tivemos {} pessoas menores de idade.'.format(menor))