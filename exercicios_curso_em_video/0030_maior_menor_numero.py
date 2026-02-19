# Lê os números, transforma em lista e converte cada um para inteiro
numeros = [int(n) for n in input('Digite seus números separados por espaço: ').split()]

# O comando max() encontra automaticamente o maior valor da lista
maior = max(numeros)
print('Esse é seu maior numero {}'.format(maior)) # Exibe o maior número encontrado

# O comando min() encontra automaticamente o menor valor da lista
menor = min(numeros)
print('Esse é seu menor numero {}'.format(menor)) # Exibe o menor número encontrado