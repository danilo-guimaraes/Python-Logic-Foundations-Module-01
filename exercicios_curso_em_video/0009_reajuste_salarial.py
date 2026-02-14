print('Bem vindo ao aumento já, site que calculamos seu saraios em até 15%.')
salario = float(input('Qual seu salario atual? R$ ')) # Lê o salário atual do usuário
novo = salario + (salario * 15 / 100) # Calcula o novo salário com acréscimo de 15%
print('Com esse aumento você que recebia {:.2f} reais, agora ganhará {:.2f} reais'.format(salario, novo)) # Exibe salário antigo e novo