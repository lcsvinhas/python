celsius = float(input('Informe a temperatura em °C: '))
farenheit = celsius * 1.8 + 32
kelvin = celsius + 273.15
print('A temperatura de {}°C corresponde a {:.2f}°F e {:.2f}K!'.format(celsius, farenheit, kelvin))