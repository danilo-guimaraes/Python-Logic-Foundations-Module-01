import math
# from math import radians, sin, cos, tan
grau = int(input('digite um numero em graus: \n'))
seno = math.sin(math.radians(int(grau)))
cosseno = math.cos(math.radians(int(grau)))
tangente = math.tan(math.radians(int(grau)))
print('O numero do seno {:.2f}, o numero do cosseno {:.2f}  e a tangente {:.2f}'.format(seno, cosseno, tangente))

# ALTERNATIVA EX 3
# an = float(input('digite um ângulo: \n'))
# seno = math.sin(math.radians(int(an)))
# print('O ângulo {} tem o seno {:.2f}'.format(an, seno))
# cosseno = math.cos(math.radians(int(an)))
# print('O ângulo {} tem o cosseno {:.2f}'.format(an, cosseno))
# tangente = math.tan(math.radians(int(an)))
# print('O ângulo {} tem o tangente {:.2f}'.format(an, tangente))