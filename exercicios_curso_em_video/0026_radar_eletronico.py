try:                                                                     # Tenta executar o bloco de código abaixo
    velocidade = float(input('Digite uma velocidade: ').strip(' '))      # Lê a entrada, remove espaços e tenta converter para decimal
    if velocidade > 80:                                                  # SE a velocidade for maior que o limite de 80km/h
        multa = (velocidade - 80) * 7                                    # Calcula R$ 7,00 por cada km acima do limite
        print('Voce foi multado em R$:{:.2f}'.format(multa))             # Exibe o valor da multa com 2 casas decimais
    else:                                                                # SENÃO (velocidade dentro do limite)
        print('Voce esta abaixo do limite de velocidade, continue assim') # Exibe mensagem de condutor prudente
except ValueError:                                                       # Caso o usuário digite letras ou caracteres inválidos
    print('Erro: Digite apenas números para a velocidade.')              # Exibe mensagem de erro amigável em vez de travar o programa