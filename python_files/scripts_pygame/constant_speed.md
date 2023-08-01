## constant_speed.py

```python
import pygame as pg

pg.init()
screen = pg.display.set_mode((640, 480))

character = {
    "x": 320,
    "y": 240,
    "speed_x": 0,
    "speed_y": 0,
    "max_speed_x": 10,
    "max_speed_y": 10,
}

character["speed_x"] = int(input("Enter speed_x: "))
character["speed_y"] = int(input("Enter speed_y: "))

if character["speed_x"] > character["max_speed_x"]:
    character["speed_x"] = character["max_speed_x"]

if character["speed_y"] > character["max_speed_y"]:
    character["speed_y"] = character["max_speed_y"]


def bounce_on_edge(character):
    if character["x"] > 640:
        character["x"] = 640
        character["speed_x"] *= -1
    if character["x"] < 0:
        character["x"] = 0
        character["speed_x"] *= -1
    if character["y"] > 480:
        character["y"] = 480
        character["speed_y"] *= -1
    if character["y"] < 0:
        character["y"] = 0
        character["speed_y"] *= -1


def update():
    pass


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    update()
    character["x"] += character["speed_x"]
    character["y"] += character["speed_y"]
    bounce_on_edge(character)
    screen.fill((0, 0, 0))
    pg.draw.circle(screen, (255, 0, 0), (character["x"], character["y"]), 50)
    pg.display.flip()
    pg.time.delay(10)

```