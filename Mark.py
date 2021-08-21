import pygame
from settings import *


# Класс Метка - персонаж можнт по ним двигаться. На них надо поставить ящики для появления портала.
class Mark(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        # пока что логика как у box, поэтому в группе box
        self.groups = game.all_sprites, game.mark
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TEXTURES_SIZE, TEXTURES_SIZE))
        self.image = pygame.image.load("data/Mark.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TEXTURES_SIZE
        self.rect.y = y * TEXTURES_SIZE
