import pygame
from settings import *


class Aqua(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        # пока что логика как у box, поэтому в группе box
        self.groups = game.all_sprites, game.box
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TEXTURES_SIZE, TEXTURES_SIZE))
        self.image = pygame.image.load("Aqua.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TEXTURES_SIZE
        self.rect.y = y * TEXTURES_SIZE
