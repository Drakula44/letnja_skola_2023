import pygame as pg
import time

pg.init()
screen = pg.display.set_mode((640, 480))

character = {
    "x": 320,
    "y": 240,
    "max_speed_x": 10,
    "max_speed_y": 10,
}

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        character["x"] -= 1
    if keys[pg.K_RIGHT]:
        character["x"] += 1
    if keys[pg.K_UP]:
        character["y"] -= 1
    if keys[pg.K_DOWN]:
        character["y"] += 1
    screen.fill((0, 0, 0))
    pg.draw.circle(screen, (255, 0, 0), (character["x"], character["y"]), 50)
    pg.display.flip()
    time.sleep(0.01)
