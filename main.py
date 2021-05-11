import pygame
# Импортируем pygame.locals для более простого доступа к клавиатуре
from pygame.locals import (
K_UP,
K_DOWN,
K_LEFT,
K_RIGHT,
K_ESCAPE,
KEYDOWN,
QUIT,
)
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    # Нажал ли пользователь на кнопку закрытия окна?
        elif event.type == QUIT:
            running = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    screen.fill((255, 255, 255))
    # Создаем “поверхность” и передаем ширину и высоту

    surf = pygame.Surface((50, 50))
    # Даем ей цвет, чтобы отделить от фона
    surf.fill((0, 73, 0))
    rect = surf.get_rect()
    screen.blit(surf, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
    pygame.display.flip()
pygame.quit()