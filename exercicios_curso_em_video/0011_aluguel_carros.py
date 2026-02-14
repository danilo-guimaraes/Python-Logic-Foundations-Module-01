kms = float(input('Seja bem-vindo a DL CAR \nPor quantos KM você percorreu? ')) # Lê a quilometragem percorrida
dias = float(input('Por quantos dias você alugou? ')) # Lê a quantidade de dias de aluguel
dia = dias * 60 # Calcula o valor total fixo pelos dias (R$ 60 por dia)
km = kms * 0.15 # Calcula o valor variável pelos KM (R$ 0,15 por KM)
aluguel = km + dia # Soma os dois valores para obter o total do aluguel
print('O valor a pagar de alguel é R${:.2f}'.format(aluguel)) # Exibe o valor final com 2 casas decimais