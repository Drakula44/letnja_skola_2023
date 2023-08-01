import pygame as pg

pg.init()
screen = pg.display.set_mode((640, 480))

running = True

screen.fill((0, 0, 0))
pg.draw.circle(screen, (255, 0, 0), (320, 240), 50)
pg.display.flip()
# pg.time.delay(10)

while running:
    # ovo se uzima tako kako je
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
