import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Definindo as constantes
LARGURA, ALTURA = 800, 600
COR_FUNDO = (0, 0, 0)
COR_BOLA = (255, 255, 255)
COR_RAQUETE = (255, 255, 255)
LARGURA_RAQUETE = 15
ALTURA_RAQUETE = 100
RADIO_BOLA = 10
VEL_RAQUETE = 6
VEL_BOLA = 5

# Configurando a tela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Pong')

# Função para desenhar a raquete
def desenhar_raquete(x, y):
    pygame.draw.rect(tela, COR_RAQUETE, pygame.Rect(x, y, LARGURA_RAQUETE, ALTURA_RAQUETE))

# Função para desenhar a bola
def desenhar_bola(x, y):
    pygame.draw.circle(tela, COR_BOLA, (x, y), RADIO_BOLA)

# Função principal do jogo
def main():
    clock = pygame.time.Clock()
    
    # Posições e velocidades iniciais
    x_raquete1, y_raquete1 = 30, ALTURA // 2 - ALTURA_RAQUETE // 2
    x_raquete2, y_raquete2 = LARGURA - 30 - LARGURA_RAQUETE, ALTURA // 2 - ALTURA_RAQUETE // 2
    x_bola, y_bola = LARGURA // 2, ALTURA // 2
    velocidade_x_bola, velocidade_y_bola = VEL_BOLA, VEL_BOLA
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Controles das raquetes
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_w] and y_raquete1 > 0:
            y_raquete1 -= VEL_RAQUETE
        if teclas[pygame.K_s] and y_raquete1 < ALTURA - ALTURA_RAQUETE:
            y_raquete1 += VEL_RAQUETE
        if teclas[pygame.K_UP] and y_raquete2 > 0:
            y_raquete2 -= VEL_RAQUETE
        if teclas[pygame.K_DOWN] and y_raquete2 < ALTURA - ALTURA_RAQUETE:
            y_raquete2 += VEL_RAQUETE
        
        # Movimentação da bola
        x_bola += velocidade_x_bola
        y_bola += velocidade_y_bola
        
        # Colisão com o topo e a base da tela
        if y_bola - RADIO_BOLA < 0 or y_bola + RADIO_BOLA > ALTURA:
            velocidade_y_bola = -velocidade_y_bola
        
        # Colisão com as raquetes
        if (x_bola - RADIO_BOLA < x_raquete1 + LARGURA_RAQUETE and
            y_bola > y_raquete1 and y_bola < y_raquete1 + ALTURA_RAQUETE):
            velocidade_x_bola = -velocidade_x_bola
        
        if (x_bola + RADIO_BOLA > x_raquete2 and
            y_bola > y_raquete2 and y_bola < y_raquete2 + ALTURA_RAQUETE):
            velocidade_x_bola = -velocidade_x_bola
        
        # Atualizando a tela
        tela.fill(COR_FUNDO)
        desenhar_raquete(x_raquete1, y_raquete1)
        desenhar_raquete(x_raquete2, y_raquete2)
        desenhar_bola(x_bola, y_bola)
        pygame.display.flip()
        
        # Controlando a taxa de quadros
        clock.tick(60)

if __name__ == "__main__":
    main()
