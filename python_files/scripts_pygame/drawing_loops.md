## drawing_loops.py

```python
import pygame as pg
import time

pg.init()
screen = pg.display.set_mode((640, 480))

# for i in range(0, 640, 10):
#     pg.draw.line(screen, (0, 0, 255), (0, i), (i, 480), 5)
#     pg.display.flip()
#     time.sleep(0.1)


# for i in range(0, 640, 10):
#     screen.fill((0, 0, 0))
#     pg.draw.rect(screen, (0, 255, 0), (i, i, 640 - 2 * i, 480 - 2 * i))
#     pg.display.flip()
#     time.sleep(0.1)

for i in range(0, 640, 10):
    for j in range(0, 480, 10):
        screen.fill((0, 0, 0))
        pg.draw.rect(screen, (0, 255, 0), (i, j, 100, 100))

        pg.draw.rect(screen, (0, 255, 255), (i+20, j+20, 100, 100))
        pg.display.flip()
        time.sleep(0.01)

pg.display.flip()
time.sleep(10000)

```