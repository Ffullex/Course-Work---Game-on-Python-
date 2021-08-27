import sys
from idlelib import window
from os import path
import pygame.sprite

from Aqua import *
from Mark import Mark
from Player import *
from Box import *
from Camera import *
from Portal import *


# Класс непосредственно игрового процесса
from Wall import Wall

# Меню
# item_list = [
#     (120, 140, 'Play', (250, 250, 30), (250, 30, 250), 0),
#     (120, 140, u'Exit', (250, 250, 30), (250, 30, 250), 1),
# ]


class Game:
    def __init__(self):
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        pygame.key.set_repeat(500, 100)
        self.clock = pygame.time.Clock()
        self.set_data()
        pygame.mixer.init()
        pygame.mixer.music.load('./music/BloodMoonWaltz.mp3')
        pygame.mixer.music.play(-1)

# Метод - получение карты
    def set_data(self):
        pygame_directory = path.dirname(__file__)
        self.map = Map(path.join(pygame_directory, 'map/map.txt'))

# Метод - рисования карты
    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.player = pygame.sprite.Group()
        self.box = pygame.sprite.Group()
        self.portal = pygame.sprite.Group()
        self.wall = pygame.sprite.Group()
        self.mark = pygame.sprite.Group()
        self.aqua = pygame.sprite.Group()
        for row, cells in enumerate(self.map.data):
            for col, cell in enumerate(cells):
                if cell == '1':
                    Box(self, col, row)
                if cell == '2':
                    Aqua(self, col, row)
                if cell == '$':
                    self.player = Player(self, col, row)
                if cell == '3':
                    Portal(self, col, row)
                if cell == '4':
                    Wall(self, col, row)
                if cell == '5':
                    Mark(self, col, row)

        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        gameplay = True
        while gameplay:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

# Метод - выход из игры
    def quit(self):
        pygame.quit()
        sys.exit()

# Метод - обновление спрайтов
    def update(self):
        self.all_sprites.update()
        self.camera.update(self.player)

# Метод - создание подземелья
    def create_dungeon(self):
        for x in range(0, SCREEN_WIDTH, TEXTURES_SIZE):
            pygame.draw.line(self.screen, SAND_COLOR, (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, TEXTURES_SIZE):
            pygame.draw.line(self.screen, SAND_COLOR, (0, y), (SCREEN_WIDTH, y))

# Метод - отрисовка
    def draw(self):
        self.screen.fill(SAND_COLOR)
        self.create_dungeon()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pygame.display.flip()

# Метод - события
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                if event.key == pygame.K_LEFT:
                    self.player.move(dx=-1)
                if event.key == pygame.K_RIGHT:
                    self.player.move(dx=1)
                if event.key == pygame.K_UP:
                    self.player.move(dy=-1)
                if event.key == pygame.K_DOWN:
                    self.player.move(dy=1)

#
# class Menu:
#     def __init__(self, items=[120, 140, 'item', (250, 250, 30), (250, 30, 250), 0]):
#         self.items = items
#
#     def menu(self):
#         done = True
#         item = 0
#         while done:
#             screen.fill((0, 100, 200))
#
#             cursor = pygame.mouse.get_pos()
#             for i in self.items:
#                 if i[0] < cursor[0] < i[0]+55 and cursor[1]>i[1] and cursor[1]<i[1]+55:
#                     item=i[5]
#                 self.render(screen, item)
#
#             for e in pygame.event.get():
#                 if e.type == pygame.QUIT:
#                     sys.exit()
#                 if e.type == pygame.KEYDOWN:
#                     if e.key == pygame.K_ESCAPE:
#                         sys.exit()
#                     if e.key == pygame.K_UP:
#                         if item > 0:
#                             item -= 1
#                     if e.key == pygame.K_DOWN:
#                         if item < 0:
#                             item += 1
#                 if e.type == pygame.MOUSEBUTTONDOWN:
#                     if item == 0:
#                         done = False
#                     elif item == 1:
#                         sys.exit()
#             window.blit(screen, (0, 0))
#             pygame.display.flip()
#


# Запуск игрового процесса
# game = Menu(item_list)
# game.Menu
g = Game()
while True:
    g.new()
    g.run()
