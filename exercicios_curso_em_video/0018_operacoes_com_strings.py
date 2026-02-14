frase = 'curso em video python'
print(frase.upper() .count('O')) # Transforma em maiúsculas e conta a letra 'O'
print(len(frase)) # Mostra o comprimento total da frase
print(len(frase.strip())) # Mostra o comprimento removendo espaços inúteis nas extremidades
print(frase.replace('python', 'Android')) # Substitui uma palavra por outra na exibição
print(frase[0:3]) # Mostra apenas do índice 0 ao 2 (fatiamento)
frase = frase.replace('python', 'Android') # Salva a substituição na variável frase
print('curso' in frase) # Verifica se a palavra 'curso' existe na frase (True/False)
print(frase.find('video')) # Mostra em qual posição a palavra 'video' começa
print(frase.lower().find('Video')) # Tenta achar 'Video' após converter tudo para minúsculo
print(frase.split()) # Divide a frase em uma lista de palavras
dividido = frase.split()
print(dividido [3] [0]) # Mostra a primeira letra da quarta palavra da lista