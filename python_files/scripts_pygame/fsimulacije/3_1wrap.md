## 3_1wrap.py

```python
# Telo sa konstantnom brzinom

import pygame
pygame.init()

WIDTH, HEIGHT = 1000, 600
RECT_WIDTH, RECT_HEIGHT = 50, 30

START_X = 100
START_Y = 285
START_SPEED = 0.1

x = START_X
y = START_Y
speed = START_SPEED

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ubrzanje")
clock = pygame.time.Clock()

def draw_rect(x, y):
    pygame.draw.rect(window, (255, 0, 0), (x, y, RECT_WIDTH, RECT_HEIGHT))

def update_rect(speed):
    global x
    x += speed
    if x > WIDTH: # <--- provera da li kvadrat izlazi iz ekrana 
        x = 0 # <--- ako da, onda ga vrati na početak

def update_environment(change):
    global speed
    speed += change

while True:
    window.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    
    update_rect(speed)
    update_environment(0.0005)
    draw_rect(x, y)
    clock.tick(300)
    pygame.display.update()
```