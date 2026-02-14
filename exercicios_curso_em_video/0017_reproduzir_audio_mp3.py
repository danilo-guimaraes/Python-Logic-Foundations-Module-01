import pygame

# 1. Inicializa o mixer de áudio
pygame.mixer.init()

# 2. Carrega o arquivo (certifique-se que o nome está idêntico)
pygame.mixer.music.load('city.mp3')

# 3. Dá o play
pygame.mixer.music.play()

print("Tocando Paradise City... Pressione ENTER para parar.")

# 4. ESSA LINHA É A CHAVE: Ela segura o programa aberto
input()