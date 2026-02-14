nome = input('Qual o seu nome completo?\n')
print(nome.upper()) # Exibe o nome todo em maiúsculas
print(nome.lower()) # Exibe o nome todo em minúsculas
letra = len("".join(nome.split())) # Junta as palavras sem espaços e conta o total de letras
print(letra)

nomes = nome.split() [0] # Divide o nome e pega apenas a primeira palavra (índice 0)
print(f"{nomes}")