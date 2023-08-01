import pygame as pg

pg.init()

WIDTH = 800
HEIGHT = 600

screen = pg.display.set_mode((WIDTH, HEIGHT))

loptica_x = 0
loptica_y = 0
move = 5

vrsta_pomeraja = 0


def draw():
    global loptica_x, loptica_y, move, vrsta_pomeraja
    screen.fill((0, 0, 0))
    pg.draw.circle(screen, (255, 255, 255), (loptica_x, loptica_y), 20)
    if vrsta_pomeraja == 0:
        loptica_x += move
        if loptica_x > WIDTH:
            vrsta_pomeraja = (vrsta_pomeraja + 1) % 4
    elif vrsta_pomeraja == 1:
        loptica_y += move
        if loptica_y > HEIGHT:
            vrsta_pomeraja = (vrsta_pomeraja + 1) % 4
    elif vrsta_pomeraja == 2:
        loptica_x -= move
        if loptica_x < 0:
            vrsta_pomeraja = (vrsta_pomeraja + 1) % 4
    elif vrsta_pomeraja == 3:
        loptica_y -= move
        if loptica_y < 0:
            vrsta_pomeraja = (vrsta_pomeraja + 1) % 4
    pg.display.update()


for i in range(9000000):
    draw()
    pg.time.delay(5)
