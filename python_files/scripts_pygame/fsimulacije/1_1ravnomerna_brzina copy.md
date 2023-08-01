## 1_1ravnomerna_brzina copy.py

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
SAMPLE_RATE = 0.01 # definicija vremenskog odabira (100 puta u sekundi)
SPEED = 100 # definicija brzine

t = SAMPLE_RATE
x = START_X 
y = START_Y

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Linearno kretanje")

def draw_rect(x, y):
    pygame.draw.rect(window, (255, 0, 0), (x, y, RECT_WIDTH, RECT_HEIGHT))

def update_rect():
    global x
    x += SPEED * t

while True:
    window.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    update_rect()
    draw_rect(x, y)

    #pygame.time.delay(t)
    time.sleep(t) # ~100 puta u sekundi računa poziciju kvadrata
    pygame.display.update()
```