import pygame
import time
import random

pygame.init()

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
verde = (0, 255, 0)
vermelho = (213, 50, 80)
azul = (50, 153, 213)

# Dimensões da tela
largura = 600
altura = 400

# Inicializar a tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Cobrinha')

# FPS (frames por segundo)
clock = pygame.time.Clock()
velocidade_cobra = 15

# Tamanho da cobra e comida
tamanho_bloco = 20

# Fonte para o texto
fonte = pygame.font.SysFont(None, 35)

def mensagem(msg, cor):
    texto = fonte.render(msg, True, cor)
    tela.blit(texto, [largura / 6, altura / 3])

def jogo():
    jogo_ativo = True
    fim_de_jogo = False

    x1 = largura / 2
    y1 = altura / 2

    x1_mudanca = 0
    y1_mudanca = 0

    cobra = []
    comprimento_cobra = 1

    comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0

    while jogo_ativo:

        while fim_de_jogo:
            tela.fill(azul)
            mensagem("Você perdeu! Pressione Q para sair ou C para jogar novamente", vermelho)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    if evento.key == pygame.K_c:
                        jogo()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x1_mudanca = -tamanho_bloco
                    y1_mudanca = 0
                elif evento.key == pygame.K_RIGHT:
                    x1_mudanca = tamanho_bloco
                    y1_mudanca = 0
                elif evento.key == pygame.K_UP:
                    y1_mudanca = -tamanho_bloco
                    x1_mudanca = 0
                elif evento.key == pygame.K_DOWN:
                    y1_mudanca = tamanho_bloco
                    x1_mudanca = 0

        if x1 >= largura or x1 < 0 or y1 >= altura or y1 < 0:
            fim_de_jogo = True
        x1 += x1_mudanca
        y1 += y1_mudanca
        tela.fill(azul)
        pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])
        cobra_cabeca = []
        cobra_cabeca.append(x1)
        cobra_cabeca.append(y1)
        cobra.append(cobra_cabeca)
        if len(cobra) > comprimento_cobra:
            del cobra[0]

        for segmento in cobra[:-1]:
            if segmento == cobra_cabeca:
                fim_de_jogo = True

        for segmento in cobra:
            pygame.draw.rect(tela, preto, [segmento[0], segmento[1], tamanho_bloco, tamanho_bloco])

        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
            comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0
            comprimento_cobra += 1

        clock.tick(velocidade_cobra)

    pygame.quit()
    quit()

jogo()


