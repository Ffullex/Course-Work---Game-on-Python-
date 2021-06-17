import sys
from os import path

from Aqua import Aqua
from Player import *
from Box import *
from Camera import *
from Portal import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(500, 100)
        self.set_data()

    def set_data(self):
        pg_directory = path.dirname(__file__)
        self.map = Map(path.join(pg_directory, 'map.txt'))

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.box = pygame.sprite.Group()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Box(self, col, row)
                if tile == '2':
                    Aqua(self, col, row)
                if tile == '$':
                    self.player = Player(self, col, row)
                if tile == 'E':
                    Portal(self, col, row)
        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        self.all_sprites.update()
        self.camera.update(self.player)

    def create_dungeon(self):
        for x in range(0, SCREEN_WIDTH, TEXTURES_SIZE):
            pygame.draw.line(self.screen, SAND_COLOR, (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, TEXTURES_SIZE):
            pygame.draw.line(self.screen, SAND_COLOR, (0, y), (SCREEN_WIDTH, y))

    def draw(self):
        self.screen.fill(SAND_COLOR)
        self.create_dungeon()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pygame.display.flip()

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


g = Game()
while True:
    g.new()
    g.run()
