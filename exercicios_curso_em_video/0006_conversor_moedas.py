real = float(input('Digite o valor do real que você quer converter? R$ ')) # Lê o valor em Reais
dolar = real / 5.32 # Calcula a conversão baseada na cotação definida
print('Com R${} você pode comprar US${}'.format(real, dolar)) # Exibe o valor em Reais e o equivalente em Dólares