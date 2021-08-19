import pygame
from settings import *


class Portal(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.portal
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TEXTURES_SIZE, TEXTURES_SIZE))
        self.image = pygame.image.load("data/Portal.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TEXTURES_SIZE
        self.rect.y = y * TEXTURES_SIZE
