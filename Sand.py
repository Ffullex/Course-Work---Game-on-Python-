import pygame as pg
from settings import *


class Sand(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.tiles
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.image.load("img/tile.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TEXTURES_SIZE
        self.rect.y = y * TEXTURES_SIZE