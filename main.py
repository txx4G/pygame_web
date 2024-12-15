import pygame
import random
import asyncio

# Инициализация Pygame
pygame.init()

# Параметры экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Pygame Game")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Переменные игры
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - player_size - 10
player_speed = 5

obstacle_width = 50
obstacle_height = 50
obstacle_x = random.randint(0, WIDTH - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 5

score = 0
font = pygame.font.Font(None, 36)

# Игровой цикл
running = True
async def main():
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Управление игроком
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
            player_x += player_speed

        # Движение препятствия
        obstacle_y += obstacle_speed
        if obstacle_y > HEIGHT:
            obstacle_y = -obstacle_height
            obstacle_x = random.randint(0, WIDTH - obstacle_width)
            score += 1

        # Проверка столкновения
        if (player_x < obstacle_x + obstacle_width and
            player_x + player_size > obstacle_x and
            player_y < obstacle_y + obstacle_height and
            player_y + player_size > obstacle_y):
            running = False

        # Отрисовка игрока и препятствия
        pygame.draw.rect(screen, BLACK, (player_x, player_y, player_size, player_size))
        pygame.draw.rect(screen, RED, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

        # Отображение счета
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        pygame.time.delay(30)
        await asyncio.sleep(0)
asyncio.run(main())
#pygame.quit()
