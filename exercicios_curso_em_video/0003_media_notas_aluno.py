n1 = float(input('Nota de avaliação do aluno bimestre 1: ')) # Lê a primeira nota como número decimal (float)
n2 = float(input('Nota de avaliação do aluno bimestre 2: ')) # Lê a segunda nota como número decimal (float)
m = (n1+n2)/2 # Soma as duas notas e divide por 2 para calcular a média aritmética
print('A média de {:.1f} e {:.1f}: {:.1f}'.format(n1, n2, m)) # Exibe as notas e a média com 1 casa decimal