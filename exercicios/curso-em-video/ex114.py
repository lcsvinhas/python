# Exercício Python 114: Crie um código em Python que teste se o site google está acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.google.com/')
except urllib.error.URLError:
    print('Google não está disponível no momento.')
else:
    print('Consegui acessar o Google com sucesso!')
