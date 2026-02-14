# Exemplo de encadeamento de métodos (Method Chaining)
frase = input('Digite uma frase: ')

# Explicação da linha abaixo:
# 1. frase.upper() -> Transforma tudo em MAIÚSCULO para não ignorar nenhum 'a'.
# 2. .count('A')   -> Conta quantas vezes o 'A' aparece após a transformação.
# 3. .format(...)  -> Coloca o resultado numérico dentro das chaves {}.

print('A letra "A" aparece {} vezes na frase toda.'.format(frase.upper().count('A')))


#########
frase = input('Digite uma frase: ').strip()

# 1. Divide a frase em uma lista de palavras
palavras = frase.split()

# 2. Isola a primeira e a última palavra
primeira_palavra = palavras[0]
ultima_palavra = palavras[-1]

# 3. Encontra a posição da PRIMEIRA letra 'A' na primeira palavra
# Usamos upper() para garantir que pegue tanto 'a' quanto 'A'
posicao_a_primeira = primeira_palavra.upper().find('A') + 1

# 4. Encontra a posição da PRIMEIRA letra 'A' na última palavra
posicao_a_ultima = ultima_palavra.upper().find('A') + 1

print(f'A primeira palavra é "{primeira_palavra}"')
if posicao_a_primeira > 0:
    print(f'Nela, a letra "A" aparece primeiro na posição: {posicao_a_primeira}')
else:
    print('Nela não existe a letra "A".')

print(f'A última palavra é "{ultima_palavra}"')
if posicao_a_ultima > 0:
    print(f'Nela, a letra "A" aparece primeiro na posição: {posicao_a_ultima}')
else:
    print('Nela não existe a letra "A".')