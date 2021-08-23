import pygame
from settings import *


# Класс коробок. Их персонаж должен двигать
class Box(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.box
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TEXTURES_SIZE, TEXTURES_SIZE))
        self.image = pygame.image.load("data/Box.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TEXTURES_SIZE
        self.rect.y = y * TEXTURES_SIZE

    def move_box(self, dx, dy):
        if self.collide_with_walls(dx, dy):
            self.x = self.x
            self.y = self.y
        elif self.collide_with_player(dx, dy):
            self.x += dx
            self.y += dy
        elif self.collide_with_mark(dx, dy):
            print('mark')
        else:
            self.x += dx
            self.y += dy

# Метод - флаг-столкновение с водой
    def collide_with_player(self, dx=0, dy=0):
        for aqua in self.game.aqua:
            if aqua.x == self.x + dx and aqua.y == self.y + dy:
                print('aqua')
                return True
        return False

# Метод - флаг-столкновение с коробками
    def collide_with_boxes(self, dx=0, dy=0):
        for box in self.game.box:
            if box.x == self.x + dx and box.y == self.y + dy:
                print('box')
                return True
        return False

# Метод - флаг-столкновение со стенами
    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.wall:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                print('wall')
                return True
        return False

# Метод - флаг-столкновение с меткой
    def collide_with_mark(self, dx=0, dy=0):
        for mark in self.game.mark:
            if mark.x == self.x + dx and mark.y == self.y + dy:
                print('mark')
                return True
        return False
