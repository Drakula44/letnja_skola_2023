## gravity.py

```python
import pygame as pg

pg.init()
screen = pg.display.set_mode((640, 480))

rectangle = {
    "x": 200,
    "y": 200,
    "width": 100,
    "height": 200,
    "vx": 0,
    "vy": 0,
    "ax": 0,
    "ay": 0.1,
    "max_vx": 5,
    "max_vy": 5,
}


def move_rect(rectangle):
    keys = pg.key.get_pressed()
    # move left and right
    if keys[pg.K_LEFT]:
        rectangle["ax"] = -0.1
    elif keys[pg.K_RIGHT]:
        rectangle["ax"] = 0.1
    else:
        rectangle["ax"] = 0
    # jump
    if keys[pg.K_UP] and rect["y"] == 480 - rect["height"]:
        rectangle["ay"] = 0.1
        rectangle["vy"] = -5


G = 0.1


def simulate_rect(rect):
    # # simulate acceleration
    # if rect["vx"] > 0:
    #     rect["ax"] -= G*0.5
    # elif rect["vx"] < 0:
    #     rect["ax"] += G*0.5

    # simulate velocity
    rect["x"] += rect["vx"]
    rect["y"] += rect["vy"]
    rect["vx"] += rect["ax"]
    rect["vy"] += rect["ay"]
    # check collision with ground
    if rect["y"] > 480 - rect["height"]:
        rect["y"] = 480 - rect["height"]
        rect["vy"] = 0
        rect["ay"] = 0

    # check collision with right wall
    if rect["x"] > 640 - rect["width"]:
        rect["x"] = 640 - rect["width"]
        rect["vx"] = 0
        rect["ax"] = 0

    # check collision with left wall
    if rect["x"] < 0:
        rect["x"] = 0
        rect["vx"] = 0
        rect["ax"] = 0

    # check max velocity
    if rect["vy"] > rect["max_vy"]:
        rect["vy"] = rect["max_vy"]
    if rect["vx"] > rect["max_vx"]:
        rect["vx"] = rect["max_vx"]


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill((0, 0, 0))
    move_rect(rectangle, pg.key.get_pressed())
    simulate_rect(rectangle)
    pg.draw.rect(screen, (255, 255, 255), (
        rectangle["x"], rectangle["y"], rectangle["width"], rectangle["height"]
    ))
    pg.display.flip()
    pg.time.delay(10)

```