import pygame
from settings import *


# Класс Стена - внутренняя граница, персонаж не может по ним и через них двигаться
class Wall(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.wall
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TEXTURES_SIZE, TEXTURES_SIZE))
        self.image = pygame.image.load("data/Wall.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TEXTURES_SIZE
        self.rect.y = y * TEXTURES_SIZE
