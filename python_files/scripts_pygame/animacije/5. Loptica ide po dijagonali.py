import pygame as pg

pg.init()

WIDTH = 1200
HEIGHT = 800
SPEED = 3
MOVE_X = WIDTH/SPEED 
MOVE_Y = HEIGHT/SPEED

screen = pg.display.set_mode((WIDTH, HEIGHT))

loptica_x = 0
loptica_y = 0


def draw():
    global loptica_x, loptica_y
    screen.fill((0, 0, 0))
    pg.draw.circle(screen, (255, 255, 255), (loptica_x, loptica_y), 10)
    loptica_x += MOVE_X
    loptica_y += MOVE_Y
    pg.display.update()


for i in range(1000):
    draw()
    pg.time.delay(10)
