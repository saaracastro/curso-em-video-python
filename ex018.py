from math import atan,sin,cos
ang = int(input('Qual é o ângulo?'))
sen = sin(ang)
cos = cos(ang)
tang = atan(ang)
print('Com o ângulo de {}, o seno é {}, o cosseno é {} e a tangente {}'.format(ang,sen,cos,tang))