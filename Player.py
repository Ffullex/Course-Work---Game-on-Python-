import sys
from os import path
import pygame
import pygame.sprite

from Box import *
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
        # elif self.collide_with_mark(dx, dy):
        #     self.x += dx

# Метод - передвижение
    def move(self, dx=0, dy=0):
        if self.collide_with_walls(dx, dy):
            self.x = self.x
            self.y = self.y
        elif self.collide_with_aqua(dx, dy):
            self.x = self.x
            self.y = self.y
        #     self.y += dy
        elif self.collide_with_boxes(dx, dy) == 1:
            self.x += dx
            self.y += dy
        elif self.collide_with_boxes(dx, dy) == 2:
            pass
        elif self.collide_with_boxes(dx, dy) == 3:
            pass
        elif self.collide_with_boxes(dx, dy) == 4:
            pass
        elif self.collide_with_portal(dx, dy):
            pygame.quit()
        else:
            self.x += dx
            self.y += dy

# Метод - флаг-столкновение с водой
    def collide_with_aqua(self, dx=0, dy=0):
        for aqua in self.game.aqua:
            if aqua.x == self.x + dx and aqua.y == self.y + dy:
                print('aqua')
                return True
        return False

# Метод - флаг-столкновение со стенами
    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.wall:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                print('wall')
                return True
        return False

# Метод - флаг-столкновение с коробками
    def collide_with_boxes(self, dx=0, dy=0):
        for box in self.game.box:
            if box.x == self.x + dx and box.y == self.y + dy:
                print('box')
                box.x += dx
                box.y += dy
                for item in self.game.mark:
                    if item.x == box.x and item.y == box.y:
                        item.kill()
                        box.kill()
                        return 1
                for item in self.game.aqua:
                    if item.x == box.x and item.y == box.y:
                        box.x = self.x
                        box.y = self.y
                        return 2
                for item in self.game.wall:
                    if item.x == box.x and item.y == box.y:
                        self.x -= dx
                        self.y -= dy
                        box.x = item.x - dx
                        box.y = item.y - dy
                        return 3
                for item in self.game.box:
                    if item.x == box.x + dx and item.y == box.y + dy:
                        self.x -= dx
                        self.y -= dy
                        box.x = item.x - dx
                        box.y = item.y - dy
                        return 4
                return True
        return False

# Метод - флаг-столкновение с порталом
    def collide_with_portal(self, dx=0, dy=0):
        for portal in self.game.portal:
            if portal.x == self.x + dx and portal.y == self.y + dy:
                print('portal')
                return True
        return False

# Метод - флаг-столкновение с меткой
    def collide_with_mark(self, dx=0, dy=0):
        for mark in self.game.mark:
            if mark.x == self.x + dx and mark.y == self.y + dy:
                print('mark')
                return True
        return False

    def update(self):
        self.rect.x = self.x * TEXTURES_SIZE
        self.rect.y = self.y * TEXTURES_SIZE
