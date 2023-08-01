import pygame as pg

screen = pg.display.set_mode((800, 800))
RADIUS = 20

x = 800/2
y = 800-RADIUS
speed = -10

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                speed -= 3

    pressed = pg.key.get_pressed()
    
    if pressed[pg.K_a]:
        x -= 3
    elif pressed[pg.K_d]:
        x += 3

    if y > 800-RADIUS:
        speed *= -0.94

    screen.fill('white')
    pg.draw.circle(screen, "red", (x,y), RADIUS)

    y += speed
    speed += 0.05 

    pg.event.pump()
    pg.display.update()
    pg.time.delay(10)