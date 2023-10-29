import pygame
from pygame.locals import *
from sys import exit
from random import randint

def morre(morreu, game, tela, texto_centro, largura, altura):
    while morreu:
        tela.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
                
            if event.type == KEYDOWN:
                if event.key == K_r:
                    return True
                
        texto_centro.center = (largura//2, altura//2)
        tela.blit(game, texto_centro)
        pygame.display.update()
                    
def aumenta(tela, cor, lista_cobra):
    for x_y in lista_cobra:
        pygame.draw.rect(tela, cor, (x_y[0], x_y[1], 30, 30))

def reiniciar():
    global pontos, comprimento, x_pers, y_pers, lista_cobra, cabeca, x_maca, y_maca, morreu, velocidade
    pontos = 0
    comprimento = 5
    x_pers = largura/2
    y_pers = altura/2
    lista_cobra = []
    cabeca = []
    x_maca = randint(40, 600)
    y_maca = randint(80, 400)
    morreu = False
    velocidade = 10
    
pygame.init()

#Janela
largura, altura = 640, 480
tela = pygame.display.set_mode((largura, altura))
titulo = pygame.display.set_caption("Olha a cobra!")
relogio = pygame.time.Clock()


#Personagem
x_pers = largura/2
y_pers = altura/2
cor = (100, 50, 38)
lista_cobra = []
comprimento = 5
velocidade = 10
morreu = False

#Controle
x_controle = velocidade
y_controle = 0

#Maçã
x_maca = randint(40, 600)
y_maca = randint(80, 400)
x_maca2 = randint(40, 600)
y_maca2 = randint(80, 400)


#Textos
fonte = pygame.font.SysFont("arial", 40, True, False)
pontos = 0
    
while True:
    #Tela
    tela.fill((255, 255, 255))
    relogio.tick(30)
    mensagem = f'Maçãs: {pontos}'
    pontuacao = fonte.render(mensagem, False, (100, 100, 100))
    
    #Eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        #Movimento da cobra
        if event.type == KEYDOWN:
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = -velocidade
                    cor = (randint(0, 190), randint(0, 190), randint(0, 230))
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = +velocidade
                    cor = (randint(0, 255), randint(0, 255), randint(0, 255))
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
                    cor = (randint(0, 255), randint(0, 255), randint(0, 255))
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
                    cor = (randint(0, 255), randint(0, 255), randint(0, 255))
        
    x_pers += x_controle
    y_pers += y_controle
    
    #Desenhar Sprites
    cobra = pygame.draw.rect(tela, cor, (x_pers, y_pers, 30, 30))
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 20, 20))
    
    if pontos != 0 and pontos % 5 == 0:
        maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 20, 20))
        maca2 = pygame.draw.rect(tela, (23, 255, 0), (x_maca2, y_maca2, 20, 20))
        if cobra.colliderect(maca2):#verifica se tem colisão com o coletavel
            x_maca2 = randint(40, 600)
            y_maca2 = randint(80, 400)
            pontos += 2
            comprimento+=1
            velocidade +=1
    else:
        maca2 = False
        
    #Crescer a cobra      
    cabeca = []
    cabeca.append(x_pers)
    cabeca.append(y_pers)
    lista_cobra.append(cabeca)
    if len(lista_cobra) > comprimento:
        lista_cobra.pop(0)
    aumenta(tela, cor, lista_cobra)
    
    #Caso a cobra se encoste
    if lista_cobra.count(cabeca) > 1:
        morreu = True
        fonte2 = pygame.font.SysFont("arial", 20, True, False)
        msg = f"Se mordeu e morreu! se quiser continuar aperte (r)"
        game = fonte2.render(msg, True, (255, 255, 255))
        texto_centro = game.get_rect()
        
        morre(morreu, game, tela, texto_centro, largura, altura)
        reiniciar()
        
     #Bate na parede morre
    """if x_pers > largura or x_pers< 0 or y_pers > altura or y_pers < 0:
        morreu = True
        fonte2 = pygame.font.SysFont("arial", 20, True, False)
        msg = f"Bateu a cabeça e morreu! se quiser continuar aperte (r)"
        game = fonte2.render(msg, True, (255, 255, 255))
        texto_centro = game.get_rect()
        
        morre(morreu, game, tela, texto_centro, largura, altura)
        reiniciar()"""
        
        
    #Ultrapassar os limites da tela vai para o outro lado   
    if x_pers > largura:
        x_pers = 0
    if x_pers< 0:
        x_pers = largura
    if y_pers > altura:
        y_pers = 0
    if y_pers < 0:
        y_pers = altura
        
    #Colisões
    if cobra.colliderect(maca):#verifica se tem colisão com o coletavelw
        x_maca = randint(40, 600)
        y_maca = randint(80, 400)
        pontos += 1 
        comprimento+=1
    
    tela.blit(pontuacao,  (450, 40))
    pygame.display.update()