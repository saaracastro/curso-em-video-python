from math import hypot
ct = float(input('Cateto oposto:'))
ca = float(input('Cateto adjacente:'))
hip = hypot(ct,ca)
print(' A hipotenusa desse triangulo é {}'.format(hip))
