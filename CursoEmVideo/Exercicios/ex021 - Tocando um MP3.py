import pygame as pg

print('===== EXERCÍCIO 021 =====')	# Tocando um mp3
print()

pg.init() # Inicialização do PyGame

pg.mixer.music.load('ex021.mp3') # Carregando o arquivo de música

pg.mixer.music.play() # Tocando a música

pg.event.wait() # Esperando o evento de fechamento da janela

# pg.quit() # Para Fechar o PyGame