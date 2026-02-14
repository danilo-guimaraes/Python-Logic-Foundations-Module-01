alt = float(input('Qual altura em metros da parede? ')) # Lê a altura da parede
larg = float(input('Qual largura em metros da parede? ')) # Lê a largura da parede
área = alt * larg # Calcula a área total em metros quadrados
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, área)) # Exibe dimensões e área
tinta = área / 2 # Calcula a quantidade de tinta (considerando que 1L pinta 2m²)
print('Para pintar toda a parede, você precisará de {}L de tinta.'.format(tinta)) # Exibe o total de litros necessários
litro = (tinta * larg) / 20 # Realiza um cálculo específico de tinta por largura
print('Você gastará {:.1f}L de tinta por área!'.format(litro)) # Exibe o gasto por área com 1 casa decimal