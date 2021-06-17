import pygame
from settings import *


class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line)
        self.boxwidth = len(self.data[0])
        self.boxheight = len(self.data)
        self.width = self.boxwidth + TEXTURES_SIZE
        self.height = self.boxheight + TEXTURES_SIZE


class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(SCREEN_WIDTH / 2)
        y = -target.rect.y + int(SCREEN_HEIGHT / 2)
        self.camera = pygame.Rect(x, y, self.width, self.height)
