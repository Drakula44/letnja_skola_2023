import pygame as pg
import random

pg.init()

WIDTH = 800
HEIGHT = 600

screen = pg.display.set_mode((WIDTH, HEIGHT))

loptica_x = 0
loptica_y = 0

move_x = 6
move_y = 5

boja = (255, 255, 255)


def draw():
    global loptica_x, loptica_y, move_x, move_y, boja
    screen.fill((0, 0, 0))
    pg.draw.circle(screen, boja,
                   (loptica_x, loptica_y), 50)
    loptica_x += move_x
    loptica_y += move_y
    if loptica_x > WIDTH or loptica_x < 0:
        move_x *= -1
        boja = (random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255))
    if loptica_y > HEIGHT or loptica_y < 0:
        move_y *= -1
        boja = (random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255))
    pg.display.update()


for i in range(5000):
    draw()
    pg.time.delay(10)
