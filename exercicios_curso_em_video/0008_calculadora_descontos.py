valor =float(input('Coloque seu produto no leitor de descontos: ')) # Lê o valor original do produto
desconto = valor * 5 / 100 # Calcula o valor correspondente a 5% de desconto
print('O preço com desconto do seu produto é {:.2f}, lembre-se, a cada compra tem mais descontos viu?!'.format(desconto)) # Exibe o valor do desconto
resta = valor - desconto # Subtrai o desconto do valor original
print('O valor a pagar é de {:.2f} reais'.format(resta)) # Exibe o preço final a ser pago