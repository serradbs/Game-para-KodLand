import pygame
import random
import math

# Inicializa o PyGame
pygame.init()

# Configurações principais
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tom & Jerry - Jogo de Fuga")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# FPS
clock = pygame.time.Clock()

# Tamanho dos personagens
player_size = 50
tom_size = 70

# Posições iniciais de Jerry (player) e Tom (inimigo)
jerry_x, jerry_y = WIDTH // 2, HEIGHT // 2
tom_x, tom_y = random.randint(0, WIDTH), random.randint(0, HEIGHT)

# Velocidade de Jerry
jerry_speed = 5

# Velocidade de Tom (inimigo)
tom_speed = 3

# Função para desenhar Jerry
def draw_jerry(x, y):
    pygame.draw.rect(screen, BLUE, (x, y, player_size, player_size))

# Função para desenhar Tom
def draw_tom(x, y):
    pygame.draw.rect(screen, RED, (x, y, tom_size, tom_size))

# Função para mover Jerry
def move_jerry(keys, x, y):
    if keys[pygame.K_LEFT] and x > 0:
        x -= jerry_speed
    if keys[pygame.K_RIGHT] and x < WIDTH - player_size:
        x += jerry_speed
    if keys[pygame.K_UP] and y > 0:
        y -= jerry_speed
    if keys[pygame.K_DOWN] and y < HEIGHT - player_size:
        y += jerry_speed
    return x, y

# Função para mover Tom em direção a Jerry
def move_tom(tom_x, tom_y, jerry_x, jerry_y):
    angle = math.atan2(jerry_y - tom_y, jerry_x - tom_x)
    tom_x += tom_speed * math.cos(angle)
    tom_y += tom_speed * math.sin(angle)
    return tom_x, tom_y

# Função para verificar colisão
def check_collision(jerry_x, jerry_y, tom_x, tom_y):
    distance = math.hypot(tom_x - jerry_x, tom_y - jerry_y)
    if distance < (player_size + tom_size) // 2:
        return True
    return False

# Menu principal
def main_menu():
    running = True
    while running:
        screen.fill(BLACK)
        font = pygame.font.SysFont("Arial", 40)
        title_text = font.render("Tom & Jerry - Pressione ENTER para começar", True, WHITE)
        screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, HEIGHT//2))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = False

# Jogo principal
def game_loop():
    global jerry_x, jerry_y, tom_x, tom_y
    running = True
    while running:
        # Eventos do PyGame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Movimentação de Jerry
        keys = pygame.key.get_pressed()
        jerry_x, jerry_y = move_jerry(keys, jerry_x, jerry_y)

        # Movimentação de Tom
        tom_x, tom_y = move_tom(tom_x, tom_y, jerry_x, jerry_y)

        # Verificar colisão
        if check_collision(jerry_x, jerry_y, tom_x, tom_y):
            running = False

        # Atualizar tela
        screen.fill(WHITE)
        draw_jerry(jerry_x, jerry_y)
        draw_tom(tom_x, tom_y)
        pygame.display.flip()

        # FPS
        clock.tick(60)

# Executar jogo
main_menu()
game_loop()
pygame.quit()
