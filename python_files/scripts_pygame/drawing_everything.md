## drawing_everything.py

```python
import pygame as pg
pg.init()
screen = pg.display.set_mode((640, 480))  # promljiva

screen.fill((0, 200, 0))  # novo

pg.display.flip()  # novo
pg.time.delay(10000)


# pg.draw.line(screen, (0, 0, 255), (0, 0), (640, 480), 5)
# pg.draw.circle(screen, (255, 0, 0), (320, 240), 50)
# pg.draw.rect(screen, (0, 255, 0), (100, 100, 200, 200))
# pg.draw.polygon(screen, (255, 255, 0), ((0, 0), (640, 0), (320, 240)))

```