import math
from math import hypot
# math.hypot ja calcula o valor sozinho, basta saber o valor dos catetos

print('Bem vindo a soma dos catetos')
oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = math.hypot(oposto, adjacente)
print('O valor da hipostenusa é Igual a {:.2f}'.format (float(hipotenusa)))

# ALTERNATIVA EX 2
# co = float(input('Digite o valor do cateto oposto: '))
# ca = float(input('Digite o valor do cateto adjacente: '))
# hi = (co ** 2 + ca ** 2)**(1/2)
# print('A hipotenusa vai medir {:.2f}'.format(hi))