## infinite_event_loop.py

```python
import pygame as pg
import time

pg.init()
screen = pg.display.set_mode((640, 480))

running = True
while running:
    screen.fill((0, 0, 0))
    pg.draw.circle(screen, (255, 0, 0), (320, 240), 50)
    pg.display.flip()
    time.sleep(0.01)

```