## sombrero.py

```python
import pygame as pg

WIDTH = 1000
HEIGHT = 900
WHITE = (255,255,255)

RECTW = 150
RECTH = 250

SW = 40
SH = 40

GROUNDH = 150
SUNPOS = (100, 100)
SUNR = 80
GROUND =((0, HEIGHT-GROUNDH), (WIDTH, GROUNDH)) 

RED = (255, 0, 0)
GREEN = (0, 255, 0)

rect = [[WIDTH/2-RECTW/2, HEIGHT-GROUNDH-RECTH], (RECTW, RECTH)]

pg.init()
pg.display.set_caption("Petlja letnja skola")

screen = pg.display.set_mode((WIDTH, HEIGHT))

def draw(screen, rect, sombrero):
    screen.fill(WHITE)
    pg.draw.rect(screen, RED, rect)
    pg.draw.rect(screen, GREEN, GROUND)
    pg.draw.circle(screen, "Yellow", SUNPOS, SUNR)
    pg.draw.polygon(screen, "Orange", sombrero)
    pg.display.update()   # pg.display.flip()


while True:
    rect[0][0] -= 1 
    #               X                       Y
    sombrero = [(rect[0][0]-SW,         rect[0][1]), # A 
                (rect[0][0]-SW,         rect[0][1]-SH), # B
                (rect[0][0],            rect[0][1]-SH), # C
                (rect[0][0],            rect[0][1]-2*SH), # D
                (rect[0][0]+RECTW,      rect[0][1]-2*SH), # E
                (rect[0][0]+RECTW,      rect[0][1]-SH), # F
                (rect[0][0]+RECTW+SW,   rect[0][1]-SH), # G
                (rect[0][0]+RECTW+SW,   rect[0][1])] # H

    draw(screen, rect, sombrero)
    pg.time.delay(10)

```