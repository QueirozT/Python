"""
O jogo de adivinhação é um jogo de palpites entre um jogador e o computador.
- O computador irá informar uma dica sobre a palavra secreta.
- O jogador deve informar um palpite para cada letra da palavra secreta.
- O jogador terá cinco palpites para tentar adivinhar a palavra secreta.
- O jogador vence se conseguir adivinhar a palavra secreta antes do fim do jogo. 
"""
from Regras import * # Importa o módulo jogo

msg('Bem vindo ao Jogo de Adivinhação') # Mensagem de boas vindas
print()

palavraSecreta('Maracujá', 'Uma Fruta') # Iniciando o jogo com uma palavra e uma dica.
