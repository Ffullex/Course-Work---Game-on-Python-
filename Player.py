import pygame as pg
from settings import *
class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.image.load("img/walk right1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.x = x * WIDTH
        self.y = y * HEIGHT

    def Movement(self, x,y):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and x > 10:
            x -= SPEED
        if keys[pg.K_RIGHT] and x < 500 - SPEED:
            x += SPEED
        if keys[pg.K_UP] and y > 10:
            y -= SPEED
        if keys[pg.K_DOWN] and y < 500 - SPEED:
            y += SPEED