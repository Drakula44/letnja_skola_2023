import pygame as pg

pg.init()
screen = pg.display.set_mode((640, 480))


def draw():
    screen.fill((255, 0, 0))
    pg.display.flip()


running = True
while running:
    # ovo se uzima tako kako je
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    draw()
