palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for cont in palavras:
    print(f'\nNa palavra {cont} temos ', end='')
    for vogal in cont:
        if vogal.upper() in 'AEIOU':
            print(vogal, end=' ')