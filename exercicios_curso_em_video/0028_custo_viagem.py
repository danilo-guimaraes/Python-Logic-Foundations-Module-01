viagem = float(input('Digite o tamanho da viagem: ').strip(' '))     # Lê a distância, remove espaços e converte para número decimal
if viagem <= 200:                                                    # SE a viagem for curta (até 200km)
    abaixo = viagem * 0.50                                           # Calcula o valor cobrando R$ 0,50 por km
    print(f'O valor pela sua viagem calculada por km é de R${abaixo:.2f}') # Exibe o resultado com 2 casas decimais usando f-string

else:                                                                # SENÃO (caso a viagem seja mais longa que 200km)
    viagem = viagem * 0.45                                        # Calcula o valor com desconto, cobrando R$ 0,45 por km
    print(f'O valor da sua viagem por km é de R${viagem:.2f}')    # Exibe o valor final com desconto aplicado
    print('Aproveite sua viagem')                                 # Mensagem de encerramento para viagens longas