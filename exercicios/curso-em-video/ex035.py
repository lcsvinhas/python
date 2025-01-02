print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
pseg = float(input('Primeiro segmento: '))
sseg = float(input('Segundo segmento: '))
tseg = float(input('Terceiro segmento: '))
if pseg < sseg + tseg and sseg < pseg + tseg and tseg < pseg + sseg:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')