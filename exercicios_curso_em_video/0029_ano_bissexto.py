ano = int(input('Escolha o ano para saber se é bissexto:  ').strip(' '))      # Lê o ano, limpa espaços e converte para inteiro
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:                # Verifica se é divisível por 4 E NÃO por 100, OU se é div. por 400
    print('Seu ano é bissexto!')                                     # Mensagem exibida se a lógica matemática for verdadeira
else:                                                                # Caso o ano não atenda aos critérios de bissexto
    print('Seu ano não é bissexto')                                  # Mensagem exibida se a lógica for falsa