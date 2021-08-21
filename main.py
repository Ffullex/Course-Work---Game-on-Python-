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


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(500, 100)
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
        self.box = pygame.sprite.Group()
        self.portal = pygame.sprite.Group()
        self.wall = pygame.sprite.Group()
        self.mark = pygame.sprite.Group()
        self.aqua = pygame.sprite.Group()
        for row, boxes in enumerate(self.map.data):
            for col, box in enumerate(boxes):
                if box == '1':
                    Box(self, col, row)
                if box == '2':
                    Aqua(self, col, row)
                if box == '$':
                    self.player = Player(self, col, row)
                if box == '3':
                    Portal(self, col, row)
                if box == '4':
                    Wall(self, col, row)
                if box == '5':
                    Mark(self, col, row)

        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        gameplay = True
        while gameplay:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()
            if not Player.collide_with_portal:
                print("no no no")
                g.quit()

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


# Запуск игрового процесса
g = Game()
while True:
    g.new()
    g.run()
