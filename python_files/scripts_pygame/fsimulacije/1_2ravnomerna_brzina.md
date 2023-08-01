## 1_2ravnomerna_brzina.py

```python
# Telo sa konstantnom brzinom

import pygame
import time
pygame.init()

WIDTH = 1000
HEIGHT = 600

RECT_WIDTH = 50
RECT_HEIGHT = 30

START_X = 100 # definicija početne pozicije (menja se)
START_Y = 285 # definicija početne pozicije na y koordinati (ne menja se)
SPEED = 0.2 # definicija brzine

x = START_X 
y = START_Y

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Linearno kretanje")
clock = pygame.time.Clock()

def draw_rect(x, y):
    pygame.draw.rect(window, (255, 0, 0), (x, y, RECT_WIDTH, RECT_HEIGHT))

def update_rect(dt: int):
    global x
    x += SPEED * dt

while True:
    window.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    dt = clock.tick(100) # ~100 puta u sekundi računa poziciju kvadrata
    print(dt)
    update_rect(dt)
    draw_rect(x, y)

    pygame.display.update()
```