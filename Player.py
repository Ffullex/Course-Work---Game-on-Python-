import sys
from os import path
import pygame
import pygame.sprite

from Camera import Map
from settings import *


# Класс персонажа
class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TEXTURES_SIZE, TEXTURES_SIZE))
        self.image = pygame.image.load("data/Jacob2.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

# Метод - передвижение
    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy
        if self.collide_with_portal(dx, dy):
            self.x += dx
            self.y += dy

# Метод - столкновение с коробками
    def collide_with_boxes(self, dx=0, dy=0):
        for box in self.game.box:
            if box.x == self.x + dx and box.y == self.y + dy:
                return True
        return False

# Метод - столкновение со стенами
    def collide_with_walls(self, dx=0, dy=0):
        for box in self.game.wall:
            if box.x == self.x + dx and box.y == self.y + dy:
                return True
        return False

# Метод - столкновение с водой
    def collide_with_aqua(self, dx=0, dy=0):
        for box in self.game.aqua:
            if box.x == self.x + dx and box.y == self.y + dy:
                return True
        return False

# Метод - столкновение с порталом
    def collide_with_portal(self, dx=0, dy=0):
        for box in self.game.portal:
            if box.x == self.x + dx and box.y == self.y + dy:
                print('la la la')
                return True
        return False

# Метод - столкновение с пометкой
    def collide_with_mark(self, dx=0, dy=0):
        for box in self.game.mark:
            if box.x == self.x + dx and box.y == self.y + dy:
                print('la la la')
                return True
        return False


    def update(self):
        self.rect.x = self.x * TEXTURES_SIZE
        self.rect.y = self.y * TEXTURES_SIZE
