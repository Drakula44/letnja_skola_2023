import pygame as pg

pg.init()

WIDTH = 800
HEIGHT = 600

screen = pg.display.set_mode((WIDTH, HEIGHT))

loptica_x = WIDTH // 2
loptica_y = HEIGHT // 2

loptica_r = 10


def draw(iteracija):
    global loptica_x, loptica_y, loptica_r
    screen.fill((0, 0, 0))
    pg.draw.circle(screen, (255, 255, 255), (loptica_x, loptica_y),
                   (iteracija % 100))
    pg.display.update()


for i in range(1000):
    draw(i)
    pg.time.delay(10)
