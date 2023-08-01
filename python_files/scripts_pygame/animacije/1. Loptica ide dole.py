import pygame as pg

pg.init()

WIDTH = 800
HEIGHT = 600
MOVE = 5

screen = pg.display.set_mode((WIDTH, HEIGHT))

loptica_x = WIDTH // 2
loptica_y = 0


def draw():
    global loptica_y
    screen.fill((0, 0, 0))
    pg.draw.circle(screen, (255, 255, 255), (loptica_x, loptica_y), 10)
    loptica_y += MOVE
    pg.display.update()


for i in range(HEIGHT // MOVE + 1):
    draw()
    pg.time.delay(50)
