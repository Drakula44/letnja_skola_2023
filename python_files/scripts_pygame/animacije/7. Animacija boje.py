import pygame as pg
import random

pg.init()

WIDTH = 800
HEIGHT = 600

LOPTICA_X = WIDTH // 2
LOPTICA_Y = HEIGHT // 2

screen = pg.display.set_mode((WIDTH, HEIGHT))


def draw(iteracija):
    screen.fill((0, 0, 0))
    boja = ((iteracija*2) % 255, (iteracija - 100) % 255, (iteracija*10 - 1000) % 255)
    pg.draw.circle(screen, boja, (LOPTICA_X, LOPTICA_Y), 50)
    pg.display.update()


for i in range(1000):
    draw(i)
    pg.time.delay(10)
