import pygame
print("""
Ex.: 021: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
""")
print('=' *99)

a = input('Insira Aqui o Nome Do Seu Arquivo mp3: ')
# iniciando pygame
pygame.mixer.init()
# carregando musica
pygame.mixer.music.load(a)
# reproduzindo musica1
pygame.mixer.music.play()
input()
# finalizar ao termino da musica
pygame.event.wait()
