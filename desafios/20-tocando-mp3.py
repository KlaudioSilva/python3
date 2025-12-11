'''
Faça um programa que abra e reproduza um áudio em mp3.
'''
import pygame
import time         #para esperar a musica tocar


pygame.init()       #inicia o pygame
pygame.mixer.init() #inicia o mixer de audio

#carrega a musica
pygame.mixer.music.load('mp3/Double-Dragon-(Arcade)-OST-Track 01.mp3')

#toca a musica
pygame.mixer.music.play()

print('\n')
print('-' * 38)
print(f'{"Iniciando Double Dragon Soundtrack":^38}')
print('-' * 38)
print('\n')

#mantem o programa rodando enquanto a musica toca
while pygame.mixer.music.get_busy():
    time.sleep(1)   #espera 1 segundo antes de verificar novamente
    #print('Tocando Double Dragon Soundtrack')

pygame.quit()       #encerra o programa
print('Fim da execução')