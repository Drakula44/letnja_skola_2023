## drawing_shapes.py

```python
import pygame as pg

pg.init()
screen = pg.display.set_mode((640, 480))

rectangle = {
    "x": 200,
    "y": 200,
    "width": 100,
    "height": 200,
}

circle = {
    "x": 300,
    "y": 300,
    "r": 50
}

line = [
    {"x": 100, "y": 100},
    {"x": 200, "y": 100},
]

point = {
    "x": 100,
    "y": 100,
}

polygon = [
    {"x": 100, "y": 100},
    {"x": 200, "y": 100},
    {"x": 200, "y": 300},
    {"x": 100, "y": 200}
]

def draw_rect(screen, rect):
    pg.draw.rect(screen, (255, 255, 255), (
        rect["x"], rect["y"], rect["width"], rect["height"]
    ))

def draw_circle(screen, circle):
    pg.draw.circle(screen, (255, 255, 255), (circle["x"], circle["y"]), circle["r"])

def draw_line(screen, line):
    pg.draw.line(screen, (255, 255, 255), (line[0]["x"], line[0]["y"]), (line[1]["x"], line[1]["y"]))

def draw_point(screen, point):
    pg.draw.circle(screen, (255, 255, 255), (point["x"], point["y"]), 5)

def draw_polygon(screen, point):
    point_list = []
    for p in point:
        point_list.append((p["x"], p["y"]))
    pg.draw.polygon(screen, (255, 255, 255), point_list)
```