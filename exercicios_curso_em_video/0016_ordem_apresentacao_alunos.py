import random

n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceiro aluno: ')
n4 = input('Digite o nome do quarto aluno: ')

# 1. Colocamos os nomes em uma lista
lista = [n1, n2, n3, n4]
random.shuffle(lista)

 # 3. Exibimos os nomes já na nova ordem
print('A ordem de apresentação será:')
print('Em primeiro o aluno: {}'.format(lista[0]))
print('Em segundo o aluno: {}'.format(lista[1]))
print('Em terceiro o aluno: {}'.format(lista[2]))
print('Em quarto o aluno: {}'.format(lista[3]))