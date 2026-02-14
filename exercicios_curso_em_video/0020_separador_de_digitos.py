numero = input('Digite um numero: ')
milhar = numero.split() [-1] [-4] # Pega o quarto dígito de trás para frente
print(f"{milhar} Milhar")
centenas = numero.split() [-1] [-3] # Pega o terceiro dígito de trás para frente
print(f"{centenas} centenas")
dezenas = numero.split() [-1] [-2] # Pega o segundo dígito de trás para frente
print(f"{dezenas} Dezenas")
unidade = numero.split() [-1] [-1] # Pega o último dígito
print(f"{unidade} Unidades")