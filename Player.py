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

# Метод - передвижение
    def move(self, dx=0, dy=0):
        if self.collide_with_walls(dx, dy):
            self.x = self.x
            self.y = self.y
        elif self.collide_with_mark(dx, dy):
            self.x = self.x
            self.y = self.y
        elif self.collide_with_aqua(dx, dy):
            self.x = self.x
            self.y = self.y
        else:
            should_move = self.collide_with_boxes(dx, dy)
            if should_move:
                self.x += dx
                self.y += dy
            if self.collide_with_portal(dx, dy):
                pygame.quit()
                sys.exit()

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
        for box_2 in self.game.box:
            if box_2.x == self.x + dx and box_2.y == self.y + dy:
                print('box')
                new_box_x = box_2.x + dx
                new_box_y = box_2.y + dy
                for item_box in self.game.box:
                    if item_box.has_collide_box(new_box_x, new_box_y):
                        return False
                for item_wall in self.game.wall:
                    if item_wall.x == new_box_x and item_wall.y == new_box_y:
                        return False
                for item_aqua in self.game.aqua:
                    if item_aqua.x == new_box_x and item_aqua.y == new_box_y:
                        box_2.x = self.x
                        box_2.y = self.y
                        return True
                for item_mark in self.game.mark:
                    if item_mark.x == new_box_x and item_mark.y == new_box_y:
                        item_mark.kill()
                        box_2.kill()
                        return True
                box_2.x = new_box_x
                box_2.y = new_box_y
        return True

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
