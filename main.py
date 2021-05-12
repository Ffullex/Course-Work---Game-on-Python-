import pygame

pygame.init()
win = pygame.display.set_mode((520, 520))
pygame.display.set_caption("Jakob`s Adventures in Dungeon")

x = 10
y = 10
width = 50
height = 50
speed = 50

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 10:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 500 - width:
        x += speed
    if keys[pygame.K_UP] and y > 10:
        y -= speed
    if keys[pygame.K_DOWN] and y < 500 - height:
        y += speed

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 0, 255), (x, y, width, height))
    pygame.display.update()
pygame.quit()
