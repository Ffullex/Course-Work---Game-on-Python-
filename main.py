import sys
from sys import path

import pygame as pg
from pygame.examples.textinput import BGCOLOR

import Player
from Sand import Sand
from settings import *


class Game():
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)

    # Метод загружает файлы
    def load_files(self):
        game_folder = path.dirname(__file__)
        self.world_dir = []
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                self.world_dir.append(line)

    # Метод загружает спрайты
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.tiles = pg.sprite.Group()
        for row, blocks in enumerate(self.world_dir):
            for col, block in enumerate(blocks):
                if block == '0':
                    Sand(self, col, row)
                if block == '1':
                    self.player = Player(self, col, row)
                if block == '2':
                    self.player = Player(self, col, row)

    # Метод поддерживает игровой цикл
    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    # Метод выходит из игрового цикла
    def quit(self):
        pg.quit()
        sys.exit()

    # Метод обновляет спрайты
    def update(self):
        self.all_sprites.update()

    # Метод создаёт поле
    def create_field(self):
        for x in range(0, SCREEN_WIDTH, TEXTURES_SIZE):
            pg.draw.line(self.screen, SAND_COLOR, (x, 0), (x, TEXTURES_SIZE))
        for y in range(0, SCREEN_HEIGHT, TEXTURES_SIZE):
            pg.draw.line(self.screen, SAND_COLOR, (0, y), (TEXTURES_SIZE, y))

    # Метод отрисовывет спрайты и переворачивает дисплей
    def draw(self):
        self.screen.fill(BGCOLOR)
        self.create_cell()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    # Метод обработки событий
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

g = Game()
while True:
    g.new()
    g.run()
#
# pg.init()
# win = pg.display.set_mode((520, 520))
# pg.display.set_caption("Jakob`s Adventures in Dungeon")
#
# x = 10
# y = 10
#
# run = True
# while run:
#     pg.time.delay(100)
#
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             run = False
#
#     keys = pg.key.get_pressed()
#     if keys[pg.K_LEFT] and x > 10:
#         x -= Player.Jakob.speed
#     if keys[pg.K_RIGHT] and x < 500 - Player.Jakob.width:
#         x += Player.Jakob.speed
#     if keys[pg.K_UP] and y > 10:
#         y -= Player.Jakob.speed
#     if keys[pg.K_DOWN] and y < 500 - Player.Jakob.height:
#         y += Player.Jakob.speed
#
#     win.fill((0, 0, 0))
#     pg.draw.rect(win, (0, 0, 255), (x, y, Player.Jakob.width, Player.Jakob.height))
#     pg.display.update()
# pg.quit()
