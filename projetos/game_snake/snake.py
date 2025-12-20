import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480
mov_x = largura/2
mov_y = altura/2

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake 1.0')
relogio = pygame.time.Clock()

#loop principal
while True:
    relogio.tick(30)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():   #evento de fechar a janela
        if event.type == QUIT:          #se o evento é tipo = Desistir
            pygame.quit()               #chama o metodo quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                mov_x = mov_x - 20
            if event.key == K_d:
                mov_x = mov_x + 20
            if event.key == K_w:
                mov_y = mov_y - 20
            if event.key == K_s:
                mov_y = mov_y + 20

    if pygame.key.get_pressed()[K_a]:
        mov_x = mov_x - 20
    if pygame.key.get_pressed()[K_d]:
        mov_x = mov_x + 20
    if pygame.key.get_pressed()[K_w]:
        mov_y = mov_y - 20
    if pygame.key.get_pressed()[K_s]:
        mov_y = mov_y + 20

    #desenhando um retangulo na tela
    pygame.draw.rect(tela, (255, 0, 0), (mov_x, mov_y, 40, 50))  #(onde será criado(cor(RGB), coordenadas na tela(x,y) e tamanho do retangulo))


    pygame.display.update()         #atualiza o display