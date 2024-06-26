from math import sqrt
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimeto do cateto adjacente: '))
h=ca**2 + co**2
raiz = sqrt(h)

print('O comprimeto da hipotenusa é {:.2}'.format(raiz))